# Guide SEO local — pages de service localisées — rushiti-renovation.fr — 08/2026

> Généré par le skill `rushiti-guide-seo-local` le 22/08/2026. Sources :
> `rushiti-defaults.md` v4 (15/08/2026) · registre
> `docs/seo/regjistri-fjale-kyce.csv` (21/08/2026) · inventaire
> `docs/seo/inventaire-grille-paliers-2026-08.csv` · plan d'action consolidé
> `docs/seo/raporte/plan-veprimi-konsoliduar-2026-08.md` (22/08/2026) ·
> architecture du cocon (`rushiti-architecte-seo`).
>
> **Pour qui :** le développeur et le rédacteur du site. Chaque section se
> termine par « Ce qu'on fait concrètement ». Pour le régénérer : skill
> `rushiti-guide-seo-local`, mode 1 — ne pas maintenir ce fichier à la main.

## 0. Comment lire ce guide

- **L'état du site prime sur ce document.** Avant d'agir : relire le sitemap
  live (`https://rushiti-renovation.fr/sitemap.xml`), le registre des
  mots-clés et le dernier plan consolidé. Ce guide donne la doctrine ; eux
  donnent l'état.
- **Rien ne part en production sans validation d'Isuf.** Toute page neuve
  passe la porte PORTA de `rushiti-keyword-map` ; toute donnée chiffrée non
  validée s'écrit `[À COMPLÉTER]`.
- Les horizons d'action : 🔴 immédiat (cette semaine) · 🟠 court terme
  (1-3 mois) · 🔵 stratégique (3-12 mois) — consolidés en section 10.

## 1. Titles et H1

### La formule maison (constatée en production le 21/08/2026)

```
Title pilier   : [Métier ou Service] à Besançon — [périmètre concret], [preuve validée]
Title grille   : [Service] à [Zone] — [angle ou preuve] | RUSHITI   (relever la convention live avant de créer)
Title B2B      : [Cible ou besoin] : [offre] à Besançon | RUSHITI
Title satellite: [Problème formulé côté client] : [promesse de réponse]
```

Exemples réels en production : « Peintre à Besançon — peinture intérieure,
devis sous 48 h » · « Plaquiste à Besançon — cloisons, plafonds, devis sous
48 h » · « Rénovation de salle de bains à Besançon | RUSHITI » ·
« Sinistres : artisan pour experts à Besançon | RUSHITI ».

### Barème d'exemples title → H1

| Page | Title (≤ 60 c., mot-clé en tête) | H1 (unique, complète le title) |
|---|---|---|
| /peinture-interieure-besancon | Peintre à Besançon — peinture intérieure, devis sous 48 h *(prod.)* | Peinture intérieure à Besançon : murs, plafonds et boiseries remis à neuf |
| /peinture-exterieure-besancon | Peinture extérieure et façade à Besançon \| RUSHITI | Ravalement et peinture de façade à Besançon |
| /platrerie-besancon | Plâtrerie et placo à Besançon — cloisons, plafonds \| RUSHITI | Plâtrerie et placo à Besançon : du plâtre ancien au BA13 |
| /degat-des-eaux-besancon | Dégât des eaux à Besançon — remise en état après sinistre | Réparer plafonds et murs après un dégât des eaux à Besançon |
| /isolation-besancon | Isolation à Besançon — combles, murs, phonique \| RUSHITI | Isolation thermique et phonique à Besançon |
| /renovation-salle-de-bain-besancon | Rénovation de salle de bains à Besançon \| RUSHITI *(prod.)* | Rénovation complète de salle de bains à Besançon |
| /papier-peint-besancon | Pose de papier peint à Besançon — intissé, toile de verre | Pose de papier peint à Besançon, dans les règles de l'art |
| /ragreage-sol-besancon | Ragréage de sol à Besançon — un support plan avant pose | Ragréage de sol à Besançon : pourquoi et comment |
| Grille peinture × Battant | Peinture à Battant (Besançon) — spécialiste bâti ancien \| RUSHITI | Peintre dans le quartier Battant : murs anciens, plâtre et pierre |
| Grille placo × École-Valentin | Placo et cloisons à École-Valentin \| RUSHITI | Pose de placo à École-Valentin : cloisons, plafonds, doublages |
| Grille DDE × Pontarlier | Dégât des eaux à Pontarlier — intervention et remise en état | Dégât des eaux à Pontarlier : assèchement puis remise en état |
| B2B syndics | Rénovation pour syndics à Besançon — parties communes \| RUSHITI | Syndics de copropriété : un artisan fiable pour vos parties communes |

