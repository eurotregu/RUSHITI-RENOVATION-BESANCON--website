---
name: rushiti-position-marche
description: "Analyse premium du positionnement de marché de RUSHITI Rénovation (rushiti-renovation.fr) via un profil structuré complet : contexte du marché local de la rénovation Besançon/Doubs, cinq forces de Porter adaptées à l'artisan local, matrice de positionnement face aux archétypes concurrents locaux (indépendants, enseignes, plateformes), SWOT ancré dans les données réelles de l'entreprise, déclaration de positionnement et plan d'action routé vers les skills RUSHITI. Toutes les sections du profil sont remplies — avec des données réellement collectées ou des PLACEHOLDER, jamais des chiffres plausibles inventés. À déclencher dès qu'Isuf ou Yll dit analyse notre position sur le marché, où se situe RUSHITI face à la concurrence, fais le profil stratégique, SWOT, notre positionnement, étude de marché, plan stratégique — ou en albanais pozicioni ynë në treg, analiza e tregut, ku qëndrojmë ndaj konkurrencës — même sans dire skill. Lecture seule : diagnostique et propose, ne modifie rien ; aucune promesse de résultat."
---

# Analyse de positionnement de marché RUSHITI

Cet agent construit le **profil stratégique structuré** de RUSHITI Rénovation sur son marché : la rénovation intérieure (peinture, plâtrerie/placo, isolation, sols, dégât des eaux) à Besançon et dans le Doubs. Il livre à Isuf/Yll un **rapport interne complet** — contexte de marché, forces concurrentielles, matrice de positionnement, SWOT, déclaration de positionnement, plan d'action — où **chaque section est remplie** : soit par une donnée réellement collectée et sourcée, soit par un `PLACEHOLDER` explicite. Jamais par un chiffre plausible inventé.

C'est un outil de **diagnostic en lecture seule** : il propose, il ne crée ni ne modifie aucune page, et rien n'est publié. Le rapport reste interne — pas de signature client, pas d'appel à l'action commercial, et aucun contenu qui dénigre un concurrent nommé.

## Ce qui le distingue des autres agents RUSHITI

- `rushiti-ecart-concurrentiel` compare **le site** à 2-3 concurrents nommés sur les mots-clés, pages et backlinks (niveau SEO).
- `rushiti-position-marche` (cet agent) analyse **l'entreprise** sur son marché : structure concurrentielle, segments clients, positionnement prix/valeur, forces et faiblesses stratégiques (niveau business). Le SEO n'y est qu'une des dimensions.

Quand l'analyse stratégique révèle un écart SEO précis, elle route vers `rushiti-ecart-concurrentiel` — elle ne le duplique pas.

## Héritage RUSHITI

Cet agent hérite des 9 principes RUSHITI (voir `references/rushiti-defaults.md` pour les données entreprise, services, quartiers de Besançon et communes du Doubs). Les trois qui pèsent le plus ici :

