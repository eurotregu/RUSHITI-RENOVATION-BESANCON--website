# Fichiers de production prêts à déployer — rushiti-renovation.fr

Corrections issues des décisions d'Isuf du 20/08/2026
(`docs/seo/decisions-isuf-2026-08-20.md`) et du relevé Search Console du même
jour (`docs/gsc/configuration-ultra-premium.md`).

Ces trois fichiers sont **complets** : ils remplacent tels quels ceux servis à la
racine de `rushiti-renovation.fr`, via le déploiement Cloudflare Pages habituel.
Ils ont été construits à partir du contenu réellement en ligne le 20/08/2026, en
ne modifiant que les lignes listées ci-dessous.

| Fichier | Destination | Ce qui change | Statut |
|---|---|---|---|
| `llms.txt` | `/llms.txt` | 3 lignes : avis 29 → **34** (×2), horaires | ✅ à déployer |
| `robots.txt` | — | 1 ligne retirée : le sitemap vide | ⛔ **inutile — voir ci-dessous** |
| `sitemap.xml` | — | 1 bloc `<sitemap>` retiré | ⛔ **inutile — voir ci-dessous** |

> ## ⛔ Correction du 20/08/2026 (soir) — `robots.txt` et `sitemap.xml` sont à ignorer
>
> Ces deux fichiers ont été préparés avant l'inspection de l'infrastructure
> Cloudflare. Ils ne serviraient à rien : **un Worker intercepte toutes les
> requêtes** du site (`image-license-jsonld`, routé sur
> `*rushiti-renovation.fr/*`) et c'est lui, pas le dépôt, qui produit
> `robots.txt` et les sitemaps.
>
> Ce que fait le Worker, relevé dans son code :
>
> | Chemin | Comportement |
> |---|---|
> | `/sitemap.xml` | **fabrique** un `<sitemapindex>` à 2 enfants — le fichier du dépôt est ignoré |
> | `/sitemap-pages.xml` | proxy vers le `/sitemap.xml` du dépôt |
> | `/robots.txt` | prend celui du dépôt et lui **ajoute** la ligne `sitemap-communes.xml` |
> | `/sitemap-communes.xml` | construit un `<urlset>` en filtrant le sitemap du dépôt |
>
> Or le dépôt de production est **déjà correct** : son `robots.txt` ne déclare
> qu'un seul sitemap, et son `sitemap.xml` contient les **1 396 URL**, communes
> comprises — depuis le commit du 20/08 à 10:54, « Sitemap : rapatrie les
> 1227 URL de communes depuis le Worker ». C'est précisément pour ça que
> `/sitemap-communes.xml` répond vide : le filtre du Worker ne trouve plus rien
> à extraire.
>
> **Le correctif est donc dans le Worker**, pas dans un fichier : retirer les
> quatre gestionnaires ci-dessus pour que le dépôt soit servi tel quel. Les deux
> fichiers sont conservés ici comme référence de la cible, pas comme livrable.

| Fichier | Destination | Ce qui change |
|---|---|---|
| `llms.txt` | `/llms.txt` | 3 lignes : avis 29 → **34** (×2), horaires |

## Détail des changements

### `llms.txt` — 3 lignes, rien d'autre

```diff
- Note 4,7/5 sur 29 avis Google.
+ Note 4,7/5 sur 34 avis Google.

- - Horaires : du lundi au vendredi, 8h–18h
+ - Horaires : du lundi au vendredi 7h–20h30, samedi 8h–20h30, dimanche 9h–17h30

- - Avis : 4,7/5 sur 29 avis Google
+ - Avis : 4,7/5 sur 34 avis Google
```

Le reste du fichier — 33 liens, les 9 guides d'expert, les coordonnées — est
repris à l'identique. Contrôle effectué : les 33 URL citées existent toutes dans
`sitemap-pages.xml`.

### `robots.txt` et `sitemap.xml` — le sitemap vide

`sitemap-communes.xml` répond en 200 avec **zéro URL**, et il est pourtant
annoncé à Google deux fois. Les pages communes sont déjà dans
`sitemap-pages.xml` : il n'y a rien à récupérer, seulement une ligne « 0 URL
détectée » à faire disparaître de Search Console.

> ⚠️ **Le sitemap est généré.** Remplacer le fichier ne suffira pas : à la
> prochaine régénération, le bloc `sitemap-communes.xml` reviendra. La correction
> durable est dans la configuration du générateur. Le fichier fourni ici est un
> dépannage immédiat, pas le correctif final.

Après déploiement : Search Console → Index → Sitemaps → supprimer l'entrée
`sitemap-communes.xml` si elle y a été soumise.

---

## Les corrections qui ne peuvent pas être livrées en fichier

Trois corrections décidées le 20/08 touchent des pages générées ou des règles de
routage : elles n'existent pas comme fichier isolé dans ce dépôt et se posent à
la source.

