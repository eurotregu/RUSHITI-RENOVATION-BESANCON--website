# Correctifs de la flotte de skills — 21/08/2026

Dosje e prodhuar nga auditi i flotës së skill-ave (21/08/2026): versionet e
korrigjuara të 9 skill-ave **të llogarisë claude.ai** (skill-at "synced" nuk
jetojnë në këtë repo — ndryshimi aplikohet duke i ringarkuar te llogaria).

## Si aplikohen — 3 hapa, në këtë radhë

1. **Fshini 4 skill-at e zëvendësuar** te claude.ai → Settings → Capabilities
   → Skills: `rushiti-audit-technique`, `rushiti-crawl-audit`,
   `rushiti-quick-wins-gsc`, `rushiti-ctr-opportunites`.
   Ata u bashkuan më 15/08/2026 në `rushiti-audit-site` dhe
   `rushiti-opportunites-gsc` — asgjë nuk humbet.
2. **Fshini edhe kopjen e llogarisë të `rushiti-keyword-map`** — versioni i
   vetëm i vlefshëm mbetet ai i këtij repo-je (`.claude/skills/rushiti-keyword-map/`),
   sepse regjistri `docs/seo/regjistri-fjale-kyce.csv` jeton këtu.
3. **Zëvendësoni SKILL.md** e 9 skill-ave të mëposhtëm me versionet e kësaj
   dosjeje (dosjet `references/` dhe `scripts/` nuk ndryshojnë). Një arkiv zip
   me dosjet e plota, gati për ringarkim, dorëzohet veç në bisedë.

## Çfarë ndryshoi, skill pas skill-i

| Skill | Ndryshimi |
|---|---|
| `rushiti-gsc` | 18 rutime të vjetruara → `rushiti-opportunites-gsc` (mode 1 / mode 2) dhe `rushiti-audit-site`, me shënimin e modalitetit në tabelat e rutimit |
| `rushiti-priorisateur-seo` | Lista e burimeve në përshkrim u modernizua; hiqet referenca fantazmë `gsc-digger` (skill që s'ka ekzistuar kurrë) |
| `rushiti-regression-seo` | 1 rutim → `rushiti-opportunites-gsc` (mode CTR) |
| `rushiti-ecart-concurrentiel` | 1 rutim → `rushiti-opportunites-gsc`; hendeku i backlinks tani ruton shprehimisht te `rushiti-backlinks` |
| `rushiti-google-ads` | 2 rutime → `rushiti-opportunites-gsc` |
| `rushiti-google-trends` | 1 rutim i dyfishtë i pastruar → `rushiti-opportunites-gsc` |
| `orphan-finder` | Kufi i ri i shkruar me `rushiti-maillage-interne` (site-wide ↔ një faqe e vetme), në përshkrim dhe në trup |
| `rushiti-keyword-clusters` | Çdo faqe e re e propozuar kalon tani nga porta PORTA e `rushiti-keyword-map` para krijimit (përshkrim, procedurë, gabarit, pièges) |
| `rushiti-declinaison-chantier` | Studimi i rastit ndjek tani gabaritin e `rushiti-etudes-de-cas` (blloku « Ce que ce chantier montre », JSON-LD Article pa Review) — një format i vetëm në sit |

Në të njëjtin commit u korrigjuan edhe **dy skill-at e repo-s**
(`.claude/skills/`): `rushiti-audit-seo` (3 rutime + kufiri me
`rushiti-audit-site` në përshkrim) dhe `rushiti-keyword-map` (1 rutim).

## Në pritje të vendimit të Isufit (pa korrigjim këtu)

- **`seo-title-meta`** — shembujt e tij autorizojnë « devis 24h » /
  « intervention sous 24h » / « équipe de 5 », ndërsa gjithë flota tjetër i
  trajton afatet e pavalidiuara si PLACEHOLDER. Duhet vendimi juaj para se ta
  rreshtoj me rregullat e markës.
- **`rushiti-seo-local`** — shpall si sit kanonik të fiche-ave **rushiti.fr**,
  ndërsa shumica e flotës trajton **rushiti-renovation.fr** si sitin kryesor.
  Cili është siti kanonik i NAP-it? Pas përgjigjes, e shkruaj njësoj kudo.