### Les règles, et leur pourquoi

- **Mot-clé pivot en tête** (le plus pondéré), « RUSHITI » en fin.
- **≤ 60 caractères (~600 px)** sinon Google tronque ou réécrit.
- **Un title = une requête pivot du registre.** Deux pages sur la même
  requête = cannibalisation (porte PORTA avant toute création).
- **« devis sous 48 h »** est la seule promesse de délai validée (elle est
  en production) ; toute autre promesse exige l'accord d'Isuf.
- **H1 unique**, plus humain que le title, porte la trame problème →
  solution ; les requêtes secondaires vivent dans les H2, souvent en
  question (couche AEO). Hiérarchie complète → `rushiti-h1-h6`.
- **Meta description** : 150-155 c. = problème/bénéfice + preuve + CTA +
  07 60 27 98 97. La mention « [N] avis, [note]/5 » uniquement relevée sur
  la fiche Google **le jour même** (au 21/08/2026 : « 34 avis, 4,7/5 »).

> **Ce qu'on fait concrètement** — 🔴 aucun title existant ne se retouche en
> masse (la dé-duplication des 40 pages de grille est déjà en production) ;
> 🟠 les réécritures passent par `rushiti-ctr-opportunites` (preuve CTR) puis
> `seo-title-meta` ; toute page neuve applique les formules ci-dessus.

## 2. Adapter les cadres SEO anglo-saxons au marché français

Le format « Best [service] in [city], [region] » ne se **traduit pas**, il se
**transpose** : « Meilleur peintre à Besançon » est un superlatif
invérifiable — risque juridique (pratique commerciale trompeuse), ton
publicitaire qui érode la confiance d'un client français, signal spam pour
Google.fr.

| Cadre anglo-saxon | Transposition RUSHITI | Pourquoi |
|---|---|---|
| « Best », « Top », « #1 » | Une **preuve** : 20 ans de métier, décennale ERGO, diagnostic gratuit sur site, avis Google relevés et datés | Vérifiable ; la preuve remplace l'adjectif |
| « in [city] » | « à [Ville] » | Grammaire française |
| « [city], [state] » | « [Ville] » en title ; « [Ville] (25) » / « Doubs » en corps de texte | Le département en title gaspille des caractères |
| « near me » | Rien sur la page : c'est la **fiche Google Business** qui sert cette requête | Une page « près de chez moi » est un anti-pattern |
| « Call Now! » | « Demandez votre devis gratuit », « Appelez le 07 60 27 98 97 » | CTA français : ferme, vouvoyé, non agressif |
| « Trusted / Verified » | SIRET affiché, décennale, normes DTU citées et expliquées | En France, la confiance passe par les garanties légales |
| « 5-star reviews » | « [N] avis Google, [note]/5 » — valeur datée du jour | Un compteur d'avis est périssable |

L'intention « meilleur » existe faiblement en requête ; on y répond en
donnant au lecteur **les critères pour juger** (assurance, méthode, avis,
chantiers réels) — jamais en s'auto-proclamant.

> **Ce qu'on fait concrètement** — tout conseil SEO venu d'un article
> anglo-saxon ou d'un outil IA externe passe par cette table de
> transposition, puis par le contrôle du skill (mode 3) avant implémentation.

## 3. Intégration naturelle des mots-clés

### La checklist de placement (une fois chacun, puis français naturel)

1. Title (en tête) · 2. H1 · 3. Slug · 4. Meta description ·
5. Premier paragraphe (~100 premiers mots) · 6. **Un** H2 ·
7. 1-2 `alt` d'images réelles · 8. Ancres des liens entrants.

**Aucune densité chiffrée** : compter les occurrences est une pratique
dépassée. Le test maison : lire à voix haute — si Isuf ne signerait pas le
paragraphe devant un client, il est sur-optimisé.

