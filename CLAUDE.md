# CLAUDE.md — RUSHITI Rénovation (site vitrine Besançon)

> Résumé d'orientation pour Claude Code. **Ce fichier n'est pas la source
> canonique** : les instructions permanentes vivent dans
> `docs/instructions-claude/instructions-claude-complete.txt`
> (v1.2 — 28/08/2026). En cas d'écart, la version complète prime.

## Règle de lecture obligatoire

Avant toute production de contenu (page, article, devis, courrier, email,
post, FAQ, JSON-LD), lire en entier
`docs/instructions-claude/instructions-claude-complete.txt`.
Pour une tâche purement technique (CSS, JS, workflow), ce résumé suffit.

## Identité — données figées

- Nom commercial : **RUSHITI Rénovation** (communication) · dénomination
  sociale : **Rushiti**, SARL (mentions légales). Jamais « SARL RUSHITI
  Rénovation ».
- NAP au caractère près : 18 rue du Professeur Haag, 25000 Besançon ·
  07 60 27 98 97 (JSON-LD : `+33760279897`) · contact@rushiti-renovation.fr
- SIRET 905 214 631 00012 · RCS Besançon 905 214 631 · TVA FR89905214631 ·
  décennale ERGO (n° de contrat : [À COMPLÉTER]).
- Métiers : peinture, plâtrerie-placo, sols, isolation (thermique et
  acoustique), dégât des eaux, rénovation de pièce, B2B — Besançon et le
  Doubs (25). Jamais de plomberie ni d'électricité.
- Charte : #002B4B · #1A75BB · #016738 · #EB1C24.

## Garde-fous essentiels

- Toujours en français, vouvoiement, zéro jargon marketing creux.
- N'inventer JAMAIS : prix, délai, taux de TVA affirmé, avis, statistique,
  certification (RGE, Qualibat), prise en charge assurance → `[À COMPLÉTER]`.
- DTU citées uniquement si exactes (table de vérité dans la version
  complète) ; sinon « selon les règles de l'art ».
- Sinistres : libellés IRSI, ne jamais se substituer à l'assureur.
- RGPD : accord écrit avant toute photo ou témoignage identifiable.
- Toute sortie est un brouillon ; rien n'est publié, déployé ni envoyé sans
  validation d'Isuf.

## Conventions du dépôt

- Site statique sans build : `index.html` et pages HTML à la racine,
  `css/`, `js/`.
- **Déploiement : tout push sur `main` publie immédiatement le dépôt entier
  via GitHub Pages** (`.github/workflows/deploy.yml`, `path: '.'`).
  Toujours travailler en branche + PR ; merger = mettre en ligne.
- `docs/` mêle français et albanais (`korrigjime-prodhim/`,
  `regjistri-fjale-kyce.csv`…) : respecter la langue du fichier existant ;
  les réponses à Isuf restent en français.
- Registre canonique page ↔ mot-clé : `docs/seo/regjistri-fjale-kyce.csv` —
  à consulter avant toute page ou balise neuve (anti-cannibalisation).
- Agents : 6 skills SEO versionnés dans `.claude/skills/` ; la suite
  complète (courriers, devis, réseaux sociaux…) vit côté claude.ai et peut
  être absente d'une session. Quand un agent couvre la demande, l'utiliser
  plutôt qu'improviser.

## Synchronisation des instructions

`instructions-claude-complete.txt` (canonique) → dérivés :
`instructions-claude-condensee.txt` (champ claude.ai) et ce `CLAUDE.md`.
Tout bump de version = mise à jour simultanée des trois fichiers + journal
dans `docs/instructions-claude/README.md`. Une correction repérée dans un
dérivé se corrige d'abord dans le canon.
