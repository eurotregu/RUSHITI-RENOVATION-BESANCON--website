# Audit des mots-clés cibles — rushiti-renovation.fr — 20/08/2026

> Audit **en lecture seule**. Rien n'a été modifié en production. Chaque
> décision listée ici attend la validation d'Isuf avant exécution.

> **Lire d'abord l'addendum en fin de document (20/08/2026, soir).** Il
> corrige le constat 2 sur la foi du code source, intègre les chiffres réels
> de Search Console et liste les corrections déjà appliquées.

## Ce qu'il faut retenir en dix lignes

Le site compte **1 395 URLs**, dont **1 368 pages « service × zone »** : exactement
**18 services × 76 zones**, sans une seule exception. La couverture n'est donc pas
le résultat d'une sélection de mots-clés — c'est un **produit cartésien**. Les
pages elles-mêmes sont bonnes (≈ 1 400 mots, paragraphes réellement locaux, FAQ,
maillage), mais le **choix des cibles** n'arbitre rien : Pontarlier reçoit le même
traitement que Champoux (≈ 90 habitants, chiffre affiché sur la page), et deux
couples de services se disputent la même intention **sur les 76 zones à la fois**
(`isolation-` vs `isolation-interieure-`, `papier-peint-` vs `toile-de-verre-`),
soit **304 pages en concurrence interne par construction**.

En parallèle, l'outil d'analyse sémantique travaille sur des requêtes qui
n'existent pas : sur les **46 analyses NeuronWriter** du projet, **22 portent sur
12 pseudo-requêtes de disponibilité** (« intervention 24/7 peinture besançon »,
« peinture écologique besançon disponible vite »…), **4 sur des slugs d'URL** et
**4 sur des chaînes de marque**. Moins d'un tiers des analyses porte sur une
requête qu'un client de Besançon peut taper.

Enfin, **aucune donnée de demande n'entre aujourd'hui dans la décision** : pas de
connecteur Semrush, pas de volume renvoyé par NeuronWriter, pas d'export Search
Console fourni. La priorisation ci-dessous est donc **qualitative et le dit** —
et la première action recommandée est précisément de rétablir la mesure.

## Fichiers livrés avec cet audit

| Fichier | Contenu |
|---|---|
| `docs/seo/audit-mots-cles-cibles-2026-08.md` | Ce rapport |
| `docs/seo/matrice-mots-cles-cibles-2026-08.csv` | 40 clusters : pivot, intention, page cible, statut, décision, priorité, agent à saisir |
| `docs/seo/inventaire-grille-paliers-2026-08.csv` | Les 76 zones, leur palier proposé et le nombre de pages à conserver ou consolider |

## Périmètre, sources et limites

| Élément | Valeur |
|---|---|
| Site audité | rushiti-renovation.fr (un site par audit ; rushiti.fr non traité ici) |
| Date du relevé | 20/08/2026 |
| Inventaire d'URLs | Sitemaps du site via Firecrawl — 1 395 URLs uniques |
| Contrôle de contenu | Relevé complet de `/cloisons-champoux` et `/isolation-interieure-besancon` |
| Titles et metas | Relevés dans l'inventaire du 20/08/2026 (sitemap + index de recherche) |
| Historique sémantique | NeuronWriter, projet `rushiti-renovation.fr` — 46 analyses |
| Volumes de recherche | **Aucun.** Semrush non connecté ; NeuronWriter ne renvoie ni volume ni difficulté |
| Positions et impressions | **Aucune.** Export Google Search Console non fourni |

**Conséquence méthodologique :** priorisation **qualitative** (valeur business >
axe géographique > demande supposée), jamais chiffrée. Aucun volume n'est estimé
dans ce rapport ; une case vide reste vide. Les décisions de fusion ou de
suppression de pages sont **conditionnées à l'export Search Console** : on ne
supprime pas une page qui imprime déjà.

**Deux accès bloqués pendant l'audit**, sans effet sur les conclusions : l'accès
réseau direct au domaine depuis l'environnement (contourné via Firecrawl), et
l'absence de métriques dans les réponses NeuronWriter.

---

## Volet 1 — Anatomie du ciblage actuel

### L'inventaire, en chiffres

| Catégorie | Nombre d'URLs |
|---|---|
| Pages « service × zone » (la grille) | **1 368** |
| Pages piliers et B2B hors grille | 10 |
| Pages utilitaires (accueil, contact, à propos, réalisations, zones, mentions, simulateur) | 7 |
| Blog (index + articles) | 11 |
| **Total** | **1 395** |

### La grille : 18 services × 76 zones, sans exception

Les 18 services déclinés sur chaque zone : `peinture-interieure`,
`peinture-exterieure`, `degat-des-eaux`, `platrerie`, `cloisons`, `faux-plafonds`,
`doublage-murs`, `isolation`, `isolation-interieure`, `ratissage-enduit`,
`papier-peint`, `toile-de-verre`, `revetements-sol`, `parquet-flottant`,
`sol-pvc`, `lino-vinyle-lvt`, `vitrification-parquet`, `ragreage-sol`.

Contrôle d'homogénéité : **75 zones sur 76 ont exactement 18 pages**, la
76e (Besançon) en a 27 — les 18 de la grille plus les 9 pages piliers propres à
la ville. Autrement dit, **aucune zone n'a été traitée différemment d'une autre**.

Les 76 zones : Besançon et ses 13 quartiers (Battant, Bregille, Butte-Grette,
Centre-ville, Chaprais, Montrapon, Palente, Planoise, Saint-Claude,
Saint-Ferjeux, Tilleroyes, Vaîte-Clairs-Soleils, Velotte), Pontarlier et le
Haut-Doubs (Arçon, Doubs, Houtaud, Vuillecin), Montbéliard, et 57 communes de la
couronne bisontine — jusqu'à des villages comme Champoux, Gratteris, Thoraise,
La Chevillotte ou Vaux-les-Prés.

