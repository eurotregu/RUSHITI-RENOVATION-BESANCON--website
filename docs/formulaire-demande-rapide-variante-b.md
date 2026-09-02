# Formulaire « Demande rapide » — variante B (envoi Web3Forms)

> **Mise à jour du 22/08/2026.** Les trois questions laissées ouvertes en bas de ce
> document ont été tranchées et mises en œuvre (décision Isuf : « choisis le plus
> pratique et applique-le »). L'ancienne version `mailto` de ce document est
> **obsolète** : le formulaire est déployé en production sur les 30 pages pilier
> `-besancon` de rushiti-renovation.fr avec envoi **Web3Forms** (le même compte
> que la page `/contact`), et la copie GitHub Pages (`index.html` de ce dépôt)
> utilise désormais le même envoi.

## Mise à jour du 02/09/2026 — protection anti-robot hCaptcha

### Ce qui s'est passé

Le 02/09/2026 entre 21h23 et 21h24, le formulaire de
`/peinture-interieure-besancon` a reçu **17 soumissions automatiques** en une
minute : Nom / Tél / E-mail / Message vides, et dans le champ `consentement`
des charges d'injection SQL (`oui' UNION ALL SELECT NULL,…`) à la place de
« oui ». C'est un balayage générique de vulnérabilités, pas une attaque ciblée,
et il ne pouvait rien atteindre : le formulaire poste chez Web3Forms, aucune
base de données ne se trouve derrière. Les 17 e-mails ont été classés en spam.

Le honeypot `botcheck` n'a rien filtré : un scanner de ce type ne coche pas
une case cachée, il rejoue le formulaire tel quel en mutant un champ à la
fois. Le piège ne protège que des robots qui remplissent tout.

### Ce qui est ajouté (31 formulaires : 30 pages pilier + `/contact`)

Web3Forms fournit un hCaptcha « zéro configuration » : pas de clé à créer, pas
de compte hCaptcha, la clé de site partagée du plan gratuit est injectée par
leur script. Trois lignes par page, posées par
`docs/seo/korrigjime-prodhim/fix_hcaptcha_formular.py` (idempotent, testé
sur les 31 pages réelles : 31 modifications, 0 erreur, second passage
0 modification) :

1. le widget, juste avant le bouton « Envoyer ma demande » :
   `<div class="h-captcha" data-captcha="true" data-lang="fr"></div>` ;
2. le script Web3Forms avant `</body>` :
   `<script src="https://web3forms.com/client/script.js" async defer></script>` ;
3. un contrôle inline (même endroit) : case non cochée → l'envoi est bloqué
   et un message en français s'affiche sous le widget, au lieu de la page
   d'erreur anglaise de Web3Forms. Si le script a été bloqué (extension,
   réseau), le contrôle se retire et le POST natif part comme avant : c'est
   Web3Forms qui tranche côté serveur.

`verifiko_demande_rapide.py` contrôle désormais les trois éléments sur les
30 pages pilier et sur `/contact`. La copie GitHub Pages (`index.html`,
`js/main.js`, `css/style.css` de ce dépôt) reçoit la même protection.

### Ce qui reste à faire par Isuf — indispensable

- **Activer hCaptcha dans le tableau de bord Web3Forms**
  (app.web3forms.com → formulaire portant la clé `1aee0248-…` → protection
  anti-spam → hCaptcha). Sans cette activation, le widget s'affiche mais une
  soumission sans captcha passe encore. Le déploiement du code peut précéder
  l'activation (le widget est alors inoffensif), l'inverse est à éviter : une
  activation sans widget bloquerait tous les envois.
- **`/simulateur-peinture`** utilise la même clé mais poste en `fetch` JSON,
  sans widget. Une fois hCaptcha activé sur la clé, Web3Forms refusera ses
  envois et le simulateur basculera sur son repli `mailto:` existant
  (demande non perdue, mais dépendante de la messagerie du visiteur). À
  traiter séparément : widget rendu explicitement dans le formulaire
  construit en JavaScript, ou clé Web3Forms distincte pour le simulateur.
  [À COMPLÉTER : décision]
- **Mentions légales** : ajouter hCaptcha (Intuition Machines, Inc.) comme
  sous-traitant du formulaire, à côté de Web3Forms. [À COMPLÉTER]
- Si hCaptcha se révèle trop pénible pour les clients (les énigmes du plan
  gratuit sont parfois laborieuses), l'alternative documentée par Web3Forms
  est Cloudflare Turnstile — réservée à leur offre payante.

## État déployé (production — dépôt `eurotregu/rushiti-renovation`)

Chaque page pilier `-besancon` porte une section `<section class="soft"
id="demande-rapide">` avec :

- formulaire en **POST natif** vers `https://api.web3forms.com/submit`
  (fonctionne même sans JavaScript) ;
