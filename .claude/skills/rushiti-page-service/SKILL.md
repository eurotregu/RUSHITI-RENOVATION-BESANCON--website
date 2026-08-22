---
name: rushiti-page-service
description: >-
  Fabrique et met à niveau les pages de service « pilier » de
  rushiti-renovation.fr (service × Besançon : peinture, placo, isolation,
  sols, dégât des eaux, B2B) — la page de tête d'un silo, pas une page
  commune. Livre 4 blocs : brief, page HTML prête à déployer (title, meta,
  Hn, 1200-1500 mots, FAQ, JSON-LD Service/BreadcrumbList/FAQPage, maillage,
  CTA), checklist de conformité, plan de mesure. Trois modes : mise à niveau
  d'une page existante (cas majoritaire), création sous porte
  rushiti-keyword-map, contrôle avant déploiement. À déclencher dès qu'Isuf
  ou Yll dit « fais une page dédiée pour ce service », « landing page placo
  », « refais la page plaquiste », « notre page isolation est faible », ou
  en albanais « faqe e veçantë për shërbimin », « përmirëso faqen e izolimit
  » — même sans dire skill. Pages commune ou quartier → rushiti-page-locale
  ; articles → rushiti-architecte-seo. Aucun prix, délai ni classement
  inventé ; rien n'est déployé sans validation d'Isuf.
metadata:
  version: 1.0.0
---

# Page de service pilier — la page commerciale de tête d'un silo

Vous fabriquez la page qui doit **gagner la requête métier sur Besançon** :
« peintre à Besançon », « plaquiste à Besançon », « isolation intérieure
Besançon », « dégât des eaux Besançon ». C'est la page la plus rentable du
site : elle capte l'intention commerciale la plus large du silo, elle
alimente les 300 pages de la grille locale, et c'est elle qu'un moteur de
réponse cite quand on lui demande un artisan à Besançon.

Votre critère de réussite : **Isuf peut déployer la page sans la réécrire**,
et un concurrent bisontin ne pourrait pas la signer — parce qu'elle contient
des choses que seul quelqu'un qui a poncé un plâtre du centre-ville sait
écrire.

## Garde-fous (non négociables)

- **Aucune page neuve sans verdict `rushiti-keyword-map`** (registre
  `docs/seo/regjistri-fjale-kyce.csv`). Le site compte déjà ~300 URL et
  couvre ses silos : dans 9 cas sur 10, la bonne action est de **renforcer
  une page existante**, pas d'en créer une qui cannibalisera sa sœur.
- **Aucune invention.** Prix, délais, taux de TVA, aides (MaPrimeRénov',
  CEE), certifications, note et nombre d'avis, prises en charge assurance,
  volumes de recherche → `[À COMPLÉTER]` / `[À VALIDER PAR ISUF]`. Un
  volume de recherche ne s'écrit **jamais** de mémoire : il vient de la
  Search Console, de NeuronWriter ou du Keyword Planner, daté et sourcé.
- **Jamais de promesse de classement ni de projection de trafic chiffrée.**
  Effets attendus : fort / moyen / faible, appuyés sur une preuve.
- **Jamais de service non confirmé.** Le carrelage, le ravalement seul,
  l'enduit à la chaux, la moquette, la menuiserie : si ce n'est pas dans
  l'offre validée (voir `references/inventaire-piliers-services.md`),
  aucune page n'est écrite — la demande reste sciemment non servie jusqu'à
  arbitrage d'Isuf.
- **Écriture dans `docs/seo/` et dans les fichiers de page fournis.** Le
  déploiement en production (dépôt Cloudflare Pages) reste la décision
  d'Isuf, par le canal habituel.
- **RGPD** : aucun nom, adresse ni photo de client sans accord écrit
  confirmé. Les témoignages se citent tels qu'ils sont publiés sur la fiche
  Google, avec la date du relevé.
- **Pas de balisage `Review` ni `aggregateRating` auto-déclaré** sur les
  pages de service : Google l'interdit pour les avis que l'entreprise
  collecte sur elle-même. La preuve sociale se met **dans le texte visible**,
  pas dans le JSON-LD.

## Quand l'utiliser — et quand router ailleurs

| La demande | L'agent |
|---|---|
| Page de service × **Besançon** (tête de silo) | **ce skill** |
| Page service × **commune ou quartier** (grille A/B/C) | `rushiti-page-locale` |
| Article de blog, satellite, plan éditorial | `rushiti-architecte-seo` |
| Attribution de requête, feu vert de création | `rushiti-keyword-map` |
| Title / meta seuls, sur une page existante | `seo-title-meta` |
| Doctrine (formules, prépositions, paliers) | `rushiti-guide-seo-local` |
| JSON-LD final à coller | `schema-builder` |
| Deux pages qui se marchent dessus | `rushiti-cannibal-check` |
| Mesure de l'effet après déploiement | `rushiti-regression-seo` |

## Les trois modes

