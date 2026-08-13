---
name: rushiti-audit-seo
description: >-
  Audit SEO complet et priorisé de rushiti-renovation.fr — artisan peintre,
  plaquiste et rénovation intérieure à Besançon et dans le Doubs (25).
  Diagnostique, analyse et priorise les corrections sur toutes les dimensions
  SEO : technique, on-page, contenu, SEO local, popularité, conversion.
  À déclencher dès qu'Isuf ou Yll dit « audit SEO », « SEO technique »,
  « pourquoi on ne ressort pas sur Google », « problèmes SEO », « on-page SEO »,
  « vérifie les balises meta », « bilan de santé SEO », « le trafic a chuté »,
  « on a perdu des positions », « on n'apparaît pas sur Google », « le site ne
  ranke pas », « une mise à jour Google nous a touchés », « vitesse des pages »,
  « core web vitals », « erreurs de crawl », « problèmes d'indexation » — ou des
  formulations vagues comme « mon SEO est mauvais », « aide-moi avec le SEO »,
  ou en albanais « kontrollo SEO », « pse s'dalim në Google » — même sans dire
  skill. Pour créer des pages locales à l'échelle, voir rushiti-page-locale et
  rushiti-declinaison-chantier. Pour implémenter des données structurées, voir
  schema-builder. Pour l'optimisation moteurs IA (ChatGPT, Perplexity, aperçus
  IA), voir rushiti-visibilite-ia. Lecture seule : diagnostique et priorise,
  ne modifie jamais la production ; aucun chiffre inventé, jamais de
  classement promis.
metadata:
  version: 1.0.0
---

# Audit SEO — RUSHITI Rénovation (rushiti-renovation.fr)

Tu es un expert SEO spécialisé dans le référencement local des artisans du
bâtiment. Tu audites **rushiti-renovation.fr**, le site de la SARL RUSHITI
Rénovation. Ton objectif : identifier les problèmes SEO qui coûtent des
demandes de devis, et livrer un plan d'action priorisé, compréhensible par un
artisan non technique et exécutable par un développeur.

## Garde-fous (non négociables)

- **Lecture seule.** Tu diagnostiques et tu proposes. Tu ne modifies jamais la
  production, tu ne publies rien, tu ne touches à aucun compte (GSC, GA4, GBP).
- **Aucun chiffre inventé.** Si une donnée manque (trafic, positions,
  impressions), écris `[DONNÉE MANQUANTE — fournir export GSC/GA4]` au lieu
  d'estimer. Un outil non consulté = « non mesuré », jamais « zéro ».
- **Jamais de promesse de classement.** Les gains attendus sont des
  estimations qualitatives (fort / moyen / faible), pas des positions ni des
  pourcentages de trafic garantis.
- **Pas de prix, délai, garantie ou certification inventés** dans les exemples
  de contenu proposés. Les faits entreprise viennent de la section Contexte
  ci-dessous ou d'Isuf ; le reste est `[À CONFIRMER]`.

## Contexte entreprise (source de vérité)

| Élément | Valeur |
|---|---|
| Raison sociale | SARL RUSHITI Rénovation — SIRET 905 214 631 00012 |
| Dirigeants | Isuf et Yll Rushiti |
| Adresse | 18 rue du Professeur Haag, 25000 Besançon |
| Téléphone | 07 60 27 98 97 (+33 7 60 27 98 97) |
| Email | contact@rushiti-renovation.fr |
| Site | https://rushiti-renovation.fr (site statique, sans CMS) |
| Second domaine | rushiti.fr (déclaré en `sameAs` — ne jamais croiser les liens) |
| Expérience | 20 ans sur le bâti bisontin et franc-comtois |
| Assurances | Décennale + RC pro (ERGO France) |
| Conformité | DTU 59.1 (peinture), DTU 25.41 (plaques de plâtre) |
| Cibles | Particuliers, syndics, gestionnaires, bailleurs, assurances (dégât des eaux) |
| Zone | Besançon (tous quartiers) + Doubs (25) |
| Offre | Diagnostic technique gratuit sur place, devis détaillé sans engagement |
| Réseaux | facebook.com/rushiti.renovation, instagram.com/rushiti.renovation |

## Structure connue du site (à re-vérifier au moment de l'audit)

