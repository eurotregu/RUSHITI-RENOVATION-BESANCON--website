# Les seize erreurs des plans « visibilité IA » génériques

> **Version 1.0 — 22/08/2026.** Ce fichier dissèque un plan de visibilité IA
> réellement produit pour RUSHITI par un outil généraliste, en août 2026.
>
> Il n'est pas là pour railler ce plan : sa structure était bonne, et plusieurs
> de ses idées sont justes. Il est là parce que **chacune de ces seize erreurs
> est plausible** — la plupart viennent de bonnes sources mal transposées à un
> artisan français. L'agent les connaît pour deux raisons : ne pas les
> reproduire, et les reconnaître quand un prestataire les propose à Isuf.

## A. Erreurs de données structurées

**1. `"siret": "905 214 631 00012"` comme propriété schema.org.**
La propriété n'existe pas dans le vocabulaire : elle est ignorée. Et le SIRET
canonique, en données structurées, s'écrit sans espaces.
→ `identifier` / `PropertyValue`, voir `grille-citabilite-page.md`.

**2. `aggregateRating` auto-déclaré avec la note et le nombre d'avis Google.**
Les consignes Google excluent le balisage des avis qu'une entreprise collecte
sur elle-même ; le risque d'action manuelle est réel, et la maison a déjà
tranché contre. Le chiffre a de surcroît le défaut d'être volatil : figé dans
le code, il devient faux au trente-cinquième avis.
→ Preuve sociale dans le texte visible, avec la date du relevé.

**3. `foundingDate` fausse.**
Le plan écrivait le 15/11/2021 ; le RCS dit le 04/11/2021. Une date d'entité
fausse est exactement le genre de contradiction que les moteurs recoupent avec
les registres publics — et le bloc marque du relevé la fera ressortir.
→ Les faits d'entité viennent des registres, jamais d'une estimation.

**4. `geoCircle` de 50 km autour de Besançon.**
Le rayon attrape Vesoul, Dole, Gray, Lons-le-Saunier : hors du Doubs, donc hors
du périmètre validé. Et un rayon déclaré ne fabrique aucune pertinence locale ;
il dilue celle qui existe.
→ Déclarer les communes réellement servies.

## B. Erreurs de fond sur le fonctionnement des moteurs

**5. Confondre `Google-Extended` et les aperçus IA.**
`Google-Extended` porte sur l'usage des contenus par les produits Gemini. Il
n'a pas d'effet sur les aperçus IA ni sur AI Mode, qui sont des surfaces de la
Recherche adossées à l'index de Googlebot. Le débloquer « pour apparaître dans
les aperçus » est une action sans effet — et pire qu'inutile, puisqu'elle
donne le sentiment qu'un problème est réglé.

**6. Présenter `llms.txt` comme un levier.**
Aucun des moteurs suivis ne documente publiquement son usage comme source
d'ancrage. Le fichier coûte quelques minutes : le publier est défendable, le
compter comme une action de visibilité ne l'est pas.

**7. Mettre `CCBot` dans la liste des robots à autoriser pour être cité.**
Common Crawl alimente des corpus d'entraînement, pas les réponses citées du
mois en cours. Les robots qui décident d'une citation affichée sont ceux de la
recherche : `OAI-SearchBot`, `PerplexityBot`, `bingbot`, `Googlebot`, et leurs
équivalents déclenchés par une question d'utilisateur.

**8. Traiter Copilot comme un moteur à optimiser en propre.**
Copilot s'appuie sur l'index Bing. L'action utile n'est pas « optimiser pour
Copilot » mais vérifier l'indexation Bing et la fiche Bing Places — un contrôle
à faire avant toute conclusion, l'indexation Bing d'un site récent étant
souvent très en retard sur Google.

**9. « Les robots IA abandonnent les pages lentes » (LCP < 2 s).**
Affirmation non documentée. La vitesse a de vraies raisons d'être bonne ; en
inventer une fausse propage le faux motif dans toutes les décisions suivantes.

**10. Confondre pré-entraînement et citation.**
« L'entreprise a été créée en 2021, donc après la date de coupure des modèles,
donc ChatGPT ne peut pas la connaître » : le raisonnement ne tient plus dès que
la recherche web est active, et c'est elle qui produit les citations. Une
entreprise de 2021 est parfaitement citable ; ce qui manque, ce sont des
sources tierces, pas des années.

## C. Erreurs de méthode

**11. Publier son propre « Top 15 des meilleurs artisans de Besançon » en s'y
plaçant premier.**
Un auto-classement n'est pas citable par un moteur qui privilégie les sources
tierces, et il met l'entreprise en porte-à-faux avec des confrères qui
travaillent dans les mêmes rues. Un comparatif de **solutions techniques** est
légitime et prélevable ; un classement d'entreprises rédigé par l'une d'elles,
non.

**12. Acheter un emplacement en vedette et le compter comme autorité.**
Un placement payant se déclare (`rel="sponsored"`). On peut acheter de la
visibilité ; jamais un signal de confiance.

**13. Se tromper de presse locale.**
Le plan visait *Le Bien Public* — quotidien de Dijon et de la Côte-d'Or. Pour
Besançon et le Doubs : L'Est Républicain (édition Besançon), macommune.info,
France 3 Bourgogne-Franche-Comté. Une erreur de titre dans un premier email le
fait classer sans réponse.

**14. Viser Wikipédia.**
Les critères d'admissibilité — notoriété établie par des sources secondaires
d'envergure — excluent une SARL artisanale de 2021. Y consacrer une phase, c'est
brûler des semaines. Wikidata est en revanche atteignable, adossé au SIREN, en
une heure : à faire si l'on veut, sans en attendre d'effet démontré sur une
citation locale.

**15. Fixer des objectifs chiffrés d'apparition (« 80 % d'aperçus IA à trois
mois »).**
Promesse de classement, interdite par les garde-fous de la maison — et
invérifiable, puisque les réponses varient d'une session à l'autre.

**16. Prendre la quantité pour la couverture** (« 30 services sur la fiche
Google », « 50 questions balisées », « 12 guides »).
Cinquante réponses proches produisent un site répétitif que les moteurs
résument en une source unique. Ce sont des **questions différentes** qui
ouvrent des paquets de sources différents.

## Ce que le plan générique avait juste

À conserver, parce qu'un fichier de pièges qui ne reconnaît rien devient
suspect à son tour :

- **Le diagnostic central est bon** : la faiblesse est l'autorité d'entité hors
  du site, pas le site lui-même.
- **La fiche Google Business est le premier levier local** — services,
  questions-réponses, réponses aux avis. C'est vrai, et c'est le meilleur
  rapport effort/effet du plan.
- **Les avis détaillés mentionnant la prestation et le quartier** valent mieux
  que des avis génériques. Vrai, sous réserve de ne jamais dicter le texte d'un
  avis ni de le rémunérer.
- **Le format compte** : réponse directe, listes, tableaux réels. C'est le
  fondement du mode 5.
- **La cohérence NAP entre toutes les sources** est bien la condition
  d'existence de l'entité pour un moteur. Le dépôt l'a déjà largement traitée.

## La différence de méthode, en une phrase

Un plan générique optimise **un site pour des moteurs**. Ce skill traite
**une entité dans un corpus de sources** : il commence par nommer les sources
que les moteurs citent déjà à Besançon, puis il y fait entrer RUSHITI — par la
porte, avec des faits vrais, et en disant lesquelles sont fermées.
