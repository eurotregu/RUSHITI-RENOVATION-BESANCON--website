# Guide des mots-clés à exclure — Google Ads RUSHITI Rénovation

> Version du 31/08/2026. Public : gestionnaire de campagnes Google Ads
> confirmé. Brouillon soumis à validation d'Isuf.
> **Aucun réglage du compte n'a été modifié** : ce guide dit quoi poser, où,
> et quand.
>
> Source de doctrine : agent `rushiti-google-ads`,
> `references/playbook-campagnes.md` §3, §4, §5, §6, §8 et
> `references/concurrence-positionnement.md` §1, §3, §5, §6. En cas d'écart,
> le playbook prime sur ce document.
>
> Livrables associés : `mots-cles-negatifs-google-ads.txt` (liste à importer)
> et `plan-google-ads-300-500e-2026-08-31.md` (structure de compte).

---

## 0. Cadre — ce qui conditionne tous les arbitrages

| Paramètre | Valeur | Conséquence sur les négatifs |
|---|---|---|
| Budget | 300–500 €/mois (10–16 €/j) — **palier 1** | Chaque euro perdu est un lead perdu. Mais chaque exclusion de trop est invisible. |
| Campagne | 1 seule, Search uniquement | Une liste partagée unique suffit ; pas de conflit inter-campagnes. |
| Groupes d'annonces | 1. Peinture intérieure · 2. Rénovation complète · 3. Dégât des eaux | Le placo n'est **pas** un groupe au palier 1 (playbook §3 : ad group 4, palier 2). |
| Correspondances achetées | expression et exact uniquement, **pas de broad** | Le bruit vient surtout de l'élargissement sémantique, pas de la requête large. |
| Objectif | génération de contacts locaux | On exclut sur l'**intention**, pas sur le vocabulaire. |

**Le point de doctrine qui justifie tout le reste** (playbook §4, veille §6) :
depuis 2025-2026 la correspondance **exacte elle-même s'est élargie
sémantiquement**. Un compte tenu en exact et expression n'est pas un compte
protégé. La revue des termes de recherche et une liste de négatifs vivante
sont obligatoires quel que soit le type de correspondance acheté. C'est la
raison pour laquelle ce guide existe, et pourquoi la liste de départ n'est
qu'un point de départ.

---

## 1. Les dix catégories d'exclusion

Huit à exclure sans discussion, deux à arbitrer.

### 1.1 — Emploi, formation, orientation professionnelle

**Pourquoi** : la personne cherche à *devenir* peintre ou plaquiste, ou à se
faire embaucher. Aucune intention d'achat, jamais. Volume élevé sur les
métiers du bâtiment, donc coût réel.

**Correspondance** : expression. **Niveau** : liste partagée.

`emploi` · `emplois` · `offre d'emploi` · `recrutement` · `recrute` ·
`salaire` · `combien gagne` · `formation` · `formations` · `cap peintre` ·
`cours` · `stage` · `alternance` · `apprentissage` · `devenir peintre` ·
`fiche métier` · `indeed` · `france travail` · `intérim`

### 1.2 — Bricolage, tutoriels, faire soi-même

**Pourquoi** : intention explicite de se passer d'un artisan. Le clic est
définitivement perdu.

**Correspondance** : expression. **Niveau** : liste partagée.

`tuto` · `tutos` · `tutoriel` · `comment faire` · `comment peindre` ·
`comment poser` · `soi meme` · `soi-même` · `diy` · `astuce` · `video` ·
`youtube` · `étape par étape`

### 1.3 — Achat de matériel, distributeurs, marques de peinture

**Pourquoi** : la personne cherche un produit ou un magasin, pas une
prestation. `peinture leroy merlin besançon` est le cas d'école : le mot
« peinture » et le mot « besançon » y sont, l'intention n'y est pas.

**Correspondance** : expression. **Niveau** : liste partagée.

`leroy merlin` · `castorama` · `brico dépôt` · `bricomarché` · `bricoman` ·
`point p` · `gedimat` · `pot de peinture` · `nuancier` · `litre` ·
`rouleau` · `pinceau` · `location` · `matériel` · `echafaudage` ·
`dulux` · `tollens` · `ripolin` · `zolpan` · `sikkens`

### 1.4 — Aides, subventions, dispositifs réglementés

