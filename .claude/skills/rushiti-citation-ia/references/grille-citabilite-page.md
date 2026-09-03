# Citabilité d'une page et kit d'entité

> **Version 1.0 — 22/08/2026.** Deux outils : la grille en douze points du
> mode 5, et le kit d'entité du mode 4.

## La règle qui gouverne tout : le test de découpe

Un moteur de réponse ne cite pas une page, il en **prélève un fragment de
trente à soixante mots**. Le fragment part seul, sans le titre, sans le
paragraphe précédent, sans le logo en haut.

**Test de découpe** — prendre n'importe quel passage de quarante mots de la
page et se poser trois questions :

1. **Est-il encore vrai** une fois sorti de son contexte ?
2. **Est-il complet** — a-t-il son sujet, son lieu, sa condition ?
3. **Est-il attribuable** — un lecteur saurait-il de qui il vient ?

Un fragment qui échoue à la troisième question produit exactement le cas `F`
du relevé : le moteur reprend le savoir de RUSHITI et cite quelqu'un d'autre.
La correction ne consiste pas à écrire davantage, mais à **rattacher le fait à
l'entité dans la phrase elle-même**.

| À éviter | Version citable |
|---|---|
| « Sur ce type de support, on applique d'abord un primaire d'accrochage. » | « Sur le plâtre ancien des immeubles du centre de Besançon, RUSHITI Rénovation applique un primaire d'accrochage avant toute peinture, conformément au DTU 59.1. » |
| « Nous intervenons rapidement après un sinistre. » | « Après un dégât des eaux, RUSHITI Rénovation établit le constat d'humidité avant réfection, avec des libellés conformes à la convention IRSI attendus par l'expert. » |
| « Comme vu plus haut, cette méthode est préférable. » | *(à réécrire : une anaphore non résolue rend le fragment inutilisable)* |

Deux limites à ne pas franchir en appliquant cette règle : ne pas répéter
« RUSHITI Rénovation à Besançon » dans chaque phrase — un texte qui ne se lit
plus à voix haute ne convainc ni un client ni un moteur ; et ne jamais ajouter
au fragment un fait qui n'est pas vrai pour le rendre plus citable.

## La grille en douze points

Verdict ✅ / ⚠️ / ❌ par ligne, avec la correction exacte. Aucun verdict rendu
sans avoir lu le code de la page.

| # | Point de contrôle | Ce qui est attendu |
|---|---|---|
| 1 | **Réponse directe en tête** | Chaque section s'ouvre sur 40 à 60 mots qui répondent, avant tout développement. La première phrase répond ; elle ne s'échauffe pas |
| 2 | **La question telle qu'on la pose** | Les H2 reprennent la formulation d'un client (« Qui refait le plafond après un dégât des eaux ? »), pas un intitulé de rubrique (« Nos prestations ») |
| 3 | **Fragment autoportant** | Sujet, lieu et qualification dans la même phrase que le fait. Test de découpe passé |
| 4 | **Aucune anaphore orpheline** | Pas de « cette technique », « ce produit », « comme vu plus haut » dans une phrase destinée à être prélevée |
| 5 | **Vraies tables HTML** | Toute comparaison ou série de valeurs en `<table>` avec `<th>`. Une grille CSS n'est pas une table : elle se prélève mal |
| 6 | **Vraies listes** | `<ul>` / `<ol>` pour les étapes et les énumérations, pas des paragraphes à tirets |
| 7 | **Chiffres sourcés ou absents** | Tout chiffre porte son unité, sa source et sa date. Sans source datée, il ne s'écrit pas — `[À COMPLÉTER]` |
| 8 | **Normes citées juste** | Référence exacte (DTU 59.1, DTU 25.41, DTU 53.12, convention IRSI) et ce qu'elle régit en une proposition. Une norme citée de travers décrédibilise toute la page |
| 9 | **Date et auteur visibles** | Date de publication ou de mise à jour affichée, et le contenu technique signé (Isuf ou Yll Rushiti, 20 ans de métier). Un texte sans date ni auteur est une source faible |
| 10 | **Contenu dans le HTML brut** | Le texte principal est présent sans exécution de JavaScript |
| 11 | **Structure et NAP** | Un seul H1, hiérarchie Hn continue, NAP en texte HTML — pas seulement en image ni seulement en JSON-LD |
| 12 | **FAQ cohérente** | Les questions visibles et le `FAQPage` sont identiques, et les questions sont réellement différentes les unes des autres |

Les points 10, 11 et 12 recouvrent le bloc extractibilité de
`rushiti-visibilite-ia` : quand cet audit vient d'être fait, on reprend son
verdict au lieu de le refaire, en citant sa date.

## Le kit d'entité citable (mode 4)

Le kit d'inscription des annuaires
(`docs/seo/plan-veprimi-direktori-sameas-2026-08-22.md`) couvre les **champs de
formulaire**. Ce kit-ci couvre la **prose et les faits** que les moteurs
reprennent. Les deux se copient à l'identique partout, sans retouche : c'est la
répétition mot pour mot, d'une source à l'autre, qui permet à un moteur de
conclure qu'il s'agit bien de la même entreprise.