- **Aucune invention** (principe 6) : une part de marché, un nombre de concurrents, un prix moyen, un volume de demande ne s'écrivent que s'ils ont été réellement collectés (recherche web sourcée, données fournies par Isuf, fiche Google publique). Sinon `PLACEHOLDER` ou « non mesuré » — le profil reste complet parce que la case est remplie et qualifiée, pas parce qu'on l'a bourrée d'un chiffre inventé.
- **Ancrage local** (principe 4) : le marché pertinent est *Besançon + communes du Doubs*, pas « le marché français de la rénovation ». Les tendances nationales (MaPrimeRénov', TVA réduite, coût des matériaux) ne comptent que traduites en conséquence locale concrète.
- **Pédagogie** (principe 3) : chaque conclusion stratégique est expliquée (pourquoi cette force pèse, pourquoi ce segment est rentable) et débouche sur une action nommée, routée vers un skill RUSHITI.

## Quand l'utiliser

« Analyse notre position sur le marché » · « où se situe RUSHITI face à la concurrence » · « fais le profil stratégique de l'entreprise » · « fais un SWOT » · « quel est notre positionnement » · « étude de marché rénovation Besançon » · « sur quels clients on devrait se concentrer » · « prépare le plan stratégique de l'année » · avant une décision d'investissement (embauche, nouveau service, nouvelle zone) · en albanais : « pozicioni ynë në treg », « analiza e tregut », « ku qëndrojmë ndaj konkurrencës ».

## Input attendu

**Rien d'obligatoire** : l'agent démarre avec les données de `references/rushiti-defaults.md` et la collecte décrite en procédure.

Optionnel, et chaque élément fourni remplace un `PLACEHOLDER` par du réel :
- chiffres internes (CA par service, panier moyen, taux de transformation devis→chantier, part de chaque type de client) ;
- concurrents qu'Isuf considère comme sérieux (nom et/ou site) ;
- retours terrain (motifs de refus de devis, questions récurrentes des clients, délais concurrents constatés).

Si une seule information manquante change la conclusion (ex. : la part du B2B syndics dans le CA), poser **une** question courte — pas un interrogatoire. En mode autonome, remplir avec `PLACEHOLDER` et le signaler dans « Méthode & limites ».

## Procédure

1. **Cadrer.** Périmètre par défaut : RUSHITI Rénovation, marché de la rénovation intérieure, zone Besançon + communes du Doubs (liste dans `references/rushiti-defaults.md`). Lire ce fichier avant d'écrire quoi que ce soit : services, différenciateurs, clients cibles, normes — c'est la matière première du SWOT et du positionnement.

2. **Collecter le contexte de marché (sourcé).** Par recherche web : cadre réglementaire et aides en vigueur (TVA réduite 10 %/5,5 %, MaPrimeRénov', obligations DPE) **revérifiés à la source officielle au moment de l'analyse, jamais de mémoire** ; tendances de coût des matériaux et de main-d'œuvre dans le bâtiment ; signaux locaux (bâti ancien bisontin, copropriétés, projets urbains). Chaque fait retenu porte sa source et sa date. Un fait non vérifiable est écarté ou marqué `[À VÉRIFIER]`.

3. **Cartographier la concurrence locale par archétypes.** Quatre archétypes structurent le marché d'un artisan rénovateur ; pour chacun, chercher 1-2 représentants réels de la zone (recherche web, SERP locale, fiches Google publiques) :
   - **artisans indépendants** (peintres, plaquistes solo ou très petites équipes) ;
   - **entreprises structurées locales** (équivalents directs de RUSHITI) ;
   - **grandes enseignes / réseaux nationaux** (pose standardisée, notoriété) ;
   - **plateformes de mise en relation** (captent la demande en ligne, sous-traitent).
   Ne retenir que des acteurs réels du métier et de la zone. Les données publiques (note Google, nombre d'avis, services affichés, présence web) se relèvent telles quelles ; tout le reste est `PLACEHOLDER` ou « non mesuré ».

4. **Analyser les cinq forces** (grille adaptée à l'artisan local, voir structure de sortie) : intensité concurrentielle locale, pouvoir des clients (particuliers vs syndics vs assurances), pouvoir des fournisseurs et rareté de la main-d'œuvre qualifiée, menace des nouveaux entrants, menace des substituts (bricolage, report des travaux, plateformes). Chaque force reçoit une évaluation qualitative argumentée (Faible / Moyenne / Élevée) **et** sa conséquence concrète pour RUSHITI.

5. **Construire la matrice de positionnement.** Positionner les quatre archétypes et RUSHITI sur les axes qui comptent pour un client local : niveau de prix, étendue de la prestation (geste isolé vs solution complète préparation + traitement + finition), réassurance (garanties, diagnostic gratuit, avis), présence digitale. Identifier **l'espace que RUSHITI occupe ou doit occuper** — typiquement : la qualité et la traçabilité d'une entreprise structurée, avec la proximité et la pédagogie d'un artisan.

6. **Rédiger le SWOT ancré dans le réel.** Forces et faiblesses **internes** tirées des données RUSHITI (20 ans d'expérience, diagnostic gratuit sur site, expertise bâti ancien, structure IRSI pour les sinistres, taille de l'équipe, dépendance aux dirigeants…) ; opportunités et menaces **externes** tirées des étapes 2-4. Chaque entrée est un fait précis, pas une généralité (« Forte notoriété » interdit ; « PLACEHOLDER avis Google, note PLACEHOLDER, contre X avis chez [concurrent] » autorisé).

7. **Formuler la déclaration de positionnement** (2-3 phrases, gabarit en structure de sortie) : pour qui, contre quelles alternatives, avec quelle preuve. Elle doit être **défendable avec les preuves collectées** — sinon la reformuler plus modestement.

8. **Prioriser le plan d'action et router chaque action** vers le skill RUSHITI qui l'exécute (table de routage ci-dessous). Ordre de priorité : (1) actions qui protègent le CA existant, (2) actions qui exploitent une opportunité déjà à portée, (3) paris à moyen terme. Une conclusion sans action routée n'a pas sa place dans le rapport.

9. **Rédiger le rapport** selon la structure de sortie : daté, sourcé, chaque `PLACEHOLDER` restant listé dans « Méthode & limites » avec la donnée qui permettrait de le remplacer.

## Table de routage des actions

| Conclusion stratégique | Action | Skill RUSHITI à lancer |
|---|---|---|
| Segment B2B (syndics, gestionnaires, assurances) sous-exploité | prospecter le premier contact | `rushiti-prospection-b2b` puis `rushiti-relance-b2b` |
| Écart SEO précis face à un concurrent nommé | analyse d'écart détaillée | `rushiti-ecart-concurrentiel` |
| Déficit de réassurance en ligne (avis, note) | collecte et réponses aux avis | `rushiti-avis-google`, `rushiti-fiche-google-business` |
| Demande locale non couverte (service × quartier/commune) | créer la page locale | `rushiti-brief-seo` puis `rushiti-page-locale` |
| Question de prix récurrente non adressée | page chiffrée (prix au m², TVA, aides) | `rushiti-pages-donnees` |
| Preuve d'expertise invisible (chantiers non racontés) | études de cas avant/après | `rushiti-etudes-de-cas` |
| Notoriété faible auprès des prescripteurs | présence LinkedIn/réseaux | `rushiti-reseaux-sociaux`, `rushiti-stats-linkedin` |
| Demande captée par les plateformes/moteurs IA | visibilité IA et part de voix | `rushiti-visibilite-ia`, `rushiti-part-de-voix-ia` |
| Acquisition payante à cadrer | campagne Search locale | `rushiti-google-ads` |
| Trésorerie fragilisée par les délais de paiement | suivi et relances | `rushiti-suivi-paiements` |

## Structure de sortie (gabarit)

Rapport **markdown à coller**, en français, interne. Reproduire cette ossature — **aucune section ne reste vide** :

```
# Profil de positionnement de marché — RUSHITI Rénovation
Zone : Besançon / Doubs · Sources : [recherche web sourcée, fiches Google publiques, données Isuf] · Date : [JJ/MM/AAAA]

## 1. Contexte du marché local
- Réglementaire / aides : [faits vérifiés à la source officielle, avec source et date]
- Économique : [coûts matériaux/main-d'œuvre — conséquence locale concrète]
- Demande locale : [bâti ancien, copropriétés, sinistres — signaux observés]
(chaque fait : source + date ; sinon [À VÉRIFIER])

## 2. Cinq forces du marché local
| Force | Évaluation | Pourquoi | Conséquence pour RUSHITI |
|---|---|---|---|
| Intensité concurrentielle locale | … | … | … |
| Pouvoir des clients (particuliers / syndics / assurances) | … | … | … |
| Fournisseurs & main-d'œuvre qualifiée | … | … | … |
| Nouveaux entrants | … | … | … |
| Substituts (bricolage, report, plateformes) | … | … | … |

## 3. Matrice de positionnement
| Acteur | Prix | Étendue de prestation | Réassurance (garanties, avis) | Présence digitale | Espace laissé à RUSHITI |
|---|---|---|---|---|---|
| Artisans indépendants | … | … | … | … | … |
| Entreprises structurées locales | … | … | … | … | … |
| Grandes enseignes / réseaux | … | … | … | … | … |
| Plateformes de mise en relation | … | … | … | … | … |
| **RUSHITI Rénovation** | … | … | … | … | position visée : … |
(données publiques relevées telles quelles ; PLACEHOLDER ou « non mesuré » sinon)

## 4. SWOT
| Forces (internes) | Faiblesses (internes) |
|---|---|
| [faits précis, sourcés dans les données RUSHITI] | [faits précis, assumés] |

| Opportunités (externes) | Menaces (externes) |
|---|---|
| [tirées des sections 1-3, avec source] | [tirées des sections 1-3, avec source] |

## 5. Déclaration de positionnement
Pour [segment prioritaire] à Besançon et dans le Doubs, RUSHITI Rénovation est [catégorie revendiquée],
contrairement à [alternative principale], parce que [preuves : 20 ans de métier, diagnostic gratuit sur site,
expertise bâti ancien, garanties décennale/biennale, structure IRSI pour les sinistres].

## 6. Plan d'action priorisé
- Vague 1 — protéger le CA existant : [action → skill RUSHITI]
- Vague 2 — exploiter les opportunités à portée : [action → skill RUSHITI]
- Vague 3 — paris à moyen terme : [action → skill RUSHITI]

## 7. Méthode & limites
Sources et dates de collecte. Liste des PLACEHOLDER restants et de la donnée interne qui permettrait
de les remplacer. Rappel : évaluations qualitatives = jugement argumenté à date, pas des garanties.
Analyse interne RUSHITI, non destinée à publication.
```

## Règles d'écriture

- **Rapport interne**, pour Isuf/Yll : ton direct et factuel, pas de formule d'appel ni de signature client, pas de CTA commercial. La trame pédagogique s'applique quand même : chaque conclusion explique son pourquoi.
- **Toutes les cases remplies, honnêtement.** Le « premium » de ce profil, c'est sa complétude *vérifiable* : une case porte une donnée sourcée, un `PLACEHOLDER` nommé, ou la mention « non mesuré » — jamais un vide, jamais un chiffre décoratif. Un profil troué fait prendre de mauvaises décisions ; un profil bourré de chiffres inventés, des pires encore.
- **Toujours dater et sourcer.** Les aides, la TVA, les seuils réglementaires changent ; un fait réglementaire se revérifie à la source officielle au moment de l'analyse, jamais de mémoire. Une analyse non datée induit en erreur dans six mois.
- **Qualitatif assumé.** Les cinq forces et la matrice sont des évaluations argumentées (Faible / Moyenne / Élevée + pourquoi), pas des scores pseudo-précis. Écrire « évaluation qualitative » là où c'en est une.
- **Local d'abord.** Une tendance nationale n'entre dans le rapport que traduite en conséquence Besançon/Doubs. Le marché pertinent d'un artisan, c'est sa zone de chantier, pas la France.
- **Chaque conclusion débouche sur une action routée.** Un SWOT qui ne déclenche rien est un exercice de style ; la valeur du profil est dans la vague 1 du plan d'action.
- **Le gain reste une estimation.** « Opportunité estimée », jamais « vous gagnerez X chantiers » : ce serait une promesse.

## Pièges à éviter

- **Produire une analyse générique de « société de rénovation digitale française »** (frameworks remplis d'hypothèses nationales plausibles, concurrents parisiens, chiffres ronds inventés) → tout ancrer dans le réel RUSHITI : entreprise de terrain à Besançon, 20 ans de métier, clientèle particuliers + syndics + assurances. Si une donnée locale manque, `PLACEHOLDER`, pas une hypothèse maquillée en fait.
- **Confondre complétude et remplissage** → « toutes les cases remplies » signifie données réelles ou lacunes explicitement qualifiées, jamais des valeurs fabriquées pour faire complet.
- **Citer un dispositif d'aide ou un taux de TVA de mémoire** → revérifier à la source officielle à chaque analyse ; ces règles changent chaque année.
- **Positionner RUSHITI par rapport à des acteurs hors marché** (plateformes nationales sans présence locale, enseignes absentes du Doubs) → ne garder que les alternatives qu'un client bisontin considère réellement.
- **Rédiger un SWOT de généralités** (« bonne réputation », « marché porteur ») → chaque entrée est un fait précis, sourcé, daté.
- **Livrer l'analyse sans plan d'action routé** → chaque conclusion pointe vers un skill RUSHITI, sinon rien ne se fait.
- **Dénigrer un concurrent nommé** → l'analyse est interne et factuelle ; elle compare, elle n'attaque pas.

## Exemple complet

**Input :** « Fais le point sur notre position sur le marché, on hésite à pousser plus fort côté syndics. »

**Output (extrait) :**

```
# Profil de positionnement de marché — RUSHITI Rénovation
Zone : Besançon / Doubs · Sources : recherche web (sources officielles citées), fiches Google publiques,
données internes PLACEHOLDER · Date : PLACEHOLDER (date d'analyse)

## 1. Contexte du marché local
- Réglementaire / aides : TVA réduite en rénovation de logement — taux et conditions à revérifier sur
  service-public.fr / impots.gouv.fr à la date de l'analyse [source + date de consultation].
- Demande locale : parc important de bâti ancien à Besançon (Battant, centre) et de copropriétés
  gérées par syndics — segment où les sinistres dégât des eaux génèrent une demande récurrente,
  cadrée par la convention IRSI.

## 2. Cinq forces du marché local (extrait)
| Force | Évaluation | Pourquoi | Conséquence pour RUSHITI |
|---|---|---|---|
| Pouvoir des clients | Élevée (particuliers), Moyenne (syndics) | le particulier compare plusieurs devis ; le syndic cherche surtout un intervenant fiable et conforme IRSI | face aux syndics, la conformité IRSI et la réactivité pèsent plus que le prix — argument à porter par rushiti-prospection-b2b |
| Substituts | Moyenne | report des travaux et bricolage sur les petits gestes ; pas de substitut crédible sur sinistres et chantiers complets | concentrer l'effort commercial sur les prestations complètes et les sinistres |

## 3. Matrice de positionnement (extrait)
| Acteur | Prix | Étendue de prestation | Réassurance | Présence digitale | Espace laissé à RUSHITI |
|---|---|---|---|---|---|
| Artisans indépendants | non mesuré | geste isolé le plus souvent | variable, peu d'avis en ligne | très faible | la solution complète tracée (devis structuré, garanties, suivi) |
| **RUSHITI Rénovation** | PLACEHOLDER | complète : préparation + traitement + finition | 20 ans, décennale, diagnostic gratuit, PLACEHOLDER avis Google | site + fiche Google | position visée : l'entreprise structurée qui garde la proximité d'un artisan |

## 4. SWOT (extrait)
| Forces (internes) | Faiblesses (internes) |
|---|---|
| Structure de devis conforme IRSI pour les sinistres — rare chez les indépendants locaux | Notoriété en ligne : PLACEHOLDER avis Google, à comparer aux concurrents relevés |

## 5. Déclaration de positionnement
Pour les syndics et gestionnaires de biens de Besançon, RUSHITI Rénovation est l'entreprise de
rénovation qui traite un sinistre de bout en bout — diagnostic gratuit sur site, devis conforme IRSI,
réfection complète préparation + traitement + finition — contrairement à l'artisan isolé qu'il faut
piloter, avec 20 ans de métier et une garantie décennale à l'appui.

## 6. Plan d'action priorisé
- Vague 1 — protéger le CA : consolider la réassurance en ligne (avis) → rushiti-avis-google.
- Vague 2 — opportunité à portée : prospection ciblée des syndics du centre et de Battant →
  rushiti-prospection-b2b, appuyée par la page syndic existante et des études de cas → rushiti-etudes-de-cas.
- Vague 3 — moyen terme : mesurer la part de voix dans les réponses IA → rushiti-part-de-voix-ia.

## 7. Méthode & limites
PLACEHOLDER restants : part du B2B dans le CA, panier moyen, nombre d'avis Google à date —
remplaçables par les chiffres internes d'Isuf et un relevé de la fiche Google. Évaluations des forces =
jugement qualitatif argumenté à date. Analyse interne, non destinée à publication.
```

## Garde-fous

- **Lecture seule** : l'agent diagnostique et propose ; il ne crée, ne modifie ni ne publie aucune page, et n'envoie rien.
- **Aucun chiffre inventé** : part de marché, prix, volume, note — uniquement des valeurs réellement collectées et sourcées. À défaut, `PLACEHOLDER` ou « non mesuré », listés en fin de rapport.
- **Aucun fait réglementaire de mémoire** : aides et taux revérifiés à la source officielle à chaque analyse.
- **Le gain est une estimation**, jamais une promesse chiffrée.
- **Analyse interne** : aucun livrable public, aucun dénigrement de concurrent nommé.
- **Validation** : les actions proposées ne s'exécutent qu'après accord d'Isuf, via les skills routés.
