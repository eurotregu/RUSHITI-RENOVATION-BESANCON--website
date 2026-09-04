#!/usr/bin/env python3
"""Vérification paquet 13 : chaque page fixe listée porte exactement un bloc geo BAN
dans un JSON-LD valide, et l'ancien couple centre-ville (47.238 / 6.0243) n'apparaît nulle part."""
import json, re, sys, pathlib
PAGES = ["peinture-interieure-besancon", "platrerie-besancon", "degat-des-eaux-besancon", "a-propos", "contact", "mentions-legales"]
LD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "."); ko = 0
for slug in PAGES:
    h = (root / f"{slug}.html").read_text(encoding="utf-8")
    ok = h.count('"latitude":47.245638,"longitude":6.00556') == 1 and "47.238" not in h
    try:
        for m in LD_RE.finditer(h): json.loads(m.group(1))
    except Exception as e:
        ok = False; print("   JSON-LD invalide :", e)
    print(("OK " if ok else "KO ") + slug); ko += (not ok)
print("total sans geo :", sum(1 for f in root.glob("*.html") if '"latitude"' not in f.read_text(encoding="utf-8")), "page(s)")
sys.exit(1 if ko else 0)
