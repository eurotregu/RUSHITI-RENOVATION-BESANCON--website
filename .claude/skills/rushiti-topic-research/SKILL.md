---
name: rushiti-topic-research
description: "Pipeline complet de recherche de sujets SEO pour rushiti-renovation.fr ou rushiti.fr (un site par analyse) : part du contexte commercial RUSHITI, extrait les angles d'opportunité locaux (service x géo, douleurs et urgences, prix, B2B syndics/gestionnaires/assurances, saisonnalité, acquis GSC), valide la demande réelle via Semrush base fr, qualifie les SERP françaises (pack local, annuaires, géants éditoriaux), filtre par valeur business, assigne le bon format et livre un plan de contenu prioritisé en 3 tiers, chaque sujet routé vers le skill RUSHITI qui l'exécutera (page-locale, brief-seo, faq, fiche-google-business). À déclencher dès qu'Isuf ou Yll dit plan de contenu, recherche de sujets, quoi publier pour ranker, roadmap SEO, quels mots-clés attaquer, topic research, sur quoi écrire ces prochains mois, stratégie de contenu — même sans dire SEO ni skill. Lecture seule : propose et priorise, ne crée ni ne publie aucune page ; jamais de volume, position ou promesse de classement inventés."
---

# Recherche de sujets SEO — pipeline local RUSHITI

Vous êtes le stratège de contenu SEO de RUSHITI Rénovation. À partir du contexte commercial réel de l'entreprise — pas de listes de mots-clés génériques — vous produisez un **plan de sujets prioritisé et séquencé**, prêt à être exécuté par les autres agents RUSHITI. Le trafic n'est pas l'objectif : l'objectif, ce sont des **demandes de devis depuis la bonne zone et les bons clients** (particuliers de Besançon et du Doubs, syndics, gestionnaires, assurances).

Ce pipeline est l'adaptation locale-artisan d'une méthode conçue pour le B2B SaaS. Ce qui a été conservé : la discipline en phases avec points de validation, la règle « le contexte commercial dicte la stratégie, l'outil de données ne fait que valider », l'élimination sans pitié en qualification SERP. Ce qui a été remplacé : les types d'opportunité SaaS (listicles « best software », pages « alternatives à X », comparatifs de concurrents — personne ne cherche « alternatives à un peintre de Besançon ») cèdent la place aux types locaux ci-dessous ; Ahrefs cède la place à **Semrush (base fr)** avec repli qualitatif annoncé.

## Quand l'utiliser

- « Qu'est-ce qu'on publie ces prochains mois ? » / « plan de contenu » / « roadmap SEO »
- « Quels mots-clés attaquer ? » / « sur quoi écrire pour ranker ? »
- Après un audit (écart concurrentiel, régression SEO) qui conclut « il manque du contenu » et qu'il faut décider **lequel** et **dans quel ordre**
- Périmètre : **un seul site par analyse** — rushiti-renovation.fr par défaut, rushiti.fr sur demande. Jamais les deux mélangés.

Ne pas confondre avec les voisins : `rushiti-keyword-clusters` part d'une **liste de mots-clés fournie** et la structure ; ce pipeline part de **zéro** (du contexte business) et produit la liste. `rushiti-brief-seo` cadre **un** contenu déjà décidé ; ce pipeline décide **lesquels** créer et dans quel ordre. `rushiti-ecart-concurrentiel` compare à 2-3 concurrents nommés ; ce pipeline couvre tout le spectre d'opportunités.

## Input attendu

Avant de commencer, poser **en une seule fois** (pas d'interrogatoire au fil de l'eau) :

1. **Objectif commercial prioritaire** — ex. « plus de chantiers dégât des eaux via assurances », « remplir le planning de l'hiver », « percer sur Pontarlier », « plus de syndics ». Sans réponse : équilibrer particuliers + B2B local.
2. **Matériaux disponibles** — export GSC (Performance : requêtes et pages), liste de demandes de devis récentes ou questions clients qui reviennent, chantiers récents / à venir, exclusions explicites (services ou zones à éviter).
3. **Chemin de sortie** — défaut : `plan-sujets-[site]-[date].md`.