### Variantes et champ lexical

- Les variantes viennent de la colonne « dytesoret » du registre (« peintre
  besançon » → « entreprise de peinture à Besançon », « peintre en
  bâtiment », « artisan peintre »). Hors registre → risque de
  cannibalisation → `rushiti-keyword-map`.
- Le vocabulaire technique prouve le métier, puis s'explique en une
  demi-phrase : sous-couche, primaire d'accrochage, ratissage, BA13, bandes
  à joints, **ragréage** (avec « a » — la faute décrédibilise), ITI,
  assèchement, humidimètre, convention IRSI, DTU 59.1 / 25.41 / 53.12.

### Anti-patterns corrigés

| ❌ | ✅ |
|---|---|
| « Peintre Besançon : votre peintre à Besançon pour tous travaux de peinture à Besançon » | « Depuis 20 ans, nous repeignons appartements et maisons à Besançon — du studio de Battant à la maison familiale de Saône. » |
| Pied de page : 60 communes en liens | Bloc « Nous intervenons aussi » : 5-8 liens vers des pages existantes et conservées |
| « à Besançon » dans chaque H2 | Zone dans le H1 + un H2 localisé ; les autres H2 = questions réelles des clients |
| `alt="peintre besançon devis peinture"` | `alt="Ratissage d'un mur ancien avant peinture, appartement quartier Battant"` |

> **Ce qu'on fait concrètement** — la checklist des 8 placements devient le
> standard de tout brief (`rushiti-brief-seo`) et de toute relecture ; le
> reste du texte s'écrit pour le lecteur, trame problème → diagnostic →
> solution, CTA + coordonnées en fin.

## 4. Socle technique : JSON-LD, fiche Google Business, NAP

### JSON-LD (type maison : `HousePainter`)

Le bloc organisation sitewide, **corrigé** (la version en production omet
`streetAddress`) :

```json
{
  "@context": "https://schema.org",
  "@type": "HousePainter",
  "name": "RUSHITI Rénovation",
  "legalName": "Rushiti",
  "url": "https://rushiti-renovation.fr/",
  "telephone": "+33760279897",
  "email": "contact@rushiti-renovation.fr",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "18 rue du Professeur Haag",
    "addressLocality": "Besançon",
    "postalCode": "25000",
    "addressRegion": "Doubs",
    "addressCountry": "FR"
  },
  "geo": { "@type": "GeoCoordinates",
    "latitude": "[À COMPLÉTER — relever sur la fiche Google Business]",
    "longitude": "[À COMPLÉTER — relever sur la fiche Google Business]" },
  "areaServed": ["Besançon", "Doubs"],
  "openingHoursSpecification": "[REPRENDRE la fiche Google Business à l'identique]",
  "sameAs": [
    "https://www.facebook.com/rushiti.renovation/",
    "https://www.instagram.com/rushiti.renovation/"
  ],
  "priceRange": "Devis gratuit"
}
```

Règles : `name` = nom commercial (**jamais** « SARL RUSHITI Rénovation » —
cette forme n'existe pas juridiquement) ; horaires et coordonnées géo
**relevés, jamais de mémoire** ; **pas d'`aggregateRating`** alimenté par
les avis Google (consignes Google : avis tiers — la note se cite en texte,
datée) ; par page, ajouter `Service`, `BreadcrumbList`, `FAQPage` ou
`Article` via `schema-builder` ; valider au Rich Results Test avant déploiement.

### Fiche Google Business

Pour « peintre besançon » et le cluster « entreprise de peinture », le pack
local s'affiche au-dessus de l'organique et en écrase le CTR (~150
impressions top 3-8, 0 clic — GSC) : la fiche est un actif au même rang que
les pages. Description, services (300 c./service), Google Posts géo-ciblés →
`rushiti-fiche-google-business` ; réponses aux avis → `rushiti-avis-google` ;
demande d'avis en fin de chantier → `rushiti-courriers-clients`.

### NAP — la règle en une phrase

Partout — site, JSON-LD, annuaires, signatures — reproduire **au caractère
près** ce qu'affiche la fiche Google : « 18 rue du Professeur Haag, 25000
Besançon » (« rue » minuscule, avec « du »), « 07 60 27 98 97 » affiché,
`+33760279897` en `tel:`/JSON-LD. L'inventaire multi-annuaires (PagesJaunes,
Facebook, Apple Plans, Bing…) n'a jamais été fait → `rushiti-seo-local`.

