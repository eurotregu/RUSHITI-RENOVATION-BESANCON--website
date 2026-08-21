# Protocoles spéciaux de rédaction

Quatre familles de sujets exigent des règles renforcées. Le brief (livrable A)
déclare toujours quels protocoles s'appliquent ; plusieurs peuvent se cumuler
(un article « prix d'une réfection après dégât des eaux dans un immeuble
ancien » les cumule presque tous).

## Protocole PRIX (« prix », « combien coûte », « budget », « tarif »)

Les pages budget convertissent — à condition d'être honnêtes. Un prix nu
n'inspire pas confiance ; un prix expliqué, oui. Et un prix inventé détruit la
crédibilité au premier devis réel.

- **Aucun chiffre sans validation.** Toute fourchette s'écrit
  `[FOURCHETTE À VALIDER PAR ISUF — €/m²]` tant qu'Isuf n'a pas donné ses
  valeurs. L'article peut être entièrement rédigé autour des PLACEHOLDER :
  la pédagogie des facteurs de prix, elle, n'attend pas.
- **Expliquer ce qui fait varier le prix** — c'est le vrai contenu : surface
  et hauteur sous plafond, état du support (un mur ancien à reprendre coûte
  plus qu'un placo neuf), nombre de couches, produits choisis, accès et
  protection du mobilier, dépose éventuelle de l'existant.
- **Toujours une fourchette, jamais un prix fixe** : « à partir de » ou
  « entre X et Y », avec la raison de l'écart. Le prix précis n'existe
  qu'après le diagnostic gratuit sur place — c'est le CTA naturel de la page.
- **Disclaimer obligatoire** : « Prix indicatifs — le devis précis se fait
  après le diagnostic technique gratuit sur place. »
- **TVA conditionnée, jamais affirmée** : 10 % (logement de plus de 2 ans) ou
  5,5 % (rénovation énergétique) *selon éligibilité*, avec la condition dans
  la même phrase.
- Interdits : « le moins cher », « imbattable », toute comparaison de prix
  avec un concurrent nommé.

## Protocole DÉGÂT DES EAUX

Le lecteur vit une situation stressante : plafond taché, assurance à gérer,
peur que ça revienne. Le ton est sérieux, posé, rassurant par la compétence —
jamais alarmiste pour vendre.

- **Ouvrir sur le vécu** : l'auréole qui s'étale, l'odeur, le doute sur ce que
  cache le plafond — puis montrer le diagnostic : l'eau s'infiltre dans les
  murs, l'isolation, les sols ; **les dégâts visibles sous-estiment l'ampleur
  réelle**. C'est le cœur de l'expertise RUSHITI sur ce sujet.
- **La chronologie technique fait le plan** : stopper la cause → sécher
  (mesures à l'humidimètre, pas « au doigt ») → traiter (antifongique si
  besoin) → reprendre le support → finition. Expliquer **pourquoi repeindre
  trop tôt fait revenir l'auréole** : c'est LA question que tout le monde se
  pose.
- **Parler le langage assurance sans se substituer à l'assureur** : décrire le
  déroulé (déclaration, expertise, devis conforme IRSI, photos datées) ;
  jamais « votre assurance prendra en charge » — la prise en charge est la
  décision de l'assureur, écrire au conditionnel et renvoyer au contrat.
- **L'urgence est légitime ici** (limiter les dégâts, documenter tôt) : un
  « contactez-nous rapidement » est justifié — sans délai d'intervention
  chiffré non validé.
- Routage : devis sinistre → `rushiti-devis-assurance` ; courrier à
  l'assurance ou au syndic → `rushiti-courriers-clients`.

## Protocole BÂTI ANCIEN

Le bâti ancien est LE différenciateur éditorial de RUSHITI : peu de
concurrents savent en parler avec précision. Justement pour cela, zéro
approximation.

- **Être spécifique ou se taire** : murs en pierre calcaire, plâtre
  traditionnel, grandes hauteurs sous plafond, humidité de remontée ou de
  condensation, enduits anciens farinants. Le « charme de l'ancien » sans
  contenu technique est du remplissage.
- **La préparation avant la finition** : sonder le support, purger ce qui ne
  tient plus, choisir des produits compatibles avec un mur qui doit respirer
  — expliquer pourquoi une peinture étanche sur un mur humide déplace le
  problème au lieu de le régler.
- **Le climat franc-comtois comme facteur technique** : hivers froids et
  humides, condensation sur les murs nord, pièces peu ventilées — il
  conditionne produits, ventilation et délais de séchage. Pas un ornement.
- **Géographie canonique** : les quartiers s'écrivent selon la liste de
  `donnees-rushiti.md` (Centre / Chapelle des Buis, Battant, Chaprais-Cras…).
  « La boucle du Doubs » peut décrire le site géographique, mais n'est pas un
  nom de quartier cible.
- Les 20 ans de métier se **montrent** (ce qu'on trouve derrière un doublage
  des années 70, comment on reconnaît un plâtre qui farine) au lieu de
  s'affirmer.

## Protocole SYNDIC / COPRO / GESTIONNAIRES (B2B)

Le lecteur est un professionnel qui gère des immeubles, des AG et des
occupants. Il achète de la fiabilité d'exécution, pas du rêve.

- Arguments dans son langage : un seul interlocuteur, planning tenu et
  communiqué aux occupants, protection des parties communes, chantier propre,
  décennale + RC pro à jour, devis détaillé par poste utilisable en AG ou en
  conseil syndical.
- Cas types : cage d'escalier, halls, remise en état entre locataires, suivi
  des sinistres parties communes/privatives (croiser avec le protocole DÉGÂT
  DES EAUX et la logique IRSI).
- Mailler vers la page `/syndic-copropriete-besancon`. Prospection et
  relances → `rushiti-prospection-b2b` / `rushiti-relance-b2b` ; courriers →
  `rushiti-courriers-clients`.

## Protocole transverse AEO / extractibilité (s'applique à tout contenu)

- Chaque H2 en question réelle ; **réponse directe dans la première phrase**
  (40-60 mots autoporteurs — extraits tels quels par les moteurs de réponse).
- Bloc « L'essentiel » (3-5 puces) en tête des articles longs.
- Processus en listes numérotées ; critères en tableaux.
- Entités associées dans le texte : RUSHITI Rénovation + service + zone +
  problème. NAP exact (règle du « du » — voir `donnees-rushiti.md`).
- E-E-A-T : expérience de terrain concrète et datée quand c'est possible,
  normes citées et expliquées, auteur artisan assumé — jamais de superlatif
  invérifiable ni de chiffre sans source.
