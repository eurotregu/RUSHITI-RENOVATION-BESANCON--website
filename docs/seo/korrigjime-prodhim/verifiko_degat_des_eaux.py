#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Outil de régression du silo « dégât des eaux » — dépôt de production
eurotregu/rushiti-renovation (audit du 24/08/2026).

À exécuter avant chaque déploiement touchant les pages degat-des-eaux-*.
Contrôle, sur les 76 pages du silo puis sur la page pilier :

  SILO   1. tous les blocs JSON-LD sont du JSON valide
         2. plus aucun doublon « mesure d'humidité, mesure de l'humidité »
         3. la barre d'appel mobile (.callbar) est présente
         4. Service + BreadcrumbList + FAQPage présents

  PILIER 5. plus de « mesure d'humidité de la fuite » (contresens métier)
         6. meta description ≤ 155 caractères et phrase terminée
         7. hasOfferCatalog présent, ≥ 4 offres
         8. bloc avis présent et rattaché au bon établissement Google (cid)
         9. les 6 ancres contextuelles du maillage sont posées
        10. parité FAQ : chaque <summary> a sa Question dans le FAQPage
        11. canonical, robots et title conformes

Sortie : 0 = conforme, 1 = au moins une erreur.
Les avertissements (KUJDES) ne font pas échouer le contrôle.