> **Ce qu'on fait concrètement** — 🔴 ajouter `streetAddress` au bloc
> JSON-LD du site ; 🟠 inventaire NAP + optimisation de la fiche (vague 2 du
> plan consolidé) ; à chaque nouvelle page : JSON-LD via `schema-builder`,
> validé au Rich Results Test.

## 5. Architecture des pages locales

### Le système en vigueur (ne pas réinventer)

- **6 silos** avec pages piliers `/{service}-besancon` (peinture,
  plâtrerie/placo, sols, isolation, dégât des eaux, rénovation de
  pièce + B2B) ; satellites blog « 1 problème = 1 contenu » ; transverses
  (/contact, /zones-intervention, /prix-travaux-renovation-besancon…).
- **Grille locale `/{service}-{zone}` par paliers** — la réponse à « une
  page par ville ? » est : *oui, mais par paliers* :

| Palier | Zones | Pages/zone | Logique |
|---|---|---|---|
| A — cœur | Besançon + quartiers forts (Battant, Centre-ville, Chaprais, Bregille…) | 18 | Volume réel + différenciation possible |
| B — pôles | Communes pôles (École-Valentin, Avanne-Aveney, Chalezeule, Beure…) | 10 | Services les plus demandés |
| C — villages | Petites communes (Amagney, Arguel, Braillans, Deluz…) | 5 | Présence minimale, le pilier fait le reste |

  La grille a déjà été **consolidée de 644 à 301 pages** (63 zones, 301
  posées dans `_redirects`) : des centaines de pages minces n'imprimaient
  pas et diluaient le crawl. **Ne jamais la regonfler**, ni recréer une URL
  fusionnée.
- **Renforcer avant de créer** : un pilier en page 2-5 vaut plus que dix
  pages de grille neuves. Ordre : piliers → maillage → grille.

### Zones qui se chevauchent : 1 requête canonique = 1 page

| Niveau | Requête | Page |
|---|---|---|
| Quartier (Battant, Planoise…) | « service + quartier » | page de grille du quartier |
| Ville | « service + besançon » | page pilier (la grille ne la vise jamais) |
| Commune limitrophe | « service + commune » | grille palier B/C |
| Département (« Doubs », « 25 ») | pas de page dédiée | corps des piliers + `areaServed` + /zones-intervention |

Hors Doubs (Belfort 90, Vesoul 70, Dole 39…) : **hors zone validée**. Une
page hors zone est une décision business d'Isuf (déplacements, rentabilité),
jamais une décision SEO — procédure : arbitrage → ajout à la zone → registre
→ porte PORTA → production.

### Maillage interne

- Satellite → **pilier en premier lien** (ancre descriptive, jamais
  « cliquez ici ») ; pilier → satellites (« Pour aller plus loin », sinon
  orphelins) ; grille → son pilier + 2-3 services frères de la même zone +
  /contact.
- Bloc « Nous intervenons aussi » : **5-8 liens max**, uniquement vers des
  pages existantes conservées par le palier.
- Jamais de lien vers rushiti.fr (arbitrage en attente) ni
  rushiti-peinture.fr (domaine éteint). Plan détaillé →
  `rushiti-maillage-interne` ; orphelines → `orphan-finder`.

> **Ce qu'on fait concrètement** — 🟠 pousser `/platrerie-besancon`
> (pos. 9,1) et `/ratissage-enduit-besancon` (pos. 10,9) vers la page 1 par
> 2 liens contextuels chacun (vague 2 du plan) ; toute idée de page neuve :
> porte PORTA d'abord, production `rushiti-page-locale` ensuite (gabarit
> existant obligatoire).

## 6. Différenciation du contenu (anti-duplication)

Google replie les pages quasi identiques — le site l'a vécu (d'où la
consolidation). Une page de grille n'existe que si elle peut être
**réellement différente**.

