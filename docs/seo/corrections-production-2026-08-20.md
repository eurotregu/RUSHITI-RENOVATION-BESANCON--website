# Corrections à porter sur rushiti-renovation.fr — relevé du 20/08/2026

Relevé effectué **en ligne** sur la production (fetch direct, `maxAge: 0`),
pas de mémoire. Chaque constat est accompagné de la citation exacte relevée et
de l'URL où elle se trouve.

Ce dépôt n'héberge pas la production : les corrections ci-dessous se posent sur
les fichiers du site en ligne. Ce qui était corrigeable **dans ce dépôt** l'a
été (voir la dernière section).

**Périmètre mesuré** : 1 395 URLs déclarées au sitemap, dont environ 1 368 pages
générées `/{service}-{commune}` (18 services × 76 communes) et 27 pages
éditoriales.

---

## Tableau de bord

| # | Constat | Gravité | Effort | Décision d'Isuf |
|---|---|---|---|---|
| 1 | Mentions légales : la clause cookies contredit le site | 🔴 P0 | 1 fichier | non |
| 2 | Fautes de français systémiques dans les pages générées | 🔴 P0 | générateur | non |
| 3 | Horaires : trois versions contradictoires en ligne | 🔴 P0 | générateur | ✅ tranchée |
| 4 | Mention « Qualification RGE » sur une seule page | 🟠 P1 | 1 page | ✅ retrait + vérif |
| 5 | `llms.txt` annonce 29 avis, le site en annonce 34 | 🟠 P1 | 1 fichier | non |
| 6 | `sitemap-communes.xml` vide et déclaré deux fois | 🟠 P1 | 2 fichiers | non |
| 7 | `/organic-ehpad-besancon` redirige vers un sujet sans rapport | 🟠 P1 | 1 règle | ✅ tranchée |
| 8 | « devis sous 48 h » promis en SERP, absent des pages | 🟠 P1 | métadonnées + pages | ✅ tranchée |
| 9 | Titre de CTA hors sujet sur la page syndics | 🟡 P2 | 1 page | non |
| 10 | Apostrophe échappée dans un `og:title` | 🟡 P2 | 1 page | non |
| 11 | Meta description d'accueil à 157 caractères | 🟡 P2 | 1 page | non |
| 12 | JSON-LD d'accueil sans horaires | 🟡 P2 | 1 page | après #3 |
| 13 | Pages communes identiques à 71–78 % entre elles | 🟡 P2 | générateur | non |

---

## 1. 🔴 Les mentions légales contredisent le comportement réel du site

`https://rushiti-renovation.fr/mentions-legales`, section 7, affirme aujourd'hui :

> « Le site rushiti-renovation.fr n'utilise pas de cookies de suivi ni de mesure
> d'audience. Aucune donnée de navigation n'est collectée à des fins
> publicitaires ou statistiques. Aucun consentement n'est donc requis. »

Or le site charge le **Pixel Meta** (identifiant `1128396322151313`) derrière un
bandeau de consentement présent sur toutes les pages, et **la même page**
comporte plus bas une section « Cookies et mesure d'audience publicitaire » qui
décrit ce Pixel. La page se contredit donc elle-même, et la version qui subsiste
en section 7 est fausse.

C'est le point le plus exposé du site : en cas de contrôle CNIL, une clause
« aucun consentement n'est requis » alors qu'un traceur publicitaire est déposé
est un écart difficile à défendre.

**Correction — remplacer intégralement la section 7 par :**

```
## 7. Cookies et traceurs

Le site rushiti-renovation.fr dépose un traceur publicitaire, le Pixel Meta
(Facebook / Instagram), destiné à mesurer l'efficacité de nos campagnes
publicitaires et à proposer des annonces pertinentes aux personnes ayant
consulté notre site.

Ce traceur n'est déposé qu'après votre consentement explicite, recueilli via le
bandeau affiché lors de votre première visite. Si vous cliquez sur « Refuser »,
aucun cookie publicitaire n'est déposé et aucune donnée n'est transmise à Meta.

Vous pouvez modifier votre choix à tout moment en effaçant les données de
navigation de ce site dans votre navigateur.

Le responsable du traitement est RUSHITI Rénovation. Les données collectées par
ce traceur sont traitées par Meta Platforms Ireland Ltd conformément à sa
politique de confidentialité.

Le site n'utilise aucun autre traceur : ni mesure d'audience, ni cookie
analytique.
```

