# Diagnostic indexation — « 1 876 pages non indexées » (GSC) — 30/08/2026

> Déclencheur : question d'Isuf « pse 1 876 faqe nuk janë indeksuar ».
> Méthode : contrôle du site servi en production (robots.txt, sitemaps,
> échantillon de pages via Firecrawl), lecture du dépôt de production
> `eurotregu/rushiti-renovation` (checkout du 30/08) et croisement avec la
> vérification du 24/08 (`verification-page-avec-redirection-2026-08-24.md`).
> Aucun chiffre inventé. L'export CSV GSC du jour n'étant pas fourni, les
> répartitions par motif s'appuient sur le relevé documenté du 24/08.

## Verdict

Les ~1 876 « pages non indexées » ne sont **pas 1 876 pages du site** : le
site n'a que **755 URL** au sitemap (757 fichiers HTML). Ce chiffre est le
**total de tous les motifs de non-indexation** de Search Console, et il est
pour l'essentiel la **trace comptable voulue de la consolidation du 21/08**
(sitemap passé de 1 395 à 755 URL, 647 redirections 301 posées) plus les
restes de l'ancien site WordPress. Relevé du 24/08 : indexées 256 ·
redirection 413 · 404 : 212 · noindex 231 · découverte non indexée 946 ·
explorée non indexée 61 — soit **1 863 non indexées**, cohérent avec les
1 876 vues aujourd'hui.

Aucun défaut technique bloquant n'a été trouvé sur les pages actives
échantillonnées. L'action n° 1 est de **vérifier que le déploiement
consécutif à la PR #28 (fusionnée ce soir) est bien parti en production** :
au moment du contrôle, la production servait encore l'ancien jeu de
sitemaps (index + `sitemap-communes.xml` vide) alors que le dépôt HEAD
porte le `sitemap.xml` unique de 755 URL.

## Vérifications (échantillon de pages actives)

Pages contrôlées en live : `/degat-des-eaux-beure` et
`/vitrification-parquet-champoux` (gabarit service × localité, représentatives
des ~740 pages programmatiques — échantillonnage explicite, le diagnostic
vaut pour le gabarit).

