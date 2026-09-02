#!/usr/bin/env python3
"""Paketa 7 — korrigjimet e Schema.org që NUK kërkojnë arbitrazh.

Zbaton mbi një checkout të prodhimit shtatë hapat e auditit të 31/08/2026
(`docs/seo/audit-schema-org-2026-08-31.md`) për të cilët nuk pritet asnjë
vendim nga Isufi. Çdo hap ndryshon **vetëm** JSON-LD-në, me ndërhyrje tekstuale
të synuara: formatimi ekzistues i bllokut ruhet, asnjë rirenditje çelësash.

  A. `aggregateRating` / `review` mbi nyjen e biznesit **hiqet vetëm nga faqet
     që s'e shfaqin notën** (P1-2). Faqja që e shfaq notën — `index.html` —
     mbetet e paprekur: aty vendimi është doktrinor dhe i takon Isufit.
  B. `addressRegion` « Doubs » → « Bourgogne-Franche-Comté » (P2-2): në Francë
     ndarja administrative e nivelit të parë është rajoni, jo departamenti.
  C. `publisher` anonim → referenca kanonike `{"@id": ".../#business"}` (P2-3),
     që blogu të mos rrëfejë një ndërmarrje të dytë.
  D. `mentions-legales.html` merr nyjen `LocalBusiness` të plotë (P2-4): faqja
     që mban SIRET-in dhe formën juridike ishte e vetmja pa asnjë identitet.
  E. `vatID` dhe `knowsAbout` përgjithësohen mbi nyjet e biznesit (P2-5).
  F. `url` mbi nyjet `Service` (P3), nxjerrë nga `@id`-ja e vetë nyjes.
  G. Përgjigjet e `FAQPage` që ndryshojnë nga teksti i shfaqur rigjenerohen
     **nga faqja drejt JSON-LD-së**, kurrë e kundërta (P1-1c).

Jashtë perimetrit me vetëdije — presin arbitrazhin e Isufit (§8 e auditit):
doktrina e avis-eve mbi `index.html`, `legalName` (dënominacioni social i
K-bis-it), koordinatat `geo` të adresës reale, imazhet e 9 artikujve,
dhe pyetja e zonës e 736 faqeve të grilës (të shfaqet apo të hiqet).

    python3 fix_schema_org.py /rruga/drejt/rushiti-renovation           # simulim
    python3 fix_schema_org.py /rruga/drejt/rushiti-renovation --apply   # zbatim

Idempotent: riekzekutimi mbi një checkout të korrigjuar prek 0 skedarë.
Shkruan vetëm nëse çdo bllok i faqes mbetet JSON i vlefshëm pas ndërhyrjes.
"""

from __future__ import annotations

import collections
import html
import json
import os
import re
import sys

BLLOKU = re.compile(
    r'(<script[^>]*type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)',
    re.S | re.I,
)
DETAJ = re.compile(
    r"<details[^>]*>\s*<summary[^>]*>(.*?)</summary>\s*"
    r'<div[^>]*class=["\'][^"\']*\bans\b[^"\']*["\'][^>]*>(.*?)</div>',
    re.S | re.I,
)

BIZNESI = "https://rushiti-renovation.fr/#business"
TIPA_BIZNESI = {"LocalBusiness", "HousePainter", "HomeAndConstructionBusiness"}

VAT_ID = "FR89905214631"
# Vlera e `index.html`-së, e vetmja listë tashmë kanonike e zanateve. Faqet që
# mbajnë një listë të vetën (revetements-sol, a-propos) nuk preken.
KNOWS_ABOUT = [
    "Peinture intérieure",
    "Peinture extérieure",
    "Plâtrerie",
    "Placo",
    "Isolation intérieure",
    "Revêtements de sol",
    "Dégât des eaux",
    "Bâti ancien",
]

