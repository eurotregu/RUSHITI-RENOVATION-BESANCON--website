#!/usr/bin/env python3
"""Paketa 14 — charte v2.7, variante B (décision d'Isuf du 04/09/2026).

Bleu nuit du site aligné sur la charte (#1B3A5B → #002B4B), vert positif
aligné (#2E7D52 → #016738), couleur d'action orange conservée (#E8743B /
#CF5E27). Rien d'autre ne change : mêmes gabarits, mêmes textes.

Ce que le script fait (idempotent, relançable) :
  A. Feuilles s971fb819.css et sda808997.css : variables --navy, --navy-dark,
     --ok ; ombres rgba(19,41,63,…) → rgba(0,30,54,…) (navy-dark).
  B. 756 pages : <meta name="theme-color"> #1B3A5B → #002B4B ; cache CSS ?v=10 → ?v=11.
  C. blog/reparer-plafond-degat-des-eaux-besancon.html : bloc :root inline complet
     (--navy, --navy-dark, --ok, ombres) traité comme les feuilles.
  D. site.webmanifest : theme_color.
  E. favicon.svg : fond #1B3A5B → #002B4B (les PNG sont régénérés à part, gen_icones.js).
  F. Coches SVG inline stroke="#2E7D52" → stroke="#016738" (7 377 coches sur 726 pages).

--navy-dark : la charte ne définit qu'un bleu nuit ; le pied de page et les
ombres utilisent une déclinaison plus sombre, dérivée de #002B4B (#001E36),
à faire entrer dans la charte v2.8 avec l'orange d'action.

Usage : python3 fix_charte_B.py /chemin/du/clone/production
"""
import re, sys, pathlib

OLD_NAVY, NEW_NAVY = "#1B3A5B", "#002B4B"
OLD_NAVY_DARK, NEW_NAVY_DARK = "#13293F", "#001E36"
OLD_OK, NEW_OK = "#2E7D52", "#016738"
OLD_SHADOW_RGB, NEW_SHADOW_RGB = "rgba(19,41,63,", "rgba(0,30,54,"
CSS_FILES = ["assets/css/s971fb819.css", "assets/css/sda808997.css"]
THEME_RE = re.compile(r'(<meta name="theme-color" content=")#1B3A5B(")', re.I)
CSSV_RE = re.compile(r'(href="/assets/css/s[0-9a-f]+\.css\?v=)10"')
INLINE_NAVY_RE = re.compile(r'--navy:\s*#1B3A5B;', re.I)
STROKE_OLD, STROKE_NEW = 'stroke="#2E7D52"', 'stroke="#016738"'

def sub_count(s, old, new):
    return s.replace(old, new), s.count(old)

def main(root):
    root = pathlib.Path(root); st = dict(css_navy=0, css_dark=0, css_ok=0, css_shadow=0, theme=0, cssv=0, inline=0, stroke=0, manifest=0, favicon=0)
    for rel in CSS_FILES:
        p = root / rel; s = p.read_text(encoding="utf-8"); s0 = s
        s, k = sub_count(s, f"--navy:{OLD_NAVY}", f"--navy:{NEW_NAVY}"); st["css_navy"] += k
        s, k = sub_count(s, f"--navy-dark:{OLD_NAVY_DARK}", f"--navy-dark:{NEW_NAVY_DARK}"); st["css_dark"] += k
        s, k = sub_count(s, f"--ok:{OLD_OK}", f"--ok:{NEW_OK}"); st["css_ok"] += k
        s, k = sub_count(s, OLD_SHADOW_RGB, NEW_SHADOW_RGB); st["css_shadow"] += k
        if s != s0: p.write_text(s, encoding="utf-8")
    pages = sorted(list(root.glob("*.html")) + list(root.glob("blog/*.html")))
    for p in pages:
        h = p.read_text(encoding="utf-8"); h0 = h
        h, k = THEME_RE.subn(lambda m: m.group(1) + NEW_NAVY + m.group(2), h); st["theme"] += k
        h, k = CSSV_RE.subn(lambda m: m.group(1) + '11"', h); st["cssv"] += k
        h, k = INLINE_NAVY_RE.subn(f"--navy:{NEW_NAVY};", h); st["inline"] += k
        for old, new in ((f"--navy-dark:{OLD_NAVY_DARK}", f"--navy-dark:{NEW_NAVY_DARK}"), (f"--ok:{OLD_OK}", f"--ok:{NEW_OK}"), (OLD_SHADOW_RGB, NEW_SHADOW_RGB)):
            h, k = sub_count(h, old, new); st["inline"] += k
        h, k = sub_count(h, STROKE_OLD, STROKE_NEW); st["stroke"] += k
        if h != h0: p.write_text(h, encoding="utf-8")
    m = root / "site.webmanifest"
    if m.exists():
        s = m.read_text(encoding="utf-8"); s2, k = sub_count(s, f'"theme_color": "{OLD_NAVY}"', f'"theme_color": "{NEW_NAVY}"'); st["manifest"] += k
        if k: m.write_text(s2, encoding="utf-8")
    f = root / "favicon.svg"
    if f.exists():
        s = f.read_text(encoding="utf-8"); s2, k = sub_count(s, f'fill="{OLD_NAVY}"', f'fill="{NEW_NAVY}"'); st["favicon"] += k
        if k: f.write_text(s2, encoding="utf-8")
    print("A. CSS : --navy", st["css_navy"], "· --navy-dark", st["css_dark"], "· --ok", st["css_ok"], "· ombres", st["css_shadow"], "(attendu 2/2/2/18 au premier passage)")
    print("B. pages : theme-color", st["theme"], "· ?v=11", st["cssv"], "(attendu 756/756)   C. inline --navy", st["inline"], "(attendu 1)")
    print("D. manifest", st["manifest"], "  E. favicon.svg", st["favicon"], "(attendu 1/1)   F. coches SVG", st["stroke"], "(attendu 7377)")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
