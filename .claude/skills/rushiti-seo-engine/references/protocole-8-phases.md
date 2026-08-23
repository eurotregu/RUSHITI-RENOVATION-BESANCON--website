# Le protocole en 8 phases — détail d'exécution

> Une phase = une question tranchée, une entrée exigée, un critère de
> passage, un livrable. **Une phase sans son entrée ne se joue pas** : elle se
> déclare bloquée, en nommant ce qui manque et qui peut le fournir.
>
> Le playbook générique commence à la phase 2 (analyse concurrentielle). Sur
> un site de ~300 URL déjà consolidé, commencer là revient à proposer de
> créer ce qui existe. D'où la phase 0.

---

## Phase 0 — ÉTAT : qu'avons-nous déjà, et qu'est-ce qui imprime ?

**Question** : la cible est-elle déjà servie par une URL en ligne, et cette
URL récolte-t-elle des impressions ?

**Entrées exigées**
- `docs/seo/regjistri-fjale-kyce.csv` — le registre page ↔ mot-clé.
- L'inventaire des piliers :
  `.claude/skills/rushiti-page-service/references/inventaire-piliers-services.md`.
- Le dernier export Search Console requête × page, avec sa période. Absent →
  la phase se poursuit en **heuristique annoncée** (balises comparées dans le
  code source uniquement), et le rapport le dit dans son en-tête.
- Le dernier plan consolidé de `docs/seo/raporte/`.

**Critère de passage** : vous savez nommer l'URL qui porte déjà la requête,
ou établir qu'aucune ne la porte — avec la preuve datée.

**Motifs de blocage** : registre non synchronisé depuis plus de trois mois ;
sitemap non relevé ; cible formulée trop vaguement pour être cherchée
(« on veut plus de visibilité »).

**Livrable** : l'état de la cible en cinq lignes — URL existante ou non,
requête portée, dernière mesure GSC datée, page voisine à risque, verdict
provisoire *renforcer / créer / ne rien faire*.

> **Le réflexe qui rapporte le plus.** 79 % des clics du site viennent de
> l'accueil (relevé du 22/08/2026) pendant que les piliers restent en
> pages 2-5. Avant toute création, la question utile est presque toujours :
> « cette visibilité existante, pourquoi ne convertit-elle pas ? »

---

## Phase 1 — PORTE : renforcer ou créer ?

**Question** : a-t-on le droit de créer une page ?

**Entrée exigée** : la sortie de la phase 0.

**Exécution** : invoquer `rushiti-keyword-map` en **mode PORTA**. Il déroule
ses quatre contrôles — collision exacte, collision d'intention, proximité
lexicale, preuve de terrain GSC — et rend un verdict écrit.

| Verdict | Suite du protocole |
|---|---|
| `LEJOHET` | la campagne continue en **création** (phases 2 → 7) |
| `LEJOHET ME KUSHTE` | continue en création, **avec** les obligations de différenciation écrites (mots interdits dans le title, maillage hiérarchique imposé) |
| `REFUZOHET` | la campagne **bascule en renforcement** de la page nommée. On ne continue jamais en création |

**Critère de passage** : un verdict écrit, daté, consigné au registre
(`verdikti_data`), et validé par Isuf avant toute commande de rédaction.

> **Interdiction absolue** : enchaîner les phases suivantes après un
> `REFUZOHET` en création. Un plan qui passe outre fabrique exactement la
> cannibalisation que la porte existe pour empêcher.

---

## Phase 2 — TERRAIN : qui gagne, et qui est cité ?

**Question** : sur cette requête, que fait la SERP — et quelles sources les
moteurs de réponse citent-ils à notre place ?

**Deux relevés distincts, jamais confondus.**

**2A — La SERP.** Agent : `rushiti-ecart-concurrentiel`. On relève le type de
page qui gagne (pilier, annuaire, plateforme de devis, forum, fiche Google),
la profondeur du contenu, les blocs SERP occupés (pack local, PAA, aperçu
IA), et surtout **ce que tous les gagnants omettent** — c'est l'ouverture.

Pour un artisan local, l'omission récurrente est la même : les gagnants sont
des annuaires génériques qui ne savent rien du bâti. Ce qu'ils ne peuvent pas
écrire : le comportement d'un plâtre traditionnel du centre ancien, la
condensation des murs nord dans le climat franc-comtois, le déroulé réel d'un
dossier IRSI. C'est là que RUSHITI est imbattable — et c'est gratuit.

