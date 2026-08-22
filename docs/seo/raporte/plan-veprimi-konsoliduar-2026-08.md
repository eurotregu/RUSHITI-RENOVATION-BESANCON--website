# Plan d'action consolidé — rushiti-renovation.fr — 22/08/2026

> Produit par `rushiti-priorisateur-seo` à la demande d'Isuf (« que faut-il
> appliquer en priorité SEO sur le site ? »). Lecture seule : ce plan ordonne
> et route, il n'exécute rien. Chaque entrée cite sa source ; aucun problème
> non constaté n'y figure. Barème : impact = valeur de page × gravité ;
> effort = gestes de pose réels (un redéploiement Cloudflare = un train qui
> embarque tout ce qui est prêt).

## Synthèse

**6 sources** ingérées : rapport KPI #1 (21/08) · opportunités GSC mode 3
(20/08) · plan éditorial automne (21/08) · corrections de l'audit du 13/08 ·
paquets `korrigjime-prodhim` (état live du 21-22/08) · état des PR du dépôt de
production au 22/08. **~24 problèmes bruts → 14 entrées** après déduplication
et retrait de ce qui est **déjà réalisé** (dé-duplication des titles sur 40
pages, consolidation de la grille 644 → 301 avec 63 pages épargnées, maillage
des 3 pages éclipsées PR #19, création du silo « rénovation de pièce » PR #15,
fusion façade PR #14). Répartition : **V1 : 3 · V2 : 4 + 1 décision · V3 : 5 ·
Écartées : 4.**

Le fil conducteur des données : **79 % des clics viennent de l'accueil** ; les
piliers restent en pages 2-5 ; le plus gros gisement mesuré est le cluster
« entreprise de peinture à besançon » (1 343 impressions, position 3,5, 0 clic)
et le cluster moisissure (≈ 620 impressions, 2 clics). Tout ce qui suit sert
soit à convertir cette visibilité, soit à sortir les piliers de l'ombre —
et d'abord à **pouvoir mesurer** (Lead `/merci`, attribution par page, GA4).

## Doublons fusionnés & arbitrages

- **Entrée 1** = PR #10 (style + consentement + Lead `/merci`) + PR #20 (champ
  `page`, formulaire prix-travaux, mentions RGPD, validité HTML) : deux PR
  complémentaires, **un seul train de déploiement**. L'événement Lead n'existe
  que dans #10 (retiré de #20 pour éviter le double comptage).
- **Entrée 2** = opportunité GSC n°1 (cluster moisissure) + ligne 1 du plan
  éditorial : même chantier ; le cœur (H2 VMC, bloc conversion, maillage) est
  **déjà en production**, seul le paquet complémentaire A-B-C-D reste à valider.
- **Entrée 8** = KPI #1 action 3 + plan éditorial ligne 2 (pilier dégât des
  eaux) : une seule entrée, fenêtre octobre.
- **Créations salle de bains / entreprise-rénovation / cuisine** (KPI #1
  actions 1 et 4, porte PORTA passée) : **déjà réalisées** par la PR #15
  mergée le 21/08 — sorties du plan, à renforcer plus tard seulement.
- **Arbitrage chaux / boiseries** : demande observée (41 + 58 impressions,
  positions 5-6) mais **prestations non offertes** (décision Isuf du 21/08 au
  soir, REFUZOHET au registre) — écartées, la demande reste sciemment non servie.

## 🟢 Vague 1 — Quick wins (cette semaine)