**Pourquoi** — et c'est propre à RUSHITI : **l'entreprise n'a pas de
certification RGE** (`CLAUDE.md` : ne jamais l'affirmer). Une demande
motivée par MaPrimeRénov' ou un crédit d'impôt aboutit à un contact que
RUSHITI ne peut pas servir. Ces clics coûtent cher *et* produisent des leads
cotés C.

**Correspondance** : expression. **Niveau** : liste partagée.

`maprimerenov` · `ma prime renov` · `prime` · `primes` · `subvention` ·
`subventions` · `aide de l'etat` · `aide financiere` · `anah` ·
`crédit d'impot` · `certificat economie energie` · `cee` · `eco ptz` ·
`rge` · `qualibat` · `simulateur aide`

> À revoir si Isuf engage une certification RGE : cette famille entière
> redeviendrait un gisement au lieu d'un poste de perte.

### 1.5 — Plateformes de mise en relation et annuaires

**Pourquoi** (concurrence §1) : Travaux.com, Quotatis, Habitatpresto,
IZI by EDF, Ootravaux ont un budget national et **revendent** le lead à 3-5
artisans. On ne gagne pas cette enchère, et la requête qui les nomme est
navigationnelle : l'internaute veut le formulaire, pas un artisan.

**Correspondance** : expression. **Niveau** : liste partagée.

`travaux.com` · `quotatis` · `habitatpresto` · `izi by edf` · `ootravaux` ·
`starofservice` · `houzz` · `pagesjaunes` · `annuaire` · `annuaires` ·
`comparateur` · `comparateurs` · `forum` · `forums`

### 1.6 — Métiers hors périmètre

**Pourquoi** : `CLAUDE.md` exclut formellement la plomberie et
l'électricité. Le reste (couverture, maçonnerie, menuiserie, terrassement)
n'est pas au catalogue.

**Correspondance** : expression. **Niveau** : liste partagée.

`plombier` · `plomberie` · `electricien` · `électricien` · `electricite` ·
`chauffagiste` · `chaudiere` · `pompe a chaleur` · `climatisation` ·
`couvreur` · `toiture` · `charpente` · `maçon` · `maconnerie` ·
`terrassement` · `menuisier` · `fenetre` · `veranda` · `serrurier` ·
`vitrier` · `ramonage` · `déménagement` · `nettoyage` · `paysagiste`

### 1.7 — Homonymie du mot « peintre » et « peinture »

**La famille la plus sous-estimée, et la plus coûteuse.** En français,
« peintre » désigne aussi l'artiste, et « peinture » désigne aussi le
loisir créatif et la carrosserie. Ces requêtes ont un volume considérable
et tombent en plein sur le mot-clé `"peintre besançon"`.

**Correspondance** : expression. **Niveau** : liste partagée.

`peinture voiture` · `peinture carrosserie` · `peinture jante` ·
`peintre artiste` · `peinture sur toile` · `peinture à l'huile` ·
`peinture acrylique` · `tableau` · `toile` · `peinture au numéro` ·
`peinture par numéro` · `peinture diamant` · `peinture sur soie` ·
`cours de peinture` · `atelier peinture` · `peinture bateau` ·
`peinture poudre` · `peinture industrielle` · `peintre en lettres`

### 1.8 — Recherche d'information pure, administratif, réglementaire

**Pourquoi** : intention de comprendre, pas d'acheter. Ces requêtes sont
déjà couvertes gratuitement par le blog du site
(`docs/seo/regjistri-fjale-kyce.csv` : les lignes marquées *Informative*
sont autant de candidats négatifs en Ads — les payer, c'est payer deux fois
pour un lecteur).

**Correspondance** : expression. **Niveau** : liste partagée.

`définition` · `c'est quoi` · `signification` · `wikipedia` · `norme` ·
`normes` · `dtu` · `réglementation` · `loi` · `pdf` · `télécharger`

**Cas particulier — l'administratif du dégât des eaux.** Ce sont des
requêtes d'assuré perdu dans sa procédure, pas de client cherchant un
artisan. Elles sont nombreuses et elles frappent directement le groupe 3.

`qui paie` · `constat amiable` · `déclaration sinistre` · `convention irsi` ·
`locataire ou propriétaire` · `délai déclaration` · `remboursement` ·
`franchise` · `indemnisation` · `recours` · `litige assurance`

⚠️ **Ne pas exclure `expert`** : « expert dégât des eaux besançon » est
souvent un syndic ou un particulier qui cherche justement un artisan capable
de produire un devis pour l'expert. C'est une requête RUSHITI.

---

## 2. Les deux catégories à arbitrer

C'est ici que se joue la différence entre une liste appliquée mécaniquement
et une liste pilotée.

### 2.1 — Les concurrents directs

Trois concurrents locaux sont identifiés dans la doctrine RUSHITI
(concurrence §5) : **Doubs en Couleurs**, **Peinture Reno**, **Peinture 25**.

Trois postures possibles, une seule recommandée à ce palier :

| Posture | Verdict | Motif |
|---|---|---|
| **Exclure leurs noms en négatif** | ✅ **recommandé** | Requête navigationnelle : l'internaute veut *cette* entreprise. CTR très bas, Quality Score dégradé pour tout le groupe d'annonces, budget consommé sans intention. |
| Enchérir sur leurs marques (conquête) | ❌ | CPC bas mais QS déplorable, mauvaise image dans un tissu local où tout le monde se connaît, risque juridique si la marque est déposée. **Interdit sans validation explicite d'Isuf** (concurrence §6). |
| Ne rien faire | ❌ | Laisse fuir du budget sans le voir. |

**Correspondance** : expression. **Niveau** : liste partagée.
`doubs en couleurs` · `peinture reno` · `peinture 25`

**Trois nuances à ne pas manquer :**

1. **Concurrent ≠ plateforme.** Les plateformes (§1.5) s'excluent pour une
   autre raison : ce ne sont pas des rivaux sur la qualité, ce sont des
   intermédiaires qui revendent le lead. Même geste, motif différent.
2. **Ne jamais exclure sa propre marque.** Au contraire : surveiller
   `rushiti` dans le rapport des termes de recherche. Si un concurrent
   enchérit sur votre nom, cela justifiera une campagne de marque —
   décision de palier 2, pas maintenant.
3. **La liste des concurrents vieillit.** Elle se met à jour depuis
   l'**Aperçu des enchères** (Campagne → Statistiques → Aperçu des
   enchères), qui est la seule source basée sur vos vraies enchères, une
   fois par mois au bilan.

