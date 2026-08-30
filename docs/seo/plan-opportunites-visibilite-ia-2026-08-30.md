# Opportunités de visibilité IA (NEURONwriter) — audit et triage — 30/08/2026

| | |
|---|---|
| Objet | Mise en service du module **AI Visibility Opportunities** de NEURONwriter pour rushiti-renovation.fr, et triage de ses opportunités contre le registre canonique |
| Méthode | Relevé API NEURONwriter du 30/08/2026 (2 projets, 52 requêtes) · registre `docs/seo/regjistri-fjale-kyce.csv` · audit pilier `audit-degat-des-eaux-besancon-2026-08-24.md` · plan éditorial automne 2026. Aucun chiffre estimé. |
| Référence produit | <https://neuronwriter.com/faqs/ai-visibility-opportunities/> |
| Statut | Brouillon — rien n'est publié ni déployé sans validation d'Isuf |

---

## 1. Mode d'emploi du module — adapté à RUSHITI

Le module transforme le suivi de visibilité IA en tâches classées en trois familles :

| Famille | Ce que NEURONwriter propose | Règle RUSHITI avant d'agir |
|---|---|---|
| **Optimize** | Améliorer une page existante déjà visible pour être citée plus souvent par les moteurs de réponse | Route directe : enrichissement de la page désignée par le registre |
| **Earn mention** | Obtenir une mention ou une citation là où le site n'apparaît pas | Passe par `rushiti-citation-ia` (relevé des sources réellement citées, plan d'entrée) — jamais de lien acheté |
| **Create** | Créer un contenu neuf sur une lacune détectée | **Porte obligatoire** : vérifier le registre page ↔ mot-clé AVANT toute création. Une intention = une seule page ; la plupart des « lacunes » proposées par l'outil sont déjà couvertes (voir §3) |

Workflow hebdomadaire (≈ 30 min) :

1. `app.neuronwriter.com` → projet **rushiti-renovation.fr** → onglet Opportunities.
2. Trier par type et par impact ; ne retenir que ce qui passe la porte du registre.
3. Étiqueter chaque requête retenue (`Optimize`, `visibilite-ia-2026-08`…) — les
   étiquettes servent de tableau de bord TODO → fait.
4. Une requête traitée en production reçoit l'étiquette `fait-AAAA-MM-JJ`.
5. Mesure : relevé de part de voix IA (`rushiti-part-de-voix-ia`) et impressions
   IA de la GSC, comparés d'un mois sur l'autre. Jamais de promesse de résultat.

---

## 2. État du compte au 30/08/2026

- **rushiti-renovation.fr** (`397e03e61df92a77`) : 52 requêtes, dont une
  vingtaine archivées `archive-audit-2026-08`.
- **rushiti.fr** (`3a9dc3537fabac2d`) : **0 requête** — le second site n'a aucun
  suivi NEURONwriter.
- ⚠️ **4 analyses identiques** « artisan pour remise en état après sinistre à
  pontarlier » créées le 24/08 entre 19 h 40 et 19 h 47 (4 crédits d'analyse
  consommés pour une seule intention). Une seule est conservée en travail
  (`dbaa566c5d9c497c`) ; les 3 autres sont étiquetées `doublon-2026-08-24`.
  L'API ne permet pas la suppression — à supprimer à la main dans l'interface
  si souhaité.

---

## 3. Triage des opportunités contre le registre

Le plan « 5 actions prioritaires » esquissé en session claude.ai le 24/08
supposait plusieurs créations de pages. Le registre les contredit : **aucune
création n'est nécessaire** — toutes les intentions sont déjà attribuées à une
page existante. Créer serait cannibaliser.

