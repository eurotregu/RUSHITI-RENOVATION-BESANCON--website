#!/usr/bin/env python3
"""Générateur d'étude de cas — RUSHITI Rénovation (03/09/2026).

Transforme une fiche chantier JSON (voir fiche-modele.json et questionnaire-chantier.md)
en page /realisations/{slug} prête à déposer dans le dépôt de production, en réutilisant
l'en-tête, la navigation, le pied de page et les scripts d'une page hôte de production
(a-propos.html), donc toujours identiques au site en ligne.

Usage :
    python3 gen_etude_de_cas.py fiche.json /chemin/vers/rushiti-renovation [--sortie DIR] [--brouillon]

Garde-fous (refus de générer, sauf --brouillon qui produit une page marquée NOINDEX pour relecture) :
  - tout champ contenant « [À COMPLÉTER] » ou « [À CONFIRMER] » ;
  - photos sans accord_photos = true ; citation sans accord_ecrit = true ;
  - aucun prix, délai ou promesse : les champs « prix », « delai_promis » sont interdits.
Le script imprime aussi la carte à ajouter dans realisations.html et la ligne du sitemap.
"""
import html, json, os, re, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SERVICES = {
    "peinture-interieure": ("Peinture intérieure", "Peinture intérieure à Besançon"),
    "peinture-exterieure": ("Peinture extérieure", "Peinture extérieure et façades à Besançon"),
    "papier-peint": ("Papier peint", "Pose de papier peint à Besançon"),
    "toile-de-verre": ("Toile de verre", "Toile de verre à Besançon"),
    "ratissage-enduit": ("Ratissage et enduit", "Ratissage et enduit à Besançon"),
    "platrerie": ("Plâtrerie et placo", "Plâtrerie et placo à Besançon"),
    "cloisons": ("Cloisons", "Cloisons à Besançon"),
    "doublage-murs": ("Doublage des murs", "Doublage des murs à Besançon"),
    "faux-plafonds": ("Faux plafonds", "Faux plafonds à Besançon"),
    "revetements-sol": ("Revêtements de sol", "Revêtements de sol à Besançon"),
    "parquet-flottant": ("Parquet flottant", "Parquet flottant à Besançon"),
    "sol-pvc": ("Sol PVC", "Sol PVC à Besançon"),
    "lino-vinyle-lvt": ("Lino, vinyle et LVT", "Lino, vinyle et LVT à Besançon"),
    "vitrification-parquet": ("Vitrification de parquet", "Vitrification de parquet à Besançon"),
    "ragreage-sol": ("Ragréage de sol", "Ragréage de sol à Besançon"),
    "isolation": ("Isolation", "Isolation à Besançon"),
    "isolation-interieure": ("Isolation par l'intérieur", "Isolation par l'intérieur à Besançon"),
    "degat-des-eaux": ("Dégât des eaux", "Réparation après dégât des eaux à Besançon"),
    "renovation-salle-de-bain": ("Rénovation de salle de bains", "Rénovation de salle de bains à Besançon"),
    "renovation-cuisine": ("Rénovation de cuisine", "Rénovation de cuisine à Besançon"),
    "renovation-appartement": ("Rénovation d'appartement", "Rénovation d'appartement à Besançon"),
}
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
PLACEHOLDER = re.compile(r"\[À (COMPLÉTER|CONFIRMER)[^\]]*\]")
BASE = "https://rushiti-renovation.fr"


def esc(s):
    return html.escape(str(s), quote=True)


def paras(txt):
    return "".join(f"<p>{esc(p.strip())}</p>" for p in str(txt).split("\n\n") if p.strip())


def check(fiche, brouillon):
    errs = []
    dump = json.dumps(fiche, ensure_ascii=False)
    if PLACEHOLDER.search(dump):
        errs.append("des champs « [À COMPLÉTER] » ou « [À CONFIRMER] » subsistent")
    for k in ("prix", "delai_promis", "tarif"):
        if k in dump.lower():
            errs.append(f"champ interdit détecté : {k}")
    if fiche.get("photos") and not fiche.get("accord_photos") is True:
        errs.append("photos présentes sans accord_photos = true (RGPD)")
    cit = fiche.get("citation") or {}
    if cit.get("texte") and cit.get("accord_ecrit") is not True:
        errs.append("citation présente sans accord_ecrit = true (RGPD)")
    for k in ("slug", "titre", "prestation_principale", "commune", "date_chantier", "en_bref", "probleme", "diagnostic", "intervention", "resultat", "meta_description"):
        if not fiche.get(k):
            errs.append(f"champ requis manquant : {k}")
    if fiche.get("prestation_principale") not in SERVICES:
        errs.append("prestation_principale inconnue")
    if len(fiche.get("meta_description", "")) > 160:
        errs.append("meta_description > 160 caractères")
    if errs and not brouillon:
        print("REFUS — corriger la fiche :"); [print("  ✗", e) for e in errs]; sys.exit(1)
    return errs


