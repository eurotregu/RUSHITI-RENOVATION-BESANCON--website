# Audit premium du site rushiti-renovation.fr — 03/09/2026

| | |
|---|---|
| Déclencheur | Demande d'Isuf : « auditoje si një profesionist premium rushiti-renovation.fr dhe më rekomandoni në detaje çka duhet përmirësuar, adaptuar, fshirë, shtuar » |
| Périmètre | **Site en ligne** rushiti-renovation.fr (servi par Cloudflare Pages + Worker), 755 URL du sitemap. Cette copie GitHub Pages n'est traitée qu'au point 26. |
| Méthode | Relevé sur pièces le 03/09/2026 : 20 pages servies (accueil, 2 piliers, 2 pages locales, blog, index blog, à propos, contact, zones, réalisations, prix, plaquiste, 4 pages B2B, mentions légales, merci, 404), `robots.txt`, `sitemap.xml`, `llms.txt`, redirections www/http, capture mobile 390 px de l'accueil, deux SERP de contrôle. Aucune page modifiée, aucun compte touché. |
| Non mesuré | Core Web Vitals terrain et labo : quota PageSpeed épuisé → `[DONNÉE MANQUANTE — lancer PSI mobile sur / , /peinture-interieure-besancon, /degat-des-eaux-besancon]`. Positions, impressions, clics : `[DONNÉE MANQUANTE — export Search Console]`. En-têtes HTTP (HSTS, cache) : non lisibles avec l'outillage de la session. |
| Skill de référence | `rushiti-audit-seo` (format du rapport), routage vers les skills d'exécution |

---

## 1. Résumé pour Isuf et Yll

**Le site est solide.** Le travail d'août a tenu : sitemap unique de 755 URL servi par le domaine, robots propre (IA autorisées, 6 aspirateurs bloqués), canonicals, www et http redirigés, FAQ visibles et balisées (les 766 questions fantômes du 31/08 sont soldées sur toutes les pages contrôlées), `/merci` en noindex, blog signé avec sources, page prix honnête, pages B2B bien pensées, bandeau sticky appel + devis, WhatsApp. Le ton « le problème avant la solution » est exactement celui des Guidelines. Ce n'est pas un site à refaire : c'est un site à **mettre en cohérence et à humaniser**.

**Ce qui coûte des devis aujourd'hui, par ordre d'impact :**

1. **Le site se contredit lui-même** sur des faits que Google et les IA lisent : `/llms.txt` annonce 29 avis, des horaires 8h–18h en semaine et « raison sociale : RUSHITI Rénovation » ; le site affiche 34 avis, 7h–20h30 et 7 jours sur 7. Une IA qui répond « fermé le samedi » vous fait perdre l'appel.
2. **Les mentions légales sont fausses sur deux points obligatoires** : hébergeur (le site n'est pas hébergé par RUSHITI) et dénomination (la SARL s'appelle « Rushiti », pas « RUSHITI Rénovation »). Et la section cookies déclare « un seul traceur » alors qu'un conteneur Google Tag Manager se charge sur chaque page.
3. **Cinq pages de conversion se terminent par le mauvais appel à l'action** : la page syndic, la page devis assurance, la page remise en état locative, la page plaquiste et la page prix se concluent par « Des murs à ratisser avant peinture ? … en lumière rasante ». Un gestionnaire d'immeuble qui lit ça referme la page.
4. **Cinq étoiles affichées sur chaque avis** alors que les notes individuelles n'ont pas été relevées (règle du 22/08) : donnée non vérifiée, sur toutes les pages.
5. **Environ 700 pages locales identiques à 88 %** (mesuré : plâtrerie Mamirolle contre Deluz). C'est le risque structurel n°1 du site, déjà identifié en août, dont le plan par paliers n'est pas appliqué.
6. **Le formulaire anti-robot hCaptcha (≈ 600 Ko de JavaScript) se charge sur chaque page commerciale**, même si personne ne touche le formulaire. Sur mobile en 4G, c'est du temps perdu avant que la page réponde.

**Gains rapides de la semaine** (chacun ≤ 1 h de travail) : corriger `/llms.txt`, corriger les mentions légales, remplacer le bloc CTA « ratisser » sur les 5 pages, retirer les étoiles par avis (ou relever les notes réelles), rendre lisible le bouton e-mail du bloc final (texte bleu nuit sur fond bleu nuit), dédoublonner la balise Google Fonts.

---

## 2. Ce qui est en ordre (à ne pas retoucher)

Vérifié sur pièces, pour que personne ne « corrige » ce qui fonctionne :

