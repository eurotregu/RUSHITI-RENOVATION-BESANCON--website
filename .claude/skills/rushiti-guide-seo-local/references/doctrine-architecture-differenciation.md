# Doctrine 2 — Architecture des pages locales et différenciation du contenu

Cette doctrine répond à trois questions : faut-il une page par zone
d'intervention (et laquelle), comment gérer les zones qui se chevauchent, et
comment différencier des dizaines de pages « même service, ville voisine »
sans tomber dans le contenu dupliqué. Elle décrit un système qui **existe
déjà** sur rushiti-renovation.fr — on l'applique, on ne le réinvente pas.

## A. L'architecture existante (la carte)

```
rushiti-renovation.fr
├── /                              accueil (requêtes marque + « entreprise de … »)
├── /{service}-besancon            pages PILIERS des 6 silos
│     peinture-interieure · peinture-exterieure · papier-peint ·
│     toile-de-verre · ratissage-enduit · platrerie · cloisons ·
│     doublage-murs · faux-plafonds · revetements-sol · parquet-flottant ·
│     sol-pvc · lino-vinyle-lvt · vitrification-parquet · ragreage-sol ·
│     isolation · isolation-interieure · degat-des-eaux ·
│     renovation-appartement · renovation-salle-de-bain · renovation-cuisine …
├── /{service}-{zone}              GRILLE locale par paliers (voir B)
├── pôle B2B                       syndic-copropriete · remise-en-etat-logement-locatif ·
│                                  amenagement-commerce-bureau · expert-assurance-sinistre ·
│                                  devis-assurance-degat-des-eaux
├── /blog/…                        satellites « Conseils » (1 problème = 1 contenu)
└── transverses                    /contact · /zones-intervention · /realisations ·
                                   /a-propos · /prix-travaux-renovation-besancon · /merci
```

Sources de vérité, dans cet ordre :

1. **Le sitemap live** `https://rushiti-renovation.fr/sitemap.xml` — à relire
   au début de chaque mission, la carte ci-dessus vieillit.
2. **Le registre** `docs/seo/regjistri-fjale-kyce.csv` — l'attribution
   canonique page ↔ requête pivot, les verdicts d'Isuf (dont les REFUZOHET).
3. **L'inventaire des paliers** `docs/seo/inventaire-grille-paliers-2026-08.csv`
   — combien de pages chaque zone conserve.

## B. Une page par zone ? Oui — mais par paliers

La réponse naïve (« une page par service et par ville ») a déjà été essayée
et corrigée : la grille est passée de **644 à 301 pages** (63 zones), parce
que des centaines de pages minces et quasi identiques n'imprimaient pas et
diluaient le crawl. Le système en vigueur :

| Palier | Zones | Pages conservées par zone | Logique |
|---|---|---|---|
| **A — cœur** | Besançon + quartiers forts (Battant, Centre-ville, Chaprais, Bregille, Butte-Grette…) | 18 (tous services) | Volume réel + différenciation possible (bâti, clientèle) |
| **B — pôles** | Communes pôles (École-Valentin, Avanne-Aveney, Chalezeule, Châtillon-le-Duc, Beure, Boussières, Dannemarie-sur-Crête…) | 10 | Les services les plus demandés seulement |
| **C — villages** | Petites communes (Amagney, Arguel, Braillans, Chaucenne, Deluz…) | 5 | Présence minimale ; le pilier Besançon fait le reste |

Règles d'application :

- **Renforcer avant de créer.** Une page pilier en page 2-5 de Google vaut
  plus que dix pages de grille neuves. L'ordre : piliers → maillage → grille.
