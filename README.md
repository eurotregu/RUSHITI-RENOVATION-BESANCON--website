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
- Formulaire de contact (ouvre le client email avec la demande pré-remplie)
- Données structurées JSON-LD (LocalBusiness / HousePainter)
- Animations au scroll

## Déploiement

Site statique - déployé automatiquement sur GitHub Pages à chaque push sur `main` (workflow `.github/workflows/deploy.yml`).

## Moteur SEO + GEO

Le travail de référencement (Google **et** moteurs de réponse IA) est piloté par des agents Claude Code, dans `.claude/skills/`. Point d'entrée unique :

```
/rushiti-seo-engine
```

Le chef d'orchestre : il décide quel agent spécialisé tourne, dans quel ordre, sur quelle cible — et il refuse de créer une page quand une page existante porte déjà la requête. Quatre modes : **CAMPAGNE** (une cible de bout en bout), **CADENCE** (quoi faire cette semaine), **TRIAGE** (arbitrer un plan SEO reçu de l'extérieur), **ÉTAT** (tableau de bord des deux portes).

| Document | Rôle |
|---|---|
| `.claude/skills/rushiti-seo-engine/` | Le moteur : protocole en 8 phases, correspondance avec les playbooks génériques, catalogue des pièges, état daté du dispositif |
| `docs/seo/prompts/prompt-maitre-moteur-seo.md` | Le même protocole en prompt bridé, pour un outil IA **hors dépôt** |
| `docs/seo/arbitrage-moteur-seo-10-skills-2026-08.md` | Pourquoi les 11 skills génériques du playbook « 10-Skill SEO Engine » ne sont pas installés |
| `docs/seo/regjistri-fjale-kyce.csv` | Le registre canonique page ↔ mot-clé (source de vérité anti-cannibalisation) |

**Règles non négociables** : lecture seule sur la production (les agents n'écrivent que dans `docs/seo/`), aucun prix, délai ni chiffre inventé, aucune promesse de classement, et rien n'est déployé sans validation d'Isuf.
