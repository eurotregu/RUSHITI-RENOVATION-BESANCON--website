# Protocole des mots-clés à exclure — pendant la campagne

> Rédigé le 31/08/2026. Complète `plan-google-ads-300-500e-2026-08-31.md`
> (section 8, routine mensuelle) et la liste `mots-cles-negatifs-google-ads.txt`.
> Brouillon soumis à validation d'Isuf. **Aucun réglage du compte Google Ads
> n'a été modifié** : ce document décrit où poser quoi, et quand.

La liste de 149 exclusions est le point de départ, pas le travail. Le travail,
c'est ce qui se passe pendant que la campagne tourne — et à 300–500 €/mois,
c'est le seul levier qui rapporte à coup sûr.

---

## 1. Trois niveaux, jamais mélangés

Google permet d'exclure à trois endroits. Se tromper de niveau est l'erreur
qui coûte le plus cher.

| Niveau | Ce qu'on y met | Exemple |
|---|---|---|
| **Liste partagée** (Bibliothèque partagée) | Ce qui n'est **jamais** un client, quelle que soit la campagne | `emploi`, `leroy merlin`, `plombier`, `maprimerenov` |
| **Campagne** | Ce qui ne concerne que cette campagne | une ville limitrophe qu'on décide de ne plus servir |
| **Groupe d'annonces** | L'aiguillage interne : envoyer la requête au bon groupe | `plaquiste` exclu du groupe Peintre |

### La règle d'or

**Un terme à exclure d'un seul groupe ne va jamais dans la liste partagée.**

Si vous mettez `placo` dans la liste partagée pour empêcher le groupe Peintre
de servir des requêtes placo, vous venez d'éteindre votre groupe Plaquiste.
La campagne continue de dépenser, les demandes s'arrêtent, et rien dans
l'interface ne vous signale la cause. C'est la panne la plus fréquente et la
plus difficile à voir après coup.

---

## 2. Le type de correspondance du négatif

| Type | Bloque | Usage |
|---|---|---|
| **Expression** `"emploi peintre"` | toute requête contenant ces mots **dans cet ordre** | **le défaut** — 90 % de vos exclusions |
| **Exact** `[peintre besançon avis]` | uniquement cette requête, mot pour mot | couper une requête précise qui a consommé sans convertir |
| **Large** `emploi peintre` | toute requête contenant **tous** ces mots, dans n'importe quel ordre | rare, et seulement avec preuve |

À l'import, choisissez **expression** pour la liste des 149. En large,
`emploi` bloquerait aussi « emploi du temps chantier ».

### Le piège numéro un : les négatifs ne suivent pas les variantes

Un mot-clé positif attrape automatiquement les pluriels, les fautes de frappe
et les variantes proches. **Un négatif, non.** Il bloque ce que vous avez
écrit, rien d'autre.

- `emploi` **ne bloque pas** « emplois »
- `tuto` **ne bloque pas** « tutos »
- `electricien` **ne bloque pas** « électricien »

C'est la raison pour laquelle une liste d'exclusions « propre » laisse quand
même filer de la dépense pendant des mois. La liste jointe contient déjà les
pluriels et les variantes sans accent des termes les plus exposés — mais
chaque nouveau négatif ajouté en cours de route doit passer le même contrôle :
**pluriel ? faute de frappe courante ? version sans accent ?**

---

## 3. Le rythme — trois phases

Le calendrier compte autant que la liste. À 13 €/jour, deux semaines sans
relevé, c'est un tiers du budget mensuel engagé à l'aveugle.

| Phase | Période | Fréquence du relevé |
|---|---|---|
| 1 — assainissement | semaines 1 et 2 | **tous les 2 ou 3 jours** |
| 2 — stabilisation | semaines 3 à 6 | hebdomadaire |
| 3 — entretien | à partir de la semaine 7 | mensuel, dans la routine de 30 min |

Chemin dans l'interface : Campagne → **Insights et rapports** → **Termes de
recherche**. Filtrer sur les 7 ou 30 derniers jours, trier par **coût
décroissant**. On lit toujours par le coût, jamais par le nombre
d'impressions : c'est l'argent qu'on cherche, pas le volume.

---

## 4. La table de décision, terme par terme

Pour chaque ligne du rapport :