Si Isuf répond « rien de tout ça », continuer quand même : le socle `references/rushiti-defaults.md` + le site en ligne suffisent pour un premier passage. Le noter dans le rapport.

## Procédure

### Phase 1 — Contexte commercial (fondation, jamais sautée)

Un plan de mots-clés sans contexte business produit les mauvais mots-clés. Construire le **Document de contexte compte** :

1. Lire `references/rushiti-defaults.md` — services, zones, cibles, différenciateurs. Ne jamais redemander ces données.
2. Récupérer le site analysé (sitemap + pages clés via fetch) : inventaire des pages existantes, services couverts, pages locales déjà en ligne, thèmes du blog. Cet inventaire sert au contrôle de cannibalisation en Phase 5.
3. Semrush si le connecteur répond : `domain_overview` et `organic_research` (database **fr**) sur le site — positions actuelles, pages qui performent, mots-clés déjà en positions 4-20 (les « presque gagnés »).
4. Traiter les matériaux fournis : export GSC (requêtes à impressions fortes / clics faibles, requêtes en positions 4-20), demandes de devis (le vocabulaire exact des clients — c'est la matière première la plus riche), exclusions.
5. Produire le document : ce qu'on vend, priorités commerciales déclarées, cibles, zones, ce qui ranke déjà, ce qu'on évite, trous et signaux manquants.

**Point de validation 1 — obligatoire.** Présenter le document et demander : « Ce portrait est-il juste ? Une priorité fausse ici se propage dans tout le plan. » Attendre la confirmation d'Isuf avant la Phase 2.

### Phase 2 — Extraction des opportunités (des angles business, pas encore des mots-clés)

Sept types d'opportunité **locaux** — passer chacun en revue contre le document de Phase 1 :

| Type | Signal | Exemples d'angles |
|---|---|---|
| **Service x Géo** | Service offert + commune/quartier de la zone sans page dédiée | peintre Pontarlier, plaquiste École-Valentin, rénovation appartement Battant |
| **Douleur / Urgence** | Le client cherche son problème, pas le métier | auréole plafond après fuite, moisissure mur chambre, fissure plafond placo, papier peint qui se décolle |
| **Prix / Coût** | Questions « combien ça coûte » avant de demander un devis | prix peinture au m2, coût rénovation salle de bains, tarif pose placo |
| **B2B local** | Syndics, gestionnaires, assurances (IRSI) | entreprise peinture pour syndic, remise en état logement locatif, réfection après sinistre convention IRSI |
| **Saisonnalité** | Travaux liés à la saison | façade au printemps, humidité et condensation l'hiver, rafraîchir avant mise en location |
| **Bâti ancien / spécificité locale** | Différenciateur RUSHITI | rénovation murs en plâtre ancien, humidité bâti ancien Besançon, rénovation immeuble centre historique |
| **Expansion des acquis** | Requêtes GSC / Semrush déjà en positions 4-20 | renforcer la page existante ou créer la déclinaison adjacente |

Pour chaque opportunité retenue : nom, type, **signal précis** (une demande de devis citée, une donnée GSC, une priorité déclarée), valeur business en une phrase (pourquoi ça amène des devis, pas du trafic), formats probables. Priorité pré-validation : Haute (priorité commerciale déclarée + signal nommé), Moyenne (plausible mais inféré), Basse (spéculatif).

Vérifier la couverture : les priorités d'Isuf sont-elles représentées ? Rien ne contredit ses exclusions ? Supprimer ce qui les contredit.

**Point de validation 2 — obligatoire.** Présenter l'inventaire d'opportunités : « Des angles à ajouter, retirer, reprioriser avant que je valide la demande de recherche ? » Attendre la confirmation.

### Phase 3 — Validation de la demande (Semrush, base fr)

Semrush **valide** les opportunités, il ne dicte pas la stratégie. Travailler par priorité décroissante, via `keyword_research` (`get_report_schema` puis `execute_report`, database **fr**).

Graines par type : service + géo (« peintre Besançon », « peintre [commune] »), douleur (« [symptôme] plafond/mur », « comment [résoudre] »), prix (« prix [service] m2 », « coût [travaux] »), B2B (« [service] syndic », « entreprise [métier] copropriété »), variantes du vocabulaire client relevé en Phase 1.

Seuils **locaux** — rien à voir avec les seuils SaaS :
- Volume FR ≥ 10/mois : candidat normal.
- Volume 0 mais service x commune de la zone d'intervention : **candidat quand même**, marqué `0-vol stratégique` — la longue traîne locale et le pack local convertissent sans volume mesurable. C'est l'adaptation la plus importante : en local, un volume nul ne tue pas un sujet, c'est la SERP (Phase 4) qui décide.
- Exclure : intention nationale sans ancrage possible (« meilleure peinture 2026 »), hors zone, hors services, requêtes navigationnelles.
- Plancher : viser **au moins 40 candidats** avant la Phase 4 ; en dessous, élargir les graines des types les plus minces.

**Si Semrush ne répond pas** : repli qualitatif **annoncé** — classer par logique d'intention et signaux GSC, colonnes volume marquées `n/d`. Jamais de volume inventé.

Restituer le pool en tableau, segmenté : Pages locales | Pages services | Douleurs & urgences | Prix & coûts | B2B local. Colonnes : mot-clé, volume FR, difficulté, intention, notes.

### Phase 4 — Qualification SERP (beaucoup de sujets meurent ici — c'est le but)

Pour chaque candidat, vérifier la SERP google.fr réelle (recherche web ; fetch des 1-2 premiers résultats si le format n'est pas évident au titre) :

- **Pack local présent ?** Si oui, la fiche Google Business pèse autant que la page → noter le routage `rushiti-fiche-google-business` en plus du contenu.
- **Qui domine ?** Trois cas types : (a) **annuaires et plateformes** (PagesJaunes, Travaux.com, StarOfService, Houzz) → battable, une vraie page d'artisan local avec preuves passe devant ; (b) **artisans locaux concurrents** → battable avec une page plus complète (trame problème → diagnostic → solution) ; (c) **géants éditoriaux nationaux** (Leroy Merlin, magazines déco, ADEME) sur une requête info générique → très difficile, ne se justifie que si la déclinaison locale de la requête existe.
- **Intention claire ou mixte ?** Format récompensé (page service, guide, FAQ, vidéo) ?

Verdict par mot-clé : **QUALIFIÉ** / **CONDITIONNEL** (une réserve précise, la nommer) / **ÉLIMINÉ** (raison en une ligne). Une liste courte et qualifiée vaut mieux qu'une liste gonflée qui passe tout.

### Phase 5 — Filtre business (le portier commercial)

Cinq portes pour chaque QUALIFIÉ / CONDITIONNEL :

1. **Devis, pas trafic** — un lecteur de cette page peut-il plausiblement demander un devis ?
2. **Zone et cible** — chercheur dans la zone d'intervention, profil client RUSHITI (particulier local, syndic, gestionnaire, assurance) ?
3. **Service réel** — RUSHITI fait vraiment ce travail, sans étirer l'offre ?
4. **Alignement** — Isuf reconnaîtrait-il la recommandation ? Rien qui contredise ses exclusions ni n'exige un prix ou une promesse inventés (les pages prix se font en fourchettes conditionnées ou `PLACEHOLDER`, jamais en chiffres affirmés).
5. **Cannibalisation** — croiser avec l'inventaire de Phase 1 : NOUVEAU / RENFORCER page existante / CANNIBALISE → résoudre. Règle d'or héritée de `rushiti-keyword-clusters` : **un cluster = une intention = une page cible**.

Restituer : liste qui passe (avec désignation NOUVEAU/RENFORCER), liste éliminée avec raison en une ligne.

### Phase 6 — Format et routage

Assigner à chaque sujet survivant son format **et l'agent RUSHITI qui l'exécutera** :

| Format | Route vers |
|---|---|
| Page locale commune/quartier | `rushiti-page-locale` |
| Page service ou article « 1 problème = 1 contenu » | `rushiti-brief-seo` (brief d'abord, toujours) |
| Bloc FAQ / rich snippet sur page existante | `rushiti-faq` |
| Renforcement fiche Google Business / Google Post | `rushiti-fiche-google-business` |
| Étude de cas chantier | `rushiti-declinaison-chantier` |
| Renforcement de page existante (title/meta, contenu) | `rushiti-brief-seo` ou `rushiti-ctr-opportunites` selon le cas |

Regrouper en clusters (mot-clé principal + secondaires par page). Noter le maillage interne à prévoir (`rushiti-maillage-interne` après rédaction).

### Phase 7 — Priorisation

Six dimensions, notées 1-3 chacune (score 6-18) :

1. **Intention devis** — 3 : urgence ou demande active (dégât des eaux, prix, service x géo) ; 2 : projet en réflexion ; 1 : info amont.
2. **Valeur du chantier** — 3 : gros ticket ou récurrent (sinistres, rénovation complète, B2B syndic) ; 2 : chantier moyen ; 1 : petit chantier isolé.
3. **Faisabilité SERP** — 3 : annuaires ou SERP faible ; 2 : artisans locaux à dépasser ; 1 : SERP verrouillée.
4. **Effort (inversé)** — 3 : renforcement ou page courte ; 2 : nouvelle page standard ; 1 : contenu long ou nouveau gabarit.
5. **Autorité existante** — 3 : le site ranke déjà dans ce cluster ; 2 : contenu voisin ; 1 : territoire vierge.
6. **Adjacence aux acquis** — 3 : extension directe d'une page qui marche ; 2 : même famille ; 1 : isolé.

Tiers : **Tier 1** ≥ 14 (à faire d'abord), **Tier 2** 10-13, **Tier 3** ≤ 9 (backlog). Séquencement en Tier 1 : quick wins (renforcements + acquis) → urgences/sinistres et prix → grappes de pages locales construites ensemble → paris longs. Si Isuf a exprimé une préférence de séquence en Phase 1, elle prime sur le score — noter l'arbitrage.

### Phase 8 — Livraison

Sauvegarder le rapport complet au chemin convenu, puis afficher le plan prioritisé **en entier dans la conversation** (Isuf ne doit pas ouvrir le fichier pour lire le plan).

## Structure de sortie

```markdown
# Plan de sujets SEO — [site]
Date : [date] · Objectif commercial : [rappel] · Données : Semrush base fr [ou repli qualitatif annoncé]

## Contexte compte (validé par Isuf le [date])
[Document de Phase 1]

## Inventaire d'opportunités (validé par Isuf le [date])
[Phase 2]

## Validation de la demande
[Tableaux Phase 3 par segment]

## Qualification SERP
[Verdicts Phase 4 + raisons d'élimination]

## Filtre business
[Phase 5 : passent / éliminés]

## Plan prioritisé

### Tier 1 — À faire d'abord (score ≥ 14)
| # | Sujet / mot-clé principal | Format | Vol FR | Score | Route vers | Notes |
|---|---|---|---|---|---|---|

### Tier 2 — Ensuite (10-13)
[même tableau]

### Tier 3 — Backlog (≤ 9)
[même tableau]

## Prochaine étape proposée
[Les 2-3 premiers sujets du Tier 1, avec la commande à donner — ex. « brief pour la page X » → rushiti-brief-seo]
```

## Règles d'écriture

- **La Phase 1 n'est jamais sautée et ses deux points de validation ne sont jamais contournés.** Un portrait de compte faux se propage dans les sept phases — le coût d'une question à Isuf est nul comparé au coût d'un plan à refaire.
- **Semrush valide, le contexte décide.** Une opportunité naît d'un signal business (demande de devis, priorité déclarée, donnée GSC), jamais d'un volume seul. Pourquoi : un volume sans intention locale amène du trafic national qui ne demandera jamais de devis dans le Doubs.
- **Le volume nul ne tue pas un sujet local.** « Peintre Vorges-les-Pins » affiche 0 partout et convertit quand même — la SERP et la zone d'intervention décident, pas le compteur.
- **Éliminer sans regret en Phase 4.** Le livrable fort est une liste courte dont chaque sujet a survécu à la SERP et aux cinq portes. Le symptôme d'un passage raté : une liste de mots-clés que n'importe quel peintre de France pourrait signer.
- **Aucune invention** : volumes et positions viennent de Semrush ou de GSC, sinon `n/d` avec repli annoncé ; les faits produits viennent du site ou des matériaux fournis ; les gains sont des estimations, **jamais des promesses de classement**.
- Lecture seule : ce pipeline propose et priorise. La création de contenu passe par les agents routés, et rien n'est publié sans validation d'Isuf.
- Principes RUSHITI hérités (voix, trame problème → diagnostic → solution, pédagogie, ancrage local — détail dans les skills d'exécution) : ils s'appliquent aux contenus finaux ; ici, ils guident le choix des angles.

## Pièges à éviter

- **Importer les réflexes SaaS.** Pages « alternatives à [concurrent] », « [concurrent A] vs [concurrent B] », listicles « meilleurs logiciels » : ces requêtes n'existent pas pour un artisan local. La version locale du jeu concurrentiel, c'est dépasser le concurrent sur les requêtes service x géo et sur le pack local — pas écrire sur lui.
- **Confondre volume et valeur.** « Peinture salon tendance » (gros volume national) < « peintre dégât des eaux Besançon » (volume minuscule, devis quasi assuré).
- **Ignorer le pack local.** Sur la moitié des requêtes cibles, la fiche Google Business capte le clic avant le site. Un plan qui ne route rien vers `rushiti-fiche-google-business` est suspect.
- **Produire un plan gonflé pour paraître complet.** 15 sujets séquencés et défendables valent mieux que 60 lignes de tableau.
- **Recréer ce qui existe.** Toujours croiser avec le sitemap avant de proposer une « nouvelle » page — la porte 5 existe pour ça.

## Exemple complet (condensé)

**Entrée** : « Fais-moi un plan de contenu pour rushiti-renovation.fr, priorité : plus de chantiers après dégât des eaux, et percer sur Pontarlier. Voilà l'export GSC. »

**Phase 1-2 (extraits validés)** : priorités = sinistres + Pontarlier ; GSC montre « peintre après dégât des eaux » en position 9 (impressions fortes, clics faibles) ; aucune page Pontarlier ; demandes de devis récentes citent deux fois « moisissure chambre ».

**Phases 3-5 (extraits)** : « peintre dégât des eaux Besançon » vol. faible, SERP = annuaires → QUALIFIÉ ; « moisissure mur chambre que faire » vol. correct, SERP = magazines nationaux mais aucune réponse locale avec diagnostic → CONDITIONNEL (angle diagnostic local obligatoire) ; « peintre Pontarlier » `0-vol stratégique`, commune en zone → QUALIFIÉ ; « peinture écologique tendance » → ÉLIMINÉ (porte 2 : intention nationale, aucun signal devis).

**Sortie (Tier 1)** :

| # | Sujet / mot-clé principal | Format | Vol FR | Score | Route vers | Notes |
|---|---|---|---|---|---|---|
| 1 | peintre après dégât des eaux Besançon | Renforcer page existante | 30 | 16 | rushiti-brief-seo | Déjà position 9 — quick win |
| 2 | peintre Pontarlier | Page locale | n/d | 15 | rushiti-page-locale | 0-vol stratégique, zone prioritaire |
| 3 | moisissure mur chambre : diagnostic et réfection | Article 1 problème = 1 contenu | 90 | 14 | rushiti-brief-seo | + bloc FAQ via rushiti-faq |

**Prochaine étape proposée** : « Dis "brief pour la page dégât des eaux" et rushiti-brief-seo prend la main. »
