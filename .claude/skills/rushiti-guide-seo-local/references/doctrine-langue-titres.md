# Doctrine 1 — Langue, titres, H1 et intégration des mots-clés

Cette doctrine couvre : comment les Français cherchent un artisan, comment
adapter les cadres SEO anglo-saxons (« Best [service] in [city] ») au marché
français, les formules de title et de H1 maison, et l'intégration naturelle
des mots-clés. Elle s'applique à toute page service, page service × zone,
page B2B ou satellite de rushiti-renovation.fr.

## A. Comment les Français cherchent un artisan

### Les intentions, dans l'ordre de valeur business

1. **Urgence / pathologie** — « dégât des eaux besançon », « auréole plafond
   que faire », « moisissure plafond salle de bain ». Le client vit un
   problème : la trame problème → diagnostic → solution est naturelle ici.
2. **Commerciale locale** — « peintre besançon », « entreprise de peinture à
   besançon », « plaquiste besançon », « artisan rénovation salle de bain ».
   Le cœur des pages piliers et de la grille locale.
3. **Prix / transaction** — « prix peinture m² », « devis peinture besançon »,
   « peintre pas cher ». Se sert avec une page prix pédagogique et un devis
   gratuit — jamais en se déclarant « pas cher ».
4. **Comparaison / choix** — « parquet ou pvc », « iti ou ite », « mat velours
   ou satin ». Territoire des satellites blog.
5. **Marque** — « rushiti », « rushiti besançon », « rushiti renovation
   avis ». Doit imprimer en position 1 (toute anomalie → `rushiti-indexation`).

### La grammaire géographique française (à / en / dans)

| Forme | Usage correct | Exemple |
|---|---|---|
| **à** + ville | La préposition reine des requêtes et des textes | « peintre à Besançon », « plaquiste à Pontarlier » |
| **dans le** + département masculin | Le Doubs est masculin | « artisan dans le Doubs », « dans le Haut-Doubs » |
| **dans le 25** | Familier, réel en requête, éviter en title | corps de texte ou FAQ uniquement |
| **en** + région | « en Franche-Comté », « en Bourgogne-Franche-Comté » | signal large, peu de valeur locale |
| **près de / autour de** | Proximité | « peintre près de Besançon » |
| **proche de moi / à proximité** | Requête mobile → c'est la fiche Google qui la sert, pas une page | ne jamais créer de page « près de chez moi » |

**Fait déterminant :** dans la barre de recherche, les Français tapent
majoritairement **sans préposition et souvent sans accents** (« peintre
besancon », « degat des eaux besancon » — visible dans les exports GSC du
site). Google normalise. La conséquence pratique :

- On **rédige toujours en français correct** (« à Besançon », accents
  compris). Écrire fautif « pour coller à la requête » n'apporte rien et
  décrédibilise devant un client ou un expert d'assurance.
- On ne crée **jamais** deux variantes de page pour « avec/sans préposition »
  ou « avec/sans accent » : même requête canonique, même page (registre
  `rushiti-keyword-map`).

### Département, code postal, quartier

- « 25 » et « 25000 » apparaissent en requêtes réelles : les servir dans le
  **corps de texte** et le **JSON-LD** (`postalCode`, `areaServed`), pas en
  bourrant les titles.
- Les requêtes quartier (« peintre battant », « placo planoise ») sont
  servies par la grille locale par paliers (doctrine 2), jamais par la page
  pilier.
- La graphie canonique des zones est celle de `rushiti-defaults.md`
  (quartiers de Besançon, communes du Doubs).

### Saisonnalité

Ne jamais affirmer une saisonnalité de mémoire ni en recopier une d'un outil
externe : c'est une donnée mesurable, donc elle se **relève** (Google Trends
France + Franche-Comté, en direct) via `rushiti-google-trends`, qui cale la
publication 6 à 8 semaines avant le pic. Un tableau de saisonnalité sans
relevé daté est une invention.

### Recherche vocale et moteurs IA

Les requêtes en langage naturel (« qui appeler pour une fuite au plafond »)
se servent par la couche AEO du cocon : question en H2, réponse directe et
autoporteuse dans la première phrase (40-60 mots), entités toujours associées
(RUSHITI Rénovation + service + zone + problème). Détail dans
`architecture-cocon.md` de `rushiti-architecte-seo` ; audit via
`rushiti-visibilite-ia`.

## B. Adapter le cadre anglo-saxon « Best [service] in [city], [region] »

