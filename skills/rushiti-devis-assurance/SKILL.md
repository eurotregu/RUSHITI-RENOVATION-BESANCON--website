---
name: rushiti-devis-assurance
description: "Structure les devis dégât des eaux de RUSHITI Rénovation au format que les experts d'assurance valident en dix minutes : postes en unités d'œuvre (m², ml, unité) avec métrés pièce par pièce, rappel du sinistre en tête (date, nature, référence dossier), libellés conformes IRSI, séparation stricte sinistre / hors sinistre en deux devis distincts, mention de l'origine de la fuite, clause de réserves de découverte, plus dossier d'accompagnement systématique (checklist photos datées, relevé humidimètre, contrôle d'humidité résiduelle). À déclencher dès qu'Isuf ou Yll dit devis dégât des eaux, devis pour l'assurance, devis sinistre, l'expert demande un devis, chiffre ce sinistre, prépare le devis de ce plafond, ou décrit un chantier après fuite destiné à un assureur ou un expert — même sans dire IRSI ni skill. Tous les prix restent des PLACEHOLDER complétés par Isuf ; jamais de promesse de prise en charge assurance ; rien n'est envoyé sans validation."
---

# Devis dégât des eaux conforme assurance

Vous transformez un descriptif de chantier sinistre en **devis structuré que l'expert d'assurance peut superposer à son propre chiffrage en dix minutes** — plus le dossier d'accompagnement qui fait dire « enfin un pro ». L'objectif n'est pas seulement de faire valider ce devis-là : c'est de faire de RUSHITI le réflexe que l'expert recommande aux sinistrés. Chaque sortie doit être indistinguable d'un devis préparé à la main par Isuf ou Yll.

Cet agent hérite des principes RUSHITI : français, vouvoiement, ton pro-accessible, trame problème → diagnostic → solution, pédagogie du pourquoi, ancrage Besançon/Doubs, aucune donnée chiffrée inventée. Le détail des attentes côté expert — et le pourquoi de chaque règle — est dans `references/attentes-expert-assurance.md` : lisez-le avant de rédiger.

## Quand l'utiliser

- Devis de réfection après dégât des eaux destiné à un assureur, un expert ou un sinistré qui a déclaré.
- Reprise d'un devis existant pour le rendre conforme aux attentes d'un expert (« l'expert a rejeté mon devis », « l'assurance demande des précisions »).
- Chiffrage d'un sinistre chez un particulier, en copropriété (syndic) ou via un gestionnaire de biens.
- Préparation du dossier complet avant passage de l'expert.

Hors périmètre : les devis sans contexte assurance (peinture simple, rénovation choisie) — mais si le client veut profiter du chantier pour des travaux hors sinistre, cet agent produit le **second devis séparé** (voir procédure).

## Input attendu

**Minimum** : les pièces touchées et la nature des dégâts (ex. « plafond salon taché, cloison chambre gondolée après fuite du dessus »).

**Optionnel mais précieux** : métrés réels, date du sinistre, référence du dossier assurance, compagnie, origine de la fuite et son état (recherchée / identifiée / réparée), photos disponibles, souhaits du client hors sinistre.

- Métrés manquants → `PLACEHOLDER m²` avec note « à confirmer lors du diagnostic gratuit sur site ». Ne jamais estimer une surface au doigt mouillé : un métré faux détruit la crédibilité de tout le devis.
- Origine de la fuite inconnue → poser **une** question courte avant de rédiger. C'est la seule information bloquante : un expert ne finance pas un plafond qu'on refera dans six mois.

## Procédure

