#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vegël regresi: paraqitja sociale (Open Graph) mbi një checkout HTML.

Deri më 02/09/2026 kjo vegël quhej `verifiko_twitter_cards.py` dhe kërkonte
praninë e balizave `twitter:*`. Isufi vendosi t'i heqë të gjitha: RUSHITI nuk
ka llogari X, dhe kanalet e vërteta të firmës — Facebook, WhatsApp, Instagram,
LinkedIn — lexojnë Open Graph. Kontrolli u përmbys, pjesa tjetër mbeti e
paprekur, sepse ajo kurrë nuk kishte të bënte me X-in.

Kontrollon, faqe për faqe:

  1. **asnjë balizë `twitter:*` e rikthyer** — një gabarit i vjetër ose një
     degë e vjetër mund ta rifusë atë pa u vënë re; ky është roja i vendimit;
  2. **og:url == canonical** (një paraqitje që tregon një URL tjetër nga
     kanonikja shpërndan variantin e gabuar);
  3. **og:image ekziston** në checkout dhe **dimensionet e deklaruara
     përputhen me skedarin real** — një raport i gabuar e detyron crawler-in
     të rezervojë përmasa të gabuara;
  4. **cilësia e imazhit**: KUJDES nëse është portret ose nën 600x315
     (rekomandimi i platformave: 1200x630).

Dalja 0 = konform. Për t'u ekzekutuar para çdo deploy-i.

    python3 verifiko_apercus_sociaux.py /rruga/drejt/rushiti-renovation
"""
from __future__ import annotations

import collections
import os
import re
import struct
import sys

META = re.compile(r"<meta\b[^>]*>", re.I)
ATTR = re.compile(r'([a-zA-Z:_-]+)\s*=\s*"([^"]*)"')
CANONIKJA = re.compile(r'<link[^>]*rel="canonical"[^>]*href="([^"]+)"', re.I)
HOST = "rushiti-renovation.fr/"

# Faqe që nuk shpërndahen kurrë në rrjete sociale: pa kartë, pa gabim.
PERJASHTIME = {"404.html"}

# Heqja e 02/09 (`fix_hiq_twitter.py`): asnjë prej tyre nuk duhet të rikthehet.
TWITTER = re.compile(r'(?:name|property)\s*=\s*["\']twitter:[^"\']*["\']', re.I)


def balizat(burimi: str) -> dict[str, str]:
    t: dict[str, str] = {}
    for tag in META.findall(burimi):
        a = {m.group(1).lower(): m.group(2) for m in ATTR.finditer(tag)}
        celes = (a.get("property") or a.get("name") or "").lower()
        if celes:
            t[celes] = a.get("content", "")
    return t


def permasat(shtegu: str) -> tuple[int, int] | None:
    """Gjerësia dhe lartësia e një JPEG/PNG, pa varësi të jashtme."""
    try:
        d = open(shtegu, "rb").read()
    except OSError:
        return None
    if d[:2] == b"\xff\xd8":  # JPEG
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
    if d[:8] == b"\x89PNG\r\n\x1a\n":  # PNG
        w, h = struct.unpack(">II", d[16:24])
        return (w, h)
    return None


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    rrenja = sys.argv[1]
    if not os.path.isdir(rrenja):
        print(f"✘ Nuk është dosje: {rrenja}")
        return 2

    kontrollo_imazhet = os.path.isdir(os.path.join(rrenja, "assets"))
    faqe = 0
    gabime: list[str] = []
    kujdes: list[str] = []
    kategorite: collections.Counter[str] = collections.Counter()

    def gabim(kategoria: str, rresht: str) -> None:
        kategorite[kategoria] += 1
        gabime.append(rresht)

    for dp, dn, fn in os.walk(rrenja):
        dn[:] = [d for d in dn if d != ".git"]
        for f in sorted(fn):
            if not f.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(dp, f), rrenja)
            if rel in PERJASHTIME:
                continue
            t = balizat(open(os.path.join(dp, f), encoding="utf-8", errors="replace").read())
            if "og:title" not in t:
                kujdes.append(f"{rel}: asnjë balizë og: — faqja s'ka kartë fare")
                continue
            faqe += 1

            burimi = open(os.path.join(dp, f), encoding="utf-8", errors="replace").read()
            for m in TWITTER.finditer(burimi):
                gabim(
                    "balizë twitter e rikthyer",
                    f"{rel}: {m.group(0)} — e hequr më 02/09, nuk duhet të rikthehet",
                )

            kanonike = CANONIKJA.search(burimi)
            if kanonike and t.get("og:url", "").rstrip("/") != kanonike.group(1).rstrip("/"):
                gabim("og:url ≠ canonical", f"{rel}: og:url {t.get('og:url')} ≠ canonical {kanonike.group(1)}")

            imazhi = t.get("og:image")
            if not imazhi:
                gabim("og:image mungon", f"{rel}: og:image mungon — asnjë vignette")
            elif kontrollo_imazhet and HOST in imazhi:
                shtegu = os.path.join(rrenja, imazhi.split(HOST)[-1])
                if not os.path.exists(shtegu):
                    gabim("og:image 404", f"{rel}: og:image tregon një skedar që s'ekziston — {imazhi}")
                else:
                    p = permasat(shtegu)
                    if p:
                        w, h = p
                        gj, la = t.get("og:image:width"), t.get("og:image:height")
                        if gj and la and (gj != str(w) or la != str(h)):
                            gabim(
                                "përmasa të deklaruara gabim",
                                f"{rel}: og:image:width/height deklaron {gj}x{la}, skedari është {w}x{h}",
                            )
                        if h > w:
                            kujdes.append(f"{rel}: og:image portret ({w}x{h}) — pritet nga karta 1.91:1")
                        elif w < 600 or h < 315:
                            kujdes.append(f"{rel}: og:image {w}x{h} nën 600x315 — vignette e vogël")

    print(f"Faqe me baliza og: {faqe}")
    if not kontrollo_imazhet:
        print("(pa dosjen `assets/`: kontrolli i imazheve u kapërcye — checkout jo i prodhimit)")
    if kujdes:
        print(f"\nKUJDES ({len(kujdes)}):")
        for k in kujdes[:20]:
            print("  ⚠", k)
        if len(kujdes) > 20:
            print(f"  … dhe {len(kujdes) - 20} të tjera")
    if gabime:
        print("\nPËRMBLEDHJE:")
        for etiketa, n in kategorite.most_common():
            print(f"  {n:6d}  {etiketa}")
        print(f"\nGABIME ({len(gabime)}):")
        for g in gabime[:30]:
            print("  ✘", g)
        if len(gabime) > 30:
            print(f"  … dhe {len(gabime) - 30} të tjera")
        return 1
    print("\n✔ Konform: asnjë balizë twitter, URL koherente, imazhe të pranishme me përmasa të sakta.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
