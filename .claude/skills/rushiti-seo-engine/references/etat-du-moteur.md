# État du moteur — la ligne de départ

> C'est l'équivalent RUSHITI du `seo-brief.md` que le playbook générique fait
> écrire par un entretien. Ici il n'est pas déclaratif : **chaque ligne vient
> d'un relevé daté du dépôt.** Ce qui n'a pas été mesuré est marqué `NM` et
> ne devient jamais `0`.
>
> **Dernière consolidation : 23/08/2026.** Toute donnée de plus de trois mois
> se signale comme périmée au moment de l'utiliser. Ce fichier ne se
> recopie pas d'un rapport à l'autre : il se re-relève.

## Sources de ce fichier

| Source | Période / date | Ce qu'elle fournit |
|---|---|---|
| Rapport KPI #1 (`docs/seo/raporte/raport-fjale-kyce-2026-08.md`) | rapport du **21/08/2026** · export principal **12 mois au 21/08** | photographie Search Console |
| Plan consolidé (`docs/seo/raporte/plan-veprimi-konsoliduar-2026-08.md`) | 22/08/2026 | 14 entrées priorisées, 6 sources fusionnées |
| Opportunités GSC (`docs/seo/opportunites-gsc-2026-08.md`) | export 10/06 → 18/08/2026, rapport du 20/08 | gisements par cluster |
| Inventaire des piliers | 22/08/2026 | URL piliers par silo, offre confirmée |
| Relevé avis Google (`docs/seo/avis-google-releve-2026-08-22.md`) | 22/08/2026 | note et nombre d'avis |
| Audit technique | 13/08/2026 | P0-A domaines, P1-B GA4, P2-B local |

## Porte 1 — Google : la photographie

Le rapport KPI #1 publie **deux colonnes**, et il avertit lui-même qu'elles
sont **incomparables ligne à ligne** : l'export courant est à 12 mois, la
baseline initialement proposée était à 3 mois. Les reprendre toutes les deux
est la seule lecture honnête — et à partir du rapport #2, la comparaison se
fait période contre période.

| Indicateur | **12 mois au 21/08/2026** *(export courant)* | 3 mois 17/05 → 16/08 *(référence initiale)* |
|---|---|---|
| Clics | **281** | 52 |
| Impressions | **24 868** | 5 670 |
| CTR | 1,13 % | 0,9 % |
| Position (pondérée impressions) | 10,4 | 14,3 |
| Pages avec impressions | **394** | 217 |
| Requêtes enregistrées | 779 | 238 |

Deux mesures qui ne figurent que dans une seule fenêtre :

| Indicateur | Valeur | Source |
|---|---|---|
| Gisement top 6 sans clic | 249 impressions | analyse Drive du 19/08/2026 |
| Requête « rushiti-renovation.fr » (chaîne du domaine) | 52 impr · pos 22,1 (19/08) puis 49 impr · pos 23,3 (export 10/06 → 18/08) · 0 clic | registre + opportunités GSC |

> **Ne pas lire la ligne du domaine comme « la position de marque ».** Sur
> 12 mois, la marque est **saine** : « rushiti besancon » 443 impressions en
> position 2,4 (26 clics), « rushiti » 257 impressions en position 3,6
> (17 clics). L'anomalie **se limite à la chaîne du domaine** tapée telle
> quelle — piste WordPress / variante www, à instruire par
> `rushiti-indexation`. La présenter comme un effondrement de marque
> ferait travailler au mauvais endroit.

**Le fait qui gouverne tout le reste** : l'accueil porte **222 des 281 clics
(79 %)** et 19 770 impressions en position 9,2 (12 mois au 21/08/2026),
pendant que les pages piliers restent en pages 2 à 5. Le site n'a pas d'abord
un problème de visibilité — il a un problème de **répartition** et de
**conversion de la visibilité existante**.

Conséquence directe sur la priorisation : avant d'écrire une page neuve, la
question rentable est « pourquoi ces impressions ne cliquent-elles pas ? ».

### Les gisements mesurés (par ordre de volume)