**Le minimum unique par page** : title/meta/H1 uniques · introduction
réécrite pour la zone (jamais un search-replace du nom) · 1 bloc « angle
local » vrai · FAQ locale (2-3 questions dont 1 spécifique) · preuve locale
seulement si elle existe (chantier réel, photo avec accord RGPD via
`rushiti-memo-chantier`) — **jamais de témoignage inventé** · maillage
propre à la zone. Le tronc commun métier (méthode, normes) peut être partagé.

**Matrice d'angles locaux** (hypothèses à confirmer par le vécu de chantier
d'Isuf/Yll — on ne publie que du vrai) : Battant/Centre/Bregille = bâti
ancien, pierre, plâtre traditionnel, accès rue étroite · Planoise/Palente =
grands ensembles, remises en état locatives, bailleurs · Chaprais/
Saint-Ferjeux = immeubles 1900-1960, plâtres fissurés · École-Valentin/
Pirey/Franois = pavillons 1970-1990, combles, façades · plateau
(Saône, Mamirolle, Nancray) = murs froids, condensation, isolation ·
Pontarlier/Haut-Doubs = altitude, hivers rudes · Montbéliard = parc ancien
et locatif.

**Le test final** : masquer le nom de la zone et relire — si la page
pourrait décrire n'importe quelle commune, elle n'est pas prête. S'il n'y a
rien de vrai à dire sur un village C au-delà de « on s'y déplace », les 5
pages du palier C suffisent : on renforce le pilier au lieu d'écrire du
remplissage.

> **Ce qu'on fait concrètement** — le test « masquer la zone » entre dans la
> checklist de mise en ligne (Annexe A) ; doublons suspectés →
> `rushiti-cannibal-check` (verdict) et `rushiti-indexation` (pages
> « dupliquée, non sélectionnée » en GSC).

## 7. Comportement de recherche des Français

| Forme | Usage | Exemple |
|---|---|---|
| **à** + ville | La préposition reine (titles, textes) | « peintre à Besançon » |
| **dans le** + département | Le Doubs est masculin | « artisan dans le Doubs » |
| **dans le 25** | Familier — corps de texte/FAQ seulement | — |
| **en** + région | Signal large, peu de valeur locale | « en Franche-Comté » |
| **près de / autour de** | Proximité | « peintre près de Besançon » |
| **proche de moi** | Servie par la fiche Google, jamais par une page | — |

Faits utiles, constatés dans les exports GSC du site : les requêtes se
tapent majoritairement **sans préposition et souvent sans accents**
(« peintre besancon », « degat des eaux besancon ») — Google normalise, donc
on **rédige toujours en français correct** et on ne crée jamais de variante
de page « sans accent ». « 25 » / « 25000 » se servent dans le corps de
texte et le JSON-LD, pas en bourrant les titles. Les requêtes quartier
relèvent de la grille, jamais du pilier.

**Saisonnalité** : jamais affirmée de mémoire — elle se **relève** (Google
Trends France + Franche-Comté) via `rushiti-google-trends`, qui cale chaque
publication 6-8 semaines avant le pic (le plan éditorial automne est déjà
calé ainsi : dégât des eaux et isolation se renforcent en octobre).

**Recherche vocale / moteurs IA** : question en H2, réponse directe
autoporteuse en première phrase (40-60 mots), entités associées (RUSHITI
Rénovation + service + zone + problème). Audit → `rushiti-visibilite-ia`.

> **Ce qu'on fait concrètement** — les formules de la section 1 encodent
> déjà ces usages ; chaque brief de contenu précise la forme géographique
> attendue (« à Besançon » / « dans le Doubs ») et les questions H2 réelles.

## 8. Mobile et performance

Le site est **statique sur Cloudflare Pages** : TTFB et cache sont bons par
construction. Les Core Web Vitals n'ont **jamais été mesurés** (audit du
13/08) — mesurer vient avant optimiser.

| Métrique | Seuil « bon » | Où |
|---|---|---|
| LCP | moins de 2,5 s | PageSpeed Insights, mobile d'abord |
| INP | moins de 200 ms | idem |
| CLS | moins de 0,1 | idem |