**2B — Le corpus IA.** Agent : `rushiti-citation-ia`. On ne mesure pas
« sommes-nous cités » (c'est `rushiti-part-de-voix-ia`), on relève **quelles
URL sont citées à notre place**, et par quelle porte on peut y entrer.
Chaque observation est classée `S` / `M` / `F` / `Ø` / `NM`.

> Le cas `F` — un fait du site repris sans que RUSHITI soit nommé — est le
> plus fréquent et le plus vite corrigé : la page est extractible, mais ses
> phrases ne portent pas l'entité. Correction en phase 4, pas en phase 2.

**Critère de passage** : vous pouvez nommer l'angle de différenciation en une
phrase, et il n'est pas « nous sommes sérieux ».

**Motif de blocage** : aucun moteur interrogeable et aucun relevé assisté
fourni → le volet 2B est `NM`, la campagne continue sur 2A seul, et le
rapport le déclare.

---

## Phase 3 — ARCHITECTURE : où se pose la cible ?

**Question** : dans quel silo, à quel niveau, avec quels voisins ?

**Entrée** : verdict de phase 1 + angle de phase 2.

**Exécution** : `rushiti-keyword-clusters` pour le placement,
`rushiti-architecte-seo` pour la cohérence du cocon.

Six silos + B2B : peinture · plâtrerie-placo · sols · isolation · dégât des
eaux · rénovation de pièce · B2B (syndics, gestionnaires, bailleurs, experts
d'assurance, commerces).

**La règle qui tient l'architecture** :

| | Page pilier (× Besançon) | Page locale (× commune/quartier) | Article de blog |
|---|---|---|---|
| Intention | commerciale large | commerciale locale | informationnelle |
| Rôle | gagne la requête métier | capte la SERP locale | pousse le pilier, attrape la longue traîne |
| Maillage | reçoit des locales et des articles, envoie vers le palier A | pointe vers le pilier | pointe vers le pilier |

**Interdit ici** : proposer d'ajouter un palier à la grille locale ou de
regonfler le nombre de pages. La grille est passée de 644 à 301 pages
volontairement. Toute reprise passe par `rushiti-keyword-map`.

**Livrable** : la place exacte de la cible, ses trois liens entrants
minimum (sinon elle naît orpheline), et la page voisine à ne pas
cannibaliser.

---

## Phase 4 — RÉDACTION : brief, puis contenu

**Question** : que dit exactement cette page, et qui l'écrit ?

**Toujours en deux temps.** Le brief d'abord (`rushiti-brief-seo`), le
contenu ensuite. Écrire sans brief produit une page qui se relit bien et qui
ne cible rien.

| La cible | L'agent qui rédige |
|---|---|
| Page pilier service × Besançon | `rushiti-page-service` |
| Page commune ou quartier | `rushiti-page-locale` |
| Article de blog, satellite | `rushiti-architecte-seo` |
| FAQ seule | `rushiti-faq` |
| Title / meta seuls | `seo-title-meta` |
| Page existante qui décline | `rushiti-refresh-planner` |

**Les règles GEO — ce qui rend une page citable par un moteur de réponse.**
Elles se vérifient à la phrase, pas à la page : un moteur prélève un fragment
de trente à soixante mots, et ce fragment doit rester **vrai, complet et
attribuable** une fois découpé.

1. **La réponse dans les deux premières phrases.** Pas de mise en contexte,
   pas d'histoire. La question posée, la réponse donnée.
2. **Un fait par phrase**, avec son ancrage : un lieu, une norme, un geste
   technique. « Sur un plafond en plaques de plâtre, la reprise après fuite
   commence par le séchage du support, contrôlé à l'humidimètre, avant tout
   enduit » — pas « nous intervenons rapidement et efficacement ».
3. **L'entité dans la phrase qui porte le fait** — c'est la correction du
   cas `F`. « RUSHITI Rénovation intervient à Besançon selon le DTU 59.1 »
   s'accroche ; « nous appliquons les DTU en vigueur » ne s'accroche pas.
4. **Tableaux pour comparer, listes ordonnées pour les procédés,**
   paragraphes de trois à quatre lignes.
5. **FAQ de vraies questions de clients**, réponse de 40 à 80 mots dont la
   première phrase répond seule.
6. **Aucun chiffre non validé.** Ni prix, ni délai, ni pourcentage
   d'économie, ni note. Un plan générique remplit ces trous avec des
   fourchettes crédibles et fausses : c'est le défaut n°1 du corpus.

**Critère de passage** : la page est complète, sans trou (`[insérer
paragraphe]` = plan, pas livrable), et chaque chiffre remonte à une source
datée.

---

## Phase 5 — BALISAGE : ce que la machine doit comprendre

**Question** : quelles données structurées, et disent-elles la vérité de la
page ?

**Agent** : `schema-builder`.

La pile habituelle, cohérente par `@id` en URL absolues
(`https://rushiti-renovation.fr/#identity`) :

- `LocalBusiness` / `HousePainter` — le socle du site : NAP au caractère
  près, `telephone` `+33760279897`, `areaServed` Besançon + Doubs.
- `Service` — la prestation de la page, `provider` pointant vers le `@id` du
  socle.
- `FAQPage` — **uniquement** sur les questions visibles dans la page.
- `BreadcrumbList` — cohérent avec le fil d'Ariane affiché.
- `WebSite` — sur l'accueil seulement.

**Interdits, sans exception** :
- `Review` et `aggregateRating` auto-déclarés — contraires aux consignes
  Google, risque de pénalité manuelle. La preuve sociale va dans le **texte
  visible**.
- Une `FAQPage` sur des questions absentes de la page.
- Des horaires, un `priceRange` ou des coordonnées géographiques non
  vérifiés. Les latitude/longitude se relèvent sur la fiche Google réelle
  (Place ID `ChIJlwZoPfpjjUcRN28uHfvIfJc`, cf.
  `docs/seo/avis-google-releve-2026-08-22.md`), jamais « approximées » — une
  coordonnée inventée est une erreur d'entité que les moteurs recoupent et
  propagent.
- Un `taxID` reconstruit : c'est `FR89905214631`, relevé, pas calculé.

**Critère de passage** : le JSON-LD ne dit rien que la page ne montre.

---

## Phase 6 — MAILLAGE : qui pousse cette page ?

**Question** : la page reçoit-elle assez de liens internes pour exister ?

**Agents** : `rushiti-maillage-interne`, puis `orphan-finder` en contrôle.

Règles :
- **Trois liens entrants minimum** depuis des pages existantes. En dessous,
  la page est orpheline quel que soit son contenu.
- Les satellites pointent **vers** le pilier ; le pilier redistribue vers le
  palier A de la grille locale.
- Ancres descriptives et naturelles — jamais « cliquez ici », jamais la
  requête exacte répétée à l'identique dix fois.
- **Silo tenu serré** : on ne relie pas le silo peinture au silo sols sans
  passer par une page chapeau. La proximité thématique est un signal ; la
  diluer coûte.

**Le gisement déjà identifié** (opportunités GSC du 20/08/2026) :
`/platrerie-besancon` est en position 9,1 et `/ratissage-enduit-besancon` en
10,9 — à une porte de la page 1 — et **aucun pilier voisin ne les pousse**.
Deux liens contextuels chacun : effort faible, impact fort.

**Livrable** : les phrases exactes à coller, avec leur page de départ et leur
ancre.

---

## Phase 7 — MESURE : la ligne de départ et la fenêtre

**Question** : comment saura-t-on, dans six semaines, si ça a marché ?

**Agent** : `rushiti-regression-seo`.

Une action sans donnée de départ datée est une action qu'on ne pourra jamais
juger. La phase 7 n'est pas un bonus de fin : **sans elle, les sept
précédentes ne sont qu'une opinion.**

Le livrable tient en cinq champs :

| Champ | Règle |
|---|---|
| Requête surveillée | celle du registre, au mot près |
| Page surveillée | l'URL canonique, une seule |
| Donnée de départ | impressions + position GSC du jour, **avec la date** ; ou `NM` assumé |
| Fenêtre de relecture | 4 à 6 semaines pour Google · 6 à 8 semaines pour le corpus IA |
| Effet attendu | fort / moyen / faible, **avec son motif** — jamais un chiffre, jamais une position promise |

Les deux portes se relisent séparément, à leur propre cadence. Les fusionner
en un « score de visibilité » unique masque exactement l'information utile :
laquelle des deux a bougé.
