# Corrections SEO prêtes à poser — audit du 13/08/2026

Source : audit `rushiti-audit-seo` (rapport du 13/08/2026). Ce document
contient les corrections **prêtes à appliquer** pour chaque constat qui exige
la production ou une décision d'Isuf/Yll. Rien ici n'est déployé : chaque bloc
se copie-colle une fois validé.

Statut des points exécutables directement dans ce dépôt :
- ✅ **Fait** — `noindex` ajouté à la copie GitHub Pages (`index.html`).
  La page syndic du dépôt garde son canonical vers la production, qui suffit.

---

## P0-A · Consolidation des domaines (constat n°1 — 🔴)

**Décision à prendre : un seul domaine principal.**
Recommandation : **rushiti-renovation.fr** (structure la plus complète, blog,
pages locales, données structurées, déjà positionné en SERP).

### Redirections 301 à mettre en place une fois validé

| Domaine source | Cible |
|---|---|
| `rushiti.fr/*` et `www.rushiti.fr/*` | page équivalente sur rushiti-renovation.fr, sinon `https://rushiti-renovation.fr/` |
| `rushiti.fr/platrerie-placo` | `https://rushiti-renovation.fr/platrerie-besancon` |
| `rushiti.fr/notre-entreprise` | `https://rushiti-renovation.fr/a-propos` |
| `rushiti-peinture.fr/*` et `www.rushiti-peinture.fr/*` | `https://rushiti-renovation.fr/peinture-interieure-besancon` (accueil → `/`) |
| `rushiti-renovation-peintre.localo.site` | supprimer le site Localo ou le faire pointer vers rushiti-renovation.fr |

> Le mapping page à page complet de rushiti.fr demande la liste de ses URLs
> (sitemap de rushiti.fr) : `[DONNÉE MANQUANTE — fournir la liste ou l'accès]`.

### Après les redirections
- Mettre à jour l'URL du site sur : fiche Google Business Profile, Facebook,
  Instagram, LinkedIn, et toute fiche annuaire.
- Dans Search Console : déclarer le changement d'adresse pour les propriétés
  rushiti.fr et rushiti-peinture.fr (→ skill **rushiti-gsc**).
- Ne PAS supprimer les anciens domaines : les 301 doivent vivre des années.

---

## P0-B · Page désamiantage (constat n°3 — 🟠)

`[À CONFIRMER auprès d'Isuf : l'entreprise détient-elle une certification
amiante (retrait) ou une formation SS4 (interventions limitées) ?]`

**Cas 1 — aucune certification :** remplacer le positionnement de
`/desamiantage-sol-besancon/` par « après désamiantage » :

- Title proposé : `Rénovation de sol après désamiantage à Besançon | RUSHITI`
- H1 proposé : `Remise en état des sols après désamiantage à Besançon`
- Angle : RUSHITI n'effectue pas le retrait d'amiante (réservé aux entreprises
  certifiées) ; RUSHITI intervient **après** : ragréage, revêtements, finitions.
  Ajouter une phrase claire : « Le retrait d'amiante est réalisé par une
  entreprise certifiée ; nous prenons le relais pour la remise en état. »
- Rediriger 301 l'ancienne URL si le slug change.

**Cas 2 — certification détenue :** l'afficher explicitement sur la page
(numéro, organisme, périmètre SS3/SS4) et dans la section « Confiance &
conformité ».

---

## P1-A · URL `/organic-ehpad-besancon/` (constat n°2 — 🟠)

1. Identifier l'origine du préfixe `organic-` (variante de campagne ?
   générateur ?) et vérifier au crawl s'il existe d'autres URLs du même
   pattern (`organic-*`, `paid-*`…).
2. Publier la page sous l'URL propre : `/ehpad-besancon`.
3. Rediriger 301. Sur Cloudflare Pages, fichier `_redirects` :

```
/organic-ehpad-besancon/ /ehpad-besancon 301
/organic-ehpad-besancon  /ehpad-besancon 301
```

4. Mettre à jour le sitemap et les liens internes.

---

## P1-B · Mesure GA4 (constat n°6 — 🟠)

À installer par **rushiti-ga4-gtm** (le skill dédié) — résumé du besoin :

- Créer la propriété GA4 → ID de mesure `G-XXXXXXXXXX` `[À CRÉER]`.
- Charger GA4 **derrière le même consentement** que le Pixel Meta (la bannière
  existante écrit `localStorage.rushiti_consent`) avec Consent Mode v2.
