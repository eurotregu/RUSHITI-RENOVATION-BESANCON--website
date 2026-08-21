---
name: rushiti-keyword-clusters
description: "Transforme une liste de mots-clés (export GSC, export Semrush, ou liste collée), enrichie de déclinaisons métier x géo x intention, en clusters exploitables pour rushiti.fr et rushiti-renovation.fr : chaque cluster est rattaché à un des 6 silos sémantiques existants, marqué Couvert / Partiel / Manquant après croisement avec le sitemap, et débouche sur une décision — page à renforcer, nouvelle page à créer (URL et title proposés), ou article de blog à planifier. Utilise Semrush pour volumes et difficulté quand le connecteur répond, sinon priorisation qualitative annoncée — jamais de volume inventé. Règle d'or : un cluster = une intention = une page cible (anti-cannibalisation par construction) ; toute nouvelle page proposée passe ensuite la porte PORTA de rushiti-keyword-map (registre canonique page ↔ mot-clé) avant création. À déclencher dès qu'Isuf ou Yll dit « regroupe ces mots-clés », « fais des clusters », « quelles pages créer avec ces requêtes », « organise ma liste de mots-clés », « plan de contenu à partir de ces keywords », ou fournit une liste de requêtes à structurer. Lecture seule : propose, ne crée ni ne modifie aucune page."
---

# Clusters de mots-clés RUSHITI

Vous transformez des listes de mots-clés en décisions : quelle requête va sur quelle page, quelle page manque, quel article de blog écrire. Votre cadre n'est pas neutre : le cocon sémantique RUSHITI existe déjà (6 silos, pages locales, axe géographique établi) — vous rangez dedans, vous ne le concurrencez pas.

## Quand l'utiliser

- Isuf ou Yll fournit une liste de mots-clés à structurer (export GSC Requêtes, export Semrush, liste collée, idées en vrac).
- Avant une vague de création de pages : décider lesquelles créer et dans quel ordre.
- Pour vérifier la couverture : « ces 80 requêtes, mon site les sert-il déjà ? »
- Pour alimenter le blog : extraire les clusters informationnels et les transformer en calendrier d'articles.

## Héritage des principes RUSHITI

Français, ancrage local Besançon/Doubs, priorisation par valeur business, aucune invention (volumes, difficulté, positions : uniquement des données réelles ou une estimation qualitative annoncée comme telle), lecture seule, rien n'est créé sans validation. Données entreprise : `references/rushiti-defaults.md`. Méthode détaillée : `references/methode-clustering.md`.

## Input attendu

**Minimum** : une liste de mots-clés, quel qu'en soit le format (CSV GSC/Semrush avec métriques, ou simple liste texte), et le site concerné (rushiti-renovation.fr par défaut pour le SEO local ; rushiti.fr si précisé).

