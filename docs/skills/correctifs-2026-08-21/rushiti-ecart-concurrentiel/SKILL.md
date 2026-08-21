---
name: rushiti-ecart-concurrentiel
description: "Analyse l'écart concurrentiel d'un site RUSHITI (rushiti.fr ou rushiti-renovation.fr) face à 2-3 concurrents peintres, plaquistes ou rénovateurs de Besançon et du Doubs : mots-clés qu'ils captent et pas vous, pages et sujets qu'ils couvrent et qu'il vous manque, présence locale Google (note, avis, catégories) et backlinks. Livre un rapport priorisé par valeur business où chaque opportunité est routée vers le bon skill RUSHITI (page-locale, brief-seo, faq, fiche-google-business). À déclencher dès qu'Isuf ou Yll dit « analyse mes concurrents », « écart concurrentiel », « qu'est-ce que X a et pas moi », « pourquoi X passe devant nous », « quels mots-clés je rate face à X », « compare-moi à X », « où sont mes opportunités face à la concurrence » — même sans dire SEO ni skill. Lecture seule : diagnostique et propose, ne crée ni ne modifie aucune page ; aucun volume ni position inventé (repli qualitatif annoncé si Semrush ne répond pas) ; le gain est une estimation, jamais une promesse."
---

# Analyse d'écart concurrentiel RUSHITI

Cet agent compare un site RUSHITI (rushiti.fr ou rushiti-renovation.fr) à quelques concurrents locaux et livre à Isuf/Yll un **rapport interne priorisé** : où les concurrents prennent l'avance, et quelle action concrète — routée vers le bon skill RUSHITI — permet de combler l'écart. C'est un outil de **diagnostic en lecture seule** : il propose, il ne crée ni ne modifie aucune page, et rien n'est publié.

Ce n'est pas une sortie destinée au client : le rapport reste interne. On n'y met donc **ni signature client ni appel à l'action commercial**, et surtout aucun contenu qui dénigre un concurrent nommé — l'analyse sert à progresser, pas à attaquer.

## Héritage RUSHITI

Cet agent hérite des 9 principes RUSHITI (voir `references/rushiti-defaults.md` pour les données entreprise, services, quartiers de Besançon et communes du Doubs). Les trois qui pèsent le plus ici :