# Nyja e identitetit për `mentions-legales.html`. Çdo vlerë vjen nga CLAUDE.md
# ose nga blloqet ekzistuese të prodhimit — asnjë e dhënë e shpikur.
# `legalName` MUNGON me qëllim: dënominacioni social pret K-bis-in (§8 e auditit).
MENTIONS_LEGALES = {
    "@type": ["LocalBusiness", "HousePainter", "HomeAndConstructionBusiness"],
    "@id": BIZNESI,
    "name": "RUSHITI Rénovation",
    "url": "https://rushiti-renovation.fr",
    "logo": "https://rushiti-renovation.fr/assets/logo.png",
    "image": "https://rushiti-renovation.fr/assets/logo.png",
    "telephone": "+33760279897",
    "email": "contact@rushiti-renovation.fr",
    "priceRange": "€€",
    "taxID": "90521463100012",
    "vatID": VAT_ID,
    "identifier": {
        "@type": "PropertyValue",
        "propertyID": "SIRET",
        "value": "90521463100012",
    },
    "founder": [
        {"@type": "Person", "name": "Isuf Rushiti"},
        {"@type": "Person", "name": "Yll Rushiti"},
    ],
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "18 rue du Professeur Haag",
        "postalCode": "25000",
        "addressLocality": "Besançon",
        "addressRegion": "Bourgogne-Franche-Comté",
        "addressCountry": "FR",
    },
    "areaServed": [
        {"@type": "City", "name": "Besançon"},
        {"@type": "AdministrativeArea", "name": "Doubs"},
    ],
    "knowsAbout": KNOWS_ABOUT,
    "openingHoursSpecification": [
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "07:00",
            "closes": "20:30",
        },
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": "Saturday",
            "opens": "08:00",
            "closes": "20:30",
        },
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": "Sunday",
            "opens": "09:00",
            "closes": "17:30",
        },
    ],
    "sameAs": [
        "https://rushiti.fr",
        "https://www.facebook.com/rushiti.renovation/",
        "https://www.instagram.com/rushiti.renovation/",
        "https://www.google.com/maps?cid=10915820577691168567",
        "https://www.pagesjaunes.fr/pros/61325501",
        "https://annuaire-entreprises.data.gouv.fr/entreprise/rushiti-905214631",
        "https://data.inpi.fr/entreprises/905214631",
    ],
}


# ---------------------------------------------------------------- ndihmësit


def nyjet(o):
    """Kalon rekursivisht çdo objekt JSON të grafit."""
    if isinstance(o, dict):
        yield o
        for v in o.values():
            yield from nyjet(v)
    elif isinstance(o, list):
        for v in o:
            yield from nyjet(v)


def tipat(nyje) -> list:
    t = nyje.get("@type")
    if t is None:
        return []
    return t if isinstance(t, list) else [t]


def eshte_biznes(nyje) -> bool:
    return bool(set(tipat(nyje)) & TIPA_BIZNESI)