### 2.2 — Les requêtes de prix : le piège classique

Le réflexe « exclure *prix* » est la faute la plus fréquente et la plus
coûteuse. Le playbook §5 la nomme explicitement. Le mot `prix` n'est pas un
signal d'absence d'intention : c'est un signal d'**intention d'achat en
phase de comparaison**.

| Requête | Intention réelle | Verdict |
|---|---|---|
| `prix rénovation appartement besançon` | Va acheter, se renseigne sur l'ordre de grandeur | **Garder** |
| `devis peinture besançon` | Intention maximale | **Garder** — c'est le mot-clé acheté |
| `prix peinture au m2 forum` | Comparaison entre particuliers, pas d'achat imminent | **Exclure** — mais via `"forum"`, pas via `"prix"` |
| `prix moyen peinture m2` | Recherche de barème, intention diffuse | **Exclure** l'expression `"prix moyen"` |
| `prix pot de peinture` | Achat de produit | Déjà couvert par `"pot de peinture"` (§1.3) |

**La règle** : n'excluez jamais `prix`, `tarif`, `devis` ni `combien` seuls.
Excluez la **collocation** qui porte l'intention nuisible —
`"prix moyen"`, `"prix au m2"`, `"prix m2"` — et laissez le mot vivre
partout ailleurs.

**Même logique pour trois autres mots tentants :**

- **`gratuit`** — **ne jamais exclure**. `devis gratuit peintre besançon`
  est exactement la requête recherchée. Excluez seulement une forme nuisible
  constatée, en exact : `[peinture gratuite]`, `"cours de peinture gratuit"`.
- **`avis`** — ne pas exclure. `avis peintre besançon` est une requête de
  quelqu'un qui va choisir un artisan. À ne trancher que si le rapport
  prouve le gaspillage.
- **`pas cher`** — arbitrage réel. Le positionnement RUSHITI interdit de se
  battre sur le prix (concurrence §2 : « aucune annonce ne parle de prix
  bas »), et ces requêtes produisent des leads cotés C. **Recommandation :
  exclure `"pas cher"`, `"moins cher"`, `"petit budget"` au lancement**, et
  réévaluer au bout de trois mois si le CPA le permet. C'est une décision de
  positionnement, à valider par Isuf, pas une évidence technique.

