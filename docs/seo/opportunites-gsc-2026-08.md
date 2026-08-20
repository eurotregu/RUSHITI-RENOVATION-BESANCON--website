# Opportunités GSC — rushiti-renovation.fr — 10/06 → 18/08/2026 — mode 3

> Analyse de l'export xlsx Search Console fourni le 20/08/2026 (feuilles
> Requêtes et Pages, non croisées). **Lecture seule** : ce rapport propose,
> rien n'est appliqué sans validation d'Isuf. Les associations requête → page
> sont des hypothèses tant que l'export croisé n'existe pas — elles sont
> marquées comme telles.

## Synthèse

L'export est étiqueté « 12 derniers mois » mais **les données ne commencent que
le 10/06/2026** : 70 jours utiles, le site est jeune sur ce domaine. Périmètre :
257 requêtes (2 817 impressions), 175 pages (7 100 impressions), seuil
d'impressions toléré à 100 (période courte, site jeune — signalé). Vingt
requêtes hors marque et hors zone sont en striking distance ; le levier CTR
classique est **marginal** ici (peu de pages dépassent le plancher statistique) ;
la vraie anomalie CTR est ailleurs : **~150 impressions en top 3-8 sur le
cluster « entreprise de peinture besançon » avec zéro clic**.

**Trois faits changent les décisions déjà en cours :**

1. **La grille locale est confirmée surdimensionnée par les données** : sur les
   1 368 pages service × zone, **63 seulement ont eu au moins une impression**
   en 70 jours, pour un cumul de **310 impressions (4 % du total du site)**.
   1 305 pages n'ont jamais été montrées. La consolidation en trois paliers
   proposée dans l'audit des mots-clés est validée — et les 63 pages qui
   impriment sont listées ci-dessous pour être **épargnées**.
2. **Le doublon façade est tranché par les données** : `/ravalement-facade-besancon`
   n'a **aucune impression** ; `/peinture-exterieure-besancon` en a 72
   (position 16,4) et porte déjà en production le title « Ravalement, crépi &
   peinture de façade ». Verdict : fusion 301 du premier vers le second.
   Et la vraie demande du secteur est **« crépi » : 191 impressions**
   (« crepissage besançon » 113, « crépis besançon » 78, positions 20-23) —
   la section crépi ajoutée en production est exactement au bon endroit.
