# Audit du balisage Schema.org (JSON-LD) — 31/08/2026

| | |
|---|---|
| Déclencheur | Demande d'Isuf : « auditoj Schema.org markup » |
| Périmètre | **Dépôt de production** `eurotregu/rushiti-renovation` (757 pages HTML, commit `3317674`) **+ cette copie GitHub Pages** (3 pages) |
| Méthode | Parsing JSON de **tous** les blocs `application/ld+json` des 757 pages — jamais un échantillon — puis, pour chaque nœud, confrontation au **texte visible de la même page** et à l'existence réelle des fichiers référencés. Trois vérifications live (Firecrawl) : `schema.org/HousePainter`, `schema.org/Painter`, une image d'article, la page d'accueil servie. Aucun chiffre estimé, aucune donnée SERP. |
| Livrables | ce rapport · `korrigjime-prodhim/verifiko_schema_org.py` (outil de régression) · les deux pages de cette copie corrigées et servant de gabarit de référence |
| **Statut** | **Base saine, 3 constats bloquants à corriger en production** |

---

## Réponse courte

Le socle est bon : **758 blocs JSON-LD, zéro erreur de syntaxe**, une entité
entreprise unique (`#business`) identique sur 743 pages, NAP au caractère près,
téléphone en E.164 partout, fil d'Ariane valide sur 748 pages. La correction
`sameAs` du 22/08 est bien en production : 741 pages portent les 7 profils
vérifiés.

Ce qui ne va pas tient en trois points, tous systémiques parce qu'ils viennent
des gabarits :

1. **766 questions FAQ sont balisées mais ne s'affichent nulle part sur la
   page** — Google interdit explicitement le contenu qui ne vit que dans le
   JSON-LD ;
2. **`zones-intervention.html` déclare une note 4,7/34 alors que la page
   n'affiche ni note ni avis** — et la page d'accueil balise une
   `aggregateRating` que la doctrine maison du 22/08 avait justement écartée ;
3. **15 URL d'images déclarées en JSON-LD renvoient un 404**, dont l'image de
   9 des 11 articles de blog.

Aucun de ces points ne relève d'une donnée inventée : la note 4,7/34 est réelle,
datée et affichée sur la page d'accueil. Ce sont des écarts de conformité et de
cohérence, pas des fabrications.

---

## 1. État des lieux chiffré (production, 757 pages)

| Mesure | Valeur |
|---|---|
| Pages HTML | 757 |
| Pages portant du JSON-LD | 756 (seule `404.html` n'en a pas — normal) |
| Blocs `application/ld+json` | 758 |
| **Erreurs de syntaxe JSON** | **0** |
| Nœuds `LocalBusiness` / `HousePainter` | 743 / 742 |
| Nœuds `BreadcrumbList` | 748, **toutes positions séquentielles, toutes URL absolues HTTPS** |
| Pages portant une `FAQPage` | 746 (4 260 questions balisées) |
| Nœuds `Service` de premier niveau | 735 (610 `Service` supplémentaires imbriqués dans des `Offer` — usage correct) |
| `@id` entreprise `https://rushiti-renovation.fr/#business` | 743 nœuds, **aucune variante** |
| `telephone` | `+33760279897` sur 743 nœuds, **aucun format local** |
| `streetAddress` / `addressLocality` | `18 rue du Professeur Haag` / `Besançon` sur 741 nœuds, **aucune variante** |
| `sameAs` avec les 7 profils vérifiés | 741 pages |
| Horaires | identiques sur 739 pages (Lun–Ven 07:00–20:30, Sam 08:00–20:30, Dim 09:00–17:30) et **conformes à ceux affichés** |

Ce tableau dit l'essentiel : le travail de fond fait en août a tenu. Les
constats qui suivent portent sur ce qui n'a jamais été contrôlé.

---

## 2. Constats bloquants (P1)

### P1-1 — 766 questions FAQ balisées mais invisibles sur la page

Google : le contenu d'une `FAQPage` doit être **visible par le visiteur** sur la
page qui le balise. Du contenu qui n'existe que dans le JSON-LD est une
violation des règles relatives aux données structurées, sanctionnable par une
action manuelle.

Sur les 4 260 questions balisées, **766 n'apparaissent nulle part dans le texte
de la page**, et **99 réponses supplémentaires diffèrent du texte affiché**.

| Famille de pages | Pages | Questions balisées | Questions invisibles | Réponses divergentes |
|---|---:|---:|---:|---:|
| `degat-des-eaux-*` | 76 | 321 | 126 | 82 |
| `peinture-*` | 115 | 553 | 92 | 17 |
| `isolation-*` | 93 | 571 | 91 | 0 |
| `revetements-sol-*` | 76 | 462 | 75 | 0 |
| `platrerie-*` | 76 | 462 | 75 | 0 |
| autres grilles (ratissage, cloisons, papier peint, faux plafond…) | 300 | 1 856 | 278 | 0 |
| **`blog/`** | **10** | **35** | **29** | 0 |
| **Total** | **746** | **4 260** | **766** | **99** |

Deux mécaniques différentes, deux correctifs différents.

**a) Les grilles locales : une question fantôme par page.** Le gabarit ajoute au
JSON-LD une question de zone qui n'est jamais rendue en HTML.