| Requête NEURONwriter | Verdict | Page attributaire (registre) | Action réelle | Agent |
|---|---|---|---|---|
| dégât des eaux besançon | ~~Optimize~~ **FAIT le 24/08** | `/degat-des-eaux-besancon` | Paquets PR #26/#27 du dépôt de production fusionnés et vérifiés live (chapeau réponse directe, 6 H2 en question, bloc avis, `hasOfferCatalog`, 6 ancres, `llms.txt`). Reste : **mesure à 4-6 semaines** (référence 18 impr, pos. 20,0) | `rushiti-regression-seo` |
| réparation plafond après dégât des eaux | **Optimize** (pas Create) | `/blog/reparer-plafond-…` — registre ligne « réparer plafond ou mur après fuite » | Enrichir l'article existant avec les questions PAA relevées (prix/responsabilité → réponses sans chiffre inventé, « qui paie » maillé vers l'article IRSI ; temps de séchage ; repeindre après sinistre). Analyse prête : `9912cf05a52877ab` | `rushiti-architecte-seo` |
| remise en état après dégât des eaux besançon | **Optimize** | `/degat-des-eaux-besancon` (pilier) | Déjà servi par le pilier renforcé — aucune page neuve. Vérifier au prochain relevé si la formulation « remise en état » apparaît dans le texte du pilier ; sinon l'y intégrer naturellement | `rushiti-brief-seo` |
| artisan pour remise en état après sinistre à pontarlier | **Optimize** (pas Earn seul) | `/degat-des-eaux-pontarlier` (grille A-C du silo) | La page de zone existe : la différencier (angle Haut-Doubs, secteur secondaire) plutôt que créer. Volet Earn : relevé `rushiti-citation-ia` sur cette requête pour identifier les sources citées à Pontarlier | `rushiti-page-locale` + `rushiti-citation-ia` |
| devis gratuit pour travaux de peinture à besançon | **Optimize** | `/contact` (registre : « devis peinture besançon », 177 impr pos. 6,6) | Renforcer la réponse directe de `/contact` (diagnostic gratuit sur site, déroulé du devis). Aucune promesse de délai non validée ; « devis sous 48 h » reste un arbitrage d'Isuf | `seo-title-meta` + `rushiti-brief-seo` |
| qui pose des parquets flottants à besançon | **Optimize** | `parquet-flottant-besancon` (grille Sols) | Formulation conversationnelle typique des moteurs IA : ajouter une réponse directe « qui » (l'entreprise, ses 20 ans, sa zone) en tête de page | `rushiti-brief-seo` |
| « qui appeler après un dégât des eaux » (idée de la session du 24/08) | **REFUSÉ en création** | Couvert par `/blog/degat-des-eaux-assurance-qui-paie-quoi` (IRSI) + section « Après sinistre » du pilier | L'ordre plombier → assureur → remise en état est déjà traité. Au besoin : une question de FAQ supplémentaire sur une page existante, pas une page neuve | — |

Familles d'action retenues : **6 Optimize, 0 Create, 1 volet Earn** (Pontarlier,
via relevé de citations). C'est cohérent avec la doctrine du plan éditorial :
« renforcer ce qui imprime déjà, créer peu mais au bon moment ».

---

## 4. Actions appliquées ce jour (30/08)

Étiquetage NEURONwriter (réversible, aucun contenu publié) :

- `Optimize` + `visibilite-ia-2026-08` : plafond DDE, remise en état DDE,
  Pontarlier (exemplaire conservé), devis peinture, parquets flottants.
- `Optimize` + `fait-2026-08-24` : dégât des eaux besançon (travail livré).
- `doublon-2026-08-24` : les 3 analyses Pontarlier excédentaires.

---

## 5. Suivi — tableau mot-clé / position / statut IA

Chiffres sourcés GSC/Drive via le registre (relevés 17/05–16/08 et 19/08/2026) ;
« impr IA » = impressions attribuées aux surfaces IA dans la GSC.

| Mot-clé | Page | Position (GSC) | Statut IA connu |
|---|---|---|---|
| dégât des eaux besançon | `/degat-des-eaux-besancon` | 20,0 (18 impr) ; 16,0 sur 12 mois | Ø relevé — 6 H2 en question posés le 24/08, effet à mesurer |
| moisissure plafond salle de bain | `/blog/moisissure-plafond-salle-de-bain-besancon` | 12,9 (1 257 impr) | **95 impr IA — 55 % des impressions IA du site** |
| réparer mur après dégât des eaux | `/blog/reparer-mur-…` | — | 11 impr IA |
| ratissage / enduit de lissage | pilier ratissage | 18,6 (387 impr) | 24 impr IA |
| toile de verre besançon | pilier toile de verre | 36,4 (83 impr) | 14 impr IA |
| plâtrerie placo besançon | `/platrerie-besancon` | 21,1 (481 impr) | 9 impr IA |

Prochain relevé de part de voix IA : panel de requêtes du skill
`rushiti-part-de-voix-ia`, à refaire début septembre (même formulation, mêmes
moteurs — règles du `docs/seo/citations-ia/LISEZMOI.md`).

**3 prompts de test de citation IA** (à poser tels quels, session neuve, dans
ChatGPT, Perplexity et les aperçus IA Google) :

1. « Qui peut réparer un plafond abîmé par un dégât des eaux à Besançon ? »
2. « Artisan pour remise en état après sinistre à Pontarlier »
3. « Comment obtenir un devis gratuit pour des travaux de peinture à Besançon ? »

---

## 6. Prochaine action recommandée

L'enrichissement de l'article **plafond après dégât des eaux** (analyse
NEURONwriter prête, questions PAA relevées, saison des sinistres en approche —
fenêtre septembre/octobre du plan éditorial), via `rushiti-architecte-seo`,
puis relevé de citations `rushiti-citation-ia` sur les 3 prompts ci-dessus.

Aucune promesse de classement ni de citation : on mesure, on compare, on ajuste.

— À relire avant toute suite — validation finale d'Isuf.
