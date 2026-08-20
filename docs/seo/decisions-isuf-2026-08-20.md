# Décisions d'Isuf du 20/08/2026 — corrections à poser

Quatre points restés ouverts depuis l'audit du 13/08 et la PR #21 ont été
tranchés par Isuf le 20/08/2026. Ce document enregistre chaque décision et la
traduit en correction exacte, avec les chaînes relevées en ligne le même jour.

Rien n'est appliqué ici : la production tourne sur **Cloudflare Pages**, ce dépôt
est la copie GitHub Pages en `noindex`. Chaque correction se pose côté hébergeur.

| # | Point | Décision d'Isuf | Portée mesurée |
|---|---|---|---|
| D1 | Certification amiante | **Détenue** — certificat désamiantage | 1 URL à rouvrir, aujourd'hui redirigée |
| D2 | Compteur d'avis Google | **34** | 1 fichier (`llms.txt`) |
| D3 | Horaires | **Version du pied de page** | `/contact`, `llms.txt`, JSON-LD, fiche Google |
| D4 | « Qualification RGE » | **Retirée** | **152 pages** + 2 PR ouvertes |

---

## D1 · Amiante : la certification est détenue → la page doit exister

**Décision.** RUSHITI détient un certificat de désamiantage. La page n'est donc
ni à supprimer (410) ni à repositionner en « après désamiantage » : elle doit
exister et porter la prestation réelle.

**État actuel — le contraire de ce que la décision implique.** Relevé le
20/08/2026 : `https://rushiti-renovation.fr/desamiantage-sol-besancon` répond en
200 **après redirection** vers `/revetements-sol-besancon`, une page qui parle de
parquet, stratifié, PVC et ragréage. Une prestation certifiée n'a donc aucune
page à elle, et l'URL que Google connaît envoie vers un autre sujet.

Deux dégâts distincts :

1. **SEO** — Google traite une redirection vers un contenu sans rapport comme un
   soft 404 : l'URL sort de l'index avec son historique (constat P0-B du dossier
   `docs/gsc/`).
2. **Commercial** — le désamiantage est la prestation la plus difficile à
   obtenir et la moins concurrencée du lot. C'est la seule des quatre décisions
   qui fait perdre du chiffre d'affaires, pas seulement des positions.

**Correction.**

1. ~~Supprimer la règle de redirection~~ — **correction du 20/08 (soir) : il
   n'y a aucune règle.** Le fichier `desamiantage-sol-besancon.html` n'existe
   pas dans le dépôt de production, donc l'URL répond 404, et le Worker
   rattrape tous les 404 avec un devineur par mots-clés qui renvoie un 301 vers
   la première correspondance — ici « sol ». Publier la page fait donc
   disparaître le mauvais 301 **sans toucher au Worker**.
