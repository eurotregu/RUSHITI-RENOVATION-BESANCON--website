# Ce qui a été produit et n'est pas en ligne — contrôle du 02/09/2026

| | |
|---|---|
| Déclencheur | Demande d'Isuf : « kontrollo çka është prodhuar dhe nuk është vendosur/aktivizuar online » |
| Méthode | Contrôle par exécution, pas par lecture : les 8 correctifs relancés **en simulation sur la production à jour** (`19079d8`) — 0 fichier à modifier = déjà en ligne ; les 6 vérificateurs passés ; chaque contenu produit cherché dans les 757 pages ; les 30 PR de production et les 27 PR du dépôt vitrine confrontées à l'état réel. |

---

## 1. Ce qui est bien en ligne — vérifié, pas supposé

**Les 8 paquets de correctifs sont tous appliqués.** Relancés en simulation sur
la production, ils annoncent tous **0 fichier à modifier** :

| Paquet | Simulation sur la production |
|---|---|
| 1 · papier peint | 0/40 fichier |
| 2 · formulaires Demande rapide | 0 |
| 3 · `sameAs` LocalBusiness | 0 |
| 4 · silo dégât des eaux | 0 |
| 5 · horaires NAP | 0 |
| 7 · Schema.org sans arbitrage | 0 |
| 8 · FAQ visible (`--afisho`) | 0 |

Cinq vérificateurs sur six sortent en **0** (papier peint, demande rapide,
`sameAs`, dégât des eaux, horaires NAP). Le sixième, `verifiko_schema_org`,
signale exactement les 17 constats en attente d'arbitrage — voir §4.

**Les contenus rédigés sont publiés** : l'enrichissement « malgré la VMC » de
l'article moisissure est en ligne ; la FAQ de `reparer-plafond-degat-des-eaux`
affiche ses 6 questions ; le bloc « méthode de calcul » du simulateur est en
place.

**Les 30 PR du dépôt de production ont toutes été fusionnées** — aucune fermée
sans l'être. Rien n'a été perdu de ce côté.

**Le retrait de la réécriture `addressRegion`** est déployé et vérifié en
direct (02/09, 15:58 UTC).

---

## 2. Produit, testé, prêt — et jamais mis en ligne

### 2.1 Twitter Cards — ⚠️ classement révisé le 02/09 (voir addendum §8)

**726 pages sur 757 n'ont aucune `twitter:card`.** Compté sur la production
à l'instant : 31 pages sur 757 en portent une.

