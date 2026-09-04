#!/usr/bin/env python3
"""Paketa 12 — reste du plan d'action de l'audit du 03/09/2026 (constats 4 geo, 2/21 GTM-GA4, 16, 18, 20, 11, 17).

Usage, sur un checkout du dépôt de production eurotregu/rushiti-renovation :
    python3 fix_reste.py /chemin/vers/rushiti-renovation           # simulation
    python3 fix_reste.py /chemin/vers/rushiti-renovation --apply   # application

Idempotent. Corrections :
  A. geo du nœud LocalBusiness : centre-ville (47.238, 6.0243) → position BAN du 18 rue du Professeur Haag
     (47.245638, 6.00556 ; Base Adresse Nationale, id 25056_4260_00018, relevé 03/09/2026).
  B. Mentions légales : hébergeur Cloudflare, Inc. (adresse et contact DPO tels que publiés dans sa politique
     de confidentialité) ; section cookies : Google Analytics 4 (G-QER2M5L3GL, chargé par GTM après consentement)
     décrit ; commentaires « À VÉRIFIER » retirés.
  C. Bandeau de consentement (755 pages) : mentionne la mesure d'audience (Google Analytics) en plus de Meta.
  D. Piliers (16 pages) : les 12 groupes de communes du bloc « par quartier et dans le Doubs » repliés dans un
     <details> ; les 13 quartiers restent visibles ; tous les liens restent dans le HTML.
  E. sitemap.xml : lastmod = date du dernier commit git touchant le fichier ; changefreq et priority retirés.
  F. Accueil : « la Boucle du Doubs, le secteur Vauban » → « le centre ancien, dans la boucle du Doubs » ;
     « appartement de la Boucle » → « appartement du centre ancien » (noms géo canoniques du socle).
  G. Blog : « Mis à jour le … » affiché quand dateModified ≠ datePublished (3 articles).
  H. CSS : galerie en 2 colonnes sous 760 px ; cache CSS ?v=10.
"""
import glob, json, os, re, subprocess, sys, datetime

BASE = "https://rushiti-renovation.fr"
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

GEO_RE = re.compile(r'"geo":(\s*)\{"@type":(\s*)"GeoCoordinates",(\s*)"latitude":(\s*)47\.238,(\s*)"longitude":(\s*)6\.0243\}')
def fix_geo(h):
    return GEO_RE.subn(lambda m: f'"geo":{m.group(1)}{{"@type":{m.group(2)}"GeoCoordinates",{m.group(3)}"latitude":{m.group(4)}47.245638,{m.group(5)}"longitude":{m.group(6)}6.00556}}', h)

SEC3_OLD_RE = re.compile(r'<p>Le site est hébergé par <b>Cloudflare, Inc\.</b>.*?</p>\n<!-- \[À VÉRIFIER avant mise en ligne\] : coordonnées de l\'hébergeur[^>]*-->', re.S)
SEC3_NEW = ('<p>Le site est hébergé par <b>Cloudflare, Inc.</b> (service Cloudflare Pages) — 101 Townsend St, San Francisco, '
            'CA 94107, États-Unis — <a href="https://www.cloudflare.com/" rel="noopener">www.cloudflare.com</a> — '
            'contact protection des données : dpo@cloudflare.com. Le code source du site est déposé sur GitHub '
            '(GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis).</p>')
SEC7_OLD_RE = re.compile(r'<p><b>Google Tag Manager — gestionnaire de balises\.</b>.*?</p>\n<!-- \[À VÉRIFIER avant mise en ligne\] : lister ici[^>]*-->', re.S)
SEC7_NEW = ('<p><b>Google Analytics 4 — mesure d\'audience.</b> Outil de Google Ireland Ltd, chargé par le gestionnaire de balises '
            'Google Tag Manager. Il mesure la fréquentation du site (pages vues, clics sur le numéro de téléphone et l\'adresse '
            'e-mail, envois de formulaire) <strong>uniquement après votre consentement</strong> : tant que vous n\'avez pas accepté, '
            'aucun cookie Google n\'est déposé (Consent Mode v2). Les données sont traitées par Google conformément à sa politique '
            'de confidentialité.</p>')
def fix_mentions(h):
    n = 0
    h, k = SEC3_OLD_RE.subn(SEC3_NEW, h); n += k
    h, k = SEC7_OLD_RE.subn(SEC7_NEW, h); n += k
    old = "<p>Le site utilise trois outils, dans les conditions suivantes :</p>"
    if old in h: h = h.replace(old, "<p>Le site utilise trois outils, dans les conditions suivantes :</p>"); 
    return h, n

BANNER_OLD = ('Nous utilisons des cookies de mesure publicitaire (Meta) pour am\\u00e9liorer nos publicit\\u00e9s. '
              'Ils ne sont d\\u00e9pos\\u00e9s qu\\u2019avec votre accord.')
BANNER_NEW = ('Nous utilisons des cookies de mesure d\\u2019audience (Google Analytics) et de mesure publicitaire (Meta) '
              'pour comprendre l\\u2019usage du site et am\\u00e9liorer nos publicit\\u00e9s. Ils ne sont d\\u00e9pos\\u00e9s '
              'qu\\u2019avec votre accord.')