Le format américain « Best Painter in Denver, CO » ne se **traduit pas**, il
se **transpose**. Traduit littéralement (« Meilleur peintre à Besançon »), il
cumule trois défauts : superlatif invérifiable (risque juridique — pratique
commerciale trompeuse — et contraire au principe d'honnêteté RUSHITI), ton
publicitaire qui érode la confiance d'un client français, et signal spam pour
Google.fr. La transposition correcte :

| Élément du cadre EN | Transposition française RUSHITI | Pourquoi |
|---|---|---|
| « Best », « Top », « #1 » | **Une preuve** : 20 ans de métier, garantie décennale (ERGO), diagnostic gratuit sur site, note et nombre d'avis Google **relevés et datés** | La preuve remplace l'autocélébration ; c'est vérifiable |
| « in [city] » | « à [Ville] » | Grammaire française |
| « [city], [state] » | « [Ville] » seule en title ; « [Ville] (25) » ou « Doubs » dans le corps | Le département en title gaspille des caractères sauf ambiguïté |
| « near me » | Rien sur la page — c'est la **fiche Google Business** et le pack local qui servent cette requête | Une page « près de chez moi » est un anti-pattern |
| « Call Now! » | « Demandez votre devis gratuit », « Appelez le 07 60 27 98 97 » | CTA français : ferme mais non agressif, vouvoiement |
| « Trusted / Verified » | SIRET affiché, assurance décennale, normes DTU citées et expliquées | En France la confiance passe par les garanties légales |
| « 5-star reviews » | « [N] avis Google, [note]/5 » — valeur relevée sur la fiche le jour J | Un chiffre d'avis est périssable : toujours daté, jamais de mémoire |

**L'intention derrière « best » existe** en France (« meilleur peintre
besançon » se tape, faiblement). On y répond en **donnant au lecteur les
critères pour juger** (assurance, avis, méthode, chantiers réels) — jamais en
s'auto-proclamant. C'est aussi ce qui distingue une page RUSHITI d'une page
générée par un concurrent pressé.

## C. Formules de title et de H1 (style maison)

### Le style maison constaté en production

Les titles en production (relevés dans le code HTML live, 21/08/2026)
suivent deux patrons validés par Isuf :

- `Peintre à Besançon — peinture intérieure, devis sous 48 h`
- `Plaquiste à Besançon — cloisons, plafonds, devis sous 48 h`
- `Rénovation de salle de bains à Besançon | RUSHITI`
- `Sinistres : artisan pour experts à Besançon | RUSHITI`

D'où les **formules canoniques** :

| Type de page | Formule | Contraintes |
|---|---|---|
| Pilier service | `[Métier ou Service] à Besançon — [périmètre concret], [preuve validée]` | ≤ 60 caractères utiles ; mot-clé en tête |
| Grille service × zone | `[Service] à [Zone] — [angle ou preuve] \| RUSHITI` ou la convention relevée sur les pages de grille existantes | **Relever la convention live avant de créer** (règle absolue : pas de pattern inventé) |
| B2B | `[Cible ou besoin] : [offre] à Besançon \| RUSHITI` | ex. réel « Sinistres : artisan pour experts… » |
| Satellite blog | `[Problème formulé côté client] : [promesse de réponse]` | ex. « Auréole au plafond après une fuite : que faire ? » |

Règles transverses, avec leur pourquoi :

- **Mot-clé pivot en tête** — c'est ce que l'œil et l'algorithme pondèrent
  le plus ; « RUSHITI » se met en fin, jamais en tête.
- **≤ 60 caractères (~600 px)** — au-delà, Google tronque ou réécrit.
- **Un title = une requête pivot** — la requête est celle du registre
  (`docs/seo/regjistri-fjale-kyce.csv`). Deux pages sur la même requête =
  cannibalisation → porte PORTA avant toute création.
- **« devis sous 48 h »** est une promesse **déjà validée en production** ;
  toute autre promesse de délai est interdite sans validation d'Isuf.
- **Jamais deux fois la même ville** dans un title (« Peintre Besançon —
  peinture Besançon » est du bourrage).
- La réécriture fine title/meta est le métier de `seo-title-meta` ; les
  quick wins CTR viennent de `rushiti-ctr-opportunites`.

### H1 — la règle

Un seul H1 par page. Le H1 **complète** le title, il ne le clone pas : plus
humain, il peut être un peu plus long et porter la trame problème →
solution. Les requêtes secondaires (« dytesoret » du registre) vivent dans
les H2, souvent en forme de question (couche AEO). La hiérarchie complète
Hn est le métier de `rushiti-h1-h6`.

### Barème d'exemples (title → H1)