Usage :  python3 verifiko_degat_des_eaux.py /chemin/vers/checkout
"""
import html as htmllib
import json
import pathlib
import re
import sys

PILIER = "degat-des-eaux-besancon.html"
MAX_DESC = 155
CID = "cid=10915820577691168567"
ANCRES = [
    ("/devis-assurance-degat-des-eaux-besancon", "devis détaillé poste par poste"),
    ("/expert-assurance-sinistre-besancon", "passage de l'expert"),
    ("/blog/degat-des-eaux-assurance-qui-paie-quoi", "convention IRSI"),
    ("/remise-en-etat-logement-locatif-besancon", "bailleur"),
    ("/renovation-syndic-gestionnaire-besancon", "syndic de copropriété"),
    ("/blog/reparer-mur-degat-des-eaux-besancon", "murs et cloisons"),
]

erreurs: list[str] = []
alertes: list[str] = []


def err(f: str, msg: str) -> None:
    erreurs.append("%s : %s" % (f, msg))


def warn(f: str, msg: str) -> None:
    alertes.append("%s : %s" % (f, msg))


def blocs_jsonld(t: str) -> list[str]:
    return re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S)


def noeuds(t: str) -> list[dict]:
    out = []
    for b in blocs_jsonld(t):
        try:
            d = json.loads(b)
        except json.JSONDecodeError:
            continue
        out.extend(d.get("@graph", [d]) if isinstance(d, dict) else d)
    return [n for n in out if isinstance(n, dict)]


def types(n: dict) -> list[str]:
    v = n.get("@type", [])
    return v if isinstance(v, list) else [v]


def controle_silo(p: pathlib.Path) -> None:
    t = p.read_text(encoding="utf-8")
    f = p.name

    for i, b in enumerate(blocs_jsonld(t), 1):
        try:
            json.loads(b)
        except json.JSONDecodeError as e:
            err(f, "JSON-LD bloc %d invalide : %s" % (i, e))

    if re.search(r"mesure d[’']humidité, mesure de l[’']humidité", t):
        err(f, "doublon « mesure de l’humidité » dans le JSON-LD")

    if 'class="callbar"' not in t:
        warn(f, "barre d’appel mobile (.callbar) absente")

    présents = {ty for n in noeuds(t) for ty in types(n)}
    for attendu in ("Service", "BreadcrumbList", "FAQPage"):
        if attendu not in présents:
            err(f, "nœud JSON-LD %s absent" % attendu)


def controle_pilier(p: pathlib.Path) -> None:
    t = p.read_text(encoding="utf-8")
    f = p.name

    # 5 — contresens métier
    if re.search(r"mesure d[’']humidité de la fuite", t):
        err(f, "contresens : « mesure d’humidité de la fuite » (lire : recherche de la fuite)")

    # 6 — description
    m = re.search(r'<meta name="description" content="([^"]*)"', t)
    if not m:
        err(f, "meta description absente")
    else:
        d = m.group(1)
        if len(d) > MAX_DESC:
            err(f, "meta description %d car. (> %d)" % (len(d), MAX_DESC))
        if not d.rstrip().endswith((".", "!", "?")):
            err(f, "meta description non terminée : « …%s »" % d[-28:])

    # 7 — hasOfferCatalog
    svc = [n for n in noeuds(t) if "Service" in types(n)]
    if not svc:
        err(f, "nœud Service absent")
    else:
        cat = svc[0].get("hasOfferCatalog", {})
        items = cat.get("itemListElement", []) if isinstance(cat, dict) else []
        if len(items) < 4:
            err(f, "hasOfferCatalog absent ou < 4 offres (%d)" % len(items))

    # 8 — preuve
    if 'class="reviews"' not in t:
        err(f, "bloc avis clients absent")
    elif CID not in t:
        err(f, "bloc avis présent mais sans lien vers la fiche Google (%s)" % CID)

    # 9 — maillage
    corps = t.split("</head>")[-1]
    main = re.search(r"<main.*?</main>", corps, re.S)
    zone = main.group(0) if main else corps
    for url, texte in ANCRES:
        motif = re.compile(r'<a[^>]*href="%s"[^>]*>([^<]*)</a>' % re.escape(url))
        trouve = [a for a in motif.findall(zone) if texte in a]
        if not trouve:
            err(f, "ancre contextuelle manquante vers %s (« %s »)" % (url, texte))

    # 10 — parité FAQ visible / FAQPage
    vis = [re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>", "", s))).strip()
           for s in re.findall(r"<summary[^>]*>(.*?)</summary>", t, re.S)]
    faq = [n for n in noeuds(t) if "FAQPage" in types(n)]
    sch = []
    if faq:
        sch = [q.get("name", "") for q in faq[0].get("mainEntity", [])]
    manquants = [q for q in vis if q not in sch]
    orphelins = [q for q in sch if q not in vis]
    if manquants:
        err(f, "%d question(s) visible(s) absente(s) du FAQPage : %s"
            % (len(manquants), manquants[:2]))
    if orphelins:
        err(f, "%d question(s) du FAQPage sans équivalent visible : %s"
            % (len(orphelins), orphelins[:2]))

    # 11 — balises
    if 'rel="canonical" href="https://rushiti-renovation.fr/degat-des-eaux-besancon"' not in t:
        err(f, "canonical absente ou non conforme")
    if 'name="robots" content="index, follow"' not in t:
        warn(f, "meta robots « index, follow » absente")
    mt = re.search(r"<title>([^<]*)</title>", t)
    if mt and len(mt.group(1)) > 60:
        warn(f, "title %d car. (> 60)" % len(mt.group(1)))


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    racine = pathlib.Path(sys.argv[1])
    pages = sorted(racine.glob("degat-des-eaux-*.html"))
    if not pages:
        print("Aucune page degat-des-eaux-*.html sous %s" % racine)
        return 2

    for p in pages:
        controle_silo(p)
    pil = racine / PILIER
    if not pil.exists():
        err(PILIER, "page pilier absente")
    else:
        controle_pilier(pil)

    llms = racine / "llms.txt"
    if llms.exists() and "recherche d'origine" in llms.read_text(encoding="utf-8"):
        warn("llms.txt", "annonce « recherche d’origine » : prestation attribuée au "
                         "plombier ailleurs sur le site")

    print("Silo dégât des eaux : %d pages contrôlées" % len(pages))
    for a in alertes:
        print("  KUJDES  %s" % a)
    for e in erreurs:
        print("  ERREUR  %s" % e)
    print("\n%s — %d erreur(s), %d avertissement(s)"
          % ("CONFORME" if not erreurs else "NON CONFORME", len(erreurs), len(alertes)))
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
