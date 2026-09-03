#!/usr/bin/env python3
"""Vérificateur de régression — paketa 11. Exit 0 = conforme.
Usage : python3 verifiko_p1.py /chemin/vers/rushiti-renovation
"""
import glob, json, os, re, sys
root = sys.argv[1] if len(sys.argv) > 1 else "."
errs = []
pages = glob.glob(os.path.join(root, "*.html")) + glob.glob(os.path.join(root, "blog", "*.html"))
def walk(x, f):
    if isinstance(x, dict):
        t = x.get("@type")
        if isinstance(t, list) and "LocalBusiness" in t:
            if x.get("legalName") != "Rushiti": errs.append(f"{f} : legalName ≠ Rushiti")
            if "aggregateRating" in x or "review" in x: errs.append(f"{f} : aggregateRating/review présents")
        for v in x.values(): walk(v, f)
    elif isinstance(x, list):
        for v in x: walk(v, f)
for p in pages:
    f = os.path.basename(p); h = open(p, encoding="utf-8").read()
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try: walk(json.loads(b), f)
        except Exception as e: errs.append(f"{f} : JSON-LD invalide ({str(e)[:50]})")
    if 'src="https://web3forms.com/client/script.js" async defer' in h:
        errs.append(f"{f} : script Web3Forms chargé au démarrage")
    if 'data-captcha="true"' in h and "/*w3f-lazy*/" not in h:
        errs.append(f"{f} : formulaire sans chargeur différé")
a = open(os.path.join(root, "a-propos.html"), encoding="utf-8").read()
for must in ('id="isuf"', "#isuf", '"@type":"FAQPage"', 'width="828"'):
    if must not in a: errs.append(f"a-propos.html : manque {must}")
c = open(os.path.join(root, "contact.html"), encoding="utf-8").read()
for must in ("24 à 48 h ouvrées", "Voir sur Google Maps", "Écrire sur WhatsApp"):
    if must not in c: errs.append(f"contact.html : manque {must}")
for e in errs[:40]: print("✗", e)
print("OK" if not errs else f"{len(errs)} écart(s)")
sys.exit(1 if errs else 0)
