# Relevés de citation IA — dictionnaire des colonnes

> Produit et exploité par le skill `rushiti-citation-ia`. Un fichier par
> relevé, nommé `releve-citations-ia-AAAA-MM-JJ.csv`. Le modèle vide est
> `releve-citations-ia-MODELE.csv`.

Une ligne par **source citée**. Un couple requête × moteur qui cite huit
sources produit huit lignes ; un couple sans aucune source produit une seule
ligne, champs de source vides.

| Colonne | Contenu | Règle |
|---|---|---|
| `date_releve` | Date du relevé, `AAAA-MM-JJ` | Jamais vide : une observation sans date n'est pas comparable |
| `moteur` | Plateforme interrogée | Aperçus IA Google, Google AI Mode, ChatGPT, Perplexity, Copilot, Gemini, Claude |
| `bloc` | `panel` ou `marque` | Deux dénominateurs distincts, jamais additionnés |
| `requete` | La formulation exacte posée | Recopiée au mot près ; la changer casse la comparabilité |
| `surface` | `S`, `M`, `F`, `Ø` ou `NM` | Même valeur répétée sur toutes les lignes d'un même couple requête × moteur |
| `rang_source` | Position de la source dans la liste affichée | Vide si le moteur n'ordonne pas ses sources |
| `url_citee` | URL complète telle qu'affichée | Jamais reconstituée de mémoire |
| `domaine_cite` | Domaine seul | Sert au comptage des occurrences |
| `famille_source` | Famille de la source | Voir `references/corpus-sources-citees.md` |
| `conditions_session` | Conditions de collecte | Session neuve ou non, compte connecté ou non, localisation annoncée |
| `observation` | Erreur factuelle sur l'entreprise repérée dans la réponse | Domaine éteint, horaire faux, service non proposé, forme juridique inexacte |

## Les cinq valeurs de `surface`

| Valeur | Signification | Ce qu'elle appelle |
|---|---|---|
| `S` | Une URL RUSHITI figure dans les sources citées | L'objectif : maintenir |
| `M` | RUSHITI est nommé dans le texte, sans lien vers le site | Trouver le tiers qui porte la mention et le renforcer |
| `F` | Un fait propre au site est repris, sans que RUSHITI soit nommé | Rattacher le fait à l'entité dans la phrase — mode 5 |
| `Ø` | Ni source, ni mention, ni reprise | Absence franche |
| `NM` | Moteur non interrogé | **Jamais compté `0`** — sinon fausse chute au relevé suivant |

## Ce qui ne se met pas dans un relevé

Une citation reconstituée de mémoire, une URL devinée, un moteur « probablement
identique à l'autre », un chiffre arrondi pour faire un total rond. Le relevé
enregistre ce qui a été vu, à la date où il a été vu.

## Une observation sur une URL se relève sur le statut, pas sur l'écran

Le contenu affiché ne dit pas ce que le serveur a répondu : une redirection
suivie et une page servie en 200 rendent exactement la même chose. Toute
observation portant sur le comportement d'une URL — 200, 301, 404, page
servie à la place d'une autre — se relève sur **l'URL finale et le code de
statut**, jamais sur le texte rendu. Et elle se contrôle avec une URL témoin
qui n'a jamais existé : si le témoin renvoie 404, il n'y a pas de catch-all.

Le relevé du 23/08 a manqué ce contrôle et a conclu à tort à un catch-all 200 :
voir `correctif-url-heritees-2026-08-24.md`.

## Correctifs

| Fichier | Ce qu'il corrige |
|---|---|
| `correctif-url-heritees-2026-08-24.md` | Retire l'affirmation « catch-all 200 » du relevé du 23/08 : les trois URL héritées redirigent, et une URL inexistante renvoie bien 404 |
