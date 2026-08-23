# Cadence — les 30 premiers jours, puis le rythme de croisière

> Le playbook générique propose un plan 30 jours qui commence par
> « cartographiez vos mots-clés » et « auditez vos pages ». **Chez RUSHITI ces
> deux étapes sont faites** : le registre existe, la grille a été consolidée,
> l'audit du 13/08 est rendu et déjà routé en 14 entrées priorisées.
>
> Le plan ci-dessous ne réinvente donc rien : il **cale la cadence sur les
> vagues du plan consolidé du 22/08/2026**, et il y ajoute ce que le plan
> consolidé ne couvrait pas encore — l'ouverture de la porte IA, jamais
> mesurée à ce jour.

## Le principe de priorisation

Trois règles, dans cet ordre. Elles expliquent pourquoi le mois ne commence
pas par écrire des pages.

1. **Ce qui débloque la mesure passe avant tout.** Aujourd'hui aucun envoi de
   formulaire n'est compté. Optimiser la conversion sans compter les
   conversions, c'est régler un moteur sans compte-tours.
2. **Ce qui convertit une visibilité existante passe avant ce qui en crée.**
   1 343 impressions en position 3,5 sans un clic valent plus d'attention que
   n'importe quelle page neuve.
3. **Ce qui est déjà rédigé et attend une validation passe avant ce qui est à
   écrire.** L'effort est déjà payé ; il ne manque qu'une décision.

## Semaine 1 — Rendre le site mesurable et débloquer ce qui est prêt

*(Vague 1 du plan consolidé — effort faible, impact fort, tout est déjà
rédigé)*

