#!/usr/bin/env python3
"""Vegël regresi: shëndeti i JSON-LD schema.org mbi një checkout të plotë.

Plotëson `verifiko_sameas.py` (i cili mbulon `@id`, `sameAs` dhe orarin).
Kjo vegël kontrollon pesë gjëra të tjera, të gjitha të konstatuara si të
prishura në auditin e 31/08/2026 (`docs/seo/audit-schema-org-2026-08-31.md`):

  1. çdo bllok `application/ld+json` mbetet JSON i vlefshëm;
  2. **FAQPage**: çdo pyetje e balisuar shfaqet fjalë për fjalë në tekstin e
     dukshëm të faqes, dhe çdo përgjigje po ashtu. Google e kërkon
     shprehimisht: përmbajtje që jeton vetëm në JSON-LD është shkelje;
  3. **asnjë `aggregateRating` dhe asnjë `review`** mbi nyjen e biznesit:
     notat e Google janë vlerësime palësh të treta, doktrina e shtëpisë i
     citon në tekst me datë, kurrë në të dhëna të strukturuara
     (`docs/seo/avis-google-releve-2026-08-22.md`);
  4. **entiteti i faqes**: URL-ja kanonike e faqes shfaqet të paktën në një
     nyje të grafit (WebPage/FAQPage/Service me `url`), që faqja të mos jetë
     anonime brenda grafit të vet;
  5. **imazhet e deklaruara**: çdo `image`/`logo`/`contentUrl` që tregon nga
     `rushiti-renovation.fr` i përgjigjet një skedari real në checkout.

Dalja 0 = konform. Për t'u ekzekutuar para çdo deploy-i.

    python3 verifiko_schema_org.py /rruga/drejt/rushiti-renovation
"""

from __future__ import annotations

import collections
import html
import json
import os
import re
import sys

BLLOKU = re.compile(
    r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.S | re.I,
)
KANONIKJA = re.compile(
    r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', re.I
)
IMAZH = re.compile(r"\.(png|jpe?g|webp|avif|svg)$", re.I)
TIPA_BIZNESI = {
    "LocalBusiness",
    "HousePainter",
    "HomeAndConstructionBusiness",
    "Organization",
}
HOST = "rushiti-renovation.fr/"


def nyjet(o):
    """Kalon rekursivisht çdo objekt JSON të grafit."""
    if isinstance(o, dict):
        yield o
        for v in o.values():
            yield from nyjet(v)
    elif isinstance(o, list):
        for v in o:
            yield from nyjet(v)


def tipat(nyje):
    t = nyje.get("@type")
    if t is None:
        return []
    return t if isinstance(t, list) else [t]


