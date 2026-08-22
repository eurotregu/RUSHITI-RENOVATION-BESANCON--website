#!/usr/bin/env python3
"""Vegël regresi: `sameAs` dhe orari i plotë në çdo nyje LocalBusiness me `@id`.

Kontrollon, mbi një checkout (prodhimi ose kopja GitHub Pages):
  1. çdo bllok `application/ld+json` mbetet JSON i vlefshëm;
  2. çdo nyje biznesi (LocalBusiness / HousePainter / Painter /
     HomeAndConstructionBusiness) me `@id` e mban `@id`-në kanonike
     `https://rushiti-renovation.fr/#business` — kurrë një të dytë;
  3. nyja që e përkufizon biznesin (ajo me adresë ose priceRange) mban
     `sameAs` me të 7 URL-të kanonike; nyjet referencë, që mbajnë të njëjtën
     `@id` me pak veti, nuk e përsërisin — JSON-LD i bashkon sipas `@id`;
  4. asnjë URL bosh apo e dyfishuar;
  5. nëse nyja deklaron `openingHoursSpecification`, orari përputhet me
     orarin e vetëm zyrtar (E hënë–E premte 07:00–20:30, E shtunë
     08:00–20:30, E diel 09:00–17:30) — mospërputhja mes sitit, Google Maps
     dhe PagesJaunes është pikërisht ajo që kërkohet të mos ndodhë më.

Një nyje biznesi pa asnjë `@id` raportohet si KUJDES, jo si gabim: nuk prish
gjë, por mbetet entitet anonim — duhet kthyer në referencë `@id`.

Dalja 0 = konform. Për t'u ekzekutuar para çdo deploy-i.

    python3 verifiko_sameas.py /rruga/drejt/rushiti-renovation
"""

from __future__ import annotations

import json
import os
import re
import sys

ID_KANONIK = "https://rushiti-renovation.fr/#business"

SAMEAS_KANONIK = [
    "https://rushiti.fr",
    "https://www.facebook.com/rushiti.renovation/",
    "https://www.instagram.com/rushiti.renovation/",
    "https://www.google.com/maps?cid=10915820577691168567",
    "https://www.pagesjaunes.fr/pros/61325501",
    "https://annuaire-entreprises.data.gouv.fr/entreprise/rushiti-905214631",
    "https://data.inpi.fr/entreprises/905214631",
]

TIPA_BIZNESI = {
    "LocalBusiness", "HousePainter", "Painter", "HomeAndConstructionBusiness"}

# Orari i vetëm zyrtar — i njëjti në sit, Google Maps dhe PagesJaunes.
ORARI_KANONIK = {
    ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"): ("07:00", "20:30"),
    ("Saturday",): ("08:00", "20:30"),
    ("Sunday",): ("09:00", "17:30"),
}

LD_BLLOK = re.compile(
    r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', re.S)


def nyjet_e_biznesit(o, jashte):
    if isinstance(o, dict):
        tipi = o.get("@type")
        tipat = tipi if isinstance(tipi, list) else [tipi]
        if any(t in TIPA_BIZNESI for t in tipat if t):
            jashte.append(o)
        for v in o.values():
            nyjet_e_biznesit(v, jashte)
    elif isinstance(o, list):
        for v in o:
            nyjet_e_biznesit(v, jashte)


def kontrollo_orarin(rel: str, nyje: dict) -> list[str]:
    """Orari, nëse deklarohet, duhet të jetë ai zyrtar — i plotë dhe i saktë."""
    specat = nyje.get("openingHoursSpecification")
    if not specat:
        return []
    if isinstance(specat, dict):
        specat = [specat]
    gjetur = {}
    for s in specat:
        if not isinstance(s, dict):
            return [f"{rel}: openingHoursSpecification me formë të papritur"]
        ditet = s.get("dayOfWeek")
        ditet = tuple(ditet) if isinstance(ditet, list) else (ditet,)
        gjetur[ditet] = (s.get("opens"), s.get("closes"))
    if gjetur == ORARI_KANONIK:
        return []
    gabime = []
    for ditet, pritur in ORARI_KANONIK.items():
        etiketa = "/".join(d[:3] for d in ditet)
        if ditet not in gjetur:
            gabime.append(f"{rel}: orari pa {etiketa}")
        elif gjetur[ditet] != pritur:
            o, c = gjetur[ditet]
            gabime.append(
                f"{rel}: orari {etiketa} {o}–{c} ≠ {pritur[0]}–{pritur[1]}")
    for ditet in gjetur:
        if ditet not in ORARI_KANONIK:
            gabime.append(f"{rel}: orar i panjohur për {ditet}")
    return gabime


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    rrenja = sys.argv[1]
    gabime: list[str] = []
    kujdes: list[str] = []
    faqe = 0

    for dp, dn, fn in os.walk(rrenja):
        dn[:] = [d for d in dn if d != ".git"]
        for f in sorted(fn):
            if not f.endswith(".html"):
                continue
            shteg = os.path.join(dp, f)
            rel = os.path.relpath(shteg, rrenja)
            with open(shteg, encoding="utf-8", errors="replace") as fh:
                html = fh.read()
            nyjet: list[dict] = []
            for bllok in LD_BLLOK.findall(html):
                try:
                    nyjet_e_biznesit(json.loads(bllok), nyjet)
                except json.JSONDecodeError as e:
                    gabime.append(f"{rel}: JSON-LD i pavlefshëm — {e}")
            if not nyjet:
                continue
            faqe += 1
            for nyje in nyjet:
                if "@id" not in nyje:
                    kujdes.append(
                        f"{rel}: nyje biznesi e ngulitur pa @id — "
                        "për ta kthyer në referencë {\"@id\": \".../#business\"}")
                    continue
                if nyje["@id"] != ID_KANONIK:
                    gabime.append(
                        f"{rel}: @id {nyje['@id']} ≠ {ID_KANONIK} — "
                        "entitet i dytë me të njëjtin emër")
                    continue
                gabime.extend(kontrollo_orarin(rel, nyje))
                same = nyje.get("sameAs")
                if same is None:
                    # Nyje referencë: mban `@id`-në kanonike dhe pak veti
                    # (telefon, areaServed). JSON-LD i bashkon nyjet sipas
                    # `@id`, prandaj `sameAs` nuk përsëritet — do të ishte
                    # dyfishim, jo plotësim. Vetëm nyja që e përkufizon
                    # biznesin (adresa ose priceRange) e mban listën.
                    if "address" in nyje or "priceRange" in nyje:
                        gabime.append(f"{rel}: nyja {nyje['@id']} pa sameAs")
                    continue
                if isinstance(same, str):
                    same = [same]
                mungojne = [u for u in SAMEAS_KANONIK if u not in same]
                if mungojne:
                    gabime.append(
                        f"{rel}: sameAs pa " + ", ".join(mungojne))
                if len(same) != len(set(same)):
                    gabime.append(f"{rel}: sameAs me URL të dyfishuara")
                if any(not u or not str(u).startswith("http") for u in same):
                    gabime.append(f"{rel}: sameAs me URL bosh ose jo-HTTP")

    print(f"Faqe me nyje biznesi: {faqe}")
    if kujdes:
        print(f"\nKUJDES ({len(kujdes)}):")
        for k in kujdes:
            print("  ⚠", k)
    if gabime:
        print(f"\nGABIME ({len(gabime)}):")
        for g in gabime[:50]:
            print("  ✘", g)
        if len(gabime) > 50:
            print(f"  … dhe {len(gabime) - 50} të tjera")
        return 1
    print("\n✔ Konform: sameAs i plotë në çdo nyje biznesi me @id.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
