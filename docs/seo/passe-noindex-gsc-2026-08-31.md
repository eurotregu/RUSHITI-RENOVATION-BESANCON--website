# Passe « Exclue par la balise noindex » — export GSC — 31/08/2026

> Analyse de l'export CoverageDrilldown fourni par Isuf le 31/08
> (`Excluded by 'noindex' tag`, 231 URL, crawls du 20/04 au 03/08/2026).
> Méthode : croisement des 231 URL avec le sitemap actuel (755 URL), les
> 646 règles de `_redirects` et les sources du dépôt de production, puis
> vérification live. Aucun chiffre inventé.

## Verdict

**85 pages commerciales vivantes portent un verdict `noindex` périmé.**
La cause a été corrigée le **20/08/2026** (PR #12 du dépôt de production :
`meta robots: noindex, follow` → `index, follow` sur 1 229 pages), mais le
dernier passage de Google sur ces URL date du **03/08 au plus tard** — deux
semaines et demie avant la correction. Aucune page du site ne sert
aujourd'hui de `noindex` : le dépôt en compte **0** sur 757 fichiers, et le
seul `X-Robots-Tag: noindex` du Worker vise `/merci`.

Action n°1 : **« Valider la correction »** sur ce motif dans Search Console.
C'est le seul motif du dossier où ce bouton est légitime — ici quelque chose
a réellement été corrigé, et la validation déclenche le recrawl du lot
entier, bien plus efficace que des demandes d'indexation une par une.

## Répartition des 231 URL

| Groupe | Nb | Nature | Sort |
|---|---|---|---|
| **Pages vivantes du sitemap** | **85** | Pages service × zone, `index, follow` en production, `lastmod 2026-08-20` au sitemap | ⚠️ **Le vrai enjeu** — recrawl à déclencher |
| Pages consolidées le 21/08 | 97 | Redirigent en 301 vers la page pilier (`/cloisons-pugey` → `/cloisons-besancon`…) | Basculeront en « Page avec redirection », motif voulu |
| Vestiges WordPress | 49 | Anciennes URL à mot-clé (`/peintre-besancon/`, `/ite-passif-besancon/`, `/etudes-de-cas/`, une URL de partage Facebook…) | 404 ou 301 via le Worker — rien à faire |

## Les 85 pages vivantes, par métier

| Service | Pages | Service | Pages |
|---|---|---|---|
| Isolation intérieure | 12 | Doublage des murs | 4 |
| Plâtrerie | 10 | Dégât des eaux | 4 |
| Revêtements de sol | 8 | Ratissage / enduit | 4 |
| Peinture extérieure | 7 | Toile de verre | 3 |
| Cloisons | 7 | Vitrification parquet | 3 |
| Peinture intérieure | 6 | Isolation | 2 |
| Papier peint | 6 | Lino / vinyle / LVT | 2 |
| Parquet flottant | 4 | Faux plafonds · Sol PVC | 1 + 1 |

**31 pages sur 12 quartiers de Besançon** (Battant, Chaprais, Planoise,
Palente, Montrapon, Bregille, Velotte, Saint-Ferjeux, Centre-ville, Butte /
Grette, Vaîte–Clairs-Soleils, Tilleroyes) et **53 pages en communes du
Doubs**, dont Pontarlier (plâtrerie) — zone d'expansion prioritaire.
Une page hors grille : `/renovation-cuisine-besancon/`.

## Preuves

| Contrôle | Résultat |
|---|---|
| `noindex` dans les sources de production | **0** occurrence sur 757 fichiers HTML |
| Balise robots des pages échantillonnées (dépôt) | `index, follow` — peinture-exterieure-centre-ville, platrerie-boussieres, parquet-flottant-planoise, degat-des-eaux-rancenay, peinture-interieure-palente |
| Contrôle live (Firecrawl, 31/08) | `/peinture-interieure-palente` → 200, `robots: index, follow` ; `/degat-des-eaux-rancenay` → 200, `robots: index, follow` |
| `X-Robots-Tag` du Worker déployé | posé uniquement sur `/merci` |
| Fichier `_headers` | absent — aucun en-tête d'indexation global |
| Date de la correction | PR #12 fusionnée le **20/08/2026 à 22h41** (1 229 pages) |
| Dernier crawl des 85 pages | **03/08/2026** (le plus récent), le plus ancien 05/05 |
| `lastmod` au sitemap | `2026-08-20` — le signal de fraîcheur est correct |

L'écart de dates est sans ambiguïté : Google n'a pas revu ces pages depuis
la correction. Il ne s'agit ni d'un défaut résiduel, ni d'une décision
éditoriale de Google, mais d'une file d'attente de crawl.

## Plan d'action

| # | Priorité | Action | Où | Effet attendu |
|---|---|---|---|---|
| 1 | 🔴 | **« Valider la correction »** sur le motif « Exclue par la balise noindex » | Search Console → Indexation → Pages → ce motif | Recrawl du lot de 231 URL ; les 85 pages vivantes peuvent enfin être indexées |
| 2 | 🟠 | Si la validation échoue ou traîne : inspection d'URL + demande d'indexation, **une seule fois**, sur une dizaine de pages à plus forte valeur (quartiers de Besançon et Pontarlier d'abord) | Search Console | Recrawl accéléré sur les pages qui comptent |
| 3 | 🟡 | Ne rien changer au contenu de ces pages pour l'instant | — | Une modification maintenant brouillerait la mesure du recrawl |
| 4 | 🟡 | Re-contrôle : nombre de pages indexées et disparition du motif | Search Console, vers le 13/09 | Mesure de l'effet réel |

## Ce que cet agent ne promet pas

Aucun délai d'indexation, et l'indexation elle-même n'est jamais garantie :
une fois le recrawl fait, Google réévalue chaque page sur son contenu et son
maillage. La validation lève l'obstacle technique, elle ne décide pas à la
place de Google. Si, après recrawl, une part de ces 85 pages bascule en
« Explorée, non indexée », le chantier deviendra celui de la différenciation
de contenu et du maillage interne — pas celui de la technique.

---

*Passe du 31/08/2026 — lecture seule, aucune modification de la production.
Sources : export GSC fourni par Isuf, sitemap et sources du dépôt
`eurotregu/rushiti-renovation` (HEAD), PR #12 de ce dépôt, contrôles live
Firecrawl.*