def normalizo(s: str) -> str:
    """Tekst i krahasueshëm: pa balisa, pa entitete, pa apostrofa tipografike."""
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    for a, b in (("’", "'"), (" ", " "), (" ", " ")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def teksti_i_dukshem(burimi: str) -> str:
    pa_kod = re.sub(
        r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", burimi, flags=re.S
    )
    return normalizo(pa_kod)


def fund_objekti(s: str, hapja: int) -> int:
    """Indeksi i kllapës mbyllëse që i përgjigjet `s[hapja] == '{'`.

    Numëron kllapat duke kapërcyer vargjet dhe sekuencat e ikjes, që një
    `{` brenda një teksti FAQ të mos e prishë numërimin.
    """
    thellesia = 0
    ne_varg = False
    i = hapja
    while i < len(s):
        c = s[i]
        if ne_varg:
            if c == "\\":
                i += 2
                continue
            if c == '"':
                ne_varg = False
        elif c == '"':
            ne_varg = True
        elif c == "{":
            thellesia += 1
        elif c == "}":
            thellesia -= 1
            if thellesia == 0:
                return i
        i += 1
    raise ValueError("objekt JSON i pambyllur")


def fillim_objekti(s: str, brenda: int) -> int:
    """Indeksi i kllapës hapëse të objektit që përmban pozicionin `brenda`.

    Kthehet mbrapsht duke provuar çdo `{` deri te e para që e mbyll pas
    `brenda` — e sigurt sepse vargjet me kllapa numërohen nga `fund_objekti`.
    """
    i = brenda
    while i >= 0:
        i = s.rfind("{", 0, i + 1)
        if i < 0:
            break
        try:
            if fund_objekti(s, i) > brenda:
                return i
        except ValueError:
            pass
        i -= 1
    raise ValueError("kllapa hapëse e pagjetur")


def stili(bllok: str) -> tuple[str, str]:
    """(ndarësi çelës/vlerë, ndarësi i elementeve) sipas formatimit të bllokut."""
    return (": ", ", ") if '": ' in bllok else (":", ",")


def fut_celes(bllok: str, hapja: int, celes: str, vlera) -> str:
    """Fut `celes` menjëherë pas kllapës hapëse të nyjes, pa prekur pjesën tjetër."""
    ndarje, ndaresi = stili(bllok)
    tekst = (
        json.dumps(celes, ensure_ascii=False)
        + ndarje
        + json.dumps(vlera, ensure_ascii=False, separators=(ndaresi, ndarje))
    )
    return bllok[: hapja + 1] + tekst + ndaresi + bllok[hapja + 1 :]


def hiq_celes(bllok: str, hapja: int, celes: str) -> str:
    """Heq `celes` (dhe presjen e tij) nga nyja që fillon në `hapja`."""
    fundi = fund_objekti(bllok, hapja)
    nyja = bllok[hapja : fundi + 1]
    m = re.search(r'"%s"\s*:\s*' % re.escape(celes), nyja)
    if not m:
        return bllok
    vlera_fillon = m.end()
    if nyja[vlera_fillon] == "{":
        vlera_mbaron = fund_objekti(nyja, vlera_fillon) + 1
    else:  # vargje, numra, lista të thjeshta: deri te ndarësi i nivelit të nyjes
        thellesia, ne_varg, j = 0, False, vlera_fillon
        while j < len(nyja):
            c = nyja[j]
            if ne_varg:
                if c == "\\":
                    j += 2
                    continue
                if c == '"':
                    ne_varg = False
            elif c == '"':
                ne_varg = True
            elif c in "[{":
                thellesia += 1
            elif c in "]}":
                if thellesia == 0:
                    break
                thellesia -= 1
            elif c == "," and thellesia == 0:
                break
            j += 1
        vlera_mbaron = j
    fillimi, mbarimi = m.start(), vlera_mbaron
    # gëlltit presjen fqinje, njërën ose tjetrën, që JSON-i të mbetet i vlefshëm
    para = re.search(r",\s*$", nyja[:fillimi])
    pas = re.match(r"\s*,", nyja[mbarimi:])
    if para:
        fillimi = para.start()
    elif pas:
        mbarimi += pas.end()
    e_re = nyja[:fillimi] + nyja[mbarimi:]
    return bllok[:hapja] + e_re + bllok[fundi + 1 :]


def ankora(bllok: str, sinjali: str, kushti) -> int | None:
    """Kllapa hapëse e nyjes së parë që përmban `sinjali` dhe plotëson `kushti`.

    `kushti` merr nyjen e analizuar. Pa të, një referencë `{"@id": "…#business"}`
    do të kapej njësoj si nyja e plotë me të njëjtin `@id` — dhe vetitë do të
    përfundonin mbi referencën.
    """
    for m in re.finditer(re.escape(sinjali), bllok):
        try:
            hapja = fillim_objekti(bllok, m.start())
            nyja = json.loads(bllok[hapja : fund_objekti(bllok, hapja) + 1])
        except (ValueError, json.JSONDecodeError):
            continue
        if kushti(nyja):
            return hapja
    return None


# ------------------------------------------------------------------- hapat


def hapi_a(bllok: str, grafi: list, dukshem: str, log) -> str:
    """A — nota e vetëshpallur, e hequr VETËM aty ku faqja s'e shfaq."""
    for nyje in grafi:
        if not eshte_biznes(nyje):
            continue
        nota = nyje.get("aggregateRating")
        if isinstance(nota, dict):
            vlera = str(nota.get("ratingValue", "")).replace(".", ",")
            numri = str(nota.get("reviewCount", ""))
            if vlera and vlera in dukshem and numri in dukshem:
                log("A~", "aggregateRating i ruajtur (nota shfaqet — vendim doktrinor i Isufit)")
            else:
                hapja = ankora(bllok, '"aggregateRating"', eshte_biznes)
                if hapja is not None:
                    bllok = hiq_celes(bllok, hapja, "aggregateRating")
                    log("A", "aggregateRating i hequr (nota nuk shfaqet në faqe)")
        avis = nyje.get("review")
        if isinstance(avis, list) and avis:
            tekstet = [normalizo(a.get("reviewBody", "")) for a in avis if isinstance(a, dict)]
            if tekstet and all(t and t in dukshem for t in tekstet):
                log("A~", "review i ruajtur (avis-et shfaqen — vendim doktrinor i Isufit)")
            else:
                hapja = ankora(bllok, '"review"', eshte_biznes)
                if hapja is not None:
                    bllok = hiq_celes(bllok, hapja, "review")
                    log("A", "review i hequr (avis-et nuk shfaqen në faqe)")
    return bllok


def hapi_b(bllok: str, log) -> str:
    """B — `addressRegion`: rajoni, jo departamenti."""
    i_ri, n = re.subn(
        r'("addressRegion"\s*:\s*")Doubs(")', r"\1Bourgogne-Franche-Comté\2", bllok
    )
    if n:
        log("B", f"addressRegion « Doubs » → « Bourgogne-Franche-Comté » ({n})")
    return i_ri


def hapi_c(bllok: str, grafi: list, log) -> str:
    """C — `publisher` anonim → referenca kanonike."""
    ka_anonim = any(
        isinstance(n.get("publisher"), dict) and not n["publisher"].get("@id")
        for n in grafi
    )
    if not ka_anonim:
        return bllok
    ndarje, _ = stili(bllok)
    ref = (
        "{"
        + json.dumps("@id", ensure_ascii=False)
        + ndarje
        + json.dumps(BIZNESI, ensure_ascii=False)
        + "}"
    )
    nga = 0
    while True:
        m = re.compile(r'"publisher"\s*:\s*').search(bllok, nga)
        if not m:
            return bllok
        fillimi = m.end()
        nga = fillimi
        if bllok[fillimi] != "{":
            continue
        try:
            fundi = fund_objekti(bllok, fillimi)
            if json.loads(bllok[fillimi : fundi + 1]).get("@id"):
                continue
        except (ValueError, json.JSONDecodeError):
            continue
        bllok = bllok[:fillimi] + ref + bllok[fundi + 1 :]
        nga = fillimi + len(ref)
        log("C", 'publisher anonim → {"@id": ".../#business"}')


def hapi_e(bllok: str, grafi: list, log) -> str:
    """E — `vatID` dhe `knowsAbout` mbi nyjet e biznesit."""
    for nyje in grafi:
        if not eshte_biznes(nyje) or nyje.get("@id") != BIZNESI:
            continue
        # nyjet-referencë (vetëm `@id`) nuk marrin veti: do të ishin dyfishim
        if len(nyje) <= 2:
            continue
        for celes, vlera in (("vatID", VAT_ID), ("knowsAbout", KNOWS_ABOUT)):
            if nyje.get(celes):
                continue
            hapja = ankora(
                bllok,
                '"' + BIZNESI + '"',
                lambda n, c=celes: eshte_biznes(n) and not n.get(c),
            )
            if hapja is not None:
                bllok = fut_celes(bllok, hapja, celes, vlera)
                log("E", f"{celes} i shtuar mbi nyjen e biznesit")
    return bllok


def hapi_f(bllok: str, grafi: list, log) -> str:
    """F — `url` mbi nyjet `Service`, nxjerrë nga `@id`-ja e tyre."""
    for nyje in grafi:
        if "Service" not in tipat(nyje) or nyje.get("url"):
            continue
        ident = nyje.get("@id", "")
        if "#" not in ident or not ident.startswith("https://rushiti-renovation.fr/"):
            continue
        hapja = ankora(
            bllok,
            '"' + ident + '"',
            lambda n: "Service" in tipat(n) and not n.get("url"),
        )
        if hapja is not None:
            bllok = fut_celes(bllok, hapja, "url", ident.split("#")[0])
            log("F", "url i shtuar mbi nyjen Service")
    return bllok


def hapi_g(bllok: str, grafi: list, dukshem: str, pergjigjet: dict, log) -> str:
    """G — përgjigjet e FAQ rigjenerohen nga teksti i shfaqur."""
    for nyje in grafi:
        if nyje.get("@type") != "Question":
            continue
        pyetja = normalizo(nyje.get("name"))
        e_balisuar = (nyje.get("acceptedAnswer") or {}).get("text")
        e_normuar = normalizo(e_balisuar)
        if not pyetja or pyetja not in dukshem or not e_normuar:
            continue
        if e_normuar in dukshem:
            continue
        e_shfaqura = pergjigjet.get(pyetja)
        if not e_shfaqura:
            log("G!", f"përgjigje divergjente pa tekst të lexueshëm — « {pyetja[:60]} »")
            continue
        i_vjeter = json.dumps(e_balisuar, ensure_ascii=False)
        i_ri = json.dumps(e_shfaqura, ensure_ascii=False)
        if i_vjeter in bllok:
            bllok = bllok.replace(i_vjeter, i_ri, 1)
            log("G", f"përgjigje e rigjeneruar nga faqja — « {pyetja[:60]} »")
    return bllok


def hapi_d(burimi: str, log) -> str:
    """D — `mentions-legales.html`: nyja e identitetit e plotë."""
    m = BLLOKU.search(burimi)
    if not m:
        return burimi
    try:
        ekzistuese = json.loads(m.group(2))
    except json.JSONDecodeError:
        return burimi
    if any(eshte_biznes(n) for n in nyjet(ekzistuese)):
        return burimi
    faqja = dict(ekzistuese)
    faqja.pop("@context", None)
    faqja.setdefault("@id", "https://rushiti-renovation.fr/mentions-legales#page")
    faqja["about"] = {"@id": BIZNESI}
    faqja["isPartOf"] = {
        "@type": "WebSite",
        "name": "RUSHITI Rénovation",
        "url": "https://rushiti-renovation.fr",
    }
    grafi = {
        "@context": "https://schema.org",
        "@graph": [faqja, MENTIONS_LEGALES],
    }
    log("D", "mentions-legales.html: nyja LocalBusiness e plotë e shtuar")
    return burimi[: m.start(2)] + json.dumps(
        grafi, ensure_ascii=False, separators=(",", ":")
    ) + burimi[m.end(2) :]


# -------------------------------------------------------------------- main


def perpuno(rel: str, burimi: str, log) -> str:
    dukshem = teksti_i_dukshem(burimi)
    pergjigjet = {
        normalizo(q): normalizo(a) for q, a in DETAJ.findall(burimi)
    }

    if os.path.basename(rel) == "mentions-legales.html" and os.path.dirname(rel) == "":
        burimi = hapi_d(burimi, log)

    dalja = []
    fundi_i_meparshem = 0
    for m in BLLOKU.finditer(burimi):
        bllok = m.group(2)
        try:
            grafi = list(nyjet(json.loads(bllok)))
        except json.JSONDecodeError:
            continue
        i_ri = hapi_a(bllok, grafi, dukshem, log)
        i_ri = hapi_b(i_ri, log)
        i_ri = hapi_c(i_ri, grafi, log)
        i_ri = hapi_e(i_ri, grafi, log)
        i_ri = hapi_f(i_ri, grafi, log)
        i_ri = hapi_g(i_ri, grafi, dukshem, pergjigjet, log)
        if i_ri == bllok:
            continue
        try:
            json.loads(i_ri)
        except json.JSONDecodeError as e:
            log("✘", f"{rel}: ndërhyrja do të prishte JSON-in ({e}) — bllok i lënë i paprekur")
            continue
        dalja.append(burimi[fundi_i_meparshem : m.start(2)])
        dalja.append(i_ri)
        fundi_i_meparshem = m.end(2)
    dalja.append(burimi[fundi_i_meparshem:])
    return "".join(dalja)


def main() -> int:
    argv = [a for a in sys.argv[1:] if a != "--apply"]
    zbato = "--apply" in sys.argv
    if len(argv) != 1:
        print(__doc__)
        return 2
    rrenja = argv[0]
    if not os.path.isdir(rrenja):
        print(f"✘ Nuk është dosje: {rrenja}")
        return 2

    numeruesi = collections.Counter()
    prekur: list[str] = []
    paralajmerime: list[str] = []

    for dp, dn, fn in os.walk(rrenja):
        dn[:] = [d for d in dn if d != ".git"]
        for f in sorted(fn):
            if not f.endswith(".html"):
                continue
            shtegu = os.path.join(dp, f)
            rel = os.path.relpath(shtegu, rrenja)
            burimi = open(shtegu, encoding="utf-8", errors="replace").read()
            if "application/ld+json" not in burimi:
                continue

            gjurma: list[tuple[str, str]] = []

            def log(hapi, mesazhi, _g=gjurma):
                _g.append((hapi, mesazhi))

            i_ri = perpuno(rel, burimi, log)
            for hapi, mesazhi in gjurma:
                if hapi.endswith("!") or hapi == "✘":
                    paralajmerime.append(f"{rel}: {mesazhi}")
                elif not hapi.endswith("~"):
                    numeruesi[hapi] += 1
            if i_ri == burimi:
                continue
            prekur.append(rel)
            if zbato:
                open(shtegu, "w", encoding="utf-8").write(i_ri)

    etiketat = {
        "A": "notë/avis të vetëshpallur të hequr (faqe që s'i shfaq)",
        "B": "addressRegion i korrigjuar",
        "C": "publisher i lidhur me entitetin",
        "D": "nyje identiteti e shtuar (mentions-legales)",
        "E": "vatID / knowsAbout të shtuar",
        "F": "url i shtuar mbi nyje Service",
        "G": "përgjigje FAQ e rigjeneruar nga faqja",
    }
    print("SIMULIM (asgjë e shkruar)" if not zbato else "ZBATIM")
    print(f"Skedarë të prekur: {len(prekur)}")
    if numeruesi:
        print("\nHAPAT:")
        for hapi in "ABCDEFG":
            if numeruesi[hapi]:
                print(f"  {numeruesi[hapi]:6d}  {hapi} — {etiketat[hapi]}")
    if paralajmerime:
        print(f"\nKUJDES ({len(paralajmerime)}):")
        for p in paralajmerime[:20]:
            print("  ⚠", p)
        if len(paralajmerime) > 20:
            print(f"  … dhe {len(paralajmerime) - 20} të tjera")
    if prekur and not zbato:
        print("\nShembuj skedarësh:")
        for r in prekur[:10]:
            print("   ", r)
        if len(prekur) > 10:
            print(f"    … dhe {len(prekur) - 10} të tjerë")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