---

## 3. À quel niveau poser chaque exclusion

Google offre trois emplacements. Se tromper de niveau est l'erreur la plus
difficile à diagnostiquer après coup, parce que **rien dans l'interface ne
signale la cause**.

### Le test en trois questions

Pour chaque terme, dans l'ordre :

1. **Ce terme serait-il indésirable dans n'importe quelle campagne RUSHITI,
   aujourd'hui et demain ?** → **liste partagée**.
2. **Indésirable dans cette campagne, mais concevable ailleurs ?** →
   **niveau campagne**.
3. **Indésirable dans ce groupe, mais souhaité dans un autre ?** →
   **niveau groupe d'annonces**, jamais plus haut.

### La règle d'or

**Un terme à exclure d'un seul groupe ne va jamais dans la liste partagée.**

Exemple concret sur ce compte : si vous mettez `rénovation` en liste
partagée pour empêcher le groupe Peinture de servir des requêtes de
rénovation globale, vous venez d'éteindre le groupe Rénovation complète. La
campagne continue de dépenser sur le groupe restant, les demandes chutent,
et aucune alerte ne remonte.

### La vérification anti-collision, obligatoire avant chaque ajout

Doctrine du playbook §5 : **tout négatif est vérifié contre les mots-clés
actifs avant d'être posé.** Un négatif qui chevauche un mot-clé acheté coupe
la diffusion en silence.

Méthode, trente secondes : Google Ads → **Mots-clés** → filtre
« Texte du mot-clé **contient** *\<le terme du négatif\>* ». Si la liste
revient non vide, le négatif entre en collision — le reformuler plus
étroitement, ou le poser au niveau groupe.

### Répartition cible sur ce compte

| Niveau | Contenu | Volume attendu |
|---|---|---|
| **Liste partagée** « RUSHITI — exclusions générales » | §1.1 à §1.8 + §2.1 | ~200 termes |
| **Campagne** | quasi vide au palier 1 : une seule campagne, tout monte en liste partagée | 0 à 5 |
| **Groupe d'annonces** | l'aiguillage entre les 3 groupes (§4) | 5 à 15 par groupe |

---

## 4. L'aiguillage entre les trois groupes

Hiérarchie d'intention : **Dégât des eaux > Rénovation complète > Peinture
intérieure.**

Le dégât des eaux gagne toujours : intention la plus urgente, page de
destination la plus spécifique (devis établi pour l'assurance). Une requête
qui porte un signal de sinistre ne doit jamais être servie par le groupe
Peinture, dont l'annonce et la page ne répondront pas à la question posée.

**À poser en négatif expression sur les groupes 1 (Peinture) et 2
(Rénovation) :**

```
dégât des eaux
degat des eaux
dégâts des eaux
après fuite
apres fuite
infiltration
sinistre
```

**À poser en négatif expression sur le groupe 1 (Peinture) uniquement**, car
la requête appartient au groupe 2 :

```
rénovation complète
rénovation appartement
rénovation maison
```

**À ne pas devancer** : pour tout le reste, n'ajoutez un négatif de groupe
que le jour où le rapport montre réellement le croisement. Avec des
mots-clés en expression et exact, les recouvrements sont rares — et une
exclusion posée par anticipation est une exclusion qu'on n'évaluera jamais.

**Cas placo.** Le groupe Plâtrerie/Placo n'existe pas au palier 1 (playbook
§3 : ad group 4, palier 2, ouvrable quand le rapport montre ≥ 10 requêtes
placo sur un mois). D'ici là, **n'excluez pas les requêtes placo** : elles
sont votre compteur d'ouverture. Laissez-les tomber dans le groupe Peinture,
notez-les, et ouvrez le groupe quand le seuil est atteint.

---

## 5. Types de correspondance : la mécanique exacte

### Les trois comportements

| Type | Écriture | Bloque |
|---|---|---|
| **Large** | `emploi peintre` | toute requête contenant **tous** ces mots, dans n'importe quel ordre |
| **Expression** | `"emploi peintre"` | toute requête contenant ces mots **dans cet ordre** |
| **Exact** | `[emploi peintre]` | **uniquement** cette requête, sans mot avant ni après |