Leviers, par rendement sur ce site : **images** (WebP/AVIF, `width`/`height`
explicites — c'est ce qui tient le CLS, `loading="lazy"` sous la ligne de
flottaison, héro préchargée si LCP) → `rushiti-images-seo` · **polices**
(Montserrat + Open Sans via Google Fonts : `font-display: swap` +
`preconnect`, ou auto-hébergement) · **CSS/JS** (critique inline, le reste
différé) · **conversion mobile** (`tel:+33760279897` cliquable partout,
cibles tactiles ≥ 48 px, CTA collant appel + devis sur les pages
commerciales, formulaire « demande rapide » court).

Pas de statistiques de marché inventées (« X % des recherches locales… ») :
l'index Google est mobile-first pour tout le monde — c'est la seule
justification nécessaire.

> **Ce qu'on fait concrètement** — 🟠 mesurer l'échantillon (accueil, pilier
> DDE, une page de grille, /contact) via `rushiti-audit-technique`
> (vague 2 du plan) ; corriger ensuite dans l'ordre du rendement ci-dessus.

## 9. Mesure : KPIs et suivi des conversions

### L'état réel au 22/08/2026 (à ne pas maquiller)

**GA4 est absent** — seul le Pixel Meta mesure ; l'événement `Lead` sur
`/merci` et l'attribution par page (champ `page` des formulaires) arrivent
avec les **PR #10/#20** ; une bannière de consentement existe déjà.
Conséquence : la première action de mesure n'est pas un dashboard, c'est
**pouvoir compter**.

### Événements de conversion (cible une fois GA4 posé — `rushiti-ga4-gtm`)

| Événement | Déclencheur | Note |
|---|---|---|
| `generate_lead` | arrivée sur `/merci` | l'attribution par page dit quelle page produit le lead |
| `phone_click` | clic `tel:` | la conversion n° 1 d'un artisan |
| `email_click` | clic `mailto:` | secondaire |
| `whatsapp_click` | clic WhatsApp | seulement si le canal existe sur le site — à vérifier |

Pas de « valeur de lead » inventée dans les événements : la valeur d'un
chantier, seul Isuf la connaît (`[À COMPLÉTER]` ou rien). Consent Mode v2
derrière la bannière : le consentement préalable est une exigence CNIL, pas
une option.

### Le tableau de bord mensuel

| KPI | Source | Agent |
|---|---|---|
| Impressions/clics/position des clusters pivots (« peintre besançon », « entreprise de peinture à besançon » — 1 343 impr., pos. 3,5, 0 clic : le plus gros gisement —, « plaquiste », pilier DDE) | GSC requête × page | `rushiti-gsc` → rapport KPI (`rushiti-keyword-map`) |
| Régressions de positions vs baseline datée | exports successifs | `rushiti-regression-seo` |
| Quick wins CTR (pos. 3-15, CTR sous la courbe) | GSC | `rushiti-ctr-opportunites` |
| Appels, itinéraires, vues fiche · avis (nombre + note, datés) | Google Business | relevé mensuel manuel |
| Leads par page | GA4 (`generate_lead` + champ `page`) | `rushiti-ga4-gtm` |
| Pages indexées/exclues | GSC Couverture | `rushiti-indexation` |
| CWV mobile (échantillon) | PageSpeed | `rushiti-audit-technique` |

**Règles de lecture** : fenêtre de **4-6 semaines** avant de juger un
changement (cadence déjà inscrite au registre) ; comparer des périodes
comparables (saisonnalité) ou le signaler ; **jamais de classement promis** —
un KPI est un constat daté, un objectif est une direction.

> **Ce qu'on fait concrètement** — 🔴 merger PR #10 puis #20 (l'événement
> `Lead` existe enfin) ; 🟠 GA4 + GTM + Consent Mode v2 ; ensuite le rapport
> KPI mensuel intègre les leads par page.

## 10. Plan d'action

Aligné sur le **plan consolidé du 22/08/2026**
(`docs/seo/raporte/plan-veprimi-konsoliduar-2026-08.md`) — qui reste la
référence d'exécution ; ce guide n'y ajoute que les actions doctrine.

