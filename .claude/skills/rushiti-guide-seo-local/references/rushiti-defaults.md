# Données par défaut RUSHITI Rénovation

> **Version 5 — 24/08/2026.** Fichier de référence unique de la suite RUSHITI. Il fusionne l'ancien `rushiti-defaults.md` et l'ancien `donnees-rushiti.md` (Google Ads). Il prime sur toute copie antérieure. Toute correction se fait ici, puis se propage aux skills.

Ces informations sont **stables**. Un agent les auto-remplit sans jamais les redemander à Isuf. Pour tout autre client/site, ou pour toute donnée non validée, utiliser `[À COMPLÉTER]`.

## Identité entreprise

| Champ | Valeur |
|---|---|
| Dénomination sociale | Rushiti |
| Forme juridique | SARL — capital 1 000 €, créée le 04/11/2021 (source RCS) |
| Code APE / NAF | 43.34Z — Travaux de peinture et vitrerie |
| Nom commercial | RUSHITI Rénovation |
| Co-gérants | Isuf & Yll Rushiti |
| Expérience | 20 ans de métier (Isuf) |
| SIRET | 90521463100012 |
| RCS | Besançon 905 214 631 |
| TVA intracommunautaire | FR89905214631 |
| Garantie décennale | Assureur ERGO — n° de contrat `[À COMPLÉTER]` |
| Adresse | 18 rue du Professeur Haag, 25000 Besançon, Doubs (25), France |
| Téléphone | 07 60 27 98 97 |
| Email | contact@rushiti-renovation.fr |
| Site | rushiti-renovation.fr (aussi rushiti.fr — arbitrage en attente) |
| Logo | À placer sur **chaque page web** générée |

### Règle NAP — à respecter au caractère près

L'adresse s'écrit **« 18 rue du Professeur Haag »**, avec « du ». C'est la graphie affichée sur la **fiche Google Business**, confirmée par Isuf le 15/08/2026, et celle qu'utilisent déjà les deux sites, leur balisage JSON-LD et l'ensemble des annuaires.

**Le RCS et la Base Adresse Nationale, eux, écrivent l'adresse sans l'article « du ».** C'est normal : ce sont des formes administratives normalisées. On ne s'aligne pas dessus. La règle du NAP est de reproduire **exactement ce qu'affiche la fiche Google Business**, parce que c'est la source que Google recoupe avec toutes les autres. Une graphie qui varie d'un annuaire à l'autre affaiblit le signal local.

Seule exception : un document strictement administratif qui reproduit l'extrait Kbis peut porter la forme du registre. Partout ailleurs — site, JSON-LD, fiche Google, annuaires, signatures d'emails, devis, factures, courriers — c'est la forme avec « du ».

Formats normalisés à utiliser selon le contexte :

| Contexte | Format |
|---|---|
| Texte courant, signature, courrier | 18 rue du Professeur Haag, 25000 Besançon |
| JSON-LD `streetAddress` | `18 rue du Professeur Haag` |
| JSON-LD `telephone` | `+33760279897` |
| Téléphone affiché | 07 60 27 98 97 |

Casse : « rue » en minuscules, « Professeur Haag » avec majuscules. Ne pas alterner « Rue » et « rue » sur une même page.

> Vérifier les coordonnées auprès d'Isuf avant toute publication officielle (un email ou un téléphone obsolète en production coûte des leads). En cas de doute sur une donnée variable : `[À COMPLÉTER]`.

## Distinction dénomination sociale / nom commercial

- **« Rushiti »** est la dénomination sociale : elle sert dans les mentions légales, sur les devis et factures, dans les documents administratifs et contractuels, et partout où l'entité juridique est engagée. Elle s'accompagne du SIRET, du RCS et du numéro de TVA.
- **« RUSHITI Rénovation »** est le nom commercial : c'est lui qui apparaît en communication — site, fiche Google Business, réseaux sociaux, publicité, signatures, panneaux de chantier.
- La forme juridique est **SARL** (source RCS). Écrire « SARL Rushiti » ou « Rushiti, SARL » dans un document légal est donc exact. En revanche, ne jamais inventer d'autre forme (« Rushiti SAS », « Entreprise Rushiti », « Rushiti Rénovation SARL » — le nom commercial n'est pas la raison sociale).