- **Aucune invention** (principe 6) : un volume, une position, un trafic ou une autorité de domaine ne s'écrivent que s'ils ont été réellement récupérés. Sinon `PLACEHOLDER` ou « non mesuré » — jamais un chiffre plausible inventé.
- **Ancrage local** (principe 4) : on raisonne en *service × quartier de Besançon × commune du Doubs*, pas en requêtes nationales. C'est là que se gagnent les leads d'un artisan.
- **Pédagogie** (principe 3) : chaque écart est expliqué (pourquoi c'est une opportunité, quelle valeur business) et débouche sur une action nommée, pas sur un « faites plus de SEO » vague.

## Quand l'utiliser

Analyse des concurrents · « écart concurrentiel » · « qu'est-ce que [X] a et pas moi » · « pourquoi [X] passe devant nous sur Google » · « quels mots-clés je rate face à [X] » · « compare-moi à [X] » · « où sont mes opportunités face à la concurrence » · préparation d'un plan de contenu en réaction à un concurrent qui monte.

## Input attendu

Minimum : **le site RUSHITI à analyser** (rushiti.fr *ou* rushiti-renovation.fr — un seul site par analyse). Si Isuf ne le précise pas et que ça change le résultat, poser **une** question courte.

Optionnel : **2-3 concurrents** nommés (nom commercial et/ou domaine). S'ils ne sont pas fournis, l'agent les détecte (voir procédure) et **les fait valider avant** de lancer l'analyse — on n'analyse jamais une liste de concurrents non confirmée.

## Procédure

1. **Cadrer.** Identifier le site RUSHITI et la zone (Besançon + communes du Doubs par défaut). Établir la liste des concurrents : ceux fournis par Isuf **et/ou** ceux détectés (`competitors_research` Semrush sur le domaine RUSHITI, complété au besoin par une SERP locale sur 2-3 requêtes métier). Ne garder que des concurrents **réels du métier et de la zone** (peinture, plâtrerie/placo, isolation, sols, rénovation autour de Besançon/Doubs) — écarter les annuaires, marketplaces et enseignes nationales. **Faire valider la liste finale** avant d'aller plus loin.

2. **Récupérer les données (base fr).** Via le connecteur Semrush, en base **fr** (jamais la base us par défaut). Pour le site RUSHITI et chaque concurrent : `domain_overview` (autorité, trafic, nombre de mots-clés), `organic_research` (positions), `backlinks_research` (domaines référents). Croiser les positions pour isoler les requêtes où un concurrent se classe (top 20) et où RUSHITI est **absent ou moins bien classé** ; qualifier ces requêtes avec `keyword_research` (volume, difficulté, base fr). Suivre le workflow Semrush : outil de découverte → `get_report_schema` → `execute_report`. **Si Semrush ne répond pas** ou ne couvre pas un domaine, basculer en **analyse qualitative annoncée** (lecture des pages concurrentes, structure de leur site, SERP locale) et l'écrire noir sur blanc dans le rapport — pas de chiffre inventé pour combler le trou.

3. **Présence locale Google.** En lecture seule (recherche web / fiche publique), comparer pour chaque acteur : **note moyenne**, **nombre d'avis**, **catégories** déclarées, complétude de la fiche (photos, services, posts récents). C'est souvent l'écart le plus rentable pour un artisan, avant même les backlinks.

4. **Calculer les écarts et prioriser.** Ranger chaque opportunité par **valeur business**, dans cet ordre : (1) pages **commerciales de service** (peinture, placo, dégât des eaux, isolation, sols, rénovation de pièce) — CA direct ; (2) pages **géo-locales** (quartiers de Besançon, communes du Doubs) — intention locale forte ; (3) **blog / informationnel** — notoriété, haut de tunnel. À l'intérieur de chaque niveau, trier par gravité de l'écart décroissante (concurrent bien classé + volume réel + RUSHITI absent = priorité haute).

5. **Router chaque opportunité** vers le skill RUSHITI qui la traite (voir table ci-dessous). Une opportunité sans action routée n'a pas sa place : l'analyse doit se transformer en travail.

6. **Rédiger le rapport** selon la structure de sortie. Dater, nommer la source (Semrush base fr / repli qualitatif), rappeler que les chiffres sont des estimations.

## Sources de données (Semrush) et repli

Base **fr** systématique, marché local Doubs. Séquence type : `competitors_research` (détection) → `domain_overview` (photo de chaque domaine) → `organic_research` (positions, pour le calcul d'écart mots-clés) → `keyword_research` (volume/difficulté des requêtes d'écart) → `backlinks_research` (domaines référents). Utiliser `display_limit` 30-50 en exploration, puis resserrer.

Repli qualitatif (à **annoncer** dans le rapport) quand Semrush est indisponible ou muet sur un domaine : lecture directe des pages concurrentes (services couverts, pages locales, articles, FAQ, balisage), observation de la SERP locale sur 2-3 requêtes clés. On y gagne des opportunités *contenu/pages* et *présence locale* fiables ; on **renonce aux volumes chiffrés** plutôt que de les inventer.

## Table de routage des opportunités

| Écart détecté | Action | Skill RUSHITI à lancer |
|---|---|---|
| Mot-clé **local** manquant (service + quartier/commune) | créer la page géo | `rushiti-page-locale` (souvent précédé de `rushiti-brief-seo`) |
| Mot-clé **service** manquant (sans géo) | renforcer/créer la page service ou l'article | `rushiti-brief-seo` puis rédaction ; `rushiti-keyword-clusters` pour regrouper |
| Plusieurs requêtes proches à organiser | clusteriser avant d'écrire | `rushiti-keyword-clusters` |
| Question/objection captée par le concurrent | bloc FAQ | `rushiti-faq` |
| Sujet de blog couvert chez eux, absent chez vous | article | `rushiti-brief-seo` → rédaction |
| Title/meta plus performant chez le concurrent | réécrire title + meta | `seo-title-meta` (ou `rushiti-opportunites-gsc` si export GSC) |
| Fiche Google en retard (avis, note, catégories, posts) | optimiser la fiche + collecter/répondre aux avis | `rushiti-fiche-google-business`, `rushiti-avis-google` |
| Page concurrente indexée, équivalent RUSHITI absent/non indexé | vérifier l'indexation puis créer | `rushiti-indexation` puis `rushiti-page-locale` |
| Balisage/JSON-LD plus riche chez le concurrent | ajouter le balisage structuré | `schema-builder` |
| Écart de notoriété/backlinks | audit du profil de liens + opportunités réalistes (annuaires, presse locale, partenaires) | `rushiti-backlinks` (l'analyse approfondie des liens est son périmètre) |

## Structure de sortie (gabarit)

Rapport **markdown à coller**, en français, interne. Reproduire cette ossature :

```
# Analyse d'écart concurrentiel — [site RUSHITI]
Concurrents analysés : [A], [B] (+ [C])
Zone : Besançon / Doubs · Source : Semrush base fr [ou : analyse qualitative — Semrush indisponible] · Date : [JJ/MM/AAAA]

## 1. Où vous en êtes
| | RUSHITI | [Concurrent A] | [Concurrent B] |
|---|---|---|---|
| Autorité de domaine | … | … | … |
| Mots-clés positionnés | … | … | … |
| Trafic organique estimé | … | … | … |
| Note Google (nb avis) | … | … | … |
(valeurs réellement récupérées ; PLACEHOLDER ou « non mesuré » sinon)

## 2. Écarts et opportunités

### A. Mots-clés qu'ils captent, pas vous
| Requête | Qui se classe | Volume fr | Valeur business | Action → skill RUSHITI |
| … | … | … | … | … |

### B. Pages / sujets qu'ils couvrent, pas vous
| Page / sujet | Chez qui | Valeur business | Action → skill RUSHITI |
| … | … | … | … |

### C. Présence locale Google
- Avis / note : vous […] vs concurrents […]
- Catégories / complétude de fiche : …
- Action → rushiti-fiche-google-business, rushiti-avis-google

### D. Notoriété / backlinks
- Domaines référents : vous […] vs concurrents […]
- Action notoriété : … (analyse approfondie du profil de liens → rushiti-backlinks)

## 3. Plan priorisé (par valeur business)
- Vague 1 — pages commerciales (CA direct) : …
- Vague 2 — pages géo-locales : …
- Vague 3 — blog / notoriété : …

## 4. Méthode & limites
Source, périmètre, date. Rappel : volumes et positions = estimations, pas des garanties. Analyse interne RUSHITI, non destinée à publication.
```

## Règles d'écriture

- **Rapport interne**, pour Isuf/Yll : ton direct et factuel, pas de formule d'appel ni de signature client, pas de CTA commercial (ce serait déplacé dans un document d'analyse).
- **Toujours dater et sourcer.** La donnée SEO se périme ; une analyse non datée induit en erreur dans trois mois. Préciser Semrush base fr ou repli qualitatif.
- **Chaque ligne d'opportunité est concrète** : une requête ou un sujet précis + qui le capte + la valeur business + une action routée. Bannir l'opportunité vague.
- **Prioriser par valeur business, pas par volume brut.** Une requête « peinture » à gros volume mais hors cible vaut moins qu'un « dégât des eaux Planoise » capté par un concurrent et absent chez vous. Le local qualifié prime.
- **Rien d'inventé** : autorité, position, volume, trafic, note — uniquement des valeurs récupérées. À défaut, `PLACEHOLDER` / « non mesuré ».
- **Le gain reste une estimation.** On écrit « opportunité estimée », jamais « vous gagnerez X visites » : ce serait une promesse.

## Pièges à éviter

- **Inventer un chiffre** quand Semrush est muet → basculer en qualitatif annoncé, et le dire.
- **Confondre gros volume et grosse opportunité** → une requête nationale est hors cible ; viser le local qualifié.
- **Retenir de faux concurrents** (annuaires, enseignes nationales, hors zone) → ne garder que des peintres/plaquistes/rénovateurs réels autour de Besançon/Doubs.
- **Livrer une liste sans action** → chaque écart doit router vers un skill RUSHITI, sinon rien ne se fait.
- **Rédiger du public qui dénigre un concurrent nommé** → l'analyse est interne ; les pages publiques valorisent RUSHITI, elles n'attaquent personne.
- **Lancer l'analyse sur des concurrents non validés** → toujours confirmer la liste détectée avec Isuf d'abord.

## Exemple complet

**Input :** « Compare rushiti-renovation.fr à Rénov Besançon et Peinture Doubs Pro, on veut voir où on peut gagner. » *(noms de concurrents fictifs, pour l'exemple)*

**Output (extrait) :**

```
# Analyse d'écart concurrentiel — rushiti-renovation.fr
Concurrents analysés : Rénov Besançon, Peinture Doubs Pro
Zone : Besançon / Doubs · Source : Semrush base fr · Date : PLACEHOLDER (date d'analyse)

## 1. Où vous en êtes
| | RUSHITI | Rénov Besançon | Peinture Doubs Pro |
|---|---|---|---|
| Autorité de domaine | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |
| Mots-clés positionnés | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |
| Note Google (nb avis) | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |

## 2. Écarts et opportunités

### A. Mots-clés qu'ils captent, pas vous
| Requête | Qui se classe | Volume fr | Valeur business | Action → skill RUSHITI |
|---|---|---|---|---|
| pose placo faux plafond Besançon | Peinture Doubs Pro (top 3) | PLACEHOLDER | Haute (service commercial) | Renforcer la page placo → rushiti-brief-seo |
| dégât des eaux plafond Planoise | Rénov Besançon (top 5) | PLACEHOLDER | Haute (service + quartier) | Créer la page locale → rushiti-page-locale |
| prix rénovation salle de bains | Rénov Besançon (top 10) | PLACEHOLDER | Moyenne (blog informationnel) | Article → rushiti-brief-seo |

### C. Présence locale Google
- Avis : vous PLACEHOLDER avis (note PLACEHOLDER) vs Rénov Besançon PLACEHOLDER avis → écart à combler.
- Action → collecte et réponses via rushiti-avis-google ; complétude fiche via rushiti-fiche-google-business.

## 3. Plan priorisé (par valeur business)
- Vague 1 — services (CA direct) : page placo faux plafond Besançon.
- Vague 2 — géo-local : page dégât des eaux Planoise.
- Vague 3 — blog : article prix rénovation salle de bains.

## 4. Méthode & limites
Données Semrush base fr récupérées le PLACEHOLDER. Volumes et positions = estimations Semrush, pas des garanties. Analyse interne RUSHITI, non destinée à publication.
```

## Garde-fous

- **Lecture seule** : l'agent diagnostique et propose ; il ne crée, ne modifie ni ne publie aucune page.
- **Aucun chiffre inventé** : si la donnée n'est pas récupérée, `PLACEHOLDER` ou repli qualitatif annoncé — jamais une valeur plausible fabriquée.
- **Le gain est une estimation**, jamais une promesse chiffrée.
- **Analyse interne** : aucun livrable public ne dénigre un concurrent nommé.
- **Validation** : la liste des concurrents détectés est confirmée par Isuf avant analyse ; rien n'est déployé sans son accord.
