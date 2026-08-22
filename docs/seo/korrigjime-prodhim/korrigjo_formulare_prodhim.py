#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Plotëson formularët « Demande rapide » të depos së prodhimit
(eurotregu/rushiti-renovation) — vendimet e 21-22/08/2026, autorizuar nga Isuf.

⚠️ Ndarja e punës me PR #10 (paraekzistues, «mise en forme et variante B»):
PR #10 mbart stilimin në CSS-në globale (?v=8), kutinë e pëlqimit RGPD dhe
eventin Lead në /merci. KY skript mbart pjesën plotësuese — asnjë mbivendosje:

1. «</main></main>» i dyfishuar → «</main>» (defekt validiteti, 11 faqe);
2. fushë e fshehtë name="page" me URL-në e faqes në çdo formular — atribuimi
   i saktë i çdo kërkese (subjekti dallon vetëm shërbimin, jo faqen);
3. prix-travaux-renovation-besancon.html — e vetmja faqe pilier pa formular —
   merr seksionin « Demande rapide » të transplantuar nga gabariti live i
   toile-de-verre-besancon.html (subjekt e para-zgjedhje të përshtatura).

Idempotent: faqet e korrigjuara kapërcehen.

Përdorimi (mbi një checkout të depos së prodhimit):
    python3 korrigjo_formulare_prodhim.py /rruga/drejt/rushiti-renovation           # simulim
    python3 korrigjo_formulare_prodhim.py /rruga/drejt/rushiti-renovation --apply   # zbatim
"""
import sys
from pathlib import Path

# Faqet pilier me formular « Demande rapide » të shpërndarë (gjendja 21/08/2026)
PAGES_ME_FORMULAR = [
    "amenagement-commerce-bureau-besancon.html",
    "cloisons-besancon.html",
    "degat-des-eaux-besancon.html",
    "devis-assurance-degat-des-eaux-besancon.html",
    "doublage-murs-besancon.html",
    "entreprise-renovation-besancon.html",
    "expert-assurance-sinistre-besancon.html",
    "faux-plafonds-besancon.html",
    "isolation-besancon.html",
    "isolation-interieure-besancon.html",
    "lino-vinyle-lvt-besancon.html",
    "papier-peint-besancon.html",
    "parquet-flottant-besancon.html",
    "peinture-exterieure-besancon.html",
    "peinture-facade-isolation-exterieure-besancon.html",
    "peinture-interieure-besancon.html",
    "plaquiste-besancon.html",
    "platrerie-besancon.html",
    "ragreage-sol-besancon.html",
    "ratissage-enduit-besancon.html",
    "remise-en-etat-logement-locatif-besancon.html",
    "renovation-appartement-besancon.html",
    "renovation-cuisine-besancon.html",
    "renovation-salle-de-bain-besancon.html",
    "renovation-syndic-gestionnaire-besancon.html",
    "revetements-sol-besancon.html",
    "sol-pvc-besancon.html",
    "toile-de-verre-besancon.html",
    "vitrification-parquet-besancon.html",
]

FAQJA_PA_FORMULAR = "prix-travaux-renovation-besancon.html"
DONATORI = "toile-de-verre-besancon.html"


def fusha_page(slug):
    return ('<input type="hidden" name="page" value="https://rushiti-renovation.fr/%s">'
            % slug)


def merr_seksionin_donator(root):
    """Nxjerr seksionin « Demande rapide » nga faqja donatore, i përshtatur
    për prix-travaux (subjekt, H2 i seksionit, opsion i para-zgjedhur)."""
    h = (root / DONATORI).read_text(encoding="utf-8")
    i = h.find('<section class="soft" id="demande-rapide">')
    j = h.find("</section>", i) + len("</section>")
    if i < 0 or j <= i:
        raise SystemExit("Seksioni donator nuk u gjet në %s" % DONATORI)
    s = h[i:j]
    s = s.replace(
        'name="subject" value="Demande rapide — Toile de verre — rushiti-renovation.fr"',
        'name="subject" value="Demande rapide — Estimation travaux — rushiti-renovation.fr"')
    s = s.replace("Demande rapide : décrivez votre projet toile de verre",
                  "Demande rapide : décrivez votre projet à estimer")
    s = s.replace("<option selected>Papier peint / toile de verre</option>",
                  "<option>Papier peint / toile de verre</option>")
    s = s.replace("<option>Autre / plusieurs travaux</option>",
                  "<option selected>Autre / plusieurs travaux</option>")
    # fusha page e faqes donatore nuk duhet trashëguar
    s = s.replace(fusha_page(DONATORI[:-5]) + "\n", "")
    s = s.replace(fusha_page(DONATORI[:-5]), "")
    return s


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    root = Path(sys.argv[1])
    apply = "--apply" in sys.argv
    ndryshime, gabime = 0, 0

    # 1. </main></main> kudo në depo
    for f in sorted(root.glob("*.html")) + sorted(root.glob("blog/*.html")):
        h = f.read_text(encoding="utf-8")
        if "</main></main>" in h:
            if apply:
                f.write_text(h.replace("</main></main>", "</main>"), encoding="utf-8")
            print("MAIN2  %s" % f.relative_to(root))
            ndryshime += 1

    # 2. Fusha page në faqet me formular
    for fname in PAGES_ME_FORMULAR:
        f = root / fname
        if not f.exists():
            print("MUNGON %s" % fname)
            gabime += 1
            continue
        h = f.read_text(encoding="utf-8")
        if 'name="page"' in h:
            continue
        ankora = 'name="redirect" value="https://rushiti-renovation.fr/merci">'
        if h.count(ankora) != 1:
            print("GABIM  %s: ankora redirect = %d" % (fname, h.count(ankora)))
            gabime += 1
            continue
        h = h.replace(ankora, ankora + "\n" + fusha_page(fname[:-5]), 1)
        if apply:
            f.write_text(h, encoding="utf-8")
        print("%s %s (page)" % ("SHTUAR" if apply else "DO SHTOHEJ", fname))
        ndryshime += 1

    # 3. Formulari për prix-travaux
    f = root / FAQJA_PA_FORMULAR
    if f.exists():
        h = f.read_text(encoding="utf-8")
        # hapi 1 mund të mos jetë shkruar ende në disk (simulim) — normalizohet këtu
        h = h.replace("</main></main>", "</main>")
        if 'id="demande-rapide"' in h:
            print("KA TASHME %s" % FAQJA_PA_FORMULAR)
        elif h.count("</main>") != 1:
            print("GABIM  %s: strukturë e papritur" % FAQJA_PA_FORMULAR)
            gabime += 1
        else:
            seksioni = merr_seksionin_donator(root)
            h = h.replace("</main>", seksioni + "\n</main>", 1)
            ank = 'name="redirect" value="https://rushiti-renovation.fr/merci">'
            h = h.replace(ank, ank + "\n" + fusha_page(FAQJA_PA_FORMULAR[:-5]), 1)
            if apply:
                f.write_text(h, encoding="utf-8")
            print("%s %s (formular i plotë)" % ("SHTUAR" if apply else "DO SHTOHEJ", FAQJA_PA_FORMULAR))
            ndryshime += 1
    else:
        print("MUNGON %s" % FAQJA_PA_FORMULAR)
        gabime += 1

    print("\n%d ndryshime%s, %d probleme."
          % (ndryshime, "" if apply else " (simulim)", gabime))
    sys.exit(1 if gabime else 0)


if __name__ == "__main__":
    main()