Supprimer ensuite la section « Cookies et mesure d'audience publicitaire »
placée en fin de page, dont le contenu est repris ci-dessus — sinon la page
traite deux fois le même sujet.

> ⚠️ Si une mesure d'audience (GA4) est installée plus tard, cette section doit
> être mise à jour **le même jour** que l'installation.

---

## 2. 🔴 Fautes de français systémiques dans les pages générées

Sur un échantillon de **14 pages** tirées de services et de communes différents,
**11 pages (79 %) comportent au moins une faute**, pour **20 fautes** au total.

Les fautes ne sont pas des accidents isolés : **chacune se répète d'une page à
l'autre**, ce qui signifie qu'elle vient d'une chaîne du générateur et qu'elle
est donc republiée sur des centaines de pages.

| Chaîne fautive (verbatim) | Correction | Constatée sur |
|---|---|---|
| « se **dégladera** avant l'hiver » | se **dégradera** | /peinture-interieure-beure, /peinture-interieure-avanne-aveney |
| « On diagnostique le support, **on ragréé**, **on pose soigné**. » | « on **ragrée**, on pose **soigneusement** » | /sol-pvc-beure, /lino-vinyle-lvt-boussieres, /ragreage-sol-boussieres |
| « font partie **de nos tous nos** revêtements de sol » | « de **tous nos** revêtements de sol » | /parquet-flottant-boussieres, /lino-vinyle-lvt-boussieres |
| « travaux **de isolation intérieure** » | « travaux **d'isolation intérieure** » | /isolation-interieure-beure |
| « la mousse **repercent** » | « la mousse **repousse** » | /peinture-exterieure-beure |
| « un fond non fixé **fait farine** » | « **farine** sous la nouvelle peinture » | /peinture-exterieure-beure |
| « **Une seule pignon** » | « **Un seul pignon** » | /peinture-exterieure-beure |
| « des lés bien **maroflés** » | « bien **marouflés** » | /toile-de-verre-beure |
| « une vraie étanchéité **bien posé** » | « **Bien posé,** le PVC offre une vraie étanchéité » | /sol-pvc-beure |
| « **les plâtrerie et placo** » | « **la plâtrerie et le placo** » | /revetements-sol-chalezeule |
| « peinture qui se **décolla** » | qui se **décolle** | /peinture-interieure-boussieres |
| « les maisons **accumulnt** les années » | **accumulent** | /peinture-interieure-beure |

**Deux défauts de gabarit s'ajoutent :**

- **Repère géographique dupliqué** : sur les pages Boussières, la phrase
  « le clocher roman du XIe siècle de l'église Saint-Étienne » apparaît **deux
  fois de suite**, la seconde introduite par « Pour situer le secteur, un
  repère : ». Le slot « repère » doit tirer un point de repère *différent* de
  celui déjà cité dans la phrase patrimoine (sur la page parquet, il tire
  correctement « le canal du Rhône au Rhin »).
  Constaté sur /papier-peint-boussieres, /ragreage-sol-boussieres,
  /doublage-murs-boussieres.
- **Fuite de localité** : /toile-de-verre-beure parle du « bâti ancien
  **bisontin** » alors que la page vise Beure. Le gabarit doit utiliser la
  commune de la page, ou une formule neutre (« le bâti ancien du secteur »).
- **Élision manquante** : prévoir un helper `de` / `d'` sur le token service,
  sinon « travaux de isolation » se reproduira sur toutes les pages isolation.

**Blocs à corriger, par priorité** (ce sont les blocs du générateur, pas les
pages) :

1. Phrase d'accroche / intro service — la plus visible, au-dessus de la ligne de flottaison.
2. Lignes « Pourquoi : » de la méthode.
3. Paragraphe géo / bâti (repère dupliqué + fuite de localité).
4. Paragraphe de maillage « nos autres services » (élision, « de nos tous nos »).

Les blocs FAQ, cartes de problèmes, tarifs et avis étaient **propres** sur les
14 pages : pas d'intervention nécessaire.

> Après correction des chaînes, relancer la génération puis **repasser un
> contrôle sur un nouvel échantillon** d'une quinzaine de pages : c'est le seul
> moyen de vérifier qu'aucune chaîne fautive ne subsiste.

---