| Cluster / page | Mesure | Lecture |
|---|---|---|
| « entreprise de peinture à besançon » | 1 343 impressions · position 3,5 · **0 clic** | Le plus gros gisement du site. Bien classé, jamais cliqué — le pack local capte le clic avant l'organique |
| Cluster moisissure (`/blog/moisissure-plafond-salle-de-bain-besancon`) | ≈ 620 impressions · 2 clics | 2ᵉ visibilité du site. Enrichissement déjà live, paquet complémentaire en validation |
| `/platrerie-besancon` | position **9,1** sur 10/06 → 18/08 · 504 impressions / position 21,8 sur 12 mois | À une porte de la page 1 **sur la fenêtre courte**. Aucun pilier voisin ne le pousse |
| `/ratissage-enduit-besancon` | position **10,9** sur 10/06 → 18/08 · 413 impressions / position 18,4 sur 12 mois | Idem |
| `/degat-des-eaux-besancon` | 33 impressions / 12 mois · position 16 | **Le silo le plus rentable du métier, quasi invisible.** Priorité de renforcement n°1 |
| `/isolation-interieure-besancon` | **0 impression** / 12 mois | La page existe et ne reçoit rien : il lui manque un satellite qui pousse |
| `/renovation-appartement-besancon` | **2 impressions** / 12 mois | Trop faible pour recevoir des pages sœurs : à renforcer avant d'élargir |

> **Les deux fenêtres ne disent pas la même chose, et c'est le point.** Une
> page à 9,1 sur trois mois et 21,8 sur douze est une page **qui monte** :
> c'est ce qui en fait un bon candidat au maillage, pas une position acquise.
> Citer la seule valeur courte sans sa fenêtre transformerait une tendance en
> promesse.

## Porte 2 — Moteurs de réponse

| Indicateur | Valeur au 23/08/2026 |
|---|---|
| Part de voix IA (panel fixe de 14 requêtes) | `NM` — aucun relevé consigné dans le dépôt |
| Relevé de corpus cité (`docs/seo/citations-ia/`) | `NM` — seuls le dictionnaire de colonnes et le modèle CSV vide existent |
| robots.txt et crawlers IA | **incident déjà constaté**, état actuel non revérifié — voir ci-dessous |

**C'est le trou le plus net du dispositif au 23/08/2026** : l'outillage est en
place (deux agents, un dictionnaire de colonnes, un modèle CSV, un panel de
14 requêtes figé), et **aucune mesure de citation n'a encore été prise**. Le
premier relevé n'aura pas de comparatif : il est la référence, et c'est normal.

> **Un antécédent à ne pas oublier.** L'agent `rushiti-visibilite-ia` est né
> d'un incident réel sur ce site : **le robots.txt managé de Cloudflare
> bloquait silencieusement tous les crawlers IA de rushiti-renovation.fr.**
> Ce n'est donc pas un terrain jamais examiné, c'est un terrain avec un mode
> de panne connu, silencieux, et qui peut revenir à chaque changement de
> configuration Cloudflare. D'où l'ordre ci-dessous, et le contrôle après
> **chaque** déploiement.

Ordre correct pour ouvrir cette porte :

1. `rushiti-visibilite-ia` — les moteurs **peuvent**-ils lire le site ?
   (Mesurer la citation d'un site que les crawlers ne lisent pas fait perdre
   la mesure et le temps.)
2. `rushiti-part-de-voix-ia` — première mesure, elle devient la référence.
3. `rushiti-citation-ia` — quelles sources sont citées à notre place, et par
   quelle porte y entrer.

## Ce qui est déjà fait — ne jamais le reproposer

Un plan générique reproposera la moitié de cette liste. Elle est close.

