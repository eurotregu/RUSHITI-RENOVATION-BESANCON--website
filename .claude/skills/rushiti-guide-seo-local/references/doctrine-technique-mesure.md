# Doctrine 3 — Technique locale, mobile et mesure

Cette doctrine couvre le socle technique du SEO local (données structurées,
fiche Google Business, cohérence NAP), les exigences mobile/performance, et
la mesure (KPIs, événements de conversion). Elle part de l'état **réel** du
site au 22/08/2026 — un site statique déployé sur Cloudflare Pages — et
route chaque exécution vers l'agent spécialiste.

## A. Données structurées (JSON-LD)

### Le choix maison : `HousePainter`

Le site utilise déjà le type `HousePainter` (sous-type de `LocalBusiness`),
plus précis que `LocalBusiness` générique pour un peintre-plaquiste — on le
conserve partout pour la cohérence. Le bloc organisation est **sitewide** ;
les pages y ajoutent selon leur type : `Service`, `BreadcrumbList`,
`FAQPage`, `Article` (blog). La génération page par page est le métier de
`schema-builder` ; la validation JSON-LD en conditions réelles (dont le
JavaScript parasite) celui de `rushiti-visibilite-ia`.

### Bloc organisation canonique (corrigé)

Le bloc en production omet `streetAddress` — une adresse complète renforce
le signal NAP. Version canonique de référence :

```json
{
  "@context": "https://schema.org",
  "@type": "HousePainter",
  "name": "RUSHITI Rénovation",
  "legalName": "Rushiti",
  "description": "Entreprise de rénovation, peinture, plâtrerie et aménagement intérieur à Besançon et dans le Doubs. Diagnostic gratuit sur site.",
  "url": "https://rushiti-renovation.fr/",
  "telephone": "+33760279897",
  "email": "contact@rushiti-renovation.fr",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "18 rue du Professeur Haag",
    "addressLocality": "Besançon",
    "postalCode": "25000",
    "addressRegion": "Doubs",
    "addressCountry": "FR"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[À COMPLÉTER — relever sur la fiche Google Business]",
    "longitude": "[À COMPLÉTER — relever sur la fiche Google Business]"
  },
  "areaServed": ["Besançon", "Doubs"],
  "openingHoursSpecification": "[REPRENDRE la fiche Google Business à l'identique — ne jamais saisir des horaires de mémoire]",
  "sameAs": [
    "https://www.facebook.com/rushiti.renovation/",
    "https://www.instagram.com/rushiti.renovation/"
  ],
  "priceRange": "Devis gratuit"
}
```

Règles non négociables, avec leur pourquoi :

- `name` = **RUSHITI Rénovation** (nom commercial), `legalName` = Rushiti.
  « SARL RUSHITI Rénovation » n'existe pas juridiquement — le nom commercial
  n'est pas la raison sociale.
- `streetAddress` = **« 18 rue du Professeur Haag »** — « rue » en
  minuscules, avec « du », à l'identique de la fiche Google Business (règle
  NAP de `rushiti-defaults.md`). C'est la graphie que Google recoupe.
- Horaires et coordonnées géo : **relevés**, jamais saisis de mémoire. Deux
  jeux d'horaires différents entre le site et la fiche affaiblissent le
  signal local (et un brouillon externe a déjà inventé des horaires avec
  ouverture le dimanche — c'est exactement l'erreur à intercepter).
- **Pas d'`aggregateRating` alimenté par les avis Google.** Les consignes
  Google interdisent de baliser des notes collectées sur une plateforme
  tierce (avis dits « self-serving ») : le balisage serait ignoré au mieux,
  pénalisé au pire. La note Google se met en avant **en texte, datée**, pas
  en données structurées — sauf le jour où le site collecte et affiche ses
  propres avis.
- `areaServed` reste aligné sur les zones déclarées à la fiche Google.
- Validation systématique : Rich Results Test + validator.schema.org avant
  déploiement.

## B. Fiche Google Business et cohérence NAP

Pour « peintre besançon » et le cluster « entreprise de peinture », le pack
local (la carte + 3 fiches) s'affiche **au-dessus** des résultats
organiques : la fiche Google est donc un actif aussi important que les
pages. Constat GSC : le pack écrase le CTR organique du cluster (~150
impressions top 3-8, 0 clic) — la fiche doit capter ce que la page ne peut
pas.

| Chantier | Contenu | Agent |
|---|---|---|
| Description (750 c.), services (300 c./service), Google Posts géo-ciblés | Rédaction optimisée, ancrée quartiers/communes | `rushiti-fiche-google-business` |
| Catégories, horaires, zones desservies | **Relever l'existant** avant de proposer ; catégories candidates alignées sur les 6 silos | `rushiti-fiche-google-business` |
| Réponses aux avis | Une réponse par avis, service + zone mentionnés naturellement | `rushiti-avis-google` |
| Collecte d'avis | Email de fin de chantier avec demande d'avis | `rushiti-courriers-clients` |
| Inventaire NAP multi-annuaires (Google, PagesJaunes, Facebook, Apple Plans, Bing…) | Tableau des écarts, corrections priorisées — jamais fait à ce jour | `rushiti-seo-local` |

