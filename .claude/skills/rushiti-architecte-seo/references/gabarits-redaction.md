# Gabarits de rédaction — les 4 livrables et les structures de contenu

L'architecte livre toujours le **paquet complet A-B-C-D**. Un contenu sans
brief part dans tous les sens ; un contenu sans checklist s'intègre mal ; un
contenu sans plan de suivi ne s'améliore jamais. Les gabarits ci-dessous sont
reproduits à l'identique.

## Livrable A — Brief récapitulatif

Si un brief `rushiti-brief-seo` existe, le résumer ici et s'y conformer (ne
pas le refaire). Sinon, produire ce cadrage minimal :

```markdown
## A. Brief — « <mot-clé principal> »
- **Type** : article satellite / enrichissement de page pilier
- **Silo & pilier** : <silo> → <URL de la page pilier maillée>
- **Intention** : <commerciale / informationnelle> + <locale / B2B / urgence>
- **Verdict PORTA (rushiti-keyword-map)** : <LEJOHET / LEJOHET ME KUSHTE +
  obligations / renfort d'une page existante> — <date>
- **Variantes à placer** : <3-6 formulations naturelles>
- **Angle différenciant RUSHITI** : <ce que la SERP ne dit pas et que 20 ans
  de terrain permettent de dire>
- **Protocoles applicables** : <PRIX / DÉGÂT DES EAUX / BÂTI ANCIEN /
  SYNDIC-COPRO / aucun> + AEO (toujours)
- **Longueur cible** : <voir repères ci-dessous>
```

## Livrable B — Contenu intégral

### Structure d'un article satellite

```markdown
## B. Contenu — prêt à valider

**Title (≤ 60 car.)** : <mot-clé + bénéfice, marque en fin si la place le permet>
**Meta (150-160 car.)** : <bénéfice concret + CTA « Diagnostic gratuit sur place »>
**Slug proposé** : <selon la convention relevée sur le site>

# <H1 : le problème ou la question, formulé comme le client le vit>

<Introduction, 100-180 mots : le problème vécu (ce que le client voit, sent,
craint), puis la promesse de l'article. Trame RUSHITI dès la première ligne :
on nomme ce qu'il vit, pas ce qu'on vend.>

**L'essentiel** (articles longs uniquement)
- <3 à 5 puces factuelles, autoporteuses, citables telles quelles>

## <H2 en question réelle : « Pourquoi… », « Comment… », « Que faire… »>
<Réponse directe dans la première phrase (40-60 mots autoporteurs), puis le
pourquoi — le diagnostic, la cause, ce que l'œil du métier voit.>

## <H2 suivant — le diagnostic s'approfondit>
<Le regard technique : causes possibles, ce qu'on vérifie sur place, les
signes qui changent le traitement. C'est ici que les 20 ans de métier parlent.>

> **Le réflexe de l'artisan** — <1-3 encadrés par article : le détail de
> terrain que seul quelqu'un qui l'a fait cent fois connaît.>

## <H2 — la solution complète : préparation + traitement + finition>
<Étapes numérotées. Expliquer le pourquoi de chaque étape. Citer la norme
utile (DTU 59.1, 25.41, 53.12…) et l'expliquer en une demi-phrase.>

<Tableau comparatif quand le sujet s'y prête (finitions, matériaux, options)
— des critères techniques honnêtes, y compris les limites de chaque option.>

## <H2 optionnel — cas particuliers, erreurs à éviter, contexte bisontin>
<Uniquement si le sujet le justifie : bâti ancien, climat, copropriété…>

## Questions fréquentes
<3 à 5 Q/R format client (réponse directe en première phrase, 40-80 mots).
Bloc complet + FAQPage JSON-LD → router vers rushiti-faq, qui fait foi.>

<CTA final : rappel du diagnostic technique gratuit sur place, devis détaillé
sans engagement — puis coordonnées : RUSHITI Rénovation · 07 60 27 98 97 ·
contact@rushiti-renovation.fr · 18 rue du Professeur Haag, 25000 Besançon.>
```

**Annexes du livrable B** (après le contenu) :

