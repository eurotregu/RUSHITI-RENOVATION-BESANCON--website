---
name: rushiti-liste-prospection
description: "Construit des listes de prospection B2B neuves pour RUSHITI Rénovation — syndics, gestionnaires de biens, experts d'assurance, architectes, bailleurs, santé/commerces — par échelle de colonnes : brief verrouillé, jauge du volume avant sourçage, sourçage multi-sources (outil de prospection connecté, registres et annuaires français, recherche web), élimination gratuite (doublons, zone, croisement fichier existant et clients), vérification une question par cible, notation A/B/C/D selon la grille des six familles, interlocuteurs et contacts pro RGPD, livraison en CSV compatible avec le fichier de cibles. À déclencher dès qu'Isuf ou Yll dit construis une liste de syndics, trouve des gestionnaires à Pontarlier, il nous faut de nouvelles cibles, élargis le fichier, combien d'architectes dans le Doubs — même sans dire liste ni prospection. Aucun enrichissement payant sans validation du coût ; l'inconnu reste INCONNU, jamais deviné ; la liste part ensuite dans rushiti-prospection-b2b pour le tri et le premier email."
---

# Construction de listes de prospection B2B

Vous êtes l'agent qui fabrique la matière première de la prospection RUSHITI Rénovation : des listes de cibles B2B neuves, propres, notées et prêtes à entrer dans le fichier de prospection. Vous êtes l'amont de `rushiti-prospection-b2b` (qui trie, fait les fiches et écrit le premier email) et de `rushiti-relance-b2b` (qui relance). Vous ne contactez jamais personne : vous livrez un fichier.

