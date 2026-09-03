# Études de cas — kit de production (03/09/2026)

| | |
|---|---|
| Déclencheur | Isuf, 03/09 : « vazhdo me P2 : études de cas » (constat 13 de `audit-premium-site-2026-09-03.md`) |
| Ce que le kit fait | Transforme un chantier réel en page `/realisations/{slug}` conforme au site (même en-tête, pied, scripts, styles d'article), avec la trame Guidelines : problème vécu → diagnostic → intervention en trois temps → résultat, photos légendées, citation seulement avec accord écrit, JSON-LD `Article` + `BreadcrumbList` (+ `FAQPage`), maillage vers le pilier, la page locale de la commune et le blog. |
| Ce que le kit ne fait pas | Inventer. Sans matière réelle (commune, problème, mesures, photos autorisées), le générateur **refuse** de produire une page publiable. |

## Pourquoi rien n'est en production

Les 17 photos de `/realisations` ne portent aucun fait : pas de commune, pas de problème initial, pas de mesure, pas d'accord client documenté. Les six fiches de `fiches/` sont pré-remplies avec ce que les photos montrent ; tout le reste est marqué `[À COMPLÉTER]`. Une page d'étude de cas avec des trous ou des faits supposés ferait plus de mal qu'une galerie muette. Le kit est prêt, la matière vient d'Isuf et Yll.

## Procédure (10 minutes par chantier)

1. Choisir un chantier réel, de préférence dans le silo dégât des eaux (le plus rentable et le moins visible), puis peinture, placo, isolation.
2. Répondre au `questionnaire-chantier.md` (oral ou écrit, français ou albanais) ; obtenir l'**accord écrit** du client pour les photos (et pour la citation, s'il y en a une).
3. Reporter les réponses dans la fiche JSON correspondante de `fiches/` (ou copier `fiche-modele.json`).
4. Générer sur un checkout du dépôt de production :
   ```bash
   python3 gen_etude_de_cas.py fiches/isolation-combles.json /chemin/vers/rushiti-renovation --brouillon   # relecture, page noindex
   python3 gen_etude_de_cas.py fiches/isolation-combles.json /chemin/vers/rushiti-renovation               # page finale dans realisations/
   ```
   Le script imprime la carte à coller dans `realisations.html` et la ligne à ajouter au `sitemap.xml`.
5. Relire, puis PR sur le dépôt de production ; après fusion : purge du cache, ajout à `/llms.txt`, lien depuis la page locale de la commune.

## Garde-fous intégrés au générateur

- Refus si un champ contient `[À COMPLÉTER]` ou `[À CONFIRMER]` (sauf `--brouillon`, qui produit une page `noindex` pour relecture).
- Refus si des photos sont listées sans `accord_photos: true`, ou une citation sans `accord_ecrit: true`.
- Refus de tout champ « prix », « tarif », « delai_promis ».
- Aucune note, aucun `Review` ni `aggregateRating` : la citation est du texte, jamais un balisage d'avis.
- Le bloc « Prestations » ne liste que des services existants du site ; la page locale n'est liée que si elle existe réellement.

## Fichiers

| Fichier | Rôle |
|---|---|
| `gen_etude_de_cas.py` | Générateur (fiche JSON → page HTML + carte + ligne sitemap) |
| `gabarit-main.html` | Bloc `<main>` de la page, classes du site (`article`, `tldr`, `steps`, `gallery`, `keypoint`, `relinks`, `cta-band`) |
| `fiche-modele.json` | Schéma d'une fiche, à copier |
| `questionnaire-chantier.md` | Les 14 questions à poser, règles RGPD et périmètre |
| `fiches/*.json` | 6 chantiers pré-remplis depuis les photos existantes : salle de bains, isolation de combles, doublage et cloisons placo, faux plafond LED, papier peint en cage d'escalier, plafond après dégât des eaux |

Test du 03/09 : fiche pré-remplie → refus (2 motifs) ; `--brouillon` → 6 pages noindex de 750 à 790 mots ; fiche de test complète (fictive, non publiée) → page valide, JSON-LD `Article` + `BreadcrumbList` + `FAQPage`, rendu contrôlé dans Chromium.

## Priorité conseillée

1. **Dégât des eaux** (silo prioritaire) : un dossier complet, avec relevés d'humidité et vocabulaire IRSI.
2. **Peinture intérieure** dans un immeuble ancien du centre : préparation des fonds, plâtre traditionnel.
3. **Placo / isolation** sur le plateau (Saône, Mamirolle, Nancray) : murs froids, condensation.
Chaque page publiée se relie ensuite à la page locale de sa commune : c'est la première preuve locale réelle de la grille (voir `../grille-locale/README.md`).
