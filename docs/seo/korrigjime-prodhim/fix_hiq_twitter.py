#!/usr/bin/env python3
"""Heqja e plotë e balizave Twitter Card (vendim i Isufit, 02/09/2026).

Konteksti. Auditi i 31/08 e nxori si mangësi mungesën e kartave Twitter mbi
726 faqe, dhe paketa përkatëse (`fix_twitter_cards.py`) i shtonte. Inventari i
02/09 e ktheu peshën e vërtetë të kësaj mangësie: **RUSHITI nuk ka llogari X**
dhe kanalet e vërteta të firmës — Facebook, WhatsApp, Instagram, LinkedIn —
lexojnë të gjitha Open Graph, jo `twitter:*`. Isufi vendosi t'i heqë të gjitha.

Çfarë hiqet. Çdo `<meta name="twitter:…">`: `card`, `title`, `description`,
`image`, `image:alt`, `site`, `creator`. Në gjendjen e 02/09 ekziston vetëm
`twitter:card` mbi 31 faqe, por skripti i mbulon të gjitha, që një rikthim i
paqëllimshëm i ndonjë gabariti të kapet në kalimin e ardhshëm.

Çfarë NUK preket. Asnjë `<meta property="og:…">`. Kjo është kushti i vetëm i
sigurisë: X-i, kur nuk gjen `twitter:*`, bie prapa mbi Open Graph — pra edhe
mbi X-in vetë asgjë nuk humbet. Skripti refuzon të shkruajë mbi një faqe që
nuk ka njëkohësisht `og:title` dhe `og:image`, e cila do të mbetej pa asnjë
paraqitje sociale.

    python3 fix_hiq_twitter.py /rruga/drejt/depos            # simulim
    python3 fix_hiq_twitter.py /rruga/drejt/depos --apply

Idempotent: kalimi i dytë prek 0 skedarë. Nuk prek asnjë fjalë të dukshme —
balizat `<meta>` jetojnë te `<head>`.
"""

from __future__ import annotations

import collections
import os
import re
import sys

# `name` ose `property`: disa gabarite e shkruajnë Twitter-in si `property`,
# ndonëse specifikimi i X-it kërkon `name`. Të dyja hiqen.
BALIZA = re.compile(
    r'<meta\s+[^>]*?(?:name|property)\s*=\s*["\']twitter:[^"\']*["\'][^>]*>\s*',
    re.I,
)
OG = re.compile(r'<meta\s+[^>]*?property\s*=\s*["\']og:(title|image)["\']', re.I)


def main() -> int:
    flamujt = {a for a in sys.argv[1:] if a.startswith("--")}
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    zbato = "--apply" in flamujt
    if len(argv) != 1:
        print(__doc__)
        return 2
    rrenja = argv[0]
    if not os.path.isdir(rrenja):
        print(f"✘ Nuk është dosje: {rrenja}")
        return 2

    numeruesi: collections.Counter[str] = collections.Counter()
    prekur: list[str] = []
    paralajmerime: list[str] = []
    balizat = 0

    for dp, dn, fn in os.walk(rrenja):
        dn[:] = [d for d in dn if d != ".git"]
        for f in sorted(fn):
            if not f.endswith(".html"):
                continue
            shtegu = os.path.join(dp, f)
            rel = os.path.relpath(shtegu, rrenja)
            burimi = open(shtegu, encoding="utf-8", errors="replace").read()
            if not BALIZA.search(burimi):
                continue

            # Kushti i sigurisë: pa Open Graph të plotë, heqja do ta linte
            # faqen pa asnjë paraqitje sociale — atëherë e lëmë të paprekur.
            og = {m.group(1).lower() for m in OG.finditer(burimi)}
            if not {"title", "image"} <= og:
                paralajmerime.append(
                    f"{rel}: pa og:title dhe og:image — faqe e lënë e paprekur"
                )
                continue

            i_ri, n = BALIZA.subn("", burimi)
            if i_ri == burimi:
                continue

            # Asnjë ndryshim jashtë `<head>`: kontroll i lirë por i vërtetë.
            if burimi.count("<body") != i_ri.count("<body"):
                paralajmerime.append(f"{rel}: prekje jashtë <head> — e anuluar")
                continue

            for m in re.finditer(
                r'(?:name|property)\s*=\s*["\'](twitter:[^"\']*)["\']', burimi, re.I
            ):
                numeruesi[m.group(1).lower()] += 1
            balizat += n
            prekur.append(rel)
            if zbato:
                open(shtegu, "w", encoding="utf-8").write(i_ri)

    print("ZBATIM" if zbato else "SIMULIM (asgjë e shkruar)")
    print(f"Skedarë të prekur: {len(prekur)}   baliza të hequra: {balizat}")
    if numeruesi:
        print()
        for e, n in numeruesi.most_common():
            print(f"  {n:6d}  {e}")
    if paralajmerime:
        print(f"\nKUJDES ({len(paralajmerime)}):")
        for p in paralajmerime[:20]:
            print("  ⚠", p)
        if len(paralajmerime) > 20:
            print(f"  … dhe {len(paralajmerime) - 20} të tjera")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
