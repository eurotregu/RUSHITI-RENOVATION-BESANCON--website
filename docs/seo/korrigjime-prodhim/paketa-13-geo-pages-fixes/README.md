# Paquet 13 — geo manquant sur six pages fixes (04/09/2026)

Relevé lors du contrôle en direct de `/peinture-interieure-besancon` après le
déploiement du Worker `2026-09-04-avis-sans-etoiles` : le nœud LocalBusiness
de six pages fixes n'avait aucun bloc `geo`, alors que les 736 autres pages
portent la position BAN du siège depuis le paquet 12 (qui ne remplaçait que
les blocs existants, hérités du centre-ville).

| Page | Avant | Après |
|---|---|---|
| `/peinture-interieure-besancon`, `/platrerie-besancon`, `/degat-des-eaux-besancon`, `/a-propos`, `/contact`, `/mentions-legales` | adresse postale sans `geo` | `geo` 47.245638 / 6.00556 (BAN 25056_4260_00018) inséré après `address` |
| `/simulateur-peinture` | nœud `provider` réduit (référence `#business`, sans adresse) | inchangé : un `geo` sans adresse n'aurait pas de sens sur un nœud de référence |

- `fix_geo_pages_fixes.py` : insertion idempotente, JSON-LD revalidé après chaque page.
- `verifiko_geo_pages_fixes.py` : un bloc geo BAN par page, aucun résidu 47.238, JSON-LD valide.
- Décision d'Isuf le 04/09/2026 (question posée avant exécution). Rien en ligne avant fusion de la PR de production.