2. Publier une vraie page sur cette URL.
3. Ajouter la prestation au méga-menu et au `sitemap-pages.xml` (elle n'y figure
   pas aujourd'hui : vérifié sur les 1 395 URL).

**Avant toute publication — informations à fournir par Isuf.**
La mention d'une certification amiante est une allégation réglementée : un
assureur, un syndic ou un expert la vérifie, et un moteur de réponse IA ne cite
une page de ce type que si l'affirmation est traçable. Elle ne peut donc pas être
écrite sans ses références. À compléter :

| Donnée | Valeur |
|---|---|
| Périmètre | `[À COMPLÉTER : SS3 (retrait) ou SS4 (interventions sur matériaux amiantés) ?]` |
| Organisme certificateur | `[À COMPLÉTER]` |
| Numéro de certificat | `[À COMPLÉTER]` |
| Date de validité | `[À COMPLÉTER]` |

Ces quatre valeurs conditionnent aussi le **contenu** de la page : SS3 et SS4 ne
recouvrent pas les mêmes travaux, et une page qui promet du retrait alors que la
certification ne couvre que la SS4 est un problème bien plus grave qu'une erreur
SEO. La rédaction est prête à démarrer dès qu'elles sont connues — pas avant.

---

## D2 · Avis Google : 34

**Décision.** Le compteur réel est **34**. Les pages ont raison, `llms.txt` est
périmé.

**Correction — un seul remplacement, dans `/llms.txt` :**

```
- Note 4,7/5 sur 29 avis Google.
+ Note 4,7/5 sur 34 avis Google.
```

```
- Avis : 4,7/5 sur 29 avis Google
+ Avis : 4,7/5 sur 34 avis Google
```

Les deux occurrences sont dans le même fichier (préambule et bloc « Coordonnées
et informations vérifiées »). Aucune page HTML n'est à modifier : `34 avis 4,7/5`
y est déjà correct — vérifié sur `/platrerie-besancon`, `/isolation-besancon`,
`/peinture-interieure-besancon`, `/revetements-sol-besancon`, et sur le bloc
d'avis visible de `/isolation-besancon` (« 4,7 / 5 ★★★★★ · 34 avis Google »).

> Ce chiffre bouge à chaque nouvel avis. Le remettre à jour à chaque campagne
> d'avis, sinon la même divergence réapparaît dans six mois.

---

## D3 · Horaires : la version du pied de page fait foi

**Décision.** La version affichée dans le pied de page est la bonne :

```
Lun – Ven : 7h – 20h30 · Sam : 8h – 20h30 · Dim : 9h – 17h30
```

Relevé complet le 20/08/2026 — le pied de page donne bien les trois lignes, y
compris samedi et dimanche. Il n'y a donc plus de zone d'ombre sur le week-end.

**La contradiction est interne à `/contact`.** Cette page affiche les deux
versions à la fois, à quelques centaines de pixels d'écart :

| Emplacement | Texte servi |
|---|---|
| Bloc « Horaires » de `/contact` | `Horaires — Lundi – Vendredi : 8h – 18h` ❌ |
| Pied de page de `/contact` | `Lun – Ven : 7h – 20h30 · Sam : 8h – 20h30 · Dim : 9h – 17h30` ✅ |

**Corrections, dans l'ordre de gravité :**

1. **`/contact`, bloc « Horaires »** — remplacer `Lundi – Vendredi : 8h – 18h`
   par les trois lignes du pied de page. C'est la seule correction visible par un
   client sur le point d'appeler : aujourd'hui la page lui dit qu'on est fermé à
   18h30 alors qu'on décroche jusqu'à 20h30.
2. **`/llms.txt`** — `Horaires : du lundi au vendredi, 8h–18h` → la version
   complète. C'est le fichier écrit pour les moteurs de réponse IA : tant qu'il
   dit 8h–18h, c'est cette réponse-là que ChatGPT ou Perplexity donneront.
3. **JSON-LD `openingHoursSpecification`** — aligner sur :

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

4. **Fiche Google Business Profile** — mêmes horaires. C'est elle qui alimente le
   « Ouvert · Ferme à … » affiché dans Google Maps et dans le pack local ; une
   fiche qui dit fermé pendant que le site dit ouvert coûte des appels le soir et
   le week-end, quand la concurrence ne répond pas.

**Note sur la copie de ce dépôt.** `index.html` porte une **troisième** version,
différente des deux autres : `Lun - Ven : 7h30 - 18h` / `Sam : 8h - 12h`
(ligne 544), et un `openingHoursSpecification` en `07:30–18:00` + samedi
`08:00–12:00` (lignes 36-49). Elle n'est pas servie au public (copie en
`noindex`) mais elle sert de gabarit : à corriger au même passage, et la PR #21
ne la traite pas — elle range les horaires parmi les points à décider.

---

## D4 · « Qualification RGE » : retirée — et c'est 152 pages, pas une

**Décision.** La mention est retirée du site.

**La portée réelle est beaucoup plus large que ce qui avait été annoncé.** La
PR #21 indique la mention « affichée sur `/isolation-besancon` uniquement ». C'est
inexact : elle est dans le **gabarit** des pages isolation. Vérifié en ligne le
20/08/2026, badge de confiance identique mot pour mot :

