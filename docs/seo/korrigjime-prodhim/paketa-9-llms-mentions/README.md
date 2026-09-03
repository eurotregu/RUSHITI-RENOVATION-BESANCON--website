# Paketa 9 — `llms.txt` + `mentions-legales.html` (03/09/2026)

| | |
|---|---|
| Déclencheur | Isuf, 03/09 : « po: korrigjoje llms.txt dhe mentions legales » (constats 1 et 2 de `docs/seo/audit-premium-site-2026-09-03.md`) |
| Dépôt cible | `eurotregu/rushiti-renovation` (production, Cloudflare Pages) — **pas ce dépôt**. L'accès `add_repo` a été refusé par le contrôleur de permissions de la session : le paquet est donc livré ici, prêt à appliquer. |
| Statut | **Appliqué en production le 03/09 dans la PR [#39](https://github.com/eurotregu/rushiti-renovation/pull/39)** (brouillon à valider par Isuf). Deux points restent marqués `[À VÉRIFIER]` en commentaire HTML (voir § 3). |

## 1. Ce qui est corrigé

### `llms.txt` (remplacement intégral)

| Ligne servie le 03/09 | Correction | Source |
|---|---|---|
| « Raison sociale : RUSHITI Rénovation » | « Nom commercial : RUSHITI Rénovation » + « Dénomination sociale : Rushiti — SARL au capital de 1 000 €, RCS Besançon 905 214 631 » | socle v4, instructions complètes |
| « Note 4,7/5 sur 29 avis Google » (2 fois) | « 4,7/5 sur 34 avis Google (relevé le 22/08/2026) » + lien fiche | `avis-google-releve-2026-08-22.md`, accueil |
| « Horaires : du lundi au vendredi, 8h–18h » | « lundi au vendredi 7h–20h30 · samedi 8h–20h30 · dimanche 9h–17h30 » | pied de page et JSON-LD de toutes les pages |
| absent | TVA intracommunautaire, assurance ERGO (attestation sur demande, sans numéro), clients cibles, section « Ce que l'entreprise ne fait pas » (plomberie, électricité, recherche de fuite, amiante) | mentions légales, pages dégât des eaux et entreprise |
| absent | Pages plaquiste, entreprise de rénovation, rénovation de pièces, 5 pages professionnelles, page prix, mentions légales | sitemap |
| absent | Les 2 articles de blog non listés (plafond dégât des eaux, rouleaux de papier peint) ; DTU 59.1 / 25.41 / 53.12 | blog, `dtu-referencat-eeat.md` |
| absent | « Dernière mise à jour : 03/09/2026 » | — |

Aucun prix, délai ni certification ajouté. Le « sous 24 à 48 h ouvrées » repris en contact est celui de `/merci`.

### `mentions-legales.html` (6 remplacements ciblés, idempotents)

| Section | Avant | Après |
|---|---|---|
| Chapeau | « …et à l'entreprise RUSHITI Rénovation » | « …et à la SARL Rushiti, exerçant sous le nom commercial RUSHITI Rénovation » |
| 1. Éditeur | « RUSHITI Rénovation — Forme juridique : SARL » | « Rushiti, SARL au capital de 1 000 €, exerçant sous le nom commercial RUSHITI Rénovation — RCS Besançon 905 214 631 » (SIRET, TVA, coordonnées inchangés) |
| 2. Directeur de la publication | « représentant légal de RUSHITI Rénovation » | « co-gérant, représentant légal de la SARL Rushiti (RUSHITI Rénovation) » |
| 3. Hébergement | « hébergé par RUSHITI Rénovation — 18 rue du Professeur Haag » | Cloudflare, Inc. (Cloudflare Pages), adresse et site ; mention du dépôt GitHub |
| 7. Cookies | « un seul traceur : le Pixel Meta … aucun autre cookie de suivi ni de mesure d'audience » | trois outils décrits : Pixel Meta (après consentement), Google Tag Manager (gestionnaire de balises, Consent Mode v2), Cloudflare Web Analytics (sans cookie) ; renvoi au lien « Gérer mes cookies » |
| Pied | « Dernière mise à jour : août 2026 » | « septembre 2026 » |

Sections 4, 5, 6, 8, 9 inchangées.

## 2. Fichiers

| Fichier | Rôle |
|---|---|
| `llms.txt` | Version corrigée complète, à copier telle quelle à la racine de la production |
| `mentions-legales-main.html` | Le bloc `<main>…</main>` corrigé, pour un copier-coller manuel si le script n'est pas utilisé |
| `fix_llms_mentions.py` | Applique les deux corrections sur un checkout de la production (`--apply`), simulation par défaut, idempotent |
| `verifiko_llms_mentions.py` | Vérificateur de régression : exit 0 si aucun des écarts du 03/09 n'est présent et si avis/horaires de `llms.txt` = `index.html` |

```bash
python3 fix_llms_mentions.py /chemin/vers/rushiti-renovation            # simulation
python3 fix_llms_mentions.py /chemin/vers/rushiti-renovation --apply    # application
python3 verifiko_llms_mentions.py /chemin/vers/rushiti-renovation       # contrôle (exit 0 = conforme)
```

Test du 03/09 sur une copie de la page servie en production : vérificateur 17 écarts avant → 6 remplacements + `llms.txt` remplacé → 0 écart après → second passage du script : 0 modification (idempotence).

## 3. À trancher par Isuf avant mise en ligne

1. **Hébergeur** — adresse de Cloudflare, Inc. reprise de ses informations publiques (101 Townsend Street, San Francisco). À confirmer avec les conditions Cloudflare en vigueur ; retirer la phrase GitHub si le déploiement ne part plus du dépôt.
2. **Conteneur GTM-KPM3GQB6** — ouvrir Tag Manager et lister les balises. Si Google Analytics 4 (ou une autre mesure d'audience) y est actif, l'ajouter au paragraphe « Google Tag Manager » **et** au texte du bandeau (qui ne cite que Meta). Si le conteneur est vide, le paragraphe reste juste tel quel.
3. Les deux commentaires HTML `[À VÉRIFIER…]` sont à supprimer une fois ces points réglés.

## 4. Après mise en ligne

- Purger `/llms.txt` et `/mentions-legales` dans le cache Cloudflare, puis relire les deux URL servies.
- Ajouter `/llms.txt` à la matrice mensuelle `rushiti-faits-marque` (le fichier était absent du contrôle : c'est comme ça que l'écart 29/34 a survécu).
- Journal des décisions : une ligne datée (`rushiti-journal-decisions`).