**Optionnel** : un thème de restriction (« seulement l'isolation », « seulement Pontarlier »), un objectif dominant (nouvelles pages ? blog ? vérif de couverture ?) — sinon l'agent livre les trois volets.

Si la liste est vide ou trop courte (< 10 mots-clés), proposer de l'enrichir d'abord largement (mode génération : services × zones × intentions) plutôt que de clusteriser trois requêtes.

## Procédure

1. **Ingérer et nettoyer** : normaliser (casse, accents, espaces), dédupliquer, écarter le hors-sujet évident (autres métiers, autres régions sans lien) en le listant en annexe plutôt qu'en le supprimant silencieusement.
2. **Enrichir** : générer les déclinaisons manquantes selon les gabarits de `references/methode-clustering.md` — service × zone (en respectant l'axe géo : Besançon et ses quartiers d'abord, puis Pontarlier, Dole, Belfort, Valdahon, Vesoul) × formulation client réelle (« prix », « avis », « qui appeler », « avant après », problèmes vécus : « auréole plafond », « mur qui cloque »). Marquer chaque mot-clé ajouté comme [enrichi] pour qu'Isuf distingue le fourni du généré.
3. **Récupérer les métriques si possible** : si le connecteur Semrush est disponible dans la conversation, interroger volumes et difficulté pour les mots-clés du marché français. Si l'outil est absent ou échoue, l'écrire en tête de rapport (« priorisation qualitative — Semrush non connecté ») et continuer sans métriques. Les métriques GSC fournies (impressions, clics, position) servent aussi de signal de demande réelle.
4. **Clusteriser** : regrouper par intention de recherche et proximité sémantique — deux mots-clés vont ensemble si la **même page** peut légitimement les servir tous les deux dans la même SERP. Rattacher chaque cluster à un silo. Nommer chaque cluster par sa requête pivot (la plus représentative, ou la plus forte en volume si les données existent).
5. **Croiser avec l'existant** : lire le sitemap du site concerné (fetch en ligne). Marquer chaque cluster :
   - **✅ Couvert** — une page existante sert ce cluster : citer l'URL.
   - **🟡 Partiel** — une page existe mais le cluster est mal servi (page trop générale, intention différente) : dire quoi renforcer.
   - **🔴 Manquant** — aucune page : proposer URL (dans la convention du site) + title (≤ 60 car.) + silo de rattachement.
   Si deux pages existantes semblent servir le même cluster → le signaler et renvoyer vers cannibal-check (ne pas refaire son travail).
6. **Livrer les trois volets** : tableau des clusters, plan de nouvelles pages priorisé, calendrier éditorial blog (clusters informationnels). Chaque page nouvelle proposée passe d'abord le verdict PORTA de rushiti-keyword-map (registre canonique) — aucune création sans ce passage ; les pages locales validées renvoient ensuite vers rushiti-page-locale pour la création ; les briefs d'articles restent des propositions.

## Structure de sortie

```
# Clusters de mots-clés — <site> — <date>

## Synthèse
<Nb de mots-clés fournis / enrichis / écartés, nb de clusters, répartition Couvert/Partiel/Manquant, source des métriques (Semrush connecté ou priorisation qualitative).>

## Volet 1 — Tableau des clusters

### Silo : <ex. Dégât des eaux>
| Cluster (requête pivot) | Intention | Mots-clés rattachés | Volume* | Statut | Page cible |
|---|---|---|---|---|---|
| peintre après dégât des eaux besançon | Locale/transac. | + 4 variantes ([enrichi] marqués) | NNN ou — | ✅ Couvert | /degat-des-eaux/… |
| auréole plafond que faire | Informationnelle | + 3 variantes | NNN ou — | 🔴 Manquant | Article blog proposé |
*Volume : Semrush si connecté, sinon « — » et priorisation qualitative.

<… un bloc par silo. Mots-clés inclassables : section « Hors silos — à arbitrer ».>

## Volet 2 — Nouvelles pages à créer (priorisées)
| Prio | URL proposée | Title proposé (≤60 car.) | Silo | Cluster servi | Justification |
|---|---|---|---|---|---|
| 1 | /communes/pontarlier-peinture | … (NN car.) | Peinture | … | <valeur business + axe géo + volume si dispo> |
→ Avant toute création : verdict PORTA via rushiti-keyword-map. Création des pages locales : agent rushiti-page-locale (avec gabarit HTML du site).

## Volet 3 — Calendrier éditorial blog (clusters informationnels)
| Mois | Article (titre de travail) | Cluster servi | Page service à mailler | Saison |
|---|---|---|---|---|
→ Chaque article existe pour pousser une page service par maillage interne, jamais pour lui-même.

## Recouvrements suspects détectés
<Clusters où deux pages existantes se concurrencent → renvoyer vers cannibal-check.>

## Annexe — mots-clés écartés
<Liste + raison en un mot (hors métier, hors zone, doublon).>
```

## Règles d'écriture

- **Un cluster = une intention = une page cible.** Si deux clusters pointent vers la même page, ils fusionnent. Si un cluster contient deux intentions (« prix peinture besançon » et « comment peindre un plafond »), il se scinde : l'une est transactionnelle, l'autre informationnelle, et elles ne vivront jamais bien sur la même page. C'est cette discipline qui empêche la cannibalisation d'entrer dans le site par la porte du contenu.
- **Le test du regroupement est la SERP, pas le vocabulaire.** « Peintre Besançon » et « entreprise de peinture Besançon » partagent une SERP → même cluster. « Peinture Besançon » (magasin ? artisan ?) est ambigu → le noter. En cas de doute, préférer scinder : fusionner deux pages plus tard est facile, dé-cannibaliser est pénible.
- **Les silos existants sont contraignants à dessein.** Un cluster inclassable dans les 6 silos est un signal à remonter à Isuf (nouveau silo ? hors périmètre ?), jamais un silo inventé en silence. Dans les rattachements, toile de verre et papier peint appartiennent au périmètre au même titre que la peinture — ne pas les diluer ni les oublier.
- **Jamais de métrique inventée.** Un volume vient de Semrush ou de GSC, ou il n'existe pas (« — »). La priorisation qualitative (valeur business > axe géo > demande supposée) est honnête et le dit ; un volume inventé est un mensonge chiffré qui orienterait de vraies décisions de création de pages.
- **L'axe géographique est un ordre, pas un buffet** : Besançon et quartiers, puis Pontarlier (frontaliers), puis Dole, Belfort, Valdahon, Vesoul. Une page locale « Lons-le-Saunier » proposée avant que Pontarlier soit complet contredit la stratégie établie.
- **URLs proposées dans la convention du site** observée dans le sitemap (structure des dossiers existants) — jamais une arborescence inventée.

## Pièges à éviter

- ❌ Clusteriser par mot commun (« tout ce qui contient peinture ensemble ») → « peinture salon » et « prix peinture façade » n'ont ni la même intention ni la même page.
- ❌ Proposer 15 nouvelles pages locales d'un coup → prioriser selon l'axe géo et la capacité réelle de création ; un plan irréaliste ne sera pas exécuté.
- ❌ Mettre un volume « estimé ~500/mois » sans source → soit Semrush/GSC, soit rien.
- ❌ Créer un cluster « toile de verre » orphelin hors silos → la toile de verre vit dans le silo peinture/préparation des murs, avec sa page dédiée si le cluster le justifie.
- ❌ Recommander une page nouvelle quand une page Partielle peut être renforcée → renforcer l'existant bat créer un doublon (et coûte un déploiement de moins).
- ❌ Ignorer que le sitemap peut être en retard sur la production → si une URL récente connue manque au sitemap, le signaler (c'est un finding en soi, pour rushiti-indexation).
- ❌ Proposer une page nouvelle sans passage par le registre rushiti-keyword-map → le verdict PORTA (LEJOHET / REFUZOHET) précède toute création ; contourner la porte fabrique la cannibalisation que ce skill prétend éviter.

## Exemple complet

**Input :** « Voici 12 requêtes de GSC, organise-les : peintre besançon prix, auréole plafond que faire, entreprise peinture pontarlier, devis peinture besançon, mur qui cloque humidité, peintre pas cher besançon, toile de verre ou enduit, prix pose toile de verre, peinture après dégât des eaux, peintre valdahon, refaire peinture salon prix, isolation mur froid intérieur »

**Extrait de sortie (volet 1, silo Peinture) :**

```
| Cluster (requête pivot) | Intention | Mots-clés rattachés | Volume | Statut | Page cible |
|---|---|---|---|---|---|
| devis peinture besançon | Locale/transac. | peintre besançon prix · peintre pas cher besançon · refaire peinture salon prix · [enrichi] tarif peintre besançon | — | ✅ Couvert | /peinture/peintre-besancon |
| entreprise peinture pontarlier | Locale/transac. | [enrichi] peintre pontarlier · [enrichi] devis peinture pontarlier | — | ✅ Couvert | /communes/pontarlier (vérifier que la page sert bien l'angle « entreprise ») |
| toile de verre ou enduit | Informationnelle | prix pose toile de verre* | — | 🔴 Manquant | Article blog → maille vers la page toile de verre |
*« prix pose toile de verre » est à la frontière transactionnelle : si le volume Semrush le justifie, le scinder vers la page service toile de verre plutôt que vers l'article.
```

**Pourquoi cette sortie est correcte :** « peintre pas cher » rejoint le cluster prix sans qu'on crée une page « pas cher » (même SERP, même page) ; les [enrichi] sont marqués ; l'ambiguïté informationnel/transactionnel de « prix pose toile de verre » est arbitrée explicitement au lieu d'être cachée ; aucun volume n'est inventé ; et chaque cluster débouche sur une décision.
