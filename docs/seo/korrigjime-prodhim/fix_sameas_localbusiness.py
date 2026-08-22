#!/usr/bin/env python3
"""Plotëson `sameAs` të nyjeve LocalBusiness me profilet e verifikuara.

Konteksti: verifikimi i 22/08/2026 (shih
`docs/seo/verifikim-sameas-localbusiness-2026-08-22.md`) tregoi se 736 faqe
deklarojnë vetëm `["https://rushiti.fr"]`, pa PagesJaunes, pa Google Maps dhe
pa asnjë regjistër tregtar. Ky skript i plotëson.

Sjellja:
  * prek VETËM vargjet `"sameAs": [...]` brenda blloqeve
    `<script type="application/ld+json">` — asnjë rishkrim i JSON-it, pra
    formatimi ekzistues (i bukur ose i minifikuar) ruhet;
  * shton URL-të që mungojnë, ruan ato që ekzistojnë (bashkim, jo zëvendësim);
  * radha përfundimtare është ajo e `SAMEAS_KANONIK`, e ndjekur nga çdo URL
    tjetër e panjohur që faqja mbante më parë;
  * idempotent: rileximi i një faqeje tashmë të korrigjuar jep 0 ndryshime;
  * për faqet me nyje biznesi me `@id` por PA `sameAs` (rasti
    `zones-intervention.html`), vargu futet para `"priceRange"`.

NUK prek: nyjet e ngulitura LocalBusiness pa `@id` (`contact.html`,
`simulateur-peinture.html`, `blog/calcul-rouleaux-papier-peint.html`) — ato
duhen shndërruar në referencë `{"@id": ".../#business"}`, vendim redaktorial,
jo zëvendësim automatik.

Përdorimi:
    python3 fix_sameas_localbusiness.py /rruga/drejt/rushiti-renovation
    python3 fix_sameas_localbusiness.py /rruga/drejt/rushiti-renovation --apply
"""

from __future__ import annotations

import json
import os
import re
import sys

# URL-të e verifikuara live më 22/08/2026 (kod HTTP 200 + përputhje entiteti).
# Asnjë URL nuk shtohet këtu pa u hapur dhe pa u verifikuar SIRET/telefoni.
SAMEAS_KANONIK = [
    "https://rushiti.fr",
    "https://www.facebook.com/rushiti.renovation/",
    "https://www.instagram.com/rushiti.renovation/",
    "https://www.google.com/maps?cid=10915820577691168567",
    "https://www.pagesjaunes.fr/pros/61325501",
    "https://annuaire-entreprises.data.gouv.fr/entreprise/rushiti-905214631",
    "https://data.inpi.fr/entreprises/905214631",
]

LD_BLLOK = re.compile(
    r'(<script[^>]*application/ld\+json[^>]*>)(.*?)(</script>)', re.S)
SAMEAS = re.compile(r'"sameAs"(\s*):(\s*)\[(.*?)\]', re.S)
PRICERANGE = re.compile(r'("priceRange"\s*:\s*"[^"]*",?)')


def bashko(ekzistuese: list[str]) -> list[str]:
    """Kanoniket në radhë, pastaj URL-të e tjera që faqja mbante."""
    shtesa = [u for u in ekzistuese if u not in SAMEAS_KANONIK]
    return SAMEAS_KANONIK + shtesa


def rishkruaj_sameas(bllok: str) -> tuple[str, int]:
    ndryshime = 0

    def zevendeso(m: re.Match) -> str:
        nonlocal ndryshime
        hapesire_para, hapesire_pas, trupi = m.group(1), m.group(2), m.group(3)
        try:
            ekzistuese = json.loads("[" + trupi + "]")
        except json.JSONDecodeError:
            return m.group(0)  # varg i pazakontë — nuk e prekim
        if not all(isinstance(u, str) for u in ekzistuese):
            return m.group(0)
        e_re = bashko(ekzistuese)
        if e_re == ekzistuese:
            return m.group(0)
        ndryshime += 1
        # Stili i ndarësit merret nga vargu ekzistues (minifikuar apo jo).
        ndares = ", " if ", " in trupi or hapesire_pas else ","
        trup_i_ri = ndares.join(json.dumps(u, ensure_ascii=False) for u in e_re)
        return f'"sameAs"{hapesire_para}:{hapesire_pas}[{trup_i_ri}]'

    return SAMEAS.sub(zevendeso, bllok), ndryshime


def fut_sameas(bllok: str) -> tuple[str, int]:
    """Fut `sameAs` në nyjet me `@id` biznesi por pa `sameAs`."""
    if '"sameAs"' in bllok or '#business' not in bllok:
        return bllok, 0
    if not PRICERANGE.search(bllok):
        return bllok, 0
    varg = ",".join(json.dumps(u, ensure_ascii=False) for u in SAMEAS_KANONIK)
    i_ri = PRICERANGE.sub(
        lambda m: m.group(1) + f'"sameAs":[{varg}],', bllok, count=1)
    return i_ri, 1 if i_ri != bllok else 0


def perpuno(shteg: str) -> int:
    with open(shteg, encoding="utf-8") as f:
        html = f.read()
    total = 0

    def per_bllok(m: re.Match) -> str:
        nonlocal total
        hapja, trupi, mbyllja = m.group(1), m.group(2), m.group(3)
        if "LocalBusiness" not in trupi and "HousePainter" not in trupi:
            return m.group(0)
        i_ri, n = rishkruaj_sameas(trupi)
        if n == 0:
            i_ri, n = fut_sameas(trupi)
        total += n
        return hapja + i_ri + mbyllja

    i_ri = LD_BLLOK.sub(per_bllok, html)
    if total and i_ri != html:
        if "--apply" in sys.argv:
            with open(shteg, "w", encoding="utf-8") as f:
                f.write(i_ri)
    return total


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    rrenja = sys.argv[1]
    zbato = "--apply" in sys.argv
    prekura = 0
    ndryshime = 0
    for dp, dn, fn in os.walk(rrenja):
        dn[:] = [d for d in dn if d != ".git"]
        for f in sorted(fn):
            if not f.endswith(".html"):
                continue
            shteg = os.path.join(dp, f)
            n = perpuno(shteg)
            if n:
                prekura += 1
                ndryshime += n
                print(f"  {'✔' if zbato else '→'} {os.path.relpath(shteg, rrenja)} ({n})")
    mode = "ZBATUAR" if zbato else "SIMULIM (pa --apply asgjë nuk shkruhet)"
    print(f"\n{mode}: {prekura} faqe, {ndryshime} vargje sameAs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
