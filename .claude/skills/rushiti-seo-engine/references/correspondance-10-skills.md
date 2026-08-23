# Correspondance — « 10-Skill SEO Engine » ↔ suite RUSHITI

> Le playbook générique propose d'installer 11 skills. **Dix de ses onze
> rôles sont déjà tenus** par des agents RUSHITI en place, plus spécialisés,
> déjà bridés sur les données réelles de l'entreprise (NAP, zone, DTU,
> offre confirmée, interdits Google).
>
> Installer les skills génériques par-dessus ne comblerait aucun manque : ça
> créerait des doublons qui se contrediraient sur les prix, la zone et les
> normes — et un agent qui invente un prix coûte plus cher qu'un agent
> absent.

## Le tableau de correspondance

| Rôle du playbook | Agent RUSHITI | Écart de périmètre à connaître |
|---|---|---|
| `/seo-onboard` — le conducteur | **`rushiti-seo-engine`** (ce skill) + socle `rushiti-defaults.md` | Le playbook fait un entretien une fois puis écrit un `seo-brief.md`. Chez RUSHITI le socle **existe déjà** et est versionné : le moteur le lit, il ne réinterroge pas Isuf sur son propre SIRET |
| `/keyword-map` | `rushiti-keyword-map` (+ `rushiti-keyword-clusters`) | Le playbook **propose** des pages. L'agent RUSHITI **garde une porte** : quatre contrôles anti-cannibalisation, verdict écrit, registre CSV canonique. Beaucoup plus strict, et c'est voulu |
| `/serp-scan` | `rushiti-ecart-concurrentiel` | Équivalent proche. L'agent RUSHITI nomme les confrères bisontins sans rien écrire de dépréciatif |
| `/content-brief` | `rushiti-brief-seo` | Équivalent |
| `/onpage-audit` | `rushiti-audit-seo` (+ `rushiti-audit-technique`, `rushiti-crawl-audit`) | RUSHITI sépare on-page, technique et crawl en trois agents. Le playbook les mélange |
| `/citation-gap` | `rushiti-citation-ia` (+ `rushiti-part-de-voix-ia`) | **RUSHITI est nettement plus avancé ici.** Le playbook mesure « cité / pas cité ». RUSHITI distingue cinq surfaces (`S` source, `M` mention, `F` reprise de fait, `Ø` absence, `NM` non mesuré) et relève **les URL citées**, ce qui seul permet un plan d'entrée |
| `/geo-writer` | `rushiti-architecte-seo`, `rushiti-page-service`, `rushiti-page-locale` | RUSHITI a trois rédacteurs selon le type de page. Un rédacteur unique produirait des pages piliers et des pages communes interchangeables — l'erreur qui a coûté la consolidation 644 → 301 |
| `/schema-smith` | `schema-builder` | Équivalent, avec les interdits Google déjà câblés (pas de `Review` ni d'`aggregateRating` auto-déclarés) |
| `/internal-linker` | `rushiti-maillage-interne` (+ `orphan-finder`) | Équivalent |
| `/rank-tracker` | `rushiti-gsc` + `rushiti-part-de-voix-ia` | Le playbook fusionne les deux tableaux dans un seul. RUSHITI les tient **séparés, à cadences différentes** — voir plus bas |
| `/content-refresh` | `rushiti-refresh-planner` (+ `rushiti-regression-seo`) | Équivalent |

## Ce que RUSHITI a en plus, et que le playbook ignore

Le playbook est écrit pour un éditeur de logiciel qui vend en ligne. RUSHITI
est un artisan du bâtiment qui vend un chantier à Besançon. D'où une moitié
de suite qui n'a aucun équivalent générique — et qui pèse souvent plus lourd
sur le chiffre d'affaires que le blog :

| Agent RUSHITI | Ce qu'il couvre | Pourquoi ça n'existe pas dans le playbook |
|---|---|---|
| `rushiti-fiche-google-business`, `rushiti-avis-google`, `rushiti-seo-local` | Fiche d'établissement, avis, cohérence NAP par annuaire | Pour un artisan, le pack local capte le clic **avant** l'organique. C'est le premier levier, pas le dernier |
| `rushiti-devis-assurance` | Devis dégât des eaux au format IRSI que les experts valident | Métier. Aucun playbook SEO ne sait ce qu'est une unité d'œuvre |
| `rushiti-memo-chantier`, `rushiti-declinaison-chantier`, `rushiti-etudes-de-cas` | Transformer un chantier réel en matière éditoriale | **La seule source de contenu qu'un concurrent ne peut pas copier** — et celle que les moteurs de réponse récompensent (expérience vécue, E-E-A-T) |
| `rushiti-prospection-b2b`, `rushiti-relance-b2b`, `rushiti-courriers-clients` | Syndics, gestionnaires, experts d'assurance | Le B2B se gagne par courrier, pas par SERP |
| `rushiti-indexation`, `rushiti-regression-seo`, `rushiti-cannibal-check` | Hygiène d'un site de 300 URL avec un héritage WordPress | Le playbook suppose un site neuf et propre |
| `rushiti-google-trends` | Saisonnalité — **quand** publier | Le ravalement et la peinture extérieure ont des pics. Publier six à huit semaines trop tard coûte la saison |
| `rushiti-visibilite-ia` | robots.txt, crawlers IA, extractibilité, E-E-A-T | Le playbook parle de citation sans jamais vérifier que les moteurs **peuvent lire** le site |

## Les trois idées du playbook : ce qui tient, ce qui se corrige

**Idée 1 — « Possédez le sujet, pas le mot-clé. »** ✅ Tient, et c'est déjà
appliqué : six silos, pages piliers, grille locale, satellites de blog.
⚠️ **Mais la conclusion opérationnelle est inversée ici.** Le playbook dit
« un pilier + 6 à 15 pages par sujet ». RUSHITI a **déjà** dépassé ce volume
et vient de réduire la grille de 644 à 301 pages parce que le trop-plein se
cannibalisait. Appliquer la recette telle quelle défait un travail payé.

**Idée 2 — « Les IA citent les pages qui répondent vite et clairement. »**
✅ Tient entièrement. C'est le cœur de la phase 4 du protocole, et RUSHITI y
ajoute ce que le playbook n'a pas : **le cas `F`** — le moteur reprend le
fait et laisse le nom. Corriger ça, c'est rattacher l'entité à la phrase,
pas écrire plus.

**Idée 3 — « Regardez les deux tableaux de bord. »** ✅ Tient. ⚠️ Avec une
correction : le playbook les met dans un même tableau, ligne par mot-clé.
Les deux portes n'ont ni le même dénominateur ni la même vitesse — Google se
relit en 4 à 6 semaines, le corpus des moteurs de réponse bouge en 6 à 8.
Un tableau unique fait lire un mouvement Google comme un mouvement IA. On les
tient **côte à côte, datés séparément**.

## Règle d'installation

**Ne jamais installer un skill générique dont le rôle est déjà tenu.**

Si un manque réel apparaît — un rôle qu'aucun agent RUSHITI ne couvre — il se
comble par `rushiti-agent-creator`, qui produit un agent aux normes de la
maison : français, vouvoiement, ancrage Besançon-Doubs, données entreprise
auto-remplies, garde-fous intégrés. Un skill générique importé tel quel
arrive sans aucun de ces verrous, et c'est précisément là que naissent les
prix inventés et les zones fantaisistes.

## Les prompts du playbook, réécrits pour RUSHITI

Les prompts copier-coller du playbook (`/keyword-map — build a topical map
for [yoursite.com]…`) sont inutilisables tels quels : ils ne portent ni le
NAP, ni la zone validée, ni les interdits. Le prompt maître bridé, prêt à
coller dans un outil IA **hors dépôt** (ChatGPT, Gemini, un consultant), est
maintenu ici :

`docs/seo/prompts/prompt-maitre-moteur-seo.md`

Dans Claude Code, on n'en a pas besoin : on invoque `rushiti-seo-engine`,
qui lit le registre, le sitemap et les rapports tout seul.