| # | Contrôle | Résultat | Preuve |
|---|---|---|---|
| 1 | Statut HTTP | ✅ 200 | Firecrawl, les deux pages |
| 2 | robots.txt servi | ✅ | `User-agent: * / Allow: /` (seuls 6 bots commerciaux bloqués : Amazonbot, Bytespider, FacebookBot, Google-CloudVertexBot, meta-externalagent, TikTokSpider) |
| 3 | Meta robots / X-Robots-Tag | ✅ | `content="index, follow"` ; **aucun `noindex` dans les 757 fichiers HTML du dépôt de production** (grep exhaustif) |
| 4 | Canonical | ✅ auto-référent | `href="https://rushiti-renovation.fr/degat-des-eaux-beure"` (idem Champoux) |
| 5 | Sitemap | ✅ | URL identiques caractère par caractère (https, sans www, sans slash final) |
| 6 | Variantes d'URL | ✅ | `/degat-des-eaux-beure/` et `.html` → 301 vers l'URL canonique (normalisation Cloudflare + `_redirects`) |
| 7 | Contenu | ✅ substantiel | ~2 350 et ~1 900 mots ; différenciation réelle à confirmer page par page (gabarit commun) |
| 8 | Version déployée | ⚠️ écart | Live : `sitemap.xml` = index vers `sitemap-pages.xml` + `sitemap-communes.xml` (vide) ; robots.txt live déclare encore `sitemap-communes.xml`. Dépôt HEAD (PR #28, fusionnée le 30/08 au soir) : `sitemap.xml` unique en urlset 755 URL, robots.txt à une seule ligne Sitemap. La production est en retard d'un déploiement. |
| 9 | Correction `/blog` (24/08) | ✅ fusionnée | `blog.html` présent + `/blog/ /blog 301` dans `_redirects` (PR #25 intégrée) |

## Pages par motif GSC (relevé du 24/08, ~1 863 non indexées)

| Motif GSC | Nb | Nature | Classement | Action |
|---|---|---|---|---|
| Page avec redirection | 413 | Les 647 × 301 de la consolidation (`service-commune → service-besancon`) + anciennes URL WordPress | **Voulu** — décision documentée et approuvée (vérif. du 24/08) | Aucune. Le « Échec » de validation est attendu ; le chiffre montera vers ~650 au fil du recrawl, c'est normal |
| Découverte, non indexée | 946 | Majoritairement : anciennes URL communales connues de Google avant consolidation (basculeront en « redirection » au recrawl) + pages actuelles en file d'attente | Mixte : comptable + décision Google | Export CSV pour séparer les deux ; pour les URL actives : maillage + différenciation, pas de demande d'indexation en masse |
| Exclue par balise noindex | 231 | **Aucun noindex n'existe dans le site actuel** (vérifié) → état de crawl périmé d'anciennes URL (ère WordPress) | Comptable / à confirmer | Export CSV pour lister ces URL ; si ce sont bien des URL mortes, rien à faire, elles s'éteindront |
| Introuvable (404) | 212 | Anciennes URL (WordPress ?) sans redirection | **Chantier ouvert** depuis le 24/08 | Passe dédiée : exporter la liste, poser des 301 dans `_redirects` pour celles qui ont des backlinks ou des impressions, laisser mourir les autres |
| Explorée, non indexée | 61 | Décision Google sur des pages jugées trop proches de leurs sœurs | Décision Google | Différenciation du contenu + liens entrants internes ; ne se répare pas par « demander l'indexation » |

**Lecture d'ensemble : 256 pages indexées sur 755 actives (~34 %).** Le vrai
chantier n'est pas le chiffre de 1 876 (gonflé aux deux tiers par des URL
volontairement supprimées ou héritées) mais l'écart 256 → 755 sur les pages
conservées, 9 jours seulement après une consolidation majeure que Google
digère encore.

## Plan d'action priorisé

| # | Priorité | Action | Où | Effet attendu |
|---|---|---|---|---|
| 1 | 🔴 | Vérifier que le déploiement post-PR #28 est bien en ligne : `https://rushiti-renovation.fr/sitemap.xml` doit devenir un urlset de 755 URL (plus un index), et robots.txt ne plus citer `sitemap-communes.xml`. Si le déploiement est manuel : redéployer le **dossier complet** | Cloudflare Pages | Google lit un sitemap unique et cohérent avec le dépôt |
| 2 | 🟠 | Fournir l'export CSV GSC « Indexation des pages » (chaque motif → Exporter) | Search Console → Pages | Permet la passe par motif : ventiler les 946 « découverte », lister les 231 « noindex » et les 212 « 404 » |
| 3 | 🟠 | Passe 404 : poser des 301 dans `_redirects` pour les anciennes URL à backlinks/impressions | Dépôt de production, `_redirects` | Récupère le jus des anciennes URL ; éteint le motif |
| 4 | 🟠 | Garde-fou D.1 toujours ouvert : export croisé requête × page pour confirmer qu'aucune page qui imprimait n'a été redirigée le 21/08 | Search Console → Performances | Clôt la seule inconnue de la consolidation |
| 5 | 🟡 | Pour les pages actives non indexées : différenciation de contenu et maillage interne (3+ liens entrants par page conservée) | → `rushiti-maillage-interne`, `rushiti-architecte-seo` | Fait monter le ratio 256/755 ; c'est le levier réel |
| 6 | 🟡 | Ne **pas** relancer la validation « Page avec redirection » ni demander l'indexation en masse | Search Console | Évite de perdre du temps sur un motif voulu |

## À faire dans Search Console

Rien à « corriger » avant l'export : la majorité des motifs sont voulus ou
hérités. Après la passe 404 (action 3), inspection d'URL et demande
d'indexation **une seule fois** sur les seules pages commerciales corrigées.

## Ce que cet agent ne promet pas

Aucun délai d'indexation : Google ne garantit rien, surtout après une
consolidation de cette ampleur (la digestion des 647 redirections prend
typiquement plusieurs semaines). Re-contrôle suggéré vers le **13/09/2026** :
si le nombre d'indexées ne progresse pas d'ici là, passer à la passe
différenciation/maillage en priorité haute.

---

*Diagnostic du 30/08/2026 — lecture seule, aucune modification de la
production. Sources : site servi (Firecrawl), dépôt `eurotregu/rushiti-renovation`
(HEAD 3c4ba4a), vérification du 24/08. Corrections à valider par Isuf.*
