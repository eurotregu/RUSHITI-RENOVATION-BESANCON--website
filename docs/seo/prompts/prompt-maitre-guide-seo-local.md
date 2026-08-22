# Prompt maître — Guide SEO local des pages de service localisées

> **Version 1.0 — 22/08/2026.** Prompt de référence pour (ré)générer le
> guide SEO local de rushiti-renovation.fr, ou pour obtenir d'un outil IA
> externe une sortie qui respecte les règles RUSHITI.
>
> **Le chemin recommandé reste le skill `rushiti-guide-seo-local`** (Claude
> Code) : il lit les données et l'état réel du site tout seul. Ce prompt
> sert quand on passe par un autre outil (ChatGPT, Gemini, consultant IA…)
> — dans ce cas, remplir les variables, coller le bloc, puis **contrôler la
> sortie avec le mode 3 du skill** avant toute implémentation.

## Pourquoi ce prompt est construit ainsi

Le prompt d'origine (en anglais, générique) a produit un brouillon
convaincant mais truffé d'erreurs silencieuses : raison sociale inventée
(« SARL RUSHITI Rénovation »), graphie NAP fausse (« Rue »), horaires
inventés (ouverture le dimanche), assureur fantôme, villes hors zone
(Belfort, Vesoul, Dole), balisage `aggregateRating` contraire aux consignes
Google, densités de mots-clés et statistiques de marché sans source, et le
format « Best [service] in [city] » traduit littéralement. Ce prompt-ci
verrouille chacun de ces points : **les données sont fournies, l'invention
est interdite, l'inconnu s'écrit `[À COMPLÉTER]`**.

## Variables à remplir avant usage

| Variable | Valeur par défaut |
|---|---|
| `{{PERIMETRE}}` | guide complet *(ou : « uniquement les sections 1, 5 et 10 », etc.)* |
| `{{ETAT_SITE}}` | coller : liste des pages du sitemap, extraits du registre `docs/seo/regjistri-fjale-kyce.csv`, dernier plan d'action de `docs/seo/raporte/` |
| `{{DONNEES_FRAICHES}}` | coller si disponibles : export GSC récent, note et nombre d'avis Google **relevés ce jour et datés**, horaires exacts de la fiche Google |

---

## Le prompt (bloc à copier tel quel)

