# Inventaire des pages pilier — état relevé le 22/08/2026

> Source : sitemap.xml de rushiti-renovation.fr, relevé le **22/08/2026**
> (~300 URL, dont la grille locale par paliers A/B/C). Ce tableau se
> re-relève avant toute décision de création : une URL absente d'ici
> peut avoir été publiée depuis.

## Silo Peinture

| Page pilier | Requête de tête |
|---|---|
| `/peinture-interieure-besancon` | peintre à Besançon · entreprise de peinture à Besançon |
| `/peinture-exterieure-besancon` | ravalement de façade Besançon (fusion faite : `/ravalement-facade-besancon` → 301) |
| `/peinture-facade-isolation-exterieure-besancon` | peinture de façade isolée par l'extérieur |
| `/papier-peint-besancon` | papier peint Besançon |
| `/toile-de-verre-besancon` | toile de verre Besançon |
| `/ratissage-enduit-besancon` | ratissage, enduit de lissage |

## Silo Plâtrerie / placo

| Page pilier | Requête de tête |
|---|---|
| `/plaquiste-besancon` | plaquiste à Besançon |
| `/platrerie-besancon` | plâtrerie placo Besançon |
| `/cloisons-besancon` | pose de cloison, créer une pièce |
| `/faux-plafonds-besancon` | faux plafond Besançon |
| `/doublage-murs-besancon` | doublage de mur *(recouvrement à surveiller avec l'ITI)* |

## Silo Isolation

| Page pilier | Requête de tête |
|---|---|
| `/isolation-besancon` | isolation Besançon *(page chapeau)* |
| `/isolation-interieure-besancon` | isolation intérieure (ITI) Besançon |

## Silo Sols

| Page pilier | Requête de tête |
|---|---|
| `/revetements-sol-besancon` | pose de revêtement de sol *(page chapeau)* |
| `/parquet-flottant-besancon` | parquet flottant, stratifié |
| `/sol-pvc-besancon` · `/lino-vinyle-lvt-besancon` | sol PVC, lino, LVT *(doublon en cours d'arbitrage)* |
| `/vitrification-parquet-besancon` | vitrification, ponçage de parquet |
| `/ragreage-sol-besancon` | ragréage de sol |

## Silo Dégât des eaux

| Page pilier | Requête de tête |
|---|---|
| `/degat-des-eaux-besancon` | dégât des eaux Besançon — **priorité de renforcement n°1** |
| `/devis-assurance-degat-des-eaux-besancon` | devis dégât des eaux pour l'assurance (IRSI) |

## Silo Rénovation de pièce et B2B

| Page pilier | Requête de tête |
|---|---|
| `/entreprise-renovation-besancon` | entreprise de rénovation Besançon |
| `/renovation-appartement-besancon` | rénovation d'appartement |
| `/renovation-salle-de-bain-besancon` | rénovation de salle de bains |
| `/renovation-cuisine-besancon` | rénovation de cuisine |
| `/prix-travaux-renovation-besancon` | prix des travaux |
| `/renovation-syndic-gestionnaire-besancon` | syndic, gestionnaire de biens |
| `/remise-en-etat-logement-locatif-besancon` | bailleur, remise en état locative |
| `/amenagement-commerce-bureau-besancon` | commerce, bureau |
| `/expert-assurance-sinistre-besancon` | expert d'assurance, sinistre |

Pages transverses : `/`, `/a-propos`, `/contact`, `/realisations`,
`/zones-intervention`, `/blog`, `/simulateur-peinture`, `/mentions-legales`.

---

# URL interdites *(elles cannibaliseraient une page déjà en place)*

Ces URL reviennent dans tous les plans génériques « une page par service ».
Aucune ne se crée : chacune doublerait une page existante qui porte déjà la
requête et récolte déjà des impressions.

| URL proposée | Décision | Page qui porte déjà la requête |
|---|---|---|
| `/peinture` | ❌ ne pas créer | `/peinture-interieure-besancon` |
| `/placo`, `/placo-platre` | ❌ ne pas créer | `/plaquiste-besancon` + `/platrerie-besancon` |
| `/isolation` | ❌ ne pas créer | `/isolation-besancon` + `/isolation-interieure-besancon` |
| `/renovation-complete` | ❌ ne pas créer | `/entreprise-renovation-besancon` + `/renovation-appartement-besancon` |
| `/renovation-salle-de-bain`, `/renovation-cuisine` | ❌ ne pas créer | leurs équivalents `-besancon` |
| `/carrelage` | ❌ hors offre confirmée | aucune — voir ci-dessous |

**Motif de fond.** Une URL sans le suffixe de zone perd le signal local (le
site vit sur des requêtes « service + ville ») et se met en concurrence avec
sa sœur : les deux pages se partagent les liens, les impressions et la
confiance, et aucune ne gagne. Si Isuf tient malgré tout à des URL courtes,
la seule forme acceptable est une **redirection 301 de la forme courte vers
la page existante** (`/peinture` → `/peinture-interieure-besancon`), jamais
une seconde page.

# Offre : ce qui est confirmé, ce qui ne l'est pas

**Confirmé** — peinture intérieure et extérieure · papier peint et toile de
verre · ratissage et enduit de lissage · plâtrerie, placo (BA13), cloisons,
faux plafonds, doublage · isolation intérieure et combles · sols (parquet
flottant et stratifié, PVC, lino, LVT, moquette, vitrification, ragréage) ·
dégât des eaux · rénovation de pièce (salle de bains, cuisine, appartement) ·
B2B syndics, gestionnaires, bailleurs, experts d'assurance, commerces.

**Refusé par Isuf (21/08/2026)** — enduit à la chaux, rénovation de
boiseries comme offre à part : la demande existe dans la Search Console, elle
reste sciemment non servie. Aucune page ne se crée pour ces requêtes.

**Non confirmé — arbitrage requis avant toute page** : carrelage (la mention
« Carrelage & Sol » figure sur une page d'accueil héritée, aucune page ni
prestation confirmée ne l'accompagne), moquette comme cible propre, peinture
du bâti ancien de la Boucle comme niche séparée.

# Zones

Palier A (cœur, ~18 pages/zone) : Besançon et ses quartiers — Battant,
Centre-ville, Chaprais, Bregille, Planoise, Montrapon, Palente,
Saint-Ferjeux, Saint-Claude, Velotte, Tilleroyes, Butte-Grette,
Vaîte-Clairs-Soleils.

Palier B (pôles, ~10) : École-Valentin, Saône, Thise, Pontarlier,
Montbéliard, Chalezeule, Miserey-Salines, Pirey, Serre-les-Sapins…

Palier C (villages, ~5) : le reste des communes du Doubs déjà en ligne.

**Hors périmètre** : Vesoul, Belfort, Dole, Dijon, Lons-le-Saunier — toute
commune hors Doubs, tant qu'Isuf n'a pas arbitré. Une page pilier ne les
mentionne pas, même dans une liste de « zones desservies ».

La grille a déjà été consolidée de 644 à 301 pages : **ne jamais proposer de
la regonfler**, ni d'ajouter un palier, sans passer par
`rushiti-keyword-map`.
