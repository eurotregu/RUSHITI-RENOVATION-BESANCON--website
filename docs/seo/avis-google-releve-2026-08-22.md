# Relevé des avis Google — 22/08/2026

Relevé effectué pour alimenter le carrousel d'avis Google de la page d'accueil
(`index.html`, section `#avis`). Ce document est la **source de vérité** de ce
qui est affiché : toute mise à jour du carrousel repart d'un nouveau relevé daté.

## Chiffres relevés

| Donnée | Valeur | Relevé le |
|---|---|---|
| Note moyenne | **4,7 / 5** | 22/08/2026 |
| Nombre d'avis | **34** | 22/08/2026 |
| Avis avec texte accessibles au relevé | 24 | 22/08/2026 |
| Avis publiés sur le site | 12 | 22/08/2026 |

**Google Place ID** : `ChIJlwZoPfpjjUcRN28uHfvIfJc`

Liens construits sur ce Place ID (utilisés dans le bandeau du carrousel) :

- Lire les avis : `https://search.google.com/local/reviews?placeid=ChIJlwZoPfpjjUcRN28uHfvIfJc`
- Laisser un avis : `https://search.google.com/local/writereview?placeid=ChIJlwZoPfpjjUcRN28uHfvIfJc`

Le second lien est celui à envoyer aux clients en fin de chantier
(voir `rushiti-courriers-clients`) : il ouvre directement le formulaire de notation.

**Source du relevé** : miroir public de la fiche Google Business de RUSHITI
Rénovation (`rushiti-renovation-peintre.localo.site`), pages `/` et `/reviews`.
Les chiffres 4,7 et 34 y sont cohérents avec le relevé du 21/08/2026 déjà
consigné dans le guide SEO local — la fiche n'a pas bougé entre les deux dates.

## Règles appliquées

Trois garde-fous de la doctrine maison ont commandé la forme du carrousel.

**1. Pas d'`aggregateRating` en JSON-LD.** La note 4,7/34 n'est **pas** balisée
en données structurées : les avis Google sont des avis tiers, et les consignes
Google interdisent de les remonter en `aggregateRating` sur son propre site.
La note est **citée en texte et datée** dans le bandeau (« Sur 34 avis · relevé
le 22/08/2026 »), exactement comme le prévoit le guide SEO local. Le JSON-LD
`HousePainter` de la page d'accueil n'a pas été touché.

**2. Aucun avis inventé, aucun texte retouché.** Les 12 avis publiés sont repris
**mot pour mot**, ponctuation, emoji et graphie du prénom compris — y compris
les prénoms en minuscules (« altin k », « jeancharles f ») tels que leurs
auteurs les affichent sur Google. Rien n'a été corrigé, raccourci ni reformulé.

**3. Aucune étoile par avis.** Le miroir de la fiche ne donne ni la note ni la
date de chaque avis : afficher « 5 étoiles » sur chaque carte reviendrait à
inventer une donnée, d'autant qu'une moyenne de 4,7 sur 34 avis implique
mécaniquement des notes inférieures à 5. Les cartes portent donc le logo Google
et la mention « Avis Google », sans étoiles. Le CSS prévoit déjà l'affichage
d'étoiles par carte (`.avis-card .avis-etoiles`) : le jour où Isuf relève les
notes individuelles depuis son interface Google Business, il suffit d'ajouter
le bloc d'étoiles dans la carte concernée.

## Avis publiés (12)

Sélectionnés pour couvrir les segments de prestation, pas pour être les plus
élogieux — le carrousel doit parler à chaque type de prospect.

| # | Auteur (graphie Google) | Segment couvert |
|---|---|---|
| 1 | Jérôme J | Peinture appartement complet + sols |
| 2 | Jean-francois D | Dégât des eaux, mandat assurance (MAIF) |
| 3 | Almir | Parquet chêne après dégât des eaux, mobilier en place |
| 4 | Lauryne S | Plafond, finition sans traces de rouleau |
| 5 | Michel R | Recommandation, conseil couleurs, devis |
| 6 | altin k | Joignabilité, ponctualité, chantier nettoyé chaque soir |
| 7 | Bashkim S | Peinture appartement, protection, délais |
| 8 | Sandrine P | Finitions, tenue des délais |
| 9 | Laura B | Pose de plafond + gros chantier peinture |
| 10 | jeancharles f | Enduit plafond + peinture appartement, délais |
| 11 | Erion A | Qualité de rendu, discrétion, conduite de chantier |
| 12 | christelle m | Réactivité, adaptation à des clients âgés |

## Avis relevés mais non publiés (12)

Écartés uniquement pour la longueur du carrousel — ils sont tout aussi
exploitables et peuvent remplacer un avis ci-dessus : Endi S, Gjon K, mensur m,
Marie B, Val V, sabrina M, Shipron R, Niels S, Orges U, JP M, severine B,
MaximeVIDEOS !.

Le texte intégral de ces avis se retrouve sur la fiche Google ; ils n'ont pas
été recopiés ici pour éviter d'entretenir une seconde copie qui divergerait.

## Point à signaler à Isuf (hors périmètre de cette modification)

Le relevé de la fiche Google fait apparaître deux écarts avec les données de
référence internes. Aucun n'a été corrigé ici — ils relèvent de la fiche
Google et du NAP, pas du carrousel :

- **Adresse** : la fiche Google affiche « 18 **Rue du** Professeur Haag », alors
  que la règle NAP de référence impose « 18 rue Professeur Haag » (sans « du »,
  graphie Base Adresse Nationale). L'écart est à arbitrer : soit la fiche Google
  est corrigée, soit la règle interne est alignée sur la fiche — mais les deux
  ne peuvent pas cohabiter sans affaiblir le signal local.
- **Horaires** : la fiche Google annonce 7h-20h30 en semaine et une ouverture le
  dimanche, quand le JSON-LD de `index.html` déclare 7h30-18h en semaine et
  8h-12h le samedi. À reprendre sur les horaires réels, en une seule fois,
  partout.

## Quand refaire ce relevé

À chaque fois que la note ou le nombre d'avis affichés à l'écran cessent d'être
vrais — c'est-à-dire à chaque nouvelle vague d'avis. La date affichée dans le
bandeau (`relevé le 22/08/2026`) et le compteur (`34 avis`, `12 avis affichés
sur 34`) sont en dur dans `index.html` : ils se mettent à jour **à la main**, en
même temps que la note. Un bandeau qui annonce une date vieille de six mois
décrédibilise la preuve qu'il est censé apporter.
