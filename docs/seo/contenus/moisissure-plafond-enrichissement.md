# Article moisissure (plafond salle de bain) — paquet de production RUSHITI

> Produit par `rushiti-architecte-seo` le 21/08/2026 (soir), sur commande
> d'Isuf (« prodhojeni » — ligne 1 du plan éditorial automne 2026).
> Page cible : `https://rushiti-renovation.fr/blog/moisissure-plafond-salle-de-bain-besancon`
> — lue en direct le 21/08/2026 (Firecrawl sur le HTML source, statut 200).

## A. Brief — et constat de terrain qui change le périmètre

- **Type** : enrichissement d'un article satellite existant · **Silo** :
  transverse (DDE + peinture + isolation) · **Famille** : pathologie.
- **Porte** : renfort d'existant — pas de création, pas de PORTA. Consigné au
  registre (ligne « moisissure plafond salle de bain », Vala 3, 21/08).
- **Preuves de demande** : « …malgré vmc » 137 impr pos. 11,2 (1re requête du
  site) · cluster ≈ 620 impr / 2 clics · article 1 385 impr/12 m · 3 ancres
  469 impr pos. 9,6 avec 0 clic (export GSC du 20/08).

**⚠️ Constat à la lecture live (ce qui change tout)** : les trois actions du
brief d'origine — H2 « malgré la VMC », bloc conversion « quand appeler un
professionnel », maillage vers dégât des eaux et peinture — **sont déjà en
production**. La page live contient les sections `#vmc` et `#quand`, les liens
vers `/degat-des-eaux-besancon`, `/blog/reparer-plafond-degat-des-eaux-besancon`,
`/peinture-interieure-besancon`, `/isolation-besancon`, `/renovation-salle-de-bain-besancon`,
un bloc auteur E-E-A-T (Isuf, 20 ans, SIRET) et deux sources (ADEME, ANSES).
Reproduire ces sections fabriquerait de la duplication — le paquet couvre donc
**ce qui manque réellement** :

1. le **bloc FAQ** (absent de la page) — 5 questions que la page ne traite pas
   déjà, formulées comme les requêtes réelles ;
2. la **spécification photos avant/après** — le seul item de la Vala 3 encore
   ouvert au registre, bloqué sur la matière RGPD ;
3. une **correction cosmétique** : le pied d'article dit « Les prix cités sont
   des fourchettes moyennes… » alors que l'article ne cite aucun prix.

- **Protocoles appliqués** : AEO (réponses directes) · PRIX (question 4 sans
  aucun chiffre) · prudence juridique/assurance (question 2, conditionnée).

## B. Contenu — les compléments, avec leur emplacement exact

### B1. Bloc FAQ

**Emplacement** : après le bloc CTA « Un doute sur votre chantier à Besançon ou
dans le Doubs ? », avant « Sources & références ». Ajouter l'entrée
« Questions fréquentes » au sommaire avec l'ancre `#faq` (même mécanique que
`#causes`, `#vmc`, `#erreur`, `#methode`, `#prevenir`, `#quand`). Balisage :
reprendre celui de la page (H2 de section + H3 par question) — le HTML
d'intégration se calque sur le gabarit existant du blog, il ne s'invente pas.

```markdown
## Questions fréquentes {#faq}

### La moisissure au plafond de la salle de bain est-elle dangereuse ?

Elle dégrade la qualité de l'air que vous respirez, et le risque augmente
avec la surface touchée et la durée d'exposition — l'ANSES et l'ADEME (citées
en fin d'article) la classent parmi les polluants de l'air intérieur à
traiter. Sans céder à la panique : une tache traitée tôt, avec la cause
réglée, ne laisse pas de séquelle au logement. On ne laisse simplement pas
s'installer un champignon dans une pièce où l'on se lave, encore moins quand
des enfants ou des personnes sensibles vivent dans le logement.

### Locataire ou propriétaire : qui doit traiter la moisissure ?

Cela dépend de la cause — et c'est précisément ce que le diagnostic établit.
Une ventilation défaillante ou un défaut du bâti (VMC hors service, pont
thermique, infiltration) relève en principe du propriétaire ; une condensation
liée à l'usage du logement (pièce jamais aérée, séchage du linge) relève de
l'occupant. En cas de fuite, on bascule dans un sinistre à déclarer à
l'assurance. Chaque situation a ses règles : le constat technique écrit que
nous remettons après diagnostic sert justement de base saine à cette
discussion.

### Quelle peinture choisir pour un plafond de salle de bain ?

Une peinture spéciale pièces humides, lessivable — et seulement sur un support
sain et sec. C'est l'ordre qui compte : aucune peinture, même
« anti-humidité », ne tient sur un plafond dont la cause de condensation n'a
pas été traitée. Une fois le support assaini, la finition adaptée fait la
différence sur la durée : elle supporte les lavages et retarde la
condensation de surface.

### Combien coûte le traitement d'une moisissure au plafond ?

Cela dépend de trois facteurs que seul un examen sur place départage : la
surface touchée, la cause (simple condensation, défaut de ventilation, ou
fuite à reprendre) et l'état du support sous la tache (un enduit à refaire
change le chantier). C'est pourquoi nous commençons par le diagnostic
technique gratuit, sur place : vous savez ce qu'il faut faire — et ce qu'il
ne faut pas faire — avant de parler budget, sur devis détaillé sans
engagement.

### La moisissure peut-elle revenir après un traitement professionnel ?

Non — si la cause a été traitée en même temps que le champignon. C'est toute
la différence avec un nettoyage de surface : tant que la vapeur d'eau
continue de se condenser sur un plafond froid ou mal ventilé, n'importe quel
traitement finit par céder. Notre méthode traite les deux dans l'ordre
(cause, puis support, puis finition), et c'est ce qui rend le résultat
durable.
```

