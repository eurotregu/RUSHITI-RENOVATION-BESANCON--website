# Arbitrage — « une page dédiée par service » (plan du 22/08/2026)

> Réponse au plan proposant de créer `/peinture`, `/placo`, `/isolation`,
> `/carrelage`, `/renovation-complete`.
> **Verdict : le principe est déjà appliqué ; les URL proposées ne doivent
> pas être créées.** Ce qui reste à faire est un travail de renforcement,
> pas de création.
>
> Relevés du 22/08/2026 : sitemap de rushiti-renovation.fr (~300 URL) et
> code source de `/peinture-interieure-besancon`. Registre de référence :
> `docs/seo/regjistri-fjale-kyce.csv`.

## 1. Ce que le plan supposait, et ce qui est vrai

| Hypothèse du plan | État réel au 22/08/2026 |
|---|---|
| « Tous les services sont listés sur une seule page » | Faux pour la production : une page pilier existe par prestation (`/peinture-interieure-besancon`, `/peinture-exterieure-besancon`, `/plaquiste-besancon`, `/platrerie-besancon`, `/cloisons-besancon`, `/faux-plafonds-besancon`, `/doublage-murs-besancon`, `/isolation-besancon`, `/isolation-interieure-besancon`, `/revetements-sol-besancon` et ses déclinaisons, `/degat-des-eaux-besancon`…), plus une grille locale par commune et quartier |
| « Créer /peinture, /placo, /isolation… » | Ces URL doubleraient des pages qui récoltent déjà des impressions : signal divisé, aucune des deux ne gagne |
| « /carrelage si le service est proposé » | Prestation **non confirmée** dans l'offre. La page d'accueil héritée mentionne « Carrelage & Sol », aucune page ni arbitrage ne l'accompagne → décision d'Isuf requise avant toute page |
| « /renovation-complete » | Couvert par `/entreprise-renovation-besancon` et `/renovation-appartement-besancon` |
| Volumes de recherche cités (« peintre à Besançon ~720/mois ») | Non sourcés. Les seules données exploitables sont celles de la Search Console, déjà consignées dans le registre |
| Zone « Montbéliard, Vesoul, Dijon, rayon 50 km » | Hors périmètre validé : la zone s'arrête au Doubs (25) |

Le seul élément du plan qui reste applicable tel quel : l'**anatomie de page**
(H1 local, contenu long, FAQ, données structurées, CTA, maillage) — c'est
elle qui a été formalisée en doctrine.

## 2. Ce qui a été livré

- **Skill `rushiti-page-service`** (`.claude/skills/rushiti-page-service/`) :
  fabrique et met à niveau les pages pilier service × Besançon. Trois modes
  (mise à niveau, création sous porte `rushiti-keyword-map`, contrôle avant
  déploiement), quatre livrables, anatomie en 12 blocs, checklist de
  40 points, plan de mesure.
- **Prompt maître**
  (`docs/seo/prompts/prompt-maitre-page-service-dediee.md`) : version bridée
  du prompt, pour les outils IA hors dépôt.

## 3. Défauts constatés sur la page pilier la plus stratégique

Relevé du 22/08/2026 sur `/peinture-interieure-besancon` — page qui porte
« peintre à Besançon » et « entreprise de peinture à Besançon » :

| Constat | Effet | Priorité |
|---|---|---|
| JSON-LD limité à `WebSite` + `LocalBusiness` : ni `Service`, ni `BreadcrumbList`, ni `FAQPage` alors que **11 questions** sont visibles dans la page | Le balisage le plus rentable du site est absent, sur la page la plus lue | P1 |
| Deux formulations de title/description coexistent selon la lecture (`Peinture intérieure à Besançon - RUSHITI Rénovation` d'un côté, `Peintre à Besançon — peinture intérieure, devis sous 48 h` de l'autre) | À vérifier dans le code source : une balise en double ou injectée fait lire la mauvaise à Google | P1 |
| « devis sous 48 h » affiché dans la description | Promesse de délai : à confirmer par Isuf, ou à retirer | P2 |
| ~1270 mots, structure conforme, bloc « ce qui fait le prix » présent | Base saine : la page est à renforcer, pas à refaire | — |

À contrôler dans le même passage sur les autres piliers, en commençant par
`/degat-des-eaux-besancon` (silo le plus rentable et le plus enfoui d'après
le registre) et `/plaquiste-besancon`.

## 4. Ordre de travail proposé

1. **Corriger les données structurées des piliers** — `Service` +
   `BreadcrumbList` + `FAQPage` là où une FAQ est visible. Aucun `Review` ni
   `aggregateRating`. *(`schema-builder`, puis contrôle
   `rushiti-page-service` mode 3.)*
2. **Vérifier l'unicité des balises title/description** sur les piliers, dans
   le code source. *(`rushiti-audit-technique`.)*
3. **Renforcer `/degat-des-eaux-besancon`** : silo le plus rentable, le plus
   invisible. *(`rushiti-page-service` mode 1 + `rushiti-maillage-interne`.)*
4. **Arbitrer le carrelage** : prestation proposée ou non ? Tant que la
   réponse n'est pas donnée, aucune page.
5. **Décider des URL courtes** : si elles sont souhaitées pour la
   communication, uniquement en **301 vers la page existante** — jamais en
   seconde page.
6. **Mesurer à 4-6 semaines** : requête cible × page dans la Search Console,
   puis `rushiti-regression-seo`.

## 5. Ce qui n'a pas été fait, et pourquoi

- Aucune page n'a été créée ni modifiée en production : le dépôt de
  production est distinct, et rien ne se déploie sans validation d'Isuf.
- Aucun volume de recherche n'a été repris du plan d'origine : ils n'étaient
  pas sourcés.
- Le carrelage n'a reçu ni page ni brief : la prestation n'est pas confirmée.