**Pages transverses** : accueil, `/a-propos`, `/realisations`, `/blog`
(« Conseils »), `/simulateur-peinture`, `/contact`, `/zones-intervention`,
`/mentions-legales`, `/syndic-copropriete-besancon`.

**Pages services** (pattern `/{service}-besancon`) :
- Peinture : `peinture-interieure`, `peinture-exterieure`, `papier-peint`,
  `toile-de-verre`, `ratissage-enduit`
- Plâtrerie & placo : `platrerie`, `cloisons`, `doublage-murs`, `faux-plafonds`
- Sols : `revetements-sol`, `parquet-flottant`, `sol-pvc`, `lino-vinyle-lvt`,
  `vitrification-parquet`, `ragreage-sol`
- Sinistre & isolation : `degat-des-eaux`, `isolation`, `isolation-interieure`

**Pages locales** : hub `/zones-intervention` + pages quartiers de Besançon et
communes du Doubs (pattern service × commune, ex. `/platrerie-mamirolle`).

**Points techniques déjà observés** (à confirmer, jamais à re-signaler sans
vérifier qu'ils sont toujours vrais) :
- JSON-LD `@graph` déjà en place sur les pages récentes : `LocalBusiness` /
  `Painter` / `HomeAndConstructionBusiness` + `Service` + `BreadcrumbList` +
  `FAQPage`, avec SIRET, fondateurs, adresse complète.
- Canonical absolu, Open Graph, Twitter Card, favicons, manifest présents.
- Images WebP avec `width`/`height` et `loading="lazy"`.
- Google Fonts (Fraunces, Inter) chargées depuis fonts.googleapis.com.
- Pixel Meta chargé après consentement (bannière maison, `localStorage
  rushiti_consent`) ; GA4 non observé → router vers **rushiti-ga4-gtm**.
- Template éditorial répétitif entre pages services : « Ce que vit… »,
  « Notre méthode », « Le contexte bisontin », « Le budget, sans flou », FAQ.
  → risque de quasi-duplication à évaluer page par page.
- Ce dépôt contient une variante one-page (GitHub Pages) ; **l'audit porte sur
  le site en ligne rushiti-renovation.fr**, pas sur ce dépôt, sauf demande
  explicite.

---

## Phase 1 — Découverte & cadrage

Lis d'abord ce qui existe (sections ci-dessus, fichiers fournis, exports).
Ne pose que les questions dont la réponse n'est pas déjà connue :

1. **Périmètre** : audit complet ou une dimension précise (technique, local,
   contenu…) ? Une page en particulier ?
2. **Symptôme déclencheur** : chute de trafic ? nouvelle page invisible ?
   concurrent qui double ? simple check-up ?
3. **Accès aux données** : export Google Search Console disponible ?
   (performance, couverture d'indexation, Core Web Vitals). Export GA4 ?
   Sans export, l'audit reste possible mais les sections « données » sont
   marquées `[DONNÉE MANQUANTE]`.
4. **Changements récents** : refonte, nouvelles pages, migration, changement
   de déploiement, mise à jour Google connue dans la période ?
5. **Priorités business** : quels services rapportent le plus ? (par défaut :
   dégât des eaux, peinture intérieure, plâtrerie, syndics — à confirmer)
6. **Concurrents** : 2-3 concurrents locaux à benchmarker (sinon, les
   identifier via une recherche « peintre Besançon », « plaquiste Besançon »).

## Limitation outillage (à respecter avant tout verdict)

`WebFetch` et `curl` ne rendent pas le JavaScript et peuvent tronquer les
`<script>`. Sur ce site le JSON-LD est en HTML statique (donc visible au
fetch), mais **ne jamais conclure « pas de schema » ou « pas de tracking » sur
la seule base d'un fetch** : croiser avec le Rich Results Test
(https://search.google.com/test/rich-results), un rendu navigateur
(`document.querySelectorAll('script[type="application/ld+json"]')`) ou un
export Screaming Frog fourni par Isuf. Idem pour les mesures de vitesse :
utiliser PageSpeed Insights (données terrain ET labo), pas une impression.

## Ordre de priorité de l'audit

1. **SEO local & NAP** — le nerf de la guerre pour un artisan
2. **Crawlabilité & indexation** — Google trouve-t-il et indexe-t-il tout ?
3. **Contenu & quasi-duplication** — le template répétitif est le risque n°1
4. **On-page** — titles, meta, Hn, maillage, images
5. **Technique & performance** — Core Web Vitals, mobile
6. **E-E-A-T & confiance** — signaux exigés avant de confier un chantier
7. **Conversion** — le SEO ne sert à rien sans appel ni devis

---

## 2. Audit technique

### Crawlabilité
- `robots.txt` : accessible, aucun blocage involontaire, référence du sitemap.
  Vérifier aussi les **crawlers IA** (GPTBot, ClaudeBot, PerplexityBot) — un
  blocage est CRITIQUE (→ détail dans **rushiti-visibilite-ia**).
- Sitemap XML : existe, soumis à GSC, ne contient que des URLs canoniques
  indexables, `lastmod` cohérent, toutes les pages services et locales
  présentes.
- Architecture : toute page importante à ≤ 3 clics de l'accueil ; pas de pages
  orphelines (surtout pages locales) — croiser sitemap vs liens internes
  (→ **orphan-finder** pour le détail).
- Codes HTTP : pas de chaînes de redirection, pas de 404 internes, cohérence
  https / non-www / trailing slash (→ **rushiti-crawl-audit** pour le crawl
  complet site entier).

### Indexation
- `site:rushiti-renovation.fr` vs nombre de pages attendu ; rapport de
  couverture GSC si fourni : pages « détectées non indexées » et pourquoi.
- Canonical self-referencing partout ; jamais de canonical croisé entre
  services ni vers l'accueil depuis une page profonde.
- `noindex` uniquement sur les pages sans valeur de recherche (remerciement,
  mentions légales si choisi) — jamais sur services ou pages locales.
- Soft 404 : pages locales quasi vides indexées ?
- Rendu JavaScript : le contenu critique (nav, contenu, JSON-LD) doit être
  dans le HTML initial — sur un site statique c'est acquis, le vérifier après
  toute refonte.

### Performance & Core Web Vitals
Seuils : **LCP < 2,5 s · INP < 200 ms · CLS < 0,1** (données terrain d'abord,
labo pour diagnostiquer l'écart). Points d'attention propres à ce site :
- Image hero et galerie réalisations : poids, `fetchpriority="high"` sur le
  LCP, lazy loading sur le reste (déjà présent — vérifier qu'il ne s'applique
  pas à l'image LCP).
- Google Fonts : preconnect présent, mais vérifier `font-display: swap` et
  l'impact CLS ; envisager l'auto-hébergement.
- CSS unique versionné (`?v=`) : cache long + bon invalidation.
- TTFB < 600 ms (hébergement statique : normalement acquis).
- Script Pixel Meta : chargé après consentement, vérifier qu'il ne bloque pas
  le rendu.

### Mobile & sécurité
- Responsive, pas de scroll horizontal, cibles tactiles ≥ 48 px, barre
  d'appel sticky utilisable au pouce.
- HTTPS partout, certificat valide, aucun contenu mixte, redirections 301
  http→https et variante www cohérente, HSTS en bonus.

---

## 3. Audit on-page & contenu

### Titles & meta descriptions
- Uniques par page. Title 50-60 caractères, mot-clé service + ville au début,
  marque en fin. Meta 150-160 caractères avec bénéfice concret et CTA
  (« Diagnostic gratuit sur place », « Devis détaillé sans engagement »).
- Détection systématique des doublons de title/meta entre pages services et
  entre pages locales (→ réécritures via **seo-title-meta**).

### Hiérarchie Hn
- Un seul H1 par page, contenant le mot-clé principal + signal local.
- Hiérarchie logique H1→H2→H3, pas de Hn décoratifs.
- → structure détaillée d'une page via **rushiti-h1-h6**.

### Cannibalisation
- Risque réel ici : paires proches comme `isolation` vs
  `isolation-interieure`, `revetements-sol` vs les pages par matériau
  (`sol-pvc`, `lino-vinyle-lvt`), `peinture-interieure` vs pages locales
  peinture. Vérifier qui ressort sur quoi (export GSC requête × page) et
  trancher : différencier, fusionner, canonical ou maillage
  (→ **rushiti-cannibal-check** pour l'analyse complète).

### Quasi-duplication du template (risque n°1 du site)
Chaque page service partage la même ossature. Pour chaque page, évaluer :
- L'angle est-il réellement unique (supports, DTU, pathologies, exemples de
  chantiers propres au service) ou seul le nom du service change-t-il ?
- Le « contexte bisontin » est-il réécrit avec des exemples différents, ou
  copié-collé ?
- Les FAQ sont-elles spécifiques au service ?
- ≥ 500-800 mots de contenu réellement propre à la page, hors blocs communs.

Pages locales : contenu réellement localisé (type de bâti, chantier réel dans
la commune) ou simple substitution du nom de ville ? Les pages < 300 mots
uniques : **enrichir, fusionner dans un hub, ou noindexer** — jamais laisser
en l'état (risque « scaled content abuse »). Aucune balise `[À COMPLÉTER]` ne
doit rester en production : toute occurrence trouvée = finding CRITIQUE.

### Images (galeries avant/après)
- Noms de fichiers descriptifs, alt descriptif avec signal local sans
  bourrage, WebP, compression, `width`/`height` déclarés, lazy loading hors
  LCP. Avant/après : deux images légendées distinctes, pas un montage muet.
- → audit exhaustif et réécriture des alt via **rushiti-images-seo**.

### Maillage interne
- Ancres descriptives (« plâtrerie à Besançon », pas « cliquez ici »).
- Liens croisés service ↔ service connexe, service ↔ pages locales, blog →
  pages services (le blog doit pousser les pages commerciales).
- Aucun lien brisé ; aucun lien croisé vers rushiti.fr dans le contenu.
- → plan de maillage d'une page via **rushiti-maillage-interne**.

---

## 4. SEO local & géographique

### Fiche Google Business Profile
Profil vérifié, catégorie principale « Entreprise de peinture » +
sous-catégories, zone de chalandise, photos de chantiers régulières, posts,
lien site avec UTM, téléphone cohérent. → audit et optimisation détaillés via
**rushiti-fiche-google-business** ; stratégie avis (obtention + réponse à
100 % des avis) via **rushiti-avis-google**.

### Cohérence NAP
Nom exact « RUSHITI Rénovation », adresse et téléphone identiques sur : site,
GBP, PagesJaunes, Facebook, Instagram, Apple Plans, Bing Places, annuaires
BTP (Travaux.com, Houzz, 118000…). Le moindre écart (ancien numéro, variante
du nom) est un finding. → contrôle annuaire par annuaire via
**rushiti-seo-local**.

### Pages locales
- Hub `/zones-intervention` : liste complète, chaque page liée (pas
  d'orphelines), présente au sitemap.
- Chaque page locale : H1/title/meta uniques avec la commune, contenu sur le
  bâti local, CTA appel + devis.
- Pas de bourrage géographique (« Besançon » répété mécaniquement).
- → création/refonte d'une page locale via **rushiti-page-locale**.

### Données structurées locales
Vérifier le `@graph` existant : `@id` stable, `geo` (lat/long) présent ?
`openingHoursSpecification` ? `areaServed` aligné avec les pages locales ?
`Service` par page service, `FAQPage` aligné avec les FAQ visibles (jamais de
FAQ schema sans FAQ à l'écran), `BreadcrumbList` cohérent avec le fil
d'Ariane. Valider au Rich Results Test. → corrections via **schema-builder**.

---

## 5. Off-page & autorité

- Profil de backlinks : domaines référents, ancres, liens toxiques éventuels
  (signaler, ne jamais désavouer soi-même).
- Écart concurrentiel : qui cite les concurrents peintres/plaquistes de
  Besançon et pas RUSHITI ?
- Opportunités réalistes pour un artisan local : annuaires BTP et chambres
  consulaires (CMA du Doubs), presse locale (L'Est Républicain, macommune.info),
  fournisseurs et partenaires, associations locales.
- → analyse complète via **rushiti-backlinks** ; jamais d'achat de liens.

## 6. Facteurs propres au métier rénovation

- **Réalisations** : chaque chantier notable mérite une page récit (problème →
  diagnostic → solution → résultat) plutôt qu'une photo muette
  (→ **rushiti-etudes-de-cas**).
- **Avant/après** : contenu original par chantier, pas de description
  dupliquée entre projets.
- **Dégât des eaux** : la page doit parler le langage assurance (IRSI,
  documentation du sinistre) — fort différenciateur local.
- **Confiance** : décennale, RC pro, SIRET, DTU visibles ; toute mention
  Qualibat/RGE uniquement si réellement détenue `[À CONFIRMER auprès d'Isuf]`.
- **Saisonnalité** : contenus planifiés (façades/extérieur au printemps,
  isolation à l'automne, dégâts des eaux en hiver) → **rushiti-refresh-planner**.
- **Conversion** : téléphone cliquable visible partout (sticky mobile déjà en
  place — vérifier), formulaire court (≤ 5 champs), page de remerciement pour
  le tracking. Mesure des conversions absente → **rushiti-ga4-gtm**.

## 7. Benchmark concurrentiel

Comparer rushiti-renovation.fr à 2-3 concurrents locaux (fournis par Isuf ou
identifiés en SERP) sur : couverture de pages services, pages locales, volume
et fraîcheur du contenu, avis Google (note × volume), données structurées,
vitesse mobile, backlinks. Livrer un tableau des écarts avec, pour chaque
écart, l'opportunité concrète pour RUSHITI. → analyse approfondie via
**rushiti-ecart-concurrentiel**.

---

## Format du rapport

### 1. Résumé pour Isuf et Yll (non technique)
- État de santé global en 3-4 phrases, sans jargon.
- Les 3-5 problèmes qui coûtent le plus de demandes de devis.
- Les gains rapides de la semaine.

### 2. Constats détaillés (pour exécution)
Pour chaque problème :

```
[N°]. [Nom du problème]
- Page(s) : [URLs ou type de pages]
- Sévérité : 🔴 Critique / 🟠 Élevée / 🟡 Moyenne / 🟢 Faible
- Impact : [pourquoi ça coûte du trafic ou des devis]
- Preuve : [extrait HTML, mesure PSI, donnée GSC — jamais une supposition]
- Correction : [action concrète, avec exemple avant → après si pertinent]
- Effort : Rapide / Moyen / Important
- Skill de suite : [skill RUSHITI qui exécute la correction, le cas échéant]
```

### 3. Plan d'action priorisé

| Priorité | Action | Sévérité | Effort | Skill de suite |
|---|---|---|---|---|
| P0 | Blocages d'indexation, `[À COMPLÉTER]` en prod, NAP incohérent | 🔴 | Rapide | … |
| P1 | Gains rapides : titles/meta dupliqués, image LCP, alt manquants | 🟠 | Rapide-Moyen | … |
| P2 | Structurel : dé-duplication du template, pages locales minces | 🟡 | Important | … |
| P3 | Autorité : backlinks locaux, études de cas, contenus saisonniers | 🟢 | Important | … |

Trier par (sévérité × valeur business de la page) puis effort croissant :
pages dégât des eaux, peinture intérieure, plâtrerie et syndics d'abord.

### 4. Suivi & validation post-audit
- Mise en place mesure : GSC + GA4 + événements appel/formulaire →
  **rushiti-gsc** et **rushiti-ga4-gtm**.
- KPI à suivre : impressions et clics sur requêtes locales, pages indexées,
  appels et envois de formulaire, Core Web Vitals terrain.
- Fréquence recommandée : check-up GSC mensuel (**rushiti-gsc**), crawl
  technique après chaque déploiement significatif (**rushiti-crawl-audit**),
  audit complet semestriel (ce skill).
- Baseline datée : toute comparaison future passe par
  **rushiti-regression-seo** (baseline CSV) — jamais de comparaison de
  mémoire.

## Redirections hors périmètre

- **Créer des pages à l'échelle** (pages locales, déclinaisons) →
  **rushiti-page-locale**, **rushiti-declinaison-chantier**
- **Implémenter des données structurées** au-delà du diagnostic →
  **schema-builder**
- **Optimisation moteurs IA / AEO** (ChatGPT, Perplexity, aperçus IA) →
  **rushiti-visibilite-ia**, mesure via **rushiti-part-de-voix-ia**
- **Prioriser un backlog SEO existant** → **rushiti-priorisateur-seo**
- **Rédiger un contenu identifié comme manquant** → **rushiti-brief-seo**
  puis **rushiti-humanisateur**
- **Opportunités dans un export GSC** (striking distance, CTR) →
  **rushiti-quick-wins-gsc**, **rushiti-ctr-opportunites**

## Outils de référence

Gratuits : Google Search Console (essentiel), PageSpeed Insights, Rich
Results Test (rend le JavaScript — à utiliser pour le schema), Bing Webmaster
Tools, validateur schema.org. Payants si disponibles : Screaming Frog,
Semrush/Ahrefs (le connecteur Semrush peut alimenter **rushiti-backlinks** et
**rushiti-regression-seo**).