### Mode 1 — Mise à niveau d'une page existante *(cas majoritaire)*

Une page pilier existe déjà pour presque chaque silo. La demande « il nous
faut une page peinture » se traduit donc, neuf fois sur dix, par : **la page
`/peinture-interieure-besancon` existe, elle est faible sur trois points
précis, on les corrige.**

1. Relever l'état réel de la page (title, meta, H1, H2/H3, mots, FAQ,
   JSON-LD, maillage, CTA) — sur le **code HTML de la page live**, jamais de
   mémoire ni depuis une SERP.
2. Croiser avec le registre : quelle requête cette page porte-t-elle, quelles
   impressions et positions GSC, quelle page lui fait de l'ombre.
3. Produire le **diff** : ce qui reste, ce qui change, ce qui s'ajoute — avec
   le motif de chaque changement.
4. Livrer le HTML complet de la page corrigée + les 4 blocs de livrables.

### Mode 2 — Création d'une page pilier neuve *(rare)*

Uniquement après verdict `rushiti-keyword-map` : requête réellement non
servie, aucune page existante ne la porte, prestation confirmée dans l'offre.
Livrer alors la page complète, plus le plan de maillage entrant (au moins
3 liens depuis des pages existantes — sans quoi la page naît orpheline) et
l'entrée de sitemap.

### Mode 3 — Contrôle avant déploiement

On vous donne un fichier HTML ou une URL de préproduction : vous rendez la
checklist de `references/controles-mesure-deploiement.md`, ligne par ligne,
avec verdict ✅ / ⚠️ / ❌ et la correction exacte à appliquer. Aucun verdict
sans avoir lu le code.

## Contexte entreprise (source de vérité — ne se redemande jamais)

| Élément | Valeur |
|---|---|
| Nom commercial | RUSHITI Rénovation *(jamais « SARL RUSHITI Rénovation »)* |
| Identifiants | SIRET 90521463100012 · RCS Besançon 905 214 631 · TVA FR89905214631 |
| NAP au caractère près | 18 rue du Professeur Haag, 25000 Besançon · 07 60 27 98 97 · contact@rushiti-renovation.fr |
| Téléphone technique | `tel:+33760279897` · WhatsApp `wa.me/33760279897` |
| Gérants | Isuf & Yll Rushiti — 20 ans de métier sur le bâti bisontin |
| Preuves stables | Diagnostic technique gratuit sur place · décennale + RC pro (ERGO) · DTU 59.1, 25.41, 53.2 · convention IRSI pour les sinistres |
| Zone validée | Besançon et ses quartiers + communes du Doubs (25), dont Pontarlier et Montbéliard. **Hors Doubs = hors périmètre** tant qu'Isuf n'a pas arbitré (pas de Vesoul, Belfort, Dole, Dijon) |
| Technique | Site statique, Cloudflare Pages · JSON-LD `HousePainter` · grille locale consolidée par paliers A/B/C — ne jamais proposer de la regonfler |

Détail : `references/inventaire-piliers-services.md` (URL réelles par silo,
URL interdites, offre confirmée et refusée).

## Procédure

1. **Identifier le silo et l'intention.** Six silos + B2B. Une page pilier
   sert une intention commerciale ; si la demande est informationnelle
   (« prix », « comment faire »), c'est un article → `rushiti-architecte-seo`.
2. **Ouvrir la porte.** Mode 2 → verdict `rushiti-keyword-map` obligatoire.
   Mode 1 → relever dans le registre la requête portée et la dernière mesure.
3. **Relever l'état réel** (page live, code HTML). Noter la date du relevé :
   toute affirmation sur le site sans date est irrecevable.
4. **Choisir l'angle de différenciation.** Une page pilier qui ne dit que
   « nous sommes sérieux et le devis est gratuit » est morte. L'angle vient
   du terrain : bâti ancien de la Boucle, plâtre traditionnel, humidité des
   rez-de-chaussée, copropriétés des Chaprais, logements locatifs entre deux
   baux, sinistres IRSI. Voir `references/anatomie-page-service.md`.
5. **Écrire la page** selon l'anatomie en 12 blocs. 1200-1500 mots utiles.
   Français, vouvoiement, phrases courtes, zéro superlatif creux.
6. **Baliser.** `Service` + `BreadcrumbList` + `FAQPage` (si FAQ visible) en
   plus du `HousePainter`/`LocalBusiness` du socle. Pas de `Review`.
7. **Mailler.** 3 liens entrants minimum depuis des pages existantes,
   3 à 6 liens sortants (silos frères, article de prix, pages locales du
   palier A), ancres exactes-mais-naturelles.
8. **Livrer les 4 blocs** et s'arrêter là : rien ne part en production sans
   la validation d'Isuf.

## Livrables (toujours les quatre, dans cet ordre)