### Trois précisions que la documentation grand public passe sous silence

**1. Pour un négatif d'un seul mot, expression et large sont équivalents.**
`"emploi"` et `emploi` bloquent exactement la même chose : toute requête
contenant le mot. Le choix du type ne commence à compter qu'à partir de deux
mots. Conserver l'écriture en expression est une convention de lisibilité,
pas une différence technique.

**2. Un négatif ne suit pas les variantes proches.** Contrairement à un
mot-clé positif, un négatif ne rattrape ni le pluriel, ni la faute de
frappe, ni la version sans accent :

- `emploi` ne bloque pas « emplois »
- `tuto` ne bloque pas « tutos »
- `electricien` ne bloque pas « électricien »

C'est la première cause de dépense qui passe malgré une liste réputée
propre. Chaque négatif ajouté doit passer trois contrôles : **pluriel ?
faute courante ? version sans accent ?**

**3. Le négatif large est un piège asymétrique.** Il ne bloque que si *tous*
les mots sont présents, ce qui le rend plus permissif qu'on ne croit sur les
requêtes courtes — et plus destructeur qu'on ne croit sur les longues.

### Choix par catégorie

| Catégorie | Type | Pourquoi |
|---|---|---|
| Emploi, bricolage, distributeurs, aides, plateformes, métiers hors périmètre, homonymie, information (§1.1 à §1.8) | **Expression** | Termes d'un ou deux mots portant une intention univoque. L'expression bloque la famille sans dépendre de l'ordre des autres mots. |
| Concurrents nommés (§2.1) | **Expression** | Le nom peut apparaître avant ou après le service. |
| Collocations de prix (§2.2) | **Expression** | Il faut l'ordre : `"prix moyen"` doit bloquer « prix moyen peinture » sans toucher « prix peinture besançon ». |
| Formes nuisibles isolées d'un mot à garder (`gratuit`, `avis`) | **Exact** | Chirurgical : on coupe une requête, la famille survit. |
| Requête pertinente qui a consommé sans convertir | **Exact** | On retire cette requête précise, pas son voisinage sémantique. |
| Cas où l'ordre varie réellement | **Large** | **Seulement avec preuve** : il faut pouvoir citer trois requêtes réelles du rapport que ce négatif bloque. |

---

## 6. Exemples concrets de requêtes à bloquer

Requêtes réalistes sur ce compte, avec le geste exact. À lire comme une
grille d'entraînement : le raisonnement compte plus que la ligne.

| Requête utilisateur | Catégorie | Négatif à créer | Type | Niveau |
|---|---|---|---|---|
| formation peintre en batiment besançon | Emploi | `formation` | expression | partagée |
| offre emploi plaquiste doubs | Emploi | `offre d'emploi` | expression | partagée |
| salaire peintre en batiment 2026 | Emploi | `salaire` | expression | partagée |
| comment peindre un plafond sans trace | Bricolage | `comment peindre` | expression | partagée |
| tuto pose placo sur rail | Bricolage | `tuto` | expression | partagée |
| peinture leroy merlin besançon | Distributeur | `leroy merlin` | expression | partagée |
| prix pot de peinture 10l blanc | Matériel | `pot de peinture` | expression | partagée |
| maprimerenov isolation 2026 | Aides | `maprimerenov` | expression | partagée |
| artisan rge besançon | Aides | `rge` | expression | partagée |
| quotatis avis devis travaux | Plateforme | `quotatis` | expression | partagée |
| devis travaux en ligne gratuit comparateur | Plateforme | `comparateur` | expression | partagée |
| plombier besançon urgence | Hors métier | `plombier` | expression | partagée |
| peintre carrosserie besançon | Homonymie | `peinture carrosserie` | expression | partagée |
| cours de peinture acrylique besançon | Homonymie | `cours de peinture` | expression | partagée |
| peinture diamant kit adulte | Homonymie | `peinture diamant` | expression | partagée |
| tableau peintre bisontin exposition | Homonymie | `tableau` | expression | partagée |
| prix moyen peinture au m2 2026 | Information | `prix moyen` | expression | partagée |
| prix peinture au m2 forum | Information | `forum` | expression | partagée |
| dtu 59-1 peinture pdf | Information | `dtu` | expression | partagée |
| dégât des eaux qui paie locataire ou propriétaire | Administratif | `qui paie` | expression | partagée |
| constat amiable dégât des eaux à remplir | Administratif | `constat amiable` | expression | partagée |
| délai déclaration sinistre dégât des eaux | Administratif | `délai déclaration` | expression | partagée |
| doubs en couleurs besançon avis | Concurrent | `doubs en couleurs` | expression | partagée |
| peintre pas cher besançon | Positionnement | `pas cher` | expression | partagée (à valider) |
| peintre besançon dégât des eaux plafond | Aiguillage | `dégât des eaux` | expression | **groupe 1** |
| rénovation appartement complète besançon | Aiguillage | `rénovation appartement` | expression | **groupe 1** |
| peinture gratuite association besançon | Forme nuisible | `[peinture gratuite]` | **exact** | partagée |
| entreprise peinture besançon horaires | Consommé sans convertir | `[entreprise peinture besançon horaires]` | **exact** | partagée |