> `platrerie-deluz.html` — balisées : 6 questions. Affichées : 5.
> La question **« Vous déplacez-vous à Deluz ? »** n'existe que dans le JSON-LD.
> Variante quartier : « Intervenez-vous dans le quartier Velotte ? »
> (`doublage-murs-velotte.html`), etc.

**b) Le blog : la FAQ entière est invisible.** Les 10 articles concernés
balisent 3 à 5 questions chacun sans qu'aucune section FAQ ne soit rendue — ni
en `<details>`, ni en accordéon, ni en texte.

> `blog/degat-des-eaux-assurance-qui-paie-quoi.html` — 3 questions balisées
> (« Dans quel délai déclarer un dégât des eaux à l'assurance ? »…),
> 0 affichée. Aucune balise `<details>` ni `<summary>` dans la page.

**c) Les 99 réponses divergentes** sont des micro-écarts de rédaction entre le
JSON-LD et le texte : la page a été retouchée, pas le balisage.

> `degat-des-eaux-mazerolles-le-salin.html` (et 74 autres pages `degat-*`)
> JSON-LD : « Une auréole **au plafond** ou une plinthe gonflée… »
> Page : « Une auréole ou une plinthe gonflée… »

**Correctif.** Deux options par famille : rendre visible la question manquante
(la meilleure — « Vous déplacez-vous à X ? » est une vraie question client), ou
la retirer du JSON-LD. Pour le blog, publier la section FAQ dans le corps de
l'article : le contenu existe déjà, il est simplement absent du HTML. Pour les
99 réponses, régénérer le JSON-LD depuis le texte affiché, jamais l'inverse.

### P1-2 — Note et avis balisés sur une page qui n'en affiche aucun

Deux pages portent `aggregateRating` 4,7/34 :

| Page | Note affichée sur la page ? | Avis affichés ? | Verdict |
|---|---|---|---|
| `index.html` | Oui — « 4,7 / 5 ★★★★★ · 34 avis Google » | Oui, 3 avis, **texte identique au balisage** | Conforme sur le fond, contraire à la doctrine (voir plus bas) |
| `zones-intervention.html` | **Non** | **Non** | **Violation** : note balisée, invisible sur la page |

`zones-intervention.html` doit perdre son `aggregateRating` : baliser une note
qu'aucun visiteur ne voit sur cette page est exactement ce que Google
interdit.

La page d'accueil pose une autre question, de cohérence interne. Le relevé du
22/08 (`avis-google-releve-2026-08-22.md`) fixe la règle : *« Pas
d'`aggregateRating` en JSON-LD. Les avis Google sont des avis tiers […] La note
est citée en texte et datée. »* Cette copie GitHub Pages porte même le
commentaire HTML qui l'explique. **La production fait l'inverse.** Et l'
`aggregateRating` déposée là n'apporte rien : depuis 2019, Google ignore les
avis qu'une entreprise héberge sur son propre site à son propre sujet
(*self-serving reviews*) — aucune étoile ne sortira dans la SERP.

Détails secondaires sur les 3 `Review` de l'accueil : ni `datePublished`, ni
`publisher` (« Google »), et les 3 notes sont à 5/5 alors que la moyenne
déclarée est 4,7 — un échantillon des meilleurs avis.