| Action | Agent / geste | Pourquoi maintenant |
|---|---|---|
| Fusionner PR #10 puis PR #20 : formulaires stylés, case de consentement, événement `Lead` sur `/merci`, attribution par page, formulaire manquant sur prix-travaux, mentions RGPD | **Isuf : 2 merges**, puis déploiement Cloudflare | Sans l'événement `Lead`, **aucun envoi de formulaire n'est compté** sur 30 pages commerciales |
| Valider le paquet moisissure A-B-C-D (FAQ, photos avant/après RGPD, pied d'article) | **Isuf : lire et valider** | 2ᵉ visibilité du site (≈ 620 impressions), le cœur est déjà en production |
| Contrôler l'anomalie de marque : « rushiti-renovation.fr » en position 23 sur son propre domaine | `rushiti-indexation` | 49 impressions, 0 clic, et c'est la requête de marque |
| Trancher le **domaine principal** (P0-A) | **Isuf : décision** | 10 minutes qui débloquent tout le netlinking |

## Semaine 2 — Convertir la visibilité existante

*(Vague 2 du plan consolidé)*

| Action | Agent | Gisement visé |
|---|---|---|
| Deux liens contextuels entrants vers `/platrerie-besancon` (position 9,1) et deux vers `/ratissage-enduit-besancon` (10,9) | `rushiti-maillage-interne` | Deux piliers à une porte de la page 1, que personne ne pousse |
| Fiche Google Business + inventaire NAP par annuaire | `rushiti-fiche-google-business` + `rushiti-seo-local` | Le pack local écrase le CTR organique du cluster « entreprise de peinture » (1 343 impressions, 0 clic) |
| Installer GA4 (Consent Mode v2 derrière la bannière existante) | `rushiti-ga4-gtm` | Aucun entonnoir téléphone / formulaire aujourd'hui |
| Mesurer les Core Web Vitals (accueil, dégât des eaux, une page locale, mobile) | `rushiti-audit-technique` | Jamais relevés |

> **Le travail hors-site de cette semaine ne demande aucun déploiement.** Il
> peut avancer en parallèle du train Cloudflare, ce qui en fait le meilleur
> usage d'une semaine où l'on attend des merges.

## Semaine 3 — Ouvrir la porte IA (jamais mesurée)

C'est l'ajout du moteur au plan consolidé. L'outillage est en place depuis
août ; **aucune mesure n'a été prise**. Dans cet ordre, sans le raccourcir :

1. `rushiti-visibilite-ia` — robots.txt, crawlers IA (GPTBot, ClaudeBot,
   Google-Extended, PerplexityBot…), validité du JSON-LD, extractibilité,
   E-E-A-T. **Mesurer la citation d'un site que les crawlers ne lisent pas
   ferait perdre la mesure et le temps.**
2. `rushiti-part-de-voix-ia` — première mesure sur le panel figé de
   14 requêtes. Elle n'aura pas de comparatif : elle **est** la référence.
3. `rushiti-citation-ia` — quelles sources sont citées à notre place, par
   famille, et par quelle porte y entrer. Sortie attendue : huit fiches
   d'annuaire exactes valent mieux que douze articles de blog.

> Pour un artisan local, le corpus que les moteurs citent est dominé par des
> sources tierces déjà en place. Y être complet et cohérent coûte quelques
> heures et pèse plus lourd, à court terme, qu'une campagne éditoriale.

## Semaine 4 — Le silo le plus rentable

*(Vague 3 du plan consolidé — fenêtre octobre, 6-8 semaines avant la haute
saison)*

| Action | Agent | Motif |
|---|---|---|
| Enrichir le pilier `/degat-des-eaux-besancon` : assèchement, déroulé assurance IRSI, maillage depuis les 3 satellites | `rushiti-brief-seo` → `rushiti-architecte-seo` | 33 impressions / 12 mois en position 16, sur le silo qui rapporte le plus au métier |
| Article « Mur froid et condensation » poussant `/isolation-interieure-besancon` | `rushiti-brief-seo` puis rédaction | La page pilier fait **0 impression en 12 mois** : il lui manque un satellite |
| Poser la baseline de mesure de tout ce qui a bougé ce mois-ci | `rushiti-regression-seo` | Sans donnée de départ datée, rien de ce mois ne sera jugeable |

## Le rituel du lundi (30 minutes)

À filtrer par l'état réel — une routine récitée fait perdre l'heure qu'elle
prétend économiser.

1. **Qu'est-ce qui a bougé ?** `rushiti-gsc` — clics, impressions, positions
   des piliers. Comparer au lundi précédent, pas à la baseline de mai.
2. **Qu'est-ce qui a glissé ?** Toute page qui perd trois positions ou plus
   part en `rushiti-refresh-planner` ou `rushiti-audit-seo`.
3. **Qu'est-ce qui est à une porte de la page 1 ?** Positions 8 à 12 : ce sont
   les moins chers à gagner, presque toujours par du maillage.
4. **Qu'est-ce qui attend une validation d'Isuf ?** Relire la liste — un
   livrable en attente est un effort déjà payé qui ne rapporte rien.
5. **Publier la prochaine cible** du plan éditorial, si le train est prêt.

**Ne fait pas partie du lundi** : re-mesurer la part de voix IA. Le corpus des
moteurs de réponse bouge en six à huit semaines. Le mesurer chaque lundi
produit du bruit qu'on prendra pour du signal.

## Le rituel mensuel

| Action | Agent |
|---|---|
| Rapport KPI (clics, impressions, CTR, position, conflits de cannibalisation) | `rushiti-keyword-map` |
| Pages en décrochage à rafraîchir | `rushiti-refresh-planner` |
| Avis Google : relevé de la note et du nombre, sollicitation des chantiers livrés | `rushiti-avis-google` |
| Saisonnalité : ce qui monte dans 6 à 8 semaines | `rushiti-google-trends` |

## Le rituel des 6-8 semaines (porte IA)

| Action | Agent |
|---|---|
| Part de voix sur le panel figé de 14 requêtes | `rushiti-part-de-voix-ia` |
| Relevé du corpus cité + avancement du plan d'entrée | `rushiti-citation-ia` |
| Contrôle post-déploiement (robots.txt, JSON-LD, extractibilité) | `rushiti-visibilite-ia` |

## Le rituel trimestriel

| Action | Agent |
|---|---|
| Pages orphelines et liens cassés | `orphan-finder` + `rushiti-maillage-interne` |
| Profil de liens et écart concurrentiel | `rushiti-backlinks` + `rushiti-ecart-concurrentiel` |
| Cohérence NAP sur tous les annuaires | `rushiti-seo-local` |
| Indexation : anciennes URL WordPress, pages non indexées | `rushiti-indexation` |

## Ce qui ne se fait jamais dans une cadence

- **Regonfler la grille locale.** Elle est passée de 644 à 301 pages
  volontairement. Toute reprise passe par `rushiti-keyword-map`.
- **Publier pour tenir un rythme.** Une page de plus qui cannibalise coûte
  plus qu'une semaine sans publication.
- **Mesurer une porte pour se rassurer.** Si la mesure ne change aucune
  décision cette semaine-là, elle attend la bonne fenêtre.
