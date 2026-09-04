#!/usr/bin/env python3
"""Vérification paquet 14 : plus aucun #1B3A5B / #13293F / #2E7D52 / rgba(19,41,63 dans le
dépôt de production (HTML, CSS, SVG, manifest), theme-color #002B4B sur toutes les pages sauf
404, cache CSS ?v=11 partout, orange d'action inchangé, PNG d'icônes sur le nouveau bleu."""
import re, sys, pathlib
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "."); errs = []
files = list(root.glob("*.html")) + list(root.glob("blog/*.html")) + list(root.glob("assets/css/*.css")) + [root / "favicon.svg", root / "site.webmanifest"]
for p in files:
    s = p.read_text(encoding="utf-8", errors="ignore"); n = p.relative_to(root)
    for bad in ("1B3A5B", "13293F", "2E7D52", "rgba(19,41,63"):
        if bad.lower() in s.lower(): errs.append(f"{n} : contient encore {bad}")
    if p.suffix == ".html" and p.name != "404.html":
        if 'name="theme-color" content="#002B4B"' not in s: errs.append(f"{n} : theme-color absent ou incorrect")
        for m in re.finditer(r'href="/assets/css/s[0-9a-f]+\.css\?v=([0-9]+)"', s):
            if m.group(1) != "11": errs.append(f"{n} : CSS ?v={m.group(1)} au lieu de 11")
for rel in ("assets/css/s971fb819.css", "assets/css/sda808997.css"):
    s = (root / rel).read_text(encoding="utf-8")
    for need in ("--navy:#002B4B", "--navy-dark:#001E36", "--ok:#016738", "--accent:#E8743B", "--accent-dark:#CF5E27"):
        if need not in s: errs.append(f"{rel} : {need} manquant")
try:
    from PIL import Image
    from collections import Counter
    for ic in ("favicon-16.png", "favicon-32.png", "apple-touch-icon.png", "favicon-192.png", "favicon-512.png"):
        p = root / ic
        if not p.exists(): errs.append(f"{ic} : absent"); continue
        im = Image.open(p).convert("RGBA"); c = Counter(px[:3] for px in im.getdata() if px[3] > 200)
        top = ["#%02x%02x%02x" % k for k, _ in c.most_common(2)]
        if "#002b4b" not in top: errs.append(f"{ic} : couleur dominante {top}, attendu #002b4b")
except ImportError:
    print("(Pillow absent : icônes non contrôlées)")
for e in errs[:40]: print("✗", e)
print("OK" if not errs else f"{len(errs)} écart(s)"); sys.exit(1 if errs else 0)
