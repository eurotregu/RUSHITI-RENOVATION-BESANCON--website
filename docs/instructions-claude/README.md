# Instructions permanentes pour Claude — RUSHITI Rénovation

Bloc à coller dans **Réglages → Instructions for Claude** (préférences valables
sur toutes les conversations et dans Cowork).

| Fichier | Usage | Taille |
|---|---|---|
| `instructions-claude-complete.txt` | **Source canonique.** Version intégrale. À utiliser si le champ accepte la longueur, sinon en **instructions de Projet**. | ~20 800 caractères |
| `instructions-claude-condensee.txt` | Version courte si le champ « Instructions for Claude » tronque. Ne perd aucun garde-fou. Dérivée du canon. | ~2 760 caractères |
| `CLAUDE.md` (racine du dépôt) | Résumé mince chargé automatiquement par Claude Code sur ce dépôt. Dérivé, jamais collé dans claude.ai. | ~3 150 caractères |

**Recommandation :** version condensée dans le champ global, version complète en
instructions de Projet. Le détail SEO opérationnel n'est volontairement pas
recopié : il vit déjà dans les agents `.claude/skills/rushiti-*`, et le dupliquer
créerait deux sources de vérité divergentes.

**Synchronisation :** `instructions-claude-complete.txt` est la source
canonique ; la condensée et le `CLAUDE.md` en dérivent. Tout changement de
version = mise à jour simultanée des trois fichiers + journal ci-dessous.
Une correction repérée dans un dérivé se corrige d'abord dans le canon.

## Sources de vérité utilisées

- `.claude/skills/rushiti-architecte-seo/references/donnees-rushiti.md` (socle v4, 15/08/2026)
- `docs/seo/dtu-referencat-eeat.md` (vérification norme par norme, 21/08/2026)
- `README.md` (NAP publié)

## Écarts corrigés par rapport au brouillon initial (v1.0 — 23/08/2026)

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

## Écarts corrigés lors de la fusion des brouillons Gemini/Kimi (v1.1 — 28/08/2026)

Les brouillons fournis le 28/08 (« GEMINI I FUNDIT », « Gemini ultra-premium »,
« Kimi 3 », questionnaire albanais « KONTEKSTI MASTER ») sont antérieurs aux
corrections v1.0 : en cas de conflit, la v1.0 fait foi. Le questionnaire
albanais est écarté (décision Isuf, 28/08) — presque vide et hors périmètre ;
ses questions encore utiles rejoignent la liste « À me confirmer ».

| Point | Brouillon | Corrigé en | Motif |
|---|---|---|---|
| « La Boucle (Centre-Ville) » | réapparaît comme quartier | non repris ; « la boucle du Doubs » reste une description géographique | Régression sur correction v1.0 |
| Liste de quartiers | « Les Chaprais, Montrapon, Clairs-Soleil, Planoise… » | liste canonique conservée (Chaprais-Cras, Montrapon-Montboucons, Vaîte-Clairs Soleils…) | Seule la liste du socle vaut |
| NF DTU 60.1, NF C 15-100 | citées (questionnaire) | non reprises | Plomberie et électricité, hors métier (APE 43.34Z) |
| Plomberie, électricité, hydraulique | services listés (questionnaire) | non repris | Hors périmètre réel de l'entreprise |
| « respect des délais » (LinkedIn) | promesse sèche | « délais annoncés tenus » | Garde-fou n° 1 : aucun délai inventé |
| Hashtags | deux blocs divergents : localisés (5-8) vs génériques | bloc localisé retenu (décision Isuf, 28/08) | Doctrine unique ; alignement de l'agent réseaux sociaux à faire (n° 6 ci-dessous) |
| Saint-Vit, Devecey | cités en première couronne | ajoutés en zone d'intervention, palier local à attribuer | Absents du socle v4 et de la grille de paliers |
| Isolation | « isolation » seule / « thermique acoustique » | « isolation thermique intérieure (ITI) et combles, isolation acoustique (cloisons et doublages) » | Précision métier ; aucune DTU ajoutée (25.41/25.42 couvrent) |
| DTU sols du socle v4 | `donnees-rushiti.md` citait encore « DTU 53.2 » | **NF DTU 53.12** (pose collée) | Alignement sur la correction v1.0 — les deux sources divergeaient |

