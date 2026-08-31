# Résolution — Worker sitemap-unique déployé — 31/08/2026

> Clôture du volet technique du dossier « 1 876 pages non indexées »
> (diagnostic du 30/08 + addendum du 31/08). Le correctif du Worker
> `image-license-jsonld` a été déployé après approbation explicite d'Isuf
> via une session Claude Code en mode de permissions par défaut (Option B),
> le contrôleur de permissions de la session principale ayant exigé une
> validation humaine.

## Contrôles après déploiement (31/08, en live)

| Contrôle | Attendu | Constaté |
|---|---|---|
| `WORKER_VERSION` du script déployé (API Workers) | `2026-08-31-sitemap-unique` | ✅ `2026-08-31-sitemap-unique`, plus aucune occurrence de `sitemapindex` dans le code |
| Purge du cache de la zone (sitemap.xml, robots.txt, anciens sitemaps, variantes www) | exécutée | ✅ `purge_success: true` |
| `https://rushiti-renovation.fr/robots.txt` | une seule ligne `Sitemap:` | ✅ `Sitemap: https://rushiti-renovation.fr/sitemap.xml`, la ligne `sitemap-communes.xml` a disparu |
| `https://rushiti-renovation.fr/sitemap.xml` | `<urlset>` de 755 URL | ✅ urlset, 755 `<loc>` |
| `https://rushiti-renovation.fr/sitemap-pages.xml` | 301 → `/sitemap.xml` | ✅ redirection suivie jusqu'à `/sitemap.xml` (200) |

Le domaine sert désormais exactement ce que porte le dépôt de production
(PR #28) : un sitemap unique, cohérent avec le robots.txt et le maillage.

## Reste à faire

1. **Synchroniser la copie versionnée** `cloudflare/worker-image-license-jsonld.js`
   du dépôt de production (règles 1 et 3 de `cloudflare/README.md`) : elle est
   restée à `2026-08-22-cache-versionne` alors que la production est passée
   par `2026-08-28-assurance-ergo-b` puis `2026-08-31-sitemap-unique`. La
   session d'approbation (Option B) peut le faire : récupérer le script
   déployé via l'API Workers et le committer tel quel dans le dépôt, en
   reportant la version dans le README. L'accès en écriture au dépôt de
   production a été refusé à la session principale par son contrôleur de
   permissions.
2. **Search Console → Sitemaps** : retirer les soumissions `sitemap-pages.xml`
   et `sitemap-communes.xml` si présentes, (re)soumettre `sitemap.xml` (Isuf).
3. **Les deux exports Search Console** (Isuf) : « Indexation des pages » par
   motif (surtout Introuvable 404 et Exclue par noindex) et « Performances »
   10/06 → 18/08/2026 — pour la passe 404, la liste des noindex et le
   garde-fou D.1.

---

*Consigné le 31/08/2026. Sources : API Cloudflare (script déployé, purge),
contrôles live Firecrawl. Aucun chiffre inventé.*
