#!/usr/bin/env python3
"""Paketa 9 — llms.txt + mentions-legales.html (03/09/2026).

Usage, sur un checkout du dépôt de production eurotregu/rushiti-renovation :
    python3 fix_llms_mentions.py /chemin/vers/rushiti-renovation           # simulation
    python3 fix_llms_mentions.py /chemin/vers/rushiti-renovation --apply   # application

Idempotent : une page déjà corrigée ne change plus (0 remplacement).
- llms.txt : remplacé intégralement par le llms.txt de ce dossier.
- mentions-legales.html : sections 1, 2, 3, 7 et date de mise à jour réécrites.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# --- Blocs cibles (HTML) ------------------------------------------------------
SEC1_OLD = re.compile(
    r"<p><b>RUSHITI Rénovation</b><br>\s*Forme juridique : SARL \(société à responsabilité limitée\)<br>\s*"
    r"Capital social : 1 000 €<br>\s*Siège social : 18 rue du Professeur Haag, 25000 Besançon, France<br>\s*"
    r"SIRET : 905 214 631 00012<br>\s*TVA intracommunautaire : FR89 905 214 631<br>\s*"
    r"Téléphone : 07 60 27 98 97<br>\s*E-mail : contact@rushiti-renovation.fr<br>\s*"
    r"Co-gérants : Isuf Rushiti et Yll Rushiti</p>", re.S)
SEC1_NEW = (
    "<p><b>Rushiti</b>, société à responsabilité limitée (SARL) au capital de 1 000 €, "
    "exerçant sous le nom commercial <b>RUSHITI Rénovation</b><br>\n"
    "RCS Besançon 905 214 631<br>\n"
    "Siège social : 18 rue du Professeur Haag, 25000 Besançon, France<br>\n"
    "SIRET : 905 214 631 00012<br>\n"
    "TVA intracommunautaire : FR89 905 214 631<br>\n"
    "Téléphone : 07 60 27 98 97<br>\n"
    "E-mail : contact@rushiti-renovation.fr<br>\n"
    "Co-gérants : Isuf Rushiti et Yll Rushiti</p>")

SEC2_OLD = ("<p>Le directeur de la publication est M. Isuf Rushiti, en qualité de représentant légal "
            "de RUSHITI Rénovation.</p>")
SEC2_NEW = ("<p>Le directeur de la publication est M. Isuf Rushiti, co-gérant, en qualité de représentant "
            "légal de la SARL Rushiti (RUSHITI Rénovation).</p>")

SEC3_OLD = ("<p>Le site est hébergé par RUSHITI Rénovation — 18 rue du Professeur Haag, 25000 Besançon, "
            "France — tél. 07 60 27 98 97.</p>")
SEC3_NEW = (
    "<p>Le site est hébergé par <b>Cloudflare, Inc.</b> (service Cloudflare Pages) — "
    "101 Townsend Street, San Francisco, CA 94107, États-Unis — "
    "<a href=\"https://www.cloudflare.com/\" rel=\"noopener\">www.cloudflare.com</a>. "
    "Le code source du site est déposé sur GitHub (GitHub, Inc., 88 Colin P. Kelly Jr. Street, "
    "San Francisco, CA 94107, États-Unis).</p>\n"
    "<!-- [À VÉRIFIER avant mise en ligne] : coordonnées de l'hébergeur telles qu'indiquées dans les "
    "conditions Cloudflare en vigueur ; supprimer la phrase GitHub si le dépôt n'est plus la source du déploiement. -->")

SEC7_OLD = re.compile(
    r"<p>Le site utilise un seul traceur : le Pixel Meta \(Facebook / Instagram\).*?"
    r"Le site n'utilise aucun autre cookie de suivi ni de mesure d'audience\.</p>", re.S)
SEC7_NEW = (
    "<p>Le site utilise trois outils, dans les conditions suivantes :</p>\n"
    "<p><b>Pixel Meta (Facebook / Instagram) — publicité.</b> Il mesure l'efficacité de nos campagnes "
    "publicitaires et permet de proposer des annonces pertinentes aux personnes ayant consulté le site. "
    "Il n'est chargé et ne dépose de cookie <strong>qu'après votre consentement explicite</strong>, recueilli "
    "via le bandeau affiché lors de votre première visite. Si vous cliquez sur « Refuser », aucun cookie "
    "publicitaire n'est déposé et le site reste pleinement utilisable. Les données collectées sont traitées "
    "par Meta Platforms Ireland Ltd conformément à sa politique de confidentialité.</p>\n"
    "<p><b>Google Tag Manager — gestionnaire de balises.</b> Cet outil (Google Ireland Ltd) sert à charger "
    "les balises du site de façon centralisée. Il ne dépose aucun cookie par lui-même ; les balises qu'il "
    "pilote respectent votre choix de consentement (Consent Mode v2) : tant que vous n'avez pas accepté, "
    "les stockages publicitaires et d'analyse restent refusés.</p>\n"
    "<!-- [À VÉRIFIER avant mise en ligne] : lister ici les balises réellement présentes dans le conteneur "
    "GTM-KPM3GQB6 (ex. Google Analytics 4). Si une balise de mesure d'audience y est active, l'indiquer "
    "dans ce paragraphe ET dans le texte du bandeau de consentement. -->\n"
    "<p><b>Cloudflare Web Analytics — mesure d'audience sans cookie.</b> Statistiques de fréquentation "
    "agrégées, sans cookie ni identifiant individuel, exemptées de consentement au sens des lignes "
    "directrices de la CNIL.</p>\n"
    "<p>Vous pouvez modifier votre choix à tout moment via le lien « Gérer mes cookies » en pied de page, "
    "qui affiche à nouveau le bandeau.</p>")

DATE_OLD = "Dernière mise à jour : août 2026"
DATE_NEW = "Dernière mise à jour : septembre 2026"

LEAD_OLD = ("Informations légales relatives au site rushiti-renovation.fr et à l'entreprise RUSHITI Rénovation.")
LEAD_NEW = ("Informations légales relatives au site rushiti-renovation.fr et à la SARL Rushiti, "
            "exerçant sous le nom commercial RUSHITI Rénovation.")


def fix_mentions(html):
    n = 0
    for old, new in ((SEC1_OLD, SEC1_NEW), (SEC7_OLD, SEC7_NEW)):
        html, k = old.subn(new, html); n += k
    for old, new in ((SEC2_OLD, SEC2_NEW), (SEC3_OLD, SEC3_NEW), (DATE_OLD, DATE_NEW), (LEAD_OLD, LEAD_NEW)):
        if old in html:
            html = html.replace(old, new); n += 1
    return html, n


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    root = sys.argv[1]; apply = "--apply" in sys.argv
    changes = 0

    # 1. llms.txt
    src = open(os.path.join(HERE, "llms.txt"), encoding="utf-8").read()
    dst = os.path.join(root, "llms.txt")
    cur = open(dst, encoding="utf-8").read() if os.path.exists(dst) else ""
    if cur != src:
        changes += 1; print("llms.txt : à remplacer")
        if apply:
            open(dst, "w", encoding="utf-8").write(src)
    else:
        print("llms.txt : déjà à jour")

    # 2. mentions-legales.html
    p = os.path.join(root, "mentions-legales.html")
    if not os.path.exists(p):
        print("mentions-legales.html introuvable dans", root); sys.exit(1)
    html = open(p, encoding="utf-8").read()
    new, n = fix_mentions(html)
    print(f"mentions-legales.html : {n} remplacement(s)" + (" (déjà corrigé)" if n == 0 else ""))
    if n:
        changes += 1
        if apply:
            open(p, "w", encoding="utf-8").write(new)

    print(("APPLIQUÉ" if apply else "SIMULATION") + f" — {changes} fichier(s) à modifier")


if __name__ == "__main__":
    main()