**Deux lignes à ne surtout pas ajouter**, pour mémoire, parce qu'elles
paraissent naturelles : `gratuit` (tuerait « devis gratuit peintre
besançon ») et `prix` (tuerait « prix rénovation appartement besançon »,
requête d'acheteur).

---

## 7. Les indicateurs qui pilotent la liste

### 7.1 — Ce qu'on regarde, où, et à partir de quel seuil

Repères issus du playbook §8. Ce sont des **ordres de grandeur du marché
français des artisans locaux, pas des promesses** ; les seuils propres au
compte se substituent à ceux-ci dès qu'il y a trois mois d'historique.

| Indicateur | Où | Repère sain | Signal d'alerte | Lecture côté négatifs |
|---|---|---|---|---|
| **CTR** | Ads, niveau mot-clé | > 5 % | < 3 % | Un CTR bas sur un mot-clé signale une inadéquation requête ↔ annonce : soit l'annonce est à réécrire, soit le mot-clé attire des requêtes à exclure. Regarder ses termes de recherche avant de trancher. |
| **CPC moyen** | Ads | 2–5 € | > 6 € soutenu | Une hausse sans changement de votre côté vient de la concurrence, pas des négatifs. Ne pas sur-exclure en réaction. |
| **Coût par conversion (CPA)** | Ads | 30–50 € | > 50 € sur 3+ semaines | **L'indicateur maître.** C'est lui qui valide ou invalide une passe d'exclusions. |
| **Taux de conversion de la page** | GA4 / Ads | 5–10 % | < 3 % | Sous 3 %, le problème est souvent la page, pas le ciblage. Exclure ne le réparera pas. |
| **Quality Score** | Ads, colonne à activer | 7+ | ≤ 5 | Un QS qui remonte après une passe de négatifs prouve que les exclusions ont amélioré la cohérence. Le meilleur signal de succès. |
| **Taux d'impressions perdues (classement)** | Ads | < 30 % | > 30 % | Problème de QS ou d'annonce, pas de négatifs. |
| **Taux d'impressions perdues (budget)** | Ads | — | > 20 % **avec CPA sous l'objectif** | Bon problème : le ciblage est propre et le budget bride. Candidat à une hausse de 10–15 %. |

**Fenêtre minimale de jugement : 2 semaines ou ~100 clics** sur l'élément
jugé. En dessous, on ne tranche pas — on note.

### 7.2 — Deux indicateurs à construire soi-même

Ils n'existent pas dans l'interface et ce sont les plus utiles.

**Part de dépense sans conversion.** Sur le rapport des termes de recherche
du mois : `coût des termes à 0 conversion ÷ coût total`. C'est le KPI
d'assainissement. On ne cherche pas zéro — une part de prospection est
saine — mais une **baisse mois après mois**. S'il ne baisse pas malgré les
exclusions, le problème est ailleurs (mots-clés trop larges, page, offre).

**Cotation A/B/C des leads** (playbook §8). Isuf note chaque contact reçu :
**A** chantier chiffré ou signé · **B** devis envoyé, sans suite pour
l'instant · **C** hors zone, hors métier, budget incompatible. Trois
semaines suffisent à révéler quel groupe attire des A et lequel remplit le
compteur de C. **C'est la donnée la plus utile du dispositif et elle ne
coûte rien** : un CPA de 35 € qui ne produit que des C est un mauvais CPA,
et aucun indicateur Google ne vous le dira.

### 7.3 — Le taux de rebond : à traiter avec prudence

Le taux de rebond est demandé par réflexe, mais sur ce compte il ne pilote
pas grand-chose, pour trois raisons :

1. **Il n'est pas dans Google Ads** — il vient de GA4, qui raisonne
   d'abord en **taux d'engagement** (le rebond en est le complément).
2. **Le volume ne le porte pas.** À 10–16 €/jour, une requête donnée génère
   quelques sessions par mois. Un taux de rebond calculé sur cinq sessions
   n'est pas un signal, c'est du bruit.
3. **Il est ambigu sur un site d'artisan.** Un visiteur qui arrive, lit le
   bloc de réassurance et appelle depuis son mobile sans seconde page est
   compté comme un rebond alors que c'est une conversion réussie.

**Ce qu'on utilise à la place** : le **CPA par groupe d'annonces**, la
**cotation A/B/C**, et le **Quality Score** comme mesure de cohérence. Le
taux d'engagement GA4 redevient exploitable au palier 2, quand le volume de
sessions le rend lisible.

### 7.4 — L'alarme de sur-exclusion

Une impression bloquée n'apparaît dans aucun rapport : vous ne saurez jamais
ce que vous vous êtes coupé. Le seul symptôme observable est indirect :

> **Volume de clics en baisse nette, CPA stable ou en hausse.**

Si les deux surviennent ensemble après une passe d'exclusions, vous avez
coupé du bon. Reprenez le journal des négatifs (§8), retirez les ajouts en
large et les expressions les plus courtes, et laissez tourner deux semaines.

---

## 8. Maintenance : fréquence, sources, journal

### 8.1 — Le rythme, par phase

| Phase | Période | Fréquence | Objectif |
|---|---|---|---|
| 1 — assainissement | semaines 1 et 2 | **tous les 2 ou 3 jours** | C'est là que se joue l'essentiel du gaspillage. À 13 €/jour, deux semaines sans relevé engagent un tiers du budget mensuel à l'aveugle. |
| 2 — stabilisation | semaines 3 à 6 | hebdomadaire (lundi, 15 min) | Le rendez-vous fixé à la checklist de lancement. |
| 3 — entretien | à partir de la semaine 7 | mensuel, au bilan | La liste est mûre ; on entretient. |
| 4 — revue de dépose | **tous les 3 mois** | trimestrielle | Relire les négatifs larges et les expressions courtes : qu'est-ce qu'ils bloquent aujourd'hui ? |

La **revue de dépose** est la plus négligée. Une liste de négatifs ne fait
que grossir si personne ne la relit ; au bout d'un an elle étouffe la
campagne sans que personne ne sache lequel des 300 termes est responsable.

### 8.2 — Le relevé, pas à pas

1. Campagne → **Insights et rapports** → **Termes de recherche**.
2. Période du relevé, tri par **coût décroissant** — jamais par
   impressions : on cherche l'argent, pas le volume.
3. Appliquer la table de décision ci-dessous ligne par ligne.
4. Vérification anti-collision (§3) sur chaque négatif retenu.
5. Poser, puis **journaliser** (§8.4).

### 8.3 — Table de décision

| Ce que vous voyez | Ce que vous faites |
|---|---|
| Requête pertinente **qui a produit une demande de devis** | L'ajouter en **mot-clé exact** dans le bon groupe. Elle est prouvée. |
| Requête pertinente, 1–2 clics, 0 conversion | **Rien.** Sous la fenêtre de jugement. |
| Requête pertinente, **> ~30 € sans lead** | Mettre le mot-clé en pause (playbook, mode 2) — pas d'exclusion : le mot-clé peut redevenir bon. |
| Requête pertinente, clics répétés, 0 conversion sur 60 j | **Négatif exact.** On coupe cette requête, pas sa famille. |
| Requête hors métier / hors intention | **Négatif expression** sur le mot pivot, **liste partagée**. |
| Requête appartenant à un autre groupe | **Négatif au niveau du groupe** qui l'a servie. |
| Requête placo, isolation, sols | **Ne rien exclure.** C'est le compteur d'ouverture des groupes 4 à 6 (playbook §3). |
| Requête ambiguë | Noter, laisser tourner, revoir au relevé suivant. Une exclusion se retire mal. |

### 8.4 — Le journal

`docs/ads/mots-cles-negatifs-google-ads.txt` sert d'historique daté : chaque
passe ajoute ses termes sous une ligne de date, avec le motif en commentaire.
L'interface Google ne conserve pas *pourquoi* un négatif a été posé ni
*quand* — sans journal, la revue de dépose est impossible et personne n'ose
plus rien retirer.

### 8.5 — Où trouver de nouveaux termes

Par ordre de rendement décroissant :

1. **Le rapport des termes de recherche.** Source n°1, et de loin. Tout le
   reste n'est qu'un complément.
2. **Les contacts non qualifiés reçus par téléphone et par formulaire.**
   La meilleure source qualitative : quand Isuf raccroche en disant « encore
   quelqu'un qui voulait un plombier », il y a un négatif à poser. La
   cotation C de la grille A/B/C sert exactement à ça.
3. **Google Search Console.** Les requêtes organiques du site révèlent le
   vocabulaire réel des chercheurs, parasites compris. Le registre
   `docs/seo/regjistri-fjale-kyce.csv` marque déjà les intentions
   *Informative* : ce sont des candidats négatifs prêts à l'emploi.
   Agents : `rushiti-gsc`, `rushiti-opportunites-gsc`.
4. **La saisie semi-automatique Google et les recherches associées** sur vos
   mots-clés pivots : révèle les collocations parasites (« … salaire »,
   « … formation », « … pdf »).
5. **L'Aperçu des enchères**, mensuel : fait apparaître de nouveaux
   concurrents à exclure (§2.1).
6. **Le Keyword Planner**, en exploration de variantes uniquement.
7. **La saisonnalité** (`rushiti-google-trends`, playbook §13) : certaines
   requêtes parasites sont saisonnières — « peinture volet » au printemps,
   les requêtes d'aides à l'automne au moment des campagnes de rénovation
   énergétique.

### 8.6 — Ce qui n'est pas contournable

Google ne publie pas les termes de recherche qui n'atteignent pas ses seuils
de confidentialité : une part de la dépense reste agrégée et ne peut pas
être exclue. La parade est en amont — des mots-clés positifs serrés — pas en
aval. Ajouter des négatifs ne récupère pas cette part.

---

## 9. Garde-fous RUSHITI

- **Lecture seule.** Ce guide recommande ; Isuf applique dans l'interface.
  Rien n'est « fait » tant qu'il n'a pas cliqué.
- **Aucun chiffre inventé.** Les repères du §7 viennent du playbook et sont
  des ordres de grandeur du marché, pas des promesses. Les chiffres du
  compte restent `[À COMPLÉTER]` tant qu'ils ne sont pas relevés.
- **Pas de RGE, pas de Qualibat.** C'est le motif d'exclusion de §1.4, et
  c'est aussi une interdiction de rédaction.
- **Pas de nom de concurrent dans une annonce**, ni d'enchère sur sa marque
  sans validation explicite d'Isuf (concurrence §6).
- **Jamais de promesse de prise en charge par l'assurance** sur le groupe
  dégât des eaux. La formule autorisée est « devis établi pour votre
  assurance ».
- **RGPD** : aucun nom de client, aucune adresse de chantier dans un
  rapport, un exemple ou un journal.

---

## 10. Checklist de démarrage

- [ ] Créer la liste partagée « RUSHITI — exclusions générales »
      (Outils → Bibliothèque partagée → Listes de mots clés à exclure)
- [ ] Importer `mots-cles-negatifs-google-ads.txt` en **correspondance
      expression**
- [ ] Appliquer la liste à la campagne « Search — RUSHITI Besançon »
- [ ] Poser les négatifs d'aiguillage sur les groupes 1 et 2 (§4)
- [ ] Vérification anti-collision sur l'ensemble : filtre « Texte du
      mot-clé contient » pour chaque terme d'un seul mot (§3)
- [ ] Confirmer avec Isuf l'arbitrage `"pas cher"` (§2.2)
- [ ] Vérifier que ni `gratuit`, ni `prix`, ni `avis`, ni `expert`, ni
      aucune requête placo ne figurent dans la liste
- [ ] Fixer le rendez-vous : relevé tous les 2-3 jours pendant deux
      semaines, puis lundi 15 min
- [ ] Préparer la grille de cotation A/B/C des leads (§7.2)