**FAQPage JSON-LD** : à produire par `rushiti-faq` à partir du texte ci-dessus
**mot pour mot** (jamais de FAQ schema sans FAQ visible, jamais deux FAQPage
sur la même page — vérifier le `@graph` existant de l'article avant d'ajouter).

### B2. Photos avant/après — spécification (matière à fournir)

**Emplacement** : dans la section « La méthode pro » (`#methode`), après
l'étape 4. **Matière** : un chantier réel de plafond de salle de bain traité
— `[MATIÈRE À FOURNIR PAR ISUF + accord écrit du client (RGPD)]`. Deux images
légendées distinctes (jamais un montage muet) :

| Image | Légende proposée | Alt text |
|---|---|---|
| Avant | Avant : taches de condensation installées au plafond | Plafond de salle de bain avant traitement anti-moisissure à Besançon : taches noires de condensation |
| Après | Après : support assaini, finition pièces humides | Même plafond après traitement antifongique et peinture spéciale pièces humides — chantier RUSHITI Rénovation |

Aucun élément identifiable (visage, adresse, objet personnel reconnaissable)
dans le cadre.

### B3. Correction du pied d'article (cosmétique)

Le disclaimer actuel — « Les prix cités sont des fourchettes moyennes
constatées dans le Doubs et ne constituent pas un devis » — parle de prix que
l'article ne cite pas. Remplacer par : « Cet article est fourni à titre
informatif. Chaque chantier est chiffré après diagnostic gratuit sur place. »
⚠️ Si ce pied est un gabarit commun à tous les articles du blog, la correction
se décide au niveau du gabarit dans le dépôt de production, pas page par page.

### Maillage

Le maillage prévu par le brief est **déjà en place** (vérifié live) : DDE dans
`#vmc` et « Pour aller plus loin », satellite réparer-plafond dans `#erreur`,
peinture/isolation/contact en fin. La FAQ n'ajoute **aucun lien nouveau** —
elle s'appuie sur ceux qui existent (pas de sur-maillage). Liens entrants vers
l'article : rien à changer, il est la 2e visibilité du site.

## C. Checklist d'optimisation

**Conformité des sections live (vérifiée le 21/08)** : ☑ H2 `#vmc` en
question réelle avec réponse directe en première phrase ☑ bloc conversion
`#quand` + CTA téléphone ☑ trame problème → diagnostic → solution ☑ E-E-A-T
(auteur, SIRET, sources ADEME/ANSES) ☑ aucun prix ni délai inventé ☑ NAP :
téléphone au format `tel:+33760279897` ☑ ancrage local précis (Planoise,
Palente, bâti ancien — quartiers canoniques).

**À valider avant intégration des compléments** : ☐ FAQ : 5 réponses
directes en première phrase, 60-90 mots, zéro chiffre, question 2 conditionnée
(jamais d'affirmation juridique absolue) ☐ FAQPage JSON-LD identique au texte
visible (→ `rushiti-faq`) ☐ ancre `#faq` au sommaire ☐ photos : accord RGPD
écrit AVANT toute intégration ☐ pied d'article : décision gabarit vs page ☐
aucun lien nouveau vers rushiti.fr ☐ passage `rushiti-humanisateur` si un
doute de ton subsiste.

## D. Plan de suivi

- **Requêtes à suivre (GSC)** : « moisissure plafond salle de bain malgré
  vmc » · « moisissure plafond salle de bain » · « plafond moisi salle de
  bain » · « plafond douche humidité » + les 3 ancres (#causes/#methode/#erreur).
- **Effet attendu (qualitatif)** : fort sur le cluster — les sections `#vmc`
  et `#quand` déployées ciblent la 1re requête du site (137 impr pos. 11,2)
  et le déficit de conversion documenté ; la FAQ vise les formulations
  interrogatives du cluster. Aucune position promise.
- **Points de contrôle** : re-export GSC ~**1er octobre** (rapport #2,
  `rushiti-regression-seo`) — mesurer position/CTR du cluster et des ancres
  **avant** de juger ; ne rien réécrire d'ici là (consigne du rapport
  d'opportunités du 20/08).
- **Rafraîchissement** : re-vérifier la question locataire/propriétaire si le
  cadre change ; photos à intégrer dès la matière RGPD disponible.
- **Attend la validation d'Isuf** : le bloc FAQ (B1), la matière photos (B2),
  la décision pied d'article (B3). Rien ne part en production sans son accord.
