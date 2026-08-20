# Configuration Google Search Console — rushiti-renovation.fr

**Relevé en ligne du 20/08/2026.** Propriété concernée : `rushiti-renovation.fr`
(hébergée sur Cloudflare Pages). Une seule propriété par session : rushiti.fr se
pilote à l'identique, dans un document séparé.

Ce document contient deux choses :

1. **Un relevé factuel** de l'état réel de la configuration, mesuré en ligne le
   20/08/2026 — chaque constat est accompagné de sa preuve.
2. **Le mode d'emploi complet** de la configuration GSC, bloc par bloc, avec la
   checklist à cocher dans l'interface.

Rien ici n'est appliqué à la production. Les fichiers prêts à déployer sont dans
le même dossier (`robots.txt`). Les actions dans l'interface Search Console
demandent le compte Google d'Isuf : elles ne peuvent pas être automatisées.

---

## Partie 1 — Relevé de l'état réel (20/08/2026)

| Bloc | État | Détail mesuré |
|---|---|---|
| `robots.txt` | ✅ Conforme | HTTP 200, `text/plain`. `User-agent: * / Allow: /` — aucun robot bloqué, robots IA compris. Deux lignes `Sitemap:`. |
| `sitemap.xml` | ✅ Conforme | HTTP 200, `application/xml`. C'est un **index** valide qui déclare 2 sitemaps enfants, `lastmod` 2026-08-16. |
| `sitemap-pages.xml` | ✅ Conforme | **1 395 URL**, toutes sans slash final, chacune avec `lastmod`. Loin sous la limite de 50 000. |
| `sitemap-communes.xml` | 🔴 **Vide** | HTTP 200 mais `<urlset></urlset>` — **0 URL**. Déclaré deux fois (robots.txt + index). |
| Redirections des URL héritées | 🔴 **Hors sujet** | 4 URL présentes dans l'index Google redirigent vers des pages d'un autre sujet (détail ci-dessous). |
| `llms.txt` | ✅ Présent | HTTP 200, complet et à jour côté services. Une incohérence de chiffre (voir P1-A). |
| Vérification DNS, utilisateurs, GA4 | ⬜ Non vérifiable | Écrans privés de Search Console / Cloudflare — à cocher par Isuf en Partie 4. |

### Méthode

Relevé par récupération directe des fichiers en ligne le 20/08/2026, puis
comptage programmatique des balises `<loc>` du sitemap. Aucun chiffre n'est
estimé : `1 395` est un décompte, `0` est un décompte.

---

## Partie 2 — Les constats à corriger

### 🔴 P0-A · `sitemap-communes.xml` est vide et redondant

**Preuve.** Le fichier répond en 200 mais son contenu intégral est :

```xml
<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>
```

**Pourquoi ça compte.** Ce sitemap vide est annoncé à Google à deux endroits :
dans `robots.txt` et dans l'index `sitemap.xml`. Soumis dans Search Console, il
remontera « 0 URL détectée » — un statut qui ressemble à une panne et qui fait
perdre du temps à chaque check-up mensuel. Ce n'est pas une pénalité, c'est du
bruit permanent dans le tableau de bord.

**Et surtout : il ne manque rien.** Les pages communes **sont déjà** dans
`sitemap-pages.xml`. Vérifié par échantillon sur les 1 395 URL :

| URL testée | Présente dans `sitemap-pages.xml` |
|---|---|
| `/cloisons-battant` | oui |
| `/peinture-interieure-planoise` | oui |
| `/degat-des-eaux-beure` | oui |
| `/isolation-thise` | oui |

Structure réelle des 1 395 URL, décomptée :

- **1 368** pages prestation × lieu — **18 prestations × 76 lieux** exactement,
  quartiers de Besançon et communes du Doubs (chaque prestation couvre les mêmes
  76 lieux, sans trou) ;