La PR [#61](https://github.com/eurotregu/RUSHITI-RENOVATION-BESANCON--website/pull/61)
(31/08) contient l'audit, le script de correctif **et** son vérificateur de
régression. Le script dérive `twitter:title`, `twitter:description` et
`twitter:image` des `og:*` de chaque page — **aucun texte inventé** — et
corrige au passage 18 dimensions d'image fausses.

C'est le seul paquet outillé et testé qui n'a jamais été appliqué.

### 2.2 Contenu rédactionnel pour la page pilier peinture

La PR [#19](https://github.com/eurotregu/RUSHITI-RENOVATION-BESANCON--website/pull/19)
(14/08) ajoute **53 lignes** à `peinture-interieure-besancon.html` — la page
pilier du silo peinture. Trois sections vérifiées **absentes de la production** :

- « Pourquoi votre peinture cloque, farine ou jaunit »
- « Quatre étapes, et un mur qui tient »
- « Dans quels cas nous intervenons à Besançon et dans le Doubs »

(La quatrième, « Pourquoi RUSHITI Rénovation », existe déjà en ligne.)

⚠️ La branche part du 14/08 : le contenu est bon, mais il doit être **réextrait
sur `main` à jour**, pas fusionné tel quel.

### 2.3 Pages et outils jamais créés en production

| PR | Livrable | État |
|---|---|---|
| [#10](https://github.com/eurotregu/RUSHITI-RENOVATION-BESANCON--website/pull/10) | Outil de diagnostic dégât des eaux en 5 questions | `diagnostic-degat-des-eaux.html` **n'existe pas** en production |
| [#9](https://github.com/eurotregu/RUSHITI-RENOVATION-BESANCON--website/pull/9) | Pages `renovation-pontarlier`, `renovation-valdahon` | **n'existent pas** — ⚠️ et la production couvre déjà Pontarlier par service (cloisons, dégât des eaux, isolation, papier peint, faux plafonds) : risque de cannibalisation, à passer par `rushiti-keyword-map` |

---

## 3. Produit, mais dont l'activation ne dépend pas du code

| PR | Livrable | Ce qui manque |
|---|---|---|
| [#62](https://github.com/eurotregu/RUSHITI-RENOVATION-BESANCON--website/pull/62) | Plan Google Ads 300–500 €/mois, guide des exclusions, 237 mots-clés négatifs | Le lancement d'une campagne — hors dépôt, je ne peux pas vérifier d'ici si elle tourne |
| [#63](https://github.com/eurotregu/RUSHITI-RENOVATION-BESANCON--website/pull/63) | Relevé part de voix IA de septembre | Vos copier-coller des réponses IA : la grille est intégralement **NM**, jamais comptée 0 |
| [#59](https://github.com/eurotregu/RUSHITI-RENOVATION-BESANCON--website/pull/59) | Passe noindex, 85 pages | Rien à appliquer : **0 page en noindex** en production, c'est un rapport d'analyse |

---

## 4. Bloqué par un arbitrage — le code est prêt, la décision manque

| Sujet | Ce qui reste | Décision attendue |
|---|---|---|
| 15 images déclarées inexistantes | dossier `assets/blog/` absent, 9 articles concernés | produire les visuels, ou retirer la propriété `image` |
| `aggregateRating` + `review` sur `index.html` | 2 des 17 constats | aligner sur la doctrine du 22/08, ou réviser la doctrine |
| `legalName` | absent partout, volontairement | la dénomination exacte au K-bis |
| `geo` | 735 pages sur le centre de Besançon | les coordonnées du 18 rue du Professeur Haag |

---

## 5. Corrections ponctuelles à récupérer, indépendamment de leur PR

- **NF DTU 53.12** (sols souples collés) — correction de norme dans la
  PR [#41](https://github.com/eurotregu/RUSHITI-RENOVATION-BESANCON--website/pull/41),
  à récupérer même si le reste de la PR est périmé ;
- **`schema-builder`** côté claude.ai : `@type: "Painter"` n'existe pas dans
  schema.org (404 ; `HousePainter` répond 200). Un `@type` inexistant fait
  ignorer le nœud entier. Les 6 skills versionnés ici portent déjà le bon type.

---

## 6. Skills produits, non versionnés ici

- **Doublons** (le skill tourne déjà côté claude.ai) : PR #14 `rushiti-gsc`,
  #13 `rushiti-h1-h6`, #12 `rushiti-google-ads`, #11 `rushiti-devis-assurance` ;
- **Inexistants ailleurs, à trancher** : #15 `rushiti-position-marche`,
  #1 `rushiti-topic-research`, #3 `rushiti-liste-prospection` + `rushiti-meta-ads`,
  #5 `rushiti-meta-ads-b2c`, #19 `rushiti-copywriting`, #42 `rushiti-seo-engine` ;
- **#29** : correctifs de routage de 10 skills, base du 21/08 — à revérifier,
  les skills ont évolué depuis.

Détail et recommandation par PR : `tri-pull-requests-2026-09-02.md`.

---

## 7. Par ordre de valeur

1. ~~**Twitter Cards** — 726 pages.~~ **Rétrogradé** : voir l'addendum §8.
   Les 18 dimensions fausses ont été corrigées le 02/09 ; le reste du paquet
   n'apporte rien de visible sur les canaux réels de RUSHITI.
2. **Les 3 sections de la page pilier peinture** — contenu déjà rédigé pour
   une page commerciale de tête, à réextraire sur `main`.
3. **Les 4 arbitrages** (§4) — ils débloquent les 17 derniers constats de
   l'audit Schema.org.
4. **Le relevé part de voix IA** — il ne tient qu'à vos copier-coller.
5. **Les pages Pontarlier/Valdahon et l'outil diagnostic** — décisions de
   contenu, à passer par la porte anti-cannibalisation.


---

## 8. Addendum du 02/09 — classement révisé, et ce qui a été fait depuis

**Je m'étais trompé de hiérarchie.** Le §2.1 classait les Twitter Cards en
tête « par ordre de valeur ». C'était exact au sens « seul paquet outillé
jamais appliqué », mais trompeur sur l'intérêt réel. Les faits, vérifiés sur
la production :

| | |
|---|---|
| Pages avec Open Graph (`og:title`) | **756 / 757** |
| Pages avec `twitter:card` | 31 / 757 |
| Compte X / Twitter de RUSHITI | **aucun** — Facebook, Instagram, Google, PagesJaunes |

Open Graph est ce que lisent Facebook, Instagram, WhatsApp et LinkedIn, et il
est déjà partout. Les balises `twitter:*` n'auraient donc rien changé de
visible sur les canaux réellement utilisés.

### Ce qui avait une vraie valeur dans ce paquet, et qui est fait

Sur arbitrage d'Isuf, le correctif a été **limité aux dimensions déclarées** :
PR de production [#32](https://github.com/eurotregu/rushiti-renovation/pull/32),
**18 fichiers**.

Le script a reçu pour cela une option `--vetem-permasat` qui saute le bloc des
balises twitter — sans elle il touchait 756 pages, avec elle exactement les 18.

Deux familles de défauts corrigées :

- **inversions portrait / paysage** : `amenagement-commerce-bureau` annonçait
  1104×828 pour une image de 828×1104 ; `cloisons-besancon` et
  `degat-des-eaux-besancon` annonçaient 900×1200 pour 828×1104 ;
- **écarts francs** : sept pages annonçaient 1104×828 pour une image de
  413×224, dont `renovation-syndic-gestionnaire`, `expert-assurance-sinistre`
  et `prix-travaux-renovation`.

Preuves : idempotence (2ᵉ passe, 0 fichier), texte visible identique sur les
757 pages, **aucune balise `twitter:` ajoutée**, comparaison clé par clé ne
montrant que `og:image:width` et `og:image:height` — 18 fois chacune. Les cinq
outils de régression antérieurs : exit 0.

### Ce qui reste, et qui n'est pas automatisable

**Trois pages sans image sociale** — `blog.html`, `contact.html`,
`mentions-legales.html`. Le script les signale mais n'y touche pas : choisir
un visuel est une décision d'Isuf.

**Sept images trop petites.** Corriger une dimension la rend exacte, pas plus
grande : une image de 413×224 restera affichée en petite vignette, en dessous
du minimum d'une grande carte sociale. Pour un aperçu pleine largeur sur
WhatsApp ou Facebook, il faudrait des visuels d'environ 1200×630 sur ces
pages — production d'images, pas balisage.

### Conséquence sur la PR #61

Le fichier `fix_twitter_cards.py` versionné ici porte désormais l'option
`--vetem-permasat`. La PR #61 reste utile pour son audit
(`audit-twitter-cards-2026-08-31.md`) et son vérificateur, mais sa version du
script est antérieure : en cas de fusion, garder celle-ci.

### Classement révisé de ce qui dort

1. **Les 3 sections rédigées pour la page pilier peinture** (§2.2) — contenu
   commercial déjà écrit, sur une page de tête, absent du site.
2. **Les 4 arbitrages** (§4) — ils débloquent les 17 derniers constats.
3. **Les visuels sociaux** — 3 pages sans image, 7 images sous-dimensionnées.
4. **Le relevé part de voix IA** — il ne tient qu'aux copier-coller d'Isuf.
5. **Les pages Pontarlier/Valdahon et l'outil diagnostic** — décisions de
   contenu, sous porte anti-cannibalisation.
6. **Les balises twitter restantes** — propreté technique, gain non visible
   tant que RUSHITI n'est pas sur X.
