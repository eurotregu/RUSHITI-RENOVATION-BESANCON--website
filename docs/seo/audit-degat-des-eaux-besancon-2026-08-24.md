# Audit de la page pilier `/degat-des-eaux-besancon` — 24/08/2026

| | |
|---|---|
| Page auditée | https://rushiti-renovation.fr/degat-des-eaux-besancon |
| Statut dans le cocon | Actif stratégique de niveau 1 — tête du silo « dégât des eaux » |
| Méthode | Lecture du **code HTML** de la page en ligne (rendu Firecrawl, 24/08) + lecture du **dépôt de production** `eurotregu/rushiti-renovation` au commit `3793684` (24/08/2026 02:32). Aucune donnée SERP, aucun chiffre estimé. |
| Comparatif | Page pilier confrontée aux **75 pages de la grille** `degat-des-eaux-<zone>` et aux 757 pages du site |
| Livrables | `korrigjime-prodhim/fix_degat_des_eaux.py` (correctif idempotent) · `korrigjime-prodhim/verifiko_degat_des_eaux.py` (outil de régression) |
| **Statut** | **Fusionné et vérifié en production le 24/08/2026** — PR [#26](https://github.com/eurotregu/rushiti-renovation/pull/26), `main` = `60da3fa` |

---

## 1. Ce que le brief supposait, et ce que le code montre

Trois hypothèses du brief de départ ne se vérifient pas dans le code de la page.
Elles proviennent d'une lecture du texte affiché, pas du HTML. Les corriger évite
de refaire un travail déjà fait.

| Hypothèse du brief | Réalité mesurée dans le code | Conséquence |
|---|---|---|
| « Mungesa e Schema.org JSON-LD 🚨 — gabimi më i madh aktual » | **Faux.** La page porte un `@graph` complet : `LocalBusiness`/`HousePainter`, `Service` avec `@id` et `provider`, `BreadcrumbList`, `FAQPage` avec **13 questions**. Le `sameAs` liste déjà 7 profils (Maps, PagesJaunes, INPI, Annuaire des Entreprises…) | Ne pas réécrire le JSON-LD. Il manque **une seule** clé : `hasOfferCatalog` (voir §2) |
| « Mungesa e Sticky CTA në mobile » | **Faux.** Le composant `.callbar` existe (`position:fixed; bottom:0`, `@media(max-width:720px)`, `body{padding-bottom:66px}`) et est présent sur **756 des 757 pages**, pilier compris : bouton `tel:+33760279897` + bouton devis | Ne rien construire. Seul le **libellé** du 2ᵉ bouton peut porter l'angle assurance (option `--cta`) |
| « Faqja … 4/10 teknik, mungon krejt markup-i strukturor » | **Faux.** Techniquement la page est saine : CSS externe versionnée (`?v=8`), polices chargées en asynchrone (`media="print" onload`) avec repli `<noscript>`, images en `.webp` avec `width`/`height` et `loading="lazy"`, GTM sous Consent Mode, `canonical` + `robots: index, follow` corrects, page dans le `sitemap.xml` (priorité 0.9), `robots.txt` ouvert aux robots IA, entrée dédiée dans `llms.txt` | Le levier n'est pas technique. Il est **éditorial et interne au silo** |

Le point du brief qui se confirme entièrement, en revanche, c'est le diagnostic
de fond : **cette page est le maillon faible de son propre silo.**

---

## 2. Constats réels, chiffrés

### 2.1 Le pilier est la seule page du silo privée de deux briques présentes partout ailleurs

Comparaison automatique pilier / 75 pages de la grille :

| Brique | Pilier | Grille (n/75) |
|---|---|---|
| `hasOfferCatalog` dans le `Service` | **NON** | 75 |
| Bloc avis clients (`4,7 / 5` · 34 avis Google + 3 témoignages) | **NON** | 75 |
| `callbar` (barre d'appel mobile) | OUI | 75 |
| `Service` + `BreadcrumbList` + `FAQPage` | OUI | 75 |
| Formulaire « Demande rapide » (Web3Forms + champ `page`) | OUI | **0** |
| Photos de chantier | OUI | **0** |

La page qui doit convertir l'intention la plus transactionnelle du site est donc
la seule du silo à ne montrer **aucune preuve sociale**, alors que les 75 pages
satellites, qui reçoivent moins de trafic commercial, l'affichent toutes.

### 2.2 Trois séquelles d'un remplacement global « recherche de fuite » → « mesure d'humidité »

Un remplacement de chaîne a été passé sur le silo à une date antérieure. Il a
atteint sa cible mais a laissé trois dégâts collatéraux, dont un contresens
métier visible par les lecteurs **et** par les moteurs de réponse :

1. **Contresens, page pilier, section « Notre périmètre »** :
   > « Une prestation n'entre pas dans notre périmètre : la **mesure d'humidité de la fuite**. Elle relève du plombier… »

   La page annonce quatre paragraphes plus haut, dans « Notre méthode », que la
   première étape est précisément la **mesure d'humidité**. La page se contredit
   donc elle-même. Le texte d'origine disait « la recherche de la fuite » — ce que
   confirment `/devis-assurance-degat-des-eaux-besancon` et
   `/expert-assurance-sinistre-besancon`, qui attribuent tous deux la recherche de
   fuite au plombier.

2. **Doublon dans le JSON-LD, 76 pages sur 76** :
   `"description": "… : mesure d'humidité, mesure de l'humidité, assèchement, …"`

3. **`llms.txt`** annonce pour cette page « recherche d'origine », prestation que
   le site attribue par ailleurs au plombier. C'est le fichier que lisent en
   priorité les moteurs de réponse : l'incohérence y est coûteuse.

### 2.3 Une meta description dont la phrase est coupée

`« … Diagnostic gratuit, devis conforme »` — 140 caractères, phrase inachevée.
Le sens attendu (« conforme à votre assurance ») est tronqué à l'endroit exact
où se joue l'argument commercial.

### 2.4 Le maillage interne : le problème n'est pas l'entrant, c'est le sortant

Mesure sur les 757 pages du site :

- **757 pages sur 757 pointent vers le pilier** — mais 1 513 de ces liens portent
  l'ancre de navigation « Dégât des eaux » et 150 « Dégât des eaux Besançon ».
  Ce sont des liens de menu et de pied de page : ajouter des liens de navigation
  supplémentaires n'apporterait rien.
- Seule une **quinzaine de pages** portent une ancre contextuelle dans le corps
  de texte.
- **Le vrai déficit est sortant** : dans son `<main>`, le pilier ne pointe
  contextuellement que vers **une seule** page — l'article plafond. Il ne pointe
  pas vers :

  | Page satellite | Liens contextuels reçus du pilier |
  |---|---|
  | `/devis-assurance-degat-des-eaux-besancon` (satellite transactionnel du silo) | **0** (1 seul lien de menu sur toute la page) |
  | `/expert-assurance-sinistre-besancon` | 0 |
  | `/renovation-syndic-gestionnaire-besancon` | 0 |
  | `/remise-en-etat-logement-locatif-besancon` | 0 |
  | `/blog/degat-des-eaux-assurance-qui-paie-quoi` (convention IRSI) | 0 |
  | `/blog/reparer-mur-degat-des-eaux-besancon` | 0 |

  La page comporte pourtant une section entière « Après sinistre : déclaration,
  passage de l'expert et indemnisation » qui nomme la convention IRSI, le syndic,
  le gestionnaire de biens et le bailleur — sans un seul lien. La tête du silo ne
  distribue pas son autorité.

### 2.5 Extractibilité par les moteurs de réponse (GEO)

Le chapeau commence par la mise en garde, pas par la réponse :

> « Après un dégât des eaux à Besançon ou dans le Doubs, **le piège est de réparer ce qui se voit**. »

Un moteur génératif qui n'extrait que la première phrase n'y trouve ni l'entité,
ni la prestation, ni la zone. Le reste du chapeau contient tout ; il suffit
d'inverser l'ordre. Le reste de la page est en revanche déjà très extractible :
13 questions/réponses en `<details>` avec **parité parfaite** entre texte visible
et `FAQPage` (13/13 contrôlées), réponses courtes et autoportantes.

---

## 3. Ce que le correctif applique

Script `korrigjime-prodhim/fix_degat_des_eaux.py`, idempotent, testé (§5).

| # | Portée | Correction | Nature |
|---|---|---|---|
| A | 76 pages | JSON-LD : suppression du doublon « mesure de l'humidité » | Bug |
| B1 | Pilier | « la mesure d'humidité de la fuite » → « la recherche de la fuite » | Bug / contresens |
| B2 | Pilier | meta + `og:description` : phrase complétée, 142 car. | Bug |
| B3 | Pilier | `hasOfferCatalog` ajouté au `Service` (5 offres, aligné sur la grille) | Alignement silo |
| B4 | Pilier | Bloc avis `4,7 / 5 · 34 avis Google` + 3 témoignages, inséré avant la FAQ comme sur les pages de zone | Preuve / E-E-A-T |
| B5 | Pilier | 6 ancres contextuelles vers les satellites du silo | Maillage |
| B6 | Pilier | Chapeau réécrit en réponse directe | GEO |
| C | `llms.txt` | « recherche d'origine » → « mesure du taux d'humidité » | Cohérence IA |
| D | Pilier, option `--cta` | Barre mobile : « Devis gratuit » → « Devis assurance » | CRO, au choix d'Isuf |

**Aucun fait nouveau n'est introduit.** Les avis, la note et le lien vers la fiche
Google sont repris à l'identique des pages de la grille déjà en ligne (relevé du
22/08/2026) ; les offres du catalogue ne listent que des prestations déjà
décrites sur la page ; le devis gratuit y est déjà annoncé.

Nouveau chapeau proposé :

> RUSHITI Rénovation remet en état les logements touchés par un dégât des eaux à
> Besançon et dans le Doubs : mesure du taux d'humidité, assèchement, traitement
> anti-moisissure, puis réfection de la plâtrerie, de la peinture et des sols.
> Diagnostic gratuit sur place et devis détaillé pour votre assurance. Le piège à
> éviter : réparer ce qui se voit, alors que l'eau a migré dans les murs, les sols
> et l'isolation.

Mêmes prestations, mêmes engagements, aucune promesse ajoutée : seul l'ordre change.

---

## 4. Ce qui reste à votre arbitrage — non appliqué

| Sujet | Situation | Pourquoi ce n'est pas tranché ici |
|---|---|---|
| **La promesse « devis sous 48 h »** | Elle figure déjà sur 9 pages du site, jamais sur le silo dégât des eaux. Le brief la met partout | C'est un engagement commercial : à vous de confirmer qu'il tient sur un sinistre avant de l'afficher sur la page la plus urgente du site |
| **`<title>` de la page** | « Dégât des eaux Besançon – Intervention rapide \| RUSHITI » (54 car.), conforme. Une variante orientée réparation/assurance est possible | La page ne pèse aujourd'hui que 18 impressions position 20,0 (GSC 17/05–16/08). Changer le title efface le point de référence : à décider avec `rushiti-regression-seo` |
| ~~**H2 en forme de question**~~ | **Fait le 24/08, 2ᵉ passe** : six H2 de section passés en question. Le doublon redouté avec la FAQ prix a été traité en même temps — la question de FAQ devient « De quoi dépend le montant d'une réparation après dégât des eaux ? », `<summary>` et `FAQPage` modifiés ensemble, parité 13/13 conservée | — |
| **Les 75 pages de zone n'ont aucun formulaire** | Constat sorti de l'audit : elles ne convertissent que par la barre d'appel et les liens | Chantier distinct du pilier, à chiffrer séparément (paquet 2 avait transplanté le formulaire sur les pages pilier uniquement) |
| ~~**Barre mobile du pilier**~~ | **Fait le 24/08, 2ᵉ passe** : « Devis gratuit » → « Devis assurance » sur le pilier. Les 75 pages de la grille gardent « Diagnostic gratuit » | Harmoniser tout le silo reste un choix de marque |

---

## 5. Preuve de test

Exécuté sur une copie du checkout de production réel (commit `3793684`, 76 pages
du silo + `llms.txt`) :

| Étape | Résultat |
|---|---|
| Contrôle avant correctif | **86 erreurs** (76 doublons JSON-LD + 10 constats pilier), 1 avertissement `llms.txt` |
| Simulation (sans `--apply`) | 77 fichiers listés, aucune écriture |
| Application | 77 fichiers modifiés, pilier : +2 275 caractères |
| Contrôle après correctif | **CONFORME — 0 erreur, 0 avertissement** |
| Ré-exécution du correctif | **0 fichier modifié** (idempotence prouvée) |
| Validation JSON-LD | 76 blocs relus par `json.loads`, **0 invalide** |
| Diff du texte visible | Limité aux 3 modifications voulues (chapeau, phrase « recherche de la fuite », bloc avis) ; les 6 ancres ne changent pas un mot du texte |

Commandes, sur un checkout du dépôt de production :

```bash
python3 fix_degat_des_eaux.py /chemin/vers/rushiti-renovation                 # simulation
python3 fix_degat_des_eaux.py /chemin/vers/rushiti-renovation --apply         # application
python3 fix_degat_des_eaux.py /chemin/vers/rushiti-renovation --apply --cta   # + libellé barre mobile
python3 verifiko_degat_des_eaux.py /chemin/vers/rushiti-renovation            # contrôle (exit 0 = conforme)
```

`verifiko_degat_des_eaux.py` est un **outil de régression permanent** : à lancer
avant chaque déploiement touchant le silo. Il contrôle la validité JSON-LD, le
doublon, le contresens métier, la longueur et la complétude de la description,
le `hasOfferCatalog`, la présence du bloc avis rattaché au bon `cid` Google, les
6 ancres, la parité FAQ visible ↔ `FAQPage`, la canonical et la barre d'appel.

---

## 6. Évaluation

| Critère | Avant | Après correctif | Ce qui reste à gagner |
|---|---|---|---|
| Technique (rendu, balises, indexation) | 8,5 | 8,5 | Déjà sain — pas un levier |
| Données structurées | 8 | 9,5 | `hasOfferCatalog` posé ; `aggregateRating` à envisager une fois les avis affichés |
| Contenu et couverture (2 100 mots, 13 FAQ) | 9 | 9 | Rien d'urgent |
| Extractibilité IA (GEO) | 6,5 | 9 | 6 H2 en questions posés le 24/08 (2ᵉ passe) |
| Preuve / E-E-A-T | 3 | 8 | Photos de chantier dégât des eaux réelles (RGPD : accord client) |
| Maillage sortant du pilier | 3 | 8 | Étendre aux pages de zone |
| Conversion (CRO) | 7 | 8,5 | « 48 h », si validé |
| Justesse éditoriale | 5 | 9,5 | — |
| **Global** | **6,3** | **8,9** | |

**La bascule ne vient pas de la technique — elle est déjà en place — mais de trois
choses : réparer un contresens qui décrédibilise la page, lui rendre la preuve
sociale que ses 75 satellites affichent déjà, et lui faire enfin distribuer son
autorité vers ses satellites.**

---

## 7. Suite recommandée

1. ~~Valider le correctif, puis l'appliquer sur le dépôt de production.~~
   **Fait le 24/08** avec l'accord d'Isuf : `eurotregu/rushiti-renovation`
   [PR #26](https://github.com/eurotregu/rushiti-renovation/pull/26), branche
   `claude/forcement-silo-degat-des-eaux`, 77 fichiers. Les trois arbitrages du
   §4 sont restés ouverts : pas de « 48 h », `<title>` inchangé, `--cta` non
   appliqué. Reste à fusionner la PR.
2. Relancer `verifiko_degat_des_eaux.py` avant déploiement, et le passer à chaque
   régénération de la grille.
3. Mesure à 4-6 semaines via `rushiti-regression-seo` : impressions et position
   moyenne de `/degat-des-eaux-besancon` (référence : 18 impressions, position
   20,0 sur 17/05–16/08/2026 ; 33 impressions, position 16,0 sur 12 mois), et
   nombre de demandes de devis attribuées à la page via le champ `page` du
   formulaire.
4. Chantier suivant du silo, par ordre de rendement : formulaire sur les 75 pages
   de zone, puis photos de chantier dégât des eaux réelles sur le pilier.

**2ᵉ passe du 24/08** — les deux arbitrages GEO et CRO ont été tranchés et
appliqués (commit `eb52bd5`, même PR #26) : six H2 de section en forme
interrogative, dédoublonnage de la question prix entre H2 et FAQ, et barre
d'appel du pilier en « Devis assurance ». Restent ouverts, inchangés : la
promesse « 48 h », la réécriture du `<title>`, le formulaire des 75 pages de
zone, et l'harmonisation de la barre mobile sur toute la grille.

---

## 8. Vérification en production — 24/08/2026, 11 h 34 UTC

PR #26 fusionnée (`main` = `60da3fa`), déploiement Cloudflare propagé. Contrôles
faits directement sur **rushiti-renovation.fr**, pas sur un aperçu :

| Marqueur | Résultat en ligne |
|---|---|
| Les six H2 en forme de question | ✅ tous servis, dans l'ordre |
| « Une prestation n'entre pas dans notre périmètre : **la recherche de la fuite** » | ✅ contresens corrigé |
| Bloc avis clients | ✅ **4,7 / 5 · 34 avis Google** |
| `hasOfferCatalog` du nœud `Service` | ✅ **5 offres** (diagnostic, assèchement, traitement, réfection, devis assurance) |
| Meta et `og:description` | ✅ terminées par « devis assurance. » |
| Barre d'appel mobile | ✅ « Appeler » + « **Devis assurance** » |
| Parité FAQ visible ↔ `FAQPage` | ✅ **13 / 13 identiques** |
| Ancien libellé de FAQ prix (doublon) | ✅ absent |
| Les 6 ancres contextuelles | ✅ toutes en place, avec leur texte prévu |
| Doublon JSON-LD sur la grille (`/degat-des-eaux-planoise`) | ✅ supprimé |

Rien à corriger après déploiement.

### Mesure à programmer

Référence à comparer dans 4 à 6 semaines, via `rushiti-regression-seo` :

- `/degat-des-eaux-besancon` : **18 impressions, position moyenne 20,0** (GSC 17/05–16/08/2026) ; **33 impressions, position 16,0** sur 12 mois ;
- nombre de demandes de devis attribuées à la page (champ `page` du formulaire) ;
- apparition éventuelle dans les aperçus IA sur les six questions désormais posées en H2.

Ces chiffres sont un point de départ de mesure, pas une promesse de résultat.
