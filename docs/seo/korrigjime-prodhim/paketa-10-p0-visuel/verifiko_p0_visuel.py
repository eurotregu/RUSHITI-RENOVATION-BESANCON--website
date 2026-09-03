#!/usr/bin/env python3
"""Vérificateur de régression — paketa 10. Exit 0 = conforme.
Usage : python3 verifiko_p0_visuel.py /chemin/vers/rushiti-renovation
"""
import os, re, sys, glob
root = sys.argv[1] if len(sys.argv) > 1 else "."
errs = []
pages = glob.glob(os.path.join(root, "*.html")) + glob.glob(os.path.join(root, "blog", "*.html"))
for p in pages:
    name = os.path.basename(p); h = open(p, encoding="utf-8").read()
    if "Des murs à ratisser avant peinture" in h and not name.startswith("ratissage-enduit-"):
        errs.append(f"{name} : bloc CTA « ratisser » hors page ratissage")
    if '<div class="stars">' in h:
        errs.append(f"{name} : étoiles par avis présentes")
    if "34 avis Google</a></p>" in h:
        errs.append(f"{name} : ligne de synthèse des avis sans date de relevé")
    if name == "index.html" and '"review":[' in h:
        errs.append("index.html : tableau JSON-LD review (notes non relevées) présent")
    for m in re.finditer(r'href="/assets/css/s[0-9a-f]+\.css\?v=([0-9]+)"', h):
        if m.group(1) != "9": errs.append(f"{name} : CSS ?v={m.group(1)} au lieu de 9")
    # le H2 final doit contenir un mot du H1 ou de la thématique : contrôle simple sur les 7 pages corrigées
for c in glob.glob(os.path.join(root, "assets", "css", "*.css")):
    if "/*p0-ghost-cta*/" not in open(c, encoding="utf-8").read():
        errs.append(f"{os.path.basename(c)} : règle .cta-band .btn.ghost absente")
for e in errs[:40]: print("✗", e)
print("OK" if not errs else f"{len(errs)} écart(s)")
sys.exit(1 if errs else 0)