### 🔴 Immédiat (cette semaine)

| # | Action | Geste | Qui |
|---|---|---|---|
| 1 | **Merger PR #10 puis PR #20** — formulaires + consentement + événement `Lead` `/merci` + attribution par page + mentions RGPD (aujourd'hui aucun envoi de formulaire n'est compté) | 2 merges, 1 déploiement | Isuf (2 clics) |
| 2 | **Valider le paquet moisissure A-B-C-D** (2ᵉ visibilité du site, ≈ 620 impr.) | lecture + validation | Isuf |
| 3 | **Anomalie marque** « rushiti-renovation.fr » en position 23 (49 impr., 0 clic) — canonical/www | contrôle + correction si constat | `rushiti-indexation` |
| 4 | **`streetAddress` dans le JSON-LD** sitewide (« 18 rue du Professeur Haag ») + géo/horaires relevés sur la fiche | 1 correction, embarquée au prochain train de déploiement | dev + `schema-builder` |

### 🟠 Court terme (1-3 mois)

| # | Action | Qui |
|---|---|---|
| 5 | Maillage entrant vers `/platrerie-besancon` (pos. 9,1) et `/ratissage-enduit-besancon` (pos. 10,9) — 2 liens contextuels chacun | `rushiti-maillage-interne` |
| 6 | Fiche Google Business (description, services, posts géo-ciblés) + **premier inventaire NAP** multi-annuaires | `rushiti-fiche-google-business` + `rushiti-seo-local` |
| 7 | GA4 + GTM + Consent Mode v2 derrière la bannière existante | `rushiti-ga4-gtm` |
| 8 | Mesurer les CWV (accueil, pilier DDE, une page de grille, /contact) puis corriger par rendement | `rushiti-audit-technique` |
| 9 | ⚖️ Décision domaine principal (rushiti.fr → 301 vers rushiti-renovation.fr ?) — 10 minutes d'arbitrage | Isuf, puis `rushiti-audit-seo` |
| 10 | Cadence d'avis : email de fin de chantier avec demande d'avis, systématique | `rushiti-courriers-clients` |

### 🔵 Stratégique (3-12 mois)

| # | Action | Fenêtre / condition | Qui |
|---|---|---|---|
| 11 | Enrichir le pilier `/degat-des-eaux-besancon` (silo le plus rentable, 33 impr./12 m) : assèchement, déroulé IRSI, maillage des 3 satellites | octobre (6-8 sem. avant la haute saison) | `rushiti-brief-seo` → `rushiti-architecte-seo` |
| 12 | Satellite « Mur froid et condensation » → pousse `/isolation-interieure-besancon` (0 impression/12 m) + enrichir `/isolation-besancon` | octobre-novembre | idem |
| 13 | Article « Prix du placo au m² » (fourchettes à valider par Isuf, protocole PRIX) | rédaction nov., publication déc. | `rushiti-architecte-seo` |
| 14 | Page crépi dédiée (191 impr. non servies) **si** le re-export GSC du ~1ᵉʳ octobre ne montre pas de remontée | conditionnelle | `rushiti-brief-seo` |
| 15 | Renforcement sélectif de la grille : zones palier A/B dont les pages impriment sans cliquer — différenciation réelle (section 6), jamais de volume pour le volume | au fil des rapports KPI | `rushiti-page-locale` après porte |
| 16 | Extension de zone (Haut-Doubs élargi, hors-Doubs type Belfort) : **arbitrage business d'Isuf d'abord**, puis registre → porte → production | quand Isuf le décide | Isuf, puis la chaîne habituelle |
| 17 | Couche IA/AEO : blocs « L'essentiel », réponses autoporteuses, audit E-E-A-T | continu | `rushiti-visibilite-ia` |

## Annexe A — Checklist de mise en ligne d'une page service × zone

