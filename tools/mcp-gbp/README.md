# rushiti-mcp-gbp — relier Claude à la fiche Google Business Profile

Serveur MCP privé, hébergé sur Cloudflare Workers, qui donne à Claude (claude.ai,
Claude Code, Cowork) un accès direct à la fiche Google Business Profile de
RUSHITI Rénovation : fiche, avis, statistiques, requêtes de recherche, posts,
photos, questions-réponses.

Même principe que le connecteur « GOOGLE SEARCH CONSOLE » déjà présent dans
claude.ai : une URL, une connexion OAuth avec le compte Google propriétaire de
la fiche, et les outils apparaissent dans la conversation.

> **Rien n'est publié sans validation.** Les 15 outils sont en lecture seule,
> sauf quatre (`gbp_reply_review`, `gbp_create_post`, `gbp_answer_question`,
> `gbp_update_location`) qui exigent le paramètre `valide_par_isuf: true`.
> Claude ne doit le passer qu'après validation écrite du texte exact dans la
> conversation. Aucune suppression n'est possible depuis ce connecteur.

## 1. Ce qu'il faut côté Google (à faire par Isuf, une seule fois)

Google n'ouvre pas l'API Business Profile librement : il faut un projet Google
Cloud **approuvé**. Sans approbation, le quota est à 0 requête par minute et
toutes les requêtes échouent.

Conditions posées par Google (page « Prerequisites » des API Business Profile,
relevée le 04/09/2026) :

- une fiche vérifiée et active depuis plus de 60 jours ;
- un site web renseigné sur la fiche ;
- la demande faite avec une adresse Google **propriétaire ou gestionnaire** de la fiche.

Étapes :

1. **Créer un projet Google Cloud** : <https://console.cloud.google.com/> →
   « Nouveau projet », nom libre (ex. `rushiti-gbp`). Noter le **numéro de
   projet** (carte « Informations sur le projet » du tableau de bord).
