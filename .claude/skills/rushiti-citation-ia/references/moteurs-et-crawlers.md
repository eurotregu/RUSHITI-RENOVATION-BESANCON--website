# Les moteurs de réponse : d'où vient une citation, plateforme par plateforme

> **Version 1.0 — 22/08/2026.** Ce fichier décrit **comment chaque plateforme
> fabrique la liste de sources** qu'elle affiche, parce que c'est cela qui
> décide d'une citation — pas une « optimisation IA » générique.
>
> **Les noms de robots et les politiques d'accès changent plusieurs fois par
> an.** Avant de produire un plan d'action qui repose sur un nom de robot,
> l'agent revérifie la documentation de l'éditeur et **écrit la date de la
> vérification** dans le rapport. Une liste de user-agents recopiée de mémoire
> est une source d'erreurs, pas une preuve.

## Le principe commun

Aucune de ces plateformes ne « classe » un site. Chacune :

1. reformule la question de l'utilisateur en une ou plusieurs recherches ;
2. récupère un petit nombre de documents — quelques unités à quelques
   dizaines ;
3. rédige une réponse à partir de ce paquet ;
4. affiche tout ou partie des documents utilisés.

Trois conséquences pratiques, qui gouvernent tout le reste :

- **Être indexé est nécessaire, jamais suffisant.** Le paquet est petit ; il
  se remplit avec ce qui répond le plus directement à la reformulation.
- **La question posée compte plus que le mot-clé.** « Qui appeler après un
  dégât des eaux à Besançon » et « peintre Besançon » ne convoquent pas les
  mêmes sources, alors que la prestation est la même.
- **Pour une requête locale, le paquet est dominé par des sources tierces** —
  annuaires, plateformes de mise en relation, fiches d'établissement — et non
  par les sites des artisans eux-mêmes. C'est le fait le plus important de ce
  fichier, et la raison pour laquelle le mode 3 passe avant le contenu.

## Plateforme par plateforme

### Aperçus IA de Google (AI Overviews) et AI Mode

- **Source** : l'index de Google, exploré par **Googlebot**. Les aperçus IA et
  AI Mode sont des surfaces de la Recherche, pas un index séparé.
- **Ce qu'on voit** : un encadré de réponse avec des liens de sources, et pour
  les requêtes locales, souvent un bloc local adossé aux fiches
  d'établissement.
- **Ce qui décide** : être indexé, répondre à la question sous une forme
  prélevable, et — pour le local — la fiche Google Business, ses services, ses
  questions-réponses et ses avis.
- **Piège documenté** : `Google-Extended` **ne concerne pas** les aperçus IA
  ni AI Mode. Ce contrôle porte sur l'usage des contenus par les produits
  Gemini. Le bloquer ne vous sort pas des aperçus ; l'autoriser ne vous y fait
  pas entrer. Ce qui vous en sortirait, c'est de bloquer Googlebot ou de
  passer en `noindex`.
- **Collecte** : requête en navigation privée, langue française, localisation
  Besançon si l'interface le permet ; capture d'écran + liste des domaines
  cités. Les aperçus ne se déclenchent pas sur toutes les requêtes : « aucun
  aperçu affiché » est une observation valable, à noter comme telle et non
  comme une absence de citation.

### ChatGPT (OpenAI)

- **Source** : recherche web intégrée pour les questions d'actualité ou
  locales ; sinon la réponse peut provenir du modèle seul, sans source.
- **Ce qu'on voit** : soit une réponse avec liens de sources, soit une réponse
  sans lien où le nom d'une entreprise peut apparaître **sans** qu'aucun site
  ne soit cité — c'est typiquement une **mention d'entité** (`M`), qui vient
  presque toujours d'un tiers agrégateur, pas de votre site.
- **Robots à connaître** : `OAI-SearchBot` (alimente la recherche et donc les
  citations), `ChatGPT-User` (récupération déclenchée par une question
  d'utilisateur), `GPTBot` (collecte pour l'entraînement). Pour une citation
  affichée, ce sont les deux premiers qui comptent.
- **Collecte** : conversation neuve, sans mémoire ni personnalisation si
  possible, recherche web activée. Poser la question, puis **demander
  explicitement les sources** si aucune n'apparaît : la réponse à cette
  relance indique si le modèle s'appuie sur des documents ou sur ses
  paramètres.

### Perplexity

