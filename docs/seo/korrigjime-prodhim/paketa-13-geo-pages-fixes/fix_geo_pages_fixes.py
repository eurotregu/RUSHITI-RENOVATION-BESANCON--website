#!/usr/bin/env python3
"""Paketa 13 — coordonnées geo manquantes sur les nœuds LocalBusiness des pages fixes.

Contexte : le paquet 12 ne corrigeait que les nœuds qui avaient déjà un bloc
"geo" (centre-ville → BAN). Six pages fixes n'en avaient aucun. Ce script
insère, juste après l'objet "address" du nœud LocalBusiness, le bloc
"geo" à la position BAN du 18 rue du Professeur Haag (47.245638 / 6.00556,
id BAN 25056_4260_00018). Idempotent : une page qui a déjà "geo" est ignorée.

Usage : python3 fix_geo_pages_fixes.py /chemin/du/clone/production
"""
import json, re, sys, pathlib

PAGES = ["peinture-interieure-besancon", "platrerie-besancon", "degat-des-eaux-besancon",
         "a-propos", "contact", "mentions-legales"]
GEO = ',"geo":{"@type":"GeoCoordinates","latitude":47.245638,"longitude":6.00556}'
ADDR_RE = re.compile(r'("address":\{"@type":"PostalAddress","streetAddress":"18 rue du Professeur Haag"[^{}]*\})')
LD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)

def main(root):
    root = pathlib.Path(root); done = 0
    for slug in PAGES:
        p = root / f"{slug}.html"; h = p.read_text(encoding="utf-8")
        if '"geo"' in h:
            print(f"  = {slug} : geo déjà présent, ignoré"); continue
        h2, n = ADDR_RE.subn(lambda m: m.group(1) + GEO, h, count=1)
        if n != 1:
            print(f"  ! {slug} : adresse non trouvée, rien fait"); continue
        for m in LD_RE.finditer(h2):
            json.loads(m.group(1))  # JSON-LD toujours valide après insertion
        p.write_text(h2, encoding="utf-8"); done += 1
        print(f"  + {slug} : geo ajouté")
    print(f"{done} page(s) modifiée(s)")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
