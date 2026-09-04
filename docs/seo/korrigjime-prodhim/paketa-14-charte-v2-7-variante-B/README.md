# Paquet 14 — charte v2.7, variante B (04/09/2026)

Décision d'Isuf le 04/09/2026, sur le dossier `docs/seo/charte/arbitrage-charte-v2-7-2026-09-03.md` :
**variante B** = bleu nuit et vert alignés sur la charte, orange conservé comme couleur d'action.

| Rôle | Avant | Après | Où |
|---|---|---|---|
| Bleu nuit `--navy` | `#1B3A5B` | `#002B4B` (charte) | 2 feuilles CSS, `theme-color` de 756 pages, `site.webmanifest`, `favicon.svg`, bloc `:root` inline d'un article de blog |
| Bleu nuit foncé `--navy-dark` (pied de page, ombres) | `#13293F` / `rgba(19,41,63,…)` | `#001E36` / `rgba(0,30,54,…)` — déclinaison dérivée de `#002B4B`, à inscrire dans la v2.8 | 2 feuilles CSS (18 ombres), même article de blog |
| Vert positif `--ok` | `#2E7D52` | `#016738` (charte) | 2 feuilles CSS + 7 377 coches SVG inline (`stroke=`) sur 726 pages |
| Orange d'action `--accent` / `--accent-dark` | `#E8743B` / `#CF5E27` | inchangé | — |
| Bandeau cookies et bloc `.u1` | `#0E2436` | inchangé (bleu-noir neutre, hors charte mais sans conflit) | — |
| Icônes | PNG sur `#1B3A5B` | régénérés depuis `favicon.svg` : 16, 32, 180 (Apple), **192 et 512 (référencés par le manifest mais absents jusqu'ici)** | racine |
| Cache CSS | `?v=10` | `?v=11` | 756 pages |

Non touché : `logo.png` (déjà en `#002B4B`), image Open Graph par défaut (= logo), textes et gabarits.
Le rouge `#EB1C24` de la charte n'est utilisé nulle part dans le code : le message « cochez la case » du
formulaire est celui du navigateur, pas du site. Rien à faire tant qu'aucune alerte n'est stylée.

## Contrastes (WCAG, calcul dans ce paquet)

| Couple | Ratio | Lecture |
|---|---|---|
| blanc sur bleu nuit `#002B4B` | 14,5:1 | meilleur qu'avant (11,7:1) |
| bleu nuit `#002B4B` sur fond doux `#F5F7FA` | 13,5:1 | titres, liens |
| vert `#016738` sur blanc | 7,0:1 | meilleur qu'avant (5,0:1) |
| textes clairs du pied de page sur `#001E36` | 10,0:1 et 6,5:1 | conformes |
| orange `#E8743B` sur bleu nuit `#002B4B` (mention « 20 ans ») | 4,8:1 | conforme |
| **blanc sur orange `#E8743B` (boutons)** | **3,0:1** | inchangé par ce paquet ; conforme pour un composant d'interface, sous le seuil 4,5:1 du texte courant. Point ouvert pour la v2.8 (orange plus foncé `#CF5E27` = 4,0:1, ou texte bleu nuit sur orange). |

## Fichiers

- `fix_charte_B.py` : correction idempotente, compteurs attendus affichés.
- `verifiko_charte_B.py` : aucun résidu des anciennes couleurs, `theme-color` et `?v=11` partout (sauf `404.html`, sans `theme-color` d'origine), variables attendues dans les deux feuilles, PNG d'icônes sur `#002B4B`.
- `gen_icones.js` : rendu des PNG depuis `favicon.svg` par Chromium (fond transparent).
- `captures_avant_apres.js` : captures Playwright ; comparatifs dans `docs/seo/charte/variante-B-avant-apres/`.

Après fusion de la PR de production : purge du cache Cloudflare (accord d'Isuf), contrôle en direct du `theme-color`, d'une coche verte et du pied de page.
