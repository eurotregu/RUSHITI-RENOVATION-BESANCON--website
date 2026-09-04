# RUSHITI RÉNOVATION BESANÇON - Website

Site web professionnel pour **RUSHITI RÉNOVATION BESANÇON**, entreprise de rénovation et peinture basée à Besançon (25000), Doubs.

Contact : 07 60 27 98 97 — contact@rushiti-renovation.fr — SIRET 905 214 631 00012

## Structure

```
index.html       - Page principale
css/style.css    - Feuille de styles
js/main.js       - Scripts interactifs
```

## Fonctionnalités

- Design responsive (mobile, tablette, desktop)
- Navigation fixe avec effet au scroll
- Section hero avec compteurs animés
- Galerie de réalisations avec filtres
- Section À Propos (assurance décennale, RGE, SIRET)
- Carrousel d'avis Google (note et avis relevés sur la fiche Google, cf. `docs/seo/avis-google-releve-2026-08-22.md`)
- Formulaire de contact (envoi Web3Forms, honeypot + hCaptcha anti-robot, redirection vers /merci)
- Données structurées JSON-LD (LocalBusiness / HousePainter)
- Animations au scroll

## Outils

- `tools/mcp-gbp/` : serveur MCP (Cloudflare Worker) reliant Claude à la fiche Google Business Profile — voir `tools/mcp-gbp/README.md`. Aucun secret dans le dépôt ; déployé séparément avec Wrangler.

## Déploiement

Site statique - déployé automatiquement sur GitHub Pages à chaque push sur `main` (workflow `.github/workflows/deploy.yml`).