- Mettre à jour le texte de la bannière : elle ne mentionne aujourd'hui que
  les cookies Meta — ajouter la mesure d'audience.
- Événements clés : `clic_telephone` (liens `tel:`), `envoi_formulaire`
  (page `/contact`), `clic_email` (liens `mailto:`).
- Relier GA4 à Search Console.

---

## P1-C · Titles longue traîne (constat n°4 — 🟡)

Règle de gabarit : **≤ 60 caractères, mot-clé + ville devant, marque UNE
seule fois en fin** (` | RUSHITI Rénovation`, ou ` | RUSHITI` si trop long).

Réécritures pour les pages observées en SERP :

| Page | Title actuel affiché (tronqué en SERP) | Title proposé |
|---|---|---|
| `/peinture-plafond-batiment-besancon/` | Plafond bâtiment à Besançon — RUSHITI Rénovation - RUSHITI … | `Peinture plafond de bâtiment à Besançon \| RUSHITI` |
| `/enduit-chaux-besancon/` | Enduit à la chaux à Besançon — RUSHITI Rénovation - RUSHITI … | `Enduit à la chaux à Besançon \| RUSHITI Rénovation` |
| `/organic-ehpad-besancon/` | EHPAD & maison de retraite à Besançon - RUSHITI Rénovation | (garder, corriger l'URL — cf. P1-A) |
| `/desamiantage-sol-besancon/` | Désamiantage sol & dalle à Besançon — RUSHITI Rénovation … | selon décision P0-B |

Vérifier ensuite **toutes** les pages longue traîne du même gabarit (le
doublon de marque vient probablement du template) : → **seo-title-meta**
sur la liste complète des URLs.

---

## P2-A · Trailing slash (constat n°5 — 🟡)

Format canonique constaté : **sans slash final**. Règle Cloudflare Pages
(`_redirects`, à adapter si autre hébergeur) — Cloudflare Pages normalise
déjà la plupart des cas ; vérifier ces URLs qui coexistent dans Google :

```
/peinture-plafond-batiment-besancon/ /peinture-plafond-batiment-besancon 301
/enduit-chaux-besancon/              /enduit-chaux-besancon              301
/desamiantage-sol-besancon/          /desamiantage-sol-besancon          301
```

Puis : sitemap uniquement en version sans slash, et crawl de contrôle
(→ **rushiti-crawl-audit**) pour trouver les autres URLs à double format.

---

## P2-B · Inventaire NAP (constat n°9 — 🟡)

NAP de référence (unique, à copier partout à l'identique) :
**RUSHITI Rénovation · 18 rue du Professeur Haag, 25000 Besançon ·
07 60 27 98 97 · https://rushiti-renovation.fr**

| Fiche | Statut | Action |
|---|---|---|
| Google Business Profile | `[À VÉRIFIER]` | URL → domaine principal, catégorie, horaires |
| Facebook | existe | vérifier NAP + URL |
| Instagram | existe | vérifier lien bio |
| LinkedIn | existe | vérifier NAP + URL |
| PagesJaunes | non trouvée en recherche | créer/rechercher la fiche |
| Apple Plans (Business Connect) | `[À VÉRIFIER]` | créer si absente |
| Bing Places | `[À VÉRIFIER]` | créer si absente |
| Site Localo | existe | cf. P0-A : supprimer ou rediriger |
| Annuaires BTP (Travaux.com, Houzz…) | `[À VÉRIFIER]` | inventaire via **rushiti-seo-local** |

---

## Données encore manquantes pour finir l'audit

1. **Export GSC** (performance 12 mois + couverture d'indexation) →
   débloquer les constats n°7 (template) et la cannibalisation.
2. **Core Web Vitals** : mesurer https://pagespeed.web.dev sur `/`,
   `/degat-des-eaux-besancon`, une page locale (mobile) et coller les
   résultats dans une session avec le skill **rushiti-audit-technique**.
3. **Liste des URLs de rushiti.fr** (sitemap) → finir le mapping 301 du P0-A.

## Ordre d'exécution recommandé (semaine 1)

1. ✅ noindex copie GitHub Pages (fait dans ce dépôt)
2. Décision domaine principal (P0-A) — 10 minutes de discussion, débloque tout
3. Confirmation certification amiante (P0-B) — une réponse oui/non
4. 301 `organic-ehpad` (P1-A) — 15 minutes
5. Titles longue traîne (P1-C) — 1-2 h selon le nombre de pages
6. Lancement installation GA4 (P1-B) — session dédiée **rushiti-ga4-gtm**