## 3. 🔴 Horaires : trois versions contradictoires, dont deux sur la même page

| Source | Valeur relevée |
|---|---|
| Pied de page (toutes les pages) | « Lun – Ven : 7h – 20h30 · Sam : 8h – 20h30 · Dim : 9h – 17h30 » |
| Bloc contact de `/contact` | « Horaires — Lundi – Vendredi : 8h – 18h » |
| `/llms.txt` | « Horaires : du lundi au vendredi, 8h–18h » |

La page `/contact` affiche donc **8h – 18h dans son bloc contact et 7h – 20h30
dans son propre pied de page**, à quelques centaines de pixels d'écart.

C'est un signal de fiabilité important : les horaires sont l'une des données
que Google recoupe entre le site et la fiche Google Business Profile, et que les
moteurs IA citent directement.

**Décision d'Isuf (20/08/2026) : les deux plages sont vraies, mais ne
désignent pas la même chose.** Il ne s'agit donc pas de choisir, mais de les
distinguer explicitement — c'est aujourd'hui leur confusion qui fait
contradiction.

Lecture retenue, à confirmer d'un mot par Isuf avant mise en ligne :

| Notion | Plage | Où l'afficher |
|---|---|---|
| **Joignabilité téléphonique** | 7h – 20h30 en semaine, samedi 8h – 20h30, dimanche 9h – 17h30 | Pied de page, à côté du numéro |
| **Horaires d'intervention et de bureau** | Lundi – vendredi, 8h – 18h | `/contact`, `llms.txt`, JSON-LD, fiche Google |

### Texte à poser

