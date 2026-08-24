# Correctif — les trois URL héritées du relevé du 23/08 redirigent, elles ne sont pas servies en 200

> Déclencheur : la vérification `docs/seo/verification-page-avec-redirection-2026-08-24.md`
> (fusionnée sur `main` en #44) établit que le site porte **645 redirections 301
> voulues** et renvoie de **vrais 404**. Cela contredisait ce que le relevé de
> citation IA du 23/08 avait conclu. Vérifié avant d'aller plus loin.
>
> Méthode : lecture du `_redirects` du dépôt de production
> `eurotregu/rushiti-renovation` (checkout du 24/08/2026), puis récupération
> serveur des URL en cache désactivé (`maxAge: 0`), en relevant l'URL finale et
> le code de statut — et pas seulement le contenu rendu.

## Ce que le relevé du 23/08 affirmait, et pourquoi c'était faux

Le relevé concluait à un **catch-all 200** : le site répondrait 200 sur des URL
héritées au lieu de 404/410, laissant « un espace d'URL infini ». Cette
conclusion venait d'une lecture du **contenu rendu** — la page affichée était
bien celle d'un autre service — sans contrôle de l'**URL finale** ni du **code
de statut**. Une redirection suivie et un catch-all produisent exactement le
même contenu à l'écran ; seuls l'URL finale et le statut les distinguent.

## Ce que la vérification établit

| URL demandée | URL finale | Statut final | Lecture |
|---|---|---|---|
| `/desamiantage-sol-besancon/` | `/revetements-sol-besancon` | 200 | Redirection |
| `/demolition-commerce-besancon/` | `/cloisons-besancon` | 200 | Redirection |
| `/organic-ehpad-besancon/` | `/platrerie-besancon` | 200 | Redirection |
| `/xyzzy-page-inexistante-test-claude/` (témoin, n'a jamais existé) | inchangée | **404** | Pas de catch-all |

L'URL témoin est la preuve décisive : une URL qui n'a jamais existé reçoit un
404 et la page « Page introuvable | RUSHITI Rénovation ». **Le site ne sert pas
de catch-all.** Les trois URL héritées relèvent des « anciennes URL WordPress
déjà redirigées volontairement » décrites par la vérification du 24/08.

**Conclusion : l'affirmation du 23/08 est retirée.** Il n'y a rien à corriger
sur ces trois URL, et la recommandation « poser un 404/410 » qui en découlait
est sans objet — un 301 vers la page de service utile vaut mieux qu'un 410.

## Ce qui reste vrai du constat initial

Les trois URL portent des libellés hors offre validée (désamiantage, démolition,
EHPAD) et ressortaient encore, le 23/08, dans les résultats de recherche sous la
marque avec ces anciens titres. C'est un fait d'index, pas un fait de serveur :
la redirection est en place, l'index met du temps à suivre. Rien à faire de plus
que laisser les 301 vivre. Le désamiantage étant une activité réglementée, si un
ancien titre restait visible plusieurs mois, l'arbitrage revient à Isuf.

## Ce qui n'a pas pu être établi

- **301 ou 302 ?** Le changement d'URL finale prouve la redirection, pas son
  code. Aucune règle ne porte ces trois URL dans le `_redirects` du dépôt de
  production, et le fichier ne contient aucun joker : la redirection est donc
  configurée **hors du dépôt**, au niveau Cloudflare. À confirmer par Isuf dans
  le tableau de bord, ou par un relevé d'en-têtes depuis un poste non filtré.
- L'environnement de cette session ne peut pas ouvrir de connexion directe vers
  les domaines RUSHITI ; toutes les récupérations passent par un service tiers
  côté serveur, qui suit les redirections sans exposer les sauts intermédiaires.

## Observations secondaires, datées du 24/08

- La page 404 est servie avec `robots: index, follow`. Sans effet pratique — un
  404 n'est pas indexé — mais `noindex` serait la valeur juste.
- Les cibles de redirection confirment deux écarts déjà relevés le 23/08 :
  `/platrerie-besancon` porte « devis sous 48 h » **dans son title**, et
  « 34 avis 4,7/5 » reste figé dans les meta descriptions.

---

*Vérification du 24/08/2026. Sources : `_redirects` du dépôt de production
`eurotregu/rushiti-renovation` (checkout réel) et récupération serveur des URL
en cache désactivé. Aucun chiffre inventé.*
