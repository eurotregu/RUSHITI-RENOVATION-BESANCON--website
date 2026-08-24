# Anatomie d'une page de service pilier — les 12 blocs

Budget global : **1200 à 1500 mots utiles** (hors navigation, footer, FAQ
comptée à part). En dessous de 900, la page ne tient pas face aux pages
concurrentes bisontines ; au-dessus de 1800, elle se dilue et le visiteur
mobile décroche avant le formulaire.

Ordre imposé. Chaque bloc a un budget et un rôle unique : deux blocs qui
disent la même chose, c'est un bloc en trop.

---

## Bloc 1 — Tête de page *(technique, invisible)*

```html
<title>Plaquiste à Besançon — cloisons, plafonds, [preuve]</title>
<meta name="description" content="Pose de placo à Besançon (25) : cloisons,
doublages, faux plafonds, reprise de plâtre ancien. [preuve datée]. Diagnostic
gratuit sur place.">
<link rel="canonical" href="https://rushiti-renovation.fr/plaquiste-besancon">
<meta name="robots" content="index, follow">
```

- Title ≤ 60 caractères, meta ≤ 155. Compter, ne pas estimer.
- Canonical **absolu**, sans slash final, en cohérence avec le sitemap.
- Open Graph : `og:title`, `og:description`, `og:url`, `og:image` (photo de
  chantier réelle, pas une banque d'images), `og:image:alt`, `og:locale`
  `fr_FR`, `og:site_name` « RUSHITI Rénovation ». Twitter :
  `summary_large_image`.
- **Un seul jeu de balises.** Un `<title>` en double dans la page (l'un
  statique, l'autre injecté) fait lire à Google le mauvais. Vérifier le code
  source, pas le rendu.

## Bloc 2 — Hero *(60-90 mots)*

- **H1** : service + zone en langue naturelle. Un seul H1 dans la page.
- Deux phrases sous le H1 : le problème du visiteur, puis ce qu'il obtient.
  Pas de slogan. « Vos cloisons sonnent creux, votre plafond s'est fissuré
  après la fuite du dessus » vaut mieux que « L'excellence au service de
  votre habitat ».
- **Deux CTA visibles sans scroller** : « Demander un devis » (ancre vers le
  formulaire) et « Diagnostic gratuit : 07 60 27 98 97 » (`tel:+33760279897`).
  Cible tactile 48×48 px minimum.
- Bandeau de preuve : 20 ans de métier · décennale et RC pro · diagnostic
  gratuit sur place. Les compteurs (note, nombre d'avis) : relevés du jour ou
  absents.

## Bloc 3 — Le problème avant la solution *(150-200 mots)*

Le bloc qui fait la différence avec un concurrent. On décrit ce que le
visiteur voit chez lui, dans ses mots : traces au plafond, plâtre qui
farine, mur froid côté nord, joint qui rouvre chaque hiver, sol qui sonne.
Puis ce que ces symptômes signifient techniquement. C'est le bloc qu'un
moteur de réponse cite, parce que c'est le seul qui répond à la question
réelle.

Interdit ici : parler de l'entreprise. On parle du mur.

## Bloc 4 — Notre méthode, étape par étape *(200-250 mots, H3 par étape)*

Quatre à cinq étapes, chacune avec un **geste technique nommé** :

1. **Diagnostic gratuit sur place** — ce qu'on regarde, ce qu'on mesure
   (humidimètre pour un sinistre, sondage du support, planéité).
2. **Préparation des supports** — la vraie valeur du métier : rebouchage,
   ratissage, ponçage, traitement des fissures, primaire d'accroche adapté.
3. **Traitement des points sensibles** — angles, jonctions plafond-mur,
   reprises sur plâtre ancien, pièces humides.
4. **Réalisation** — mise en œuvre, nombre de couches ou d'épaisseurs,
   règles de l'art (DTU 59.1 peinture, 25.41 plaques de plâtre, 53.12 sols).
5. **Réception** — contrôle avec le client, reprises, remise en état.

Les DTU se citent parce qu'ils encadrent réellement le travail — jamais
comme décor. Aucun délai chiffré sans validation.

## Bloc 5 — Matériaux et choix techniques *(120-180 mots)*

Ce qu'on pose et **pourquoi**, pas un catalogue de marques. Exemples de
choix qui prouvent l'expertise : plaque hydrofuge en pièce humide, plaque
phonique sur mur mitoyen d'immeuble ancien, finition velours qui pardonne
un support irrégulier, sous-couche d'accroche sur ancienne peinture
glycéro. Toute marque citée doit être réellement employée — sinon,
`[À VALIDER PAR ISUF]`.

## Bloc 6 — Le contexte bisontin *(120-180 mots)*

L'ancrage local qui ne s'invente pas : bâti ancien en pierre de la Boucle,
plâtre traditionnel des immeubles du centre, rez-de-chaussée humides le
long du Doubs, copropriétés des Chaprais et de Battant, barres et
appartements de Planoise et Montrapon, pavillons de la couronne
(École-Valentin, Pirey, Serre-les-Sapins), climat continental du plateau
et du Haut-Doubs pour l'isolation.

Ce bloc justifie la légitimité locale mieux que dix répétitions de
« à Besançon ».

## Bloc 7 — Zones d'intervention *(80-120 mots, listes courtes)*

Groupées par secteur, avec liens vers les pages locales du **palier A**
uniquement. Jamais un pavé des 76 communes : ce n'est ni lisible ni utile,
et cela dilue le maillage. Hors Doubs = absent.

## Bloc 8 — Ce qui fait le prix *(150-200 mots, H3 par facteur)*

**Aucun tarif chiffré sans validation d'Isuf.** On explique les variables :
surface, état du support, nombre de couches ou épaisseur, finition, hauteur
sous plafond, travaux annexes, accès et étage. Puis un lien vers l'article
prix du silo (`/blog/prix-peinture-interieure-besancon-2026`, et son
équivalent quand il existe) et vers `/prix-travaux-renovation-besancon`.

C'est le bloc qui convertit : le visiteur qui comprend pourquoi il ne peut
pas avoir un prix au clic demande un devis.

## Bloc 9 — Cas de figure et publics *(100-150 mots)*

Particulier, copropriété et syndic, bailleur et logement locatif entre deux
baux, commerce et bureau, sinistre assurance. Chaque public en deux
phrases, avec le lien vers sa page B2B dédiée quand elle existe
(`/renovation-syndic-gestionnaire-besancon`,
`/remise-en-etat-logement-locatif-besancon`,
`/amenagement-commerce-bureau-besancon`,
`/expert-assurance-sinistre-besancon`).

## Bloc 10 — Réalisations *(6 à 8 visuels)*

Photos réelles de chantiers, en WebP, `loading="lazy"`, `width` et `height`
déclarés (sinon la page saute au chargement et le CLS se dégrade).

Alt text : **description de ce qu'on voit** + service + zone. Jamais une
liste de mots-clés.

- ✅ `alt="Plafond refait après dégât des eaux dans un appartement du centre de Besançon"`
- ❌ `alt="plaquiste besançon placo cloison doubs pas cher devis gratuit"`

Avant/après : deux images distinctes, chacune avec son alt, jamais un
montage illisible sur mobile.

## Bloc 11 — FAQ *(6 à 11 questions)*

Les questions viennent de trois sources réelles, jamais de l'imagination :
ce qu'on demande à Isuf au téléphone, les requêtes GSC de la page, les
« autres questions posées » de la SERP. Réponse : 40 à 80 mots, la réponse
utile dans la **première phrase** — c'est ce qui rend le bloc extractible
par les moteurs de réponse.

Mélanger les registres : technique (« Combien de couches faut-il ? »),
pratique (« Faut-il déménager les meubles ? »), local (« Peut-on peindre sur
un plâtre ancien fissuré du centre ? »), administratif (« Travaillez-vous
pour les copropriétés et les bailleurs ? »).

Aucune question sur le prix ne se répond par un chiffre non validé : on
renvoie à l'article prix et au diagnostic gratuit.

## Bloc 12 — Conversion et maillage *(80-120 mots)*

- Rappel du diagnostic gratuit, formulaire court (nom, téléphone, e-mail,
  nature du projet, message ; le téléphone et l'e-mail suffisent à
  rappeler — chaque champ en plus coûte des demandes).
- Téléphone cliquable, WhatsApp, e-mail, NAP complet.
- **Maillage sortant** : 3 à 6 liens vers les silos frères et les pages
  locales du palier A, avec ancres descriptives (« pose de cloisons à
  Besançon »), jamais « cliquez ici ».
- **Maillage entrant à prévoir** : au moins 3 pages existantes doivent
  pointer vers cette page (accueil, page sœur du silo, article de blog du
  silo). Une page pilier orpheline ne se classe pas.

---

# Données structurées

Sur le socle `WebSite` + `LocalBusiness`/`HousePainter` déjà présent, la page
de service ajoute :

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Pose de plaques de plâtre et cloisons",
  "provider": {
    "@type": "HousePainter",
    "name": "RUSHITI Rénovation",
    "telephone": "+33760279897",
    "email": "contact@rushiti-renovation.fr",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "18 rue du Professeur Haag",
      "addressLocality": "Besançon",
      "postalCode": "25000",
      "addressCountry": "FR"
    }
  },
  "areaServed": [
    { "@type": "City", "name": "Besançon" },
    { "@type": "AdministrativeArea", "name": "Doubs" }
  ],
  "url": "https://rushiti-renovation.fr/plaquiste-besancon"
}
</script>
```

Plus `BreadcrumbList` (Accueil → Services → la page) et `FAQPage`
strictement limité aux questions **visibles** dans le bloc 11.

Interdits : `aggregateRating` et `Review` auto-déclarés, `priceRange` inventé,
`openingHours` non vérifiés sur la fiche Google, un `@type` qui ne
correspond pas à la prestation.

Le JSON-LD final se génère avec `schema-builder` puis se valide avant
déploiement (test des résultats enrichis + validator schema.org).

---

# Angles de différenciation par silo

| Silo | Angle qui fait la page | Piège à éviter |
|---|---|---|
| Peinture intérieure | La préparation du support : c'est elle qui tient dans le temps sur plâtre ancien | Parler couleurs et tendances |
| Peinture extérieure / façade | Diagnostic du support, saison de mise en œuvre, façades isolées par l'extérieur | Promettre une intervention par tous les temps |
| Plaquiste / plâtrerie | Reprise de plâtre traditionnel vs pose neuve, phonique en immeuble ancien | Le catalogue de plaques |
| Cloisons / faux plafonds | Créer une pièce sans casser, passage des réseaux, isolation phonique | Confondre avec le doublage |
| Doublage / isolation intérieure | Épaisseur contre surface perdue, mur froid, point de rosée | Citer des aides et des économies non validées |
| Sols | Diagnostic du support et ragréage avant pose, choix pièce par pièce | Vendre le produit sans parler du support |
| Dégât des eaux | Assèchement avant réfection, humidimètre, IRSI, devis lisible par l'expert | Promettre une prise en charge assurance |
| Rénovation de pièce | Coordination des lots par un seul interlocuteur | Se faire passer pour un maître d'œuvre tous corps d'état |
| B2B syndic / bailleur / commerce | Interlocuteur unique, chantier en site occupé, remise en état entre deux baux | Le discours grand public recyclé |

---

# Voix RUSHITI

- Vouvoiement, français simple, phrases de 15 à 20 mots, paragraphes de 3 à
  4 lignes maximum (lecture mobile).
- On nomme les gestes techniques, on explique ce qu'ils changent. Le savoir
  se prouve par la précision, jamais par l'adjectif.
- Bannis : « leader », « n°1 », « incontournable », « solutions
  sur-mesure innovantes », « à des prix imbattables », « nous mettons un
  point d'honneur ».
- Chaque affirmation passe le test : **Isuf pourrait-il la répéter devant un
  client, sur le chantier, sans se contredire ?** Sinon, elle saute.
