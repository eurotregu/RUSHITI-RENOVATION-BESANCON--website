# Pages de service dédiées — relevé live et verdict PORTA

| | |
|---|---|
| Date | 22/08/2026 |
| Demande | « Créer une landing page dédiée pour chaque service principal (ex. `rushiti-renovation.fr/peinture`, `/placo`, `/isolation`) » |
| Agent | `rushiti-keyword-map` — mode PORTA (porte de création) |
| Portée | rushiti-renovation.fr uniquement |
| Source de la vérification | sitemap live relevé le 22/08/2026 (754 URL) — voir `inventaire-pages-services-live-2026-08-22.csv` |
| Écriture | `docs/seo/` + copie GitHub Pages de ce dépôt. **Aucune modification du site de production.** |

## Përgjigje e shkurtër (SQ)

Rekomandimi **është zbatuar tashmë** në prodhim: siti nuk i ka shërbimet vetëm
në ballinë — ka **30 faqe piliere shërbimi** të dedikuara (`/peinture-interieure-besancon`,
`/plaquiste-besancon`, `/platrerie-besancon`, `/isolation-besancon`,
`/isolation-interieure-besancon`, `/degat-des-eaux-besancon`…) plus **706 faqe
shërbim × zonë**, gjithsej 754 URL në sitemap-in e 22/08/2026.

Krijimi i `/peinture`, `/placo`, `/isolation` **refuzohet**: do të ishin faqe të
dyta mbi të njëjtat fjalë kyçe që i mban tashmë një faqe ekzistuese —
kanibalizim, jo fitim. Puna e vërtetë sot është **forcimi** i faqeve ekzistuese
(dégât des eaux, isolation/ITI, plaquiste) dhe **maillage-i** drejt tyre, jo
faqe të reja. E vetmja mungesë reale e gjetur: **carrelage**, i shpallur në
ballinë pa asnjë faqe as pivot — kërkon arbitrazhin e Isufit (a ofrohet apo jo).

## 1. Constat : la recommandation est déjà en place

Relevé du sitemap live le 22/08/2026 : **754 URL**, dont **736 pages de service**
(30 pages piliers `/{service}-besancon` + 706 pages de la grille service × zone),
12 URL de blog et 6 pages transverses (`/a-propos`, `/contact`, `/realisations`,
`/simulateur-peinture`, `/zones-intervention`, `/mentions-legales`).

Les services ne sont donc pas « listés sur la page d'accueil » : chaque service
a sa page, et la plupart l'ont déclinée par commune et par quartier. Détail
famille par famille dans `inventaire-pages-services-live-2026-08-22.csv`.

Extrait (pages piliers) :

| Silo | Pages dédiées en ligne |
|---|---|
| Peinture | `/peinture-interieure-besancon` · `/peinture-exterieure-besancon` · `/peinture-facade-isolation-exterieure-besancon` · `/papier-peint-besancon` · `/toile-de-verre-besancon` · `/ratissage-enduit-besancon` |
| Plâtrerie & placo | `/platrerie-besancon` · `/plaquiste-besancon` · `/cloisons-besancon` · `/doublage-murs-besancon` · `/faux-plafonds-besancon` |
| Sols | `/revetements-sol-besancon` · `/parquet-flottant-besancon` · `/sol-pvc-besancon` · `/lino-vinyle-lvt-besancon` · `/vitrification-parquet-besancon` · `/ragreage-sol-besancon` |
| Isolation | `/isolation-besancon` · `/isolation-interieure-besancon` |
| Dégât des eaux | `/degat-des-eaux-besancon` · `/devis-assurance-degat-des-eaux-besancon` |
| Rénovation de pièce & B2B | `/entreprise-renovation-besancon` · `/renovation-appartement-besancon` · `/renovation-salle-de-bain-besancon` · `/renovation-cuisine-besancon` · `/prix-travaux-renovation-besancon` · `/amenagement-commerce-bureau-besancon` · `/renovation-syndic-gestionnaire-besancon` · `/remise-en-etat-logement-locatif-besancon` · `/expert-assurance-sinistre-besancon` |

**Précision utile :** la page d'accueil de ce dépôt (`index.html`) est la copie
GitHub Pages, en `noindex, nofollow` — le site officiel et indexable est
rushiti-renovation.fr, hébergé dans le dépôt de production `eurotregu/rushiti-renovation`.
C'est cette copie qui donne l'impression d'un site « une page ».

## 2. Verdict PORTA sur les trois URL proposées

Les quatre contrôles de la porte de création, dans l'ordre imposé :