- **27** autres pages : l'accueil, `/blog` et ses 10 articles, les pages de fond
  (`/a-propos`, `/contact`, `/realisations`, `/zones-intervention`,
  `/mentions-legales`) et les pages de conversion (`/simulateur-peinture`,
  `/renovation-syndic-gestionnaire-besancon`, `/devis-assurance-degat-des-eaux-besancon`,
  `/prix-travaux-renovation-besancon`, `/plaquiste-besancon`,
  `/renovation-appartement-besancon`, `/ravalement-facade-besancon`,
  `/amenagement-commerce-bureau-besancon`, `/remise-en-etat-logement-locatif-besancon`,
  `/peinture-facade-isolation-exterieure-besancon`).

**Correction recommandée : supprimer le sitemap communes**, puisque son contenu
est déjà couvert. Deux gestes, tous les deux côté Cloudflare Pages :

1. Retirer la ligne `Sitemap: https://rushiti-renovation.fr/sitemap-communes.xml`
   de `robots.txt` → fichier corrigé prêt à déployer : **`docs/gsc/robots.txt`**.
2. Retirer le bloc `<sitemap>` correspondant de l'index `sitemap.xml` :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://rushiti-renovation.fr/sitemap-pages.xml</loc>
    <lastmod>2026-08-16</lastmod>
  </sitemap>
</sitemapindex>
```

3. Puis, dans Search Console → Index → Sitemaps : supprimer l'entrée
   `sitemap-communes.xml` si elle y a déjà été soumise.

> **Variante si vous préférez le garder** (utile plus tard, si les pages communes
> devenaient trop nombreuses pour un seul fichier) : il faut alors le **remplir**
> et retirer les URL correspondantes de `sitemap-pages.xml` — une même URL ne doit
> pas figurer dans deux sitemaps. Tant qu'il reste vide, la première option est la
> bonne.

---

### 🔴 P0-B · Quatre URL héritées redirigent vers un sujet différent

Les quatre URL ci-dessous étaient observées dans l'index Google lors de l'audit
du 13/08/2026. Elles répondent aujourd'hui en 200 **après redirection**, mais
vers une page qui ne traite pas le même sujet :

| URL héritée (connue de Google) | Redirige vers | Le sujet correspond-il ? |
|---|---|---|
| `/enduit-chaux-besancon` | `/ratissage-enduit-besancon` | **Non** — l'enduit à la chaux est un enduit de façade/mur ancien, le ratissage est un enduit de lissage intérieur. Proche, mais ce n'est pas la même prestation. |
| `/peinture-plafond-batiment-besancon` | `/faux-plafonds-besancon` | **Non** — *peindre* un plafond ≠ *poser* un faux plafond. |
| `/desamiantage-sol-besancon` | `/revetements-sol-besancon` | **Non** — retrait d'amiante ≠ pose de revêtements. |
| `/organic-ehpad-besancon` | `/platrerie-besancon` | **Non** — EHPAD (secteur client) ≠ plâtrerie (prestation). Déjà signalé dans la PR #21. |

**Pourquoi ça compte.** Google traite une redirection vers un contenu sans
rapport comme un **soft 404** : la page de destination n'est pas créditée, et
l'URL d'origine sort de l'index en emportant l'historique qu'elle avait. C'est
exactement le type de ligne qui apparaîtra en « Page avec redirection » puis en
« Soft 404 » dans le rapport Index → Pages, et c'est la première chose qu'on
cherchera à expliquer au prochain check-up.

Aucune de ces quatre URL n'est dans le sitemap — normal pour des URL redirigées,
mais cela veut dire que le sitemap ne peut pas servir à les diagnostiquer :
elles ne se verront que dans le rapport d'indexation GSC.

**Correction — trois cas, une décision par ligne :**

1. **La prestation existe sous un autre nom** → rediriger vers la page qui traite
   *réellement* le même sujet. Pour `/peinture-plafond-batiment-besancon`, la
   cible juste est `/peinture-interieure-besancon` (murs, **plafonds**,
   boiseries), pas `/faux-plafonds-besancon`.
2. **La prestation n'existe pas / n'est pas proposée** → servir un **410 Gone**
   plutôt qu'une redirection trompeuse. C'est le cas de `/desamiantage-sol-besancon`
   si la réponse au point P0-B de l'audit du 13/08 (« l'entreprise détient-elle
   une certification amiante ? ») est non. `[À CONFIRMER par Isuf]`
3. **L'URL vaut la peine d'exister** → créer la page sur l'URL propre et rediriger.
   C'est le cas de `/organic-ehpad-besancon` → `/ehpad-besancon`, déjà tranché
   dans `docs/seo/corrections-audit-2026-08.md` (P1-A).

Ces règles se posent dans le mécanisme de redirection de la production
(fichier `_redirects` de Cloudflare Pages, ou le Worker si c'est lui qui gère les
routes — à vérifier au moment de poser, les deux existent sur ce site).

---

### 🟠 P1-A · Le nombre d'avis Google diverge selon la page

**Preuve, relevée le même jour sur la même production :**

| Source | Valeur affichée |
|---|---|
| `/llms.txt` | « Note 4,7/5 sur **29 avis** Google » |
| meta description de `/platrerie-besancon` | « 34 avis 4,7/5 » |
| meta description de `/isolation-besancon` | « 34 avis 4,7/5 » |
| meta description de `/peinture-interieure-besancon` | « 34 avis 4,7/5 » |
| meta description de `/revetements-sol-besancon` | « 34 avis 4,7/5 » |

La note (4,7/5) est cohérente partout ; c'est le **compteur** qui ne l'est pas.
Un des deux chiffres est périmé — vraisemblablement `llms.txt`, non régénéré
depuis la mise à jour des pages.

**Pourquoi ça compte ici.** Ce n'est pas un sujet de configuration GSC, mais
c'est le genre de contradiction qui fait qu'un moteur de réponse IA (ChatGPT,
Perplexity, l'Aperçu IA de Google) préfère ne pas citer de chiffre du tout, et
`llms.txt` est précisément le fichier écrit pour eux.

**Correction :** relever le compteur réel sur la fiche Google Business Profile,
puis aligner **toutes** les occurrences sur cette valeur. `[À CONFIRMER : chiffre
exact au jour de la correction]` — ne pas trancher entre 29 et 34 sans regarder
la fiche.

---

### 🟡 P2-A · `priority` et `changefreq` dans le sitemap

Les 1 395 entrées portent chacune un `priority` et un `changefreq`. Google
**ignore ces deux balises** depuis des années ; seul `lastmod` est lu, et
uniquement s'il est honnête. Aucun mal, mais c'est du poids inutile dans un
fichier déjà volumineux. À retirer à la prochaine régénération du sitemap, pas
avant : ce n'est pas une correction qui justifie un déploiement à elle seule.

---

## Partie 3 — La configuration, bloc par bloc

Les six blocs d'une configuration GSC propre. Les blocs 1, 2, 5 et 6 se font
dans l'interface (compte Google d'Isuf) ; les blocs 3 et 4 sont déjà en place et
n'ont besoin que des corrections de la Partie 2.

### Bloc 1 — Type de propriété : **Domaine**, pas « Préfixe d'URL »

Choisir la propriété **Domaine** (`rushiti-renovation.fr`, sans `https://`, sans
`www`). Elle couvre d'un seul coup `http` et `https`, `www` et non-`www`, et tous
les sous-domaines. Une propriété « Préfixe d'URL » ne couvre qu'une seule de ces
variantes : si le site répond aussi en `www`, la moitié des données part dans une
propriété que personne ne regarde.

