# Article plafond dégât des eaux — enrichissement FAQ — paquet de production RUSHITI

> Produit par `rushiti-architecte-seo` le 30/08/2026, en exécution du plan
> validé `docs/seo/plan-opportunites-visibilite-ia-2026-08-30.md`.
> **Livré en PR de production** :
> [eurotregu/rushiti-renovation#28](https://github.com/eurotregu/rushiti-renovation/pull/28)
> — en attente de fusion par Isuf (fusion = mise en ligne).

## A. Brief

- Type : **enrichissement** d'un satellite existant — jamais de page neuve
  (porte registre : la requête est attribuée à `/blog/reparer-plafond-…`,
  ligne « réparer plafond ou mur après fuite », verdict du 20/08).
- Silo 5 (dégât des eaux) → pilier `/degat-des-eaux-besancon`.
- Requête NEURONwriter : « réparation plafond après dégât des eaux »
  (analyse `9912cf05a52877ab`, PAA relevées le 30/08).
- Constat déclencheur : la page portait un `FAQPage` JSON-LD **sans FAQ
  visible** — défaut de parité, alors que la doctrine du silo est contrôlée
  à 13/13 sur le pilier. Deux questions PAA n'étaient pas couvertes.
- Protocoles : DÉGÂT DES EAUX (jamais de substitution à l'assureur) ·
  PRIX (facteurs, aucun montant) · AEO (réponses autoportantes).

## B. Contenu ajouté (intégral)

Section « Questions fréquentes » (`<details>`, ancre `#faq`, ajoutée au
sommaire), en parité stricte avec le `FAQPage` :

1-4. Les quatre réponses déjà présentes dans le JSON-LD, rendues visibles
à l'identique (réparer / repeindre / temps de séchage / qui paie — IRSI).

5. **Quand faut-il faire appel à un professionnel pour un plafond touché
par un dégât des eaux ?** — « Dès que la peinture se décolle en plaques,
que le plâtre sonne creux ou que des points noirs apparaissent dans les
angles : ces signes indiquent que l'eau a dépassé la surface visible. Un
professionnel mesure l'humidité réelle du support et détermine ce qui se
conserve et ce qui se dépose. Le diagnostic est gratuit, sur place, à
Besançon et dans le Doubs. »

6. **De quoi dépend le prix de la réparation d'un plafond après un dégât
des eaux ?** — « De la surface réellement touchée, de la nature du plafond
(plaque de plâtre ou plâtre sur lattis), de la durée d'assèchement et d'un
éventuel traitement anti-moisissure. Aucun montant sérieux ne s'annonce
sans mesure : le devis se chiffre après diagnostic gratuit sur place,
poste par poste, dans un format lisible par votre assureur. »

Également : `dateModified` → 2026-08-30. Sur `/contact`, phrase de réponse
directe ajoutée au chapeau : « Le devis est gratuit pour tous nos travaux —
peinture, plâtrerie-placo, sols, isolation, réparation après dégât des
eaux : visite sur place, relevé des surfaces, puis devis poste par poste. »

## C. Checklist d'optimisation

- ✅ Aucune page neuve (anti-cannibalisation respectée)
- ✅ Parité FAQ visible ↔ `FAQPage` : 6/6 identiques (contrôle automatique)
- ✅ JSON-LD revalidé (`json.loads`) sur les 2 pages : 0 invalide
- ✅ `verifiko_degat_des_eaux.py` : 76 pages du silo, 0 erreur, 0 avertissement
- ✅ Aucun prix, délai, promesse ou chiffre inventé ; question prix traitée
  par les facteurs uniquement (distincte de la FAQ prix du pilier)
- ✅ NAP et coordonnées inchangés

## D. Plan de suivi

- Requêtes GSC à suivre : « réparation plafond après dégât des eaux »,
  « plafond dégât des eaux », « repeindre plafond dégât des eaux »
  (référence : `reparer-mur` portait 11 impr IA au relevé du 19/08 ;
  l'article plafond n'avait pas de relevé IA propre).
- Prompts de test de citation IA (session neuve, formulation exacte) :
  1. « Qui peut réparer un plafond abîmé par un dégât des eaux à Besançon ? »
  2. « Combien de temps sécher un plafond avant de repeindre ? »
  3. « Comment obtenir un devis gratuit pour des travaux de peinture à Besançon ? »
- Mesure via `rushiti-regression-seo` à 4-6 semaines **après fusion** de la
  PR #28 ; part de voix via `rushiti-part-de-voix-ia` (relevé de septembre).
- Effet attendu qualitatif (jamais promis) : moyen à fort sur l'article —
  la thématique DDE du site imprime déjà en surfaces IA (95 impr IA sur
  l'article moisissure, relevé du 19/08).

**En attente d'Isuf : fusion de la PR #28 (fusion = mise en ligne).**
