#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Twitter Cards — depoja e prodhimit eurotregu/rushiti-renovation.

Konstati i 31/08/2026 (`docs/seo/audit-twitter-cards-2026-08-31.md`):
Open Graph-u është kudo (756/757 faqe), por `twitter:card` vetëm në 31 faqe —
dhe asnjë faqe e vetme e sitit nuk deklaron `twitter:title`,
`twitter:description`, `twitter:image` apo `twitter:image:alt`.

Çfarë korrigjon skripti, në mënyrë **idempotente**:

  A. shton `twitter:card = summary_large_image` në çdo faqe që ka `og:title`
     dhe s'e ka ende;
  B. shton `twitter:title`, `twitter:description`, `twitter:image` duke i
     **derivuar nga `og:*` e vetë faqes** — asnjë tekst i shpikur;
  C. shton `twitter:image:alt` (X-i nuk e lexon `og:image:alt`). Teksti merret
     nga `og:image:alt` i vetë faqes; nëse ajo s'e ka, merret alt-i që siti
     **tashmë deklaron live për të njëjtin skedar imazhi** në një faqe tjetër.
     Kur i njëjti tekst përdoret për disa imazhe të ndryshme, ai është një
     alt gjenerik i kopjuar: preferohet alt-i i veçantë i atij imazhi. Asnjë
     tekst nuk shpiket: pa burim në sit, baliza nuk shtohet;
  D. korrigjon `og:image:width` / `og:image:height` kur ndryshojnë nga përmasat
     reale të skedarit — 18 faqe deklaronin përmasa të gabuara, disa duke
     shpallur peizazh për një foto portret.

Çfarë NUK bën, me vetëdije:

  - asnjë `twitter:site` / `twitter:creator`: RUSHITI s'ka llogari X të
    deklaruar në `sameAs`; një identifikues i shpikur çon kartën te dikush
    tjetër;
  - asnjë `og:image` i ri për tri faqet që s'kanë fare (`blog.html`,
    `contact.html`, `mentions-legales.html`): zgjedhja e vizualit i takon
    Isufit;
  - asnjë ndryshim i `og:title` / `og:description` ekzistuese;
  - asnjë prekje e `404.html`.

Usage :  python3 fix_twitter_cards.py /rruga/drejt/checkout [--apply] [--vetem-permasat]
         (pa --apply: simulim, asgjë nuk shkruhet)

