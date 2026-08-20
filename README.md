# RUSHITI RÉNOVATION BESANÇON - Website

Site vitrine de **RUSHITI Rénovation**, entreprise artisanale (SARL) de rénovation
et de peinture basée à Besançon (25000), Doubs.

Contact : 07 60 27 98 97 — contact@rushiti-renovation.fr
18 rue du Professeur Haag, 25000 Besançon — SIRET 905 214 631 00012

## ⚠️ Ce dépôt n'est pas le site de production

Le site officiel est **https://rushiti-renovation.fr** (environ 1 400 pages :
pages services, pages par commune, blog, réalisations). Il est hébergé et
déployé ailleurs, **pas depuis ce dépôt**.

Ce dépôt contient une page vitrine autonome, publiée sur GitHub Pages. Comme
elle dupliquerait le contenu de production sur un domaine `github.io`, elle est
volontairement exclue de l'indexation :

- `meta robots: noindex, nofollow` sur chaque page HTML ;
- `<link rel="canonical">` pointant vers la page équivalente en production ;
- `robots.txt` en `Disallow: /`.

Toute modification du contenu doit rester **cohérente avec la production** :
les faits de l'entreprise (ancienneté, adresse, horaires, assurances) sont
repris de https://rushiti-renovation.fr/a-propos, `/mentions-legales` et
`/llms.txt`. Les corrections à porter sur la production, elles, sont
documentées dans `docs/seo/`.

## Structure

```
index.html                          - Page vitrine
syndic-copropriete-besancon.html    - Copie d'une page B2B (canonical vers la production)
robots.txt                          - Exclut cette copie de l'indexation
css/style.css                       - Feuille de styles
js/main.js                          - Scripts interactifs
docs/seo/                           - Audits et corrections à porter sur la production
```

## Fonctionnalités

- Design responsive (mobile, tablette, desktop)
- Navigation fixe avec effet au scroll, menu mobile accessible (`aria-expanded`, touche Échap)
- Lien d'évitement vers le contenu principal et styles `:focus-visible`
- Prise en charge de `prefers-reduced-motion` (CSS et JS)
- Section hero avec compteur animé
- Galerie par type de chantier avec filtres
- Section À propos (assurance décennale et RC pro, DTU, SIRET)
- Section Engagements
- Formulaire de contact (ouvre le client email avec la demande pré-remplie,
  avec adresse de repli affichée et mention RGPD)
- Données structurées JSON-LD (LocalBusiness / Painter / HomeAndConstructionBusiness)
- Animations au scroll

## Déploiement

Site statique — déployé automatiquement sur GitHub Pages à chaque push sur
`main` (workflow `.github/workflows/deploy.yml`).
