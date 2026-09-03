# Tri des 29 pull requests ouvertes — 02/09/2026

| | |
|---|---|
| Déclencheur | 29 PR ouvertes, dont 22 brouillons d'août jamais tranchés |
| Méthode | Pour chaque PR : différentiel réel contre `main` (`git diff main...branche`), date du point de départ, fichiers touchés, puis confrontation à l'état actuel du dépôt **et** du dépôt de production. Aucun verdict pris sur le titre seul. |
| **Constat le plus important** | La copie GitHub Pages annonçait **« plus de 10 ans d'expérience »** alors que la production annonce **20 ans**. Corrigé dans cette PR. |

---

## Pourquoi ce tri

Une PR ouverte n'est pas neutre : elle contient un diff figé à sa date de
création. Plus `main` avance, plus ce diff devient un piège — fusionner en
septembre une branche partie du 2 août peut réécrire des pages que trois
paquets de correctifs ont entre-temps mises à niveau.

**Onze PR touchent `index.html` ou `css/style.css`.** Quatre partent d'août.
C'est là que se trouve le risque réel, pas dans le nombre de PR.

---

## 1. Le constat qui ne pouvait pas attendre

`index.html` de cette copie affichait, à trois endroits :

> « Peinture, aménagement intérieur et rénovation complète. **Plus de 10 ans
> d'expérience** au service de votre habitat. »
> Compteur animé : `data-target="10"` — « 10+ Ans d'Expérience »
> « **Avec plus de 10 ans d'expérience**, nous intervenons auprès des
> particuliers comme des professionnels… »

Or **les 757 pages de production annoncent « 20 ans d'expérience »**, jamais
« 10 ans » — vérifié fichier par fichier. Et le workflow `deploy.yml` publie
cette copie sur GitHub Pages à chaque push sur `main` : la page était donc
publique, avec la moitié de l'expérience réelle d'Isuf et Yll.

La PR **#8** (8 août) corrigeait exactement cela. Elle est restée en brouillon
un mois.

**Corrigé ici**, sur le libellé exact de la production (« 20 ans d'expérience »,
sans « plus de »), compteur inclus. Ce n'est pas un arbitrage : c'est aligner
la copie sur une donnée déjà publiée et déjà validée.

---

## 2. Les trois PR à fermer

| PR | Titre | Pourquoi la fermer |
|---|---|---|
| **#51** | *addressRegion unifié sur « Doubs » + SIRET sur l'accueil* | **Ferait régresser le balisage.** L'audit du 31/08 établit qu'en France la division administrative de premier niveau est la **région** : la bonne valeur est « Bourgogne-Franche-Comté », que `main` porte déjà. Son second apport, le SIRET sur l'accueil, est lui aussi déjà en `main`. Il ne reste que la régression. |
| **#8** | *Unifie l'expérience à 20 ans sur la page d'accueil* | **Absorbée** : son contenu est appliqué dans la présente PR, sur le libellé de la production plutôt que celui d'août. |
| **#45** | *Diagnostic des 212 pages « Introuvable (404) »* | **Périmée** : la passe 404 du 31/08 (`passe-404-gsc-2026-08-31.md`, déjà en `main`) reprend le même export GSC de 212 URL et le solde — 202 déjà en 301 via le Worker, 10 résiduels légitimes. Le diagnostic du 24/08 est l'état antérieur de la même analyse. |

---

## 3. Les six PR à fusionner sans risque

Documentation seule ou base à jour, aucun conflit, aucune page vivante remise
en cause.

| PR | Titre | Nature |
|---|---|---|
| **#65** | Paquet 8 — les 766 questions FAQ invisibles | Script + doc |
| **#63** | Relevé part de voix IA de septembre | Grille + protocole (attend vos relevés, mais le protocole est utilisable tel quel) |
| **#62** | Google Ads : plan de compte, 237 négatifs | `docs/ads/` seulement |
| **#61** | Twitter Cards : 726 pages sans carte | Base du 02/09, donc à jour ; touche les 2 pages vivantes sans conflit |
| **#59** | Passe noindex : 85 pages commerciales | Doc seulement |
| **#50** | Journal : point 7 soldé | Doc seulement |

---

## 4. Les quatre PR de skills devenus inutiles

Ces PR ajoutent au dépôt un skill **qui tourne déjà côté claude.ai**. Les
fusionner créerait une seconde version, appelée à diverger de celle qui sert
réellement.

| PR | Skill ajouté | Statut réel |
|---|---|---|
| **#14** | `rushiti-gsc` | actif côté claude.ai |
| **#13** | `rushiti-h1-h6` | actif côté claude.ai |
| **#12** | `rushiti-google-ads` | actif côté claude.ai |
| **#11** | `rushiti-devis-assurance` | actif côté claude.ai |

Recommandation : **fermer les quatre**, en gardant la règle du `CLAUDE.md` —
seuls 6 skills SEO sont versionnés ici, le reste vit côté claude.ai. Si vous
voulez au contraire tout versionner, c'est une décision d'architecture à
prendre une fois pour toutes, pas PR par PR.

---

## 5. Les cinq PR de skills qui n'existent nulle part

Contrairement aux précédentes, ces skills **n'existent ni ici ni côté
claude.ai**. La question n'est donc pas technique : les voulez-vous ?