**Pied de page** (remplacer la ligne d'horaires actuelle) :

```
Joignables par téléphone : lun – ven 7h – 20h30 · sam 8h – 20h30 · dim 9h – 17h30
Interventions et bureau : lun – ven 8h – 18h
```

**Bloc contact de `/contact`** (remplacer le bloc « Horaires ») :

```
Interventions et bureau : lundi – vendredi, 8h – 18h
Téléphone : 7j/7, lun – ven 7h – 20h30, sam 8h – 20h30, dim 9h – 17h30
```

**`llms.txt`** (remplacer la ligne « Horaires ») :

```
- Horaires d'intervention : du lundi au vendredi, 8h–18h
- Joignabilité téléphonique : 7j/7 — lun-ven 7h–20h30, sam 8h–20h30, dim 9h–17h30
```

**JSON-LD** : `openingHoursSpecification` reçoit les **horaires d'intervention**
(lun – ven 8h – 18h, cf. #12), pas la plage d'appel. La joignabilité élargie est
un argument commercial qui se dit en texte, pas une donnée d'ouverture.

> ⚠️ La **fiche Google Business Profile** doit porter la même chose que le
> JSON-LD : Google recoupe les deux. Si la fiche affiche aujourd'hui la plage
> large, l'aligner sur 8h – 18h et mentionner la joignabilité élargie dans la
> description de l'établissement.

---

## 4. 🟠 « Qualification RGE » affichée sur une seule page

`https://rushiti-renovation.fr/isolation-besancon` affiche dans sa barre de
confiance : **« Qualification RGE »**.

Cette mention **n'apparaît nulle part ailleurs** : ni sur l'accueil (dont la
section de confiance « Un artisan déclaré, assuré et engagé » liste la
décennale, le SIRET et la conformité DTU), ni sur `/a-propos`, ni dans
`llms.txt`, ni dans les mentions légales — lesquelles détaillent pourtant
précisément le contrat d'assurance sans jamais mentionner RGE.

RGE est un label **réglementé et vérifiable publiquement**, qui conditionne
l'accès à la plupart des aides. L'afficher sans le détenir expose à une
qualification de pratique commerciale trompeuse.

**Décision d'Isuf (20/08/2026) : à vérifier — la mention est retirée par
précaution en attendant confirmation.**

### Action immédiate

Retirer **« Qualification RGE »** de la barre de confiance de
`/isolation-besancon`. Remplacer par une mention vérifiée, alignée sur le reste
du site :

```
Mise en œuvre conforme aux DTU
```

### Vérification officielle à mener

La qualification RGE est publique et se vérifie sur le SIRET, gratuitement :

- **Annuaire France Rénov'** : https://france-renov.gouv.fr/annuaires-professionnels/artisan-rge-architecte
- **Open data ADEME** (même source, interrogeable directement) :
  `https://data.ademe.fr/data-fair/api/v1/datasets/liste-des-entreprises-rge-2/lines?q=905214631`

**Résultat préliminaire du 20/08/2026 — à confirmer :** l'appel ci-dessus sur le
SIREN `905214631` a répondu `{"total":0,"results":[]}` (HTTP 200), c'est-à-dire
aucune qualification RGE trouvée. **Ce résultat n'est pas concluant en l'état** :
la requête de contrôle qui aurait prouvé que le paramètre de recherche fonctionne
n'a pas pu être exécutée (service d'accès web indisponible au moment du test). Un
`total: 0` peut donc aussi bien signifier « aucune qualification » que « requête
mal formée ». À rejouer, avec une recherche de contrôle sur une entreprise
connue comme RGE.

- **Si la vérification confirme l'absence de RGE** : la mention reste retirée,
  définitivement.
- **Si une qualification est trouvée** : la réafficher partout où elle a de la
  valeur (accueil, `/a-propos`, `llms.txt`, pages isolation), avec l'organisme
  certificateur, le domaine de travaux couvert et la date de validité — c'est un
  argument commercial fort, aujourd'hui quasiment invisible.

Note : la FAQ de cette même page indique, à propos des aides, « Nous ne nous
substituons pas aux organismes officiels » sans invoquer RGE — cohérent avec
l'hypothèse d'une mention posée par erreur.

---

## 5. 🟠 `llms.txt` annonce 29 avis, le reste du site en annonce 34

`https://rushiti-renovation.fr/llms.txt` (deux fois) :

> « Note 4,7/5 sur 29 avis Google » · « Avis : 4,7/5 sur 29 avis Google »

Toutes les autres surfaces relevées disent **34** : corps de l'accueil
(« 4,7 / 5 ★★★★★ · 34 avis Google »), JSON-LD de l'accueil
(`reviewCount "34"`), et les meta descriptions de `/peinture-interieure-besancon`,
`/platrerie-besancon`, `/isolation-besancon`, `/revetements-sol-besancon`.

`llms.txt` est donc le seul fichier en retard — c'est le fichier que lisent les
moteurs IA pour décrire l'entreprise.

**Correction — dans `llms.txt`, remplacer les deux occurrences de**
`4,7/5 sur 29 avis Google` **par** `4,7/5 sur 34 avis Google`.

> Le nombre d'avis augmente avec le temps : plutôt que de le corriger à la main
> à chaque fois, mieux vaut ne l'écrire qu'à un seul endroit du générateur et
> l'injecter partout, `llms.txt` compris.

---

## 6. 🟠 `sitemap-communes.xml` est vide, et déclaré deux fois

`https://rushiti-renovation.fr/sitemap-communes.xml` renvoie un sitemap
**sans aucune URL** :

```xml
<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>
```

Il est pourtant déclaré **deux fois** : dans `robots.txt`
(`Sitemap: https://rushiti-renovation.fr/sitemap-communes.xml`) et dans l'index
`sitemap.xml`. Les pages communes, elles, sont bien listées — mais dans
`sitemap-pages.xml`, qui contient les 1 395 URLs.

Un sitemap vide déclaré à Google n'est pas pénalisant, mais il remonte en erreur
dans Search Console et brouille le suivi d'indexation.

**Correction, au choix :**

- **Le plus simple** — supprimer `sitemap-communes.xml`, retirer sa ligne de
  `robots.txt` et son entrée de l'index `sitemap.xml`.
- **Ou** le remplir réellement avec les ~1 368 URLs communes et retirer
  celles-ci de `sitemap-pages.xml` : deux sitemaps thématiques permettent de
  suivre séparément, dans Search Console, l'indexation des pages éditoriales et
  celle des pages générées. C'est plus utile à terme.

Dans les deux cas, retirer la ligne `Sitemap:` redondante de `robots.txt` : un
sitemap déjà présent dans l'index n'a pas à y être déclaré une seconde fois.

---

## 7. 🟠 `/organic-ehpad-besancon` redirige vers un sujet sans rapport

L'URL `https://rushiti-renovation.fr/organic-ehpad-besancon` redirige
aujourd'hui vers `https://rushiti-renovation.fr/platrerie-besancon`.

Le précédent audit (13/08) recommandait de rediriger cette URL — dont le
préfixe `organic-` était un artefact — vers une URL propre `/ehpad-besancon`.
La redirection posée pointe vers la **plâtrerie**, sujet différent de celui
attendu par l'internaute qui cherchait une page EHPAD.

Google traite une redirection vers une page hors sujet comme un *soft 404* : le
lien entrant ne transmet rien et l'URL sort de l'index sans que la nouvelle
page en profite.

**Décision d'Isuf (20/08/2026) : la cible EHPAD est conservée — la page est
republiée sous une URL propre.**

### Actions

1. Republier le contenu EHPAD sous **`/ehpad-besancon`** (sans le préfixe
   `organic-`, qui était un artefact de campagne).
2. Remplacer la redirection actuelle vers `/platrerie-besancon` par une 301 vers
   la nouvelle page. Sur Cloudflare Pages, fichier `_redirects` :

```
/organic-ehpad-besancon/ /ehpad-besancon 301
/organic-ehpad-besancon  /ehpad-besancon 301
```

3. Ajouter `/ehpad-besancon` au sitemap, et la lier depuis les pages qui la
   servent : `/renovation-syndic-gestionnaire-besancon` (même public
   professionnel), `/peinture-interieure-besancon` et `/revetements-sol-besancon`.
4. Vérifier au crawl qu'aucune autre URL ne porte le préfixe `organic-` ou
   `paid-` : si le générateur a produit ce préfixe une fois, il a pu le faire
   ailleurs.

Le title relevé en SERP à l'époque — « EHPAD & maison de retraite à Besançon —
RUSHITI Rénovation » — reste bon, il suffit de le porter sur la nouvelle URL.

> À surveiller : une page EHPAD s'adresse à des directeurs d'établissement, pas
> à des particuliers. L'angle qui convertit y est la contrainte de site occupé —
> chantier en milieu de soin, phasage par zone, propreté, nuisances sonores,
> continuité de service. C'est le même argumentaire que la page syndics, appliqué
> à un établissement de santé.

---

## 8. 🟠 « devis sous 48 h » : promis dans la SERP, absent des pages

La promesse apparaît **uniquement dans les titles et meta descriptions** :

- `/` — title « Peintre & plaquiste à Besançon — devis sous 48 h | RUSHITI »
- `/peinture-interieure-besancon`, `/revetements-sol-besancon` — « Devis sous 48 h. »
- `/platrerie-besancon`, `/isolation-besancon` — « visite et devis sous 48 h »

**Aucune page ne reprend ce délai dans son corps de texte** : les pages parlent
de « diagnostic gratuit » et de « devis détaillé sans engagement ». Pire, la FAQ
de `/renovation-syndic-gestionnaire-besancon` répond à « Sous quel délai
obtient-on un devis ? » par « Nous convenons rapidement d'une visite sur
place », sans jamais citer 48 h.

Un visiteur qui clique sur la promesse ne la retrouve pas : c'est une déception
au premier écran, et un engagement commercial pris sans être tenu par écrit.

**Décision d'Isuf (20/08/2026) : le délai est tenable — il est donc assumé
dans le texte des pages, et non plus seulement dans la SERP.**

Reste un point à préciser d'un mot : **48 h après la visite technique**, ou
**48 h après le premier contact** ? Les textes ci-dessous retiennent *après la
visite*, seule version opérationnellement cohérente — un devis détaillé suppose
d'avoir vu les supports. Si c'est le premier contact qui compte, remplacer la
formule partout.

### Texte à poser dans le bloc méthode (toutes les pages service)

```
Devis sous 48 h. Après la visite technique, vous recevez un devis détaillé
poste par poste sous 48 heures ouvrées — pas une fourchette au téléphone,
un chiffrage qui correspond à ce que nous avons vu sur place.
```

### Question à ajouter aux FAQ des pages service

```
Sous quel délai reçoit-on le devis ?
Sous 48 heures ouvrées après la visite technique. La visite et le devis sont
gratuits et sans engagement. Ce délai nous permet de chiffrer poste par poste
à partir de l'état réel des supports relevé sur place.
```

### Harmonisation

- Ajouter la promesse aux metas des pages qui ne la portent pas encore :
  `/degat-des-eaux-besancon`, `/cloisons-besancon`.
- **Corriger la FAQ de `/renovation-syndic-gestionnaire-besancon`**, qui répond
  aujourd'hui « Nous convenons rapidement d'une visite sur place » sans jamais
  citer 48 h — elle contredit la promesse affichée en SERP. Y porter la même
  réponse que ci-dessus.

> Une promesse chiffrée tenue vaut mieux qu'une promesse vague : c'est
> exactement ce que compare un syndic entre deux devis. Mais elle n'a de valeur
> que si elle est écrite au même endroit que le reste — sinon le visiteur qui a
> cliqué sur « devis sous 48 h » ne la retrouve nulle part et doute du reste.

---

## 9. 🟡 Titre de CTA hors sujet sur la page syndics

`https://rushiti-renovation.fr/renovation-syndic-gestionnaire-besancon` se
termine par le titre :

> « Des murs à ratisser avant peinture à Besançon ? »

C'est un reliquat de copier-coller depuis la page ratissage. Sur une page qui
s'adresse à des syndics et des gestionnaires, le dernier appel à l'action —
celui qui précède le formulaire — parle d'un autre métier.

**Correction — remplacer par :**

> Des parties communes à rénover ou un sinistre à traiter ?

---

## 10. 🟡 Apostrophe échappée dans un `og:title`

`https://rushiti-renovation.fr/zones-intervention` expose :

```html
<meta property="og:title" content="Zones d\'intervention — RUSHITI Rénovation, Besançon et Doubs">
```

L'antislash est visible tel quel : il s'affichera dans l'aperçu au partage sur
Facebook, LinkedIn et WhatsApp. C'est un échappement PHP/JS resté dans la
sortie HTML.

**Correction** : `Zones d'intervention — RUSHITI Rénovation, Besançon et Doubs`,
et vérifier dans le générateur que l'échappement n'est pas appliqué deux fois
sur les autres attributs `content`.

Accessoirement, l'`og:description` de cette page diffère de sa meta
description : sans raison éditoriale, mieux vaut aligner les deux.

---

## 11. 🟡 Meta description d'accueil : 157 caractères

> « Artisan peintre et plaquiste à Besançon et dans le Doubs : peinture,
> plâtrerie, sols, isolation, dégâts des eaux. 20 ans de métier, 34 avis, devis
> sous 48 h. »

157 caractères : la fin est susceptible d'être tronquée dans la SERP. C'est la
**seule** meta hors limite du site — toutes les autres tiennent entre 139 et
154 caractères, et tous les titles entre 41 et 60. Le travail sur les métadonnées
est donc bon dans l'ensemble.

**Correction proposée (152 caractères)** — à ajuster selon l'arbitrage du #8 :

```
Artisan peintre et plaquiste à Besançon et dans le Doubs : peinture, plâtrerie, sols, isolation, dégâts des eaux. 20 ans de métier, diagnostic gratuit.
```

Signaler aussi la meta de `/degat-des-eaux-besancon`, qui se termine sur
« Diagnostic gratuit, devis conforme » — conforme à quoi ? La phrase est coupée.

---

## 12. 🟡 JSON-LD d'accueil : horaires absents, note à surveiller

Le JSON-LD de l'accueil porte bien `ratingValue 4.7` et `reviewCount 34`, mais
**aucun `openingHoursSpecification`**. Pour un artisan local, c'est la donnée
structurée qui alimente directement les résultats locaux.

**À ajouter une fois le #3 tranché** (valeurs ci-dessous à remplacer par la
plage confirmée) :