### Ce qui est déjà bien fait — à ne pas casser

Ces points sont solides et l'audit ne recommande **pas** d'y toucher :

- **Le silo Dégât des eaux est complet et bien pensé** : page Besançon, 75 pages
  communes, page devis assurance, trois articles de blog (mur, plafond, qui paie
  quoi). C'est le silo le plus rentable du métier, et c'est celui qui est le mieux
  couvert. Rien à redire.
- **Les pages de la grille ne sont pas des coquilles vides.** Relevé sur
  `/cloisons-champoux` : ≈ 1 400 mots, un paragraphe réellement spécifique à la
  commune (distance à Besançon, nombre d'habitants, nature du bâti), méthode en
  quatre étapes, FAQ de cinq questions, maillage vers les autres services de la
  même commune. C'est très au-dessus du niveau habituel des pages locales
  générées.
- **Le vocabulaire client est respecté dans les titles piliers** : « Peintre à
  Besançon » plutôt que « peinture intérieure », « Plâtrerie & placo » plutôt que
  « travaux de plâtrerie ». La page d'accueil vise « Peintre & plaquiste à
  Besançon », qui est bien le pivot du métier.
- **Le maillage transversal existe** : chaque page de zone renvoie aux autres
  services de la même zone et aux zones voisines du même service.
- **L'axe informationnel est amorcé proprement** : les 10 articles de blog
  ciblent de vrais symptômes (auréole, moisissure salle de bains, fissures,
  ragréage avant parquet) et mènent vers une page service.

---

## Volet 2 — Les constats, par gravité

### 🔴 Constat 1 — La sélection des mots-clés est un produit cartésien, pas un arbitrage

**Fait :** 18 services × 76 zones = 1 368 pages, 75 zones sur 76 ayant exactement
le même jeu de 18 pages.

**Pourquoi c'est un problème.** Une sélection de mots-clés cibles, c'est un choix :
quelles requêtes méritent une page, lesquelles n'en méritent pas. Ici, aucun
choix n'a été fait — la grille a été remplie. Cela produit des cibles comme
« vitrification parquet Champoux » ou « lino vinyle LVT Gratteris », requêtes que
personne ne tape dans un village de quelques dizaines de foyers, tandis que
l'effort d'écriture, le budget de crawl et l'autorité interne se répartissent à
parts égales entre une page à demande réelle et une page à demande nulle.

**Le risque concret** n'est pas seulement l'inefficacité : une masse de pages
quasi jumelles à faible demande est exactement le profil que Google traite comme
des *doorway pages*. Le contenu étant ici de bonne qualité, le risque est
modéré — mais il croît avec le nombre de pages qui n'obtiennent jamais
d'impression.

**Décision recommandée :** ne rien supprimer avant l'export Search Console, puis
appliquer la logique de paliers du Volet 4.

### 🔴 Constat 2 — Deux couples de services se disputent la même intention sur les 76 zones

**Fait 1 — Isolation.** Relevé du 20/08/2026 :

| URL | Title relevé |
|---|---|
| `/isolation-besancon` | Isolation intérieure à Besançon — murs et plafonds \| RUSHITI |
| `/isolation-interieure-besancon` | Isolation intérieure (ITI) Besançon \| RUSHITI |

Les deux titles commencent par « Isolation intérieure » et visent Besançon. La
page `/isolation-interieure-besancon` renvoie elle-même vers `/isolation-besancon`
sous le libellé « isolation (tous travaux) » : la hiérarchie voulue existe dans
la tête de l'auteur, **mais pas dans les titles**, donc pas dans la SERP. Le
couple est répliqué **sur les 76 zones : 152 pages**.

**Fait 2 — Papier peint et toile de verre.** Les pages `papier-peint-<zone>` sont
titrées « Papier peint **& toile de verre** <zone> » (relevé sur
`/papier-peint-boussieres` et `/papier-peint-besancon`) alors qu'une page
`toile-de-verre-<zone>` dédiée existe pour chacune des 76 zones. Là encore :
**152 pages, deux cibles, une seule intention servie deux fois**.

**Ce qui n'est PAS un problème, pour être juste :** `platrerie` / `cloisons` /
`faux-plafonds` / `doublage-murs` d'un côté, et `revetements-sol` /
`parquet-flottant` / `sol-pvc` / `lino-vinyle-lvt` / `vitrification-parquet` /
`ragreage-sol` de l'autre, correspondent à des requêtes réellement distinctes
(« faux plafond » n'est pas « cloison », « ragréage » n'est pas « parquet
flottant »). Ces familles sont légitimes **à l'échelle de Besançon**. C'est leur
réplication mécanique sur 76 zones qui pose problème, pas leur existence.

**Décision recommandée (Volet 4, vague 2) :** différencier les titles, ce qui se
règle dans deux gabarits et non page par page.

### 🟠 Constat 3 — Trois pages se disputent la façade à Besançon

| URL | Title relevé | Intention visée |
|---|---|---|
| `/peinture-exterieure-besancon` | Ravalement, crépi & peinture de façade à Besançon \| RUSHITI | ravalement + peinture façade |
| `/ravalement-facade-besancon` | *(non relevé)* | ravalement façade |
| `/peinture-facade-isolation-exterieure-besancon` | Peinture façade isolée par l'extérieur à Besançon \| RUSHITI | façade sous ITE |

La troisième est légitime et bien ciblée : « peinture de façade isolée par
l'extérieur » est une vraie niche, distincte, et elle a fait l'objet d'une
analyse NeuronWriter le 18/08/2026. Le problème est le doublon entre les deux
premières : le title de `/peinture-exterieure-besancon` revendique explicitement
« Ravalement » alors qu'une page `/ravalement-facade-besancon` existe.

**Décision recommandée :** une seule page porte « ravalement façade Besançon ».
Soit `/ravalement-facade-besancon` devient la page de référence et
`/peinture-exterieure-besancon` retire « Ravalement » de son title, soit
l'inverse et `/ravalement-facade-besancon` fusionne en 301. À trancher au vu des
impressions Search Console.

### 🟠 Constat 4 — Inversion de la priorité géographique

**Fait :** Pontarlier, Montbéliard, École-Valentin, Thise, Champoux, Gratteris et
Thoraise reçoivent **exactement le même nombre de pages** (18) et le même
gabarit.

La stratégie de référence de la suite RUSHITI fixe pourtant un ordre :
Besançon et ses quartiers, puis Pontarlier (clientèle frontalière), puis les
autres pôles. Aujourd'hui, cet ordre n'existe nulle part dans la structure du
site : rien ne signale à Google — ni aux visiteurs — que Pontarlier compte plus
que Champoux. Aucune page Pontarlier n'a de profondeur supplémentaire, de
contenu propre au Haut-Doubs, ni de maillage renforcé.

**Décision recommandée :** créer un écart visible entre les paliers (Volet 4),
et enrichir en priorité les 18 pages de Pontarlier plutôt que d'en créer de
nouvelles ailleurs.

### 🟠 Constat 5 — Le silo « Rénovation de pièce » est presque absent

Sur les six silos de référence, cinq sont couverts en profondeur (Peinture,
Plâtrerie/placo, Sols, Dégât des eaux, Isolation). Le sixième — **Rénovation de
pièce** — repose sur une seule page : `/renovation-appartement-besancon`.

Manquent donc, alors que ce sont des prestations réellement assurées par
l'entreprise et des requêtes à forte valeur commerciale :

- rénovation de **salle de bains** à Besançon ;
- rénovation de **cuisine** à Besançon ;
- **entreprise de rénovation** / rénovation de **maison** à Besançon (la requête
  « chapeau » du métier, aujourd'hui servie par aucune page dédiée).

C'est le plus gros trou de couverture du site : 1 368 pages produites, et le
silo le plus proche du panier moyen élevé en compte une.

### 🟠 Constat 6 — La moitié des analyses sémantiques porte sur des requêtes qui n'existent pas

Sur les **46 analyses** du projet NeuronWriter `rushiti-renovation.fr` :

| Nature de la requête analysée | Analyses | Requêtes distinctes |
|---|---|---|
| Pseudo-requêtes de disponibilité (« disponible », « immédiat », « urgence », « 24/7 », « rapide ») | **22** | 12 |
| Slugs d'URL passés comme mots-clés (`revetements-sol-besancon`, `travaux-de-peinture/peinture-pour-degat-des-eaux/`…) | 4 | 4 |
| Chaînes de marque ou de title (« … \| rushiti », « … assurance habitation allianz \| rushiti ») | 4 | 4 |
| Trop génériques, hors périmètre local (« rénovation », « moisissures ») | 2 | 2 |
| **Requêtes réellement plausibles** | **≈ 13** | ≈ 13 |

Les 22 analyses de disponibilité proviennent **d'une seule session, le
15/02/2026**, et comportent des doublons purs (« peinture appartement disponible
besançon » analysée 4 fois, « peinture façade besançon disponible immédiatement »
3 fois).

**Pourquoi c'est grave pour la sélection de mots-clés :** ces libellés sont des
arguments d'annonce publicitaire, pas des requêtes. Un habitant de Besançon tape
« peintre besançon », « devis peinture appartement besançon », éventuellement
« peintre besançon urgence » — pas « peinture appartement disponible besançon ».
Chaque analyse lancée sur une pseudo-requête produit un brief calé sur un
vocabulaire absent des SERP, et consomme un crédit qui aurait servi un vrai
pivot.

**À noter, à l'inverse :** les analyses de 2026 les plus récentes (dégât des
eaux, plaquiste, isolation intérieure, rénovation appartement, peinture de façade
isolée par l'extérieur) sont, elles, **bien choisies**. La dérive est datée, elle
n'est pas la pratique actuelle — mais l'historique pollue le projet.

### 🟡 Constat 7 — Aucune donnée de demande n'entre dans la décision

Ni volume, ni difficulté, ni impression, ni position n'était disponible pendant
cet audit. La sélection des mots-clés cibles se fait donc aujourd'hui « au
jugé » — ce qui explique mécaniquement les constats 1, 4 et 6.

**Trois données débloquent tout le reste :**

1. **Export Search Console 12 mois**, onglet Performances, dimensions *Requêtes*
   **et** *Pages* (deux exports). C'est la seule source qui dira quelles pages de
   la grille impriment réellement, et sur quelles requêtes.
2. **Couverture d'indexation Search Console** : combien des 1 368 pages de la
   grille sont réellement indexées, et combien sont en « Explorée, actuellement
   non indexée » — le symptôme classique d'une grille trop large.
3. **Volumes** : connecteur Semrush, ou à défaut Google Keyword Planner sur les
   ≈ 25 pivots du Volet 3.

### 🟡 Constat 8 — Signal dilué entre `www` et non-`www` (à vérifier)

L'index de recherche interrogé pendant l'inventaire renvoie certaines pages sous
`https://www.rushiti-renovation.fr/…` et d'autres sous
`https://rushiti-renovation.fr/…` (exemples relevés :
`www.rushiti-renovation.fr/isolation-interieure-la-chevillotte`,
`www.rushiti-renovation.fr/renovation-syndic-gestionnaire-besancon`). Le sitemap,
lui, ne contient **que** la forme sans `www`.

Deux URLs pour une même page, c'est un signal partagé en deux sur le même mot-clé.
**À vérifier au crawl** (redirection 301 `www` → non-`www` et canonical) — ce
point sort du périmètre « mots-clés » : → **rushiti-audit-site**.

Rappel : la consolidation des domaines (`rushiti.fr`, `rushiti-peinture.fr`)
reste ouverte depuis l'audit du 13/08/2026 (point P0-A). Tant qu'elle n'est pas
tranchée, deux sites peuvent viser les mêmes mots-clés.

---

## Volet 3 — Carte des mots-clés cibles, par silo

Statuts : ✅ couvert et bien ciblé · 🟡 couvert mais cible à corriger · 🔴 manquant.
Colonne Volume vide = donnée absente, jamais estimée.

### Silo 1 — Peinture

| Cluster (requête pivot) | Intention | Volume | Statut | Page cible | Décision |
|---|---|---|---|---|---|
| peintre besançon | Locale/transac. | — | ✅ | `/peinture-interieure-besancon` | Ne rien changer : le title dit bien « Peintre à Besançon » |
| peinture intérieure <commune> | Locale | — | ✅ | `peinture-interieure-<zone>` ×76 | Conserver sur tous les paliers |
| ravalement façade besançon | Locale/transac. | — | 🟡 | `/ravalement-facade-besancon` **et** `/peinture-exterieure-besancon` | Doublon : une seule page porte la cible (constat 3) |
| peinture façade isolée par l'extérieur | Locale/niche | — | ✅ | `/peinture-facade-isolation-exterieure-besancon` | Bonne niche, à garder distincte |
| papier peint besançon | Locale/transac. | — | 🟡 | `papier-peint-<zone>` ×76 | Retirer « & toile de verre » du title |
| toile de verre besançon | Locale/transac. | — | 🟡 | `toile-de-verre-<zone>` ×76 | Devient seule porteuse de la cible |
| ratissage / enduit de lissage besançon | Locale/technique | — | ✅ | `ratissage-enduit-<zone>` ×76 | Cible technique juste, bien différenciée de la peinture |
| prix peinture m² besançon | Transac./informationnel | — | ✅ | `/blog/prix-peinture-interieure-besancon-2026` | Article qui fonctionne comme page prix : à mailler davantage |
| peinture bâti ancien / boucle besançon | Locale/niche | — | 🔴 | — | À arbitrer : angle différenciant fort, mais requête incertaine |

### Silo 2 — Plâtrerie / placo

| Cluster (requête pivot) | Intention | Volume | Statut | Page cible | Décision |
|---|---|---|---|---|---|
| plaquiste besançon | Locale/transac. | — | ✅ | `/plaquiste-besancon` | Vocabulaire client : à garder comme porte d'entrée |
| plâtrerie placo besançon | Locale/transac. | — | ✅ | `/platrerie-besancon` + 75 communes | Conserver |
| pose de cloison / créer une pièce | Locale/transac. | — | ✅ | `cloisons-<zone>` ×76 | Cible distincte, légitime |
| faux plafond besançon | Locale/transac. | — | ✅ | `faux-plafonds-<zone>` ×76 | Cible distincte, légitime |
| doublage de mur besançon | Locale/technique | — | 🟡 | `doublage-murs-<zone>` ×76 | Proche de l'ITI : à surveiller avec le couple isolation |
| prix placo au m² besançon | Transac. | — | 🔴 | — | Article de blog, sur le modèle de l'article prix peinture |

### Silo 3 — Sols

| Cluster (requête pivot) | Intention | Volume | Statut | Page cible | Décision |
|---|---|---|---|---|---|
| pose revêtement de sol besançon | Locale/transac. | — | ✅ | `revetements-sol-<zone>` ×76 | Page chapeau du silo |
| parquet flottant / stratifié besançon | Locale/transac. | — | ✅ | `parquet-flottant-<zone>` ×76 | Cible distincte |
| sol PVC / lino / LVT besançon | Locale/transac. | — | 🟡 | `sol-pvc-<zone>` **et** `lino-vinyle-lvt-<zone>` | Deux pages, un même univers produit : à fusionner hors palier A |
| vitrification parquet besançon | Locale/transac. | — | ✅ | `vitrification-parquet-<zone>` ×76 | Cible distincte |
| ragréage de sol besançon | Locale/technique | — | ✅ | `ragreage-sol-<zone>` ×76 | Cible distincte, appuyée par un article de blog |
| moquette besançon | Locale/transac. | — | 🔴 | — | Prestation assurée mais non ciblée : à arbitrer avec Isuf |

### Silo 4 — Dégât des eaux

| Cluster (requête pivot) | Intention | Volume | Statut | Page cible | Décision |
|---|---|---|---|---|---|
| dégât des eaux besançon | Locale/urgence | — | ✅ | `degat-des-eaux-<zone>` ×76 | Silo modèle, ne rien casser |
| devis dégât des eaux pour l'assurance | Transac./B2B | — | ✅ | `/devis-assurance-degat-des-eaux-besancon` | Conserver |
| réparer un plafond / un mur après fuite | Informationnel | — | ✅ | 2 articles de blog | Conserver |
| dégât des eaux : qui paie quoi (IRSI) | Informationnel | — | ✅ | `/blog/degat-des-eaux-assurance-qui-paie-quoi` | Conserver |
| assèchement après dégât des eaux besançon | Locale/technique | — | 🔴 | — | Sous-cible possible de la page dégât des eaux : renforcer plutôt que créer |

### Silo 5 — Isolation

| Cluster (requête pivot) | Intention | Volume | Statut | Page cible | Décision |
|---|---|---|---|---|---|
| isolation intérieure (ITI) besançon | Locale/transac. | — | 🟡 | `isolation-interieure-<zone>` ×76 | Garde la cible ITI |
| isolation besançon (chapeau, combles + phonique) | Locale/transac. | — | 🟡 | `isolation-<zone>` ×76 | Title à requalifier : ne doit plus dire « isolation intérieure » |
| isolation des combles besançon | Locale/transac. | — | 🟡 | traitée dans les deux pages ci-dessus | Cible à attribuer explicitement à la page chapeau |
| ITI ou ITE : que choisir | Informationnel | — | ✅ | `/blog/isolation-interieure-iti-perte-de-place-epaisseur` | Conserver |
| mur froid / condensation que faire | Informationnel | — | 🔴 | — | Article de blog à écrire (symptôme très tapé) |

### Silo 6 — Rénovation de pièce, B2B et transverse

| Cluster (requête pivot) | Intention | Volume | Statut | Page cible | Décision |
|---|---|---|---|---|---|
| rénovation appartement besançon | Locale/transac. | — | ✅ | `/renovation-appartement-besancon` | Conserver |
| **rénovation salle de bains besançon** | Locale/transac. | — | 🔴 | — | **Page à créer — priorité 1** |
| **entreprise de rénovation besançon** | Locale/transac. | — | 🔴 | — | **Page à créer — priorité 2** |
| **rénovation cuisine besançon** | Locale/transac. | — | 🔴 | — | **Page à créer — priorité 3** |
| aménagement de commerce / bureau besançon | B2B | — | ✅ | `/amenagement-commerce-bureau-besancon` | Conserver |
| syndic de copropriété / gestionnaire | B2B | — | ✅ | `/renovation-syndic-gestionnaire-besancon` | Conserver |
| remise en état de logement locatif | B2B | — | ✅ | `/remise-en-etat-logement-locatif-besancon` | Conserver |
| prix travaux de rénovation besançon | Transac. | — | ✅ | `/prix-travaux-renovation-besancon` | Conserver, mailler depuis les pages service |
| **expert d'assurance / cabinet de gestion de sinistres** | B2B | — | 🔴 | — | Cible B2B logique vu le silo dégât des eaux : à arbitrer |

---

## Volet 4 — Décision sur la grille : trois paliers de zones

**Principe :** cesser de traiter 76 zones à l'identique. Un palier = un jeu de
services proportionné à la demande plausible de la zone.

| Palier | Zones | Services conservés | Pages |
|---|---|---|---|
| **A — Cœur** | Besançon + ses 13 quartiers (14 zones) | **les 18** | 252 |
| **B — Pôles et couronne dense** | Pontarlier, Montbéliard, École-Valentin, Thise, Chalezeule, Saône, Pouilley-les-Vignes, Miserey-Salines, Pirey, Franois, Serre-les-Sapins, Châtillon-le-Duc, Avanne-Aveney, Beure, Morre, Montfaucon, Roche-lez-Beaupré, Novillars, Mamirolle, Marchaux, Grandfontaine, Boussières, Montferrand-le-Château, Dannemarie-sur-Crête (24 zones) | **10** : peinture intérieure, peinture extérieure, dégât des eaux, plâtrerie, cloisons, faux plafonds, isolation intérieure, revêtements de sol, papier peint, ratissage/enduit | 240 |
| **C — Villages** | les 38 zones restantes | **5** : peinture intérieure, dégât des eaux, plâtrerie, isolation intérieure, revêtements de sol | 190 |

La grille passerait de **1 368 à ≈ 682 pages**, chaque page supprimée étant
**redirigée en 301 vers la page du même service au palier supérieur** (ex.
`/vitrification-parquet-champoux` → `/vitrification-parquet-besancon`), jamais
vers l'accueil.

> ⚠️ **Condition impérative.** Cette consolidation ne s'exécute **qu'après**
> l'export Search Console. Toute page de palier B ou C qui imprime déjà sur une
> requête locale **est conservée**, quel que soit son palier théorique. On ne
> supprime jamais une page qui travaille : on supprime celles que personne ne
> voit. Sans ce contrôle, la manœuvre ferait perdre du trafic acquis.

**Effet attendu, sans promesse de classement :** budget de crawl concentré,
maillage interne resserré sur les pages qui peuvent réellement se classer, et
fin de la duplication d'intention à 76 exemplaires. Aucun gain de position n'est
garanti ici — c'est une remise en ordre du ciblage, pas un levier magique.

---

## Volet 5 — Pages à créer, priorisées

| Prio | URL proposée | Title proposé | Car. | Silo | Cluster servi | Justification |
|---|---|---|---|---|---|---|
| 1 | `/renovation-salle-de-bain-besancon` | `Rénovation de salle de bains à Besançon \| RUSHITI` | 52 | Rénovation de pièce | rénovation salle de bains besançon | Silo le plus rentable et le moins couvert ; prestation réellement assurée |
| 2 | `/entreprise-renovation-besancon` | `Entreprise de rénovation à Besançon \| RUSHITI` | 48 | Rénovation de pièce | entreprise de rénovation besançon | Requête chapeau du métier, aujourd'hui sans page dédiée |
| 3 | `/renovation-cuisine-besancon` | `Rénovation de cuisine à Besançon \| RUSHITI` | 45 | Rénovation de pièce | rénovation cuisine besançon | Complète le silo, même clientèle propriétaire |
| 4 | `/expert-assurance-sinistre-besancon` | `Sinistres : artisan pour experts à Besançon \| RUSHITI` | 55 | Dégât des eaux (B2B) | expert d'assurance, cabinet de gestion de sinistres | Prolonge le silo le plus fort vers sa clientèle B2B |
| 5 | Renforcement, pas création | — | — | Peinture | pontarlier + haut-doubs | Enrichir les 18 pages Pontarlier avant d'ouvrir une zone de plus |

> Création des pages locales : agent **rushiti-page-locale** (exige un gabarit
> HTML du site). Titles et metas : **seo-title-meta**. FAQ : **rushiti-faq**.
> Aucun prix, délai ni taux de TVA ne doit être affirmé sur ces pages sans
> validation d'Isuf.

**Ce que l'audit ne recommande PAS :** ouvrir de nouvelles communes. 76 zones
sont déjà couvertes ; le problème n'est pas l'étendue géographique, c'est la
profondeur là où la demande existe.

---

## Volet 6 — Clusters informationnels manquants (calendrier blog)

Chaque article existe pour pousser une page service par maillage interne, jamais
pour lui-même. Saisonnalité à confirmer avec **rushiti-google-trends** avant
calage définitif.

| Mois | Article (titre de travail) | Cluster servi | Page service à mailler |
|---|---|---|---|
| Sept. 2026 | Mur qui cloque ou peinture qui s'écaille : les causes | symptôme mur | `/peinture-interieure-besancon` |
| Oct. 2026 | Mur froid et condensation : isoler ou ventiler ? | mur froid / condensation | `/isolation-interieure-besancon` |
| Nov. 2026 | Fissure au plafond : quand faut-il s'inquiéter ? | fissure plafond | `/ratissage-enduit-besancon` |
| Déc. 2026 | Prix du placo au m² à Besançon | prix placo | `/platrerie-besancon` |
| Janv. 2027 | Papier peint qui se décolle : pourquoi, et quoi faire | symptôme papier peint | `/papier-peint-besancon` |
| Fév. 2027 | TVA 10 % ou 5,5 % sur vos travaux : les conditions | TVA travaux | `/prix-travaux-renovation-besancon` |
| Mars 2027 | Lire un devis de peinture sans se faire avoir | devis / prix | `/contact` |
| Avr. 2027 | Ravalement de façade : à quelle fréquence, et quels signes | ravalement | page façade retenue au constat 3 |

> Le sujet TVA reprend la règle de référence (10 % rénovation de plus de 2 ans,
> 5,5 % rénovation énergétique) : à **toujours conditionner**, jamais affirmer
> pour un cas précis.

---

## Volet 7 — Plan d'exécution en quatre vagues

### Vague 1 — Rétablir la mesure (aucun déploiement)

1. Exporter Search Console 12 mois : *Requêtes* et *Pages* (deux CSV), plus le
   rapport de couverture d'indexation. → **rushiti-opportunites-gsc**, puis
   retour ici pour chiffrer le Volet 4.
2. Nettoyer le projet NeuronWriter : archiver les 22 analyses de disponibilité et
   les 4 slugs, relancer les analyses sur les pivots du Volet 3.
3. Trancher la question du domaine principal, ouverte depuis le 13/08/2026
   (point P0-A). Dix minutes de décision qui débloquent tout le reste.

### Vague 2 — Corriger les cibles dupliquées (deux gabarits, 152 pages)

4. Requalifier le title des pages `isolation-<zone>` pour qu'elles ne visent plus
   « isolation intérieure » (proposition : `Isolation combles & phonique à
   <zone> | RUSHITI`) et laisser l'ITI à `isolation-interieure-<zone>`.
5. Retirer « & toile de verre » du title des pages `papier-peint-<zone>`.
6. Trancher le doublon façade (constat 3) et appliquer.

→ Exécution : **seo-title-meta** sur la liste complète des URLs concernées.

### Vague 3 — Consolider la grille (conditionnée à la vague 1)

7. Appliquer les paliers du Volet 4, page par page, en épargnant toute URL qui
   imprime dans Search Console. Redirections 301 vers le service au palier
   supérieur, mise à jour du sitemap et du maillage interne.
8. Contrôle d'indexation après coup → **rushiti-indexation**.

### Vague 4 — Combler les trous

9. Créer les pages 1 à 4 du Volet 5 → **rushiti-page-locale** + **rushiti-faq**.
10. Lancer le calendrier blog du Volet 6, un article par mois.
11. Enrichir les 18 pages Pontarlier (contenu propre au Haut-Doubs, maillage).

---

## Annexe A — Requêtes NeuronWriter à retirer du projet

Les 12 pseudo-requêtes de disponibilité, analysées 22 fois le 15/02/2026 :
« artisan peintre disponible besançon » (×2) · « peinture appartement disponible
besançon » (×4) · « peinture façade besançon disponible immédiatement » (×3) ·
« peinture extérieure besançon intervention rapide » (×2) · « remise en peinture
murs besançon immédiat » (×2) · « dépannage peinture besançon urgence » (×2) ·
« intervention immédiate peinture doubs » (×2) · « intervention 24/7 peinture
besançon » · « peinture écologique besançon disponible vite » · « retouches
peinture besançon urgent » · « peinture locative rapide besançon » · « entreprise
de peinture murs disponible immédiatement a besancon/rushiti ».

Slugs analysés comme mots-clés : `revetements-sol-besancon` ·
`degat-des-eaux-besancon` · `papier-peint-a-peindre-zone-humide-besancon/` ·
`travaux-de-peinture/peinture-pour-degat-des-eaux/`.

Chaînes de marque ou de title : « entreprise rushiti travaux de peinture interieur
a besancon doubs france » · « service de peintre en batiment a besançon france par
entreprise rushiti besancon » · « peinture après dégât des eaux-rushiti a
besançon » · « réparation après dégâts des eaux à besançon – assurance habitation
allianz | rushiti » (cette dernière cite une marque d'assureur tiers : à ne pas
reprendre comme cible).

Trop génériques pour un artisan local : « rénovation » · « moisissures ».

## Annexe B — Relevé hors périmètre « mots-clés », transmis pour information

Ces points sont sortis du relevé de contenu sans faire partie de l'audit de
mots-clés. Ils ne sont pas instruits ici, seulement signalés :

1. **Prix affichés sur les pages de la grille** (« à partir de 40–60 €/m² »
   sur `/cloisons-champoux`, « 45–70 €/m² » sur `/isolation-interieure-besancon`).
   À confirmer qu'ils ont bien été validés par Isuf — la règle de la suite est
   qu'aucun prix ne se publie sans validation.
2. **Assureur cité** : les pages mentionnent « Phénix Assurances / Tétris
   Assurance » alors que le fichier de référence de la suite indique ERGO. L'un
   des deux est à corriger → **rushiti-refresh-planner**.
3. **Mention « Qualification RGE »** sur `/isolation-interieure-besancon` : à
   confirmer (certification en cours de validité ?) avant tout appui SEO dessus.
4. **`www` / non-`www`** : cf. constat 8 → **rushiti-audit-site**.

---

*Audit réalisé le 20/08/2026 par l'agent rushiti-keyword-clusters. Lecture seule :
aucune page, aucun title, aucune redirection n'a été modifié. Aucun volume de
recherche n'est estimé dans ce document ; les cases vides le sont faute de
donnée. Aucun gain de position n'est promis.*

---

# Addendum du 20/08/2026 (soir) — vérification sur le code source et données Search Console

Après la première version de ce rapport, deux sources sont devenues accessibles :
le **dépôt du site en production** (`eurotregu/rushiti-renovation`, commit
`ad8cdcb` du 20/08/2026) et une **analyse Search Console** conservée dans le
Drive de l'entreprise (période 17/05 → 16/08/2026, relevé du 19/08/2026).
Tout ce qui suit prime sur la première version.

## A. Une correction : le constat 2 était partiellement faux

**Ce que disait la première version :** les titles de `/isolation-besancon` et de
`/isolation-interieure-besancon` commençaient tous deux par « Isolation
intérieure », donc visaient la même requête.

**Ce que dit le code source :**

| URL | Title réel dans le dépôt |
|---|---|
| `/isolation-besancon` | `Isolation Besançon – Devis gratuit \| RUSHITI` |
| `/isolation-interieure-besancon` | `Isolation intérieure (ITI) Besançon \| RUSHITI` |

Les H1 et les descriptions sont eux aussi distincts sur les 76 zones
(« Isolation thermique et phonique à… » contre « Isolation par l'intérieur
(ITI) à… »). **Le couple isolation est donc différencié dans les balises.**

**D'où venait l'erreur :** le title relevé (« Isolation intérieure à Besançon —
murs et plafonds ») provenait d'un index de recherche, pas du site : c'était un
titre **réécrit par Google**. Le contrôle a d'ailleurs montré que les
descriptions du même relevé (« 34 avis 4,7/5, visite et devis sous 48 h ») sont
elles aussi fabriquées par Google — l'expression « sous 48 h » n'existe que dans
un seul fichier du dépôt.

**Leçon de méthode, valable pour les prochains audits :** un title lu dans une
SERP ou dans un index tiers n'est pas le title du site. Tant que le code source
n'est pas consulté, une différence de balise reste une hypothèse.

**Ce qui reste vrai du constat 2 :** le risque de concurrence entre les deux
pages sur la requête « isolation <zone> » existe toujours — mais il se juge sur
les impressions, pas sur les balises. Search Console montre `/isolation-besancon`
à **184 impressions, position 28,3, zéro clic** : la page ne se classe pas, avec
ou sans doublon. Le sujet passe de « corriger les balises » à « renforcer la
page », et le verdict revient à **rushiti-cannibal-check** avec l'export
requête × page.

## B. Une confirmation : papier peint / toile de verre était bien un doublon

Vérifié fichier par fichier dans le dépôt :

- **73 pages sur 76** portaient « toile de verre » dans leur `<title>` ;
- **74 pages sur 76** dans leur `<h1>` ;
- **75 pages sur 76** dans leur `meta description` et leur `og:description` ;
- et **76 pages `toile-de-verre-<zone>` dédiées** existent en parallèle.

La page `papier-peint-besancon` avait déjà été corrigée dans ce sens : elle
servait de modèle.

## C. Les données Search Console (17/05 → 16/08/2026)

Source : analyse Search Console du 19/08/2026 conservée dans le Drive de
l'entreprise. Ces chiffres ne sont pas estimés.

| Indicateur | Valeur |
|---|---|
| Clics (3 mois) | 52 |
| Impressions | 5 670 |
| CTR moyen | 0,9 % |
| Position moyenne | 14,3 |
| Pages remontées dans le rapport | 217 |

**Ce que ces chiffres font au constat 1.** Le site publie 1 395 URLs ; Search
Console en fait remonter **217**. La grille produit donc massivement des pages
que Google ne montre jamais. La tendance dit la même chose autrement :
impressions par jour **+62 %** sur les 28 derniers jours, mais position moyenne
**−2 places** et CTR **−33 %**. Les nouvelles pages entrent en page 2, 3 ou 4 :
elles ajoutent des impressions sans clic et tirent la moyenne vers le bas. C'est
la signature exacte d'une grille trop large — le constat 1 est confirmé par la
mesure, plus seulement par la structure.

**Le gisement immédiat : 249 impressions en top 6, zéro clic.**

| Requête | Position | Impressions | Clics |
|---|---|---|---|
| renov bois besançon | 6,2 | 58 | 0 |
| entreprise de peinture à besançon | 3,3 | 37 | 0 |
| plaquiste besançon | 6,2 | 31 | 0 |
| entreprise de peinture besncon *(faute de frappe)* | 1,0 | 30 | 0 |
| enduit à la chaux besançon | 5,8 | 30 | 0 |
| peintre besançon | 4,4 | 20 | 0 |
| peintre en batiment besancon | 1,3 | 7 | 0 |

Ce n'est pas un problème de classement : c'est ce que Google affiche du site qui
ne déclenche pas le clic. C'est l'action la moins chère et la plus rapide du
plan — et une partie a été appliquée (section D).

**Les piliers enterrés**, à mettre en regard du Volet 4 :

| Page | Clics | Impressions | Position |
|---|---|---|---|
| / (accueil) | 20 | 1 808 | 11,4 |
| /blog/moisissure-plafond-salle-de-bain-besancon | 4 | 1 257 | 12,9 |
| /platrerie-besancon | 4 | 481 | 21,1 |
| /peinture-interieure-besancon | 1 | 189 | 24,8 |
| /isolation-besancon | 0 | 184 | 28,3 |
| /papier-peint-besancon | 3 | 181 | 14,1 |
| /toile-de-verre-besancon | 1 | 83 | 36,4 |
| /peinture-exterieure-besancon | 0 | 59 | 15,1 |
| **/degat-des-eaux-besancon** | **0** | **18** | **20,0** |

Deux lectures qui changent des priorités de ce rapport :

1. **Le silo dégât des eaux n'est pas le point fort du site — il est
   invisible.** 18 impressions en trois mois. Le Volet 1 le présentait comme le
   silo modèle sur la foi de sa couverture éditoriale ; en visibilité réelle,
   c'est le silo à remonter en premier, parce que c'est celui qui amène les
   assurances et les syndics.
2. **`/papier-peint-besancon` (position 14,1) devance largement
   `/toile-de-verre-besancon` (position 36,4)** : la page qui portait les deux
   cibles écrasait la page dédiée. La correction de la section D vise
   précisément cela — avec une réserve honnête : elle peut coûter des
   impressions « toile de verre » aux pages papier peint avant que les pages
   dédiées ne remontent. À mesurer dans quatre à six semaines.

**Deux anomalies héritées, hors périmètre de cet audit mais à ne pas perdre :**
la requête de marque « rushiti-renovation.fr » ressort en position 22,1 ; et des
pages de l'ancien site WordPress continuent d'imprimer sur des prestations qui
ne sont pas au catalogue (bardage métallique 88 impressions, restauration de
meubles 78, désamiantage 19, montage de meuble 10, piscines 8, démolition 6).
Environ 170 impressions viennent par ailleurs de villes hors zone
d'intervention. → **rushiti-indexation** et arbitrage d'Isuf.

## D. Ce qui a été exécuté

Sur autorisation explicite d'Isuf, deux corrections ont été **appliquées dans le
dépôt de production**, sur la branche `claude/ciblage-mots-cles-corrections`
(commit `ab23ae9`, 78 fichiers, aucune URL supprimée ni redirigée, aucun contenu
de page retiré) :

1. **Dé-duplication papier peint / toile de verre — 75 fichiers.** Title, H1,
   meta description et og:description des pages `papier-peint-<zone>` ne visent
   plus « toile de verre » ; tous les titles tiennent en 60 caractères ; la
   toile de verre reste dans le corps de page et le lien vers la page dédiée est
   conservé sur les 76 zones.
2. **Snippets des pages vues sans être cliquées — 3 fichiers.**
   `peinture-interieure-besancon` prend le title `Peintre & entreprise de
   peinture à Besançon | RUSHITI` (52 caractères, calé sur les requêtes réelles
   du tableau ci-dessus) et une description portant les 20 ans de métier et la
   note 4,7/5 sur 34 avis ; `plaquiste-besancon` et `platrerie-besancon`
   reçoivent les mêmes preuves dans leur description. Aucun argument n'est
   inventé : tous figurent déjà sur ces pages.

**État : commit prêt, non poussé.** L'environnement de cette session bloque le
`git push` vers le dépôt de production. La branche existe localement ; il faut
soit débloquer la permission, soit rejouer les deux scripts
(`fix_papier_peint.py`, `fix_ctr.py`) depuis un poste qui a le droit de pousser.

**Volontairement non traité :** le doublon ravalement entre
`/peinture-exterieure-besancon` (59 impressions, position 15,1) et
`/ravalement-facade-besancon` (aucune impression relevée). Retirer la cible de la
seule des deux pages qui a de la visibilité serait un pari ; la décision demande
le croisement requête × page dans Search Console.

## E. Le Volet 7 corrigé — par quoi commencer maintenant

1. **Fait, en attente de déploiement** : dé-duplication papier peint et snippets
   des trois pages (section D).
2. **Exporter le croisement requête × page** dans Search Console (les deux
   exports séparés ne suffisent pas pour trancher les cas ravalement et
   isolation).
3. **Remonter `/degat-des-eaux-besancon`** : 18 impressions, position 20, c'est
   le silo le plus rentable et le moins visible du site.
4. **Nettoyer l'héritage WordPress** : pages hors métier encore indexées,
   requête de marque en position 22.
5. **Puis seulement** la consolidation de la grille du Volet 4, toujours sous la
   même condition : aucune page qui imprime n'est supprimée.