| Ce que vous voyez | Ce que vous faites |
|---|---|
| Requête pertinente **qui a produit une demande de devis** | L'ajouter comme **mot-clé exact** dans le bon groupe. Elle est prouvée, elle mérite son enchère. |
| Requête pertinente, 1 ou 2 clics, aucune conversion | **Rien.** Trop tôt pour juger. |
| Requête pertinente, clics répétés, aucune conversion sur 60 jours | **Négatif exact**, pas expression. On coupe cette requête-là, pas sa famille. |
| Requête hors métier (plomberie, emploi, bricolage…) | **Négatif expression** sur le mot pivot, dans la **liste partagée**. |
| Requête qui appartient à un autre de vos groupes | **Négatif au niveau du groupe** qui l'a servie. Jamais campagne, jamais liste partagée. |
| Requête ambiguë | La noter, laisser tourner, revoir au relevé suivant. Une exclusion se retire mal. |

---

## 5. L'aiguillage entre vos trois groupes

Hiérarchie : **GA1 Dégât des eaux > GA2 Plaquiste > GA3 Peintre.**

Le dégât des eaux gagne toujours : c'est l'intention la plus urgente et la
page de destination est la plus adaptée (devis conforme à l'expert). Une
requête qui contient « dégât des eaux », « fuite » ou « après fuite » ne doit
jamais être servie par le groupe Peintre.

Bloc à poser en **négatif expression, au niveau des groupes GA2 et GA3** :

```
dégât des eaux
degat des eaux
dégâts des eaux
après fuite
apres fuite
infiltration
sinistre
```

Bloc à poser en **négatif expression, au niveau du groupe GA3 (Peintre)
uniquement** :

```
plaquiste
pose de cloison
faux plafond
doublage
```

Pour le reste, ne devancez pas le rapport : n'ajoutez un négatif de groupe
que le jour où une requête croisée apparaît réellement. Avec des mots-clés
positifs en exact et expression, les croisements sont rares.

---

## 6. Le garde-fou inverse : ne pas trop exclure

Une exclusion est invisible. Une impression bloquée n'apparaît dans aucun
rapport — vous ne saurez jamais ce que vous vous êtes coupé. À faible budget,
c'est le risque symétrique du gaspillage, et il est plus difficile à
diagnostiquer.

- **Un négatif large seulement si vous pouvez citer trois requêtes réelles
  qu'il bloque.** Sinon, expression.
- **Jamais un mot du métier seul** : `peinture`, `placo`, `sol`, `mur`,
  `plafond`, `rénovation`. Vous vous couperiez de tout.
- **Attention à `prix`, `tarif`, `devis`.** Ce sont des mots d'intention
  d'achat. « prix peinture m2 » est à exclure, mais « devis peinture
  besançon » est probablement votre meilleure requête. Donc négatif
  **expression** sur `prix peinture m2`, jamais négatif sur `prix` seul.
- **Ne jamais exclure `gratuit`** : « devis gratuit » est une requête client.
- **Ne jamais exclure un nom de quartier ou de commune du Doubs**, même
  inhabituel.

---

## 7. Ce que le rapport ne vous montrera pas

Google ne publie pas les termes de recherche qui n'atteignent pas ses seuils
de confidentialité. Une part de la dépense reste donc invisible, regroupée
sous une ligne « autres termes ». Ce n'est pas contournable et ça ne
s'exclut pas.

La seule parade est en amont, pas en aval : **des mots-clés positifs serrés**
(exact et expression, jamais large). Ajouter des négatifs ne récupère pas
cette part-là.

---

## 8. Comment on travaille ensemble pendant la campagne

Je n'ai pas d'accès au compte Google Ads : aucun connecteur Ads n'est
disponible dans nos sessions. Je ne peux donc rien poser moi-même, et il ne
faut pas compter dessus.

Le circuit qui fonctionne, à chaque relevé :

1. Vous exportez le rapport **Termes de recherche** en CSV (bouton
   téléchargement en haut à droite du rapport), sur la période du relevé.
2. Vous me le donnez dans une session.
3. Je vous rends trois blocs prêts à coller, séparés et étiquetés :
   - à ajouter à la **liste partagée**,
   - à ajouter au **groupe** X,
   - **nouveaux mots-clés positifs** à créer (les requêtes qui ont converti).
4. Vous collez, vous validez. Trois copier-coller, moins de cinq minutes.

Je garde aussi trace des exclusions posées dans
`mots-cles-negatifs-google-ads.txt`, avec la date, pour qu'on sache toujours
ce qui a été coupé et quand — ce que l'interface Google ne montre pas.

Pour que je puisse trier votre export, l'idéal est qu'il contienne au
minimum les colonnes : terme de recherche, type de correspondance, coût,
clics, conversions.