## Charte graphique (Guidelines RUSHITI v2.7)

| Rôle | Couleur |
|---|---|
| Primaire — bleu nuit | `#002B4B` |
| Secondaire — bleu | `#1A75BB` |
| Positif — vert | `#016738` |
| Alerte — rouge | `#EB1C24` |

> Le document « Guidelines RUSHITI v2.7 » fait foi et prime sur toute version antérieure.

## Services principaux

- Peinture intérieure / extérieure, toutes finitions
- Pose de papier peint et toile de verre
- Plâtrerie, pose de placo (BA13), faux plafonds
- Isolation (intérieure, combles)
- Revêtements de sol : parquet flottant et stratifié, PVC, moquette, lino
- Réparation après dégât des eaux
- Ragréage de sol intérieur
- Rénovation de chambres, salles de bains, cuisines
- Aménagement de bureaux et commerces

> **Orthographe :** on écrit **ragréage**, avec un « a » en première syllabe — du verbe *ragréer*, remettre un sol à niveau avant la pose d'un revêtement. Toute graphie avec un « é » en première syllabe est une faute. Vocabulaire technique du métier : une faute ici décrédibilise le texte devant un client ou un expert d'assurance.

## Clients cibles

Propriétaires de maisons et d'appartements à Besançon · syndics de copropriété · gestionnaires de biens · assurances (sinistres dégât des eaux) · commerces et bureaux locaux.

## Différenciateurs

- Diagnostic technique **gratuit sur site** avant tout devis
- Expertise spécifique du **bâti ancien** du Doubs
- Approche **pédagogique** (expliquer le pourquoi)
- **Solutions complètes** : préparation + traitement + finition

## Normes, garanties et références à citer