Apports intégrés en v1.1 : section [3] Périmètre de délégation — Framework 4D
(D1 à D4, transparence haut risque, règles emails/SOP) · point 7 « ouverture
de session » de la MÉTHODE · section [10] Réseaux sociaux — cadrage ·
première couronne GBM + secteurs secondaires (Pontarlier, Val de Morteau,
Haut-Doubs, Montbéliard) · isolation acoustique · création du `CLAUDE.md`
racine. Renumérotation [0]–[11] ; le texte de la description Google Business
([11]) est inchangé au caractère près.

## À me confirmer avant usage en production

1. **RGE** — mentionné dans la section « À Propos » du site, mais classé
   `[À CONFIRMER]` par le socle. Certification réellement détenue, ou à retirer ?
2. **Carrelage** — « Carrelage & Sol » apparaît dans `index.html`, sans page de
   service. Prestation proposée ou mention à supprimer ?
3. **Numéro de contrat décennale ERGO**, horaires d'ouverture, coordonnées géo
   exactes — pour compléter le JSON-LD.
4. **« Devis gratuit assurance sous 48h »** — présent dans la description Google
   officielle. Engagement tenu ? C'est le seul délai chiffré conservé.
5. **Palier local de Saint-Vit et Devecey** — cités en première couronne dans
   les brouillons, absents du socle v4 et de la grille
   `docs/seo/inventaire-grille-paliers-2026-08.csv`. Palier A/B/C à attribuer.
6. **Banque de hashtags de l'agent `rushiti-reseaux-sociaux`** (côté claude.ai)
   — à aligner AVANT le premier post publié : remplacer sa banque par le socle
   localisé (#RUSHITIrenovation, #ArtisanBesancon…) et passer son plafond
   Facebook/Instagram de 4-6 à 5-8 (LinkedIn 3-5 déjà conforme ; Google
   Business 0-2). Bloc prêt à coller fourni par Claude le 28/08.
7. **Écarts relevés en production le 28/08** — **corrigés** par la PR #49,
   mergée le 29/08 : « SARL RUSHITI Rénovation » (page syndic) → « SARL
   Rushiti (nom commercial RUSHITI Rénovation) » ; « RGE » retiré du footer
   et du badge À propos de l'accueil ; horaires du footer syndic alignés sur
   le paquet 5 ; `priceRange` retiré des deux JSON-LD ; type unifié sur
   `HousePainter`. Restent ouverts : le RGE si la certification est
   réellement détenue (point 1) et l'`openingHoursSpecification` de la page
   syndic une fois les horaires confirmés (point 3).
8. **Exposition publique** — GitHub Pages publie tout le dépôt (`path: '.'`),
   donc `docs/` et `CLAUDE.md` sont servis en ligne. Aucun secret n'y figure
   (n° ERGO en `[À COMPLÉTER]`) ; confirmer que cette exposition convient.

## Journal des versions

- **v1.2 — 28/08/2026** : doctrine hashtags précisée par plateforme —
  banque localisée inchangée, volumes réconciliés avec les plafonds de
  l'agent réseaux sociaux (LinkedIn 3 à 5, Facebook/Instagram 5 à 8,
  Google Business 0 à 2), sur délégation d'Isuf.
- **v1.1 — 28/08/2026** : fusion des brouillons Gemini/Kimi (tableau
  ci-dessus). Nouvelles sections Framework 4D et Réseaux sociaux, protocole
  d'ouverture de session, géographie élargie, isolation acoustique,
  `CLAUDE.md` racine. Questionnaire albanais écarté.
- **v1.0 — 23/08/2026** : création — consolidation initiale, 13 écarts
  corrigés par rapport au brouillon initial (tableau ci-dessus).