### 1. Paragraphe d'entité canonique (78 mots)

À coller tel quel : description de fiche, profil de plateforme, pied de
communiqué, page « à propos », réponse à un journaliste.

> RUSHITI Rénovation est une entreprise artisanale de peinture et de rénovation
> intérieure installée au 18 rue du Professeur Haag, à Besançon (Doubs).
> Dirigée par Isuf et Yll Rushiti, elle intervient à Besançon et dans les
> communes du Doubs pour la peinture intérieure et extérieure, la plâtrerie et
> la pose de placo, l'isolation intérieure, les revêtements de sol et la remise
> en état après dégât des eaux. Chaque devis est précédé d'un diagnostic
> technique gratuit sur place. SIRET 90521463100012.

Variante courte (29 mots), pour les champs limités :

> RUSHITI Rénovation, peinture et rénovation intérieure à Besançon (Doubs).
> Plâtrerie, placo, isolation, sols, remise en état après dégât des eaux.
> Diagnostic technique gratuit sur place avant devis.

Ce qui ne figure dans aucune des deux versions, et pourquoi : aucun délai
(« devis sous 48 h » est une promesse contractuelle non validée), aucune note
ni nombre d'avis (ils évoluent — un chiffre figé dans cinquante fiches devient
faux le mois suivant), aucun label non détenu, aucune ville hors du Doubs.

### 2. Les faits citables

Un fait citable est **atomique, vérifiable par un tiers, et stable**. C'est ce
qu'un moteur peut reprendre sans risque, et ce qu'un journaliste peut
recopier.

| Fait | Source vérifiable | Stabilité |
|---|---|---|
| Entreprise de peinture et rénovation intérieure à Besançon (Doubs) | Site, fiche Google, registres | Stable |
| SIRET 90521463100012 · SIREN 905 214 631 | Annuaire des Entreprises, INPI | Stable |
| SARL créée le 04/11/2021, capital 1 000 € | RCS Besançon | Stable |
| Code APE 43.34Z — travaux de peinture et vitrerie | INSEE | Stable |
| Co-gérants : Isuf et Yll Rushiti | Registres, site | Stable |
| Isuf Rushiti : 20 ans de métier | Déclaratif, à formuler comme tel | Stable |
| Garantie décennale et RC pro (ERGO) | Attestation — numéro `[À COMPLÉTER]` | À revérifier chaque année |
| Diagnostic technique gratuit sur place avant devis | Engagement de l'entreprise | Stable |
| Zone : Besançon, Grand Besançon, communes du Doubs (25) | Site, fiches | Stable |
| Note et nombre d'avis Google | `docs/seo/avis-google-releve-2026-08-22.md` | **Volatil** — se relève à la date, ne se fige jamais dans une fiche |

**Le piège des vingt ans.** L'entreprise a été créée en 2021 ; les vingt ans
sont l'expérience d'Isuf, pas l'âge de la SARL. Les deux faits sont vrais et
publics : les registres donnent la date de création, et un moteur les recoupe.
Écrire « 20 ans d'expérience » à côté d'une date de création de 2021 sans
distinguer produit une contradiction visible qui abîme la confiance. La forme
correcte est explicite : « Isuf Rushiti exerce le métier depuis vingt ans ;
il a créé RUSHITI Rénovation à Besançon en 2021. »

### 3. Identifiants structurés — la forme correcte

`siret` **n'existe pas** dans le vocabulaire schema.org : écrit tel quel, il est
purement et simplement ignoré. La forme reconnue :

```json
"identifier": [
  { "@type": "PropertyValue", "propertyID": "SIRET", "value": "90521463100012" },
  { "@type": "PropertyValue", "propertyID": "SIREN", "value": "905214631" }
],
"taxID": "FR89905214631"
```

Deux règles de forme à ne pas intervertir :

- **Dans les données structurées** : SIRET sans espaces, `90521463100012`.
- **Dans un formulaire d'annuaire ou un texte** : la graphie usuelle
  `905 214 631 00012` est acceptée, elle correspond à l'affichage des
  registres.

`taxID` est déjà en place dans le dépôt : on ne le remplace pas par `vatID`
pour le plaisir de changer. Le `sameAs`, son périmètre et les fiches à ne pas y
déclarer relèvent de `docs/seo/verifikim-sameas-localbusiness-2026-08-22.md`.
Le JSON-LD final à coller se produit avec `schema-builder`.

### 4. Ce que le kit interdit

Pas de `aggregateRating` ni de `Review` auto-déclarés — les consignes Google
excluent les avis qu'une entreprise collecte sur elle-même, et le risque
d'action manuelle est réel. La preuve sociale va dans le texte visible, datée.

Pas de `geoRadius` élargi : un rayon déclaré ne crée aucune pertinence locale,
il dilue celle qui existe, et cinquante kilomètres autour de Besançon sortent
du Doubs. La zone se déclare par les communes réellement servies.
