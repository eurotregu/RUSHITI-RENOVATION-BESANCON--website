# Paketa 10 — corrections P0 visibles (03/09/2026)

| | |
|---|---|
| Déclencheur | Isuf, 03/09 : « corriger /llms.txt, corriger les mentions légales, remplacer le bloc CTA « ratisser » sur les 5 pages, retirer les étoiles par avis (ou relever les notes réelles), rendre lisible le bouton e-mail du bloc final, dédoublonner la balise Google Fonts » |
| Dépôt cible | `eurotregu/rushiti-renovation` — **appliqué directement** : PR [#39](https://github.com/eurotregu/rushiti-renovation/pull/39), branche `claude/auditim-profesionist-premium-fj4m76` (brouillon, en attente de validation d'Isuf) |
| Paquet 9 | `llms.txt` et `mentions-legales.html` : appliqué dans la même PR avec `../paketa-9-llms-mentions/fix_llms_mentions.py` |

## Ce que fait `fix_p0_visuel.py`

| | Correction | Portée réelle |
|---|---|---|
| A | Bloc CTA final « Des murs à ratisser avant peinture ? » remplacé par un appel à l'action propre à la page | **7 pages**, pas 5 : l'audit en avait vu 5, le dépôt en contient 7 (s'ajoutent commerces et bureaux, rénovation d'appartement). Les 49 pages `ratissage-enduit-*` gardent le leur |
| B | `<div class="stars">★★★★★</div>` retiré sous chaque avis (notes individuelles non relevées, doctrine du 22/08) ; « · relevé le 22/08/2026 » ajouté après « 34 avis Google » ; tableau JSON-LD `review` retiré de `index.html` (reviewRating 5 par avis, même donnée) | 723 pages, 2 169 blocs |
| C | Bouton fantôme illisible : `.btn.ghost{color:var(--navy)}` (spécificité 0,2,0) battait `.u6{color:#fff}` (0,1,0) dans `.cta-band`. Règle `/*p0-ghost-cta*/.cta-band .btn.ghost,.btn.ghost.u6{color:#fff;…}` ajoutée en fin des deux feuilles (`s971fb819.css`, `sda808997.css`) ; `?v=7`/`?v=8` → `?v=9` | 2 CSS + 756 pages |
| D | Google Fonts : **faux positif de l'audit**. Le second `<link>` est le repli `<noscript>` du motif `media="print" onload="this.media='all'"`. Rien à changer ; le constat 9 de l'audit est retiré | — |

Non touché, volontairement : `aggregateRating` de `index.html` (arbitrage du 31/08 en attente), note moyenne « 4,7 / 5 ★★★★★ » (donnée relevée).

## Usage

```bash
python3 fix_p0_visuel.py /chemin/vers/rushiti-renovation            # simulation
python3 fix_p0_visuel.py /chemin/vers/rushiti-renovation --apply    # application
python3 verifiko_p0_visuel.py /chemin/vers/rushiti-renovation       # régression (exit 0 = conforme)
```

Exécution du 03/09 sur le clone de production (`c9b5434`) : simulation 758 fichiers → application → second passage 0 fichier → vérificateurs paquets 9 et 10 à 0 écart → JSON-LD de `index.html` valide, `</html>` unique sur 757 pages.

## Après fusion de la PR #39

1. Purger le cache Cloudflare (HTML en cache edge 24 h + CSS inliné par le Worker).
2. Relire en ligne : `/llms.txt`, `/mentions-legales` (sections 1, 3, 7), `/renovation-syndic-gestionnaire-besancon` (H2 final), bouton e-mail du bloc final sur mobile, absence d'étoiles sous les avis.
3. Ajouter `/llms.txt` à la matrice `rushiti-faits-marque` ; ligne au journal des décisions.