### 1. Horaires de `/contact` — le plus urgent

La page affiche **les deux versions à la fois** :

| Emplacement | Texte servi |
|---|---|
| Bloc « Horaires » | `Lundi – Vendredi : 8h – 18h` ❌ |
| Pied de page de la même page | `Lun – Ven : 7h – 20h30 · Sam : 8h – 20h30 · Dim : 9h – 17h30` ✅ |

Remplacer le bloc « Horaires » par les trois lignes du pied de page. C'est la
seule correction du lot qu'un client voit au moment de décider s'il appelle :
aujourd'hui la page lui dit fermé à 18h alors qu'on décroche jusqu'à 20h30.

Aligner dans la foulée le JSON-LD `openingHoursSpecification` :

```json
"openingHoursSpecification": [
  { "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "07:00", "closes": "20:30" },
  { "@type": "OpeningHoursSpecification",
    "dayOfWeek": "Saturday", "opens": "08:00", "closes": "20:30" },
  { "@type": "OpeningHoursSpecification",
    "dayOfWeek": "Sunday", "opens": "09:00", "closes": "17:30" }
]
```

… et la fiche Google Business Profile, qui alimente le « Ouvert · Ferme à … »
du pack local.

### 2. « Qualification RGE » — 152 pages, une chaîne de gabarit

Badge relevé mot pour mot sur `/isolation-besancon`, `/isolation-thise` et
`/isolation-interieure-besancon` ; absent de `/peinture-interieure-besancon`
(page témoin). Deux familles × 76 lieux = **152 pages**.

Retirer l'élément `Qualification RGE` de la liste de badges du **gabarit
isolation**, puis regénérer. Ne rien mettre à la place : les quatre autres
badges (20 ans, diagnostic gratuit, DTU 25.41, artisan local) sont vrais et
suffisent.

Contrôle après déploiement : la chaîne ne doit plus apparaître sur
`/isolation-besancon` **ni** sur deux pages commune tirées au hasard.

### 3. `/desamiantage-sol-besancon` — il n'y a aucune règle à supprimer

**Correction du 20/08 (soir).** Cette URL ne fait l'objet d'aucune règle de
redirection : le fichier `desamiantage-sol-besancon.html` **n'existe pas** dans
le dépôt de production, donc l'URL répond 404 — et le Worker rattrape tous les
404 avec un **devineur par mots-clés** (`legacyTarget`) qui renvoie un 301 vers
la première page dont un mot-clé apparaît dans l'URL. « sol » →
`/revetements-sol-besancon`.

Le même mécanisme explique les trois autres cas relevés le matin :

| URL en 404 | Mot-clé qui déclenche | Cible devinée |
|---|---|---|
| `/desamiantage-sol-besancon` | `sol` | `/revetements-sol-besancon` |
| `/peinture-plafond-batiment-besancon` | `plafond`, testé avant `peinture` | `/faux-plafonds-besancon` |
| `/enduit-chaux-besancon` | `enduit` | `/ratissage-enduit-besancon` |
| `/organic-ehpad-besancon` | `organic` | `/platrerie-besancon` |

Ce n'est donc pas un problème de quatre URL mais un comportement **systémique** :
toute URL morte ou mal orthographiée contenant « sol », « peinture »,
« plafond »… reçoit un 301 vers une page sans rapport, que Google traite en
soft 404.

**Conséquence pratique, et elle est bonne :** publier la page désamiantage fait
disparaître le 404, donc le mauvais 301, sans toucher au Worker.

**Décision distincte à prendre** (elle dépasse le désamiantage) : rendre le
rattrapage 404 conservateur — ne rediriger que sur une correspondance certaine,
sinon servir un vrai 404. Ce changement touche **chaque requête du site** : il
n'est pas posé sans validation explicite d'Isuf. **La rédaction attend les références
du certificat** — périmètre SS3/SS4, organisme, numéro, validité : elles
déterminent le contenu autant que la conformité de l'affirmation.

---

## Ordre de déploiement

1. Horaires `/contact` + JSON-LD + fiche Google
2. Retrait RGE des 152 pages isolation
3. `llms.txt`
4. Page désamiantage — supprime d'elle-même le mauvais 301 ; bloquée tant que les références du certificat manquent
5. Worker : gestionnaires sitemap/robots, puis rattrapage 404 — sur décision d'Isuf

## Vérification après mise en ligne

```
/llms.txt        → « 34 avis », horaires complets, plus aucun « 8h–18h »
/contact         → une seule version des horaires sur la page
/isolation-thise → plus de « Qualification RGE »
(après intervention sur le Worker uniquement :)
/robots.txt      → une seule ligne Sitemap:
/sitemap.xml     → les 1 396 URL directement, plus d'index à 2 enfants
```
