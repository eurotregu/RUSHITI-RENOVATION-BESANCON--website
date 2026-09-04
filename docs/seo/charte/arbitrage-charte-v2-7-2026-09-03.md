# Charte graphique v2.7 sur rushiti-renovation.fr — dossier d'arbitrage (03/09/2026)

| | |
|---|---|
| Constat | Audit du 03/09, constat 25 : le site tourne en `--navy #1B3A5B` et `--accent #E8743B` (orange) ; les Guidelines v2.7 fixent bleu nuit `#002B4B`, bleu `#1A75BB`, vert `#016738`, rouge `#EB1C24`. Deux identités coexistent entre le site, les devis, les courriers et les réseaux. |
| Décision attendue | Isuf : quelle palette pour le site, et quelle couleur pour le bouton d'action. |
| Ce dossier | Trois aperçus de l'accueil rendus à l'identique (1280 px), sans autre changement que les variables CSS. Rien n'est en production. |

## Les trois options

| | Bleu nuit | Bouton d'action | Positif | Alerte | Aperçu |
|---|---|---|---|---|---|
| Actuel | `#1B3A5B` | orange `#E8743B` | `#2E7D52` | — | `apercu-actuel.png` |
| **Variante A** — charte stricte | `#002B4B` | bleu `#1A75BB` | `#016738` | `#EB1C24` réservé aux erreurs de formulaire et aux alertes dégât des eaux | `apercu-variante-A-cta-bleu.png` |
| **Variante B** — charte + couleur d'action | `#002B4B` | orange `#E8743B` conservé | `#016738` | idem | `apercu-variante-B-cta-orange.png` |

## Lecture

- **Variante A** met le site en cohérence totale avec les documents. Coût : le bouton bleu contraste moins avec le bleu nuit des bandeaux de fin de page ; sur fond `#002B4B`, un bouton `#1A75BB` reste lisible (contraste texte blanc/`#1A75BB` ≈ 4,6:1) mais ressort moins qu'aujourd'hui. Le bandeau sticky mobile « Appeler / Devis gratuit » perd son accent.
- **Variante B** garde l'orange comme couleur d'action, ce que la charte ne prévoit pas. Si elle est retenue, la charte v2.8 devrait l'ajouter comme « couleur d'action » pour que devis, courriers et site racontent la même chose.
- **Ne pas faire** : utiliser le rouge `#EB1C24` pour « Demander un devis ». Le rouge signale une alerte ; il est déjà utilisé à bon escient pour le message « cochez la case » du formulaire.

## Ce que l'application demande, une fois la décision prise

1. Remplacer les variables `:root` des deux feuilles (`s971fb819.css`, `sda808997.css`) et la couleur `theme-color` des 757 pages (`#1B3A5B`).
2. Régénérer le favicon, le logo et l'image Open Graph par défaut si leurs bleus diffèrent.
3. Contrôler les contrastes WCAG sur : boutons, liens, chips, bandeau sticky, bloc CTA final, cartes d'avis.
4. Script idempotent + captures avant/après, comme pour les paquets précédents ; purge du cache Cloudflare après fusion.

Effort estimé : une demi-journée, sans risque fonctionnel.