def build(fiche, prod, brouillon):
    slug = fiche["slug"]; url = f"{BASE}/realisations/{slug}"
    svc = fiche["prestation_principale"]; svc_nom, pilier_ancre = SERVICES[svc]
    commune = fiche["commune"]; zone_slug = fiche.get("zone_slug", "")
    try:
        y, m = fiche["date_chantier"].split("-")[:2]; date_aff = f"{MOIS[int(m) - 1]} {y}"
    except (ValueError, IndexError):
        date_aff = "[date à compléter]"
    titre_court = fiche.get("titre_court") or fiche["titre"]
    # fiche chantier (faits, jamais de prix)
    rows = [("Commune", commune)]
    if fiche.get("quartier"): rows.append(("Quartier", fiche["quartier"]))
    if fiche.get("type_bati"): rows.append(("Type de bâti", fiche["type_bati"]))
    rows.append(("Prestations", ", ".join(SERVICES[s][0] for s in fiche.get("prestations", [svc]) if s in SERVICES)))
    if fiche.get("duree"): rows.append(("Durée du chantier", fiche["duree"]))
    if fiche.get("client_type"): rows.append(("Client", fiche["client_type"]))
    rows.append(("Période", date_aff))
    fiche_html = '<div class="factors">' + "".join(f'<div class="factor"><b>{esc(k)}</b><span>{esc(v)}</span></div>' for k, v in rows) + "</div>"
    # photos
    photos_html = ""
    if fiche.get("photos"):
        figs = []
        for p in fiche["photos"]:
            src = "/assets/realisations/" + p["fichier"]
            dims = ""
            try:
                from PIL import Image
                w, h = Image.open(os.path.join(prod, "assets", "realisations", p["fichier"])).size
                dims = f' width="{w}" height="{h}"'
            except Exception:
                pass
            met = {"avant": "Avant", "pendant": "Pendant les travaux", "apres": "Après"}.get(p.get("etape", ""), "")
            figs.append(f'<figure class="real"><img src="{src}" alt="{esc(p["alt"])}" loading="lazy"{dims}><figcaption>' + (f'<span class="met">{met}</span>' if met else "") + f'<span class="cap">{esc(p["legende"])}</span></figcaption></figure>')
        photos_html = '<h2 id="photos">Le chantier en images</h2><div class="gallery">' + "".join(figs) + "</div>"
    # points clés
    pc = fiche.get("points_cles") or []
    points_html = ('<div class="keypoint"><b>À retenir</b><ul>' + "".join(f"<li>{esc(x)}</li>" for x in pc) + "</ul></div>") if pc else ""
    # citation
    cit = fiche.get("citation") or {}
    citation_html = ""
    if cit.get("texte") and cit.get("accord_ecrit") is True:
        citation_html = f'<div class="reviews"><div class="review"><p>« {esc(cit["texte"])} »</p><b>{esc(cit.get("auteur_affiche", "Client"))} · {esc(commune)}</b></div></div>'
    # faq
    faq = fiche.get("faq") or []
    faq_html = ""
    if faq:
        faq_html = '<h2 id="faq">Questions fréquentes</h2><div class="factors">' + "".join(f'<details class="faq-item"><summary>{esc(q["q"])}</summary><p>{esc(q["a"])}</p></details>' for q in faq) + "</div>"
    # relinks
    links = [(f"/{svc}-besancon", f"{pilier_ancre} &rarr;")]
    if zone_slug and os.path.exists(os.path.join(prod, f"{svc}-{zone_slug}.html")):
        links.append((f"/{svc}-{zone_slug}", f"{svc_nom} à {esc(commune)} &rarr;"))
    for s in fiche.get("prestations", []):
        if s != svc and s in SERVICES: links.append((f"/{s}-besancon", f"{SERVICES[s][0]} &rarr;"))
    for b in fiche.get("articles_lies", []): links.append((b["url"], esc(b["ancre"]) + " &rarr;"))
    links += [("/realisations", "Toutes nos réalisations &rarr;"), ("/contact", "Diagnostic gratuit &rarr;")]
    relinks = "".join(f'<a href="{u}">{a}</a>' for u, a in links)
    interv = fiche["intervention"]
    main = open(os.path.join(HERE, "gabarit-main.html"), encoding="utf-8").read().format(
        titre=esc(fiche["titre"]), titre_court=esc(titre_court), commune_affichee=esc(commune) + (f" ({esc(fiche['quartier'])})" if fiche.get("quartier") else ""),
        prestation_affichee=esc(svc_nom), date_affichee=date_aff, en_bref=esc(fiche["en_bref"]), pilier_url=f"/{svc}-besancon", pilier_ancre=esc(pilier_ancre),
        fiche_chantier=fiche_html, probleme=paras(fiche["probleme"]), diagnostic=paras(fiche["diagnostic"]),
        preparation=paras(interv.get("preparation", "")), traitement=paras(interv.get("traitement", "")), finition=paras(interv.get("finition", "")),
        photos=photos_html, resultat=paras(fiche["resultat"]), points_cles=points_html, citation=citation_html, faq=faq_html, relinks=relinks,
        cta_titre=esc(fiche.get("cta_titre") or f"Un projet similaire à {commune} ou dans le Doubs ?"))
    # JSON-LD
    images = [f"{BASE}/assets/realisations/{p['fichier']}" for p in fiche.get("photos", [])]
    graph = [{"@type": "Article", "@id": url + "#article", "headline": fiche["titre"], "description": fiche["meta_description"], "inLanguage": "fr-FR",
              "datePublished": fiche.get("date_publication") or datetime.date.today().isoformat(), "dateModified": fiche.get("date_publication") or datetime.date.today().isoformat(),
              "author": {"@id": f"{BASE}/a-propos#isuf"}, "publisher": {"@id": f"{BASE}/#business"}, "mainEntityOfPage": url,
              "about": {"@type": "Service", "name": pilier_ancre, "url": f"{BASE}/{svc}-besancon", "provider": {"@id": f"{BASE}/#business"}},
              "contentLocation": {"@type": "Place", "name": commune, "address": {"@type": "PostalAddress", "addressLocality": commune, "addressRegion": "Bourgogne-Franche-Comté", "addressCountry": "FR"}}},
             {"@type": "BreadcrumbList", "itemListElement": [
                 {"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE + "/"},
                 {"@type": "ListItem", "position": 2, "name": "Réalisations", "item": BASE + "/realisations"},
                 {"@type": "ListItem", "position": 3, "name": titre_court, "item": url}]}]
    if images: graph[0]["image"] = images
    if faq: graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q["q"], "acceptedAnswer": {"@type": "Answer", "text": q["a"]}} for q in faq]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    # page hôte
    host_path = os.path.join(prod, "a-propos.html"); host = open(host_path, encoding="utf-8").read()
    blog = open(os.path.join(prod, "blog", "reparer-plafond-degat-des-eaux-besancon.html"), encoding="utf-8").read()
    art_style = re.search(r"<style>(\.article\{.*?)</style>", blog, re.S)
    page = host
    page = re.sub(r"<title>.*?</title>", f"<title>{esc(fiche.get('title_seo') or fiche['titre'])}</title>", page, count=1, flags=re.S)
    page = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(fiche["meta_description"])}">', page, count=1)
    page = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', page, count=1)
    page = re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="' + ("noindex, nofollow" if brouillon else "index, follow") + '">', page, count=1)
    page = re.sub(r'<meta property="og:type" content="[^"]*">', '<meta property="og:type" content="article">', page, count=1)
    page = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{esc(fiche.get("title_seo") or fiche["titre"])}">', page, count=1)
    page = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{esc(fiche["meta_description"])}">', page, count=1)
    page = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', page, count=1)
    if images: page = re.sub(r'<meta property="og:image" content="[^"]*">', f'<meta property="og:image" content="{images[0].replace(".webp", ".jpg") if os.path.exists(os.path.join(prod, "assets/realisations", fiche["photos"][0]["fichier"].replace(".webp", ".jpg"))) else images[0]}">', page, count=1)
    page = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">' + ld + "</script>", page, count=1, flags=re.S)
    if art_style: page = page.replace("</head>", "<style>" + art_style.group(1) + "</style></head>", 1)
    page = re.sub(r"<main>.*?</main>", lambda m: main, page, count=1, flags=re.S)
    # carte pour realisations.html + sitemap
    cover = fiche["photos"][0] if fiche.get("photos") else None
    card = (f'<a href="/realisations/{slug}" style="text-decoration:none"><figure class="real">' + (f'<img src="/assets/realisations/{cover["fichier"]}" alt="{esc(cover["alt"])}" loading="lazy">' if cover else "") + f'<figcaption><span class="met">{esc(svc_nom)} · {esc(commune)}</span><span class="cap">{esc(titre_court)}</span></figcaption></figure></a>')
    sitemap = f"  <url><loc>{url}</loc><lastmod>{datetime.date.today().isoformat()}</lastmod></url>"
    return page, card, sitemap


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2:
        print(__doc__); sys.exit(2)
    fiche = json.load(open(args[0], encoding="utf-8")); prod = args[1]
    brouillon = "--brouillon" in sys.argv
    out = sys.argv[sys.argv.index("--sortie") + 1] if "--sortie" in sys.argv else os.path.join(prod, "realisations")
    errs = check(fiche, brouillon)
    page, card, sitemap = build(fiche, prod, brouillon)
    os.makedirs(out, exist_ok=True)
    slug_fichier = PLACEHOLDER.sub("brouillon", fiche["slug"]).strip("-") if brouillon else fiche["slug"]
    dst = os.path.join(out, slug_fichier + ".html")
    open(dst, "w", encoding="utf-8").write(page)
    print(("BROUILLON (noindex) " if brouillon else "PAGE ") + dst, f"— {len(re.sub(r'<[^>]+>', ' ', page).split())} mots")
    if errs: print("  Points à régler avant publication :"); [print("   ✗", e) for e in errs]
    print("\nCarte à insérer dans realisations.html :\n" + card)
    print("\nLigne sitemap.xml :\n" + sitemap)
    print("\nRappel : ajouter la page à /llms.txt (section Réalisations) et relier depuis la page locale de la commune si elle existe.")


if __name__ == "__main__":
    main()
