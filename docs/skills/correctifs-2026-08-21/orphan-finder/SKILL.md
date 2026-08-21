---
name: orphan-finder
description: Analyse une liste de pages d'un site web pour identifier les pages ORPHELINES (0 lien interne entrant) et FAIBLES (<3 liens internes), puis génère un plan de maillage interne avec pages sources suggérées et anchor texts naturels prêts à poser. À utiliser dès que l'utilisateur mentionne un crawl Screaming Frog, un export Google Search Console (GSC), un audit de maillage interne, des pages non indexées ou mal classées, un batch de contenu fraîchement publié, un audit on-page, ou pose des questions du type "quelles pages devraient pointer vers X ?" / "pourquoi cette page ne ranke pas ?" — même sans utiliser explicitement le mot "orpheline". Contexte RUSHITI Rénovation : priorise les pages commerciales (pages services payants) et les pages géo-locales (quartiers Besançon 25000 + communes du Doubs 25), respecte les silos sémantiques (peinture, plâtrerie, sols, dégât des eaux, isolation, rénovation pièce). Sortie en français, tableau Markdown trié par valeur business décroissante. Périmètre — détection à l'échelle du site à partir d'une liste ou d'un crawl ; le maillage détaillé d'une seule page (brouillon à relier, phrases d'insertion rédigées) relève de rushiti-maillage-interne.
---

# orphan-finder

Spécialiste SEO technique du maillage interne. Identifie les pages mal liées d'un site et génère un plan d'action concret : qui linke vers quoi, avec quelle ancre, dans quel ordre de priorité.

## À quoi sert ce skill

Une page sans liens internes entrants — ou avec trop peu — ne reçoit pas de jus SEO, ne se fait pas découvrir par Googlebot, et ne se classe pas. C'est un problème classique après publication d'un batch de contenu (les nouvelles pages restent isolées), après une refonte, ou simplement parce que le maillage n'a jamais été pensé.

Ce skill prend une liste de pages en entrée, classe chaque page (orpheline / faible / saine), et **pour chaque page faible ou orpheline** propose jusqu'à 3 pages existantes qui devraient pointer vers elle, avec l'anchor text à utiliser.

Sortie : un tableau prêt à exécuter, page par page.

## Frontière avec rushiti-maillage-interne

Ce skill travaille **à l'échelle du site** : il part d'une liste de pages (crawl, export GSC) et dit qui doit linker vers quoi. Pour le maillage complet d'**une seule page** — un brouillon à relier avant mise en ligne, avec les phrases d'insertion rédigées prêtes à coller — passe la main à `rushiti-maillage-interne` : c'est son périmètre.

## Quand déclencher ce skill

Déclenche si l'utilisateur :
- Colle ou uploade un export Screaming Frog (colonnes "Address", "Inlinks", "Title 1", "H1-1"...)
- Colle ou uploade un export GSC Pages (colonnes "Page", "Clicks", "Impressions"...)
- Liste manuellement des URLs avec leur sujet
- Demande "quelles pages devraient linker vers X ?", "où placer mes liens internes ?", "pourquoi cette page n'est pas indexée ?", "comment relier mes nouvelles pages au reste du site ?"
- Mentionne "maillage interne", "orphan pages", "pages orphelines", "internal linking", "link equity", "PageRank interne", "jus SEO"

## Inputs supportés (3 formats)

Adapte le parsing au format reçu. Ne demande des précisions que si le format est ambigu.

### Format 1 — Export Screaming Frog (CSV)
Colonnes typiques : `Address`, `Status Code`, `Title 1`, `H1-1`, `Inlinks`, `Unique Inlinks`, `Indexability`.

**C'est le format idéal.** La colonne `Inlinks` ou `Unique Inlinks` donne le compte direct. Utilise `Unique Inlinks` en priorité (compte les pages sources distinctes, pas les liens dupliqués header/footer).

Filtrer avant analyse :
- Garder uniquement les pages avec `Status Code = 200`
- Garder uniquement les pages avec `Indexability = Indexable`
- Exclure les pages techniques (404 personnalisées, pages de remerciement, pages de tag, pagination)

### Format 2 — Export GSC Pages (CSV)
Colonnes typiques : `Page`, `Clicks`, `Impressions`, `CTR`, `Position`.

**Pas de compteur de liens.** Tu dois inférer le maillage à partir des sujets/URLs. Dans ce cas :
- Tu n'as pas accès au compte d'inlinks réel → tu signales cette limite à l'utilisateur en début de réponse
- Tu travailles sur "pages probablement orphelines" en te basant sur la structure URL (pages profondes, peu de mots-clés rankés, 0 impression = signal fort d'isolation)
- Signal de page probablement orpheline : 0 ou très faibles impressions ET URL profonde (>2 niveaux) ET sujet niche

### Format 3 — Liste collée dans le chat
Format libre, généralement `URL — sujet/titre` une par ligne. L'utilisateur fait alors confiance à ton jugement topique pour proposer le maillage. Tu opères sans données de comptage.

## Workflow

Suis ces étapes dans l'ordre :

### 1. Identifier le format et parser

Détecte le format en regardant les en-têtes (CSV) ou la structure (liste). Si le fichier est gros (>500 lignes), confirme à l'utilisateur le nombre de pages avant de traiter, et propose éventuellement un filtre (par silo, par section du site).

### 2. Filtrer et nettoyer

Exclure du périmètre d'analyse :
- Pages de mentions légales, CGU, politique de confidentialité, cookies
- Pages de remerciement / confirmation
- Pages de tag, archives mensuelles, pagination
- Pages 404 personnalisées
- Page d'accueil (par définition pas orpheline si bien structurée — sauf cas pathologique)

Ces pages peuvent légitimement avoir peu de liens entrants et ne sont pas un problème SEO.

### 3. Classer chaque page

Trois statuts :
- **ORPHAN** : 0 lien interne entrant (`Unique Inlinks = 0` ou inférence forte)
- **WEAK** : 1 ou 2 liens internes entrants
- **OK** : 3+ liens internes entrants (ne pas inclure dans le tableau de sortie, sauf si l'utilisateur demande l'inventaire complet)

Sur GSC ou liste collée (pas de compteurs), classe en "probablement orphelin" / "probablement faible" en te basant sur le signal d'impressions et la profondeur URL.

### 4. Pour chaque page flaggée, suggérer jusqu'à 3 pages sources

C'est le cœur du skill. Pour chaque page Orphan ou Weak, propose jusqu'à 3 pages existantes du site qui devraient logiquement linker vers elle.

Critères de sélection des sources (par ordre de priorité) :

1. **Pertinence topique forte** — la page source traite d'un sujet adjacent ou parent de la cible
2. **Autorité supposée** — page d'accueil > pages piliers (services principaux) > pages catégories > pages détail
3. **Silo cohérent** — préfère lier dans le même silo sémantique (voir `references/rushiti-silos.md` pour la cartographie RUSHITI)
4. **Cohérence géo** — pour les pages géo-localisées (quartier, commune), lier depuis les pages géo parentes et les services associés à cette zone
5. **Bidirectionnel évité** — si A linke déjà vers B, ne pas systématiquement proposer B → A (sauf si pertinent navigationnel)

**Ne jamais inventer une page source qui n'existe pas dans la liste fournie.** Si rien ne convient, indique-le ("pas de source pertinente identifiable dans l'inventaire fourni — créer du contenu intermédiaire ou élargir le périmètre").

### 5. Rédiger l'anchor text de chaque suggestion

L'anchor text suggéré doit être :
- **Descriptif** : il décrit ce que l'utilisateur va trouver sur la cible
- **Naturel** : il s'intègre dans une phrase, ce n'est pas un slug brut
- **Varié** : ne répète pas exactement le titre ou le mot-clé cible (anti-Penguin, anti-suroptimisation)
- **Contextualisé** : peut inclure un signal géo, un cas d'usage, un bénéfice — pas juste le mot-clé sec

**Exemples d'anchors RUSHITI bien rédigés :**

| Cible | Mauvais anchor (exact match spam) | Bon anchor (descriptif, naturel) |
|---|---|---|
| `/peinture-interieure-besancon` | "peinture intérieure Besançon" (3× sur le site) | "nos prestations de peinture intérieure à Besançon" |
| `/degat-des-eaux-planoise` | "dégât des eaux Planoise" | "intervention après dégât des eaux dans le quartier Planoise" |
| `/pose-toile-de-verre` | "pose toile de verre" | "préparation des murs par pose de toile de verre" |
| `/platrerie-besancon` | "plâtrerie Besançon" | "notre savoir-faire en plâtrerie traditionnelle" |

### 6. Prioriser et trier la sortie

Tri du tableau de sortie, du plus prioritaire au moins prioritaire :

**Niveau 1 — Pages commerciales orphelines** (haute valeur business)
- Pages services payants : `/peinture-interieure`, `/platrerie`, `/degats-des-eaux`, `/sols`, `/isolation`, `/papier-peint`, `/toile-de-verre`...
- Pages géo-services commerciales : `/peinture-interieure-besancon`, `/degat-des-eaux-pontarlier`...

**Niveau 2 — Pages géo-locales orphelines** (haute valeur SEO local)
- Pages quartiers Besançon (Battant, Planoise, Palente, Chaprais, Velotte, Bregille, Saint-Ferjeux, Montrapon, Saint-Claude, Vaîte, Tilleroyes...)
- Pages communes Doubs prioritaires (Pontarlier, Montbéliard, Thise, Chalezeule, Saône, Morre, École-Valentin, Pouilley-les-Vignes, Châtillon-le-Duc, Dannemarie-sur-Crête...)

**Niveau 3 — Pages chantiers / réalisations orphelines** (preuve sociale, conversions)

**Niveau 4 — Pages blog / éducation orphelines** (valeur informationnelle, top of funnel)

**Niveau 5 — Pages WEAK** dans le même ordre (commerciales > géo > chantiers > blog)

## Format de sortie

Toujours produire un tableau Markdown en français. Structure exacte :

```markdown
## Analyse maillage interne — [date] — [N pages analysées]

**Résumé :**
- 🔴 X pages ORPHELINES (0 lien entrant)
- 🟠 Y pages FAIBLES (1-2 liens entrants)
- 🟢 Z pages saines (3+ liens entrants, hors tableau)

[Si format GSC ou liste : mentionner la limite méthodologique]

## Plan d'action — maillage interne

| # | Page cible | Statut | Page source suggérée | Anchor text proposé |
|---|---|---|---|---|
| 1 | /peinture-interieure-planoise | 🔴 ORPHELINE | /peinture-interieure-besancon | nos chantiers de peinture intérieure dans le quartier Planoise |
| 1 | /peinture-interieure-planoise | 🔴 ORPHELINE | /quartiers/planoise | rénovation et peinture des appartements du quartier Planoise |
| 1 | /peinture-interieure-planoise | 🔴 ORPHELINE | / (accueil) | interventions de peinture sur Planoise et Châteaufarine |
| 2 | /degat-des-eaux-pontarlier | 🔴 ORPHELINE | /degats-des-eaux | notre équipe d'intervention sur Pontarlier et la frontière |
| ... | ... | ... | ... | ... |
```

Le numéro `#` est l'index de **priorité** (regroupe les 3 lignes d'une même cible). Une cible = une priorité = jusqu'à 3 lignes.

## Quand demander des précisions à l'utilisateur

Avant de lancer l'analyse, demande seulement si :
- Le format est ambigu (ex : CSV sans en-têtes clairs)
- Le périmètre est énorme (>1000 pages) — propose un découpage par silo
- L'utilisateur veut un filtre spécifique (ex : "uniquement les pages quartiers")

Sinon, **enchaîne directement sur l'analyse**. Pas de questions de confort.

## Limites à signaler proactivement

À mentionner en haut du livrable :
- **GSC Pages ou liste collée** : "Analyse basée sur l'inférence topique — pour des compteurs réels d'inlinks, fournir un crawl Screaming Frog."
- **Pages 404 / non-indexables détectées** : "X pages exclues car non-indexables (codes 3xx/4xx/5xx ou noindex)."
- **Aucune source pertinente trouvée pour une cible** : "Cible isolée — envisager la création de contenu intermédiaire ou un lien depuis la home/menu."

## Référence détaillée

Pour la cartographie complète des silos sémantiques RUSHITI et la liste de priorisation géo Doubs, consulte `references/rushiti-silos.md` quand tu travailles sur un export rushiti.fr ou rushiti-renovation.fr.