```markdown
### Maillage prévu
| Sens | Page | Ancre / phrase d'insertion |
|---|---|---|
| Sortant (1er lien) | <page pilier> | <ancre descriptive> |
| Sortant | <contenu frère> | <ancre> |
| Entrant | <pages à modifier> | → plan détaillé via rushiti-maillage-interne |

### Images
| Emplacement | Sujet | Alt text (descriptif + signal local, sans bourrage) |
|---|---|---|

### Données structurées recommandées
<Types : Article ou BlogPosting + FAQPage + BreadcrumbList. Le JSON-LD
lui-même est produit par schema-builder — jamais recopié de mémoire.>
```

**Repères de longueur** (calibrés sur la requête, pas sur un chiffre fétiche) :
article satellite **1 200 à 2 000 mots** — assez pour couvrir UN problème à
fond (règle d'or), jamais du remplissage pour atteindre un total. Un sujet
épuisé en 900 mots honnêtes vaut mieux que 2 000 mots délayés ; un sujet qui
en demande 2 500 devient deux satellites (à repasser par PORTA).

### Structure d'un enrichissement de page pilier

Le risque n°1 du site (audit du 20/08/2026) est la **quasi-duplication du
template** entre pages services. Un enrichissement ne reproduit donc jamais
l'ossature commune : il ajoute de la matière **propre au service** — viser
au moins 500-800 mots réellement uniques hors blocs communs :

- pathologies et supports propres au service (ce qu'on rencontre à Besançon) ;
- le déroulé réel d'un chantier type (étapes, points de contrôle, séchage) ;
- les choix techniques expliqués (produits, finitions, quand ils s'imposent) ;
- la section « Pour aller plus loin » qui maille les satellites du silo.

Livrer chaque ajout avec son emplacement précis dans la page existante
(« après la section … »), en reprenant le balisage du gabarit fourni — jamais
une structure inventée.

## Livrable C — Checklist d'optimisation

```markdown
## C. Checklist avant intégration
**On-page** : ☐ title ≤ 60 car., mot-clé en tête ☐ meta 150-160 car. + CTA
☐ un seul H1 ☐ Hn hiérarchiques, formulés en questions réelles
☐ variantes du mot-clé placées naturellement (zéro bourrage)
**Cocon** : ☐ 1er lien → page pilier ☐ 3-8 liens sortants, ancres descriptives
☐ liens entrants demandés à rushiti-maillage-interne ☐ aucun lien vers
rushiti.fr / rushiti-peinture.fr
**AEO / entités** : ☐ réponses directes en 1re phrase ☐ bloc « L'essentiel »
si long ☐ RUSHITI Rénovation + service + zone associés dans le texte
☐ E-E-A-T : expérience terrain concrète, normes expliquées
**Conformité RUSHITI** : ☐ trame problème → diagnostic → solution ☐ vouvoiement,
zéro jargon creux ☐ aucun prix/délai/TVA/garantie non validé (PLACEHOLDER)
☐ compteurs (avis, note) vérifiés du jour ou absents ☐ CTA + coordonnées NAP
exactes ☐ logo prévu sur la page ☐ RGPD photos/témoignages
**Intégration** : ☐ alt texts fournis ☐ schéma recommandé (→ schema-builder)
☐ FAQ alignée texte visible = JSON-LD (→ rushiti-faq) ☐ passage
rushiti-humanisateur si le texte sent la machine
```

## Livrable D — Plan de suivi (jamais de projection chiffrée)

Les promesses de trafic et de position sont interdites : un plan de suivi
donne des **directions de travail mesurables**, pas des prophéties.

```markdown
## D. Plan de suivi
- **Requêtes à suivre dans GSC** : <mot-clé principal + 2-4 variantes>
- **Effet attendu (qualitatif)** : <fort / moyen / faible> parce que <preuve :
  demande observée dans GSC, SERP faible, page pilier qui imprime déjà…>
- **Points de contrôle** : indexation de l'URL (Search Console) sous quelques
  jours ; impressions/position à 4-6 semaines (rushiti-gsc) ; opportunités
  CTR une fois positionné (rushiti-ctr-opportunites) ; baseline et régressions
  (rushiti-regression-seo)
- **Rafraîchissement** : <déclencheur : saisonnalité, donnée périssable,
  norme à re-vérifier> (rushiti-refresh-planner)
- **Attend validation d'Isuf** : <liste des PLACEHOLDER et décisions ouvertes>
```
