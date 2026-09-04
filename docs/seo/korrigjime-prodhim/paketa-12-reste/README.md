# Paketa 12 — reste du plan d'action (03/09/2026)

| | |
|---|---|
| Déclencheur | Isuf, 03/09 : « vazhdoni me të gjithat e papërfunduara » |
| Dépôt cible | `eurotregu/rushiti-renovation` — appliqué directement (PR de production, brouillon à valider) |
| Script | `fix_reste.py` (idempotent, simulation par défaut, `--apply`) |

## Ce qui est appliqué (760 fichiers)

| Constat | Correction | Portée |
|---|---|---|
| 4 (geo) | Coordonnées du 18 rue du Professeur Haag relevées dans la **Base Adresse Nationale** (id `25056_4260_00018`, score 0,82) : 47.245638 / 6.00556, à la place du centre-ville | 735 nœuds LocalBusiness |
| 2 (hébergeur) | Cloudflare, Inc., 101 Townsend St, San Francisco, CA 94107, contact dpo@cloudflare.com — tels que publiés dans la politique de confidentialité de Cloudflare (relevé 03/09) ; commentaire « à vérifier » retiré | mentions-legales.html |
| 2 / 21 (GTM) | Conteneur lu : GA4 `G-QER2M5L3GL` + 4 événements, conditionnés au consentement. Section 7 réécrite ; commentaire retiré. Voir `../../mesure/inventaire-gtm-ga4-2026-09-03.md` | mentions-legales.html |
| 2 (bandeau) | Bandeau : « cookies de mesure d'audience (Google Analytics) et de mesure publicitaire (Meta) » | 755 pages |
| 16 | Bloc « par quartier et dans le Doubs » des piliers : 13 quartiers visibles, les 12 groupes de communes (62 liens) dans un `<details>` replié. Tous les liens restent dans le HTML : le maillage vers la grille est intact, seule la hauteur de page change | 16 piliers |
| 20 | `sitemap.xml` : `lastmod` = date du dernier commit git du fichier ; `changefreq` et `priority` retirés | 755 URL |
| 18 | Accueil : « la Boucle du Doubs, le secteur Vauban » → « le centre ancien, dans la boucle du Doubs » ; « appartement de la Boucle » → « appartement du centre ancien » | index.html |
| 17 | « Mis à jour le … » dans la ligne de métadonnées des 3 articles dont `dateModified` ≠ `datePublished` | 3 articles |
| 11 | Galerie en 2 colonnes sous 760 px (accueil et réalisations) | 2 CSS, `?v=10` |

## Non appliqué, et pourquoi

| Constat | Raison |
|---|---|
| 19 Twitter Cards | **Décision d'Isuf du 02/09** (`fix_hiq_twitter.py`) : pas de compte X, les cartes ont été retirées volontairement. Le constat 19 de l'audit est caduc. |
| 25 Charte v2.7 | Décision d'Isuf : dossier d'arbitrage avec 3 aperçus dans `../../charte/`. |
| 5 RDV Artisans | Site tiers : courrier prêt dans `../../annuaires/rdv-artisans-doublon-2026-09-03.md`. |
| 15 Cannibalisation | Export Search Console requis. |
| 11 (image de tête humaine), 12 (portraits) | Photos à fournir. |
| 26 Copie GitHub Pages | Alignée dans ce dépôt (compteurs inventés retirés, plomberie/électricité et carrelage retirés, `priceRange` retiré) ; l'option « redirection vers la production » reste ouverte. |

Test du 03/09 : simulation 760 fichiers → application → second passage 0 ; 755 JSON-LD valides, une seule latitude restante (47.245638) ; sitemap parsé ; vérificateurs des paquets 10 et 11 à 0 écart ; captures : bloc communes replié/déplié, galerie mobile 2 colonnes.

## Après fusion

Purger le cache Cloudflare ; relire `/mentions-legales` (sections 3 et 7), le bandeau, `/peinture-interieure-besancon` (bloc zones), l'accueil sur mobile ; soumettre à nouveau `sitemap.xml` dans la Search Console.