2. **Demander l'accès à l'API** : formulaire
   <https://support.google.com/business/contact/api_default>, choisir
   « Application for Basic API Access », indiquer le numéro de projet, le site
   `https://rushiti-renovation.fr`, et l'usage (gestion de la fiche de sa propre
   entreprise). Délai de réponse : [À COMPLÉTER — Google ne s'engage pas].
   Vérification de l'approbation : dans « API et services → Quotas », le quota
   passe de 0 à 300 requêtes par minute.
3. **Activer les API** dans le projet (« API et services → Bibliothèque »),
   après approbation :
   - My Business Account Management API
   - My Business Business Information API
   - Business Profile Performance API
   - My Business Q&A API
   - Google My Business API (v4 : avis, posts, médias)
4. **Écran de consentement OAuth** (« API et services → Écran de consentement
   OAuth ») : type *Externe*, nom « RUSHITI Rénovation — Claude », e-mail de
   contact `contact@rushiti-renovation.fr`, périmètre
   `https://www.googleapis.com/auth/business.manage`. Passer l'application
   **en production** (bouton « Publier l'application ») : en mode test, Google
   révoque le refresh token au bout de 7 jours et il faudrait se reconnecter
   chaque semaine. Google affichera un avertissement « application non
   validée » à la première connexion, normal pour un usage interne ;
   la validation formelle par Google n'est pas nécessaire ici [À VÉRIFIER
   si Google l'exige pour ce périmètre au moment de la mise en place].
5. **Identifiants OAuth** (« API et services → Identifiants → Créer → ID client
   OAuth », type *Application Web*) :
   - Origine JavaScript autorisée : `https://rushiti-mcp-gbp.<sous-domaine>.workers.dev`
   - URI de redirection autorisé : `https://rushiti-mcp-gbp.<sous-domaine>.workers.dev/callback`

   Conserver l'ID client et le secret client : ils seront posés en secrets
   Cloudflare à l'étape suivante. Ne jamais les coller dans le dépôt.

Le `<sous-domaine>` est celui du compte Cloudflare (visible dans Workers &
Pages → Vue d'ensemble, à droite : `xxx.workers.dev`). Il est possible de
préparer les étapes 1, 2 et 4 avant même de déployer le Worker.

## 2. Déployer le Worker (Cloudflare)

Prérequis : Node 20+, un compte Cloudflare connecté (`npx wrangler login`).

```bash
cd tools/mcp-gbp
npm install

# Espace KV pour les états OAuth (une fois) :
npx wrangler kv namespace create OAUTH_KV
# → recopier l'« id » renvoyé dans wrangler.jsonc à la place de A_COMPLETER_ID_KV

# Secrets (chacun demande la valeur au clavier) :
npx wrangler secret put GOOGLE_CLIENT_ID
npx wrangler secret put GOOGLE_CLIENT_SECRET
npx wrangler secret put COOKIE_ENCRYPTION_KEY      # openssl rand -hex 32
npx wrangler secret put ALLOWED_EMAILS             # ex. isuf@…,yll@… (vide = tout le monde)

npm run check      # vérification TypeScript
npm run dry-run    # construction sans déploiement
npm run deploy     # mise en ligne
```

L'URL du serveur est affichée à la fin du déploiement :
`https://rushiti-mcp-gbp.<sous-domaine>.workers.dev`. Le point d'entrée MCP est
`/mcp`.

`ALLOWED_EMAILS` est la ceinture de sécurité : seuls ces comptes Google
peuvent terminer la connexion. Un tiers qui trouverait l'URL ne verrait de
toute façon que ses propres fiches (il s'authentifie avec son propre compte
Google), mais consommerait le quota du projet.

## 3. Brancher dans claude.ai

1. claude.ai → Paramètres → Connecteurs → « Ajouter un connecteur personnalisé ».
2. Nom : `Google Business Profile`. URL :
   `https://rushiti-mcp-gbp.<sous-domaine>.workers.dev/mcp`. Laisser vide
   l'ID client et le secret (le serveur gère l'enregistrement dynamique).
3. Cliquer « Connecter » : écran de consentement du Worker, puis connexion
   Google avec le compte propriétaire de la fiche. Accepter le périmètre
   « Gérer vos fiches d'établissement ».
4. Activer le connecteur dans la conversation (icône des outils). Tester avec :
   « Liste mes établissements Google Business » → `gbp_list_locations` doit
   renvoyer la fiche RUSHITI Rénovation, 18 rue du Professeur Haag.

Dans Claude Code (terminal) : `claude mcp add --transport http gbp
https://rushiti-mcp-gbp.<sous-domaine>.workers.dev/mcp`, puis `/mcp` pour
lancer l'authentification.

## 4. Outils exposés

| Outil | Lecture / écriture | Ce qu'il fait |
|---|---|---|
| `gbp_list_accounts` | lecture | Comptes Business Profile accessibles |
| `gbp_list_locations` | lecture | Fiches d'un compte ou de tous ; renvoie `name` et `v4Path` |
| `gbp_get_location` | lecture | Fiche complète : NAP, description, horaires, catégories, services |
| `gbp_get_google_updates` | lecture | Modifications appliquées ou suggérées par Google |
| `gbp_update_location` | **écriture** | Corrige des champs (description, site, horaires…) ; `validateOnly` d'abord |
| `gbp_list_reviews` | lecture | Avis, note moyenne, total ; filtre « sans réponse » |
| `gbp_get_review` | lecture | Un avis |
| `gbp_reply_review` | **écriture** | Publie la réponse validée à un avis |
| `gbp_performance` | lecture | Impressions Maps/Recherche, appels, clics site, itinéraires, par période |
| `gbp_search_keywords` | lecture | Requêtes ayant affiché la fiche, par mois |
| `gbp_list_posts` | lecture | Posts publiés |
| `gbp_create_post` | **écriture** | Publie un post « Nouveautés » validé |
| `gbp_list_media` | lecture | Photos et vidéos, vues |
| `gbp_list_questions` | lecture | Questions-réponses publiques |
| `gbp_answer_question` | **écriture** | Publie la réponse validée à une question |

Les outils d'écriture refusent tout appel sans `valide_par_isuf: true`.

## 5. Skills qui en tirent parti

- `rushiti-fiche-google-business` : description, services, posts → lecture
  de l'existant avec `gbp_get_location`, `gbp_list_posts`.
- `rushiti-avis-google` : brouillon de réponse à partir de
  `gbp_list_reviews` (`sansReponseSeulement: true`), publication avec
  `gbp_reply_review` après validation.
- `rushiti-faits-marque`, `rushiti-seo-local` : contrôle NAP et horaires de
  la fiche face au site (`gbp_get_location`).
- `rushiti-lundi-matin`, `rushiti-revue-mensuelle` : `gbp_performance` et
  `gbp_search_keywords` à côté des exports Search Console.
- `rushiti-keyword-map` : requêtes GBP à rapprocher du registre
  `docs/seo/regjistri-fjale-kyce.csv`.

## 6. Points d'attention

- **Le dépôt est publié tel quel** (GitHub Pages et Cloudflare Pages servent
  tout le dépôt) : ce dossier est donc lisible en ligne. Il ne contient aucun
  secret ; les identifiants vivent uniquement dans les secrets Cloudflare.
  `node_modules/`, `.wrangler/` et `.dev.vars` sont ignorés par Git.
- **Données de performance** : Google fournit environ 18 mois d'historique,
  avec 2 à 3 jours de décalage. Aucune donnée n'est stockée par le Worker.
- **Refresh token** : conservé chiffré dans le jeton remis à claude.ai
  (mécanisme de la bibliothèque `@cloudflare/workers-oauth-provider`). Pour
  couper l'accès : retirer l'application dans
  <https://myaccount.google.com/permissions> ou supprimer le connecteur dans
  claude.ai.
- **Mise à jour du modèle amont** : `src/workers-oauth-utils.ts` est copié tel
  quel du modèle Cloudflare `cloudflare/ai/demos/remote-mcp-google-oauth`
  (licence MIT) ; `src/google-handler.ts` et `src/utils.ts` en sont adaptés.
- **Ce que le connecteur ne fait pas** : supprimer un avis, une réponse, un
  post ou une photo ; téléverser une photo (l'API v4 le permet, volontairement
  non exposé : passer par l'interface Google avec l'accord RGPD du client).

## 7. Développement local

```bash
cp .dev.vars.example .dev.vars   # puis remplir
npm run dev                      # http://localhost:8788/mcp
npx @modelcontextprotocol/inspector   # pour tester les outils
```

En local, ajouter `http://localhost:8788/callback` aux URI de redirection de
l'ID client OAuth Google.