| URL testée | Badge servi |
|---|---|
| `/isolation-besancon` | « 20 ans d'expérience · Diagnostic gratuit sur site · Travaux selon DTU 25.41 · Artisan local · **Qualification RGE** » |
| `/isolation-thise` | idem |
| `/isolation-interieure-besancon` | idem |
| `/peinture-interieure-besancon` | *aucune mention* (page témoin, autre gabarit) |

Deux familles de pages sont donc concernées, chacune déclinée sur les 76 lieux
du sitemap : `isolation-{lieu}` et `isolation-interieure-{lieu}`, soit
**152 pages**. Une correction page par page n'a aucun sens ici : c'est **une
chaîne du générateur** à retirer, exactement comme les fautes de français
relevées dans la PR #21.

**Correction.** Retirer l'élément `Qualification RGE` de la liste de badges du
gabarit isolation, puis regénérer. Ne rien mettre à la place : les quatre autres
badges (20 ans, diagnostic gratuit, DTU 25.41, artisan local) sont vrais et
suffisent. Contrôle après déploiement : `Qualification RGE` ne doit plus
apparaître sur `/isolation-besancon` **ni** sur deux pages commune tirées au
hasard.

### ⚠️ Deux PR ouvertes contredisent cette décision

**PR #21 — la retire, mais sous-estime la portée.** Elle supprime « Certifié
RGE » de `index.html` (copie du dépôt) et signale la mention de production comme
« à confirmer ou à retirer ». Bon réflexe, périmètre incomplet : la corriger avec
les 152 pages en tête.

**PR #19 — la réintroduit.** C'est le point à traiter avant toute fusion. La
PR #19 enregistre la décision **inverse**, datée : « RGE : confirmé par Isuf
(14/08/2026) — utilisable dans les textes ». Neuf occurrences, trois fichiers :

| Fichier | Ce qu'il contient |
|---|---|
| `.claude/skills/rushiti-copywriting/SKILL.md` | RGE inscrit dans la **source de vérité** du skill de rédaction — donc réutilisé par tout texte écrit ensuite |
| `docs/prompts/creation-skill-copywriting.md` | « Certification : RGE — confirmé par Isuf (14/08/2026) » |
| `peinture-interieure-besancon.html` | Badge visible « **Certifié RGE** — Reconnu Garant de l'Environnement », **plus** la même affirmation dans une réponse de FAQ **et dans le JSON-LD `FAQPage`** |

Le cas du JSON-LD est le plus gênant : une affirmation retirée du texte visible
mais laissée dans les données structurées reste lue par Google et par les moteurs
de réponse IA.

**À faire avant de fusionner #19 :** retirer les neuf occurrences, et remplacer
la ligne de la source de vérité du skill par une mention explicite du
revirement — sinon la prochaine page rédigée avec ce skill remettra RGE toute
seule. Une décision du 14/08 annulée le 20/08 doit être écrite comme telle, pas
simplement effacée.

---

## Ordre d'exécution proposé

| Ordre | Action | Où | Pourquoi en premier |
|---|---|---|---|
| 1 | Horaires de `/contact` | Production | Un client qui lit « fermé à 18h » n'appelle pas à 19h |
| 2 | Retrait RGE du gabarit isolation (152 pages) | Production | Allégation réglementée, retirée par décision |
| 3 | Nettoyage RGE dans la PR #19 | Dépôt | Sinon la fusion la republie, JSON-LD compris |
| 4 | `llms.txt` : avis 34 + horaires | Production | Le fichier que lisent les moteurs IA |
| 5 | JSON-LD horaires + fiche Google | Production / GBP | Cohérence du pack local |
| 6 | Page désamiantage | Production | Bloqué tant que les références du certificat manquent |

Les actions 1, 2, 4 et 5 ne demandent aucune information supplémentaire : elles
sont prêtes à poser. L'action 6 attend les quatre valeurs du tableau D1.

---

*Décisions prises par Isuf le 20/08/2026. Chaînes de production relevées en ligne
le même jour ; les portées (152 pages, 1 395 URL du sitemap) sont des décomptes,
pas des estimations.*
