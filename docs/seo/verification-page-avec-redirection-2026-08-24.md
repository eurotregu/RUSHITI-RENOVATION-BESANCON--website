# Vérification — alerte Search Console « Page avec redirection » (24/08/2026)

> Déclencheur : e-mail Search Console du 23/08/2026 19h44 (`[WNC-20237597]`),
> nouveau motif de non-indexation « Page avec redirection » sur
> `https://rushiti-renovation.fr/`. Question posée par Isuf : les ~700 pages
> communales qui redirigent vers les pages piliers sont-elles voulues ?
> Réponse demandée : **vérifier d'abord**, la décision n'étant plus en mémoire.
>
> Méthode : lecture des sources du dépôt de documentation et du **code réel du
> dépôt de production** `eurotregu/rushiti-renovation` (checkout du 24/08),
> contrôle croisé sitemap ↔ `_redirects` ↔ fichiers HTML. Aucun chiffre repris
> de mémoire.

## Verdict : la consolidation est voulue, décidée et tracée

Oui. Elle n'est pas une panne, et il n'y a rien à « réparer » du côté des 413
pages signalées. Quatre preuves indépendantes et datées :

| Source | Ce qu'elle établit |
|---|---|
| `_redirects` du dépôt de production, en-tête du bloc | Critère écrit dans le fichier lui-même : *« Consolidation de la grille (audit des mots-clés, 21/08/2026) : zones hors palier, aucune impression GSC sur 10/06-18/08/2026 »* |
| `propozim-skill-keyword-map-2026-08.md` § 5.3 | Règle de doctrine : *page à demande réelle zéro (vérifiée GSC + volumes) → **301 vers le service du niveau supérieur**, mise à jour sitemap + maillage*. Grille de 686 pages candidates |
| Même document, addendum du 21/08 § B | Constat d'exécution : sitemap passé de 1 395 à **755 URL**, `sitemap-communes.xml` vidé, **646 redirections 301** dans `_redirects`, toutes du type `service-commune → service-besancon` |
| `raporte/plan-veprimi-konsoliduar-2026-08.md` (22/08), synthèse | La *« consolidation de la grille 644 → 301 avec 63 pages épargnées »* est listée parmi les chantiers **déjà réalisés**, retirés du plan à ce titre |

Autorisation : Isuf a donné le feu vert (« kryeni të gjitha veprimet e
nevojshme ») puis approuvé l'accès push au dépôt de production le 21/08 au soir
(addendum § D.4).

**Conséquence pour Search Console :** les 413 « Page avec redirection »
recouvrent ces 645 redirections voulues plus les anciennes URL WordPress déjà
redirigées volontairement. Google signale la disparition d'URL qu'il avait au
sitemap — comportement normal après une consolidation. La validation « Échec »
sur ce motif est attendue et n'appelle aucune correction.

## L'anomalie réelle : `/blog`

Contrôle croisé des 755 URL du sitemap contre les fichiers du dépôt de
production, le 24/08 :

| Contrôle | Résultat |
|---|---|
| URL du sitemap sans fichier correspondant | **1** — `/blog` |
| URL à la fois déclarée au sitemap et redirigée | 0 |
| Fichiers orphelins (ni sitemap ni redirection) | `/404`, `/merci` — attendus |

Mécanique du défaut : `blog/index.html` n'était servi qu'à `/blog/`, alors que
le sitemap déclarait `/blog`, que la balise canonique de la page pointait vers
`/blog` — donc vers l'URL qui redirige — et que **1 542 liens internes**
pointent vers `/blog`. Sitemap, canonical et maillage se contredisaient. C'est
très probablement le « nouveau motif » remonté par l'e-mail.

**Correction posée** — PR #25 du dépôt de production, en brouillon :
`blog/index.html` → `blog.html` (donc `/blog` en 200, canonical exacte) et
`/blog/ /blog 301` dans `_redirects`. Format canonique sans slash final,
conforme à la doctrine P2-A de l'audit du 13/08. Aucun chemin relatif dans la
page (7 `href`/`src`, tous absolus) : le déplacement ne casse rien. Contrôle
croisé rejoué après correction : 755/755 URL du sitemap ont un fichier.

## Garde-fou toujours ouvert

Le plan de consolidation posait une condition : **« aucune page qui imprime
n'est supprimée »**. Elle n'a jamais été confirmée. Elle exige l'export croisé
requête × page de Search Console, qui reste non fourni — c'est le point D.1 de
l'addendum du 21/08, déjà signalé en ⚠️ à l'époque. Les 645 redirections ont
été posées sur le seul critère « 0 impression 10/06-18/08 », sans cette
contre-vérification.

Tant que cet export manque, il n'est pas établi que la consolidation n'a pas
redirigé une page qui recevait des impressions. Rien dans les données
disponibles ne dit qu'elle l'a fait ; rien ne dit le contraire non plus.

## Autres motifs de l'e-mail, non traités ici

Relevé Search Console du 24/08 : indexées 256 · Page avec redirection 413
(validation en échec) · Introuvable 404 : 212 (validation non lancée) · Exclue
par balise noindex 231 · Découverte non indexée 946 · Explorée non indexée 61.
Les 212 « Introuvable (404) » n'ont pas été instruites dans cette vérification
et demandent leur propre passe (→ `rushiti-indexation`).

---

*Vérification du 24/08/2026. Sources : dépôt de documentation et code du dépôt
de production `eurotregu/rushiti-renovation` (checkout réel). Aucun chiffre
inventé, aucun classement promis.*
