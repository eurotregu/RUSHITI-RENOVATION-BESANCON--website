#!/usr/bin/env python3
"""Paketa 8 — 766 pyetjet FAQ të balisuara por të padukshme (P1-1 e auditit).

Google e kërkon shprehimisht: përmbajtja e një `FAQPage` duhet të jetë **e
dukshme për vizitorin** mbi faqen që e balison. Përmbajtje që jeton vetëm në
JSON-LD është shkelje e rregullave të të dhënave të strukturuara, e
ndëshkueshme me veprim manual.

Auditi i 31/08 numëroi 766 pyetje të tilla, në dy familje me mekanika të
ndryshme:

  **grila** (≈736 faqe) — gabariti shton në JSON-LD një pyetje zone që nuk
  jepet kurrë në HTML: « Vous déplacez-vous à Deluz ? » ose, për lagjet,
  « Intervenez-vous dans le quartier Velotte ? » ;

  **blogu** (9 artikuj, 29 pyetje) — e gjithë seksioni FAQ mungon nga trupi i
  artikullit, ndonëse i balisuar. Artikulli i dhjetë,
  `blog/reparer-plafond-degat-des-eaux-besancon.html`, e shfaq të vetin: ai
  është gabariti që ndiqet këtu, fjalë për fjalë.

Dy rrugë, sa kohë Isufi nuk ka vendosur:

    --afisho   (parazgjedhje, rekomandimi i auditit)
        E bën të dukshme pyetjen që tashmë ekziston në JSON-LD. **Asnjë fjalë
        nuk shkruhet**: teksti vjen fjalë për fjalë nga `acceptedAnswer`, i
        shkruar dhe i validuar më parë. « Vous déplacez-vous à X ? » është një
        pyetje e vërtetë klienti — fshehja e saj humbet një përgjigje të mirë.

    --hiq
        Heq nga JSON-LD pyetjet që faqja nuk i shfaq. Konformiteti rikthehet
        po aq mirë, por faqja humbet përmbajtje dhe pasurimin e mundshëm.

Të dyja e kthejnë `verifiko_schema_org.py` në zero për këtë kontroll. Zgjedhja
midis tyre është redaktoriale, jo teknike — prandaj skripti i mban të dyja dhe
nuk vendos në vend të Isufit.

    python3 fix_faq_dukshme.py /rruga/drejt/rushiti-renovation                    # simulim
    python3 fix_faq_dukshme.py /rruga/drejt/rushiti-renovation --afisho --apply
    python3 fix_faq_dukshme.py /rruga/drejt/rushiti-renovation --hiq --apply

Idempotent në të dyja mënyrat. Shkruan vetëm nëse çdo bllok JSON-LD i faqes
mbetet i vlefshëm dhe balanca e tageve `<details>` mbetet e mbyllur.
"""

from __future__ import annotations

import collections
import html as htmllib
import json
import os
import re
import sys

