#!/usr/bin/env python3
"""Mesure de différenciation des pages de grille /{service}-{zone} (03/09/2026).

Pour chaque page de grille, compare le texte du <main> (hors nav, footer, scripts)
avec : (1) la page du même service pour une zone « sœur » du même palier,
(2) la page pilier /{service}-besancon. Ratio = part des séquences de 5 mots
propres à la page. Écrit un CSV trié par palier puis ratio croissant.

Usage : python3 mesure_differenciation.py /chemin/vers/rushiti-renovation /chemin/inventaire-grille-paliers-2026-08.csv sortie.csv
"""
import csv, glob, html, os, re, sys
root, inv, out = sys.argv[1], sys.argv[2], sys.argv[3]
SERVICES = ["peinture-interieure","peinture-exterieure","papier-peint","toile-de-verre","ratissage-enduit","platrerie","cloisons","doublage-murs","faux-plafonds","revetements-sol","parquet-flottant","sol-pvc","lino-vinyle-lvt","vitrification-parquet","ragreage-sol","isolation-interieure","isolation","degat-des-eaux"]
palier = {r["zone"]: r["palier"] for r in csv.DictReader(open(inv, encoding="utf-8"), delimiter=";")}
def split(name):
    for s in sorted(SERVICES, key=len, reverse=True):
        if name.startswith(s + "-"): return s, name[len(s) + 1:]
    return None, None
def text(path):
    h = open(path, encoding="utf-8").read()
    m = re.search(r"<main.*?</main>", h, re.S); b = m.group(0) if m else h
    b = re.sub(r"<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", b, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", " ", b)); t = re.sub(r"\s+", " ", t).lower()
    return t
def grams(t, n=5):
    w = t.split(); return set(tuple(w[i:i+n]) for i in range(len(w) - n + 1)), len(w)
pages = {}
for p in glob.glob(os.path.join(root, "*.html")):
    s, z = split(os.path.basename(p)[:-5])
    if s: pages[(s, z)] = p
cache = {}
def G(key):
    if key not in cache: cache[key] = grams(text(pages[key]))
    return cache[key]
rows = []
for (s, z), p in pages.items():
    if z == "besancon": continue
    pal = palier.get(z, "?")
    g, n = G((s, z))
    sisters = sorted(zz for (ss, zz) in pages if ss == s and zz != z and zz != "besancon" and palier.get(zz) == pal)
    sis = sisters[0] if sisters else None
    if sis:
        gs, _ = G((s, sis)); r_sis = round(100 * len(g - gs) / max(1, len(g)))
    else: r_sis = ""
    if (s, "besancon") in pages:
        gp, _ = G((s, "besancon")); r_pil = round(100 * len(g - gp) / max(1, len(g)))
    else: r_pil = ""
    h = open(p, encoding="utf-8").read()
    faq = h.count("<details")
    rows.append({"page": "/" + s + "-" + z, "service": s, "zone": z, "palier": pal, "mots": n,
                 "zone_soeur": sis or "", "pct_unique_vs_soeur": r_sis, "pct_unique_vs_pilier": r_pil, "faq": faq})
rows.sort(key=lambda r: (r["palier"], r["pct_unique_vs_soeur"] if r["pct_unique_vs_soeur"] != "" else 999, r["page"]))
with open(out, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter=";"); w.writeheader(); w.writerows(rows)
import statistics
for pal in "ABC":
    v = [r["pct_unique_vs_soeur"] for r in rows if r["palier"] == pal and r["pct_unique_vs_soeur"] != ""]
    if v: print(f"palier {pal}: {len(v)} pages, unique vs sœur médiane {statistics.median(v)} %, min {min(v)} %, max {max(v)} %")
print("total pages de grille :", len(rows), "→", out)