**Vérification : enregistrement DNS TXT dans Cloudflare.**
Cloudflare → domaine `rushiti-renovation.fr` → DNS → Records → Add record :

| Champ | Valeur |
|---|---|
| Type | `TXT` |
| Name | `@` |
| Content | `google-site-verification=…` (valeur fournie par GSC à l'écran) |
| TTL | Auto |

Ne jamais supprimer cet enregistrement ensuite : Google le revérifie
périodiquement et retire la propriété s'il disparaît.

### Bloc 2 — Utilisateurs : Isuf **et** Yll, chacun sur son compte

Search Console → Paramètres → Utilisateurs et autorisations → Ajouter, niveau
**Propriétaire** pour les deux.

Deux comptes distincts, jamais un compte partagé : si le compte unique est perdu,
bloqué ou lié à une adresse qui n'existe plus, la propriété **et tout son
historique** partent avec — et l'historique GSC ne se reconstitue pas, il ne
remonte que 16 mois.

### Bloc 3 — Sitemaps : soumettre **l'index seul**

Search Console → Index → Sitemaps → soumettre exactement :

```
sitemap.xml
```

Une seule ligne. `sitemap.xml` est un index : Google suit tout seul les sitemaps
enfants qu'il déclare. Soumettre en plus `sitemap-pages.xml` créerait un doublon
de suivi sans rien apporter.

Statut attendu : « Réussite ». Le nombre d'URL découvertes doit converger vers
**1 395** (moins la correction P0-A, qui ne retire aucune URL réelle).

Re-soumettre un sitemap n'accélère rien. Il se soumet **une fois** ; ensuite il
se met à jour tout seul à chaque page ajoutée ou retirée, et `lastmod` fait le
reste.

### Bloc 4 — `robots.txt`

État actuel, relevé le 20/08/2026 — conforme, robots IA inclus :

```
User-agent: *
Allow: /

Sitemap: https://rushiti-renovation.fr/sitemap.xml
Sitemap: https://rushiti-renovation.fr/sitemap-communes.xml
```

Une seule modification à faire : retirer la seconde ligne `Sitemap:` (P0-A).
Fichier corrigé prêt à déployer : **`docs/gsc/robots.txt`**.

À ne pas faire : lister les robots IA un par un pour les « autoriser ».
`User-agent: * / Allow: /` les autorise déjà tous, et une liste explicite finit
toujours par être incomplète le jour où un nouveau robot apparaît.

### Bloc 5 — Liaison GA4

Search Console → Paramètres → Associations → Google Analytics.

**Prérequis non rempli à ce jour :** la propriété GA4 n'existe pas encore
(constat P1-B de l'audit du 13/08/2026, toujours ouvert — identifiant de mesure
`[À CRÉER]`). Ce bloc reste donc en attente ; il ne bloque aucun autre.

L'intérêt de la liaison, une fois GA4 en place : croiser la requête tapée et ce
qui s'est passé ensuite. Sans elle, GSC dit quelles requêtes amènent du trafic,
mais pas lesquelles amènent des **appels** — et pour un artisan, c'est l'appel
qui compte, pas la visite.

L'installation de GA4 elle-même (Consent Mode v2 derrière le même bandeau que le
Pixel Meta, événements `clic_telephone` / `envoi_formulaire` / `clic_email`)
appartient au skill `rushiti-ga4-gtm`, en session dédiée.