def fix_pilier_zones(h):
    if 'class="zones-more"' in h: return h, 0
    m = re.search(r'(par quartier et dans le Doubs</h2>.*?)(<h3 class="u30">.*?)(</div></div></section>)', h, re.S)
    if not m: return h, 0
    groups = m.group(2)
    n_links = len(re.findall(r'<a href="/', groups))
    wrapped = f'<details class="zones-more"><summary>Voir toutes les communes du Doubs où nous intervenons ({n_links})</summary>{groups}</details>'
    return h[:m.start(2)] + wrapped + h[m.end(2):], 1

HOME_REPL = [("un cœur historique classé — la Boucle du Doubs, le secteur Vauban — et", "un cœur historique classé — le centre ancien, dans la boucle du Doubs — et"),
             ("Un appartement de la Boucle présente", "Un appartement du centre ancien présente")]

def fix_blog_maj(h):
    p = re.search(r'"datePublished":"(\d{4}-\d{2}-\d{2})"', h); d = re.search(r'"dateModified":"(\d{4}-\d{2}-\d{2})"', h)
    if not p or not d or p.group(1) == d.group(1) or "Mis à jour le" in h: return h, 0
    y, mo, da = d.group(1).split("-"); txt = f"{int(da)} {MOIS[int(mo) - 1]} {y}"
    h2 = re.sub(r'(<div class="meta-row">.*?)(</div>)', lambda m: m.group(1) + f'<span>·</span><span>Mis à jour le {txt}</span>' + m.group(2), h, count=1, flags=re.S)
    return h2, int(h2 != h)

CSS_MARK = "/*p12*/"
CSS_RULE = (CSS_MARK + ".zones-more{margin-top:14px}.zones-more>summary{cursor:pointer;font-weight:700;color:var(--navy);padding:8px 0}"
            "@media(max-width:760px){.gallery{grid-template-columns:1fr 1fr;gap:10px}.gallery figcaption .cap{font-size:.85rem}}\n")
CSS_HREF_RE = re.compile(r'(href="/assets/css/s[0-9a-f]+\.css\?v=)[0-9]+"')

def sitemap(root, apply):
    p = os.path.join(root, "sitemap.xml"); x = open(p, encoding="utf-8").read()
    locs = re.findall(r"<loc>(.*?)</loc>", x)
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in locs:
        path = u.replace(BASE, "").lstrip("/") or "index"
        f = path + ".html"
        try:
            d = subprocess.check_output(["git", "-C", root, "log", "-1", "--format=%cs", "--", f], text=True).strip()
        except Exception:
            d = ""
        if not d: d = datetime.date.today().isoformat()
        out.append(f"  <url><loc>{u}</loc><lastmod>{d}</lastmod></url>")
    out.append("</urlset>\n")
    new = "\n".join(out)
    if new != x and apply: open(p, "w", encoding="utf-8").write(new)
    return int(new != x), len(locs)

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    root = sys.argv[1]; apply = "--apply" in sys.argv
    pages = sorted(glob.glob(os.path.join(root, "*.html")) + glob.glob(os.path.join(root, "blog", "*.html")))
    st = dict(geo=0, mentions=0, banner=0, piliers=0, home=0, blog=0, cssv=0, css=0); touched = 0
    for p in pages:
        name = os.path.basename(p); h = open(p, encoding="utf-8").read(); h0 = h
        h, k = fix_geo(h); st["geo"] += k
        if name == "mentions-legales.html": h, k = fix_mentions(h); st["mentions"] += k
        if BANNER_OLD in h: h = h.replace(BANNER_OLD, BANNER_NEW); st["banner"] += 1
        if name.endswith("-besancon.html"): h, k = fix_pilier_zones(h); st["piliers"] += k
        if name == "index.html":
            for a, b in HOME_REPL:
                if a in h: h = h.replace(a, b); st["home"] += 1
        if p.replace("\\", "/").split("/")[-2] == "blog": h, k = fix_blog_maj(h); st["blog"] += k
        h, k = CSS_HREF_RE.subn(lambda m: m.group(1) + '10"', h)
        if k and CSS_HREF_RE.sub(lambda m: m.group(1) + '10"', h0) != h0: st["cssv"] += 1
        if h != h0:
            touched += 1
            if apply: open(p, "w", encoding="utf-8").write(h)
    for c in sorted(glob.glob(os.path.join(root, "assets", "css", "*.css"))):
        css = open(c, encoding="utf-8").read()
        if CSS_MARK in css: continue
        st["css"] += 1; touched += 1
        if apply: open(c, "w", encoding="utf-8").write(css.rstrip("\n") + "\n" + CSS_RULE)
    sm, nloc = sitemap(root, apply); touched += sm
    print(("APPLIQUÉ" if apply else "SIMULATION") + f" — {touched} fichier(s)")
    print(f"  A. geo corrigé : {st['geo']} nœud(s)   B. mentions légales : {st['mentions']} bloc(s) (attendu 2)   C. bandeau : {st['banner']} page(s)")
    print(f"  D. piliers repliés : {st['piliers']} (attendu 16)   E. sitemap : {'réécrit' if sm else 'inchangé'} ({nloc} URL)   F. accueil : {st['home']} (attendu 2)")
    print(f"  G. blog « Mis à jour le » : {st['blog']} (attendu 3)   H. CSS règle : {st['css']} feuille(s), version v=10 : {st['cssv']} page(s)")

if __name__ == "__main__":
    main()
