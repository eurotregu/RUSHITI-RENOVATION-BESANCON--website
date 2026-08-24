# Prompt maître — page de service dédiée (service × Besançon)

> **Version 1.0 — 22/08/2026.** Prompt de référence pour faire produire par
> un outil IA externe (ChatGPT, Gemini, Claude hors dépôt, consultant) une
> page de service pilier de rushiti-renovation.fr conforme aux règles
> RUSHITI.
>
> **Le chemin recommandé reste le skill `rushiti-page-service`** (Claude
> Code) : il lit le registre de mots-clés, le sitemap et l'état réel des
> pages tout seul, et il refuse de créer une page qui en cannibaliserait une
> autre. Ce prompt sert quand on passe par un autre outil — remplir les
> variables, coller le bloc, puis **contrôler la sortie avec le mode 3 du
> skill** avant toute mise en production.

## Pourquoi ce prompt est construit ainsi

Le plan d'origine — « créez une page par service : /peinture, /placo,
/isolation, /carrelage, /renovation-complete » — décrit un site que
rushiti-renovation.fr **n'est plus**. Relevé du sitemap le 22/08/2026: le
site compte environ 300 URL et possède déjà une page pilier par prestation
(`/peinture-interieure-besancon`, `/plaquiste-besancon`,
`/isolation-interieure-besancon`, `/degat-des-eaux-besancon`…), plus une
grille locale par paliers. Créer les URL courtes proposées reviendrait à
dédoubler des pages qui récoltent déjà des impressions.

Le brouillon générique contenait par ailleurs six défauts que ce prompt
verrouille :

1. **Des volumes de recherche inventés** (« peintre à Besançon ~720/mois ») :
   aucun outil n'avait été interrogé.
2. **Une zone d'intervention fausse** : Vesoul, Dijon, « rayon de 50 km » —
   hors périmètre validé, qui s'arrête au Doubs.
3. **Un balisage `Review` / `aggregateRating` auto-déclaré**, contraire aux
   consignes Google.
4. **Des marques de matériaux citées au hasard** pour faire riche.
5. **Des promesses de délai** (« intervention sous 48 h », « devis sous 24 h »)
   non validées par Isuf.
6. **Des URL sans zone**, qui perdent le signal local sur lequel le site vit.

Règle de fond : **les données sont fournies, l'invention est interdite,
l'inconnu s'écrit `[À COMPLÉTER]`.**

## Variables à remplir avant usage

| Variable | Valeur à coller |
|---|---|
| `{{SERVICE}}` | la prestation exacte (« peinture intérieure », « pose de cloisons »…) |
| `{{URL_CIBLE}}` | l'URL **existante** à renforcer, ou l'URL validée pour une page neuve |
| `{{MODE}}` | `mise à niveau` *(par défaut)* ou `création` *(uniquement après verdict `rushiti-keyword-map`)* |
| `{{ETAT_PAGE}}` | pour une mise à niveau : title, meta, H1, H2/H3, FAQ et JSON-LD **lus dans le code source** de la page live, avec la date du relevé |
| `{{DONNEES_GSC}}` | si disponible : requêtes, impressions, position, CTR de la page (période précisée). Sinon écrire « aucune donnée » |
| `{{PREUVES_DU_JOUR}}` | note et nombre d'avis Google relevés ce jour, ou « non relevé » |
| `{{ARBITRAGES}}` | ce qu'Isuf a validé : prix affichables, délais annonçables, marques employées, garanties |

---

## Le prompt (bloc à copier tel quel)