**1. Brief d'intention** — une demi-page : requête cible et requêtes
secondaires (sourcées ou `[À SOURCER]`), intention, page concurrente interne
à ne pas cannibaliser, angle de différenciation, preuves mobilisées,
ce qui manque et bloque (`[À COMPLÉTER]`).

**2. Page HTML complète** — prête à coller : `<title>`, meta description,
canonical, Open Graph et Twitter, JSON-LD, structure H1→H3, contenu rédigé
en entier (jamais de « [insérer paragraphe ici] »), FAQ, CTA, maillage,
alt text de chaque image.

**3. Checklist de conformité** — celle de
`references/controles-mesure-deploiement.md`, cochée, avec les points en
`[À COMPLÉTER]` listés séparément pour Isuf.

**4. Plan de mesure** — quelle requête surveiller, sur quelle page, avec
quelle donnée de départ (impressions et position GSC du jour, datées), et
quand relire : 4 à 6 semaines, via `rushiti-regression-seo`. Effet attendu
qualifié fort / moyen / faible **avec son motif**, jamais chiffré.

## Formules de title et H1 (doctrine française)

- **Title, 60 caractères max**, structure : `<métier ou service> à Besançon
  — <preuve ou bénéfice concret>`. Exemple live :
  « Peintre à Besançon — peinture intérieure, devis sous 48 h ».
- **Jamais** « Meilleur peintre à Besançon », « N°1 », « Pas cher »,
  « TOP 10 » : calques anglo-saxons, sans crédibilité en France et
  ininterprétables par Google comme preuve.
- **Meta description, 155 caractères max** : le service, la zone entre
  parenthèses `(25)`, une preuve vérifiable, une action. Les preuves
  chiffrées (20 ans, note et nombre d'avis) se vérifient le jour de
  l'écriture ou ne s'écrivent pas.
- **H1 ≠ title.** Le H1 porte le service et la zone en langue naturelle :
  « Peinture intérieure à Besançon et dans le Doubs ». Un seul H1.
- **Préposition** : « à Besançon », « dans le Doubs », « en
  Bourgogne-Franche-Comté ». Le code postal n'entre ni dans le H1 ni dans
  l'URL — il vit dans le NAP et le JSON-LD.

## Anti-cannibalisation : pilier contre grille locale

La page pilier et les pages `<service>-<commune>` visent la même prestation.
Ce qui les sépare :

| | Page pilier (× Besançon) | Page locale (× commune/quartier) |
|---|---|---|
| Requête | métier large : « plaquiste à Besançon » | « plaquiste École-Valentin » |
| Contenu | expertise, méthode, matériaux, cas de figure | ancrage : bâti local, accès, chantiers du secteur |
| Longueur | 1200-1500 mots | selon palier A/B/C |
| Maillage | reçoit des locales, envoie vers le palier A | pointe vers le pilier |
| Ce qu'elle ne fait pas | lister les 76 communes en pavé | refaire l'exposé technique du pilier |

Si une page locale commence à mieux se positionner que le pilier sur la
requête métier, ce n'est pas une victoire : c'est un signal de confusion →
`rushiti-cannibal-check`.

## Les onze erreurs qui tuent une page de service

Elles viennent toutes de brouillons réels (prompts génériques, sorties d'IA
non bridées, consultants) :

1. **Créer `/peinture` quand `/peinture-interieure-besancon` existe** — la
   page neuve n'apporte rien et divise le signal. Voir les URL interdites.
2. **Inventer des volumes de recherche** (« ~720/mois ») : aucun outil n'a
   été interrogé, le chiffre est décoratif et fausse la priorisation.
3. **Élargir la zone à Vesoul, Dijon, Belfort** : hors périmètre validé,
   et un « rayon de 50 km » écrit sur une page ne crée aucune pertinence
   locale — il dilue celle qui existe.
4. **Promettre un délai** (« intervention sous 48 h ») sans validation :
   promesse contractuelle, pas argument marketing.
5. **Baliser des avis en `aggregateRating`** auto-déclaré : contraire aux
   consignes Google, risque de pénalité manuelle.
6. **Citer des marques de matériaux non utilisées** pour faire riche.
7. **Recopier le même texte d'un silo à l'autre** en changeant le mot-clé.
8. **Empiler des mots-clés** dans le H1, les alt et le premier paragraphe
   au point que la phrase ne se lit plus à voix haute.
9. **Oublier le maillage entrant** : une page pilier sans lien depuis
   l'accueil et les pages sœurs reste invisible, quel que soit son contenu.
10. **Mettre une FAQ visible sans `FAQPage`** — ou l'inverse : du `FAQPage`
    sur des questions absentes de la page.
11. **Livrer une page à trous** (`[insérer ici le paragraphe sur…]`) :
    ce n'est pas un livrable, c'est un plan.

## Ce que le skill ne fait pas

Il ne déploie rien, ne pousse rien en production, ne modifie pas le sitemap
live, ne soumet rien à la Search Console, et n'affirme aucun chiffre qu'il
n'a pas lu lui-même dans une source datée.
