#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renforcement du silo « dégât des eaux » — dépôt de production
eurotregu/rushiti-renovation (audit de la page pilier du 24/08/2026).

Constat de départ : la page pilier /degat-des-eaux-besancon est le seul actif
du silo à ne PAS avoir reçu les deux enrichissements appliqués aux 75 pages de
la grille (hasOfferCatalog + bloc avis Google), et elle porte trois séquelles
d'un remplacement global « recherche de fuite » → « mesure d'humidité ».

Ce que le script fait, dans l'ordre :

  A. SILO (76 pages degat-des-eaux-*.html)
     JSON-LD Service : « mesure d'humidité, mesure de l'humidité, assèchement »
                     → « mesure d'humidité, assèchement »  (doublon)

  B. PILIER (/degat-des-eaux-besancon uniquement)
     B1  corps : « Une prestation n'entre pas dans notre périmètre : la mesure
         d'humidité de la fuite » → « la recherche de la fuite »
         (la phrase actuelle contredit la section « Notre méthode », qui
          annonce précisément la mesure d'humidité comme prestation)
     B2  meta description + og:description : phrase tronquée « devis conforme »
         → « devis pour votre assurance. » (≤ 155 caractères)
     B3  JSON-LD Service : ajout de hasOfferCatalog (présent sur 75/75 pages de
         la grille, absent du pilier)
     B4  ajout du bloc « Avis clients » (4,7/5 · 34 avis Google + 3 avis),
         repris à l'identique de la grille, inséré avant la FAQ comme sur les
         pages de zone
     B5  maillage interne : 6 ancres contextuelles dans <main> vers les
         satellites du silo (devis assurance, expert, syndic, locatif, IRSI,
         réparation de mur)
     B6  chapeau (<p class="lead">) réécrit en réponse directe — extractibilité
         par les moteurs de réponse. Aucun fait nouveau : mêmes prestations,
         mêmes engagements, ordre inversé.

  C. llms.txt : la ligne dégât des eaux annonce « recherche d'origine », que le
     site attribue par ailleurs au plombier (/devis-assurance-… et
     /expert-assurance-…). Alignement sur le positionnement réel.

  D. (option --cta) barre d'appel mobile du PILIER uniquement :
     « Devis gratuit » → « Devis assurance ». La barre existe déjà sur les 76
     pages du silo ; les 75 pages de la grille portent « Diagnostic gratuit »
     et ne sont pas touchées — harmoniser tout le silo est un arbitrage
     éditorial qui revient à Isuf. Hors --cta, rien n'est modifié ici.

Le script est idempotent : une page déjà corrigée est ignorée.
Aucun prix, délai ni avis n'est inventé : le bloc avis et la note 4,7/5
proviennent des pages de la grille déjà en production (relevé Google du
22/08/2026), le devis gratuit est déjà annoncé sur la page.

Usage :  python3 fix_degat_des_eaux.py /chemin/vers/checkout [--apply] [--cta]
         (sans --apply : simulation, rien n'est écrit)
"""
import json
import pathlib
import re
import sys

PILIER = "degat-des-eaux-besancon.html"
MAX_DESC = 155

# ---------------------------------------------------------------- A. silo
DOUBLON_AV = "mesure d’humidité, mesure de l'humidité, assèchement"
DOUBLON_AP = "mesure d’humidité, assèchement"

# ---------------------------------------------------------------- B. pilier
FUITE_AV = "Une prestation n'entre pas dans notre périmètre : la mesure d’humidité de la fuite."
FUITE_AP = "Une prestation n'entre pas dans notre périmètre : la recherche de la fuite."

DESC_AV = ("Dégât des eaux à Besançon (25) : mesure d’humidité, assèchement, "
           "traitement anti-moisissure et réfection. Diagnostic gratuit, devis conforme")
DESC_AP = ("Dégât des eaux à Besançon (25) : mesure d’humidité, assèchement, "
           "traitement anti-moisissure et réfection. Diagnostic gratuit, devis assurance.")

OFFRES = [
    "Diagnostic et mesure du taux d’humidité",
    "Assèchement et séchage des supports",
    "Traitement anti-moisissure et antifongique",
    "Réfection plâtrerie, placo et peinture",
    "Devis détaillé pour votre dossier d’assurance",
]
ANCRE_OFFRE = ('"areaServed":[{"@type":"City","name":"Besançon"},'
               '{"@type":"AdministrativeArea","name":"Doubs"}]},'
               '{"@type":"BreadcrumbList"')

AVIS_HTML = (
    '<section class="soft"><div class="wrap"><span class="eyebrow">Avis clients</span>'
    '<h2>Ils nous ont fait confiance</h2><p class="u27"><b>4,7 / 5</b> '
    '<span class="u5">★★★★★</span> · <a class="u11" '
    'href="https://www.google.com/maps?cid=10915820577691168567" target="_blank" '
    'rel="noopener">34 avis Google</a></p><div class="reviews">'
    '<div class="review"><div class="stars">★★★★★</div><p>« Nous avons fait appel à '
    "l'entreprise Rushiti pour repeindre entièrement un appartement et refaire les "
    'sols. Le travail est très soigné et a été réalisé rapidement. M. Rushiti est '
    'accessible et courtois. »</p><div class="who">Jérôme J. · Avis Google</div></div>'
    '<div class="review"><div class="stars">★★★★★</div><p>« Repeinte complète de notre '
    'appartement : nous sommes entièrement satisfaits. Dès le début, la communication '
    'a été excellente et il a su répondre à toutes nos questions. »</p>'
    '<div class="who">Marie B. · Avis Google</div></div>'
    '<div class="review"><div class="stars">★★★★★</div><p>« Recommandés par des amis '
    "très contents : nous n'avons pas été déçus. On ne pouvait pas espérer de "
    'meilleurs résultats. »</p><div class="who">Michel R. · Avis Google</div></div>'
    '</div></div></section>\n'
)
ANCRE_AVIS = ('<section class="soft"><div class="wrap">'
              '<span class="eyebrow">Questions fréquentes</span><h2>Vos questions</h2>')

LEAD_AV = ('<p class="lead">Après un dégât des eaux à Besançon ou dans le Doubs, le piège '
           'est de réparer ce qui se voit. RUSHITI Rénovation mesure l’humidité et traite '
           "l'étendue réelle — murs, sols et isolation — avant toute réfection. "
           'Diagnostic gratuit, devis conforme à votre assurance.</p>')
LEAD_AP = ('<p class="lead">RUSHITI Rénovation remet en état les logements touchés par un '
           'dégât des eaux à Besançon et dans le Doubs : mesure du taux d’humidité, '
           'assèchement, traitement anti-moisissure, puis réfection de la plâtrerie, de la '
           'peinture et des sols. Diagnostic gratuit sur place et devis détaillé pour votre '
           "assurance. Le piège à éviter : réparer ce qui se voit, alors que l'eau a migré "
           'dans les murs, les sols et l’isolation.</p>')

# maillage interne : (texte à ancrer, url, contexte unique de contrôle)
LIENS = [
    ("un devis détaillé poste par poste",
     "/devis-assurance-degat-des-eaux-besancon",
     "nous établissons un devis détaillé poste par poste"),
    ("lors du passage de l'expert",
     "/expert-assurance-sinistre-besancon",
     "nous sommes présents lors du passage de l'expert si vous le souhaitez"),
    ("la convention IRSI",
     "/blog/degat-des-eaux-assurance-qui-paie-quoi",
     "souvent la convention IRSI lorsque plusieurs logements"),
    ("bailleur",
     "/remise-en-etat-logement-locatif-besancon",
     "que vous soyez particulier, bailleur, ou que le sinistre"),
    ("un syndic de copropriété ou un gestionnaire de biens",
     "/renovation-syndic-gestionnaire-besancon",
     "passe par un syndic de copropriété ou un gestionnaire de biens"),
    ("les murs et cloisons touchés",
     "/blog/reparer-mur-degat-des-eaux-besancon",
     "la dépose des placo et isolants perdus"),
]
# le 6e lien n'a pas de texte hôte existant : il est greffé sur une formulation
# de la section « Notre périmètre » (voir MUR_AV / MUR_AP)
MUR_AV = ("nos travaux de remise en état couvrent la dépose des placo et isolants perdus,")
MUR_AP = ("nos travaux de remise en état couvrent la dépose des placo et isolants perdus "
          'sur les <a href="/blog/reparer-mur-degat-des-eaux-besancon">murs et cloisons '
          "touchés</a>,")

CTA_AV = '<a class="btn ghost" href="/contact">Devis gratuit</a></div>'
CTA_AP = '<a class="btn ghost" href="/contact">Devis assurance</a></div>'

LLMS_AV = ("- [Réparation après dégât des eaux](https://rushiti-renovation.fr/"
           "degat-des-eaux-besancon) : recherche d'origine, assèchement,")
LLMS_AP = ("- [Réparation après dégât des eaux](https://rushiti-renovation.fr/"
           "degat-des-eaux-besancon) : mesure du taux d'humidité, assèchement,")


def offer_catalog() -> str:
    items = ",".join(
        '{"@type":"Offer","itemOffered":{"@type":"Service","name":"%s"}}' % o
        for o in OFFRES
    )
    return ('"hasOfferCatalog":{"@type":"OfferCatalog","name":"Prestations après dégât '
            'des eaux","itemListElement":[%s]},' % items)


def lien_html(texte: str, url: str) -> str:
    return '<a href="%s">%s</a>' % (url, texte)


def fix_silo(path: pathlib.Path) -> list[str]:
    """A — doublon JSON-LD, applicable aux 76 pages du silo."""
    html = path.read_text(encoding="utf-8")
    if DOUBLON_AV not in html:
        return []
    n = html.count(DOUBLON_AV)
    path.write_text(html.replace(DOUBLON_AV, DOUBLON_AP), encoding="utf-8") \
        if FIX_APPLY else None
    return ["JSON-LD : doublon « mesure de l’humidité » supprimé (×%d)" % n]


def fix_pilier(path: pathlib.Path) -> list[str]:
    html = path.read_text(encoding="utf-8")
    orig = html
    ch: list[str] = []

    # B1 — recherche de fuite
    if FUITE_AV in html:
        html = html.replace(FUITE_AV, FUITE_AP)
        ch.append("corps : « mesure d’humidité de la fuite » → « recherche de la fuite »")

    # B2 — description tronquée (meta + og)
    if DESC_AV in html:
        n = html.count(DESC_AV)
        html = html.replace(DESC_AV, DESC_AP)
        ch.append("description : phrase complétée, %d car. (×%d)" % (len(DESC_AP), n))

    # B3 — hasOfferCatalog
    if "hasOfferCatalog" not in html and ANCRE_OFFRE in html:
        remplacement = ANCRE_OFFRE.replace(
            '"areaServed"', offer_catalog() + '"areaServed"', 1)
        html = html.replace(ANCRE_OFFRE, remplacement, 1)
        ch.append("JSON-LD : hasOfferCatalog ajouté (%d offres)" % len(OFFRES))

    # B4 — bloc avis
    if 'class="reviews"' not in html and ANCRE_AVIS in html:
        html = html.replace(ANCRE_AVIS, AVIS_HTML + ANCRE_AVIS, 1)
        ch.append("bloc « Avis clients » (4,7/5 · 34 avis Google) inséré avant la FAQ")

    # B5 — maillage interne
    for texte, url, contexte in LIENS[:-1]:
        if lien_html(texte, url) in html:   # idempotence : ancre déjà posée
            continue
        if contexte not in html:
            ch.append("ATTENTION : contexte introuvable pour %s" % url)
            continue
        html = html.replace(contexte, contexte.replace(texte, lien_html(texte, url), 1), 1)
        ch.append("maillage : « %s » → %s" % (texte, url))
    if MUR_AV in html:
        html = html.replace(MUR_AV, MUR_AP, 1)
        ch.append("maillage : « murs et cloisons touchés » → /blog/reparer-mur-…")

    # B6 — chapeau en réponse directe
    if LEAD_AV in html:
        html = html.replace(LEAD_AV, LEAD_AP, 1)
        ch.append("chapeau réécrit en réponse directe (GEO)")

    if html != orig and FIX_APPLY:
        path.write_text(html, encoding="utf-8")
    return ch


def fix_cta(path: pathlib.Path) -> list[str]:
    html = path.read_text(encoding="utf-8")
    if CTA_AV not in html:
        return []
    if FIX_APPLY:
        path.write_text(html.replace(CTA_AV, CTA_AP), encoding="utf-8")
    return ["barre d’appel : « Devis gratuit » → « Devis assurance »"]


def fix_llms(path: pathlib.Path) -> list[str]:
    if not path.exists():
        return []
    txt = path.read_text(encoding="utf-8")
    if LLMS_AV not in txt:
        return []
    if FIX_APPLY:
        path.write_text(txt.replace(LLMS_AV, LLMS_AP), encoding="utf-8")
    return ["llms.txt : « recherche d’origine » → « mesure du taux d’humidité »"]


def controle_json(path: pathlib.Path) -> list[str]:
    """Relit tous les blocs JSON-LD du fichier et signale les invalides."""
    html = path.read_text(encoding="utf-8")
    pbs = []
    for i, m in enumerate(re.finditer(
            r'<script type="application/ld\+json">(.*?)</script>', html, re.S), 1):
        try:
            json.loads(m.group(1))
        except json.JSONDecodeError as e:
            pbs.append("JSON-LD bloc %d invalide : %s" % (i, e))
    return pbs


FIX_APPLY = False


def main() -> int:
    global FIX_APPLY
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    racine = pathlib.Path(args[0])
    FIX_APPLY = "--apply" in sys.argv
    cta = "--cta" in sys.argv
    if not racine.is_dir():
        print("Répertoire introuvable : %s" % racine)
        return 2

    pages = sorted(racine.glob("degat-des-eaux-*.html"))
    if not pages:
        print("Aucune page degat-des-eaux-*.html sous %s" % racine)
        return 2

    total = 0
    for p in pages:
        ch = fix_silo(p)
        if p.name == PILIER:
            ch += fix_pilier(p)
        if cta and p.name == PILIER:
            ch += fix_cta(p)
        if ch:
            total += 1
            print("• %s" % p.name)
            for c in ch:
                print("    - %s" % c)

    ch = fix_llms(racine / "llms.txt")
    if ch:
        total += 1
        print("• llms.txt")
        for c in ch:
            print("    - %s" % c)

    if FIX_APPLY:
        pbs = controle_json(racine / PILIER)
        for pb in pbs:
            print("!! %s" % pb)
        if pbs:
            return 1

    print("\n%s : %d fichier(s) %s" % (
        "APPLIQUÉ" if FIX_APPLY else "SIMULATION",
        total,
        "modifié(s)" if FIX_APPLY else "à modifier"))
    if not FIX_APPLY:
        print("Relancer avec --apply pour écrire.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
