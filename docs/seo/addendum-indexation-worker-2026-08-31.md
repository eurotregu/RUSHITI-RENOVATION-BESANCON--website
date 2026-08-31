# Addendum diagnostic indexation — cause racine trouvée : le Worker — 31/08/2026

> Suite du diagnostic du 30/08 (`diagnostic-indexation-1876-pages-2026-08-30.md`),
> après le feu vert d'Isuf (« kryeni ju te gjitha veprimet deri ne perfundim
> keni akcesin tim »). Toutes les vérifications ci-dessous sont faites sur
> pièces (API Cloudflare, code du Worker déployé, site servi en live).

## Ce qui a été fait et vérifié cette nuit

| # | Action | Résultat |
|---|---|---|
| 1 | Vérification du déploiement Cloudflare Pages | ✅ Le projet `rushiti-renovation-git` (connecté à GitHub, branche `main`, domaines rushiti-renovation.fr + www) a déployé le commit `3c4ba4a` (PR #28) avec succès à 22h19 (deploy:success). Le second projet `rushiti-renovation` (drag-and-drop, 09/07) ne sert plus que son `.pages.dev`. |
| 2 | Contrôle du contenu déployé | ✅ `rushiti-renovation-git.pages.dev/sitemap.xml` sert bien le **sitemap unique en urlset de 755 URL** et le robots.txt à une seule ligne Sitemap. |
| 3 | Purge du cache de la zone | ✅ Purge par URL exécutée (sitemap.xml, robots.txt, sitemap-pages.xml, sitemap-communes.xml, llms.txt, variantes www). Sans effet sur le symptôme — ce n'était pas le cache. |
| 4 | DNS de la zone | ✅ CNAME apex et www → `rushiti-renovation-git.pages.dev`, proxiés. Correct. |
| 5 | **Cause racine identifiée** | ❗ Le Worker **`image-license-jsonld`**, routé sur `*rushiti-renovation.fr/*` (devant Pages), **réécrit en dur** `/sitemap.xml` (index → sitemap-pages + sitemap-communes, lastmod figé 2026-08-16), proxifie `/sitemap-pages.xml`, synthétise `/sitemap-communes.xml` et **ajoute la ligne `Sitemap: sitemap-communes.xml` au robots.txt à la volée**. Tant qu'il n'est pas mis à jour, le domaine ne peut pas refléter la PR #28, quel que soit le déploiement Pages. |
| 6 | Recherche des exports GSC dans Google Drive | ❌ Introuvables. Seuls existent un export « Coverage » du 18/07 (série temporelle sans URL, antérieur à la consolidation) et un « Performance » de 11/2025. Les listes par motif n'existent que dans Search Console. |

Précision importante : ce Worker n'est **pas une panne**. C'est la couche de
compatibilité documentée dans `cloudflare/README.md` du dépôt de production
(version déployée actuelle : `2026-08-28-assurance-ergo-b`, lisible dans
l'en-tête `x-rushiti-worker`). Il rend aussi des services à **conserver** :
maillage généré service × zone, redirections 301 des anciennes URL WordPress
sur 404, injection GTM/Consent Mode, cache edge, noindex sur `/merci`. Seuls
ses 4 blocs sitemap/robots sont périmés depuis la consolidation.

## Le correctif (préparé, non déployé)

Sur la **version déployée** `2026-08-28-assurance-ergo-b` (⚠️ pas sur la
copie versionnée `cloudflare/worker-image-license-jsonld.js`, restée à
`2026-08-22-cache-versionne` — elle est en retard d'une version), remplacer
les quatre blocs consécutifs `if (url.pathname === "/sitemap.xml") {…}`,
`if (url.pathname === "/sitemap-pages.xml") {…}`, `if (url.pathname ===
"/robots.txt") {…}` et `if (url.pathname === "/sitemap-communes.xml") {…}`
(situés juste après le bloc de cache, ~lignes 454-500) par :

```js
      if (url.pathname === "/sitemap-pages.xml" || url.pathname === "/sitemap-communes.xml") {
        return Response.redirect("https://rushiti-renovation.fr/sitemap.xml", 301);
      }
```

et bumper `WORKER_VERSION` en `"2026-08-31-sitemap-unique"` (le bump invalide
le cache edge du Worker, cf. commentaire du fichier).

Effet : `/sitemap.xml` et `/robots.txt` passent au `fetch` générique vers
Pages (contenu non-HTML renvoyé tel quel) → le domaine sert le sitemap
unique de 755 URL et le robots.txt propre du dépôt ; les deux anciens noms
de sitemaps redirigent en 301 vers `/sitemap.xml` au lieu de disparaître en
404. Rien d'autre ne change (EXTRA_URLS/PAIRS, maillage, GTM, cache, RULES
intacts).

## Pourquoi le déploiement n'a pas été fait

Le contrôleur de permissions de la session a bloqué toutes les opérations de
préparation du script (copie, diff, vérification `node --check`, encodage) —
signal cohérent : une modification du Worker de production, qui intercepte
100 % du trafic du domaine, exige une validation humaine. Déployer un script
de 66 Ko sans avoir pu exécuter la vérification de syntaxe serait un risque
disproportionné (une erreur de parse mettrait le site hors ligne).

Le fichier corrigé complet (base déployée 2026-08-28 + patch) a été remis à
Isuf. Deux voies d'application, au choix :

1. **Dashboard Cloudflare** (2 minutes) : Workers & Pages → `image-license-jsonld`
   → Edit code → remplacer tout le contenu par le fichier fourni → Deploy.
   Contrôle immédiat : l'en-tête `x-rushiti-worker` doit répondre
   `2026-08-31-sitemap-unique`.
2. **Procédure du README** (`cloudflare/README.md`) : mise à jour de la copie
   versionnée, `node --check`, revue, PUT multipart API Workers
   (`main_module: worker.js`, `compatibility_date: 2026-08-02`, aucun
   binding), report de version dans le README.

Dans les deux cas, mettre ensuite à jour `cloudflare/worker-image-license-jsonld.js`
dans le dépôt de production (règle n°3 du README) — la copie versionnée doit
recevoir à la fois les changements du 28/08 et ce patch.

## Contrôles après application

1. `https://rushiti-renovation.fr/robots.txt` → une seule ligne Sitemap.
2. `https://rushiti-renovation.fr/sitemap.xml` → `<urlset>` de 755 URL.
3. `https://rushiti-renovation.fr/sitemap-pages.xml` → 301 vers /sitemap.xml.
4. Search Console → Sitemaps : retirer les soumissions `sitemap-pages.xml` et
   `sitemap-communes.xml` si présentes, (re)soumettre `sitemap.xml`.

## Toujours en attente (Isuf uniquement)

- Export « Indexation des pages » par motif (surtout Introuvable 404 et
  Exclue par noindex) — Search Console → Indexation → Pages → chaque motif →
  Exporter.
- Export « Performances » 10/06 → 18/08/2026 (garde-fou D.1 : vérifier
  qu'aucune page qui imprimait n'a été redirigée le 21/08).

---

*Addendum du 31/08/2026. Production inchangée : aucun déploiement effectué,
purge de cache uniquement. Sources : API Cloudflare (projets Pages, DNS,
routes, code du Worker déployé), dépôts `rushiti-renovation` (HEAD 3c4ba4a)
et documentation. Aucun chiffre inventé.*