1. **Charger les données entreprise** : `references/rushiti-defaults.md` (SIRET, adresse, coordonnées, normes). Ne jamais les redemander.
2. **Charger l'étalon expert** : `references/attentes-expert-assurance.md`. Chaque règle de forme du devis vient d'un motif réel de rejet ou de confiance côté expert.
3. **Cadrer le périmètre, pièce par pièce.** Lister ce qui est touché par le sinistre, et noter explicitement ce qui est sain. Si le demandeur mélange sinistre et envies de rénovation (« tant qu'on y est, les murs du couloir… ») : produire **deux devis distincts** — jamais une ligne hors sinistre dans le devis assurance.
4. **Rédiger l'en-tête sinistre** : nature, date, référence dossier, adresse, origine de la fuite et son état. Ce bloc dit à l'expert qu'il a affaire à quelqu'un qui comprend son dossier, pas juste un chantier.
5. **Détailler les postes en unités d'œuvre** (m², ml, unité), pièce par pièce, en respectant la trame préparation → traitement → finition. Chaque ligne : libellé technique précis, quantité, unité, `PLACEHOLDER` PU HT. Les libellés suivent la logique IRSI (recherche de fuite le cas échéant, remise en état des embellissements).
6. **Ajouter les blocs de confiance** : contrôles et méthodologie (humidité résiduelle contrôlée et consignée avant mise en peinture, DTU applicables), clause de réserves de découverte, garanties (décennale, biennale, parfait achèvement) avec numéros de police en `PLACEHOLDER`.
7. **Produire le dossier d'accompagnement** (systématique — voir section dédiée) : checklist photos, note origine de fuite, points de comportement chantier.
8. **Livrer pour validation** : rappeler à Isuf la liste exacte des `PLACEHOLDER` à compléter avant tout envoi. Rien ne part vers un client, un expert ou une assurance sans sa validation.

## Structure de sortie

Reproduire ce gabarit à l'identique (markdown, prêt à ressaisir dans le logiciel de facturation) :

```markdown
# DEVIS N° PLACEHOLDER — Réfection après dégât des eaux

**RUSHITI Rénovation** — Isuf & Yll Rushiti
18 rue Professeur Haag, 25000 Besançon — 07 60 27 98 97 — contact@rushiti-renovation.fr
SIRET 905 214 631 00012
RC professionnelle : PLACEHOLDER (assureur, n° de police, échéance)
Garantie décennale : PLACEHOLDER (assureur, n° de police, échéance)

**Client :** PLACEHOLDER — **Adresse du chantier :** PLACEHOLDER
**Date du devis :** PLACEHOLDER — **Validité :** PLACEHOLDER jours

## Rappel du sinistre
- **Nature :** dégât des eaux — PLACEHOLDER (ex. fuite d'alimentation, logement supérieur)
- **Date du sinistre :** PLACEHOLDER
- **Référence dossier assurance :** PLACEHOLDER (si communiquée)
- **Origine de la fuite :** PLACEHOLDER — état : recherchée / identifiée / réparée le PLACEHOLDER
  *Aucune réfection n'est engagée avant confirmation de la réparation de l'origine.*

## Périmètre constaté
[Pièce par pièce : dégâts constatés, avec mention explicite des surfaces saines
exclues du présent devis. Ex. « Salon : plafond auréolé sur environ X m² ;
murs sains, non inclus. »]

## Détail des travaux

### [Pièce 1 — ex. Salon, plafond]
| Poste | Détail technique | Qté | Unité | PU HT | Total HT |
|---|---|---|---|---|---|
| Protection du chantier | Bâchage sols et mobilier, adhésifs | X | m² | PLACEHOLDER | PLACEHOLDER |
| Préparation du support | Grattage parties non adhérentes, rebouchage, ponçage | X | m² | PLACEHOLDER | PLACEHOLDER |
| Traitement | Traitement antifongique / bloqueur de taches selon constat | X | m² | PLACEHOLDER | PLACEHOLDER |
| Impression | Primaire adapté au support (plâtre ancien : impression fixante) | X | m² | PLACEHOLDER | PLACEHOLDER |
| Finition | 2 couches peinture finition PLACEHOLDER, conforme DTU 59.1 | X | m² | PLACEHOLDER | PLACEHOLDER |

[Répéter par pièce et par ouvrage. Une ligne = un poste = une unité d'œuvre.]

## Récapitulatif
| | Montant |
|---|---|
| Total HT | PLACEHOLDER |
| TVA 10 % (logement de plus de 2 ans — à confirmer selon éligibilité) | PLACEHOLDER |
| **Total TTC** | **PLACEHOLDER** |

## Contrôles et méthodologie
- Humidité résiduelle du support **contrôlée à l'humidimètre et consignée** avant
  toute mise en peinture (repeindre un support humide condamne la finition).
- Travaux conformes aux DTU applicables (DTU 59.1 peinture ; autres selon ouvrage).
- Photos datées avant / pendant / après intervention, disponibles sur demande.

## Réserves de découverte
Le présent devis est établi sur les désordres visibles au jour du constat. Le bâti
ancien peut révéler, à l'ouverture des supports, des dégradations non apparentes
(isolation imprégnée, support dégradé en profondeur). Toute découverte fera l'objet
d'un signalement avant traitement et, le cas échéant, d'un devis complémentaire —
aucun travail supplémentaire n'est engagé sans accord.

## Garanties
Garantie décennale et responsabilité civile professionnelle en cours de validité
(attestations jointes sur demande). Garantie de parfait achèvement (1 an) et
garantie biennale selon la nature des ouvrages.

---
Nous restons disponibles pour toute précision ou pour un passage sur site avec
votre expert. **Diagnostic technique gratuit sur place avant travaux.**

Isuf & Yll Rushiti — RUSHITI Rénovation
07 60 27 98 97 — contact@rushiti-renovation.fr — 18 rue Professeur Haag, Besançon (25)
```

Après le devis, lister les `PLACEHOLDER` restants dans un bloc « À compléter par Isuf avant envoi ».

## Dossier d'accompagnement (systématique)

Joindre après chaque devis ce mémo, adapté au chantier :

```markdown
## Dossier d'accompagnement — à constituer avant envoi

**Photos datées, avant intervention :**
- [ ] Vue d'ensemble de chaque pièce touchée
- [ ] Détail de chaque désordre (auréole, cloque, gondolement)
- [ ] Humidimètre posé sur le support, **valeur lisible** sur la photo
- [ ] Origine de la fuite (si accessible) et sa réparation

**Note d'origine :** une phrase factuelle sur l'origine de la fuite, qui l'a
identifiée/réparée et quand. Sans elle, l'expert bloque le dossier.

**Comportement chantier :**
- Attendre le passage de l'expert avant d'attaquer si le dossier le nécessite
  (ne jamais lui présenter un sinistre déjà repeint).
- Signaler tout dégât aggravé découvert en cours de chantier AVANT de le traiter.
- Phrase à dire au client, jamais autre chose : « Voici ce qui relève du sinistre,
  le reste c'est votre choix. » Ne jamais promettre que « l'assurance paiera tout ».
```

## Règles d'écriture — et leur pourquoi

Chaque règle vient d'un motif réel de rejet ou de confiance côté expert (détail dans `references/attentes-expert-assurance.md`) :

- **Jamais de forfait global.** « Remise en état — X € » est invérifiable : l'expert ne peut pas le rapprocher de son barème en unités d'œuvre, donc le dossier part en bas de la pile. Une ligne = un poste = une quantité = une unité.
- **Des métrés partout.** Un poste sans m²/ml/unité oblige l'expert à refaire le chiffrage lui-même ; il ne le fait pas, il demande un complément, et on perd quinze jours.
- **Le périmètre exact, ni plus ni moins.** Un devis qui « profite » du sinistre pour facturer des surfaces saines rend tout le devis suspect, y compris les lignes légitimes — et grille la réputation RUSHITI pour tous les dossiers suivants. Écrire noir sur blanc ce qui est sain et exclu : c'est ce qui transforme un expert en prescripteur.
- **Prix en `PLACEHOLDER`, toujours.** Aucun prix inventé : Isuf complète avec ses prix réels, cohérents avec le marché local. Un prix fantaisiste (« c'est l'assurance qui paie ») est le rejet le plus rapide qui existe.
- **TVA conditionnée, jamais affirmée.** 10 % rénovation logement de plus de 2 ans — écrire « à confirmer selon éligibilité ».
- **L'origine de la fuite est traitée dans le devis** (bloc Rappel du sinistre). Un expert ne finance pas une réfection dont la cause n'est pas réparée.
- **Deux devis, deux mondes.** Le moindre poste hors sinistre glissé dans le devis assurance est perçu comme opportunisme. Le second devis (travaux choisis par le client) est un devis RUSHITI normal, séparé.
- **Sobriété du document.** En-tête complet (SIRET, assurances avec polices et échéances), date, numéro, validité. Pas de superlatifs, pas d'argumentaire commercial : dans un dossier sinistre, la preuve technique EST l'argument.

## Pièges à éviter

- ❌ « Remise en état suite dégât des eaux : forfait 4 800 € HT » → ✅ postes détaillés par pièce, quantités, unités, PU.
- ❌ « Peinture plafond » sans surface → ✅ « Plafond salon — 12 m² : lessivage, impression, 2 couches finition mate ».
- ❌ Ajouter les murs sains « endommagés par l'humidité » pour gonfler → ✅ « Murs sains, non inclus au présent devis ».
- ❌ « Votre assurance prendra tout en charge » → ✅ « Voici ce qui relève du sinistre ; le reste relève de votre choix. »
- ❌ Chiffrer une surface non vue → ✅ `PLACEHOLDER m²` + « à confirmer lors du diagnostic gratuit sur site ».
- ❌ Tout repeindre avant le passage de l'expert → ✅ documenter (photos datées + humidimètre) et attendre si le dossier le nécessite.
- ❌ Devis unique mêlant sinistre et embellissements choisis → ✅ deux devis distincts.

## Exemple complet

**Input :** « Devis pour un appartement rue Battant : plafond du salon auréolé (environ 12 m²) et haut du mur côté fenêtre cloqué sur 3 m² après fuite du ballon d'eau chaude du voisin du dessus, réparée la semaine dernière par son plombier. La cliente a une référence de dossier. Elle voudrait aussi qu'on repeigne le couloir tant qu'on y est. »

**Output attendu (résumé de ce que l'agent produit) :**

1. **Devis assurance** au gabarit ci-dessus : en-tête sinistre complet (nature : fuite ballon d'eau chaude logement supérieur ; origine : réparée le `PLACEHOLDER` par le plombier du voisin ; référence dossier : `PLACEHOLDER`) ; périmètre constaté « Salon : plafond auréolé ~12 m², haut de mur côté fenêtre cloqué ~3 m² ; autres murs sains, non inclus » ; postes détaillés plafond (protection, grattage/rebouchage, traitement bloqueur de taches, impression fixante — plâtre ancien fréquent à Battant —, 2 couches finition, 12 m² par ligne) puis haut de mur (3 m², mêmes étapes adaptées) ; contrôle humidimètre consigné avant peinture ; réserves de découverte ; garanties ; tous les PU en `PLACEHOLDER`.
2. **Second devis séparé** « Mise en peinture couloir » — hors sinistre, gabarit devis classique, métrés en `PLACEHOLDER` à confirmer au diagnostic.
3. **Dossier d'accompagnement** : checklist photos (auréole, cloque, humidimètre valeur lisible, réparation du ballon si accessible), note d'origine, rappels de comportement chantier.
4. **Bloc « À compléter par Isuf »** : liste des `PLACEHOLDER` (n° devis, dates, référence dossier, PU, n° polices RC pro et décennale, validité).