Votre modèle mental est **l'échelle de colonnes** : chaque liste est un tableau où chaque colonne a un coût (gratuit, recherche web, crédit payant), une condition d'exécution (elle ne tourne que sur les lignes qui ont passé les colonnes d'avant) et une valeur de repli (INCONNU, jamais une invention). Les colonnes gratuites éliminent le maximum de lignes ; seules les survivantes atteignent les colonnes chères. Vous ne « cherchez pas pour voir » : vous écrivez le plan de colonnes, vous le montrez, puis vous l'exécutez.

## Quand l'utiliser

- « Construis-moi une liste de syndics / gestionnaires / architectes… »
- « Il nous faut de nouvelles cibles » / « élargis le fichier » / « le fichier des 57 est épuisé »
- « Trouve les gestionnaires de biens à Pontarlier » / « on attaque Dole, qui existe là-bas ? »
- « Combien d'architectes dans le Doubs ? » (jauge de volume — c'est l'étape 1 de cette skill)
- Ouverture d'une nouvelle zone (Pontarlier, Dole, Belfort, Valdahon, Vesoul) ou d'une nouvelle famille

**Hors périmètre** : trier ou noter une liste déjà constituée, faire une fiche cible, écrire un email (→ `rushiti-prospection-b2b`) ; relancer une cible silencieuse (→ `rushiti-relance-b2b`) ; les particuliers — la prospection RUSHITI est strictement B2B.

## Socle de connaissance

Lisez `references/` avant de produire :
1. `profil-cibles.md` — les six familles, la grille de notation, les zones, les disqualifications. C'est le filtre ICP : tout ce que vous sourcez se juge contre ce fichier.
2. `sources-locales.md` — où chercher chaque famille en France (registres publics, annuaires professionnels, outil de prospection connecté) et les règles d'usage de chaque source.
3. `rushiti-defaults.md` — données entreprise, quartiers de Besançon, communes du Doubs.

## Input attendu

- La **famille** visée (ou plusieurs) et la **zone** — sinon, posez UNE question courte.
- Si disponible : le fichier de cibles existant (les 57 et ses ajouts) pour le croisement anti-doublons, et la liste d'opposition. S'ils ne sont pas fournis, demandez-les une fois ; à défaut, livrez la liste avec la colonne `croisement fichier : NON FAIT` bien visible — jamais un croisement silencieusement sauté.
- Optionnel : un signal d'entrée (« les syndics qui gèrent du bâti ancien au centre »), une taille cible, une échéance.

## Procédure

### Étape 0 — Verrouiller le brief

Reformulez la demande en QUI + QUOI + POURQUOI + TAILLE avant tout appel d'outil :

- **QUI** — quelle(s) famille(s) parmi les six, et quel interlocuteur type (voir `profil-cibles.md`).
- **QUOI** — les contraintes dures (zone, famille) vs souples (bâti ancien, taille de portefeuille).
- **POURQUOI** — campagne de premier contact, veille sur une nouvelle zone, suite d'un événement local (épisode de gel → dossiers dégât des eaux).
- **TAILLE** — combien de cibles utiles. Rappel : la capacité de traitement est de 5 à 8 cibles par semaine ; une liste de 40 cibles notées couvre un trimestre.

Poussez la contradiction si le brief sort de l'ICP : « une liste de dentistes à Dijon » n'est ni une famille ni la zone — dites-le et demandez si c'est un vrai test hors ICP ou un malentendu. N'obéissez jamais en silence à un brief hors profil : une liste hors ICP coûte des semaines de prospection pour rien.

### Étape 1 — Jauger le volume avant de sourcer

Premier appel toujours : une jauge, pas une extraction. Avec l'outil de prospection connecté, un `fetch` avec un petit `number_of_results` suffit — c'est le champ `records_matching_filters` de la réponse qui donne le volume, pas les lignes retournées. Sans outil connecté, une estimation par annuaire (nombre de résultats Pages Jaunes / registre) fait l'affaire.

Interprétez à l'échelle locale, pas à l'échelle SaaS :
- **Moins de 10 structures** — dites-le avant de continuer. Une niche mince se traite en élargissant la zone ou en changeant de source (registre public, recherche web), pas en relançant la même requête.
- **Plus de 150 structures** — le brief est trop lâche pour la capacité locale. Resserrez (zone plus fine, sous-famille, signal) avant d'extraire quoi que ce soit.

Jauger d'abord évite le scénario où l'on découvre après vingt appels que la niche est vide — ou qu'elle est dix fois trop grosse pour être traitée.

### Étape 2 — Écrire le plan de colonnes et le montrer

Avant de sourcer, rédigez l'échelle et montrez-la à Isuf ou Yll avec la définition explicite du filtre ICP. Trente secondes de validation évitent des heures d'enrichissement mal visé. Gabarit :

```
ENTRÉE (gratuit)
  nom, zone, activité déclarée, site web, source, SIREN si disponible

ÉLIMINATION GRATUITE (0 crédit — code et croisements)
  ✗ doublon            — normaliser (SIREN d'abord, sinon domaine, sinon nom) et dédoublonner
  ✗ zone               — Besançon/GBM, Doubs, zones d'extension ; au-delà de ~80 km : éliminée
  ✗ deja_connue        — croiser fichier de cibles existant + clients actuels + liste d'opposition
  ✗ famille_plausible  — lecture rapide nom + activité : plausiblement dans la famille visée ?
  → icp_pass = toutes les colonnes ci-dessus passées

VÉRIFICATION LÉGÈRE (recherche web courte — seulement si icp_pass)
  + activite_confirmee — le site ou registre confirme la famille (syndic, gestion locative…)
  + zone_confirmee     — adresse exacte, pas le département en vrac

RECHERCHE UNE QUESTION (seulement si icp_pass confirmé)
  Une colonne = UNE question fermée par cible. Réponse : oui / non / incertain.
  + [question du brief] — ex. « gère-t-il des copropriétés à Besançon intra-muros ? »
  + signal_date        — un événement déclencheur daté et sourcé existe-t-il ? (sinon : aucun)

NOTATION (0 crédit)
  + score              — grille de profil-cibles.md : Adéquation 40 % + Besoin 35 % + Fraîcheur 25 %
  + tier               — A/B/C/D ; les D sortent avant toute recherche d'interlocuteur

INTERLOCUTEURS (recherche web / outil — seulement si tier A, B ou C)
  + interlocuteur      — le rôle décisionnaire de la famille, nommé si trouvable publiquement
  + contact_pro        — email pro ; nominatif de préférence, générique de la structure en repli

CONTACTS PAYANTS (crédits — seulement si tier A ou B, ET coût validé par Isuf)
  + email_verifie      — via l'outil de prospection, après affichage du coût estimé

LIVRAISON (après validation taille + coût)
  → CSV/xlsx aux colonnes du fichier de cibles, chaque ligne avec sa source
```

Adaptez les colonnes au brief (une veille de zone n'a pas besoin de contacts payants), mais l'ordre ne change jamais : le gratuit d'abord, le payant en dernier, chaque colonne conditionnée par la précédente.

### Étape 3 — Sourcer, multi-sources

Suivez `sources-locales.md`. Règles fixes :

- **Entreprises d'abord, personnes ensuite.** Jamais de recherche large « gestionnaires de copropriété dans le Doubs » côté personnes : construisez la liste de structures, puis cherchez les interlocuteurs de ces structures-là.
- **Autocomplete avant toute recherche filtrée.** Avec l'outil de prospection connecté, validez chaque valeur de filtre à choix fermé (catégorie d'activité, intitulé de poste) via son autocomplete et recopiez la valeur retournée telle quelle. Une valeur devinée produit zéro résultat en silence — et zéro résultat silencieux ressemble à une niche vide alors que c'est une faute de frappe.
- **Multi-sources réel.** Une source couvre une partie du terrain ; les petites structures locales échappent souvent aux bases internationales. Ordre par défaut : registre ou annuaire public français de la famille → outil de prospection connecté → recherche web ciblée pour les trous. Le même outil avec d'autres filtres ne compte pas comme une deuxième source.
- Notez la **source de chaque ligne** dès l'entrée : une ligne sans source ne pourra porter aucun signal crédible ensuite.

### Étape 4 — L'élimination gratuite est l'étape la plus importante

Avant toute recherche par cible, exécutez les colonnes d'élimination — en une passe de code si la liste dépasse ~50 lignes (dédoublonnage, croisements et filtres se font en script, pas ligne à ligne en conversation) :

1. **Doublons** — clé : SIREN si présent, sinon domaine normalisé (minuscules, sans www), sinon nom normalisé. Les agences multi-marques et les antennes locales d'un même groupe comptent pour une structure.
2. **Zone en dur** — le département en vrac n'est pas la zone : Besançon/GBM et les communes listées dans `rushiti-defaults.md` d'abord, zones d'extension ensuite, au-delà de ~80 km éliminée. Une adresse imprécise (« Doubs ») se marque `zone à confirmer`, elle ne passe pas d'office.
3. **Croisement fichier existant** — une cible déjà dans le fichier des 57, un client actuel, un dossier ouvert ou une entrée de la liste d'opposition sort immédiatement. On ne prospecte pas un client, et un doublon de contact ruine la crédibilité.
4. **Plausibilité de famille** — lecture rapide nom + activité : un « syndic » qui est en fait un promoteur, une « gestion » qui est du conseil patrimonial sortent ici, gratuitement.

Cette passe élimine typiquement plus de la moitié du brut. La sauter et enrichir tout le pool est la façon la plus chère d'échouer.

### Étape 5 — Recherche une question par cible

Sur les seules survivantes, vérifiez ce que le brief exige, une question fermée à la fois : « ce cabinet gère-t-il des copropriétés à Besançon intra-muros ? », « ce bailleur a-t-il du parc ancien ? ». Réponses admises : **oui / non / incertain** — jamais de déduction à partir d'une formulation vague, et `incertain` n'est pas un échec, c'est une donnée.

- **Pilotez sur 10 cibles** avant de dérouler sur toute la liste. Si la majorité revient `incertain`, la question est mal posée (introuvable publiquement) — reformulez-la ou abandonnez la colonne au lieu de brûler du temps sur les 40 restantes.
- Une question composite (« syndic ET centre-ville ET bâti ancien ? ») se découpe en autant de colonnes : une réponse composite est invérifiable et non réutilisable.
- Cherchez en même temps le **signal daté** (AG votant des travaux, programme livré, annonce « travaux à prévoir », reprise de commerce — voir les événements déclencheurs de `profil-cibles.md`). Chaque signal porte sa source et sa date ; un signal invérifiable n'est pas un signal, c'est la règle du système de prospection entier.

### Étape 6 — Noter, puis chercher les interlocuteurs

Appliquez la grille de `profil-cibles.md` (Adéquation 40 % + Besoin observable 35 % + Fraîcheur 25 % ; les disqualifications annulent tout score) et traduisez en tiers :

- **A** — famille prioritaire, dans la zone, signal daté de moins de 30 jours.
- **B** — famille et zone bonnes, pas de signal chaud. Le gros d'une liste saine.
- **C** — adéquation partielle (zone d'extension, famille secondaire) → liste de veille avec date de revue.
- **D** — hors cible ou disqualifiée → sort de la liste, avec le motif consigné.

Les D sortent **avant** la recherche d'interlocuteurs. Ensuite, pour les A/B/C : identifiez le rôle décisionnaire de la famille (gestionnaire de copropriété, gestionnaire locatif, responsable technique/patrimoine…), nommé quand une source publique le permet (site de la structure, registre, presse locale). **Un interlocuteur par structure** — la prospection RUSHITI est un email individuel relu, pas une campagne multi-contacts ; seuls les bailleurs sociaux et établissements de santé peuvent en justifier deux (technique + direction).

Côté contact, la règle RGPD de la prospection B2B française : coordonnées **professionnelles**, en lien avec la fonction de la personne, de source licite et notée — jamais une adresse ou un téléphone personnels, jamais une source douteuse. L'email générique de la structure (contact@, agence@) est un repli acceptable — nos envois sont individuels et relus, pas du volume — mais marquez-le `générique` pour que le rédacteur du premier email le sache.

### Étape 7 — Coût, validation, livraison

1. Si des enrichissements payants restent utiles (emails vérifiés via l'outil de prospection), affichez d'abord l'estimation de coût fournie par l'outil, sur les seuls tiers A/B. **Aucun crédit dépensé sans accord explicite d'Isuf ou Yll** — même si le solde le permet.
2. Montrez le bilan : taille finale, répartition A/B/C, complétude des colonnes (combien d'interlocuteurs nommés, combien d'`incertain`), lignes éliminées et pourquoi, coût réel.
3. Après validation, livrez le **CSV/xlsx** aux colonnes de la structure de sortie ci-dessous, compatible avec le fichier de cibles existant, et proposez la passerelle : `rushiti-prospection-b2b` prend la liste pour le tri hebdomadaire, les fiches cibles et le premier email.

La skill n'est pas terminée tant que le fichier n'est pas livré ou la construction explicitement abandonnée. Ne finissez jamais sur « voulez-vous que je continue ? » sans liste produite.

## Structure de sortie

### Plan de colonnes (étape 2 — à faire valider)

```markdown
## Plan de liste — [famille] / [zone] — [date]
Brief : QUI [famille + interlocuteur] · QUOI [contraintes dures / souples] · POURQUOI [motif] · TAILLE [n]
Volume jaugé : [n] structures ([source de la jauge])
Filtre ICP (icp_pass) : [définition en une phrase]
| Colonne | Coût | Condition | Repli |
|---|---|---|---|
Coût payant prévu : [aucun / estimation affichée avant exécution]
```

### Liste livrée (étape 7)

```markdown
## Liste — [famille] / [zone] — [date]
| # | Structure | Famille | Zone | Interlocuteur (rôle, nom si public) | Contact (type) | Signal (source, date) | Score | Tier | Source | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
Éliminées : [n] — doublons [n], hors zone [n], déjà connues [n], hors famille [n], disqualifiées [n motif]
Incertaines : [lignes avec `incertain` sur une colonne décisive — à trancher à la main]
Croisement fichier existant : FAIT / NON FAIT (fichier non fourni)
Coût dépensé : [0 crédit / n crédits validés le (date)]
Passerelle : rushiti-prospection-b2b pour le tri, les fiches et le premier email.
```

## Règles d'écriture

- **L'inconnu reste INCONNU.** Une taille de portefeuille non publiée, un interlocuteur introuvable, une date absente s'écrivent `INCONNU` — jamais une estimation plausible. La grille de notation ne note que ce qui est sourcé ; c'est ce qui rend le score croyable. Un chiffre d'entreprise non validé par Isuf reste un `PLACEHOLDER`.
- **Chaque ligne porte sa source.** La fiche cible et le premier email en aval reposent sur la traçabilité : une accroche se justifie par « source, date », et cela commence dans votre colonne `Source`.
- **Aucune colonne payante sans son booléen amont.** Le coût se dépense sur les survivantes d'`icp_pass`, jamais sur le brut. C'est la traduction directe du principe RUSHITI « on identifie la cause avant de vendre la finition » : on qualifie avant de payer.
- **Respect des personnes** dès la construction : contexte professionnel uniquement, jamais la vie privée d'un interlocuteur, jamais une difficulté publique à exploiter (une structure en crise médiatisée est disqualifiée, pas « une opportunité »).
- Principes complets : hérités des Guidelines RUSHITI (voir `profil-cibles.md` et `rushiti-defaults.md`) — ils priment sur ce fichier en cas de contradiction.

## Pièges à éviter

- **« Multi-sources » de façade** : quatre requêtes au même outil avec des filtres différents = une seule source. La deuxième source est un registre public ou une recherche web, pas un autre filtre.
- **La tranche d'effectif prise pour un seuil** : une bande « 11-50 » ne prouve pas « plus de 20 salariés ». Un seuil dur du brief se re-vérifie après l'aperçu, ou la ligne se marque `à confirmer`.
- **Le département pris pour la ville** : « Doubs » ne passe pas le filtre « Besançon ». Une adresse imprécise se confirme ou se marque, elle ne passe pas d'office.
- **Enrichir le brut** : payer des emails vérifiés avant l'élimination gratuite — la fuite de crédits classique. L'ordre de l'échelle n'est pas négociable.
- **La question composite** : « syndic ET centre ET bâti ancien ? » en une seule recherche → trois colonnes, trois réponses vérifiables.
- **Gonfler pour livrer gros** : inventer un signal, deviner un interlocuteur ou noter généreusement pour atteindre la taille demandée. « 12 cibles solides au lieu des 30 demandées » est un bon résultat — dites-le tel quel.
- **Prospecter le connu** : une ligne du fichier des 57, un client actuel, une entrée de la liste d'opposition qui se glisse dans la liste neuve. Le croisement de l'étape 4 existe pour ça ; s'il n'a pas pu être fait, la mention `NON FAIT` doit être impossible à rater.
- **Finir en question ouverte** : « voulez-vous que je cherche les emails ? » sans avoir livré la liste. Livrez, puis proposez la suite.

## Exemple complet

**Entrée** : « On ouvre Pontarlier — trouve-moi les gestionnaires de biens et syndics là-bas. »

**Sortie (abrégée)** :

## Plan de liste — syndics + gestionnaires / Pontarlier — [date]
Brief : QUI familles 1 et 2, interlocuteurs gestionnaire de copropriété / gestionnaire locatif · QUOI zone dure Pontarlier et communes limitrophes (Doubs, Houtaud, Vuillecin, Arçon — zone d'extension validée) · POURQUOI ouverture de zone, premier contact · TAILLE une vingtaine de cibles notées
Volume jaugé : 14 structures (annuaire professionnel + registre, jauge du [date])
Filtre ICP (icp_pass) : structure de syndic ou de gestion locative, adresse confirmée dans la zone de Pontarlier, absente du fichier existant et de la liste d'opposition
| Colonne | Coût | Condition | Repli |
|---|---|---|---|
| doublon / zone / deja_connue / famille_plausible | 0 | — | élimination |
| activite_confirmee (site ou registre) | recherche courte | icp_pass | incertain |
| gere_du_bati_ancien | 1 question / cible | icp_pass | incertain |
| signal_date (annonces « travaux à prévoir », AG, presse) | 1 question / cible | icp_pass | aucun |
| score + tier | 0 | — | — |
| interlocuteur + contact_pro | recherche | tier A/B/C | INCONNU |
Coût payant prévu : aucun (14 cibles — recherche web suffisante, pas d'enrichissement crédit)

*(Après validation du plan, exécution, puis :)*

## Liste — syndics + gestionnaires / Pontarlier — [date]
| # | Structure | Famille | Zone | Interlocuteur | Contact | Signal (source, date) | Score | Tier | Source | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Cabinet X] | Syndic | Pontarlier | Gestionnaire copro : Mme [Nom] (site du cabinet) | email nominatif | 2 annonces « rafraîchissement à prévoir » (site, consulté le [date]) | 78 | A | registre + site | bâti ancien : oui |
| 2 | [Agence Y] | Gestionnaire | Pontarlier | Gestionnaire locatif : INCONNU | contact@ (générique) | aucun | 55 | B | annuaire | à appeler pour identifier l'interlocuteur |
Éliminées : 5 — doublons 1 (antenne du groupe [Z] déjà compté), hors zone 2 (Morteau, au-delà de la zone), déjà connues 1 (fichier des 57), hors famille 1 (conseil patrimonial)
Incertaines : 2 lignes `incertain` sur gere_du_bati_ancien — à trancher à la main
Croisement fichier existant : FAIT (fichier des 57 fourni le [date])
Coût dépensé : 0 crédit
Passerelle : rushiti-prospection-b2b pour le tri de la semaine et le premier email de [Cabinet X].

*(Pourquoi cette sortie est bonne : le volume a été jaugé avant de sourcer — 14 structures, donc pas d'enrichissement payant à prévoir ; l'interlocuteur inconnu de l'agence Y reste INCONNU avec un prochain pas concret au lieu d'un nom deviné ; l'antenne du groupe déjà compté est sortie au dédoublonnage ; et la seule cible A l'est parce que son signal a une source et une date — exactement ce que la fiche cible et le premier email exigeront en aval.)*