> **Décision à arbitrer par Isuf** : soit la production s'aligne sur la doctrine
> (retrait de `aggregateRating` et `review` des deux pages, la note reste citée
> en texte et datée), soit la doctrine est révisée et le relevé du 22/08 mis à
> jour. Recommandation : **s'aligner sur la doctrine** — le balisage ne rapporte
> rien ici, et deux règles contradictoires dans deux dépôts finiront par
> ressortir dans un autre audit.

### P1-3 — 15 images déclarées en JSON-LD renvoient un 404

Vérifié fichier par fichier dans le dépôt de production, puis en ligne :
`https://rushiti-renovation.fr/assets/blog/degat-des-eaux-assurance-qui-paie-quoi.jpg`
→ **404** (page d'erreur servie).

| Fichier manquant | Déclaré par |
|---|---|
| `assets/blog/*.jpg` — 9 fichiers (le dossier `assets/blog/` **n'existe pas**) | 9 des 11 articles, en `BlogPosting.image` |
| `assets/realisations/doublage-placo-2.jpg`, `faux-plafond-dalles.jpg`, `faux-plafond-suspendu.jpg`, `papier-peint-escalier.jpg`, `salle-de-bain-1.jpg`, `salle-de-bain-2.jpg` | `realisations.html`, en `ImageObject` |

Conséquence : `image` est une propriété requise du rich result Article — ces 9
articles en sont exclus, et une image déclarée qui n'existe pas est un signal de
qualité négatif. Correctif : publier les visuels, ou retirer la propriété
`image` tant qu'ils n'existent pas. Ne pas laisser une URL qui ment.

---

## 3. Constats importants (P2)

### P2-1 — `legalName` : « RUSHITI Rénovation » sur 150 pages

`legalName` désigne la **dénomination sociale**, pas le nom commercial. Or
`CLAUDE.md` est explicite : nom commercial **RUSHITI Rénovation**, dénomination
sociale **Rushiti**, SARL. Les 150 pages qui déclarent
`"legalName": "RUSHITI Rénovation"` déclarent donc le nom commercial deux fois
(`name` et `legalName`) et la dénomination sociale nulle part.

À confirmer sur le K-bis avant correction — c'est une donnée d'identité, elle ne
se corrige pas au jugé. Même remarque pour le fichier de défauts du skill
`schema-builder`, qui porte la même valeur.

### P2-2 — `addressRegion` : deux pages en écart

738 pages déclarent `"addressRegion": "Bourgogne-Franche-Comté"` (correct : en
France, la division administrative de premier niveau est la région).
**`index.html` et `a-propos.html` déclarent `"Doubs"`**, qui est le département.
Les deux pages les plus visitées du site sont les deux qui portent l'écart.

### P2-3 — Le blog est détaché de l'entité entreprise

Sur les ~40 pages du blog et assimilées :

- le `publisher` est un `Organization` **sans `@id`** → 40 nœuds anonymes que
  rien ne relie à `https://rushiti-renovation.fr/#business` ;
- aucun nœud `LocalBusiness` : 42 pages sans `sameAs`, 43 sans `url`, 40 sans
  `telephone` ni adresse.

Pour un moteur — et plus encore pour un moteur de réponse qui cherche à
consolider une entité avant de la citer — le blog raconte donc une entreprise
distincte du reste du site. Correctif à coût nul : donner au `publisher`
l'`@id` canonique, `{"@id": "https://rushiti-renovation.fr/#business"}`, plutôt
qu'un bloc dupliqué.

### P2-4 — `mentions-legales.html` ne déclare aucune identité

Le seul nœud de la page est `{"@type": "WebPage", "name": ..., "url": ...}`.
La page qui porte SIRET, forme juridique et représentant légal est la seule à ne
rien en dire en données structurées. C'est la page à baliser en priorité pour
l'E-E-A-T : y placer le `LocalBusiness` complet avec `taxID`, `vatID` et
`founder`.

### P2-5 — Le gabarit enrichi n'est présent que sur ~20 % des pages

| Propriété | Pages qui la portent (sur 756) |
|---|---:|
| `priceRange` | 739 |
| `taxID` (SIRET) | 738 |
| `foundingDate`, `legalName`, `slogan`, `hasOfferCatalog` | ~150 |
| **`vatID`** (TVA FR89905214631) | **3** |
| **`knowsAbout`** | **3** |

`vatID` et `knowsAbout` sont deux des signaux les plus utiles pour la
consolidation d'entité. Les porter partout ne coûte qu'une régénération de
gabarit.

---

## 4. Constats mineurs (P3)

- **`Service` sans `url`** : 733 des 735 nœuds `Service` de premier niveau. La
  page reste identifiée grâce à l'`@id` (`…/cloisons-besancon#service`), donc ce
  n'est pas bloquant — mais `url` est gratuit et lève toute ambiguïté.
- **`geo`** : 735 pages portent `47.238, 6.0243`, soit le centre de Besançon, pas
  le 18 rue du Professeur Haag. Une page porte `47.245638, 6.00556`. À unifier
  sur les coordonnées réelles de l'adresse.
- **Nœuds de page** : 2 nœuds `WebSite` et 7 nœuds `WebPage` sur 757 pages. Un
  `WebSite` unique référencé en `isPartOf` structurerait le graphe.
- **`zones-intervention.html`** découpe son balisage en 3 blocs `<script>`
  séparés. Un seul `@graph` est préférable (parsing unique, références croisées
  par `@id`).

---

## 5. Ce qui est sain — à ne pas casser

- **0 erreur de syntaxe** sur 758 blocs. C'est rare sur un site de cette taille.
- **`BreadcrumbList` sur 748 pages**, toutes conformes. C'est le rich result le
  plus régulièrement affiché par Google : le principal levier d'affichage enrichi
  du site est déjà en place et correct.
- **NAP irréprochable en JSON-LD** : une seule `@id`, un seul téléphone au format
  E.164, une seule adresse, des horaires identiques partout et conformes à
  l'affichage.
- **`sameAs`** : les 7 profils vérifiés le 22/08 (PagesJaunes, Google Maps,
  Annuaire des Entreprises, INPI, Facebook, Instagram, rushiti.fr) sont en place
  sur 741 pages. Le constat rouge de l'audit du 22/08 est refermé.
- **`HousePainter` est le bon type.** Vérifié en direct : `schema.org/HousePainter`
  répond 200 (`Thing > Organization > LocalBusiness > HomeAndConstructionBusiness
  > HousePainter`), **`schema.org/Painter` répond 404**. Le site a raison ; c'est
  la référence du skill `schema-builder` qui se trompe (`references/local-business.md`
  affirme que `Painter` existe, et `references/rushiti-defaults.md` l'utilise dans
  le bloc à copier tel quel). **À corriger côté skill** : un `@type` inexistant
  ferait ignorer le nœud entier sur toute page future.
- **Les articles de blog sont bien balisés** : `headline`, `datePublished`,
  `dateModified`, `author` (Person + jobTitle), `publisher`, `mainEntityOfPage`.
  Il ne leur manque que l'image (P1-3) et le rattachement d'entité (P2-3).

---

## 6. Ce qui est livré dans cette PR

**`korrigjime-prodhim/verifiko_schema_org.py`** — outil de régression, à lancer
avant chaque déploiement. Complète `verifiko_sameas.py` (qui couvre `@id`,
`sameAs`, horaires) en contrôlant les cinq points ci-dessus :

```bash
python3 docs/seo/korrigjime-prodhim/verifiko_schema_org.py /chemin/vers/rushiti-renovation
```

Sortie actuelle sur la production :

```
Faqe me JSON-LD: 756

PËRMBLEDHJE:
     766  pyetje e balisuar por e padukshme
      99  përgjigje që ndryshon nga teksti i faqes
      15  imazh i deklaruar që s'ekziston
       2  aggregateRating mbi biznesin
       1  review mbi biznesin
```

Sortie sur cette copie après correction : `✔ Konform` (code de sortie 0).

**Les deux pages de cette copie corrigées**, qui servent désormais de gabarit de
référence pour la production :

| Correction | `index.html` | `syndic-copropriete-besancon.html` |
|---|---|---|
| `addressRegion` → `Bourgogne-Franche-Comté` | ✔ | déjà correct |
| `areaServed` en objets `City` / `AdministrativeArea` (au lieu de chaînes) | ✔ | déjà correct |
| `geo`, `hasMap`, `priceRange` | ✔ | ✔ |
| `taxID`, `vatID`, `identifier` (SIRET) | ✔ | `vatID` ajouté |
| `founder`, `foundingDate`, `knowsAbout` | ✔ | ✔ |
| `description` sur le nœud entreprise | ✔ | ✔ |
| Horaires | déjà présents | ✔ ajoutés |
| Nœud `WebSite` + nœud de page (`WebPage` / `FAQPage` avec `@id`, `url`, `isPartOf`, `about`, `breadcrumb`) | ✔ | ✔ |
| `url` sur le nœud `Service` | — | ✔ |
| Passage en `@graph` unique | ✔ | déjà en `@graph` |
| `aggregateRating` / `review` | **non ajoutés** (doctrine) | — |

Les 7 questions de la FAQ syndic restent vérifiées mot pour mot contre le texte
affiché : 7 balisées, 7 visibles.

---

## 7. Ordre de marche proposé pour la production

| # | Action | Où | Effort |
|---|---|---|---|
| 1 | Retirer `aggregateRating` de `zones-intervention.html` | 1 page | 5 min |
| 2 | Arbitrer la doctrine avis, puis aligner `index.html` | 1 page | décision d'Isuf |
| 3 | Retirer la propriété `image` des 9 articles sans visuel, ou publier les visuels | 9 + 1 pages | selon l'option |
| 4 | Publier la section FAQ des 10 articles de blog (le contenu existe déjà dans le JSON-LD) | 10 pages | rédactionnel |
| 5 | Afficher la question de zone des grilles, ou la retirer du gabarit | ~736 pages | 1 passe de gabarit |
| 6 | Régénérer les 99 réponses divergentes depuis le texte affiché | 99 items | 1 passe de gabarit |
| 7 | `addressRegion` sur `index.html` et `a-propos.html` | 2 pages | 5 min |
| 8 | `publisher` du blog → `{"@id": "…/#business"}` | ~40 pages | 1 passe |
| 9 | `LocalBusiness` complet sur `mentions-legales.html` | 1 page | 15 min |
| 10 | `vatID` + `knowsAbout` généralisés, `url` sur les `Service`, `geo` unifié | gabarits | 1 passe |

Étapes 1, 3, 7 et 9 sont des correctifs ponctuels ; 5, 6, 8 et 10 relèvent d'une
passe de gabarit unique, à valider par `verifiko_schema_org.py` avant push.

---

## 8. À valider par Isuf

- [ ] **Doctrine avis** : retrait de `aggregateRating`/`review` en production, ou
      révision du relevé du 22/08 ?
- [ ] **Dénomination sociale exacte** au K-bis, pour `legalName` (« Rushiti » ?).
- [ ] **Coordonnées GPS exactes** du 18 rue du Professeur Haag, pour remplacer
      l'approximation « centre de Besançon » sur 735 pages.
- [ ] **Visuels des 9 articles de blog** : à produire, ou propriété `image`
      retirée en attendant ?
- [ ] **Question de zone des grilles** : à afficher sur la page, ou à retirer du
      balisage ?
- [ ] Correction du skill `schema-builder` (`Painter` → `HousePainter` dans
      `references/local-business.md` et `references/rushiti-defaults.md`) — ces
      fichiers vivent côté claude.ai, hors de ce dépôt.

---

## 9. Test

Les blocs corrigés de cette copie ont été validés par parsing JSON strict et par
confrontation au texte affiché. Le contrôle final se fait sur l'URL en ligne,
après déploiement :

<https://search.google.com/test/rich-results>

Aucun classement n'est promis dans ce rapport : les correctifs P1 lèvent des
risques de conformité et rendent les pages éligibles, ils ne garantissent aucun
affichage.

---

## 10. Suite donnée — paquet 7 (02/09/2026)

Les six actions du §7 qui ne demandent aucun arbitrage sont désormais
outillées : `korrigjime-prodhim/fix_schema_org.py` couvre les points 1, 6, 7,
8, 9 et 10 (hors `geo`, qui attend les coordonnées réelles).

Testé sur une copie du checkout de production `b7e42cb` : **755 fichiers**,
idempotence prouvée, 758 blocs JSON-LD toujours valides, **texte visible
identique bit pour bit**, aucun fichier touché hors JSON-LD, et les cinq
autres outils de régression du dépôt inchangés (exit 0 avant et après). Les
99 réponses divergentes tombent à 0.

Le script **ne touche pas `index.html`** : la note y est affichée, donc le
sujet n'est pas la conformité mais la doctrine du 22/08 — point 2 du §8,
qui reste à arbitrer, comme les cinq autres.

Détail, journal de test et mode d'emploi : `korrigjime-prodhim/README.md`,
section « Paketa 7 ».
