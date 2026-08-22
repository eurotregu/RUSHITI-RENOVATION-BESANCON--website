#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vegël e përhershme regresi: verifikon shëndetin e formularëve « Demande
rapide » në depon e prodhimit (eurotregu/rushiti-renovation). Ekzekutohet pas
çdo rigjenerimi faqesh, ndryshimi gabariti ose para çdo deploy-i.

Kontrollet për secilën nga 30 faqet pilier me formular:
  - 1 formular që poston te Web3Forms me access_key identik me /contact;
  - subjekt jo bosh që mbaron me « — rushiti-renovation.fr »;
  - redirect /merci, honeypot botcheck, lidhja /mentions-legales;
  - fusha e fshehtë page = URL-ja e faqes (atribuim për faqe);
  - stili /*dr-style në <head> (CSS-ja globale nuk mbart rregulla formulari);
  - strukturë e shëndoshë: 1 </head>, 1 </main>, 1 </body>, <form> = </form>,
    asnjë «</main></main>» i dyfishuar.
Plus: /merci mbart eventin Lead /*lead-formulaire (numërimi i konvertimeve).

Përdorimi:
    python3 verifiko_demande_rapide.py /rruga/drejt/rushiti-renovation
Exit 0 = konform, 1 = probleme.
"""
import re
import sys
from pathlib import Path

ACCESS_KEY = "1aee0248-cb88-4790-aa90-c1a76b26d0bb"  # i njëjti me /contact

PAGES = [
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
    "prix-travaux-renovation-besancon.html",
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


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    root = Path(sys.argv[1])
    gabime = 0

    for fname in sorted(PAGES):
        f = root / fname
        if not f.exists():
            print("MUNGON %s" % fname)
            gabime += 1
            continue
        h = f.read_text(encoding="utf-8")
        p = []
        if h.count('action="https://api.web3forms.com/submit"') != 1:
            p.append("formulari Web3Forms: %d herë" % h.count('action="https://api.web3forms.com/submit"'))
        if h.count(ACCESS_KEY) != 1:
            p.append("access_key: %d herë" % h.count(ACCESS_KEY))
        m = re.search(r'name="subject" value="([^"]+)"', h)
        if not m or not m.group(1).strip() or not m.group(1).endswith("— rushiti-renovation.fr"):
            p.append("subjekt bosh ose jashtë formatit")
        if 'name="redirect" value="https://rushiti-renovation.fr/merci">' not in h:
            p.append("redirect /merci mungon")
        if 'name="botcheck"' not in h:
            p.append("honeypot botcheck mungon")
        if 'href="/mentions-legales"' not in h:
            p.append("lidhja /mentions-legales mungon")
        if ('name="page" value="https://rushiti-renovation.fr/%s"' % fname[:-5]) not in h:
            p.append("fusha page nuk tregon faqen")
        if "/*dr-style" not in h:
            p.append("stili dr-style mungon")
        if "</main></main>" in h:
            p.append("</main></main> i dyfishuar")
        for tag in ("</head>", "</main>", "</body>"):
            if h.count(tag) != 1:
                p.append("%s: %d herë" % (tag, h.count(tag)))
        if h.count("<form") != h.count("</form>"):
            p.append("<form> %d ≠ </form> %d" % (h.count("<form"), h.count("</form>")))

        if p:
            gabime += 1
            print("GABIM  %s — %s" % (fname, "; ".join(p)))
        else:
            print("OK     %s" % fname)

    merci = root / "merci.html"
    if not merci.exists() or "/*lead-formulaire" not in merci.read_text(encoding="utf-8"):
        print("GABIM  merci.html — eventi Lead /*lead-formulaire mungon")
        gabime += 1
    else:
        print("OK     merci.html (eventi Lead i pranishëm)")

    print("\n%d faqe + /merci të kontrolluara, %d me probleme." % (len(PAGES), gabime))
    sys.exit(1 if gabime else 0)


if __name__ == "__main__":
    main()
