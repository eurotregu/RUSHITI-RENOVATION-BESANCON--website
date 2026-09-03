#!/usr/bin/env python3
"""Paketa 10 — corrections P0 visibles (03/09/2026), audit-premium-site-2026-09-03.md constats 3, 6, 7.

Usage, sur un checkout du dépôt de production eurotregu/rushiti-renovation :
    python3 fix_p0_visuel.py /chemin/vers/rushiti-renovation           # simulation
    python3 fix_p0_visuel.py /chemin/vers/rushiti-renovation --apply   # application

Idempotent. Quatre corrections :
  A. Bloc CTA final « Des murs à ratisser… » remplacé sur les 7 pages qui ne parlent pas de ratissage.
  B. Étoiles par avis (<div class="stars">★★★★★</div>) retirées : notes individuelles non relevées
     (doctrine avis-google-releve-2026-08-22.md) ; date du relevé ajoutée à la ligne de synthèse.
     Sur index.html, le tableau JSON-LD "review" (reviewRating 5 par avis, même donnée non relevée) est retiré.
  C. Bouton fantôme (.btn.ghost) illisible sur fond bleu nuit (.cta-band) : règle CSS de spécificité
     suffisante ajoutée aux deux feuilles ; version du cache CSS passée à ?v=9 sur toutes les pages.
  D. (rien : la double balise Google Fonts était un faux positif — motif media="print" + <noscript>).
"""
import os, re, sys, glob

CTA_OLD = ('<h2>Des murs à ratisser avant peinture à Besançon ?</h2><p>Décrivez-nous votre projet. '
           'Nous passons examiner vos murs en lumière rasante, et vous repartez avec un devis clair, '
           'détaillé et sans engagement.</p>')
CTA_NEW = {
    "amenagement-commerce-bureau-besancon.html":
        "<h2>Un commerce ou des bureaux à rénover à Besançon ?</h2><p>Décrivez-nous le local et vos "
        "contraintes d'ouverture. Nous passons le voir, et vous repartez avec un devis clair, détaillé et "
        "sans engagement.</p>",
    "devis-assurance-degat-des-eaux-besancon.html":
        "<h2>Un dégât des eaux à documenter pour votre assurance ?</h2><p>Décrivez-nous le sinistre : pièces "
        "touchées, date, état de la fuite. Nous passons gratuitement mesurer l'humidité, et vous recevez un "
        "devis détaillé pour votre dossier.</p>",
    "plaquiste-besancon.html":
        "<h2>Une cloison, un plafond ou un doublage à Besançon ?</h2><p>Décrivez-nous votre projet. Nous "
        "passons voir les supports, et vous repartez avec un devis clair, détaillé et sans engagement.</p>",
    "prix-travaux-renovation-besancon.html":
        "<h2>Un chantier à chiffrer à Besançon ?</h2><p>Décrivez-nous votre projet. Nous passons voir les "
        "lieux, et la fourchette devient un prix ferme, écrit dans un devis détaillé et sans engagement.</p>",
    "remise-en-etat-logement-locatif-besancon.html":
        "<h2>Un logement à relouer à Besançon ?</h2><p>Indiquez-nous l'adresse, le type de logement et la "
        "date de sortie du locataire. Nous passons le voir, et vous recevez un devis détaillé, sans "
        "engagement.</p>",
    "renovation-appartement-besancon.html":
        "<h2>Un appartement à rénover à Besançon ?</h2><p>Décrivez-nous votre appartement et votre projet. "
        "Nous passons voir les lieux, et vous repartez avec un devis clair, détaillé et sans engagement.</p>",
    "renovation-syndic-gestionnaire-besancon.html":
        "<h2>Un immeuble à remettre en état à Besançon ?</h2><p>Décrivez-nous l'immeuble et les travaux "
        "envisagés. Nous passons sur place, et vous recevez un devis détaillé poste par poste, présentable "
        "en conseil syndical.</p>",
}

STARS_CARD = '<div class="stars">★★★★★</div>'
SYNTH_OLD = '34 avis Google</a></p>'
SYNTH_NEW = '34 avis Google</a> · relevé le 22/08/2026</p>'
REVIEW_RE = re.compile(r',"review":\[\{"@type":"Review".*?\}\](?=[,}])', re.S)

CSS_MARK = "/*p0-ghost-cta*/"
CSS_RULE = (CSS_MARK + ".cta-band .btn.ghost,.btn.ghost.u6{color:#fff;border-color:rgba(255,255,255,.55)}"
            ".cta-band .btn.ghost:hover,.btn.ghost.u6:hover{color:#fff;background:rgba(255,255,255,.12);"
            "border-color:#fff;box-shadow:none}\n")
CSS_HREF_RE = re.compile(r'(href="/assets/css/s[0-9a-f]+\.css\?v=)[0-9]+"')
CSS_V = "9"


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    root = sys.argv[1]; apply = "--apply" in sys.argv
    pages = sorted(glob.glob(os.path.join(root, "*.html")) + glob.glob(os.path.join(root, "blog", "*.html")))
    stats = {"cta": 0, "stars_pages": 0, "stars_divs": 0, "synth": 0, "review": 0, "css_v": 0, "css_files": 0}
    touched = 0

    for p in pages:
        name = os.path.basename(p)
        h = open(p, encoding="utf-8").read(); h0 = h
        # A. CTA
        if name in CTA_NEW and CTA_OLD in h:
            h = h.replace(CTA_OLD, CTA_NEW[name]); stats["cta"] += 1
        # B. étoiles par avis + date du relevé
        n = h.count(STARS_CARD)
        if n:
            h = h.replace(STARS_CARD, ""); stats["stars_divs"] += n; stats["stars_pages"] += 1
        if SYNTH_OLD in h:
            h = h.replace(SYNTH_OLD, SYNTH_NEW); stats["synth"] += 1
        if name == "index.html":
            h, k = REVIEW_RE.subn("", h); stats["review"] += k
        # C. version CSS
        h, k = CSS_HREF_RE.subn(lambda m: m.group(1) + CSS_V + '"', h)
        if h != h0:
            if k and CSS_HREF_RE.sub(lambda m: m.group(1) + CSS_V + '"', h0) != h0: stats["css_v"] += 1
            touched += 1
            if apply:
                open(p, "w", encoding="utf-8").write(h)

    # C. règle CSS dans les deux feuilles
    for c in sorted(glob.glob(os.path.join(root, "assets", "css", "*.css"))):
        css = open(c, encoding="utf-8").read()
        if CSS_MARK in css: continue
        stats["css_files"] += 1; touched += 1
        if apply:
            open(c, "w", encoding="utf-8").write(css.rstrip("\n") + "\n" + CSS_RULE)

    print(("APPLIQUÉ" if apply else "SIMULATION") + f" — {touched} fichier(s) à modifier")
    print(f"  A. CTA remplacés : {stats['cta']} page(s) (attendu 7)")
    print(f"  B. étoiles par avis retirées : {stats['stars_divs']} bloc(s) sur {stats['stars_pages']} page(s) ; "
          f"date du relevé ajoutée : {stats['synth']} ; tableau review JSON-LD retiré : {stats['review']}")
    print(f"  C. version CSS passée à v={CSS_V} : {stats['css_v']} page(s) ; règle .btn.ghost ajoutée : {stats['css_files']} feuille(s)")


if __name__ == "__main__":
    main()
