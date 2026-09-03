# Grille locale `/{service}-{zone}` — état des lieux et plan (03/09/2026)

| | |
|---|---|
| Déclencheur | Isuf, 03/09 : « vazhdo me P2 : grille locale » (constat 14 de `audit-premium-site-2026-09-03.md`) |
| Source | Dépôt de production `eurotregu/rushiti-renovation` au 03/09 (HEAD après PR #40), `inventaire-grille-paliers-2026-08.csv`, `guide-seo-local-pages-service-ville-2026-08.md` |
| Correction de l'audit | Le constat 14 affirmait que le plan par paliers n'était pas appliqué. **C'est faux** : il l'est depuis août (644 → 301 redirections, 706 pages conservées, Worker filtré par `EXTRA_URLS`). Ce qui reste est un problème de **contenu**, pas de volume. |

## 1. Ce qui est en place

| Palier | Zones | Quota | Réel en production |
|---|---|---|---|
| A (cœur) | 14 : Besançon + 13 quartiers | 18 pages | 18 partout |
| B (pôles) | 24 communes | 10 pages | 10 à 12 |
| C (villages) | 38 communes | 5 pages | 5 à 8 |

Total : **706 pages de grille** (+ 49 pages transverses, blog et piliers = 755 URL au sitemap). Les 5 pages du palier C sont toujours peinture intérieure, plâtrerie, revêtements de sol, isolation par l'intérieur, dégât des eaux.

**Dépassements de quota** (31 zones, 1 à 3 pages en plus, surtout `vitrification-parquet`, `ratissage-enduit`, `parquet-flottant`, `cloisons`) : ces pages ont été conservées en août parce qu'elles imprimaient dans la Search Console. Ne pas les supprimer sans l'export GSC qui l'a justifié : liste complète en fin de fichier, à confronter au rapport requête × page avant toute décision.

## 2. Le vrai problème : 16 % de contenu propre

`mesure_differenciation.py` compare chaque page de grille à la page du même service d'une zone sœur du même palier (séquences de 5 mots propres à la page) :

| Palier | Pages | Part de contenu propre (médiane) | Min | Max |
|---|---|---|---|---|
| A | 234 | 16 % | 10 % | 61 % |
| B | 252 | 15 % | 9 % | 35 % |
| C | 215 | 16 % | 10 % | 39 % |

Détail page par page : `mesure-differenciation-2026-09-03.csv` (colonnes : mots, zone sœur comparée, % propre vs sœur, % propre vs pilier, nombre de questions FAQ). Les pages du palier A à 10-12 % (centre-ville, Battant, Chaprais sur toile de verre, lino, ratissage, faux plafonds…) sont celles où le risque « contenu à l'échelle » est le plus fort, parce qu'elles visent des quartiers où Google a de vraies requêtes à servir.

Ce que le contenu propre contient aujourd'hui : un paragraphe géographique (distance, population, altitude), une phrase de « chantier type », la dernière question de FAQ. Le test « masquer la zone » du guide (section 6) échoue sur la quasi-totalité des pages.

## 3. Ce qu'on ne fait pas

- **Pas de recherche-remplacement** de mots-clés locaux, pas de paragraphes « à propos de {commune} » générés : ce serait ajouter du contenu à l'échelle au contenu à l'échelle.
- **Pas de suppression** de pages sans export GSC ; la consolidation d'août a déjà fait le tri sur données.
- **Pas de nouvelle page** (porte `rushiti-keyword-map`).

## 4. Le plan, dans l'ordre

1. **Preuves locales réelles, une zone à la fois** : chaque étude de cas publiée (`../etudes-de-cas/`) est reliée à la page locale de sa commune, avec 2-3 phrases propres (bâti rencontré, problème, résultat) et une photo autorisée. Priorité aux 14 zones A, puis aux pôles B où RUSHITI a réellement travaillé. C'est la seule différenciation qui tienne au test « masquer la zone ».
2. **Angle local par zone A** (matrice du guide, section 6) : à confirmer par le vécu d'Isuf et Yll avant écriture. Fiche à remplir par zone : type de bâti dominant, 2 problèmes récurrents rencontrés, 1 contrainte d'accès ou de copropriété, 1 chantier réel. Sans réponse, la page garde son tronc commun : on ne remplit pas.
3. **Export Search Console requête × page (16 semaines)** : (a) confirmer que les 31 pages en dépassement de quota impriment encore ; (b) repérer les pages de grille à 0 impression sur 16 semaines → candidates à une consolidation supplémentaire vers le pilier, décision d'Isuf ; (c) alimenter `rushiti-cannibal-check` sur plaquiste/plâtrerie et isolation/ITI.
4. **Mesure** : refaire tourner `mesure_differenciation.py` après chaque vague ; l'objectif n'est pas un pourcentage, c'est que les pages A passent le test « masquer la zone ».

## 5. Fichiers

| Fichier | Rôle |
|---|---|
| `mesure_differenciation.py` | Mesure reproductible (usage dans l'en-tête du script) |
| `mesure-differenciation-2026-09-03.csv` | Baseline datée, 706 pages |

## Annexe — pages en dépassement de quota (à confronter à la GSC)

amagney (C) +parquet-flottant · arguel (C) +vitrification-parquet · audeux (C) +vitrification-parquet · avanne-aveney (B) 11 · busy (C) +ratissage-enduit · chalezeule (B) 11 · champoux (C) +vitrification-parquet · chaucenne (C) +parquet-flottant, ratissage-enduit · chaudefontaine (C) +cloisons, papier-peint · chemaudin (C) +isolation, ratissage-enduit · dannemarie-sur-crete (B) 11 · deluz (C) +cloisons, ratissage-enduit, sol-pvc · fontain (C) +vitrification-parquet · franois (B) 11 · houtaud (C) +cloisons, papier-peint, parquet-flottant · larnod (C) +vitrification-parquet · les-auxons (C) +parquet-flottant · marchaux (B) 11 · mazerolles-le-salin (C) +lino-vinyle-lvt · miserey-salines (B) 12 · montbeliard (B) 11 · montfaucon (B) 11 · morre (B) 11 · pelousey (C) +vitrification-parquet · pouilley-les-vignes (B) 11 · saone (B) 11 · thise (B) 12 · thoraise (C) +ratissage-enduit · torpes (C) +ratissage-enduit, vitrification-parquet · vaire-le-petit (C) +vitrification-parquet · vorges-les-pins (C) +ratissage-enduit, vitrification-parquet