- **Source** : son propre index web, complété par des récupérations en direct.
  C'est la plateforme la plus explicitement adossée aux sources : chaque
  affirmation est numérotée.
- **Robots à connaître** : `PerplexityBot` (indexation), `Perplexity-User`
  (récupération déclenchée par une question).
- **Pourquoi elle est la plus utile à mesurer** : elle affiche la liste
  complète des sources. C'est le meilleur relevé du corpus disponible, et le
  plus rapide à collecter — commencer par elle.
- **Collecte** : session neuve, mode de recherche par défaut (ne pas changer de
  mode entre deux relevés), copier la réponse **et** la liste complète des
  sources numérotées.

### Microsoft Copilot

- **Source** : l'index **Bing**. Copilot n'a pas d'index propre.
- **Conséquence directe** : « optimiser pour Copilot » n'existe pas. Ce qui
  existe, c'est vérifier l'indexation Bing du site (Bing Webmaster Tools) et
  la fiche **Bing Places**. Pour un site récent, l'indexation Bing est souvent
  très en retard sur Google — c'est un contrôle à faire avant toute conclusion
  sur une absence de citation.
- **Robot** : `bingbot`. Un site bloqué pour `bingbot` est invisible pour
  Copilot, quelle que soit sa position dans Google.
- **Collecte** : navigation privée, Copilot web, question en français, relever
  les liens de sources affichés.

### Gemini (Google)

- **Source** : ancrage sur la Recherche Google pour les questions factuelles
  et locales.
- **Robot** : `Google-Extended` s'applique ici — c'est sa vraie portée.
- **Collecte** : session neuve. Gemini affiche parfois un bouton de
  vérification des sources : l'activer et relever ce qu'il donne.

### Claude (Anthropic)

- **Source** : recherche web lorsqu'elle est disponible dans le produit.
- **Robots à connaître** : `ClaudeBot` (collecte), `Claude-User` (récupération
  déclenchée par une question), `Claude-SearchBot`.
- **Collecte** : conversation neuve, recherche activée, sources demandées
  explicitement.

## Ce qui n'a aucun effet mesurable sur une citation

À dire clairement à Isuf quand une de ces actions lui est proposée par un
outil ou un prestataire — non parce qu'elles sont nuisibles, mais parce
qu'elles consomment un budget d'attention limité :

| Action souvent proposée | Ce qu'elle produit réellement |
|---|---|
| Publier un fichier `llms.txt` | Convention émergente. Aucun des moteurs suivis ne documente publiquement son usage comme source d'ancrage. Coût quasi nul : à publier si l'on veut, jamais à compter comme une action de visibilité |
| Autoriser `CCBot` | Common Crawl alimente des corpus d'entraînement, pas les réponses citées du mois en cours |
| Débloquer `Google-Extended` « pour les aperçus IA » | Aucun effet sur les aperçus IA ni sur AI Mode (voir plus haut) |
| Viser un LCP sous 2 s « parce que les robots IA abandonnent les pages lentes » | La vitesse a de vraies raisons d'être bonne — conversion, exploration — mais celle-là n'est pas documentée. Une bonne action justifiée par un faux motif propage le faux motif ailleurs |
| Multiplier les questions-réponses balisées (« 50 FAQ ») | Cinquante réponses proches produisent un site répétitif que les moteurs résument en une seule source. Ce sont des questions **différentes** qui ouvrent des paquets différents |
| Répéter le nom de la ville dans chaque phrase | Détériore la lecture sans améliorer la pertinence locale, qui se joue sur la cohérence d'entité et les sources tierces |

## Protocole de collecte (à remettre à Isuf tel quel)

1. **Une session neuve par requête**, en navigation privée, hors compte
   connecté quand c'est possible. Un compte qui connaît déjà RUSHITI
   personnalise la réponse et fausse la mesure.
2. **Coller la formulation exacte** du panel, sans rien ajouter, sans
   reformuler, sans préciser « à Besançon » si la requête ne le dit pas.
3. **Copier la réponse entière et la liste des sources**, pas un résumé.
4. **Noter** : moteur, date, heure, conditions (connecté ou non, localisation
   annoncée par l'interface s'il y en a une).
5. **Ne pas relancer** une requête dont la réponse déplaît pour en obtenir une
   meilleure. Le relevé enregistre ce qui s'est passé, pas ce qu'on espérait.
6. En cas d'aperçu absent ou de moteur indisponible : `NM`, avec la raison.
