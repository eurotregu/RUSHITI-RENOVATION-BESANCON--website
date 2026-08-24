#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cohérence des horaires (NAP) — dépôt de production eurotregu/rushiti-renovation.

Constat du 24/08/2026, confirmé par Isuf : les horaires réels sont
**7 h – 20 h 30 en semaine, 8 h – 20 h 30 le samedi, 9 h – 17 h 30 le dimanche**,
soit 7 jours sur 7. Le site en annonçait deux versions contradictoires.

Ce que le script corrige :

  A. contact.html — le bloc « Horaires » affiche « Lundi – Vendredi : 8h – 18h »,
     alors que le pied de page des 755 pages annonce 7 h – 20 h 30, 7 j/7, et que
     le JSON-LD de 153 pages déclare la version longue. Un visiteur de /contact
     lit deux horaires opposés sur la même page.

  B. openingHoursSpecification — 586 pages portent un nœud LocalBusiness complet
     (adresse + téléphone) SANS horaires, alors que 153 les déclarent. Un moteur
     qui fusionne le graphe par @id voit une entité aux horaires incohérents
     selon la page d'entrée. Le bloc est inséré après "priceRange", à
     l'identique de celui déjà en production.

  C. Page pilier dégât des eaux — le nœud Service gagne "url" et
     "availableChannel" (canal téléphone + page de contact) : c'est ce qu'un
     moteur de réponse lit pour indiquer comment joindre l'entreprise sur une
     recherche d'urgence.

Ce que le script NE fait PAS, volontairement :

  - aucun "geo" : les coordonnées exactes du 18 rue du Professeur Haag doivent
    être relevées sur la fiche Google, pas devinées ;
  - aucun "aggregateRating" : la politique de Google sur les données
    structurées écarte les avis auto-publiés pour LocalBusiness — le balisage
    n'apporterait pas d'étoiles ;
  - aucune diversification des ancres vers la page pilier : sur les 150 liens,
    75 sont des fils d'Ariane (ils doivent refléter le BreadcrumbList) et 75
    sont des puces courtes dans une rangée de libellés de quartier. Les allonger
    casserait l'un ou l'autre.

Le script est idempotent : une page déjà corrigée est ignorée.

Usage :  python3 fix_horaires_nap.py /chemin/vers/checkout [--apply]
         (sans --apply : simulation, rien n'est écrit)
"""
import json
import pathlib
import re
import sys

PILIER = "degat-des-eaux-besancon.html"

# ------------------------------------------------------------------ A. contact
HORAIRES_AV = "<b>Horaires</b>Lundi – Vendredi : 8h – 18h"
HORAIRES_AP = ("<b>Horaires</b>Lundi – Vendredi : 7h – 20h30<br>"
               "Samedi : 8h – 20h30<br>Dimanche : 9h – 17h30")

# ------------------------------------------------------------------ B. JSON-LD
HORAIRES_JSONLD = (
    '"openingHoursSpecification":[{"@type":"OpeningHoursSpecification",'
    '"dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],'
    '"opens":"07:00","closes":"20:30"},'
    '{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday",'
    '"opens":"08:00","closes":"20:30"},'
    '{"@type":"OpeningHoursSpecification","dayOfWeek":"Sunday",'
    '"opens":"09:00","closes":"17:30"}],'
)
# le format d'écriture varie en production : avec ou sans espace après ':'
PRICE_RANGE = re.compile(r'("priceRange":\s*"€€",)')

# ------------------------------------------------------------------ C. Service
SERVICE_AV = '"provider":{"@id":"https://rushiti-renovation.fr/#business"},'
SERVICE_AP = (
    '"provider":{"@id":"https://rushiti-renovation.fr/#business"},'
    '"url":"https://rushiti-renovation.fr/degat-des-eaux-besancon",'
    '"availableChannel":[{"@type":"ServiceChannel",'
    '"servicePhone":{"@type":"ContactPoint","telephone":"+33760279897",'
    '"contactType":"customer service","areaServed":"FR","availableLanguage":"French"}},'
    '{"@type":"ServiceChannel",'
    '"serviceUrl":"https://rushiti-renovation.fr/degat-des-eaux-besancon#demande-rapide"}],'
)

FIX_APPLY = False


def noeuds_biz(html: str) -> list:
    """Nœuds LocalBusiness complets (adresse ou téléphone présents)."""
    out = []
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                        html, re.S):
        try:
            d = json.loads(b)
        except json.JSONDecodeError:
            continue
        for n in (d.get("@graph", [d]) if isinstance(d, dict) else d):
            if not isinstance(n, dict):
                continue
            if "LocalBusiness" in str(n.get("@type", "")) and (
                    "address" in n or "telephone" in n):
                out.append(n)
    return out


def fix_page(path: pathlib.Path) -> list[str]:
    html = path.read_text(encoding="utf-8")
    orig = html
    ch: list[str] = []

    # A — texte visible de /contact
    if path.name == "contact.html" and HORAIRES_AV in html:
        html = html.replace(HORAIRES_AV, HORAIRES_AP)
        ch.append("texte : « Lun–Ven 8h–18h » → horaires réels 7 j/7")

    # B — horaires dans le nœud LocalBusiness complet
    biz = noeuds_biz(html)
    if biz and not any("openingHoursSpecification" in n for n in biz):
        html, n = PRICE_RANGE.subn(lambda m: m.group(1) + HORAIRES_JSONLD,
                                   html, count=1)
        if n:
            ch.append("JSON-LD : openingHoursSpecification ajouté")
        else:
            ch.append("ATTENTION : point d’insertion « priceRange » introuvable")

    # C — enrichissement du nœud Service du pilier
    if path.name == PILIER and SERVICE_AV in html and '"availableChannel"' not in html:
        html = html.replace(SERVICE_AV, SERVICE_AP, 1)
        ch.append("JSON-LD : Service → url + availableChannel (téléphone, formulaire)")

    if html != orig:
        # garde-fou : le JSON doit rester valide, sinon on n’écrit pas
        for i, b in enumerate(re.findall(
                r'<script type="application/ld\+json">(.*?)</script>', html, re.S), 1):
            try:
                json.loads(b)
            except json.JSONDecodeError as e:
                return ["ERREUR : JSON-LD bloc %d invalide après correction (%s) "
                        "— fichier NON modifié" % (i, e)]
        if FIX_APPLY:
            path.write_text(html, encoding="utf-8")
    return ch


def main() -> int:
    global FIX_APPLY
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    racine = pathlib.Path(args[0])
    FIX_APPLY = "--apply" in sys.argv
    if not racine.is_dir():
        print("Répertoire introuvable : %s" % racine)
        return 2

    pages = sorted(racine.rglob("*.html"))
    if not pages:
        print("Aucune page HTML sous %s" % racine)
        return 2

    total = 0
    erreurs = 0
    resume: dict[str, int] = {}
    for p in pages:
        ch = fix_page(p)
        if not ch:
            continue
        total += 1
        for c in ch:
            cle = c.split(" :")[0]
            resume[cle] = resume.get(cle, 0) + 1
            if c.startswith("ERREUR") or c.startswith("ATTENTION"):
                erreurs += 1
                print("!! %s : %s" % (p.name, c))

    print("\n%s" % ("APPLIQUÉ" if FIX_APPLY else "SIMULATION"))
    for k, v in sorted(resume.items(), key=lambda x: -x[1]):
        print("  %-14s %d fichier(s)" % (k, v))
    print("  %s : %d fichier(s)" % (
        "total modifié" if FIX_APPLY else "total à modifier", total))
    if not FIX_APPLY:
        print("Relancer avec --apply pour écrire.")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