3. **Le dépôt git est en retard sur la production** pour les pages piliers
   (constat détaillé dans le PR #11) : les snippets live des piliers sont déjà
   réécrits (« devis sous 48 h », « 34 avis 4,7/5 »), **postérieurs à la
   période mesurée**. Les zéro-clics du point CTR ci-dessous reflètent les
   ANCIENS snippets : la correction est déjà posée, il reste à la **mesurer**
   (re-export dans 4-6 semaines).

## Synthèse croisée priorisée

| # | Page (hypothèse si non croisé) | Requête principale | Position | Impressions | Angle | Levier(s) | Priorité |
|---|---|---|---|---|---|---|---|
| 1 | `/blog/moisissure-plafond-salle-de-bain-besancon` | moisissure plafond salle de bain (+7 variantes) | 11,2–17,4 | **≈ 600** (requêtes) / 1 333 + 469 ancres (page) | **Les deux** | 1. Snippet (CTR 0,3 % vs ~1,1 % attendu) · 2. Conversion + maillage vers dégât des eaux | Haute |
| 2 | `/` (accueil) | peintre besancon | 13,2 | 110 | Striking distance | Maillage + snippet déjà posé en prod → mesurer | Haute |
| 3 | `/platrerie-besancon` | plâtrerie à besançon | 9,1 | 73 + 31 + 23 | Striking distance | Maillage entrant (quasi nul depuis la grille) | Haute |
| 4 | `/peinture-exterieure-besancon` | crepissage / crépis besançon | 20,4–23,3 | **191** | Striking distance (limite) | Section crépi déjà posée en prod → mesurer ; si stagne : page dédiée | Haute |
| 5 | cluster « entreprise de peinture besançon » | entreprise de peinture à besançon | **3,3–8,6** | ≈ 150 | CTR (top 6, 0 clic) | Snippets déjà réécrits en prod → mesurer dans 4-6 sem. | Posée |
| 6 | `/papier-peint-besancon` | papier peint besancon | 13,9 | 47 | Striking distance | Dé-duplication toile de verre (PR #11) + maillage | Posée (PR #11) |
| 7 | `/ratissage-enduit-besancon` | enduit besançon | 10,9 | 40 | Striking distance | Maillage entrant depuis peinture intérieure + blog | Moyenne |
| 8 | `/contact` | (marque / navigation) | 6,5 | 183 | CTR | Snippet peu engageant, mais page de destination secondaire | Basse |

## Bloc 1 — Striking distance

### Opportunité n°1 — le cluster « moisissure plafond salle de bain »

- **Requêtes** : « moisissure plafond salle de bain malgré vmc » (137 impr,
  pos 11,2) · « moisissure plafond salle de bain » (136, pos 13,9) ·
  « moisissure plafond » (100, pos 17,4) · « moisissure salle de bain
  plafond » (85, pos 15,0) · « plafond moisi salle de bain » (61, pos 13,6) ·
  « plafond douche humidité » (51, pos 18,2) · « champignon plafond » (28) ·
  « plafond humide salle de bain » (22) — **≈ 620 impressions cumulées, 2 clics**.
- **Page** : l'article moisissure — 1 333 impressions en propre, plus **469
  impressions sur ses trois ancres** (`#causes`, `#methode`, `#erreur`,
  position 9,6, 0 clic) : Google affiche des liens de section qui ne
  convertissent pas.
- **Constat** : c'est la deuxième visibilité du site, et le contenu répond bien.
  Il manque la conversion (le lecteur repart informé, pas client) et la
  requête pivot exacte « malgré la VMC » mérite sa section H2 dédiée — elle est
  la première requête du site en volume et l'article ne la traite qu'en creux.
- **Actions prêtes à poser** :
  1. Ajouter un H2 « Moisissure au plafond malgré la VMC : pourquoi ça revient »
     avec réponse directe en tête de section (2-3 phrases extractibles).
  2. Bloc de conversion en fin des sections méthode/erreurs : « À partir de
     quand faut-il un professionnel » + rappel du diagnostic gratuit sur site.
  3. Maillage : lien vers `/degat-des-eaux-besancon` quand la cause est une
     fuite, et vers `/peinture-interieure-besancon` pour la réfection —
     l'article pousse aujourd'hui trop peu vers les pages qui vendent.
- **Gain visé** : candidate au top 5-7 sur le cluster — jamais de promesse chiffrée.

### Opportunité n°2 — « peintre besancon » (110 impr, pos 13,2)

Association page non prouvée (export non croisé) ; l'accueil est l'hypothèse la
plus probable (1 853 impressions, position 11,4). Le snippet de production est
déjà réécrit. **Levier restant : le maillage interne** — l'accueil et
`/peinture-interieure-besancon` doivent se répartir clairement « peintre
besançon » (accueil, métier) et « peinture intérieure » (page service) ; la
page service est aujourd'hui à la position moyenne 25,6, signe que Google
hésite. → à confirmer avec un export croisé ; si les deux pages alternent sur
la même requête : **rushiti-cannibal-check**.

### Opportunité n°3 — « plâtrerie à besançon » (73 + 31 + 23 impr, pos 9,1–21,2)

`/platrerie-besancon` est à une porte de la page 1 sur sa requête exacte.
Le snippet de production est déjà bon. **Levier : le maillage entrant** — les
75 pages `platrerie-<zone>` pointent vers elle, mais aucune page pilier d'un
autre silo ne la pousse. Ajouter un lien contextuel depuis
`/peinture-interieure-besancon` (« murs abîmés à reprendre en plâtrerie avant
peinture ») et depuis l'article placo du blog.

### Opportunité n°4 — crépi : 191 impressions, positions 20-23, aucune page dédiée dans git

La plus grosse demande non servie du site. La production a déjà ajouté une
section crépi sur `/peinture-exterieure-besancon` — c'est le bon premier
geste. **Mesurer au prochain export** : si « crepissage besançon » ne remonte
pas vers le top 10 en 6-8 semaines, créer la page dédiée
`/crepi-facade-besancon` (title proposé : `Crépi de façade à Besançon –
réfection & pose | RUSHITI`, 53 car.) avec 301 de rien — c'est une création,
pas une fusion. → **rushiti-brief-seo** le moment venu.

## Bloc 2 — CTR

Le calcul classique donne peu : sur la période, seules 9 pages dépassent 100
impressions en position 3-15, et les gains estimés sont de l'ordre de **2 à 10
clics** chacun — le site est trop jeune pour que le levier snippet pèse lourd,
sauf sur deux cas :

| # | URL / cluster | Position | Impressions | CTR observé | CTR attendu | Gain estimé* |
|---|---|---|---|---|---|---|
| 1 | cluster requêtes « entreprise de peinture (à) besançon » | 3,3–8,6 | ≈ 150 | **0 %** | 3–10 % | ~8-10 clics/période |
| 2 | `/blog/moisissure-…` + 3 ancres | 9,6–12,8 | 1 802 | 0,2 % | ~1,3 % | ~19 clics/période |

*Estimations adossées à la courbe de CTR moyenne du marché, jamais garanties.

**Cas 1 — déjà traité en production.** Les titles/metas live des piliers
contiennent désormais les preuves (20 ans, 4,7/5 sur 34 avis, devis sous 48 h).
La période mesurée (10/06-18/08) précède au moins en partie ces réécritures.
**Aucune nouvelle réécriture recommandée** : re-exporter GSC vers le
**1er octobre 2026** et comparer le CTR à position comparable. Vérifier aussi
la SERP réelle : sur « entreprise de peinture à besançon », le pack local
Google Maps et PagesJaunes écrasent mécaniquement le CTR organique — le
levier complémentaire est la fiche Google Business (→
**rushiti-fiche-google-business**).

**Cas 2 — les ancres de l'article moisissure.** 469 impressions sur des liens
de section qui n'apportent aucun clic. Les actions du Bloc 1 (opportunité n°1)
traitent la cause ; pas de réécriture séparée.

## Validation de la consolidation de la grille (données réelles)

| Mesure | Valeur |
|---|---|
| Pages de la grille locale avec ≥ 1 impression | **63 / 1 368** |
| Impressions cumulées de la grille locale | **310 / 7 100 (4 %)** |
| Pages de la grille locale avec ≥ 1 clic | 2 (`/platrerie-mamirolle`, 1 clic · 1 page ancienne) |
| Meilleures pages locales | `/peinture-interieure-pirey` (40 impr, pos 20) · `/platrerie-mamirolle` (26 impr, pos 4,7, 1 clic) · `/isolation-interieure-tilleroyes` (22) · `/ratissage-enduit-thoraise` (21) · `/revetements-sol-thise` (17, pos 6,8) |

**Décision d'exécution pour la vague 3 de l'audit** : les 63 pages qui
impriment sont épargnées quelle que soit leur position dans les paliers
A/B/C. Le reste de la consolidation peut s'exécuter — la condition « export
GSC d'abord » est maintenant remplie.

**Signal doorway confirmé au passage** : la grille attire des requêtes
d'autres villes (« ratissage lons-le-saunier » 35 impr position 12,
« pose de placo vieux-boucau » 35 impr) — des pages quasi jumelles se classent
sur des zones où l'entreprise n'ira jamais. C'est exactement le symptôme que
la consolidation corrige.

## Pages hors périmètre

- `/` (accueil) : CTR 1,1 % pour position 11,4 — dans la norme, ne pas toucher.
- `/papier-peint-besancon` : CTR 1,5 % pour position 14,1 — au-dessus de
  l'attendu, snippet efficace.
- Piliers en position > 20 (`/isolation-besancon` 27,5 · `/revetements-sol-besancon`
  29,8 · `/peinture-interieure-besancon` 25,6 · `/cloisons-besancon` 35,8 ·
  `/faux-plafonds-besancon` 48,0 · `/toile-de-verre-besancon` 29,9) : problème
  de classement de fond, pas de snippet — autorité et maillage, pas de quick win ici.
- `/degat-des-eaux-besancon` : 33 impressions, position 16 — le silo le plus
  rentable reste quasi invisible ; c'est un chantier de fond (maillage,
  citations locales, B2B), pas un quick win.

