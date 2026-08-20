# Configuration Google Search Console — rushiti-renovation.fr

| Fichier | Quoi | Où ça va |
|---|---|---|
| `configuration-ultra-premium.md` | Le relevé du 20/08/2026 + le mode d'emploi complet de la configuration GSC, bloc par bloc, avec la checklist à cocher | Document de travail — reste dans le dépôt |
| `robots.txt` | Le `robots.txt` de production **corrigé** : la ligne `Sitemap: …/sitemap-communes.xml` est retirée, ce sitemap étant vide (0 URL) et redondant | **Racine de rushiti-renovation.fr**, via le déploiement Cloudflare Pages |

## Attention au périmètre

Ce dépôt est la **copie GitHub Pages** du site, en `noindex` depuis la PR #18.
La production `rushiti-renovation.fr` tourne sur **Cloudflare Pages** : fusionner
une PR ici ne déploie rien en ligne, et n'apparaîtra jamais dans Search Console.

Le `robots.txt` fourni est donc volontairement rangé dans `docs/gsc/` et **non**
à la racine du dépôt : à la racine, il serait servi par GitHub Pages, c'est-à-dire
au mauvais endroit — et il autoriserait l'indexation d'une copie qui doit rester
invisible.

## Les actions non automatisables

Tout ce qui se passe dans l'interface Search Console (vérification de propriété,
utilisateurs, soumission du sitemap, inspection d'URL) demande le compte Google
d'Isuf. Aucun outil ne peut s'y substituer : ces points sont listés en Partie 4
du document sous forme de checklist.

Pour faire analyser les données GSC ensuite, il faut fournir un **export CSV**
(Performance sur 3 mois minimum, ou Index → Pages) — les skills d'analyse
travaillent sur le fichier, pas sur l'écran.