```
□ Porte PORTA passée (registre à jour, requête pivot attribuée, score cannibalisation ok)
□ Palier respecté (A 18 / B 10 / C 5) — la zone a droit à cette page
□ Title : formule maison, ≤ 60 c., mot-clé en tête, unique sur le site
□ H1 unique, complète le title, zone canonique
□ Slug conforme à la convention relevée au sitemap
□ Meta description 150-155 c. : problème + preuve + CTA + 07 60 27 98 97
□ Checklist des 8 placements de mot-clé (section 3) — une fois chacun
□ Prépositions correctes (« à [ville] », « dans le Doubs ») ; français accentué
□ Trame problème → diagnostic → solution ; pédagogie du pourquoi
□ Bloc angle local VRAI (validé terrain) ; test « masquer la zone » réussi
□ FAQ locale 2-3 questions (dont 1 spécifique) — format réponse directe (AEO)
□ Aucune donnée inventée : prix, délai, horaires, avis, témoignage → [À COMPLÉTER]
□ NAP au caractère près ; logo présent ; tel: cliquable
□ JSON-LD HousePainter + Service/Breadcrumb (schema-builder), validé Rich Results
□ Maillage : lien pilier + 2-3 frères de zone + /contact ; ancres descriptives
□ Bloc « Nous intervenons aussi » ≤ 8 liens, pages existantes conservées
□ Images : WebP/AVIF, width/height, lazy, alt descriptif réel
□ CTA final + coordonnées ; page dans le sitemap ; validation d'Isuf obtenue
□ Mesure programmée à 4-6 semaines (rushiti-regression-seo)
```

## Annexe B — Routage vers la suite RUSHITI

Porte et registre `rushiti-keyword-map` · production de pages
`rushiti-page-locale` · titles/meta `seo-title-meta` +
`rushiti-ctr-opportunites` · Hn `rushiti-h1-h6` · JSON-LD `schema-builder` ·
fiche Google `rushiti-fiche-google-business` · avis `rushiti-avis-google` ·
NAP/annuaires `rushiti-seo-local` · maillage `rushiti-maillage-interne` ·
GA4/GTM `rushiti-ga4-gtm` · GSC `rushiti-gsc` · régressions
`rushiti-regression-seo` · indexation `rushiti-indexation` · technique/CWV
`rushiti-audit-technique` · saisonnalité `rushiti-google-trends` · briefs et
contenus `rushiti-brief-seo` + `rushiti-architecte-seo` · cannibalisation
`rushiti-cannibal-check` · visibilité IA `rushiti-visibilite-ia`.

## Annexe C — Corrections apportées au brouillon externe (08/2026)

Un guide produit par un outil IA externe circulait avant celui-ci. Ce qu'il
fallait corriger — **ne pas implémenter l'ancien document** :

| Brouillon externe | Correction (ce guide) |
|---|---|
| « SARL RUSHITI Rénovation » | Nom commercial : RUSHITI Rénovation ; raison sociale : Rushiti (SARL) |
| « 18 Rue du Professeur Haag » | « 18 rue du Professeur Haag » — graphie NAP de la fiche Google |
| Horaires inventés (7 h-20 h 30, ouvert le dimanche) | Horaires : uniquement ceux de la fiche Google, relevés |
| « Assurances ERGO France et Phénix Assurances » | Décennale : assureur ERGO (n° `[À COMPLÉTER]`) — pas d'assureur fantôme |
| Pages Belfort (90), Vesoul (70), Dole (39), Lons-le-Saunier (39) | Hors zone validée — arbitrage business d'Isuf avant toute page |
| `aggregateRating` 4,7/34 en JSON-LD | Interdit (avis Google = tiers) ; la note se cite en texte, datée |
| « Meilleur… » / traduction du cadre « Best X in Y » | Formule maison : mot-clé + preuve validée (section 2) |
| Densités de mots-clés chiffrées | Checklist de placement, zéro densité (section 3) |
| Statistiques de marché et saisonnalité sans source (« 68 % mobile », « 85 % 5G ») | Aucune statistique inventée ; saisonnalité relevée via Google Trends |
| Valeur de lead « 150 € » dans GA4 | `[À COMPLÉTER]` par Isuf ou rien |
| Architecture `/ville/service/` à créer | La grille `/{service}-{zone}` par paliers existe déjà, consolidée 644 → 301 |
| Témoignages types « Mme Dupont » | Jamais de témoignage inventé — preuve réelle RGPD ou rien |
