#!/usr/bin/env python3
"""Vérificateur de régression — paketa 9. Exit 0 = conforme.
Usage : python3 verifiko_llms_mentions.py /chemin/vers/rushiti-renovation
Contrôle que llms.txt et mentions-legales.html ne réintroduisent aucun des écarts du 03/09/2026
et que les faits partagés (horaires, avis) sont identiques à ceux de index.html.
"""
import os, re, sys

root = sys.argv[1] if len(sys.argv) > 1 else "."
errs = []

llms = open(os.path.join(root, "llms.txt"), encoding="utf-8").read()
for bad, why in (("Raison sociale : RUSHITI Rénovation", "nom commercial présenté comme raison sociale"),
                 ("sur 29 avis", "compteur d'avis périmé"),
                 ("8h–18h", "horaires faux")):
    if bad in llms: errs.append(f"llms.txt : {why} ({bad!r})")
for must in ("Dénomination sociale : Rushiti", "SIRET : 905 214 631 00012", "18 rue du Professeur Haag",
             "07 60 27 98 97", "7h–20h30", "Dernière mise à jour"):
    if must not in llms: errs.append(f"llms.txt : manque {must!r}")

ml = open(os.path.join(root, "mentions-legales.html"), encoding="utf-8").read()
for bad, why in (("hébergé par RUSHITI Rénovation", "hébergeur faux"),
                 ("<p><b>RUSHITI Rénovation</b><br>\nForme juridique", "nom commercial à la place de la dénomination"),
                 ("un seul traceur", "section cookies incomplète (GTM chargé)")):
    if bad in ml: errs.append(f"mentions-legales.html : {why}")
for must in ("Cloudflare", "RCS Besançon 905 214 631", "Google Tag Manager"):
    if must not in ml: errs.append(f"mentions-legales.html : manque {must!r}")

# Cohérence avec la page d'accueil (horaires et compteur d'avis)
idx = os.path.join(root, "index.html")
if os.path.exists(idx):
    home = open(idx, encoding="utf-8").read()
    m = re.search(r"(\d+) avis Google", home)
    if m and f"sur {m.group(1)} avis" not in llms:
        errs.append(f"llms.txt : compteur d'avis ({m.group(1)} sur index.html) différent")
    if "7h – 20h30" in home and "7h–20h30" not in llms:
        errs.append("llms.txt : horaires différents de index.html")

for e in errs: print("✗", e)
print("OK" if not errs else f"{len(errs)} écart(s)")
sys.exit(1 if errs else 0)