| Chantier | Date | Preuve |
|---|---|---|
| Dé-duplication des titles sur 40 pages | août 2026 | plan consolidé 22/08 |
| Consolidation de la grille locale (réduction de plus de moitié, 63 pages épargnées — *compte exact contesté, voir l'écart en fin de fichier*) | août 2026 | idem |
| Maillage des 3 pages éclipsées | PR #19 | idem |
| Création du silo « rénovation de pièce » (salle de bains, cuisine, entreprise-rénovation) | PR #15, mergée le 21/08 | idem |
| Fusion façade (`/ravalement-facade-besancon` → 301) | PR #14 | inventaire des piliers |
| Skill + prompt maître « page de service dédiée » | 22/08/2026 | `docs/seo/arbitrage-pages-service-dediees-2026-08.md` |

## Ce qui bloque la mesure (à traiter avant d'optimiser)

Optimiser ce qu'on ne mesure pas revient à travailler à l'aveugle. Ces trois
points passent avant toute campagne de contenu :

| Blocage | État | Agent |
|---|---|---|
| **Aucun envoi de formulaire n'est compté** — l'événement `Lead` sur `/merci` n'existe pas | PR #10 + PR #20 prêtes, en attente de 2 merges | Isuf (2 clics), puis déploiement Cloudflare |
| **GA4 absent** — seul le Pixel Meta mesure ; aucun entonnoir téléphone / formulaire | à installer, Consent Mode v2 derrière la bannière existante | `rushiti-ga4-gtm` |
| **Core Web Vitals jamais mesurés** (accueil, dégât des eaux, une page locale, mobile) | jamais relevés | `rushiti-audit-technique` |

## Décisions ouvertes qui attendent Isuf

| Décision | Enjeu | Effort |
|---|---|---|
| **Domaine principal** — `rushiti.fr`, `rushiti-peinture.fr` (éteint mais encore publié par des agrégateurs) et le microsite Localo dispersent l'autorité (audit du 13/08, P0-A). Recommandation : tout en 301 vers `rushiti-renovation.fr` | Fort | 10 minutes de décision + le sitemap de `rushiti.fr` |
| **Carrelage** — « Carrelage & Sol » figure sur l'accueil héritée, aucune prestation ni page confirmée | Cohérence de l'offre | Une phrase de réponse |
| **« devis sous 48 h »** — présent dans un title live et dans les preuves du registre, mais classé « promesse à valider » par deux autres agents | Engagement contractuel | Une phrase de réponse |
| **`/sol-pvc-besancon` vs `/lino-vinyle-lvt-besancon`** — doublon signalé | Cannibalisation | → `rushiti-cannibal-check` |

## Données périssables — à revérifier le jour de l'usage

- **Note et nombre d'avis Google** : 34 avis, 4,7/5 au relevé du 22/08/2026.
  Ne jamais recopier d'un ancien document : ce compteur bouge.
- **Nombre d'URL du sitemap** : **contesté entre les sources** — voir
  l'écart ci-dessous. À re-relever avant tout usage chiffré.
- **Positions et impressions** : toute valeur ci-dessus est datée, et sa
  **fenêtre** fait partie de la valeur. Au-delà de trois mois, elle sert
  d'historique, plus de baseline.

## L'écart à lever — la taille du site

**C'est le chiffre le moins fiable de tout le dossier, et il est cité
partout.** Trois sources internes, à un jour d'intervalle, ne disent pas la
même chose :

| Source | Ce qu'elle dit | Date |
|---|---|---|
| Rapport KPI #1 | sitemap actuel ≈ **755 URL** (394 pages avec impressions) | 21/08/2026 |
| Proposition keyword-map | **755 URL** dans `sitemap-pages.xml`, relevé live · `_redirects` contient **646 redirections 301** | 21/08/2026 |
| Inventaire des piliers · plan consolidé · guide SEO local | « ~300 URL », « grille consolidée de **644 → 301** pages » | 22/08/2026 |
| Colonne 3 mois du KPI #1 | 217 pages avec impressions sur **1 395** publiées | 17/05 → 16/08 |

Une lecture cohérente se dessine — 1 395 URL historiques moins 646
redirections 301 posées ≈ 749, soit les ~755 mesurés — ce qui suggère que
« 301 » a été repris comme **un nombre de pages** alors qu'il désigne le
**code HTTP** des redirections. Le plan de consolidation lui-même parle de
1 368 → ≈ 682 pages de grille, pas de 644 → 301.

**Cette lecture n'est pas tranchée, et ce fichier ne la tranche pas.**
Conséquences pratiques, à respecter :

1. **Ne jamais réutiliser le ratio « pages avec impressions / pages
   publiées »** comme indicateur tant que le périmètre n'est pas fixé : les
   deux nombres viennent de périmètres différents.
2. **Ne pas écrire un compte d'URL comme un fait** dans un livrable. Le
   moteur écrit « plusieurs centaines d'URL » tant que le relevé n'a pas été
   refait.
3. **Faire trancher par `rushiti-indexation`** : relevé live du sitemap,
   comptage des 301 effectivement posées, et correction de la formule
   « 644 → 301 » dans les documents qui la portent si elle est confirmée
   erronée.

L'argument qui compte, lui, ne dépend pas du chiffre exact : la grille **a
été délibérément réduite**, et la regonfler défait un travail payé. C'est
cette conclusion-là qui gouverne les décisions, pas le nombre.