### Bloc 6 — Indexation d'une page neuve

À chaque publication (page locale, page service, article) :

1. Vérifier que la page répond en **200**, sans `noindex`, avec un canonical
   vers elle-même, et qu'elle est **liée depuis au moins une page existante**
   (une page orpheline s'indexe mal).
2. Vérifier qu'elle figure dans `sitemap-pages.xml`. Sinon : mettre à jour le
   sitemap **d'abord**.
3. GSC → Inspection d'URL → « Demander une indexation ». **Une fois suffit.**
4. Ne promettre aucun délai : l'indexation prend de quelques heures à quelques
   semaines et personne ne la maîtrise. Point de contrôle au check-up suivant.

---

## Partie 4 — Checklist d'exécution

À cocher par Isuf dans Search Console et Cloudflare. Les lignes ⬜ n'ont pas pu
être vérifiées depuis cette session : ce sont des écrans privés.

**Configuration**

- [ ] Propriété **Domaine** `rushiti-renovation.fr` créée (et non « Préfixe d'URL »)
- [ ] Enregistrement DNS TXT `google-site-verification=…` présent dans Cloudflare, statut « Validée »
- [ ] Isuf : accès **Propriétaire**
- [ ] Yll : accès **Propriétaire**, sur son propre compte Google
- [ ] `sitemap.xml` soumis (Index → Sitemaps), statut « Réussite »
- [ ] `sitemap-communes.xml` **retiré** de la liste des sitemaps soumis
- [ ] Le nombre d'URL découvertes est cohérent avec 1 395
- [ ] Sécurité et actions manuelles : « Aucun problème détecté » sur les deux écrans
- [ ] GA4 : propriété créée, puis associée *(en attente — voir Bloc 5)*

**Corrections de production à déployer** (Cloudflare Pages)

- [ ] P0-A — `robots.txt` sans la ligne `sitemap-communes.xml` (fichier fourni)
- [ ] P0-A — `sitemap.xml` sans le bloc `<sitemap>` communes
- [ ] P0-B — redirection de `/peinture-plafond-batiment-besancon` repointée vers `/peinture-interieure-besancon`
- [ ] P0-B — `/desamiantage-sol-besancon` : décision certification amiante, puis 410 ou page dédiée `[À CONFIRMER]`
- [ ] P0-B — `/organic-ehpad-besancon` : page `/ehpad-besancon` créée puis redirection repointée
- [ ] P0-B — `/enduit-chaux-besancon` : cible réellement équivalente, ou 410 `[À CONFIRMER]`
- [ ] P1-A — compteur d'avis aligné partout sur la valeur réelle de la fiche Google `[À CONFIRMER]`

**Après déploiement**

- [ ] Re-vérifier `robots.txt` et `sitemap.xml` en ligne (200, contenu attendu)
- [ ] Inspection d'URL sur une URL corrigée pour confirmer la nouvelle cible

---

## Partie 5 — Le check-up mensuel

La configuration n'est pas une fin : elle sert à ce que le check-up mensuel soit
lisible. Six passages, toujours dans cet ordre — le détail complet et les seuils
d'alerte sont dans le skill `rushiti-gsc` (Mode 2) :

| # | Écran | Ce qu'on cherche |
|---|---|---|
| 1 | Performance — Résultats de recherche | Requêtes métier **+ géo** en progression ou en chute. Écarter d'emblée le hors-zone : 2 000 impressions hors Doubs valent zéro chantier. |
| 2 | Index — Pages | Variation du nombre d'indexées, et les **motifs** d'exclusion. C'est là que P0-B se verra. |
| 3 | Expérience — Core Web Vitals | **Mobile d'abord.** « Pas assez de données » sur un petit site n'est ni bon ni mauvais signe. |
| 4 | Améliorations — Données structurées | Erreurs à corriger, avertissements à examiner sans urgence. |
| 5 | Liens | Nouveaux domaines référents, dont les suspects. |
| 6 | Sécurité et actions manuelles | Doit afficher « Aucun problème détecté ». Tout autre état passe **en tête** du rapport. |

Chaque signal détecté part vers le skill spécialiste (`rushiti-quick-wins-gsc`,
`rushiti-ctr-opportunites`, `rushiti-regression-seo`, `rushiti-indexation`,
`rushiti-cannibal-check`…) — une ligne de signalement, jamais une demi-analyse.

**Discipline d'export :** couvrir au moins 3 mois (le site a peu de volume, une
semaine ne prouve rien), noter la période exacte dans le nom du fichier, et ne
jamais comparer deux saisons sans le dire (ravalement au printemps, isolation à
l'automne).

---

## Ce qui n'a pas pu être vérifié dans cette session

À traiter à la prochaine occasion, ou par Isuf directement — ces points sont
ouverts, pas résolus :

1. **Écrans Search Console** (vérification, utilisateurs, sitemaps soumis,
   indexation, sécurité) : ils demandent le compte Google d'Isuf. Aucun outil ne
   peut les lire. Pour les traiter : captures d'écran ou export CSV.
2. **Enregistrement DNS TXT** dans Cloudflare : non lisible depuis cette session.
3. **Balise `google-site-verification` dans le HTML** : non observée sur les
   pages relevées, mais l'outil utilisé ne remonte pas les métabalises
   arbitraires — absence non prouvée. Sans importance si la vérification DNS est
   en place (elle est plus robuste).
4. **Canonicalisation `www` et `http`** : `https://www.rushiti-renovation.fr/`
   n'a pas pu être testée (service de relevé indisponible au moment du contrôle).
   À vérifier : elle doit rediriger en 301 vers la version sans `www`. La
   propriété Domaine du Bloc 1 protège des conséquences en cas d'oubli.
5. **Core Web Vitals** : non mesurés ici. Passage par PageSpeed Insights, skill
   `rushiti-audit-technique`.

---

*Relevé du 20/08/2026. Les constats sont datés : une production évolue, un
document ne se relit pas comme un état actuel six mois plus tard.*