La règle NAP tient en une phrase : **partout, reproduire au caractère près
ce qu'affiche la fiche Google Business** — « 18 rue du Professeur Haag,
25000 Besançon », « 07 60 27 98 97 » (affichage) / « +33760279897 »
(JSON-LD et `tel:`). Un annuaire qui porte l'ancien libellé ou une graphie
divergente se corrige, il ne se « tolère » pas.

## C. Mobile et performance

### Le contexte réel

Le site est **statique, servi par Cloudflare Pages** : le TTFB et la mise en
cache sont déjà bons par construction. Les Core Web Vitals n'ont en revanche
**jamais été mesurés** (audit du 13/08) — mesurer vient avant optimiser.

### Cibles (seuils Google, à vérifier sur mobile d'abord)

| Métrique | Seuil « bon » | Outil |
|---|---|---|
| LCP | moins de 2,5 s | PageSpeed Insights (pagespeed.web.dev) |
| INP | moins de 200 ms | PageSpeed Insights |
| CLS | moins de 0,1 | PageSpeed Insights |
| Échantillon à tester | accueil · un pilier (DDE) · une page de grille · /contact | `rushiti-audit-technique` |

### Leviers, par ordre de rendement sur ce site

1. **Images** : WebP/AVIF, dimensions HTML explicites (`width`/`height` —
   c'est ce qui tient le CLS), `loading="lazy"` sous la ligne de flottaison,
   photo héro préchargée si elle est le LCP. Audit → `rushiti-images-seo`.
2. **Polices** : Montserrat + Open Sans passent par Google Fonts —
   `font-display: swap` + `preconnect`, ou auto-hébergement pour supprimer
   le tiers. Jamais plus de 2 familles.
3. **CSS/JS** : le critique inline, le reste différé ; pas de framework pour
   un site statique.
4. **Conversion mobile** : numéro cliquable `tel:+33760279897` partout,
   cibles tactiles ≥ 48 px, CTA collant (appel + devis) sur les pages
   commerciales, formulaires courts (le formulaire « demande rapide » du
   site est la référence).

Ne jamais citer de statistiques de marché inventées (« X % des recherches
locales sont mobiles ») : l'index Google est mobile-first pour tout le
monde, c'est la seule justification nécessaire.

## D. Mesure : KPIs et suivi des conversions

### L'état réel (à ne pas maquiller)

Au 22/08/2026 : **GA4 est absent** — seul le Pixel Meta mesure ; l'événement
`Lead` sur `/merci` et l'attribution par page arrivent avec les PR #10/#20 ;
le site a une bannière de consentement. Conséquence : la première action de
« mesure » n'est pas un dashboard, c'est **pouvoir compter** (plan d'action
consolidé, vague 1).

### Événements de conversion (cible, une fois GA4 posé)

| Événement | Déclencheur | Note |
|---|---|---|
| `generate_lead` | arrivée sur `/merci` après envoi de formulaire | l'attribution par page (champ `page` du formulaire) dit quelle page a produit le lead |
| `phone_click` | clic sur un lien `tel:` | la conversion n° 1 d'un artisan |
| `email_click` | clic sur `mailto:` | secondaire |
| `whatsapp_click` | clic sur le lien WhatsApp | **seulement si le canal existe sur le site** — à vérifier, pas à supposer |

Pas de « valeur de lead » inventée dans les événements (un brouillon externe
proposait 150 € par lead) : la valeur d'un chantier, seul Isuf la connaît —
`[À COMPLÉTER]` ou rien. Installation GA4 + GTM + Consent Mode v2 derrière
la bannière existante : `rushiti-ga4-gtm` (la CNIL impose le consentement
préalable — Consent Mode v2 est le mécanisme, pas une option).

### Le tableau de bord mensuel (qui alimente quoi)

| KPI | Source | Agent |
|---|---|---|
| Impressions / clics / position des clusters pivots (« peintre besançon », « entreprise de peinture à besançon », « plaquiste », pilier DDE) | Export GSC requête × page | `rushiti-gsc`, consolidé au rapport KPI de `rushiti-keyword-map` |
| Régressions de positions (baseline datée, comparaison mensuelle) | Exports successifs | `rushiti-regression-seo` |
| Quick wins CTR (position 3-15, CTR sous la courbe attendue) | Export GSC | `rushiti-ctr-opportunites` |
| Appels, itinéraires, vues de la fiche | Statistiques Google Business | relevé manuel mensuel |
| Nombre d'avis et note (donnée datée) | Fiche Google | relevé manuel |
| Leads par page (`generate_lead` + champ `page`) | GA4 | `rushiti-ga4-gtm` |
| Pages indexées / exclues (dupliquées, soft 404) | GSC Couverture | `rushiti-indexation` |
| CWV (échantillon mobile) | PageSpeed | `rushiti-audit-technique` |

### Deux règles de lecture

- **Fenêtre de 4 à 6 semaines** minimum avant de juger un changement (c'est
  la cadence déjà inscrite au registre pour chaque action « en matje ») ;
  comparer des périodes comparables, saisonnalité comprise — sinon le
  signaler, jamais le maquiller.
- **Jamais de classement promis.** Un KPI est un constat daté et sourcé ;
  un objectif est une direction. « Top 3 garanti » n'existe dans aucune
  sortie RUSHITI.
