# Architecture du cocon sémantique — rushiti-renovation.fr

Le cocon RUSHITI **existe déjà** : 6 silos, des pages piliers en ligne, une
grille locale service × zone, un pôle B2B, un blog « Conseils ». Ce fichier
décrit la doctrine d'architecture que l'architecte applique et complète. Il ne
remplace jamais la réalité du site : **au début de chaque mission, relire le
sitemap en ligne** (`https://rushiti-renovation.fr/sitemap.xml`) — la carte
ci-dessous date de la dernière mise à jour du fichier et peut avoir vieilli.

## Les 6 silos et leurs pages piliers

Une **page pilier** est la page commerciale qui ancre un silo : elle vise la
requête la plus large du service (« peinture intérieure Besançon ») et reçoit
le maillage de tous ses satellites. Pages piliers connues (pattern
`/{service}-besancon`, à re-vérifier au sitemap) :

| Silo | Pages piliers / commerciales connues |
|---|---|
| 1. Peinture | `peinture-interieure`, `peinture-exterieure`, `papier-peint`, `toile-de-verre`, `ratissage-enduit` |
| 2. Plâtrerie & placo | `platrerie`, `cloisons`, `doublage-murs`, `faux-plafonds` |
| 3. Sols | `revetements-sol`, `parquet-flottant`, `sol-pvc`, `lino-vinyle-lvt`, `vitrification-parquet`, `ragreage-sol` |
| 4. Isolation | `isolation`, `isolation-interieure` |
| 5. Dégât des eaux | `degat-des-eaux` |
| 6. Rénovation de pièce & pros | `syndic-copropriete-besancon` (B2B) + pages pièce `[vérifier au sitemap]` |

Pages transverses : accueil, `/a-propos`, `/realisations`, blog « Conseils »,
`/simulateur-peinture`, `/contact`, `/zones-intervention`, hub des pages
locales (grille service × zone en 3 paliers : A cœur / B pôles / C villages —
gouvernée par `rushiti-keyword-map`, créée par `rushiti-page-locale`).

## Les satellites — 5 familles

Un **satellite** est un contenu (le plus souvent un article du blog
« Conseils ») qui traite **un** problème ou **une** question à fond — la règle
d'or « 1 problème = 1 contenu » — et pousse sa page pilier par le maillage.
Cinq familles, chacune avec son intention :

1. **Budget & décision** — « prix », « combien coûte », « devis » : intention
   commerciale chaude. Toujours sous protocole PRIX
   (`protocoles-speciaux.md`).
2. **Choix & comparatifs** — « mat, velours ou satin », « parquet ou PVC »,
   « toile de verre ou ratissage » : le lecteur hésite, on l'aide à trancher
   avec des critères techniques honnêtes (et un tableau comparatif).
3. **Pathologies & problèmes vécus** — « auréole au plafond », « mur qui
   cloque », « moisissure sur mur nord », « fissures dans le plâtre » : la
   famille reine, parce que la trame problème → diagnostic → solution y est
   naturelle et que c'est ainsi que les clients cherchent réellement.
4. **Méthode & pédagogie** — « comment préparer un mur ancien avant
   peinture », « les étapes d'un ragréage », un DTU expliqué en clair : la
   pédagogie RUSHITI, qui prouve les 20 ans de métier mieux qu'un slogan.
