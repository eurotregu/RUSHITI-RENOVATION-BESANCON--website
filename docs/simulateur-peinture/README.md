# Bloc « Méthode de calcul » — /simulateur-peinture

## Pourquoi

La page `/simulateur-peinture` n'expose à Google qu'environ 125 mots : le formulaire
remplace le contenu de la question affichée à chaque étape au lieu de l'ajouter, donc
seule la question 1 existe dans le HTML servi. Résultat : `1 H1, 0 H2, 0 H3`.

La page Zolpan
(`zolpan.fr/expertises/tous-nos-conseils/preparation/calcul-pour-la-quantite-de-peinture`)
publie 629 mots statiques en `1 H1 + 2 H2 + 4 H3`. C'est elle qui capte la requête
informationnelle « comment calculer sa quantité de peinture ».

Ce bloc ajoute un contenu **permanent, visible sans cliquer** :
`+278 mots`, `+1 H2`, `+3 H3` → la page passe d'environ 125 à environ 400 mots indexables.

## Contenu

`bloc-methode-calcul.html` — HTML autonome, aucun CSS à ajouter.
Les classes utilisées (`section.soft`, `.wrap`, `.u55`, `.eyebrow`, `.lead`) existent
déjà dans la feuille de style de la page (vérifié dans le `<style>` servi).

Aucun prix n'y figure. Les chiffres cités ne sont pas nouveaux : ils sont repris tels
quels du calcul interne du simulateur (`js` de la page) —

| Valeur citée dans le bloc | Source dans le simulateur |
|---|---|
| −10 % pour portes et fenêtres | `* 0.9` |
| hauteurs 2,35 / 2,50 / 2,80 m | `basse` / `standard` / `haute` |
| ~10 m²/L par couche, 2 couches | `Math.ceil(surf / 5)` |

## Où le poser

Le HTML source du site est dans **`eurotregu/rushiti-renovation`, branche `main`**
(projet Cloudflare Pages `rushiti-renovation-git`, qui sert `rushiti-renovation.fr`).
Un push sur `main` redéploie automatiquement.

Dans le fichier de la page `/simulateur-peinture` : coller le contenu de
`bloc-methode-calcul.html` **juste avant `</main>`**, c'est-à-dire après la `</section>`
qui contient le simulateur et la ligne « Estimation indicative et gratuite… », et avant
`<footer class="site">`.

## Vérifier après déploiement

```
curl -s https://rushiti-renovation.fr/simulateur-peinture | grep -c "Comment calculer la quantité"   # attendu : 1
curl -s https://rushiti-renovation.fr/simulateur-peinture | grep -o "<h[23]" | sort | uniq -c        # attendu : 1 h2, 3 h3
```

Puis demander une réindexation de l'URL dans Google Search Console.

## Repli si la page n'est pas modifiable à la source

Le Worker `image-license-jsonld` réécrit déjà le HTML de cette page (il y remplace
`<title>` et les meta description). On peut y injecter le bloc de la même façon, dans
`corrigerContenu()`, à l'intérieur du `if (chemin === "/simulateur-peinture")` :

```js
if (html.indexOf("Comment calculer la quantité de peinture nécessaire") === -1) {
  html = html.replace(/<\/main>/, function () { return BLOC_METHODE_SIM + "</main>"; });
}
```

`BLOC_METHODE_SIM` étant une constante `template literal` contenant le fichier
`bloc-methode-calcul.html`, déclarée à côté de `TITRE_SIM` / `DESC_SIM`.

Attention : l'ancre est `</main>` et **pas** `</section></main>` — dans le HTML
réellement servi les deux balises sont séparées par un saut de ligne.
Ce repli a été testé à blanc sur le HTML de production (insertion unique, idempotente,
sans effet sur les autres pages), mais il reste moins propre que la correction à la
source : le bloc n'existerait alors que derrière le Worker.