```json
"openingHoursSpecification": [
  {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "08:00",
    "closes": "18:00"
  }
]
```

**Point de vigilance sur `aggregateRating`** : la note et le nombre d'avis
proviennent de Google. Les consignes de Google sur les données structurées
d'avis excluent les avis auto-déclarés par l'entreprise sur son propre site
pour l'obtention de résultats enrichis. Le balisage n'est pas « faux » (la note
est bien affichée sur la page), mais il ne produira probablement pas d'étoiles
en SERP, et il devra être mis à jour à chaque évolution du nombre d'avis —
sinon il deviendra une donnée périmée de plus (cf. #5).

---

## 13. 🟡 Pages communes : 71 à 78 % de texte identique entre communes voisines

Mesure faite sur deux paires de pages, même service, communes différentes,
noms de communes et codes postaux neutralisés :

| Paire | Similarité caractères | Jaccard 5-grammes | Lignes identiques | Mots en blocs identiques |
|---|---|---|---|---|
| peinture-interieure : Beure vs Boussières | 87,4 % | 59,6 % | 104 / 135 | 71,3 % |
| degat-des-eaux : Beure vs Boussières | 90,7 % | 69,3 % | 130 / 154 | 78,2 % |

**Ce qui va bien, et qu'il ne faut pas casser :**

- Volume réel : 1 600 à 1 950 mots par page, ce n'est pas du contenu mince.
- Title, meta description et H1 **uniques** et qualifiés par la commune.
- **Canonical auto-référent** correct sur chaque page.
- 21 à 29 % du texte est **réellement réécrit** et raisonne sur le bâti local —
  ce n'est pas un simple remplacement de nom de commune. Exemple, pour le même
  service : « Beure est installé en fond de vallée, au bord du Doubs…
  remontées, ruissellement et sous-sols humides » contre « Boussières se trouve
  à proximité du Doubs, mais le bourg est établi en hauteur : les désordres
  d'humidité y viennent plus souvent d'une fuite intérieure ».
- Le recouvrement entre **services différents** est faible (7 % de Jaccard) :
  les gabarits de service sont bien distincts.

**Le risque réel** n'est donc pas la pénalité pour pages satellites, mais la
**sélection d'URL** : sur 76 communes par service, Google indexera une poignée
de pages par grappe et laissera les autres en « explorée, actuellement non
indexée ». Le travail de génération ne se transforme alors pas en trafic.

**Ce qui déplace l'aiguille, par ordre d'efficacité :**

1. **Concentrer** : identifier les 10 à 15 communes qui pèsent réellement
   (population, chantiers déjà réalisés, distance) et n'enrichir que celles-là,
   plutôt que d'entretenir 76 variantes par service.
2. **Différencier par le vécu** : une photo de chantier réalisée dans la
   commune, une phrase sur un chantier réel, un délai de déplacement — c'est ce
   qu'aucun concurrent ne peut générer, et c'est le signal que les moteurs
   valorisent.
3. **Varier les blocs communs** : méthode, tarifs et FAQ sont aujourd'hui
   identiques mot pour mot d'une commune à l'autre. Trois ou quatre variantes
   rédactionnelles par bloc, tirées selon la commune, feraient tomber le
   recouvrement sans réécrire quoi que ce soit à la main.
4. Suivre dans Search Console le ratio **pages indexées / pages publiées** par
   service : c'est la mesure qui dit si la stratégie fonctionne.

> À ne pas faire : mettre les pages communes en `noindex` ou les supprimer en
> masse. Elles sont correctement construites ; le sujet est leur différenciation,
> pas leur existence.

---

## Ce qui a été corrigé dans ce dépôt

Ce dépôt ne publie qu'une copie GitHub Pages, désindexée, distincte du site de
production. Les corrections suivantes y ont été faites — elles n'affectent pas
la production :

- **Ancienneté corrigée** : « plus de 10 ans » → **20 ans**, conforme à
  `/a-propos`, `llms.txt` et la page syndics.
- **Mention « Certifié RGE » retirée** de la page d'accueil de la copie, faute
  de pouvoir la vérifier (cf. #4), et remplacée par une mention vérifiée :
  conformité DTU 59.1 / 25.41.
- **Témoignages clients supprimés.** Les quatre avis signés « Marie L. »,
  « Pierre D. », « Sophie D. » et « Jean M. » provenaient du gabarit d'origine
  du dépôt et ne correspondent à aucun avis réel : publier de faux avis est une
  pratique commerciale trompeuse. Ils sont remplacés par une section
  « Engagements » qui ne s'appuie que sur des faits vérifiés.
- **Statistiques invérifiables retirées** : « 500+ projets réalisés » et
  « 100 % clients satisfaits » (cette dernière contredisant par ailleurs la note
  de 4,7/5).
- **Réalisations** : les vignettes de couleur légendées comme des chantiers
  précis (« Villa Chalezeule », « Maison Planoise ») sont requalifiées en types
  de prestations, avec un lien vers les photos réelles de `/realisations`.
- **NAP complété** : ajout de « 18 rue du Professeur Haag » dans le corps de
  page, le pied de page et le JSON-LD.
- **JSON-LD** aligné sur celui de la production (`LocalBusiness` + `Painter` +
  `HomeAndConstructionBusiness`, `@id`, SIRET, dirigeants, `priceRange` « €€ »
  au lieu de la valeur invalide « Devis gratuit »).
- **Page syndics** : son `canonical` pointait vers
  `/syndic-copropriete-besancon`, **qui renvoie un 404 en production** — la page
  n'a jamais été déployée. Le canonical, l'`og:url` et le JSON-LD pointent
  désormais vers la page équivalente en ligne,
  `/renovation-syndic-gestionnaire-besancon`. La page était par ailleurs en
  `index, follow` : elle est passée en `noindex, nofollow` comme le reste de la
  copie.
- **`robots.txt`** ajouté (`Disallow: /`) pour la copie GitHub Pages.
- **Accessibilité et confort** : lien d'évitement, `aria-expanded` et fermeture
  au clavier du menu mobile, `aria-pressed` sur les filtres, styles
  `:focus-visible`, prise en charge de `prefers-reduced-motion` (CSS et JS),
  écouteur de défilement unique throttlé en `requestAnimationFrame`.
- **Formulaire** : mention RGPD (finalité, durée de conservation, droits),
  adresse de repli affichée si aucune messagerie ne s'ouvre, attributs
  `autocomplete`.
- **Correction de bug** : le compteur animé partait en boucle infinie en
  affichant « NaN » dès qu'un élément `.stat-number` n'avait pas d'attribut
  `data-target` numérique.

**Horaires — point ouvert.** La copie affiche « Lundi – Vendredi : 8h – 18h »,
valeur retenue parce qu'elle est celle de `/contact` et de `llms.txt`. Si
l'arbitrage du #3 retient la plage du pied de page (7h – 20h30 + week-end),
il faudra la reporter ici aussi.

---

## Ordre d'exécution recommandé

Les quatre arbitrages qui bloquaient ont été rendus par Isuf le 20/08/2026
(constats #3, #4, #7, #8). Tout ce qui suit est désormais exécutable.

1. **Section 7 des mentions légales** (#1) — un seul fichier, exposition
   juridique, texte de remplacement déjà rédigé.
2. **Retirer la mention RGE** de `/isolation-besancon` (#4) — une ligne, à faire
   tout de suite ; la vérification officielle par SIRET suit et décidera d'un
   éventuel retour.
3. **`llms.txt` : 29 → 34 avis** (#5) et **sitemap vide** (#6) — deux corrections
   de dix minutes.
4. **Poser les horaires distingués** (#3) — pied de page, `/contact`, `llms.txt`,
   JSON-LD (#12), puis aligner la fiche Google Business Profile.
5. **Corriger les chaînes fautives du générateur** (#2) puis régénérer, et
   recontrôler sur un nouvel échantillon d'une quinzaine de pages.
6. **Assumer le délai 48 h dans le texte** (#8) et **republier `/ehpad-besancon`**
   avec sa 301 (#7).
7. Correctifs de détail : titre de CTA syndics (#9), `og:title` (#10), meta
   d'accueil (#11).
8. **Stratégie pages communes** (#13) — chantier de fond, à mener une fois le
   reste assaini.

## Données encore manquantes

- **Export Google Search Console** (performance 12 mois + couverture) : c'est ce
  qui permettrait de mesurer le ratio pages indexées / publiées du #13, et de
  savoir quelles communes méritent l'effort du point 1 de ce même constat.
- **Core Web Vitals** : non mesurés ici (PageSpeed Insights non accessible
  depuis cet environnement). À relever sur `/`, `/degat-des-eaux-besancon` et
  une page commune, en mobile.
- **Statut exact de la redirection** `/organic-ehpad-besancon` (301 ou 302) :
  la redirection a été constatée, son code HTTP n'a pas pu être isolé.
- **Contrôle RGE à rejouer** (#4) : le premier appel a renvoyé « aucun
  résultat » sur le SIREN, mais la requête de contrôle qui aurait validé la
  méthode n'a pas pu être exécutée. Résultat non concluant tant qu'il n'est pas
  rejoué.
- **Accès au dépôt de la production** : les corrections ci-dessus portent sur les
  fichiers du site en ligne, dont la source est le dépôt privé
  `eurotregu/rushiti-renovation` — distinct de ce dépôt-ci. Son rattachement à la
  session a été refusé par le garde-fou de permissions ; sans lui, ces
  corrections restent rédigées mais non appliquées.