BLLOKU = re.compile(
    r'(<script[^>]*type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)',
    re.S | re.I,
)
SKRIPT = re.compile(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", re.S)
CTA_BLOGU = '<div class="cta-soft">'
H2_FAQ = '<h2 id="faq">Questions fréquentes</h2>'


def nyjet(o):
    if isinstance(o, dict):
        yield o
        for v in o.values():
            yield from nyjet(v)
    elif isinstance(o, list):
        for v in o:
            yield from nyjet(v)


def normalizo(s: str) -> str:
    s = htmllib.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    for a, b in (("’", "'"), (" ", " "), (" ", " ")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def maskuar(burimi: str) -> str:
    """Burimi me përmbajtjen e `<script>`/`<style>` të zbrazur, gjatësi e njëjtë.

    Lejon të gjesh pozicionin e `</details>` të fundit **të vërtetë** pa u
    ngatërruar nga një `</details>` brenda një vargu JavaScript — rasti real i
    `simulateur-peinture.html`.
    """
    return SKRIPT.sub(lambda m: " " * len(m.group(0)), burimi)


def pyetjet_e_padukshme(burimi: str) -> list[tuple[str, str]]:
    """(pyetja, përgjigjja) për çdo `Question` që faqja nuk e shfaq."""
    dukshem = normalizo(maskuar(burimi))
    dalja, pare = [], set()
    for m in BLLOKU.finditer(burimi):
        try:
            grafi = json.loads(m.group(2))
        except json.JSONDecodeError:
            continue
        for nyje in nyjet(grafi):
            if nyje.get("@type") != "Question":
                continue
            pyetja = normalizo(nyje.get("name"))
            pergjigja = normalizo((nyje.get("acceptedAnswer") or {}).get("text"))
            if not pyetja or not pergjigja or pyetja in dukshem or pyetja in pare:
                continue
            pare.add(pyetja)
            dalja.append((pyetja, pergjigja))
    return dalja


def detaj(pyetja: str, pergjigja: str) -> str:
    """Një `<details>` sipas gabaritit të faqeve që e shfaqin FAQ-në e tyre."""
    return (
        "<details><summary>"
        + htmllib.escape(pyetja, quote=False)
        + '</summary><div class="ans">'
        + htmllib.escape(pergjigja, quote=False)
        + "</div></details>"
    )


def afisho(rel: str, burimi: str, cifte: list, log) -> str:
    """Shfaq në HTML pyetjet që janë vetëm në JSON-LD."""
    blloku = " ".join(detaj(p, pp) for p, pp in cifte)

    # Blogu: seksioni FAQ i tërë mungon → futet para CTA-së, si te gabariti.
    if rel.startswith("blog" + os.sep) and "<details" not in maskuar(burimi):
        pika = burimi.find(CTA_BLOGU)
        if pika < 0:
            log("!", f"{rel}: pa pikë ankorimi për seksionin FAQ — i lënë i paprekur")
            return burimi
        log("blog", f"{len(cifte)} pyetje të shfaqura në një seksion FAQ të ri")
        return burimi[:pika] + H2_FAQ + " " + blloku + "\n  " + burimi[pika:]

    # Grila: FAQ-ja ekziston, i mungon vetëm pyetja e zonës → shtohet në fund.
    fundi = maskuar(burimi).rfind("</details>")
    if fundi < 0:
        log("!", f"{rel}: asnjë <details> ekzistues — i lënë i paprekur")
        return burimi
    fundi += len("</details>")
    log("grile", f"{len(cifte)} pyetje e shfaqur në fund të FAQ-së")
    return burimi[:fundi] + blloku + burimi[fundi:]


def hiq(burimi: str, cifte: list, log) -> str:
    """Heq nga JSON-LD pyetjet që faqja nuk i shfaq."""
    emrat = {p for p, _ in cifte}
    dalja, fundi_i_meparshem = [], 0
    for m in BLLOKU.finditer(burimi):
        try:
            grafi = json.loads(m.group(2))
        except json.JSONDecodeError:
            continue
        prekur = False
        for nyje in nyjet(grafi):
            lista = nyje.get("mainEntity")
            if not isinstance(lista, list):
                continue
            e_re = [
                q
                for q in lista
                if not (
                    isinstance(q, dict)
                    and q.get("@type") == "Question"
                    and normalizo(q.get("name")) in emrat
                )
            ]
            if len(e_re) != len(lista):
                nyje["mainEntity"] = e_re
                prekur = True
        if not prekur:
            continue
        log("hequr", f"{len(cifte)} pyetje të hequra nga balisimi")
        dalja.append(burimi[fundi_i_meparshem : m.start(2)])
        dalja.append(json.dumps(grafi, ensure_ascii=False, separators=(",", ":")))
        fundi_i_meparshem = m.end(2)
    dalja.append(burimi[fundi_i_meparshem:])
    return "".join(dalja)


def i_shendetshem(rel: str, burimi: str, log) -> bool:
    """JSON i vlefshëm kudo, dhe `<details>` të balancuara."""
    for m in BLLOKU.finditer(burimi):
        try:
            json.loads(m.group(2))
        except json.JSONDecodeError as e:
            log("✘", f"{rel}: JSON i prishur ({e}) — faqe e lënë e paprekur")
            return False
    m = maskuar(burimi)
    if m.count("<details") != m.count("</details>"):
        log("✘", f"{rel}: <details> të pabalancuara — faqe e lënë e paprekur")
        return False
    return True


def main() -> int:
    flamujt = {a for a in sys.argv[1:] if a.startswith("--")}
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    zbato = "--apply" in flamujt
    menyra = "hiq" if "--hiq" in flamujt else "afisho"
    if len(argv) != 1 or ("--hiq" in flamujt and "--afisho" in flamujt):
        print(__doc__)
        return 2
    rrenja = argv[0]
    if not os.path.isdir(rrenja):
        print(f"✘ Nuk është dosje: {rrenja}")
        return 2

    numeruesi = collections.Counter()
    pyetje = 0
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
            cifte = pyetjet_e_padukshme(burimi)
            if not cifte:
                continue

            gjurma: list[tuple[str, str]] = []

            def log(etiketa, mesazhi, _g=gjurma):
                _g.append((etiketa, mesazhi))

            if menyra == "afisho":
                i_ri = afisho(rel, burimi, cifte, log)
            else:
                i_ri = hiq(burimi, cifte, log)

            for etiketa, mesazhi in gjurma:
                if etiketa in ("!", "✘"):
                    paralajmerime.append(mesazhi)
                else:
                    numeruesi[etiketa] += 1
            if i_ri == burimi or not i_shendetshem(rel, i_ri, log):
                for etiketa, mesazhi in gjurma[len(gjurma) - 1 :]:
                    if etiketa == "✘":
                        paralajmerime.append(mesazhi)
                continue
            pyetje += len(cifte)
            prekur.append(rel)
            if zbato:
                open(shtegu, "w", encoding="utf-8").write(i_ri)

    print("ZBATIM" if zbato else "SIMULIM (asgjë e shkruar)")
    print(f"Mënyra: {'--hiq (heqje nga balisimi)' if menyra == 'hiq' else '--afisho (shfaqje në faqe)'}")
    print(f"Skedarë të prekur: {len(prekur)}   pyetje të trajtuara: {pyetje}")
    etiketat = {
        "grile": "faqe grile — pyetja e zonës e shfaqur",
        "blog": "artikull blogu — seksioni FAQ i shfaqur",
        "hequr": "faqe — pyetje të hequra nga balisimi",
    }
    if numeruesi:
        print()
        for e, n in numeruesi.most_common():
            print(f"  {n:6d}  {etiketat.get(e, e)}")
    if paralajmerime:
        print(f"\nKUJDES ({len(paralajmerime)}):")
        for p in paralajmerime[:20]:
            print("  ⚠", p)
        if len(paralajmerime) > 20:
            print(f"  … dhe {len(paralajmerime) - 20} të tjera")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