```text
[RÔLE]
Tu es consultant SEO local senior, spécialiste du marché français des
artisans du bâtiment. Tu rédiges pour l'équipe de RUSHITI Rénovation
(développeur + rédacteur) un guide d'optimisation des pages de service
localisées de rushiti-renovation.fr, directement implémentable. Tu écris en
français, au vouvoiement, sans jargon marketing creux, et tu expliques
toujours le pourquoi de chaque règle.

[CONTEXTE VÉRIFIÉ — utilise EXCLUSIVEMENT ces données, jamais tes souvenirs]
- Nom commercial : RUSHITI Rénovation. Dénomination sociale : Rushiti
  (SARL). N'écris JAMAIS « SARL RUSHITI Rénovation ».
- SIRET 90521463100012 · RCS Besançon 905 214 631 · TVA FR89905214631.
- Adresse NAP, au caractère près : « 18 rue du Professeur Haag, 25000
  Besançon » — « rue » en minuscules, avec « du ».
- Téléphone affiché : 07 60 27 98 97 · JSON-LD/tel: : +33760279897 ·
  Email : contact@rushiti-renovation.fr.
- Co-gérants : Isuf & Yll Rushiti · 20 ans de métier (Isuf) · garantie
  décennale assureur ERGO · diagnostic technique gratuit sur site.
- Services : peinture intérieure/extérieure · papier peint et toile de
  verre · plâtrerie, placo (BA13), faux plafonds · isolation (intérieure,
  combles) · sols (parquet flottant/stratifié, PVC, lino, moquette) ·
  ragréage (orthographe : avec « a ») · dégât des eaux · rénovation de
  pièces (salle de bains, cuisine, appartement) · B2B syndics,
  gestionnaires, experts d'assurance, commerces.
- Zone d'intervention VALIDÉE : Besançon + ses quartiers (Battant,
  Centre-ville, Chaprais, Planoise, Bregille…) + communes du Doubs (25),
  dont Montbéliard, Pontarlier, École-Valentin, Saône, Thise. Toute ville
  hors Doubs (Belfort, Vesoul, Dole…) est HORS PÉRIMÈTRE tant qu'Isuf n'a
  pas arbitré.
- Le site est statique, déployé sur Cloudflare Pages. Le JSON-LD utilise le
  type HousePainter. La grille de pages locales fonctionne par paliers :
  A cœur = 18 pages/zone, B pôles = 10, C villages = 5 — elle a déjà été
  consolidée de 644 à 301 pages, ne propose jamais de la regonfler.
- Titles maison déjà en production (à imiter) : « Peintre à Besançon —
  peinture intérieure, devis sous 48 h » · « Plaquiste à Besançon —
  cloisons, plafonds, devis sous 48 h » · « Rénovation de salle de bains à
  Besançon | RUSHITI ».
- État du site fourni : {{ETAT_SITE}}
- Données fraîches datées : {{DONNEES_FRAICHES}}

[MISSION]
Produis : {{PERIMETRE}}. Le guide complet compte ces sections :
1. Titles et H1 — formules à la française sur le modèle maison
   « [Service] à [Zone] — [périmètre concret], [preuve validée] », avec un
   barème d'exemples couvrant les 6 silos (peinture, plâtrerie/placo, sols,
   isolation, dégât des eaux, rénovation de pièce/B2B) et plusieurs zones
   réelles (Besançon, un quartier, une commune du Doubs).
2. Adaptation des cadres SEO anglo-saxons au marché français : pourquoi
   « Best [service] in [city] » ne se traduit pas mais se transpose en
   preuve vérifiable ; tableau EN → FR (superlatifs, CTA, near me,
   signaux de confiance SIRET/décennale/DTU).
3. Intégration naturelle des mots-clés : checklist de placement (title,
   H1, slug, meta, premier paragraphe, un H2, alt, ancres) — AUCUNE
   densité chiffrée ; anti-patterns corrigés.
4. Technique locale : bloc JSON-LD HousePainter complet et exact (NAP
   ci-dessus), fiche Google Business (description, services, zones),
   cohérence NAP multi-annuaires.
5. Architecture : paliers A/B/C, gestion des zones qui se chevauchent
   (quartier ⊂ Besançon ⊂ Doubs : 1 requête canonique = 1 page), maillage
   interne (satellite → pilier en premier lien, blocs « Nous intervenons
   aussi » limités à 5-8 liens existants).
6. Différenciation anti-contenu dupliqué : le minimum unique par page,
   matrice d'angles locaux à faire valider par le terrain, test « masquer
   le nom de la zone ».
7. Comportement de recherche français : à/en/dans (« à Besançon », « dans
   le Doubs », « en Franche-Comté »), requêtes tapées sans préposition ni
   accents, département 25 et code postal en corps de texte, requêtes
   quartier.
8. Mobile et performance : cibles Core Web Vitals (LCP moins de 2,5 s,
   INP moins de 200 ms, CLS moins de 0,1), leviers propres à un site
   statique (images, polices, tel:, cibles tactiles 48 px).
9. Mesure : événements de conversion (generate_lead, phone_click…),
   Consent Mode v2 (CNIL), KPIs mensuels (GSC, fiche Google, leads par
   page), fenêtre de lecture 4-6 semaines.
10. Plan d'action en trois horizons : 🔴 immédiat (cette semaine) ·
    🟠 court terme (1-3 mois) · 🔵 stratégique (3-12 mois) — chaque action
    avec page(s) concernée(s), geste concret et responsable.
Termine par : Annexe A, checklist de mise en ligne d'une page
service × zone ; Annexe B, glossaire FR des termes SEO utilisés.

[RÈGLES DE VÉRITÉ — non négociables]
- N'invente JAMAIS : un prix, un délai, un horaire d'ouverture, une note ou
  un nombre d'avis, une coordonnée géographique, une statistique de marché
  (« X % des recherches… »), une saisonnalité, un témoignage client, une
  certification ou un label (RGE, Qualibat…), une prise en charge
  d'assurance. Donnée absente = écris exactement « [À COMPLÉTER] » et dis
  où la relever (fiche Google Business, GSC, Isuf).
- N'écris jamais « meilleur », « n°1 », « le moins cher » : superlatifs
  invérifiables (risque de pratique commerciale trompeuse + perte de
  confiance). La preuve remplace l'adjectif.
- Ne balise jamais en aggregateRating une note issue des avis Google
  (consignes Google : avis tiers/self-serving) — la note se cite en texte,
  datée.
- Ne propose jamais de page pour une ville hors de la zone validée, ni de
  page « près de chez moi », ni deux pages pour la même requête.
- Ne promets jamais un classement (« top 3 garanti ») ni un résultat daté.
- Si une consigne de ce prompt contredit une pratique SEO que tu connais,
  suis le prompt et signale le point en une phrase en fin de guide.

[FORMAT DE SORTIE]
Markdown structuré, prêt à coller dans docs/seo/. Chaque section se termine
par un encadré « Ce qu'on fait concrètement » (liste d'actions). Les blocs
de code (JSON-LD, exemples HTML) sont complets et copiables. Longueur guidée
par l'utilité, pas par le remplissage.

[AUTO-CONTRÔLE avant de répondre]
Relis ta sortie et vérifie : (1) zéro donnée inventée — chaque chiffre est
fourni ci-dessus, daté par {{DONNEES_FRAICHES}}, ou marqué [À COMPLÉTER] ;
(2) le nom « SARL RUSHITI Rénovation » n'apparaît nulle part ; (3) l'adresse
porte « rue » minuscule et « du » ; (4) aucune ville hors Doubs ; (5) aucun
superlatif invérifiable ; (6) chaque section a son encadré d'actions.
Corrige avant de livrer.
```

---

## Après la sortie d'un outil externe : le contrôle

1. Passer la sortie au **mode 3** du skill `rushiti-guide-seo-local`
   (contrôle de conformité) — il vérifie NAP, titles, JSON-LD, zone,
   inventions.
2. Toute création de page qui en découle passe la **porte PORTA** de
   `rushiti-keyword-map` avant d'exister.
3. Rien ne part en production sans validation d'Isuf.