5. **Cas & saisons** — chantiers racontés (→ matière via
   `rushiti-memo-chantier` et `rushiti-etudes-de-cas`) et sujets saisonniers
   (façades au printemps, isolation à l'automne, condensation en hiver) —
   calage du calendrier via `rushiti-google-trends`, jamais au jugé.

## Vivier d'idées satellites (points de départ, PAS des pages décidées)

Chaque idée passe par la porte PORTA de `rushiti-keyword-map` puis un brief
avant d'exister. Exemples par silo, formulés côté client :

- **Peinture** : quelle finition pour quelle pièce (mat/velours/satin) ·
  peindre une pièce humide (salle de bains, mur nord) · peinture d'une chambre
  d'enfant (produits A+, faible odeur) · repeindre après un dégât des eaux
  (pourquoi l'auréole revient) · remise en état entre deux locataires ·
  parties communes de copropriété.
- **Plâtrerie & placo** : cloison qui isole du bruit · cloison hydrofuge en
  salle de bains · créer une chambre ou un bureau (télétravail) · faux plafond
  pour passer des réseaux · plâtre ancien fissuré : reprendre ou doubler ?
- **Sols** : parquet flottant ou stratifié · pourquoi ragréer avant de poser ·
  sol PVC ou lino, pour quelle pièce · raviver un parquet (vitrification).
- **Isolation** : mur nord froid et condensation · isoler sans perdre trop de
  surface (doublage) · combles perdus.
- **Dégât des eaux** : les bons réflexes des 48 premières heures · pourquoi
  attendre le séchage complet avant de repeindre · comment se passe le
  chantier avec l'assurance (IRSI, sans promesse de prise en charge).
- **Rénovation de pièce / B2B** : rafraîchir un appartement avant mise en
  location · cage d'escalier de copropriété : comment se déroule le chantier.

## Doctrine de maillage (le squelette du cocon)

- **Satellite → pilier** : le premier lien du texte pointe vers la page pilier
  du silo, avec une ancre descriptive (« peinture intérieure à Besançon »,
  jamais « cliquez ici ») — le premier lien est celui que Google pondère le
  plus.
- **Satellite → 1-2 contenus frères** réellement évoqués dans le texte, +
  **la page contact / diagnostic gratuit** dans le CTA final.
- **Pilier → satellites** : la page pilier liste ses satellites (section
  « Pour aller plus loin » ou équivalent du gabarit du site) — sans cela, les
  satellites restent orphelins.
- **Jamais de lien croisé** vers rushiti.fr, jamais vers rushiti-peinture.fr
  (domaine éteint).
- Le plan de maillage détaillé (liens entrants avec phrases d'insertion) est
  le métier de `rushiti-maillage-interne` : lui transmettre chaque brouillon.

## Conventions d'URL et de gabarit

Ne jamais inventer un pattern d'URL ni une structure HTML : relever la
convention réelle du site (sitemap + un contenu existant du même type) et la
suivre. Même règle que `rushiti-page-locale` : **pas de gabarit existant, pas
de production HTML** — en l'absence de gabarit, livrer le contenu en markdown
prêt à intégrer et le signaler. Slugs : courts, en français sans stop-words
inutiles, mot-clé en tête, tirets (ex. `auréole-plafond-que-faire` →
`aureole-plafond-degat-des-eaux` selon la convention relevée).

## Ordre de priorité éditorial (valeur business d'abord)

1. **Dégât des eaux** et **rénovation de pièce** — les chantiers qui
   rapportent, et un différenciateur assurance fort.
2. **B2B syndics / gestionnaires** — récurrence de chantiers.
3. **Peinture, plâtrerie, sols, isolation** — le cœur de volume.
4. **Blog satellites** des silos ci-dessus, dans le même ordre.

La grille locale (quartier × commune) est hors périmètre de cet agent :
`rushiti-keyword-map` gouverne, `rushiti-page-locale` produit.

À priorité égale, caler la saisonnalité avec `rushiti-google-trends`
(publier 6 à 8 semaines avant le pic) et croiser avec les opportunités GSC
(`rushiti-opportunites-gsc`) : renforcer une page qui imprime déjà passe
avant créer une page qui part de zéro.

## Couche IA / extractibilité (AEO)

Chaque contenu du cocon doit pouvoir être **cité tel quel** par un moteur de
réponse (aperçus IA Google, ChatGPT, Perplexity) :

- La question posée en H2, la **réponse directe dans la première phrase**
  (40-60 mots autoporteurs), le pourquoi ensuite.
- Un bloc « L'essentiel » en tête des articles longs (3-5 puces factuelles).
- Des listes numérotées pour tout processus étape par étape.
- Les entités toujours associées dans le texte : RUSHITI Rénovation + le
  service + la zone (Besançon, quartier canonique, commune) + le problème —
  c'est ce qui relie la marque au sujet dans les graphes de connaissance.
- E-E-A-T : de l'expérience de terrain vérifiable (ce qu'on voit sur les
  chantiers bisontins), les normes citées et expliquées, jamais de superlatif
  invérifiable. Audit complet → `rushiti-visibilite-ia` ; mesure de citation →
  `rushiti-part-de-voix-ia`.
