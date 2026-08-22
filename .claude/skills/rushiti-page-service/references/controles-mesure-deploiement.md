# Contrôles, déploiement et mesure

## A. Checklist avant déploiement

Verdict par ligne : ✅ conforme · ⚠️ à corriger · ❌ bloquant · `[À COMPLÉTER]`
si l'information manque. **Aucun ✅ sans avoir lu le code de la page.**

### Balises et indexation
1. `<title>` unique dans le document, ≤ 60 caractères, service + Besançon,
   sans « meilleur / n°1 / pas cher ».
2. Meta description ≤ 155 caractères, une preuve vérifiable, une action.
3. Aucun `<title>` ni `<meta description>` en double (statique + injecté).
4. `<link rel="canonical">` absolu, sans slash final, cohérent avec le
   sitemap et l'`og:url`.
5. `<meta name="robots" content="index, follow">` — et pas de `noindex`
   hérité d'une préproduction.
6. `<html lang="fr">`.
7. Open Graph complet (`og:title`, `og:description`, `og:url`, `og:image`,
   `og:image:alt`, `og:locale`, `og:site_name`) + `twitter:card`.
8. `og:image` : photo de chantier réelle, existante (HTTP 200), ≥ 1200 px de
   large de préférence.

### Structure et contenu
9. Un seul `<h1>`, distinct du title, avec le service et la zone.
10. Hiérarchie H2/H3 sans saut de niveau, chaque H2 introduit un vrai bloc.
11. 1200-1500 mots utiles ; aucun passage recopié d'une autre page du site.
12. Les 12 blocs de `anatomie-page-service.md` sont présents et dans l'ordre.
13. Aucun trou (`[insérer…]`, lorem, « paragraphe à venir »).
14. Aucun prix, délai, aide financière, taux de TVA ni garantie non validés —
    sinon `[À COMPLÉTER]` visible dans le livrable, jamais dans le HTML livré
    comme définitif.
15. Aucune ville hors Doubs.
16. NAP au caractère près : « 18 rue du Professeur Haag, 25000 Besançon ».
17. Nom écrit « RUSHITI Rénovation » (jamais « SARL RUSHITI Rénovation »).
18. Compteurs d'avis et note : relevés du jour et datés, ou absents.

### Données structurées
19. `Service` présent, `serviceType` cohérent avec la page.
20. `BreadcrumbList` présent et conforme au fil d'Ariane visible.
21. `FAQPage` limité aux questions **visibles** dans la page ; réciproquement,
    une FAQ visible sans balisage est un ⚠️.
22. Aucun `aggregateRating` ni `Review` auto-déclaré.
23. `HousePainter`/`LocalBusiness` du socle non dupliqué avec des valeurs
    divergentes (téléphone, adresse, URL).
24. JSON-LD sans JavaScript parasite, valide au test des résultats enrichis
    **et** au validator schema.org.

### Images et performance
25. Toutes les images ont un `alt` descriptif (pas une liste de mots-clés) ;
    le logo a un alt de marque, pas de mot-clé.
26. `width` et `height` déclarés sur chaque image (stabilité de mise en page).
27. `loading="lazy"` sauf l'image du hero, qui doit rester prioritaire.
28. Format WebP, images de galerie compressées.
29. Aucune ressource bloquante ajoutée par la page (pas de bibliothèque
    externe pour un carrousel de 6 photos).

### Conversion
30. Deux CTA visibles sans scroller sur mobile, cibles ≥ 48×48 px.
31. Téléphone cliquable `tel:+33760279897` présent en haut **et** en bas.
32. Formulaire : champs minimaux, labels explicites, `type="tel"` et
    `type="email"` corrects, police ≥ 16 px (évite le zoom iOS).
33. Message de confirmation après envoi, et destinataire réellement branché.
34. WhatsApp et e-mail présents dans le bloc de conversion.

### Maillage et rattachement
35. 3 à 6 liens sortants contextuels, ancres descriptives, aucune vers une
    page hors périmètre ni vers rushiti.fr ou rushiti-peinture.fr.
36. Au moins 3 pages existantes pointent vers cette page (à vérifier dans le
    code des pages sources, pas en intention).
37. Fil d'Ariane visible, cohérent avec le `BreadcrumbList`.
38. Page présente dans le sitemap ; aucune URL orpheline.
39. Aucune concurrence frontale avec une page sœur (voir
    `rushiti-cannibal-check` en cas de doute).
40. Entrée mise à jour dans `docs/seo/regjistri-fjale-kyce.csv` : requête
    portée, page, date du verdict, agent de mesure.

## B. Redirections 301

- Une URL existante ne change **jamais** sans 301 : la page perd sinon son
  historique, ses liens et ses positions.
- Redirection **directe**, sans chaîne (A → C, pas A → B → C).
- Après déploiement : vérifier le code de statut sur l'URL réelle, mettre à
  jour tous les liens internes vers la nouvelle cible (une 301 ne dispense
  pas de corriger le maillage), retirer l'ancienne URL du sitemap.
- Consigner la règle et son motif dans le fichier de redirections du dépôt de
  production, avec la date.

## C. Après déploiement

1. Vérifier l'URL live : statut 200, title et meta lus **dans le code
   source** (une SERP peut afficher un titre réécrit par Google — ce n'est
   pas une preuve du contenu de la balise).
2. Sitemap régénéré, puis inspection de l'URL dans la Search Console et
   demande d'indexation.
3. Contrôle des résultats enrichis sur l'URL live.
4. Relever et **dater** le point de départ : impressions, clics, position
   moyenne, CTR de la page et de sa requête cible.
5. Vérifier que le déploiement est complet : sur Cloudflare Pages, un
   déploiement partiel laisse des pages à l'ancienne version — recontrôler
   quelques URL voisines (voir `rushiti-visibilite-ia`).

## D. Mesure

Fenêtre : **4 à 6 semaines** minimum avant de conclure. En dessous, on lit du
bruit et de la saisonnalité.

| Indicateur | Source | Lecture |
|---|---|---|
| Impressions de la requête cible sur la page | Search Console, croisement requête × page | La page porte-t-elle sa requête, ou une autre page la lui prend-elle ? |
| Position moyenne de la requête cible | Search Console | Comparer à la valeur de départ datée, jamais à un souvenir |
| CTR à position comparable | Search Console | Un CTR faible à bonne position = problème de title/meta → `rushiti-ctr-opportunites` |
| Pages qui se partagent la requête | croisement requête × page | Plus d'une page = cannibalisation → `rushiti-cannibal-check` |
| Demandes de devis attribuées | formulaire, appels, WhatsApp | Le seul indicateur qui paie les factures |

Règles de restitution :

- Un effet se qualifie **fort / moyen / faible**, avec le motif et la preuve.
  Aucun « +150 % de trafic », aucun « top 3 en 3 mois ».
- Une comparaison entre deux périodes non comparables (saison, longueur,
  changement de site) se signale — elle ne se maquille pas.
- Si la donnée manque, on écrit qu'elle manque.

Passage de relais : `rushiti-regression-seo` pour le suivi dans le temps,
`rushiti-quick-wins-gsc` pour les gains rapides, `rushiti-maillage-interne`
si la page reste sous-liée.