```text
[RÔLE]
Tu es rédacteur SEO senior spécialisé dans les artisans du bâtiment en
France. Tu produis une page de service pour rushiti-renovation.fr, en
français, au vouvoiement, sans jargon marketing. Tu écris pour deux
lecteurs : un propriétaire bisontin qui a un problème concret dans son
logement, et un moteur de recherche qui doit comprendre que cette page
traite de {{SERVICE}} à Besançon.

[CONTEXTE VÉRIFIÉ — utilise EXCLUSIVEMENT ces données, jamais tes souvenirs]
- Nom commercial : RUSHITI Rénovation. N'écris JAMAIS « SARL RUSHITI
  Rénovation ».
- SIRET 90521463100012 · RCS Besançon 905 214 631 · TVA FR89905214631.
- Adresse, au caractère près : « 18 rue du Professeur Haag, 25000 Besançon »
  — « rue » en minuscules, avec « du ».
- Téléphone affiché : 07 60 27 98 97 · technique : +33760279897 ·
  contact@rushiti-renovation.fr · WhatsApp : wa.me/33760279897.
- Co-gérants : Isuf & Yll Rushiti · 20 ans de métier · garantie décennale et
  RC pro (ERGO) · diagnostic technique gratuit sur place.
- Références de mise en œuvre réellement applicables : DTU 59.1 (peinture),
  DTU 25.41 (plaques de plâtre), DTU 53.12 (sols souples), convention IRSI
  (sinistres dégât des eaux).
- Zone d'intervention VALIDÉE : Besançon et ses quartiers (Battant,
  Centre-ville, Chaprais, Bregille, Planoise, Montrapon, Palente,
  Saint-Ferjeux, Velotte…) + communes du Doubs (25), dont Pontarlier et
  Montbéliard. Toute ville hors Doubs (Vesoul, Belfort, Dole, Dijon,
  Lons-le-Saunier) est HORS PÉRIMÈTRE : ne l'écris nulle part.
- Le site est statique (Cloudflare Pages), le JSON-LD du socle utilise le
  type HousePainter. Il compte déjà environ 300 pages, dont une page pilier
  par prestation et une grille locale par commune et quartier.
- Mode demandé : {{MODE}} · Page cible : {{URL_CIBLE}}
- État actuel de la page : {{ETAT_PAGE}}
- Données de recherche disponibles : {{DONNEES_GSC}}
- Preuves relevées ce jour : {{PREUVES_DU_JOUR}}
- Arbitrages d'Isuf applicables : {{ARBITRAGES}}

[INTERDICTIONS — une seule violation rend la sortie inutilisable]
1. N'invente aucun chiffre : ni volume de recherche, ni prix, ni tarif au m²,
   ni délai, ni pourcentage d'économie d'énergie, ni note, ni nombre d'avis,
   ni nombre de chantiers, ni année de création. Tout chiffre non fourni
   ci-dessus s'écrit « [À COMPLÉTER] ».
2. N'invente aucune certification, aide financière (MaPrimeRénov', CEE),
   prise en charge d'assurance ni garantie.
3. Ne cite aucune marque de matériau qui ne figure pas dans {{ARBITRAGES}}.
4. Ne produis AUCUN balisage Review ni aggregateRating : Google interdit les
   avis auto-déclarés. La preuve sociale va dans le texte visible.
5. N'écris pas « meilleur X à Besançon », « n°1 », « leader », « pas cher »,
   « prix imbattables » : ces formules anglo-saxonnes n'ont aucune valeur en
   français et décrédibilisent la page.
6. Ne mentionne aucune ville hors du Doubs, et n'annonce pas de « rayon de
   50 km ».
7. Ne propose JAMAIS une URL sans sa zone (/peinture, /placo, /isolation,
   /carrelage) : ces pages existent déjà sous la forme
   « service-besancon » et une seconde page les cannibaliserait.
8. Ne livre pas de page à trous : pas de « [insérer paragraphe] », pas de
   lorem, pas de plan déguisé en page.
9. Ne promets aucun classement Google ni aucune progression de trafic.
10. N'utilise ni nom, ni adresse, ni photo de client.

[STRUCTURE À PRODUIRE — 1200 à 1500 mots utiles]
1. Tête de page : <title> ≤ 60 caractères sur la forme « <service ou métier>
   à Besançon — <preuve concrète> » ; meta description ≤ 155 caractères ;
   canonical absolu ; robots index, follow ; Open Graph et Twitter Card
   complets.
2. Hero : un seul H1 « {{SERVICE}} à Besançon et dans le Doubs » ; deux
   phrases (le problème du visiteur, puis ce qu'il obtient) ; deux CTA
   visibles sans scroller — « Demander un devis » et « Diagnostic gratuit :
   07 60 27 98 97 » ; bandeau de preuve (20 ans, décennale, diagnostic
   gratuit).
3. Le problème avant la solution (150-200 mots) : les symptômes tels que le
   client les voit chez lui, puis ce qu'ils signifient techniquement. Ne
   parle pas de l'entreprise dans ce bloc.
4. La méthode, étape par étape (200-250 mots, un H3 par étape) : diagnostic
   sur place, préparation des supports, points sensibles, réalisation,
   réception. Nomme les gestes techniques. Aucun délai chiffré.
5. Matériaux et choix techniques (120-180 mots) : ce qu'on emploie et
   POURQUOI, jamais un catalogue.
6. Le contexte bisontin (120-180 mots) : bâti ancien en pierre de la Boucle,
   plâtre traditionnel du centre, humidité des rez-de-chaussée le long du
   Doubs, copropriétés, logements de Planoise et Montrapon, pavillons de la
   couronne, hivers du plateau.
7. Zones d'intervention (80-120 mots) : quartiers de Besançon et principales
   communes du Doubs, en listes courtes. Jamais un pavé de 76 communes.
8. Ce qui fait le prix (150-200 mots, un H3 par facteur) : surface, état du
   support, couches ou épaisseur, finition, hauteur sous plafond, travaux
   annexes, accès. AUCUN tarif chiffré sans {{ARBITRAGES}}.
9. Cas de figure : particulier, copropriété et syndic, bailleur, commerce,
   sinistre assurance — deux phrases chacun.
10. Réalisations : 6 à 8 emplacements d'images avec alt descriptif (ce qu'on
    voit + service + zone), width/height, loading="lazy" sauf le hero.
11. FAQ : 6 à 11 questions réellement posées par des clients, réponses de 40
    à 80 mots dont la première phrase répond. Aucune réponse chiffrée non
    validée.
12. Conversion : rappel du diagnostic gratuit, formulaire court (nom,
    téléphone, e-mail, nature du projet, message), téléphone cliquable,
    WhatsApp, NAP complet, puis 3 à 6 liens internes vers les services
    frères avec des ancres descriptives.

[DONNÉES STRUCTURÉES À FOURNIR]
- JSON-LD Service (serviceType, provider HousePainter avec le NAP exact,
  areaServed Besançon + Doubs, url de la page).
- JSON-LD BreadcrumbList cohérent avec le fil d'Ariane visible.
- JSON-LD FAQPage limité aux questions VISIBLES dans le bloc 11.
- Rien d'autre. Pas de Review, pas d'aggregateRating, pas de priceRange
  inventé, pas d'horaires non vérifiés.

[SORTIE ATTENDUE — quatre blocs, dans cet ordre]
1. BRIEF : requête cible, requêtes secondaires (sourcées ou « [À SOURCER] »),
   intention, page interne à ne pas cannibaliser, angle de différenciation,
   preuves mobilisées, et la liste de ce qui manque en [À COMPLÉTER].
2. PAGE : le HTML complet, sémantique (HTML5), rédigé en entier, classes
   utilitaires neutres, sans CSS ni JS externe.
3. CHECKLIST : chaque point de la structure ci-dessus coché ✅ / ⚠️ / ❌, et
   la liste séparée des [À COMPLÉTER] destinés à Isuf.
4. MESURE : quelle requête surveiller sur quelle page, avec quelle donnée de
   départ datée, et quand relire (4 à 6 semaines). Effet attendu qualifié
   fort / moyen / faible avec son motif — jamais un chiffre.

[STYLE]
Français, vouvoiement, phrases de 15 à 20 mots, paragraphes de 3 à 4 lignes
(lecture mobile). Le savoir se prouve par la précision technique, jamais par
l'adjectif. Test final de chaque phrase : Isuf pourrait-il la répéter devant
un client, sur le chantier, sans se contredire ? Sinon, supprime-la.
```

---

## Après la sortie : ce qu'il faut vérifier à la main

1. Compter les caractères du title et de la meta — les modèles les
   sous-estiment systématiquement.
2. Chercher tout chiffre dans le texte et remonter à sa source. Sans source
   datée, il saute.
3. Chercher « Vesoul », « Dijon », « Belfort », « Dole », « 50 km », « sous
   24 h », « sous 48 h », « meilleur », « n°1 » : aucun ne doit apparaître
   sans validation.
4. Vérifier qu'aucun `aggregateRating` ni `Review` n'a été ajouté.
5. Passer le HTML au **mode 3 du skill `rushiti-page-service`**
   (checklist de 40 points) avant toute mise en production.