| # | Problème (consolidé) | Page(s) | Sources | Impact | Effort | Exécutant / geste |
|---|---|---|---|---|---|---|
| 1 | **Fusionner PR #10 puis PR #20** : formulaires stylés + case consentement + événement `Lead` sur `/merci` (aujourd'hui **aucun envoi de formulaire n'est compté**) + attribution par page + formulaire manquant sur prix-travaux + mentions légales RGPD (§7 contradictoire, sous-traitant non déclaré) | 30 pages pilier + `/merci` + mentions | PR #10 · PR #20 · session 22/08 | **Fort** (conversion + mesure + conformité, 30 pages commerciales) | **Faible** (tout est rédigé et vérifié — 2 merges, 1 déploiement) | **Isuf : 2 clics de merge** ; le déploiement Cloudflare suit |
| 2 | **Valider le paquet moisissure A-B-C-D** (FAQ, photos avant/après RGPD, pied d'article) — le cluster est la 2ᵉ visibilité du site (≈ 620 impr., 2 clics) et le cœur de l'enrichissement est déjà live | `/blog/moisissure-plafond-salle-de-bain-besancon` | Opport. GSC n°1 · plan édito L1 · `docs/seo/contenus/` | Moyen-fort | **Faible** (déjà rédigé, en validation) | **Isuf : lire et valider** → pose au prochain train |
| 3 | **Anomalie « rushiti-renovation.fr » en position 23** quand on tape le domaine (49 impr., 0 clic) — contrôle canonical / variante www | site entier | Opport. GSC (signalements) · constat du 19/08 | Fort (marque) | Faible (contrôle) | `rushiti-indexation` (vérification, correction si constat) |

## 🟠 Vague 2 — Prochain train + hors-site (2-3 semaines)

| # | Problème | Page(s) | Sources | Impact | Effort | Exécutant |
|---|---|---|---|---|---|---|
| 4 | **Maillage entrant vers `/platrerie-besancon`** (pos. 9,1 — à une porte de la page 1) **et `/ratissage-enduit-besancon`** (pos. 10,9) : aucun pilier voisin ne les pousse | 2 piliers + pages sources | Opport. GSC n°3 et n°7 | Fort | Moyen (2 liens contextuels chacun, à rédiger) | `rushiti-maillage-interne` → train suivant |
| 5 | **Fiche Google Business + inventaire NAP** : le pack local écrase le CTR organique du cluster « entreprise de peinture » (≈ 150 impr. top 3-8, 0 clic) ; fiches annuaires jamais inventoriées | hors-site | Opport. GSC bloc 2 · audit 13/08 P2-B | Fort | Moyen (hors-site, aucun déploiement) | `rushiti-fiche-google-business` + `rushiti-seo-local` |
| 6 | **GA4 absent** : seul le Pixel Meta mesure ; aucun entonnoir téléphone / formulaire / pages | site entier | Audit 13/08 P1-B | Moyen (levier de mesure) | Moyen (session dédiée, Consent Mode v2 derrière la bannière existante) | `rushiti-ga4-gtm` |
| 7 | **Core Web Vitals jamais mesurés** (accueil, DDE, une page locale, mobile) | site entier | Audit 13/08 (données manquantes) | Moyen | Faible-moyen | `rushiti-audit-technique` (PageSpeed) |
| ⚖️ | **Décision domaine principal (P0-A)** : rushiti.fr, rushiti-peinture.fr et le site Localo dispersent l'autorité ; recommandation de l'audit : tout en 301 vers rushiti-renovation.fr | multi-domaines | Audit 13/08 P0-A | Fort | **Décision de 10 minutes** + sitemap de rushiti.fr à fournir | **Isuf tranche** → puis `rushiti-audit-seo` instruit les 301 |

## 🔵 Vague 3 — Chantiers de fond (calendrier automne, déjà cadencé)

| # | Chantier | Fenêtre | Sources | Exécutant |
|---|---|---|---|---|
| 8 | **Enrichir le pilier `/degat-des-eaux-besancon`** — silo le plus rentable, quasi invisible (33 impr./12 m, pos. 16) : assèchement, déroulé assurance IRSI, maillage depuis les 3 satellites | Octobre (6-8 sem. avant la haute saison) | KPI #1 act. 3 · plan édito L2 | `rushiti-brief-seo` → `rushiti-architecte-seo` |
| 9 | **Article « Mur froid et condensation »** → `/isolation-interieure-besancon` (0 impression en 12 mois — la page a besoin d'un satellite qui pousse) | Octobre | Plan édito L3 · registre 20/08 | `rushiti-brief-seo` puis rédaction |
| 10 | **Enrichir `/isolation-besancon`** : combles + condensation (184 impr., pos. 28,3, 0 clic) | Octobre-novembre | Plan édito L4 | `rushiti-architecte-seo` |
| 11 | **Article « Prix du placo au m² »** (fourchettes À VALIDER par Isuf) | Rédaction nov. → publication début déc. | Plan édito L5 · registre | `rushiti-architecte-seo` (protocole PRIX) |
| 12 | **Page crépi dédiée** — 191 impressions, la plus grosse demande non servie ; la section crépi est posée sur peinture-extérieure : **décision au re-export GSC du ~1ᵉʳ octobre** (si « crepissage besançon » ne remonte pas vers le top 10) | Conditionnelle, octobre | Opport. GSC n°4 | `rushiti-brief-seo` le moment venu |

## ⚪ Écarté (assumé)

| Problème | Raison |
|---|---|
| Titles longue traîne WordPress, `/organic-ehpad`, trailing slash (audit 13/08 P1-A, P1-C, P2-A) | Obsolètes : le site a été refondu en statique depuis l'audit ; les URLs héritées répondent déjà en 301 (vérifié le 20/08) |
| Pages enduit à la chaux / rénovation boiseries (demande observée 41 + 58 impr.) | Prestations non offertes — arbitrage Isuf du 21/08 (REFUZOHET au registre) |
| Article « Peut-on repeindre en hiver ? » | Preuve de demande absente (0 requête dans les 779 de GSC) — parking jusqu'à validation volume |
| Renfort de `/renovation-appartement-besancon` (2 impr.) | Trop tôt : page toute neuve (PR #15) — laisser Google la découvrir, re-juger au rapport #2 |

## Mesure & prochain point

1. **Dès la fusion du train V1** : re-contrôle `rushiti-visibilite-ia` post-déploiement (JSON-LD, extractibilité) + un envoi de test du formulaire pour voir l'e-mail, la page `/merci` et l'événement `Lead` (consentement accepté).
2. **~1ᵉʳ octobre** : re-export GSC **croisé requête × page**, même périmètre → `rushiti-regression-seo` / rapport KPI #2 : effet des titles CTR, du maillage PR #19, de la dé-duplication papier peint ; tranche la décision crépi (entrée 12) et l'anomalie domaine (entrée 3 si non résolue).
3. **Prochaine consolidation** : début octobre, après le rapport #2 — elle recompose les vagues d'automne avec les premières données post-corrections.