Pas ekzekutimit: `python3 verifiko_twitter_cards.py /rruga/drejt/checkout`
"""

from __future__ import annotations

import collections
import os
import re
import struct
import sys

META = re.compile(r"<meta\b[^>]*>", re.I)
ATTR = re.compile(r'([a-zA-Z:_-]+)\s*=\s*"([^"]*)"')
HOST = "rushiti-renovation.fr/"
PERJASHTIME = {"404.html"}


def balizat(burimi: str) -> dict[str, str]:
    t: dict[str, str] = {}
    for tag in META.findall(burimi):
        a = {m.group(1).lower(): m.group(2) for m in ATTR.finditer(tag)}
        celes = (a.get("property") or a.get("name") or "").lower()
        if celes:
            t[celes] = a.get("content", "")
    return t


def permasat(shtegu: str) -> tuple[int, int] | None:
    try:
        d = open(shtegu, "rb").read()
    except OSError:
        return None
    if d[:2] == b"\xff\xd8":
        i = 2
        while i < len(d) - 9:
            if d[i] != 0xFF:
                i += 1
                continue
            m = d[i + 1]
            if m in (0xC0, 0xC1, 0xC2, 0xC3):
                h, w = struct.unpack(">HH", d[i + 5 : i + 9])
                return (w, h)
            if m in (0xD8, 0xD9) or 0xD0 <= m <= 0xD7:
                i += 2
                continue
            i += 2 + struct.unpack(">H", d[i + 2 : i + 4])[0]
        return None
    if d[:8] == b"\x89PNG\r\n\x1a\n":
        w, h = struct.unpack(">II", d[16:24])
        return (w, h)
    return None


def harta_e_alteve(rrenja: str) -> dict[str, str]:
    """imazh → alt, ndërtuar nga ajo që siti deklaron tashmë live.

    Kur i njëjti tekst shfaqet për disa imazhe të ndryshme, është një alt
    gjenerik i kopjuar: preferohet kandidati i veçantë i atij imazhi.
    """
    kandidate: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    imazhet_e_altit: dict[str, set[str]] = collections.defaultdict(set)
    for dp, dn, fn in os.walk(rrenja):
        dn[:] = [d for d in dn if d != ".git"]
        for f in fn:
            if not f.endswith(".html"):
                continue
            t = balizat(open(os.path.join(dp, f), encoding="utf-8", errors="replace").read())
            im, alt = t.get("og:image"), t.get("og:image:alt")
            if im and alt:
                kandidate[im][alt] += 1
                imazhet_e_altit[alt].add(im)
    harta: dict[str, str] = {}
    for im, c in kandidate.items():
        veçantë = [(n, a) for a, n in c.items() if len(imazhet_e_altit[a]) == 1]
        harta[im] = max(veçantë)[1] if veçantë else c.most_common(1)[0][0]
    return harta


def rregullo(
    burimi: str, rrenja: str, alte: dict[str, str], vetem_permasat: bool = False
) -> tuple[str, list[str]]:
    """Kthen burimin e korrigjuar dhe listën e ndryshimeve."""
    t = balizat(burimi)
    ndryshime: list[str] = []
    if "og:title" not in t:
        return burimi, ndryshime

    # D. përmasat e deklaruara
    imazhi = t.get("og:image")
    if imazhi and HOST in imazhi and t.get("og:image:width") and t.get("og:image:height"):
        p = permasat(os.path.join(rrenja, imazhi.split(HOST)[-1]))
        if p and (t["og:image:width"] != str(p[0]) or t["og:image:height"] != str(p[1])):
            burimi = re.sub(
                r'(<meta[^>]*property="og:image:width"[^>]*content=")[^"]*(")',
                lambda m: m.group(1) + str(p[0]) + m.group(2),
                burimi,
                count=1,
            )
            burimi = re.sub(
                r'(<meta[^>]*property="og:image:height"[^>]*content=")[^"]*(")',
                lambda m: m.group(1) + str(p[1]) + m.group(2),
                burimi,
                count=1,
            )
            ndryshime.append(
                f"përmasa {t['og:image:width']}x{t['og:image:height']} → {p[0]}x{p[1]}"
            )

    # A–C. balizat twitter që mungojnë, të derivuara nga og:*
    # Në modalitetin `--vetem-permasat` ky bllok kapërcehet: arbitrazhi i Isufit
    # (02/09) e kufizoi korrigjimin te përmasat, sepse RUSHITI nuk është në X
    # dhe Open Graph-u — i lexuar nga Facebook, Instagram, WhatsApp, LinkedIn —
    # është tashmë i pranishëm në 756/757 faqe.
    if vetem_permasat:
        return burimi, ndryshime
    burimi_twitter = {
        "twitter:card": "summary_large_image",
        "twitter:title": t.get("og:title"),
        "twitter:description": t.get("og:description"),
        "twitter:image": t.get("og:image"),
        "twitter:image:alt": t.get("og:image:alt") or alte.get(t.get("og:image", "")),
    }
    reja = [
        f'<meta name="{k}" content="{v}">'
        for k, v in burimi_twitter.items()
        if k not in t and v
    ]
    if reja:
        # e ngjisim pas balizës së fundit og: së faqes, aty ku pret redaktori
        fundi = None
        for m in META.finditer(burimi):
            a = {x.group(1).lower(): x.group(2) for x in ATTR.finditer(m.group(0))}
            if (a.get("property") or "").lower().startswith("og:"):
                fundi = m
        if fundi is not None:
            burimi = burimi[: fundi.end()] + "".join(reja) + burimi[fundi.end() :]
            ndryshime.append(f"+{len(reja)} baliza twitter ({', '.join(k.split(':',1)[1] for k in burimi_twitter if k not in t and burimi_twitter[k])})")

    return burimi, ndryshime


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    rrenja = args[0]
    apliko = "--apply" in sys.argv
    vetem_permasat = "--vetem-permasat" in sys.argv
    if not os.path.isdir(rrenja):
        print(f"✘ Nuk është dosje: {rrenja}")
        return 2

    alte = harta_e_alteve(rrenja)
    prekura = 0
    pa_imazh: list[str] = []
    for dp, dn, fn in os.walk(rrenja):
        dn[:] = [d for d in dn if d != ".git"]
        for f in sorted(fn):
            if not f.endswith(".html"):
                continue
            shtegu = os.path.join(dp, f)
            rel = os.path.relpath(shtegu, rrenja)
            if rel in PERJASHTIME:
                continue
            burimi = open(shtegu, encoding="utf-8", errors="replace").read()
            t = balizat(burimi)
            if "og:title" in t and "og:image" not in t:
                pa_imazh.append(rel)
            i_ri, ndryshime = rregullo(burimi, rrenja, alte, vetem_permasat)
            if not ndryshime:
                continue
            prekura += 1
            if prekura <= 10:
                print(f"  {rel}: {' · '.join(ndryshime)}")
            if apliko:
                open(shtegu, "w", encoding="utf-8").write(i_ri)

    if prekura > 10:
        print(f"  … dhe {prekura - 10} faqe të tjera")
    print(f"\nFaqe të prekura: {prekura}")
    if pa_imazh:
        print(f"\nPa og:image, për Isufin (zgjedhja e vizualit s'automatizohet): {pa_imazh}")
    if not apliko:
        print("\nSimulim — asgjë nuk u shkrua. Rilëshoni me --apply për të shkruar.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
