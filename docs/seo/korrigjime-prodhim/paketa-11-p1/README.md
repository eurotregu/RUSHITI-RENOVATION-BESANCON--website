# Paketa 11 — corrections P1 (03/09/2026)

| | |
|---|---|
| Déclencheur | Isuf, 03/09 : « vazhdo me P1 : aggregateRating, hCaptcha, page À propos, Contact » (constats 4, 8, 10, 12 de `docs/seo/audit-premium-site-2026-09-03.md`) |
| Dépôt cible | `eurotregu/rushiti-renovation` — **appliqué directement** : PR [#40](https://github.com/eurotregu/rushiti-renovation/pull/40), branche `claude/auditim-profesionist-premium-fj4m76` (brouillon, validation d'Isuf attendue) |

## Ce que fait `fix_p1.py`

| | Correction | Portée |
|---|---|---|
| A | `aggregateRating` retiré du nœud LocalBusiness de l'accueil (avis tiers, doctrine du 22/08) ; `legalName: "Rushiti"` ajouté au nœud LocalBusiness de toutes les pages, formats compact et espacé | 1 + 743 nœuds ; **150 pages** portaient `legalName: "RUSHITI Rénovation"` (nom commercial), corrigé |
| B | Chargement différé du script client Web3Forms (`web3forms.com/client/script.js`), qui est ce qui injecte hCaptcha (≈ 600 Ko + 2 iframes) : chargeur inline `/*w3f-lazy*/`, déclenché à 600 px du formulaire (`IntersectionObserver`) ou au premier `focusin`/`pointerdown` dans le formulaire ; repli immédiat sans `IntersectionObserver`. Le garde-fou « cochez la case » (paquet hCaptcha du 02/09) est inchangé | 31 pages (30 piliers + `/contact`) |
| C | Page À propos : `<main>` remplacé par `a-propos-main.html`, JSON-LD remplacé par `a-propos-jsonld.json` (AboutPage, LocalBusiness avec `founder`/`employee` → `Person` #isuf et #yll, BreadcrumbList, FAQPage 6 questions = FAQ visible) | 1 page, 390 → 1 200 mots |
| D | Page Contact : délai « sous 24 à 48 h ouvrées » (déjà publié sur `/merci`), lien Google Maps (`cid` existant), carte « Ce qui se passe après votre demande », mention urgence, bouton WhatsApp | 1 page, 3 remplacements |

Faits utilisés pour À propos : socle v4 (`rushiti-architecte-seo/references/donnees-rushiti.md` : SARL créée le 04/11/2021, APE 43.34Z, 20 ans de métier d'Isuf, garanties légales, DTU), mentions légales (ERGO Bâtisseurs, activités garanties), pages existantes (mesure d'humidité, lumière rasante, hors périmètre plomberie/électricité/recherche de fuite). Aucun prix, délai ni certification ajouté. Pas de portrait : aucune photo des dirigeants dans le dépôt.

## Usage

```bash
python3 fix_p1.py /chemin/vers/rushiti-renovation            # simulation
python3 fix_p1.py /chemin/vers/rushiti-renovation --apply    # application
python3 verifiko_p1.py /chemin/vers/rushiti-renovation       # régression (exit 0 = conforme)
```

Exécution du 03/09 sur le clone de production (`f444bf7`) : 744 fichiers, second passage à 0 modification, 755 JSON-LD valides, FAQ À propos 6/6 visible, test Chromium du chargeur différé (script absent au chargement, présent après défilement et après focus), captures mobile et bureau relues.

## Après fusion de la PR #40

1. Purger le cache Cloudflare.
2. Relire `/a-propos`, `/contact` ; sur `/peinture-interieure-besancon`, descendre jusqu'au formulaire et vérifier que la case hCaptcha apparaît.
3. Rich Results Test sur `/a-propos` (FAQPage, BreadcrumbList) et `/` (LocalBusiness sans aggregateRating).
4. Décisions à consigner : retrait de l'`aggregateRating` (tranché le 03/09), portraits à fournir.