- `access_key` du compte Web3Forms existant (identique à `/contact`) ;
- `subject` propre à la page : `Demande rapide — <Service> — rushiti-renovation.fr` ;
- champ caché `page` avec l'URL de la page (attribution précise de chaque lead) ;
- redirection vers `https://rushiti-renovation.fr/merci` après envoi ;
- honeypot `botcheck` (case cachée : cochée = robot, Web3Forms ignore l'envoi) ;
- depuis le 02/09/2026 : widget hCaptcha avant le bouton + script Web3Forms
  et contrôle inline avant `</body>` (voir la mise à jour ci-dessus) ;
- phrase de consentement RGPD avec lien vers `/mentions-legales` ;
- service pré-sélectionné selon la page (liste identique à `/contact`).

Le CSS global du site ne contenait aucune règle pour `label / input / select /
textarea / .form-grid` : la mise en forme (grille 2 colonnes, focus, case de
consentement, bandeau de réassurance) arrive par la **PR #10** du dépôt de
production (`assets/css/s971fb819.css`, cache-buster `?v=8`), complétée par la
**PR #20** (champ `page`, formulaire prix-travaux, mentions légales, validité).

## Pour poser le formulaire sur une nouvelle page

Ne pas repartir de ce document : **copier la section `id="demande-rapide"`
d'une page pilier existante** (par ex. `toile-de-verre-besancon.html` — les
styles viennent de la feuille globale depuis la PR #10), puis adapter trois
choses :

1. `subject` : `Demande rapide — <Service ou objet> — rushiti-renovation.fr` ;
2. champ caché `page` : l'URL exacte de la nouvelle page ;
3. l'`<option selected>` du service + le `<h2>` (« Demande rapide : décrivez … »).

Les scripts `docs/seo/korrigjime-prodhim/korrigjo_formulare_prodhim.py`
(complétion idempotente) et `verifiko_demande_rapide.py` (régression : structure,
clé, subject, champ page — à lancer avant chaque déploiement) automatisent et
contrôlent l'ensemble.

## Décisions prises le 21–22/08/2026 (anciennement « À décider »)

1. **Envoi par messagerie ou par serveur → serveur (Web3Forms).** Le POST natif
   part directement chez Web3Forms qui achemine l'e-mail à
   `contact@rushiti-renovation.fr` : plus aucune demande perdue si le visiteur
   n'a pas de messagerie configurée, accusé visuel via la page `/merci`, et zéro
   dépendance JavaScript. Le compte existait déjà (page `/contact`) — aucun
   nouveau prestataire, aucune activation nécessaire.
2. **Mentions légales.** La page `/mentions-legales` existait déjà et couvrait
   l'essentiel. Complétée le 22/08 : Web3Forms déclaré comme sous-traitant RGPD,
   droits complétés (effacement, opposition, portabilité, réclamation CNIL),
   et la section 7 « Cookies » réécrite — elle affirmait « pas de cookies, pas
   de consentement requis » alors que le site charge le Pixel Meta après
   consentement (bandeau Accepter/Refuser). Le doublon de section en bas de
   page a été supprimé.
3. **Suivi des conversions.** Trois niveaux, sans nouveau traceur :
   - chaque envoi = un e-mail reçu (comptable, avec service en objet et page
     d'origine dans le corps) + compteur du tableau de bord Web3Forms ;
   - la page `/merci` déclenche désormais `fbq('track','Lead',
     {content_name:'formulaire'})` — uniquement si le consentement cookies a été
     donné. C'était le trou principal : aucun envoi de formulaire n'était compté
     côté Meta (seuls les clics « devis » l'étaient) ;
   - les clics téléphone (`Contact`) et clics devis (`Lead / devis`) existants
     sont conservés tels quels.