- **Toute création passe la porte PORTA** de `rushiti-keyword-map` (4
  contrôles anti-cannibalisation, preuve de demande GSC/Trends à l'appui).
  Aucune exception, même pour « juste une petite page ».
- **La production** est le métier de `rushiti-page-locale`, qui exige un
  gabarit HTML existant du site — jamais de structure inventée.
- **Ne jamais recréer** une page consolidée : les fusions sont posées en 301
  dans `_redirects` (ex. `/ravalement-facade-besancon` → 301 →
  `/peinture-exterieure-besancon`). Recréer l'URL casserait la consolidation.

### Zones qui se chevauchent (quartier ⊂ ville ⊂ département)

Le principe : **1 requête canonique = 1 page**, et chaque niveau
géographique a sa requête.

| Niveau | Requête servie | Page |
|---|---|---|
| Quartier (Battant, Planoise…) | « service + quartier » | page de grille du quartier |
| Ville (Besançon) | « service + besançon » | page pilier — la grille ne la vise jamais |
| Commune limitrophe | « service + commune » | page de grille palier B/C |
| Département (« Doubs », « 25 ») | pas de page dédiée | corps de texte des piliers + `areaServed` du JSON-LD + /zones-intervention |

Deux pièges connus :

- Une page quartier qui optimise « à Besançon » partout cannibalise le
  pilier. Elle dit « à Battant », « dans le quartier Battant (Besançon) ».
- « Doubs » seul est trop large pour convertir : aucune page « peintre
  Doubs » — la requête est servie par le pilier + l'accueil.

### Hors du Doubs (Belfort 90, Vesoul 70, Dole 39…)

Ces villes sont **hors zone validée** (`rushiti-defaults.md` ne liste que
Besançon + communes du Doubs). Créer une page hors zone est une **décision
business d'Isuf** (déplacements, rentabilité chantier), jamais une décision
SEO — et encore moins celle d'un outil externe qui propose « Belfort,
Vesoul, Dole » parce qu'elles sont sur la carte. Procédure : arbitrage
d'Isuf → ajout à la zone dans les données → entrée au registre → porte
PORTA → production.

## C. Maillage interne (le squelette qui porte la grille)

- **Satellite → pilier** : le premier lien du texte pointe le pilier du
  silo, ancre descriptive (« peinture intérieure à Besançon »), jamais
  « cliquez ici » — le premier lien est le plus pondéré.
- **Pilier → satellites** : section « Pour aller plus loin » ; sans elle les
  satellites sont orphelins (contrôle → `orphan-finder`).
- **Page de grille → son pilier service** (lien systématique) + 2-3 services
  frères **dans la même zone** + /contact.
- **Bloc « Nous intervenons aussi »** en pied de page service : 5 à 8 liens
  maximum, uniquement vers des pages **existantes et conservées par le
  palier** (jamais un annuaire de 60 communes — c'est un footer spam et la
  moitié des liens seraient rouges après consolidation).
- **Jamais** de lien vers rushiti.fr (arbitrage domaine en attente) ni vers
  rushiti-peinture.fr (domaine éteint).
- Le plan de liens détaillé, avec phrases d'insertion, est le métier de
  `rushiti-maillage-interne`.

## D. Différenciation — éviter le contenu dupliqué

### Pourquoi c'est le risque n° 1 de la grille

Google replie les pages quasi identiques : une seule est indexée, les autres
deviennent « Dupliquée, non sélectionnée comme canonique ». Le site l'a
**vécu** (d'où la consolidation 644 → 301 et la dé-duplication des titles
sur 40 pages, vérifiée en production le 21/08/2026). La règle qui en
découle : une page de grille n'existe que si elle peut être **réellement
différente** — sinon le palier la supprime.

### Le minimum unique par page de grille

| Élément | Exigence |
|---|---|
| Title / meta / H1 | Uniques (formules doctrine 1, zone canonique) |
| Introduction | Réécrite pour la zone, jamais un search-replace du nom de ville |
| 1 bloc « angle local » | Le bâti, la clientèle ou la contrainte propres à la zone (voir matrice) |
| FAQ locale | 2-3 questions dont au moins une spécifique à la zone |
| Preuve locale | Chantier réel de la zone (photo RGPD ok via `rushiti-memo-chantier`) quand il existe ; **sinon rien** — jamais de témoignage ou de « Mme Dupont » inventé |
| Maillage | Liens propres à la zone (services frères de la même zone) |

Le tronc commun (description du service, méthode, normes DTU) **peut** être
partagé : c'est le même métier partout. C'est l'habillage local qui doit
être vrai et propre à la zone.

### Matrice d'angles locaux (candidats à valider par le terrain)

Ces angles sont des **hypothèses de départ** cohérentes avec le bâti
régional ; avant publication, les confirmer avec Isuf/Yll (ce qu'ils voient
réellement en chantier) — on ne publie que du vécu.

| Zone | Angles candidats |
|---|---|
| Battant, Centre-ville, Bregille | Bâti ancien : murs en pierre, plâtre traditionnel, grandes hauteurs sous plafond, copropriétés anciennes, contraintes d'accès en rue étroite |
| Planoise, Palente-Orchamps | Grands ensembles, logements locatifs : remises en état entre locataires, délais serrés, interlocuteurs bailleurs/gestionnaires |
| Chaprais-Cras, Saint-Ferjeux | Immeubles 1900-1960, appartements familiaux : rafraîchissements complets, plâtres fissurés |
| École-Valentin, Pirey, Miserey-Salines, Franois | Pavillons années 1970-1990 : combles à isoler, façades, sols à moderniser |
| Saône, Mamirolle, Nancray (plateau) | Maisons familiales, hivers plus rudes : condensation, murs froids, isolation |
| Pontarlier et Haut-Doubs | Altitude : contraintes hivernales fortes, planification de chantier |
| Montbéliard | Parc ancien + locatif : remises en état, copropriétés |

### Le test final

Masquer le nom de la zone et lire la page : si elle pourrait décrire
n'importe quelle autre commune, elle n'est pas prête. Et si, pour un village
palier C, il n'y a **rien de vrai à dire** au-delà de « on s'y déplace » —
c'est le signal que les 5 pages du palier C suffisent et qu'on renforce le
pilier au lieu d'écrire du remplissage.

### Contrôles associés

- Cannibalisation requête × page : `rushiti-cannibal-check` (verdict), score
  au registre (`rushiti-keyword-map`).
- Pages exclues « dupliquée / soft 404 » : `rushiti-indexation` (GSC,
  rapport Couverture).
- Fraîcheur et divergences factuelles entre pages (horaires, compteurs
  d'avis) : `rushiti-refresh-planner`.
