# État du moteur — la ligne de départ

> C'est l'équivalent RUSHITI du `seo-brief.md` que le playbook générique fait
> écrire par un entretien. Ici il n'est pas déclaratif : **chaque ligne vient
> d'un relevé daté du dépôt.** Ce qui n'a pas été mesuré est marqué `NM` et
> ne devient jamais `0`.
>
> **Dernière consolidation : 24/08/2026.** Toute donnée de plus de trois mois
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
| Vérification « Page avec redirection » (`docs/seo/verification-page-avec-redirection-2026-08-24.md`) | 24/08/2026 | **taille réelle du site**, contrôle croisé sitemap ↔ `_redirects` ↔ fichiers de production |

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
| Consolidation de la grille locale : **1 395 → 755 URL**, par **646 redirections 301** (63 pages épargnées) | 21/08/2026, vérifiée le 24/08 | plan consolidé 22/08 + vérification du 24/08 |
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
- **Nombre d'URL du sitemap** : **755**, contrôlées une à une contre les
  fichiers de production le 24/08/2026. Écart clos — voir ci-dessous.
- **Positions et impressions** : toute valeur ci-dessus est datée, et sa
  **fenêtre** fait partie de la valeur. Au-delà de trois mois, elle sert
  d'historique, plus de baseline.

## L'écart levé — la taille réelle du site

**Cet écart a été tranché le 24/08/2026**, par contrôle croisé du sitemap, du
fichier `_redirects` et des fichiers du dépôt de production
(`docs/seo/verification-page-avec-redirection-2026-08-24.md`). Les chiffres
mesurés, à retenir :

| Grandeur | Valeur vérifiée | Date |
|---|---|---|
| URL déclarées au sitemap | **755** | 24/08/2026 |
| URL du sitemap sans fichier correspondant | **1** (`/blog`, corrigée depuis) | 24/08/2026 |
| URL à la fois au sitemap et redirigée | **0** | 24/08/2026 |
| Redirections 301 dans `_redirects` | **646** | 21/08/2026 |
| Sitemap avant consolidation | 1 395 URL | — |

**Ce que « 644 → 301 » voulait dire.** La formule circule dans plusieurs
documents internes ; l'exécution réelle est **1 395 → 755 URL, par 646
redirections 301**. Le « 301 » de la formule est le **code HTTP** des
redirections, pas un nombre de pages restantes. À ne plus recopier sous cette
forme : écrire « consolidation de 1 395 à 755 URL (646 redirections 301,
21/08/2026) ».

**Conséquence sur le ratio d'indexation.** Les deux nombres du rapport KPI #1
sont maintenant lisibles : 217/1 395 est la colonne 3 mois (périmètre
d'**avant** consolidation), 394/755 la colonne 12 mois (périmètre courant).
Le ratio « pages avec impressions / pages publiées » redevient utilisable, à
condition de rester dans la même colonne.

**Un effet de bord à ne pas confondre avec une panne.** Search Console signale
413 URL en « Page avec redirection » et une validation en échec : c'est le
comportement **attendu** après une consolidation voulue, tracée et autorisée.
Aucune correction n'est à faire de ce côté. La seule anomalie réelle trouvée
au contrôle était `/blog` (sitemap, canonical et 1 542 liens internes pointant
vers une URL qui redirigeait), corrigée dans le dépôt de production.

L'argument de fond reste inchangé, et il ne dépendait pas du chiffre : la
grille **a été délibérément réduite**, et la regonfler défait un travail payé.