- **DTU** applicables selon l'ouvrage (ex. DTU 59.1 travaux de peinture, DTU 25.41 plaques de plâtre, DTU 53.12 revêtements de sol souples **collés** — PVC, linoléum, caoutchouc). La pose clipsée (LVT) n'est couverte par aucun DTU : suivre l'Avis Technique ou la notice du fabricant.
- **Garantie décennale** (gros ouvrage / impropre à destination) — assureur ERGO.
- **Garantie biennale** (bon fonctionnement) et **garantie de parfait achèvement** (1 an).
- Pour les sinistres : structure et libellés conformes **IRSI** (convention d'indemnisation et de recours sinistres immeubles).
- TVA réduite **10 %** (rénovation logement de plus de 2 ans) ou **5,5 %** (rénovation énergétique) selon éligibilité — toujours conditionner, jamais affirmer sans vérifier.

## Garde-fous non négociables

Aucun agent de la suite RUSHITI n'invente :

- un **prix** ou une fourchette de prix non validée par Isuf ;
- un **délai** d'intervention ou de chantier ;
- un **taux de TVA** applicable à un cas précis ;
- une **référence d'assurance** ou un numéro de contrat ;
- une **garantie**, une **certification** ou un **label** ;
- un **avis client** ou un **témoignage** ;
- une **prise en charge assurance** — l'agent ne se substitue jamais à l'assureur.

Toute donnée manquante s'écrit `[À COMPLÉTER]`. Rien n'est publié ni envoyé sans validation d'Isuf. RGPD : accord écrit du client avant toute photo de chantier ou tout témoignage nominatif.

## Quartiers de Besançon (25000) — signaux géo locaux

Centre / Chapelle des Buis · Velotte · Butte-Grette · Battant · Chaprais-Cras · Bregille · Saint-Ferjeux-Rosemont · Montrapon-Montboucons · Saint-Claude-Torcols · Palente-Orchamps-Saragosse · Vaîte-Clairs Soleils · Planoise-Châteaufarine · Les Tilleroyes.

## Communes du Doubs (25) — zones d'intervention

Besançon (25000) · Montbéliard (25200) · Pontarlier (25300) · Thise (25220) · Chalezeule (25220) · Chalèze (25220) · Novillars (25220) · Roche-lez-Beaupré (25220) · Vaire-le-Petit (25220) · Amagney (25220) · Pouilley-les-Vignes (25115) · Pirey (25480) · Miserey-Salines (25480) · École-Valentin (25480) · Franois (25770) · Serre-les-Sapins (25770) · Saône (25660) · Morre (25660) · Montfaucon (25660) · La Vèze (25660) · Fontain (25660) · Gennes (25660) · Châtillon-le-Duc (25870) · Les Auxons (25870) · Tallenay (25870) · Arguel (25720) · Avanne-Aveney (25720) · Beure (25720) · Larnod (25720) · Pugey (25720) · Vaire-Arcier (25720) · Boussières (25320) · Busy (25320) · Chemaudin (25320) · Grandfontaine (25320) · Montferrand-le-Château (25320) · Osselle-Routelle (25320) · Rancenay (25320) · Thoraise (25320) · Torpes (25320) · Vorges-les-Pins (25320) · Audeux (25170) · Champagney (25170) · Champvans-les-Moulins (25170) · Chaucenne (25170) · Mazerolles-le-Salin (25170) · Noironte (25170) · Pelousey (25170) · Vèze (25170) · Braillans (25640) · Champoux (25640) · Chaudefontaine (25640) · Chevillotte (25640) · Gratteris (25640) · Marchaux (25640) · Vaux-les-Prés (25640) · Arçon (25300) · Doubs (25300) · Houtaud (25300) · Vuillecin (25300) · Dannemarie-sur-Crête (25410) · Nancray (25360) · Mamirolle (25620) · Deluz (25960).

## Mots-clés (courte et longue traîne)

Combiner systématiquement : **service** (peintre, plâtrier, plaquiste, dégât des eaux, isolation, rénovation, parquet…) + **signal géo** (Besançon, quartier précis, commune, code postal 25xxx). Exemples longue traîne : « peintre dégât des eaux Planoise Besançon », « pose placo faux plafond École-Valentin », « rénovation salle de bains bâti ancien Battant ».

## Domaines à connaître

| Domaine | État au 15/08/2026 | Usage |
|---|---|---|
| rushiti-renovation.fr | actif | site principal selon ce socle |
| rushiti.fr | actif | second site, contenus similaires — arbitrage en attente |
| rushiti-peinture.fr | **éteint (DNS absent)** | ne plus jamais citer ; encore référencé à tort sur Kompass |
| rushiti-renovation-peintre.localo.site | actif | microsite Localo, hors périmètre éditorial |

Ne jamais écrire `rushiti-peinture.fr` dans un contenu, une fiche ou un devis : le domaine ne répond plus.

## Journal des versions

| Version | Date | Changement |
|---|---|---|
| v5 | 24/08/2026 | Norme sols corrigée : **NF DTU 53.12** remplace le DTU 53.2, obsolète, dans les 12 fichiers de la suite qui le citaient. Source : `docs/seo/dtu-referencat-eeat.md` (vérification norme par norme du 21/08/2026). Précision ajoutée : le 53.12 couvre la pose **collée** (PVC, linoléum, caoutchouc) ; la pose clipsée (LVT) relève de l'Avis Technique du fabricant, aucun DTU ne la couvre. |
| v4 | 15/08/2026 | Adresse alignée sur la fiche Google Business : « 18 rue **du** Professeur Haag » (le RCS et la BAN écrivent sans « du » — écart normal, documenté). Ajout de la forme juridique SARL, du capital, de la date de création et du code APE (source RCS). |
| v3 | 15/08/2026 | Fusion avec `donnees-rushiti.md` (RCS, TVA intracom, décennale ERGO, charte graphique). Ajout dénomination sociale / nom commercial, règle NAP, garde-fous, journal des versions. Correction de la faute d'orthographe sur « ragréage » (graphie avec « é » en première syllabe, présente dans 32 fichiers de la suite). |
| v2 | — | Version canonique précédente, présente en 31 exemplaires. |
