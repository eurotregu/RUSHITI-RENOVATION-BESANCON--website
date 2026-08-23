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
| Rapport KPI #1 (`docs/seo/raporte/raport-fjale-kyce-2026-08.md`) | 17/05 → 16/08/2026 | baseline Search Console |
| Plan consolidé (`docs/seo/raporte/plan-veprimi-konsoliduar-2026-08.md`) | 22/08/2026 | 14 entrées priorisées, 6 sources fusionnées |
| Opportunités GSC | 20/08/2026 | gisements par cluster |
| Inventaire des piliers | 22/08/2026 | sitemap ~300 URL |
| Relevé avis Google (`docs/seo/avis-google-releve-2026-08-22.md`) | 22/08/2026 | note et nombre d'avis |
| Audit technique | 13/08/2026 | P0-A domaines, P1-B GA4, P2-B local |

## Porte 1 — Google : la baseline

| Indicateur | Valeur | Période |
|---|---|---|
| Clics | 52 | 17/05 → 16/08/2026 |
| Impressions | 5 670 | idem |
| CTR | 0,9 % | idem |
| Position moyenne | 14,3 | idem |
| Pages avec impressions | 217 | idem |
| Gisement top-10 sans clic | 249 impressions | idem |
| Position de la requête de marque | 22,1 🔴 | idem |

**Le fait qui gouverne tout le reste** : **79 % des clics viennent de
l'accueil** (relevé du 22/08/2026), pendant que les pages piliers restent en
pages 2 à 5. Le site n'a pas d'abord un problème de visibilité — il a un
problème de **répartition** et de **conversion de la visibilité existante**.

Conséquence directe sur la priorisation : avant d'écrire une page neuve, la
question rentable est « pourquoi ces impressions ne cliquent-elles pas ? ».

### Les gisements mesurés (par ordre de volume)

| Cluster / page | Mesure | Lecture |
|---|---|---|
| « entreprise de peinture à besançon » | 1 343 impressions · position 3,5 · **0 clic** | Le plus gros gisement du site. Bien classé, jamais cliqué — le pack local capte le clic avant l'organique |
| Cluster moisissure (`/blog/moisissure-plafond-salle-de-bain-besancon`) | ≈ 620 impressions · 2 clics | 2ᵉ visibilité du site. Enrichissement déjà live, paquet complémentaire en validation |
| `/platrerie-besancon` | position **9,1** | À une porte de la page 1. Aucun pilier voisin ne le pousse |
| `/ratissage-enduit-besancon` | position **10,9** | Idem |
| `/degat-des-eaux-besancon` | 33 impressions / 12 mois · position 16 | **Le silo le plus rentable du métier, quasi invisible.** Priorité de renforcement n°1 |
| `/isolation-interieure-besancon` | **0 impression** / 12 mois | La page existe et ne reçoit rien : il lui manque un satellite qui pousse |
| Requête « rushiti-renovation.fr » | position 23 · 49 impressions · 0 clic | Anomalie de marque : on ne ressort pas sur son propre domaine. Contrôle canonical / variante www |

## Porte 2 — Moteurs de réponse

| Indicateur | Valeur au 23/08/2026 |
|---|---|
| Part de voix IA (panel fixe de 14 requêtes) | `NM` — aucune mesure consignée dans le dépôt |
| Relevé de corpus cité (`docs/seo/citations-ia/`) | `NM` — seul le modèle CSV vide existe |
| robots.txt et crawlers IA | `NM` — à vérifier par `rushiti-visibilite-ia` |

**C'est le trou le plus net du dispositif au 23/08/2026** : l'outillage est en
place (deux agents, un dictionnaire de colonnes, un modèle CSV, un panel de
14 requêtes figé), **aucune mesure n'a encore été prise**. Le premier relevé
n'aura pas de comparatif : il est la référence, et c'est normal.

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
| Consolidation de la grille locale **644 → 301 pages** (63 épargnées) | août 2026 | idem |
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
| **Domaine principal** — `rushiti.fr`, `rushiti-renovation.fr` et le microsite Localo dispersent l'autorité (audit du 13/08, P0-A). Recommandation : tout en 301 vers `rushiti-renovation.fr` | Fort | 10 minutes de décision + le sitemap de `rushiti.fr` |
| **Carrelage** — « Carrelage & Sol » figure sur l'accueil héritée, aucune prestation ni page confirmée | Cohérence de l'offre | Une phrase de réponse |
| **« devis sous 48 h »** — présent dans un title live et dans les preuves du registre, mais classé « promesse à valider » par deux autres agents | Engagement contractuel | Une phrase de réponse |
| **`/sol-pvc-besancon` vs `/lino-vinyle-lvt-besancon`** — doublon signalé | Cannibalisation | → `rushiti-cannibal-check` |

## Données périssables — à revérifier le jour de l'usage

- **Note et nombre d'avis Google** : 34 avis, 4,7/5 au relevé du 22/08/2026.
  Ne jamais recopier d'un ancien document : ce compteur bouge.
- **Nombre d'URL du sitemap** : ~300 au 22/08/2026.
- **Positions et impressions** : toute valeur ci-dessus est datée. Au-delà de
  trois mois, elle sert d'historique, plus de baseline.

## Un écart à lever

Le rapport KPI #1 rapporte **217 pages avec impressions sur 1 395 pages
publiées**, alors que le sitemap relevé le 22/08/2026 compte **~300 URL**.
L'écart s'explique probablement par l'héritage d'avant la consolidation
644 → 301 et par d'anciennes URL WordPress encore connues de Google. Il
**n'est pas tranché** : avant de réutiliser le ratio « pages avec
impressions / pages publiées » comme indicateur, le faire vérifier par
`rushiti-indexation`. Un ratio calculé sur deux périmètres différents ne
mesure rien.
