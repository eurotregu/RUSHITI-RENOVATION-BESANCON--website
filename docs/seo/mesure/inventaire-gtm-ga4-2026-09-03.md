# Inventaire du conteneur GTM-KPM3GQB6 (relevé le 03/09/2026)

Source : script du conteneur servi par googletagmanager.com, lu tel quel (aucun accès au compte Tag Manager). Répond aux constats 2 et 21 de l'audit du 03/09.

| Élément | Valeur relevée |
|---|---|
| Google Analytics 4 | **G-QER2M5L3GL** — balise de configuration `__googtag` |
| Événements GA4 (`__gaawe`) | `click_phone`, `click_email`, `generate_lead`, `simulator_lead` |
| Condition de consentement | toutes les balises sont conditionnées à `analytics_storage` (Consent Mode v2) : rien n'est envoyé avant acceptation |
| Google Ads | aucun identifiant `AW-` ; les domaines googleadservices / doubleclick présents dans le script sont ceux de la bibliothèque GTM elle-même, pas d'une balise configurée |
| Meta, Hotjar, Clarity, Matomo | absents du conteneur (le Pixel Meta est chargé par le site lui-même, après consentement) |

## Conséquences appliquées (paquet 12, PR de production)

- Mentions légales, section 7 : Google Analytics 4 décrit (mesure d'audience, chargé par GTM, uniquement après consentement, événements listés).
- Bandeau de consentement : « cookies de mesure d'audience (Google Analytics) et de mesure publicitaire (Meta) ».

## Ce qui reste à faire, côté compte (Isuf)

1. Vérifier dans GA4 que les 4 événements arrivent bien et sont marqués comme **conversions** (`generate_lead`, `click_phone` au minimum).
2. Ajouter un événement `click_whatsapp` (lien `wa.me`) : le Pixel Meta le trace déjà, GA4 non.
3. Relier GA4 à la Search Console (rapport « Requêtes » dans GA4) : base du suivi mensuel `rushiti-revue-mensuelle`.
4. Durée de conservation des données GA4 : régler sur 14 mois (valeur maximale), sinon les comparaisons annuelles sont impossibles.