## Signalements hors périmètre

- **Anciennes URLs WordPress** (≈ 190 impressions résiduelles : bardage,
  désamiantage, velux…) : vérifié en ligne le 20/08 — elles **redirigent déjà
  en 301** vers les pages actuelles (`/bardage-metallique-besancon-2/` →
  `/peinture-exterieure-besancon`). Rien à faire ; les impressions se
  consolideront seules. → surveillance **rushiti-indexation**.
- **Requête « rushiti-renovation.fr » en position 23,3** (49 impressions,
  0 clic) : anomalie déjà relevée le 19/08 — quand on tape le domaine, le site
  devrait être 1er. → **rushiti-indexation** (contrôle canonical/www).
- **Requête « isolation phonique besançon travauxninja.fr »** (28 impr,
  pos 5,2) : le site se classe sur une requête portant la marque d'un annuaire
  tiers — à ignorer, aucune action.
- **Accueil vs page peinture sur « peintre besançon »** : si l'export croisé
  confirme l'alternance → **rushiti-cannibal-check**.
- **Dépôt git en retard sur la production** (pages piliers) : à resynchroniser
  avant tout déploiement complet — détail dans le PR #11 du dépôt du site.

## Plan d'action

1. **Poser le PR #11** (75 pages papier peint) — après resynchronisation
   git ↔ production, redéploiement complet Cloudflare Pages.
2. **Enrichir l'article moisissure** (H2 « malgré la VMC », bloc conversion,
   2 liens vers dégât des eaux et peinture) — une demi-journée, plus gros
   levier du moment.
3. **Maillage entrant** vers `/platrerie-besancon` et `/ratissage-enduit-besancon`
   (2 liens chacun depuis les piliers voisins et le blog).
4. **Exécuter la consolidation de la grille** (vague 3 de l'audit), en
   épargnant les 63 pages qui impriment.
5. **Mesure** : re-export GSC (même périmètre, si possible **croisé
   requête × page**) vers le **1er octobre** — vérifier le CTR du cluster
   « entreprise de peinture », la position du crépi, et l'effet des titles
   papier peint.

## Limites de l'analyse

Export non croisé (associations requête → page hypothétiques, marquées) ;
période réelle de 70 jours malgré le filtre « 12 mois » (site jeune) ; pas de
seconde période comparable → détecteur de requêtes montantes désactivé ; seuil
d'impressions abaissé à 100 (tolérance signalée) ; les snippets de production
ont changé pendant la période mesurée (piliers), ce qui rend le CTR observé
partiellement obsolète — d'où la consigne de mesurer plutôt que réécrire.
Aucun chiffre de ce rapport ne vient d'ailleurs que de l'export fourni et des
lectures live du 20/08/2026.