| URL proposée | 1. Collision exacte | 2. Collision d'intention | 3. Proximité lexicale | 4. Preuve de terrain | Verdict |
|---|---|---|---|---|---|
| `/peinture` | Oui — pivot « peintre besançon » déjà attribué à `/peinture-interieure-besancon` | Oui — même intention commerciale, même zone, même famille | Recouvrement total | La requête imprime déjà sur l'accueil et sur la page pilier (page pilier : 189 impr, pos. 24,8 — GSC 17/05–16/08/2026) | **REFUZOHET** → le contenu renforce `/peinture-interieure-besancon` |
| `/placo` | Oui — deux pivots existants : « plaquiste besançon » (`/plaquiste-besancon`) et « plâtrerie placo besançon » (`/platrerie-besancon`) | Oui | Recouvrement total | `/platrerie-besancon` : 481 impr, pos. 21,1 (GSC 17/05–16/08/2026) | **REFUZOHET** → renforcer les deux pages existantes |
| `/isolation` | Oui — pivot « isolation besançon (chapeau combles + phonique) » attribué à `/isolation-besancon` | Oui | Recouvrement total, plus le couple isolation / ITI déjà sous surveillance (score de cannibalisation 40 🟠) | silo isolation (chapeau combles + phonique) : 184 impr, pos. 28,3 (GSC 17/05–16/08/2026) | **REFUZOHET** → une page de plus aggraverait le conflit isolation / ITI |

Deux remarques de doctrine qui s'ajoutent au verdict :

1. **Les URL proposées n'ont pas de marqueur local.** Le ciblage RUSHITI est
   local : c'est « peintre **à Besançon** », pas « peintre ». Le pattern du site
   (`/{service}-{zone}`) porte déjà cette intention ; `/peinture` seul serait
   plus faible que `/peinture-interieure-besancon` sur la requête visée.
2. **Une page de plus sur un pivot déjà attribué ne monte pas, elle divise.**
   Le site a déjà payé ce prix : le doublon `ravalement-facade` / `peinture-exterieure`
   a dû être traité en 301 le 21/08, et le double ciblage papier peint /
   toile de verre a demandé un dé-duplication sur 40 URL.

## 3. Ce qui reste réellement ouvert

Classé par valeur business, selon la règle « renforcer avant de créer ».

| # | Sujet | Constat | Action | Agent |
|---|---|---|---|---|
| 1 | Dégât des eaux | Silo le plus rentable et le moins visible : 18 impr, pos. 20,0 (GSC 17/05–16/08/2026) malgré 76 pages | Renforcer la page pilier + maillage entrant. Priorité 1 | `rushiti-brief-seo` + `rushiti-maillage-interne` |
| 2 | Isolation vs ITI | `/isolation-interieure-besancon` : 0 impression sur 12 mois, sa propre requête est servie par `/isolation-besancon` et l'accueil. Score 40 🟠 | Verdict approfondi avant toute autre action sur le silo | `rushiti-cannibal-check` |
| 3 | Sol PVC vs lino/LVT | Deux pages pour un même univers produit | Fusion hors palier A après contrôle GSC | `rushiti-cannibal-check` |
| 4 | Plaquiste | Page dédiée sans impression sur 12 mois, éclipsée par l'accueil (899 impr, pos. 3,3 sur la requête) | Renforcement + maillage à ancre exacte (déjà amorcé en production, PR #19) | `rushiti-brief-seo` |
| 5 | **Carrelage** | « Carrelage mural et sol » est annoncé dans les services de la page d'accueil, mais **aucune page, aucun pivot au registre**, et le carrelage ne figure pas dans l'offre de référence des agents | **Arbitrage d'Isuf : la prestation est-elle proposée ?** Si oui → PORTA puis création ; si non → retirer la mention de la page d'accueil | Isuf, puis `rushiti-keyword-map` |
| 6 | `syndic-copropriete-besancon.html` (ce dépôt) | Brouillon prêt à déployer, absent du sitemap live ; son sujet recoupe `/renovation-syndic-gestionnaire-besancon` déjà en ligne | Passer la PORTA avant déploiement : soit différenciation écrite, soit fusion | `rushiti-keyword-map` |

## 4. Ce qui a été fait dans cette branche

- Relevé live et inventaire des pages de service :
  `inventaire-pages-services-live-2026-08-22.csv` (31 lignes, dont la ligne
  « carrelage » manquante).
- Ce verdict PORTA.
- **Copie GitHub Pages (`index.html`)** : les six blocs de services ne
  renvoyaient vers aucune page de service — ils pointaient uniquement vers des
  ancres internes. Chaque bloc liste désormais ses pages dédiées en ligne, avec
  des ancres exactes (« Plaquiste à Besançon », « Isolation intérieure (ITI) »,
  « Entreprise de rénovation à Besançon »…). La page reste en `noindex` :
  l'intérêt est la cohérence du parcours et le modèle de maillage, l'effet SEO
  se joue sur le site de production, où le maillage équivalent est déjà en
  ligne (PR #19).

## 5. En attente de validation d'Isuf

1. Carrelage : prestation proposée ou non (point 5 du tableau ci-dessus).
2. Ordre de bataille confirmé : dégât des eaux d'abord, puis le verdict
   isolation / ITI, avant toute nouvelle page.
3. Sort du brouillon `syndic-copropriete-besancon.html`.

*Aucun classement n'est promis ici : les effets attendus sont qualitatifs. Tous
les chiffres cités portent leur source et leur période ; aucune valeur n'est
estimée.*