- `robots.txt` : une seule ligne `Sitemap`, `User-agent: *` autorisé, GPTBot / ClaudeBot / PerplexityBot non bloqués ; Amazonbot, Bytespider, FacebookBot, Google-CloudVertexBot, meta-externalagent, TikTokSpider bloqués. Le correctif Worker du 31/08 est en production.
- `sitemap.xml` : `<urlset>` unique de 755 URL, aucune URL www, aucun slash final, `/merci` absent (correct).
- Redirections : `http://www.rushiti-renovation.fr/` → `https://rushiti-renovation.fr/` (une seule cible finale).
- Page 404 : vrai code 404, contenu utile (6 raccourcis services + CTA).
- Titles et meta descriptions : uniques, 49–58 caractères pour les titles, 138–154 pour les descriptions, mot-clé + ville devant, marque en fin. Aucun `[À COMPLÉTER]` en production sur les pages contrôlées.
- Un seul H1 par page, hiérarchie H2/H3 logique, FAQ en `<details>` visibles et strictement égales au JSON-LD `FAQPage` (0 question invisible sur peinture, dégât des eaux, Mamirolle, blog).
- JSON-LD : `LocalBusiness`+`HousePainter`+`HomeAndConstructionBusiness` avec `@id` unique, NAP au caractère près, téléphone E.164, horaires identiques au pied de page, `sameAs` 7 profils ; `Service` + `BreadcrumbList` + `FAQPage` sur les piliers ; `BlogPosting` avec auteur, dates, `ContactPage`, `AboutPage`, `CollectionPage`.
- Images : WebP, `alt` descriptifs, `width`/`height` déclarés sur les piliers, `loading="lazy"` hors image de tête, image LCP en `preload` + `loading="eager"`.
- Conversion : téléphone cliquable dans l'en-tête, le corps, le pied et la barre sticky ; formulaire 7 champs + consentement ; WhatsApp pré-rempli ; page `/merci` avec « ce qui se passe maintenant ».
- Contenu : piliers de 1 970 (peinture) et 2 300 mots (dégât des eaux), structure problème → diagnostic → méthode → prix → FAQ conforme aux Guidelines ; TVA toujours conditionnée (« 10 %, 5,5 % ou 20 % selon l'éligibilité ») ; DTU cités exacts (59.1, 25.41) ; IRSI présent sur le silo sinistre ; recherche de fuite explicitement hors périmètre ; aucune mention RGE / Qualibat.
- Pixel Meta chargé uniquement après consentement ; Consent Mode v2 par défaut « denied » ; lien « Gérer mes cookies » en pied de page.

---

## 3. Constats détaillés

Sévérité : 🔴 critique · 🟠 élevée · 🟡 moyenne · 🟢 faible. Verbe demandé par Isuf entre crochets : **[Corriger] [Adapter] [Supprimer] [Ajouter]**.

### A. Cohérence des faits et conformité

**1. `/llms.txt` contredit le site** 🔴 [Corriger]
- Page : `https://rushiti-renovation.fr/llms.txt`
- Impact : ce fichier est écrit pour les moteurs de réponse IA. Ils y lisent aujourd'hui « 4,7/5 sur **29** avis » (site : 34), « Horaires : du lundi au vendredi, **8h–18h** » (site et JSON-LD : Lun–Ven 7h–20h30, Sam 8h–20h30, Dim 9h–17h30), « **Raison sociale : RUSHITI Rénovation** » (dénomination sociale : Rushiti, SARL). Trois des 12 faits validés du skill `rushiti-faits-marque` sont faux à la source.
- Preuve : contenu servi le 03/09/2026, lignes « Avis », « Horaires », « Raison sociale ».
- Correction : régénérer `/llms.txt` depuis le socle (34 avis datés, horaires du pied de page, « Dénomination sociale : Rushiti (SARL) — nom commercial RUSHITI Rénovation »), y ajouter le SIRET déjà présent, la décennale ERGO, les 4 pages B2B et la page prix (absentes), et dater le fichier. Ajouter ce fichier à la matrice mensuelle faits × sources.
- Effort : Rapide · Skill : `rushiti-faits-marque` (contrôle), `rushiti-visibilite-ia` (rédaction)

**2. Mentions légales : hébergeur et dénomination faux, section cookies incomplète** 🔴 [Corriger]
- Page : `/mentions-legales`
- Impact : l'article 6-III de la LCEN impose le nom et les coordonnées de l'hébergeur. La page dit « hébergé par RUSHITI Rénovation — 18 rue du Professeur Haag » alors que le site est servi par Cloudflare Pages. L'éditeur est présenté comme « RUSHITI Rénovation, SARL » : le nom commercial est mis à la place de la dénomination sociale (règle absolue des Guidelines). La section 7 affirme « un seul traceur : le Pixel Meta » et « aucun autre cookie de suivi ni de mesure d'audience », alors que chaque page charge le conteneur Google Tag Manager `GTM-KPM3GQB6` (au premier geste de l'utilisateur ou 1,5 s après le chargement) et la balise Cloudflare Web Analytics.
- Preuve : texte servi le 03/09 ; scripts inline de l'accueil (`gtm.js?id=GTM-KPM3GQB6`, `static.cloudflareinsights.com/beacon.min.js`).
- Correction : (a) Éditeur : « Rushiti, SARL au capital de 1 000 €, nom commercial RUSHITI Rénovation, RCS Besançon 905 214 631 » ; (b) Hébergeur : Cloudflare, Inc. `[À COMPLÉTER : adresse et contact de l'hébergeur tels qu'indiqués dans les CGU Cloudflare]` ; (c) Cookies : ouvrir le conteneur GTM et lister ce qu'il contient `[À VÉRIFIER dans Tag Manager]` — si une balise GA4 ou Google Ads y vit, le bandeau et la section 7 doivent mentionner la mesure d'audience, sinon retirer le conteneur ; mentionner Cloudflare Web Analytics (sans cookie, exempté de consentement, mais à déclarer par transparence).
- Effort : Rapide · Décision : Isuf (document légal — cadre fourni, texte à valider)

**3. Cinq étoiles affichées sur chaque avis, notes individuelles non relevées** 🔴 [Corriger]
- Pages : bloc « Ils nous ont fait confiance » partagé par l'accueil, tous les piliers, toutes les pages locales et B2B (≈ 740 pages)
- Impact : le relevé du 22/08 (`avis-google-releve-2026-08-22.md`) précise que le miroir de la fiche ne donne pas la note de chaque avis et interdit d'afficher « 5 étoiles » par carte (« une moyenne de 4,7 sur 34 implique mécaniquement des notes inférieures à 5 »). En production, chaque carte porte ★★★★★. C'est une donnée inventée au sens du garde-fou n°1, et un risque de contestation par un lecteur qui compare avec la fiche Google. La mention « relevé le 22/08/2026 » prévue par la doctrine est absente.
- Preuve : texte servi (« ★★★★★ « Nous avons fait appel… » Jérôme J. · Avis Google ») sur l'accueil, `/platrerie-deluz`, `/plaquiste-besancon`, `/prix-travaux-renovation-besancon`.
- Correction : soit Isuf relève la note réelle de chacun des 3 avis affichés dans son interface Google Business (alors les étoiles restent, avec la date du relevé), soit retirer les étoiles par carte et ne garder que « 4,7 / 5 · 34 avis Google · relevé le JJ/MM/AAAA ».
- Effort : Rapide (un gabarit) · Décision : Isuf

**4. `aggregateRating` et `review` dans le JSON-LD de l'accueil** 🟠 [Supprimer]
- Page : `/` (nœud `LocalBusiness`)
- Impact : la doctrine du 22/08 exclut l'`aggregateRating` (avis tiers Google) ; les consignes Google interdisent les avis « auto-déclarés » sur `LocalBusiness` (le rich result ne s'affiche pas et le balisage peut être considéré comme trompeur). Le point est en attente d'arbitrage depuis l'audit schema du 31/08.
- Preuve : JSON-LD servi : `"aggregateRating": {"ratingValue": "4.7", "reviewCount": "34"}` + `"review"`.
- Correction : retirer les deux propriétés ; garder la note en texte visible daté. Ajouter au même nœud `legalName: "Rushiti"` (absent partout) et remplacer les coordonnées `geo` du centre-ville (47.238, 6.0243, présentes sur 735 pages) par celles du 18 rue du Professeur Haag `[À COMPLÉTER : relever sur la fiche Google]`.
- Effort : Rapide · Skill : `schema-builder` puis `rushiti-jsonld-validator`

**5. Doublon de fiche sur RDV Artisans** 🟡 [Corriger]
- Source : SERP « plaquiste Besançon », résultat rdvartisans.fr : « RUSHITI Rénovation · DAOU MCHINDRA · **SARL RUSHITI** · … »
- Impact : deux fiches pour la même entreprise = signal NAP incohérent (nom), avis dispersés.
- Correction : réclamer la fiche « SARL RUSHITI », la fusionner ou la faire supprimer, aligner sur le NAP de référence.
- Effort : Rapide · Skill : `rushiti-seo-local`

### B. Conversion et expérience

**6. Bloc de fin « Des murs à ratisser avant peinture ? » sur cinq pages qui ne parlent pas de ratissage** 🟠 [Corriger]
- Pages : `/renovation-syndic-gestionnaire-besancon`, `/devis-assurance-degat-des-eaux-besancon`, `/remise-en-etat-logement-locatif-besancon`, `/plaquiste-besancon`, `/prix-travaux-renovation-besancon`, et, vus au dépôt le 03/09, `/amenagement-commerce-bureau-besancon`, `/renovation-appartement-besancon` (les piliers, pages locales, accueil, à propos, contact et zones ne sont pas touchés)
- Impact : dernier bloc avant le pied de page, donc dernier argument lu par un syndic, un gestionnaire ou un expert d'assurance : « Nous passons examiner vos murs en lumière rasante ». Fuite de gabarit qui casse la crédibilité au moment de décider.
- Preuve : H2 final servi le 03/09 sur les 5 URL.
- Correction : un bloc de fin par intention — syndic : « Un immeuble à remettre en état à Besançon ? … devis présentable en conseil syndical » ; assurance : « Un sinistre à documenter ? … devis détaillé pour votre dossier » ; locatif : « Un logement à relouer ? … » ; plaquiste : « Une cloison, un plafond, un doublage ? … » ; prix : « Un chantier à chiffrer ? … ». Vérifier par script que le H2 final de chaque page contient un mot du H1 (test de régression à ajouter à `korrigjime-prodhim/`).
- Effort : Rapide

**7. Bouton e-mail illisible dans le bloc CTA final** 🟠 [Corriger]
- Pages : accueil (bloc « Un diagnostic gratuit, et vous saurez exactement quoi faire »), même gabarit sur les piliers et pages locales
- Impact : le bouton `btn ghost` affiche « contact@rushiti-renovation.fr » en bleu nuit sur fond bleu nuit (capture mobile 390 px) : contraste quasi nul, illisible, non conforme WCAG 1.4.3 (RGAA). C'est l'un des trois moyens de contact du site.
- Correction : texte et bordure en blanc (ou `--bg-soft`) sur fond `--navy-dark`, contraste ≥ 4,5:1 ; contrôler aussi le bouton `ghost` du 404 et de `/merci`.
- Effort : Rapide (une règle CSS)

**8. hCaptcha chargé à l'ouverture sur toutes les pages à formulaire « Demande rapide »** 🟠 [Adapter]
- Pages : piliers (peinture, dégât des eaux…), prix, plaquiste, 4 pages B2B, contact
- Impact : `js.hcaptcha.com/1/api.js` est appelé dès le chargement (async/defer), puis injecte ≈ 617 Ko de script et deux iframes, sur des pages dont le formulaire est en bas. Sur mobile, cela pèse sur l'INP et le temps de réactivité, pour une protection qui ne sert qu'au moment de l'envoi. Chiffres terrain : `[DONNÉE MANQUANTE — PSI]`.
- Correction : charger hCaptcha au premier `focus` sur un champ du formulaire ou quand le formulaire entre dans le viewport (`IntersectionObserver`, déjà utilisé sur le site pour les animations). Alternative : Cloudflare Turnstile (invisible, sans case à cocher, gratuit, déjà chez l'hébergeur), soutenu par Web3Forms.
- Effort : Moyen · Skill : `rushiti-audit-technique`

**9. Google Fonts appelé deux fois, en bloquant le rendu** ~~🟡~~ **Retiré le 03/09 : faux positif.** Le second `<link>` vu dans le rendu est le repli `<noscript>` du motif `media="print" onload="this.media='all'"` ; les sources ne contiennent qu'un appel, non bloquant. Reste valable : l'auto-hébergement des polices (optionnel).
- Pages : toutes
- Preuve : deux balises `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces…&family=Inter…">` strictement identiques dans le `<head>` servi (une avec `media="all"`), après deux `preconnect`.
- Impact : requête dupliquée, CSS de polices bloquant, dépendance à un domaine tiers pour l'affichage du texte.
- Correction : une seule balise ; mieux : auto-héberger Fraunces (600/700, sous-ensemble latin) et Inter (400/500/600) en woff2 sur `/assets/fonts/`, `font-display: swap`, `preload` de la police de titre. Supprime aussi la question RGPD des Google Fonts.
- Effort : Moyen

**10. Page Contact trop nue** 🟡 [Ajouter]
- Page : `/contact` (313 mots)
- Impact : pas de repère de délai (le « sous 24 à 48 h ouvrées » validé n'apparaît que sur `/merci`), pas de plan d'accès, pas de visage, pas de « ce qui se passe après ». Le prospect hésitant n'a rien pour se rassurer avant de donner son numéro.
- Correction : reprendre les 3 étapes de `/merci` au-dessus du formulaire ; ajouter « Nous vous rappelons sous 24 à 48 h ouvrées » ; carte (lien `hasMap` existant, ou iframe Google Maps chargée au clic pour éviter les cookies) ; photo d'Isuf et Yll (accord RGPD non requis pour les dirigeants, à confirmer par eux) ; bouton WhatsApp à côté du téléphone.
- Effort : Rapide

**11. Accueil mobile : 13 000 px de haut, galerie en colonne unique** 🟢 [Adapter]
- Preuve : capture 390 × 13 036 px ; 8 cartes réalisations pleine largeur ; hero sans visuel au-dessus de la ligne de flottaison (l'image arrive après la liste de 4 coches).
- Correction : galerie en 2 colonnes sur mobile (ou carrousel horizontal), 4 réalisations au lieu de 8 sur l'accueil ; remonter l'image de tête à côté du H1 dès 390 px ; préférer une photo des artisans au travail (preuve humaine) au papier peint à motifs.
- Effort : Moyen

### C. Contenu et confiance (E-E-A-T)

**12. Page À propos trop mince pour porter la confiance** 🟠 [Ajouter]
- Page : `/a-propos` (390 mots, 3 photos de chantier sans dimensions déclarées, aucune photo des dirigeants)
- Impact : Google et les IA évaluent l'expérience réelle sur cette page ; un client qui confie un appartement veut voir qui vient. La page répète les blocs de l'accueil (méthode, garanties) et n'apporte rien de propre.
- Correction : (a) portraits d'Isuf et Yll sur chantier, prénoms, rôles ; (b) parcours en 4 dates `[À COMPLÉTER par Isuf : formation, années, création de la SARL le 04/11/2021]` ; (c) « pourquoi nous faisons le diagnostic gratuit » en 3 phrases ; (d) matériel et méthodes (humidimètre, lumière rasante, produits) ; (e) attestation décennale ERGO téléchargeable en PDF (le numéro de contrat est déjà public dans les mentions légales) ; (f) JSON-LD `Person` pour Isuf et Yll avec `@id`, reliés à `founder` et à `author` des articles ; (g) `width`/`height` sur les 3 images.
- Effort : Moyen · Skill : `rushiti-page-service` (mode mise à niveau), `schema-builder`

**13. Réalisations : 17 photos muettes, aucune étude de cas, aucun avant/après** 🟠 [Ajouter]
- Page : `/realisations`
- Impact : c'est la page « preuve » et elle ne raconte rien : pas de problème, pas de diagnostic, pas de résultat, pas de commune, pas de durée. Les pages locales renvoient toutes vers cette galerie générique. Les IA ne peuvent rien en citer.
- Correction : 3 à 5 études de cas sur URL propre `/realisations/{slug}` (problème vécu → diagnostic → intervention en trois temps → résultat → citation client avec accord écrit), une par silo prioritaire (dégât des eaux, peinture, placo, isolation) ; paires avant/après légendées ; lien depuis la page locale de la commune concernée (première vraie différenciation locale). Matière brute : `rushiti-memo-chantier`, rédaction : `rushiti-etudes-de-cas`. RGPD : jamais de nom ni d'adresse, accord écrit pour toute photo identifiable.
- Effort : Important (mais le plus rentable du plan)

**14. Grille locale : ≈ 700 pages identiques à 88 %** 🟠 [Adapter] [Supprimer]
- Pages : `/{service}-{zone}` — 114 peinture, 92 isolation, 75 plâtrerie, 75 sols, 75 dégât des eaux, 45 ratissage, 42 cloisons, 40 papier peint, 38 faux plafonds, 27 vitrification, 18 parquet, 18 doublage, 16 toile de verre, 16 sol PVC, 15 ragréage, 15 lino
- Preuve : `/platrerie-mamirolle` (1 646 mots) contre `/platrerie-deluz` (1 582 mots) : **12 % de mots uniques**, 19 % de séquences de 5 mots uniques. Le contenu propre se limite à un paragraphe géographique (distance, population, altitude, repère), une phrase de « chantier type » et la dernière question FAQ. Les avis, la méthode, les prix, les FAQ sont identiques.
- Impact : Google traite ce motif comme du contenu à l'échelle : pages indexées mais jamais classées, budget de crawl dilué, et risque d'action manuelle « scaled content abuse ». **Rectificatif du 03/09 (soir)** : le plan par paliers d'août (A 18 / B 10 / C 5) **est appliqué** en production (706 pages de grille, 644 → 301 redirections, 31 zones en léger dépassement justifié par la GSC). Le problème restant est le contenu : 16 % de contenu propre en médiane sur les 706 pages (`grille-locale/mesure-differenciation-2026-09-03.csv`).
- Correction : (a) ~~appliquer la grille~~ déjà fait en août ; ne pas supprimer les 31 pages en dépassement sans l'export GSC qui les a justifiées ; (b) pour les zones A et B, exiger une preuve locale réelle par page (étude de cas, photo, avis mentionnant la commune, type de bâti observé) ou ne pas garder la page ; (c) ne jamais créer de page « rénovation-{commune} » sans passer par la porte `rushiti-keyword-map` (la PR #9 avait créé ce risque) ; (d) mesurer avant/après avec un groupe témoin.
- Effort : Important · Décision : Isuf (suppression d'URL) · Skills : `rushiti-keyword-map`, `rushiti-page-locale`, `rushiti-journal-experiences`

**15. Cannibalisation probable plaquiste / plâtrerie et isolation / isolation intérieure** 🟡 [Adapter]
- Pages : `/plaquiste-besancon` vs `/platrerie-besancon` (+ `/cloisons-`, `/doublage-murs-`, `/faux-plafonds-besancon`) ; `/isolation-besancon` vs `/isolation-interieure-besancon`
- Preuve : l'accueil lie « plaquiste à Besançon » vers `/plaquiste-besancon`, la navigation lie « Plâtrerie » vers `/platrerie-besancon`, le pied de page lie les deux ; la page prix affiche des fourchettes **identiques** pour isolation et ITI (45–70 / 70–100 €/m²), ce qui prouve que l'offre est la même.
- Correction : sans export GSC, aucune fusion à décider aujourd'hui. Demander le rapport requête × page sur « plaquiste besançon », « plâtrier besançon », « isolation besançon », « isolation intérieure besançon » ; si deux URL se partagent une requête, différencier (ITI = murs par l'intérieur uniquement ; isolation = combles + phonique) ou canonicaliser.
- Effort : Moyen · Skill : `rushiti-cannibal-check` (données requises : `[DONNÉE MANQUANTE — GSC 16 semaines]`)

**16. Blocs de liens locaux surdimensionnés sur les piliers** 🟢 [Adapter]
- Pages : `/peinture-interieure-besancon` (120 liens internes uniques, 12 sous-titres H3 « Vallée du Doubs (NE) », « Plateau Ouest »…), `/degat-des-eaux-besancon` (123)
- Impact : ces blocs poussent la FAQ et le formulaire loin sous la ligne de flottaison et diluent le maillage ; ils font double emploi avec `/zones-intervention` (340 liens).
- Correction : garder 13 quartiers + 8 communes palier A sur le pilier, renvoyer le reste vers le hub zones ; passer le bloc en `<details>` replié sur mobile.
- Effort : Rapide · Skill : `rushiti-maillage-interne`

**17. Blog : bon socle, deux ajouts** 🟢 [Ajouter]
- Page : `/blog` (11 articles du 02/06 au 20/08, auteur, sources, FAQ visible)
- Correction : (a) relier chaque signature « Isuf Rushiti » à une ancre `/a-propos#isuf` portant le `Person` du point 12 ; (b) afficher « Mis à jour le » (le JSON-LD porte `dateModified` 30/08, la page ne l'affiche pas) ; (c) prochain article à écrire côté silo dégât des eaux B2B (« ce que l'expert d'assurance vérifie sur un devis ») : `rushiti-architecte-seo`.
- Effort : Rapide

**18. Termes géographiques non canoniques sur l'accueil** 🟢 [Corriger]
- Preuve : « la Boucle du Doubs, le secteur Vauban » dans « Le contexte bisontin ».
- Correction : « le centre ancien de Besançon » et un quartier canonique (Battant, Chaprais-Cras) — liste du socle. Le mot « Boucle » avec majuscule est toléré comme description, jamais comme quartier.
- Effort : Rapide

### D. Technique

**19. Cartes Twitter absentes sur 100 % des pages contrôlées** ~~🟡~~ **Caduc (03/09 soir)** : retrait volontaire décidé par Isuf le 02/09 (pas de compte X, les réseaux utilisés lisent l'Open Graph).
- Preuve : 0 balise `twitter:*` sur les 9 pages analysées (OG complet partout). Le correctif testé existe (PR #61, 726 pages).
- Impact : limité (LinkedIn, WhatsApp, Facebook lisent l'OG) mais X, Slack et certains agrégateurs non.
- Correction : appliquer le script de la PR #61 dérivé des `og:*`.
- Effort : Rapide

**20. `lastmod` du sitemap non maintenu** 🟢 [Corriger]
- Preuve : 711 URL au 2026-08-20, 32 au 2026-08-21, 11 articles de blog au **2026-06-12** alors que `dateModified` = 2026-08-30 dans le JSON-LD ; `changefreq`/`priority` sur 755 URL (ignorés par Google).
- Correction : générer `lastmod` depuis la date réelle de modification du fichier (git) ou le retirer ; supprimer `changefreq` et `priority`.
- Effort : Rapide

**21. Chargement de GTM indépendant du consentement** 🟡 [À vérifier]
- Preuve : `GTM-KPM3GQB6` se charge au premier geste ou 1,5 s après `load`, avant tout clic sur le bandeau ; Consent Mode par défaut « denied » sur les 4 signaux.
- Impact : conforme uniquement si toutes les balises du conteneur respectent le Consent Mode. Aucun `G-` GA4 n'est visible dans le HTML : la mesure d'audience passe donc par GTM ou n'existe pas. Sans GA4, aucune conversion (appel, formulaire, WhatsApp) n'est mesurée côté Google.
- Correction : inventaire du conteneur `[À VÉRIFIER par Isuf ou accès GTM]` ; si vide, brancher GA4 + événements `clic_telephone`, `envoi_formulaire`, `clic_whatsapp` derrière le consentement (le Pixel Meta trace déjà ces trois événements) ; mettre le bandeau et les mentions légales en accord.
- Effort : Moyen · Skill : `rushiti-ga4-gtm`

**22. Coordonnées `geo` approximatives et `legalName` absent** 🟢 — voir point 4.

**23. Images sans dimensions sur À propos** 🟢 — voir point 12.

**24. En-têtes de sécurité et cache** — non mesurables ici. À contrôler : `Strict-Transport-Security`, `X-Content-Type-Options`, `Cache-Control` long sur `/assets/` avec versionnement. `[DONNÉE MANQUANTE — curl -I depuis un poste non filtré]`.

### E. Identité visuelle

**25. Charte graphique Guidelines v2.7 non appliquée** 🟡 [Adapter] · Décision Isuf
- Preuve : variables CSS servies : `--navy: #1B3A5B`, `--accent: #E8743B` (orange), `--ok: #2E7D52`. Guidelines : `#002B4B` (bleu nuit), `#1A75BB` (bleu), `#016738` (vert), `#EB1C24` (rouge alerte). Polices Fraunces + Inter (site) contre Montserrat + Open Sans (copie GitHub Pages) : deux identités visuelles coexistent.
- Impact : incohérence entre le site, les devis, les courriers et les réseaux qui suivent la charte.
- Correction proposée (à trancher) : aligner `--navy` sur `#002B4B`, liens et éléments secondaires sur `#1A75BB`, états positifs sur `#016738`, réserver `#EB1C24` aux alertes (dégât des eaux, erreurs de formulaire). Pour le bouton principal, l'orange actuel n'est pas dans la charte : soit la charte ajoute une couleur d'action, soit le CTA passe en `#1A75BB` sur fond clair et blanc sur fond bleu nuit. Ne pas utiliser le rouge pour « Demander un devis ». Vérifier tous les contrastes après changement.
- Effort : Moyen

### F. Cette copie GitHub Pages

**26. La copie one-page contredit la production et les garde-fous** 🟡 [Supprimer] ou [Adapter]
- Fichier : `index.html` de ce dépôt (publié sur GitHub Pages à chaque push sur `main`, en `noindex`)
- Preuve : « Rénovation de A à Z : sols, murs, plafonds, **électricité et plomberie** » (hors métier), « Carrelage & Sol » (prestation non arbitrée), compteurs « **500+ Projets Réalisés** » et « **100 % Clients Satisfaits** » (statistiques inventées), galerie en placeholders colorés, `priceRange: "€€"` et `geo` approximatifs, polices et couleurs différentes du site.
- Impact : la page est en `noindex` mais reste publique et partageable ; elle porte des affirmations interdites par les Guidelines.
- Correction : décision Isuf — soit remplacer `index.html` par une redirection vers `https://rushiti-renovation.fr/` (le dépôt garde son rôle : docs, skills, scripts), soit aligner le contenu (retirer électricité/plomberie/carrelage, supprimer les compteurs, vraies photos). La première option est la plus sûre.
- Effort : Rapide

---

## 4. Plan d'action priorisé

| Priorité | Action | Verbe | Sévérité | Effort | Qui décide / exécute |
|---|---|---|---|---|---|
| P0 | Régénérer `/llms.txt` (34 avis datés, horaires réels, dénomination) | Corriger | 🔴 | Rapide | `rushiti-visibilite-ia` → validation Isuf |
| P0 | Mentions légales : dénomination, hébergeur, cookies/GTM | Corriger | 🔴 | Rapide | cadre fourni, texte validé par Isuf |
| P0 | Étoiles par avis : relever les notes réelles ou retirer ; dater le relevé | Corriger | 🔴 | Rapide | Isuf |
| P0 | Bloc CTA « ratisser » sur 5 pages B2B/prix/plaquiste | Corriger | 🟠 | Rapide | gabarit |
| P0 | Bouton e-mail illisible (contraste) | Corriger | 🟠 | Rapide | CSS |
| P1 | Retirer `aggregateRating`/`review`, ajouter `legalName`, vraies `geo` | Supprimer / Ajouter | 🟠 | Rapide | `schema-builder`, `rushiti-jsonld-validator` |
| P1 | hCaptcha à la demande (ou Turnstile) | Adapter | 🟠 | Moyen | `rushiti-audit-technique` |
| P1 | ~~Google Fonts : une balise~~ (faux positif, retiré le 03/09) ; auto-hébergement optionnel | Adapter | 🟢 | Moyen | CSS |
| P1 | Page À propos : visages, parcours, attestation, `Person` | Ajouter | 🟠 | Moyen | `rushiti-page-service` |
| P1 | Page Contact : étapes, délai validé, carte, WhatsApp | Ajouter | 🟡 | Rapide | gabarit |
| P1 | Inventaire GTM, GA4 + événements derrière consentement | À vérifier / Ajouter | 🟡 | Moyen | `rushiti-ga4-gtm` |
| P1 | Fiche doublon RDV Artisans | Corriger | 🟡 | Rapide | `rushiti-seo-local` |
| P2 | 3 à 5 études de cas avec avant/après, liées aux pages locales | Ajouter | 🟠 | Important | `rushiti-memo-chantier` → `rushiti-etudes-de-cas` |
| P2 | Grille locale par paliers : consolider palier C, exiger une preuve locale en A/B | Adapter / Supprimer | 🟠 | Important | Isuf + `rushiti-keyword-map` + `rushiti-page-locale` |
| P2 | Cannibalisation plaquiste/plâtrerie, isolation/ITI (après export GSC) | Adapter | 🟡 | Moyen | `rushiti-cannibal-check` |
| P2 | Blocs de liens locaux des piliers → hub zones | Adapter | 🟢 | Rapide | `rushiti-maillage-interne` |
| P2 | Charte v2.7 : arbitrage couleurs, puis application | Adapter | 🟡 | Moyen | Isuf |
| P3 | Twitter Cards (PR #61), `lastmod` réel, termes géographiques canoniques, « Mis à jour le » sur le blog | Ajouter / Corriger | 🟢 | Rapide | scripts existants |
| P3 | Copie GitHub Pages : redirection vers la production ou alignement | Supprimer / Adapter | 🟡 | Rapide | Isuf |
| P3 | Accueil mobile : galerie 2 colonnes, image de tête humaine | Adapter | 🟢 | Moyen | gabarit |

Ordre de tri : sévérité × valeur business de la page (dégât des eaux, peinture, plâtrerie, syndics en premier), puis effort croissant.

---

## 5. Ce que dit la SERP (contrôle du 03/09, non personnalisé, hors pack local)

Deux requêtes de contrôle via Firecrawl (localisation Besançon) : « peintre Besançon » et « plaquiste Besançon ». rushiti-renovation.fr n'apparaît dans aucun des 10 premiers résultats organiques ; les annuaires dominent (Travaux.com, AlloVoisins, PagesJaunes, Obat, RDV Artisans, Mappy), suivis de concurrents directs à site propre : Franche Comté Peinture, Petetin Peinture, Nuances Déco, Fort Rénovation, Locatelli Wilfrid. Ce relevé ne remplace pas la Search Console (`[DONNÉE MANQUANTE]`) et ne dit rien du pack local, mais il indique deux leviers : présence propre et cohérente sur ces annuaires (citations NAP), et backlinks locaux (fournisseurs, CMA du Doubs, presse locale) → `rushiti-backlinks`, `rushiti-ecart-concurrentiel`.

---

## 6. Données à fournir pour la suite

| Donnée | Pour quel point | Où la prendre |
|---|---|---|
| Export Search Console requête × page, 16 semaines | 14, 15 | Performances → Exporter |
| Rapport Indexation des pages par motif | 14 | Indexation → Pages |
| PageSpeed Insights mobile sur 3 URL | 8, 9, 11 | pagespeed.web.dev |
| Contenu du conteneur GTM-KPM3GQB6 | 2, 21 | tagmanager.google.com |
| Notes individuelles des 3 avis affichés | 3 | Interface Google Business → Avis |
| Coordonnées GPS du 18 rue du Professeur Haag | 4 | Fiche Google → « Partager » |
| Accord d'Isuf et Yll pour leurs portraits | 12 | — |

## 7. Suivi

- Baseline datée avant tout changement : `rushiti-regression-seo`.
- Chaque modification de masse (grille locale, étoiles, CTA) : fiche d'expérience avec groupe témoin, fenêtre 6 semaines : `rushiti-journal-experiences`.
- Décisions prises sur ce rapport : une ligne par décision dans `docs/seo/decisions/2026-09.md` : `rushiti-journal-decisions`.
- Contrôle après déploiement : `rushiti-lundi-matin` (statuts HTTP des 755 URL, liens cassés) et `rushiti-jsonld-validator` sur les 5 gabarits.
- Prochain audit complet : mars 2027, ou après toute refonte de gabarit.

---

*Contrôle après purge (04/09) : cache Cloudflare purgé (`purge_everything`, zone rushiti-renovation.fr) puis relecture en direct de l'accueil, À propos, Contact, syndic, un article de blog, `platrerie-deluz`, le sitemap et les mentions légales : conformes aux paquets 9 à 12 (geo BAN, `legalName`, bandeau GA4, « relevé le 22/08/2026 », `Mis à jour le`, lastmod). La feuille `s971fb819.css?v=10` servie contient bien le bloc `/*p12*/` (l'absence constatée le 03/09 venait d'une copie edge antérieure à la purge). Un seul écart : les piliers (`/peinture-interieure-besancon`…) affichent encore trois `div.stars` par avis, injectés par le Worker (`AVIS_BLOCK`) et non par les sources → correctif PR [#42](https://github.com/eurotregu/rushiti-renovation/pull/42) du dépôt de production (brouillon ; déploiement par l'API Workers après validation, version `2026-09-04-avis-sans-etoiles`).*

*Suivi (nuit) : constats 2 (hébergeur, GTM), 4 (geo), 11, 16, 17, 18, 20, 21 appliqués dans le paquet 12 (PR de production) ; 5 → courrier `annuaires/` ; 25 → dossier `charte/` ; 19 caduc ; 26 aligné dans ce dépôt.*

*Suivi (soir) : constats 4, 8, 10, 12 appliqués dans la PR [#40](https://github.com/eurotregu/rushiti-renovation/pull/40) (fusionnée) ; constat 13 → kit `etudes-de-cas/` (matière à fournir par Isuf) ; constat 14 rectifié → `grille-locale/README.md`.*

*Suivi : constats 1, 2, 3, 6, 7 appliqués le 03/09 dans la PR [#39](https://github.com/eurotregu/rushiti-renovation/pull/39) du dépôt de production (fusionnée) ; constats 4, 8, 10, 12 appliqués dans la PR [#40](https://github.com/eurotregu/rushiti-renovation/pull/40) (brouillon) ; constat 9 retiré (faux positif). Découverte en passant : 150 pages portaient `legalName: "RUSHITI Rénovation"`, corrigé dans la PR #40.*

*Rapport du 03/09/2026. Lecture seule : rien n'a été modifié en production, rien n'est déployé sans validation d'Isuf. Sources : pages servies par rushiti-renovation.fr le 03/09/2026 (Firecrawl, rendu navigateur), capture mobile 390 px, `docs/seo/` de ce dépôt (audits des 13/08, 22/08, 31/08 et 02/09). Aucun chiffre estimé : les mesures manquantes sont marquées comme telles.*