| Page | Title | H1 |
|---|---|---|
| /peinture-interieure-besancon | Peintre à Besançon — peinture intérieure, devis sous 48 h *(en prod.)* | Peinture intérieure à Besançon : murs, plafonds et boiseries remis à neuf |
| /peinture-exterieure-besancon | Peinture extérieure et façade à Besançon \| RUSHITI | Ravalement et peinture de façade à Besançon |
| /platrerie-besancon | Plâtrerie et placo à Besançon — cloisons, plafonds \| RUSHITI | Plâtrerie et placo à Besançon : du plâtre ancien au BA13 |
| /degat-des-eaux-besancon | Dégât des eaux à Besançon — remise en état après sinistre | Réparer plafonds et murs après un dégât des eaux à Besançon |
| /isolation-besancon | Isolation à Besançon — combles, murs, phonique \| RUSHITI | Isolation thermique et phonique à Besançon |
| /renovation-salle-de-bain-besancon | Rénovation de salle de bains à Besançon \| RUSHITI *(en prod.)* | Rénovation complète de salle de bains à Besançon |
| /papier-peint-besancon | Pose de papier peint à Besançon — intissé, toile de verre | Pose de papier peint à Besançon, dans les règles de l'art |
| /ragreage-sol-besancon | Ragréage de sol à Besançon — un support plan avant pose | Ragréage de sol à Besançon : pourquoi et comment |
| Grille : peinture × Battant | Peinture à Battant (Besançon) — spécialiste bâti ancien \| RUSHITI | Peintre dans le quartier Battant : murs anciens, plâtre et pierre |
| Grille : placo × École-Valentin | Placo et cloisons à École-Valentin \| RUSHITI | Pose de placo à École-Valentin : cloisons, plafonds, doublages |
| Grille : DDE × Pontarlier | Dégât des eaux à Pontarlier — intervention et remise en état | Dégât des eaux à Pontarlier : assèchement puis remise en état |
| B2B syndic | Rénovation pour syndics à Besançon — parties communes \| RUSHITI | Syndics de copropriété : un artisan fiable pour vos parties communes |

> Les exemples de grille sont des **propositions par défaut** : avant toute
> création, relever la convention réelle des pages de grille au sitemap et
> l'appliquer (elle prime).

### Meta description

150-155 caractères : problème ou bénéfice + une preuve + CTA + téléphone.
Ex. : « Auréole, plafond taché ? Diagnostic gratuit sur site, remise en état
complète après dégât des eaux à Besançon. 20 ans de métier. 07 60 27 98 97. »
La mention « [N] avis, [note]/5 » n'entre dans une meta que **relevée sur la
fiche Google le jour même** (donnée périssable — celle du 21/08/2026 était
« 34 avis, 4,7/5 »).

## D. Intégration naturelle des mots-clés (anti-bourrage)

### La checklist de placement (le squelette suffit)

Une page bien optimisée place la requête pivot à ces endroits, **une fois
chacun**, puis s'écrit en français naturel :

1. Title (en tête) · 2. H1 · 3. Slug (`peinture-interieure-besancon`) ·
4. Meta description · 5. Premier paragraphe (dans les ~100 premiers mots) ·
6. Un H2 (pas tous !) · 7. 1-2 attributs `alt` d'images réelles ·
8. L'ancre des liens entrants (maillage → `rushiti-maillage-interne`).

Il n'existe **aucune densité cible** : compter les occurrences est une
pratique de 2010. Le test maison : lire le paragraphe à voix haute — si Isuf
ne le signerait pas tel quel devant un client, il est sur-optimisé.

### Varier avec le registre, pas au hasard

Les variantes viennent de la colonne « dytesoret » du registre (ex. pivot
« peintre besançon » → « entreprise de peinture à Besançon », « peintre en
bâtiment », « artisan peintre »). On les emploie là où elles sont naturelles.
Inventer des variantes hors registre risque la cannibalisation avec une
autre page : en cas de doute → `rushiti-keyword-map`.

### Champ lexical par silo (ce qui prouve le métier)

Employer le vocabulaire technique juste — puis l'expliquer en une
demi-phrase (pédagogie RUSHITI) :

- **Peinture** : sous-couche, primaire d'accrochage, ratissage, enduit de
  lissage, finition mat/velours/satin, glycéro/acrylique, DTU 59.1.
- **Plâtrerie/placo** : BA13, rails et montants, bandes à joints, doublage,
  faux plafond, reprise de plâtre ancien, DTU 25.41.
- **Sols** : parquet flottant, stratifié, PVC/LVT, **ragréage** (avec « a » —
  la graphie fautive décrédibilise), vitrification, DTU 53.2.
- **Isolation** : ITI, doublage isolant, combles perdus, pont thermique,
  condensation, mur froid.
- **Dégât des eaux** : assèchement, humidimètre, traitement antifongique,
  auréole, convention IRSI, réserves de découverte.

### Anti-patterns, avec correction

| ❌ Bourrage | ✅ Version RUSHITI |
|---|---|
| « Peintre Besançon : votre peintre à Besançon pour tous travaux de peinture à Besançon » | « Depuis 20 ans, nous repeignons appartements et maisons à Besançon — du studio de Battant à la maison familiale de Saône. » |
| Pied de page listant 60 communes en liens | Bloc « Nous intervenons aussi » de 5-8 liens vers des pages **existantes et conservées** (doctrine 2) |
| « à Besançon » répété dans chaque H2 | La zone dans le H1 + un H2 localisé ; les autres H2 portent les questions réelles des clients |
| `alt="peintre besançon peinture besançon devis"` | `alt="Ratissage d'un mur ancien avant peinture, appartement quartier Battant"` |
| Un paragraphe « SEO » caché en bas de page | Rien — tout le texte est écrit pour le lecteur |

### La trame reste reine

Même sur une page très optimisée, la structure du contenu reste la trame
RUSHITI : **problème vécu → expertise diagnostic → approche complète**
(préparation + traitement + finition), close par le CTA + coordonnées. Une
page qui ranke mais ne convertit pas n'a aucune valeur.
