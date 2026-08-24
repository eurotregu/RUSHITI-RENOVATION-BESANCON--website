# Instructions permanentes pour Claude — RUSHITI Rénovation

Bloc à coller dans **Réglages → Instructions for Claude** (préférences valables
sur toutes les conversations et dans Cowork).

| Fichier | Usage | Taille |
|---|---|---|
| `instructions-claude-complete.txt` | Version intégrale. À utiliser si le champ accepte la longueur, sinon en **instructions de Projet** ou en `CLAUDE.md`. | ~15 300 caractères |
| `instructions-claude-condensee.txt` | Version courte si le champ « Instructions for Claude » tronque. Ne perd aucun garde-fou. | ~2 460 caractères |

**Recommandation :** version condensée dans le champ global, version complète en
instructions de Projet. Le détail SEO opérationnel n'est volontairement pas
recopié : il vit déjà dans les agents `.claude/skills/rushiti-*`, et le dupliquer
créerait deux sources de vérité divergentes.

## Sources de vérité utilisées

- `.claude/skills/rushiti-architecte-seo/references/donnees-rushiti.md` (socle v4, 15/08/2026)
- `docs/seo/dtu-referencat-eeat.md` (vérification norme par norme, 21/08/2026)
- `README.md` (NAP publié)

## Écarts corrigés par rapport au brouillon initial

| Point | Brouillon | Corrigé en | Motif |
|---|---|---|---|
| Raison sociale | « SARL RUSHITI Rénovation » | « Rushiti » (SARL) / nom commercial « RUSHITI Rénovation » | Forme explicitement interdite par le socle : le nom commercial n'est pas la raison sociale |
| DTU placo | « conforme DTU 25.1 » | **NF DTU 25.41** | 25.1 = enduits intérieurs en plâtre, pas les plaques. Erreur repérable par un expert |
| DTU cité | « DTU 60.1 » | supprimé | 60.1 = plomberie, hors métier |
| DTU sols | 53.2 (socle v4) | **53.12** | Vérification du 21/08 : 53.12 est la norme en vigueur pour la pose collée |
| Quartier | « La Boucle » | quartiers canoniques (Battant, Chaprais-Cras…) | « La Boucle » n'est pas un quartier : description géographique uniquement |
| Téléphone | `[À COMPLÉTER]` | 07 60 27 98 97 | Donnée validée, publiée dans le `README.md` |
| Délai | « intervention sous 4 h en zone Besançon » | supprimé | Délai inventé — viole le garde-fou n° 1 |
| `priceRange: "€€"` | affirmé | `[À COMPLÉTER]` | Indication de prix non validée |
| Coordonnées géo | 47.2380, 6.0244 « approximatif » | `[À COMPLÉTER]` | Ne correspondent pas à l'adresse réelle ; à relever sur la fiche Google |
| Silos | 7 silos | 6 silos métier + axe B2B transversal | Alignement sur l'architecture réelle des agents |
| « page PILON » | — | « page **pilier** » | *Pilon* = pilon de poulet ; le terme SEO est *pilier* |
| Typos | « INSTRICTIONS », « inclis » | corrigés | — |
| Doublons | bloc entier répété deux fois | fusionné | — |

## À me confirmer avant usage en production

1. **RGE** — mentionné dans la section « À Propos » du site, mais classé
   `[À CONFIRMER]` par le socle. Certification réellement détenue, ou à retirer ?
2. **Carrelage** — « Carrelage & Sol » apparaît dans `index.html`, sans page de
   service. Prestation proposée ou mention à supprimer ?
3. **Numéro de contrat décennale ERGO**, horaires d'ouverture, coordonnées géo
   exactes — pour compléter le JSON-LD.
4. **« Devis gratuit assurance sous 48h »** — présent dans la description Google
   officielle. Engagement tenu ? C'est le seul délai chiffré conservé.