| PR | Skill proposé | Recouvrement avec l'existant |
|---|---|---|
| **#15** | `rushiti-position-marche` | aucun skill ne couvre le positionnement de marché |
| **#1** | `rushiti-topic-research` | recouvre `rushiti-keyword-clusters` et `rushiti-brief-seo` |
| **#3** | `rushiti-liste-prospection` + `rushiti-meta-ads` | prospection déjà couverte par `rushiti-prospection-b2b` ; Meta Ads, non |
| **#5** | `rushiti-meta-ads-b2c` | doublon partiel du précédent |
| **#19** | `rushiti-copywriting` | recouvre `rushiti-humanisateur` et `rushiti-architecte-seo` |

Recommandation : **ne garder que ce qui manque vraiment** — Meta Ads (#3 ou #5,
pas les deux) et éventuellement le positionnement de marché (#15). Fermer #1
et #19, dont le terrain est déjà occupé.

⚠️ **#5 et #19 touchent aussi `index.html`** depuis une base du 2 août et du
14 août. À ne pas fusionner en l'état, même si vous voulez le skill : il
faudrait le réextraire sur `main` à jour.

---

## 6. Les six PR à risque — à ne pas fusionner en l'état

Toutes partent d'une base ancienne et touchent des pages vivantes. Leur diff
s'appliquerait par-dessus trois paquets de correctifs postérieurs.

| PR | Base | Ce qu'elle réécrirait | Verdict |
|---|---|---|---|
| **#21** | 20/08 | `index.html` + `css/style.css`, **189 ajouts / 217 suppressions** | Le plus dangereux du lot. À réextraire sur `main` si le contenu vous intéresse encore, sinon fermer. |
| **#36** | 22/08 | `index.html` + `css/style.css` (60 lignes) | Blocs services. À revérifier contre l'état actuel avant tout. |
| **#9** | 02/08 | crée `renovation-pontarlier.html` et `renovation-valdahon.html` | ⚠️ **Risque de cannibalisation** : la production couvre déjà Pontarlier par service (`cloisons-pontarlier`, `degat-des-eaux-pontarlier`, `isolation-interieure-pontarlier`, `papier-peint-pontarlier`, `faux-plafonds-pontarlier`). Une page « rénovation Pontarlier » générique entrerait en concurrence avec elles. À passer par `rushiti-keyword-map` avant toute décision. |
| **#6** | 02/08 | `index.html` — vocabulaire « peintre / plaquiste » | Intention juste — la copie ne contient toujours pas « plaquiste » — mais le diff d'août réécrirait title, meta et JSON-LD déjà refaits depuis. À refaire proprement, pas à fusionner. |
| **#20** | 14/08 | `docs/simulateur-peinture/bloc-methode-calcul.html` | Bloc pour une page `/simulateur-peinture` qui existe en production. Sans risque pour la copie, mais à appliquer côté production, pas ici. |
| **#10** | 02/08 | crée `diagnostic-degat-des-eaux.html` | La page n'existe **pas** en production. C'est donc une création de contenu à part entière, à décider comme telle — pas une PR technique à fusionner. |

---

## 7. Les trois PR de correctifs de skills — à examiner une par une

| PR | Objet | Remarque |
|---|---|---|
| **#42** | Skill `rushiti-seo-engine` (chef d'orchestre) + prompt maître | 1 581 lignes, 6 fichiers de références. Décision d'architecture : voulez-vous un skill qui pilote les autres ? |
| **#41** | Relevé citation IA + correction NF DTU 53.12 | ⚠️ Contient une **correction de norme** (DTU 53.12 pour les sols souples collés) qui, elle, est factuelle et à récupérer même si le reste est périmé. |
| **#29** | Correctifs de routage de 10 skills | Base du 21/08 ; les skills ont évolué côté claude.ai depuis. À revérifier avant de fusionner. |

---

## 8. Ordre de marche proposé

1. **Fusionner** cette PR (correction « 20 ans »), puis #65, #62, #61, #59, #50, #63.
2. **Fermer** #51 (régression), #8 (absorbée), #45 (périmée).
3. **Fermer** #14, #13, #12, #11 (skills déjà vivants ailleurs) — sauf si vous
   décidez de tout versionner ici.
4. **Trancher** les cinq skills inexistants (§5) : lesquels vous manquent vraiment ?
5. **Récupérer** la correction NF DTU 53.12 de #41, indépendamment du sort de la PR.
6. **Laisser fermées ou réextraire** les six PR à risque (§6) — aucune ne doit
   être fusionnée telle quelle.

Rien de tout cela n'est fait sans votre accord : ce document trie et
argumente, il ne ferme aucune PR.

---

## 9. Hors dépôt — la correction du skill `schema-builder`

L'audit du 31/08 relevait que `schema-builder` utilise `@type: "Painter"`,
un type qui **n'existe pas** dans schema.org (`schema.org/Painter` répond 404,
`schema.org/HousePainter` répond 200). Un `@type` inexistant fait ignorer le
nœud entier.

Les 6 skills versionnés ici portent tous `HousePainter` — vérifié. Le fichier
fautif vit côté claude.ai, hors de ce dépôt. La correction à y faire :

- `references/local-business.md` : remplacer l'affirmation que `Painter` existe ;
- `references/rushiti-defaults.md` : `"@type": "Painter"` → `"@type": "HousePainter"`
  (ou le tableau complet `["LocalBusiness", "HousePainter", "HomeAndConstructionBusiness"]`,
  comme le fait la production).