def normalizo(s: str) -> str:
    """Tekst i krahasueshëm: pa balisa, pa entitete, pa apostrofa tipografike."""
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    for a, b in (("’", "'"), (" ", " "), (" ", " ")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def teksti_i_dukshem(burimi: str) -> str:
    pa_kod = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", burimi, flags=re.S)
    return normalizo(pa_kod)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    rrenja = sys.argv[1]
    if not os.path.isdir(rrenja):
        print(f"✘ Nuk është dosje: {rrenja}")
        return 2

    faqe = 0
    gabime: list[str] = []
    kujdes: list[str] = []

    # Kontrolli i imazheve ka kuptim vetëm mbi checkout-in e prodhimit, i vetmi
    # që i mban skedarët. Mbi kopjen GitHub Pages (3 faqe, pa `assets/`) do të
    # jepte gabime false: aty kalohet.
    kontrollo_imazhet = os.path.isdir(os.path.join(rrenja, "assets"))

    for dp, dn, fn in os.walk(rrenja):
        dn[:] = [d for d in dn if d != ".git"]
        for f in sorted(fn):
            if not f.endswith(".html"):
                continue
            shtegu = os.path.join(dp, f)
            rel = os.path.relpath(shtegu, rrenja)
            burimi = open(shtegu, encoding="utf-8", errors="replace").read()
            blloqe = BLLOKU.findall(burimi)
            if not blloqe:
                continue
            faqe += 1

            grafi = []
            for i, b in enumerate(blloqe):
                try:
                    grafi += list(nyjet(json.loads(b)))
                except json.JSONDecodeError as e:
                    gabime.append(f"{rel}: blloku {i} nuk është JSON i vlefshëm ({e})")

            # 2. FAQPage e dukshme dhe identike
            dukshem = teksti_i_dukshem(burimi)
            for nyje in grafi:
                if nyje.get("@type") != "Question":
                    continue
                pyetja = normalizo(nyje.get("name"))
                pergjigja = normalizo((nyje.get("acceptedAnswer") or {}).get("text"))
                if pyetja and pyetja not in dukshem:
                    gabime.append(f"{rel}: pyetje e balisuar por e padukshme — « {pyetja[:70]} »")
                elif pergjigja and pergjigja not in dukshem:
                    gabime.append(
                        f"{rel}: përgjigja ndryshon nga teksti i faqes — « {pyetja[:60]} »"
                    )
                if not pergjigja:
                    gabime.append(f"{rel}: pyetje pa acceptedAnswer — « {pyetja[:60]} »")

            # 3. asnjë notë e vetëshpallur
            for nyje in grafi:
                if not set(tipat(nyje)) & TIPA_BIZNESI:
                    continue
                if nyje.get("aggregateRating"):
                    gabime.append(f"{rel}: aggregateRating mbi nyjen e biznesit (avis palësh të treta)")
                if nyje.get("review"):
                    gabime.append(f"{rel}: review mbi nyjen e biznesit (avis palësh të treta)")

            # 4. entiteti i faqes
            kanonike = KANONIKJA.search(burimi)
            if kanonike:
                url = kanonike.group(1).rstrip("/")
                gjetur = any(
                    str(n.get("url", "")).rstrip("/") == url or str(n.get("@id", "")).startswith(url + "#")
                    for n in grafi
                )
                if not gjetur:
                    kujdes.append(f"{rel}: asnjë nyje nuk e mban URL-në kanonike — faqe anonime në grafin e vet")

            # 5. imazhet e deklaruara ekzistojnë
            for nyje in grafi if kontrollo_imazhet else ():
                for celes in ("image", "logo", "contentUrl", "thumbnailUrl"):
                    v = nyje.get(celes)
                    if isinstance(v, dict):
                        v = v.get("url") or v.get("contentUrl")
                    if not isinstance(v, str) or HOST not in v or not IMAZH.search(v):
                        continue
                    shtegu_i_imazhit = os.path.join(rrenja, v.split(HOST)[-1])
                    if not os.path.exists(shtegu_i_imazhit):
                        gabime.append(f"{rel}: {celes} tregon një skedar që s'ekziston — {v}")

    print(f"Faqe me JSON-LD: {faqe}")
    if not kontrollo_imazhet:
        print("(pa dosjen `assets/`: kontrolli i imazheve u kapërcye — checkout jo i prodhimit)")
    if kujdes:
        print(f"\nKUJDES ({len(kujdes)}):")
        for k in kujdes[:30]:
            print("  ⚠", k)
        if len(kujdes) > 30:
            print(f"  … dhe {len(kujdes) - 30} të tjera")
    if gabime:
        # përmbledhje sipas kategorie, pastaj shembujt
        kategorite = collections.Counter()
        for g in gabime:
            for etiketa, shenja in (
                ("pyetje e balisuar por e padukshme", "pyetje e balisuar"),
                ("përgjigje që ndryshon nga teksti i faqes", "përgjigja ndryshon"),
                ("pyetje pa acceptedAnswer", "pa acceptedAnswer"),
                ("aggregateRating mbi biznesin", "aggregateRating mbi"),
                ("review mbi biznesin", "review mbi"),
                ("imazh i deklaruar që s'ekziston", "s'ekziston"),
                ("JSON i pavlefshëm", "nuk është JSON"),
            ):
                if shenja in g:
                    kategorite[etiketa] += 1
                    break
        print("\nPËRMBLEDHJE:")
        for etiketa, n in kategorite.most_common():
            print(f"  {n:6d}  {etiketa}")
        unike = sorted(set(gabime))
        print(f"\nGABIME ({len(gabime)}, {len(unike)} unike):")
        for g in unike[:50]:
            print("  ✘", g)
        if len(unike) > 50:
            print(f"  … dhe {len(unike) - 50} të tjera")
        return 1
    print("\n✔ Konform: FAQ e dukshme, pa notë të vetëshpallur, imazhe të pranishme.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
