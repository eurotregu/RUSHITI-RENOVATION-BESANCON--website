# Formulaire « Demande rapide » — variante B (envoi Web3Forms)

> **Mise à jour du 22/08/2026.** Les trois questions laissées ouvertes en bas de ce
> document ont été tranchées et mises en œuvre (décision Isuf : « choisis le plus
> pratique et applique-le »). L'ancienne version `mailto` de ce document est
> **obsolète** : le formulaire est déployé en production sur les 30 pages pilier
> `-besancon` de rushiti-renovation.fr avec envoi **Web3Forms** (le même compte
> que la page `/contact`), et la copie GitHub Pages (`index.html` de ce dépôt)
> utilise désormais le même envoi.

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
