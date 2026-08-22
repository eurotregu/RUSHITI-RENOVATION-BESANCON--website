# Korrigjimet e prodhimit — dé-duplikimi papier peint / toile de verre

| | |
|---|---|
| Data | 21/08/2026 |
| Objekti | Konstati 2 i auditit të fjalëve kyçe (20/08): faqet `papier-peint-<zonë>` synonin edhe «toile de verre» në title/H1/meta/og, në konkurrencë me faqet e dedikuara `toile-de-verre-<zonë>` |
| Depoja e synuar | `eurotregu/rushiti-renovation` (siti në prodhim) — **jo kjo depo** |

## ⚡ Përditësim i rëndësishëm (21/08, pasdite): korrigjimi rezulton i shpërndarë

Inventari live i kryer më 21/08 pasdite mbi **të 40 URL-të** `papier-peint-*` të sitemap-it aktual (workflow me 8 agjentë skanimit + 4 rikontrolle manuale, lexim i kodit HTML të faqeve — kurrë SERP) tregoi:

- **40/40 faqe të korrigjuara**: title «Papier peint <Zonë> – Pose et raccords | RUSHITI» (ose variant i shkurtuar ≤ 60 shenja), asnjë «toile de verre» në baliza;
- shpërndarja po propagandohej gjatë ditës: `/papier-peint-boussieres` u kap në mëngjes ende me cibël të dyfishtë, një orë më vonë i korrigjuar;
- konsolidimi i grilës gjithashtu në zbatim: 40 faqe papier-peint (nga 76), shembull `/papier-peint-champoux` → 301 → `/papier-peint-besancon`.

Inventari i plotë: **`inventar-live-2026-08-21.csv`**.

**Rrjedhimisht skriptet e kësaj dosjeje nuk janë më korrigjim urgjent** — mbeten si vegla verifikimi dhe regresi.

## Skedarët

| Skedari | Roli sot |
|---|---|
| `fix_papier_peint.py` | Skripti i dé-duplikimit, **idempotent** (faqet e korrigjuara i kapërcen). I dobishëm nëse shtohen zona të reja me gabaritin e vjetër, ose si referencë e transformimit |
| `verifiko_papier_peint.py` | **Vegla e përhershme e regresit**: kontrollon që asnjë faqe papier-peint të mos rikthejë «toile de verre» në baliza, që çdo title të mbetet ≤ 60 shenja dhe që lidhja drejt faqes toile-de-verre të ruhet. Për t'u ekzekutuar pas çdo gjenerimi të ri të grilës |
| `inventar-live-2026-08-21.csv` | Fotografia e verifikuar e 21/08: 40/40 URL me title-in ekzakt të lexuar live |

## Përdorimi (mbi një checkout të depos së prodhimit)

```bash
python3 fix_papier_peint.py /rruga/drejt/rushiti-renovation           # simulim
python3 fix_papier_peint.py /rruga/drejt/rushiti-renovation --apply   # zbatim
python3 verifiko_papier_peint.py /rruga/drejt/rushiti-renovation      # verifikim (exit 0 = konform)
```

## Prova e testimit

Skriptet u testuan më 21/08 mbi HTML-në **reale** të prodhimit (`/papier-peint-boussieres`, marrë live në gjendjen e pakorrigjuar të mëngjesit):

- title: `Papier peint & toile de verre Boussières | RUSHITI` → `Papier peint Boussières – Pose et raccords | RUSHITI` (52 shenja) — identik me modelin live të Pontarlier;
- H1 dhe të dyja description-et transformuar sipas modelit të Besançon-it;
- lidhja `toile-de-verre-boussieres` e paprekur;
- `verifiko_papier_peint.py`: 0 gabime; riekzekutimi i fix-it: 0 ndryshime (idempotencë e provuar).

*Shënim aksesi: qasja push në depon e prodhimit u bllokua nga klasifikuesi i lejeve në sesionin e 21/08 — prandaj kjo paketë jetohet këtu. Për seanca të ardhshme që duhet ta prekin prodhimin, jepni lejen `add_repo` kur t'ju kërkohet.*

---

# Paketa 2 — plotësimi i formularëve « Demande rapide » (22/08/2026)

| | |
|---|---|
| Data | 22/08/2026 |
| Objekti | Tri vendimet e hapura të formularit (dërgimi, mentions légales, numërimi i lead-eve) — vendosur e zbatuar me autorizimin e Isufit |
| Depoja e synuar | `eurotregu/rushiti-renovation` — kësaj radhe me **akses direkt**: ndryshimet u dorëzuan me PR në degën `claude/demande-rapide-web3forms-mentions` |

## Çfarë u konstatua

Formulari « Demande rapide » rezultoi **tashmë i shpërndarë** në 29 faqe pilier
`-besancon` me POST nativ Web3Forms (i njëjti çelës me `/contact`) — pra vendimi
« mailto apo server » ishte de facto i marrë. Mangësitë reale që u korrigjuan:

1. **`/merci` pa event konvertimi** — asnjë dërgim formulari nuk numërohej te
   Meta (vetëm klikimet « devis »). U shtua `Lead {content_name:"formulaire"}`
   pas pëlqimit të cookies;
2. **CSS-ja globale pa asnjë rregull formulari** (`label/input/select/.form-grid`
   mungojnë në `assets/css/s971fb819.css`) — formulari shfaqej i pastilizuar.
   U shtua blloku `/*dr-style*/` i fokusuar te `#demande-rapide` në çdo faqe;
3. **Pa atribuim për faqe** — u shtua fusha e fshehtë `page` me URL-në;
4. **`prix-travaux-renovation-besancon`** ishte e vetmja faqe pilier pa formular
   — iu transplantua nga gabariti live i `toile-de-verre-besancon`;
5. **`</main></main>` i dyfishuar** në 11 faqe — u normalizua;
6. **`mentions-legales.html`**: §7 thoshte « asnjë cookie, s'duhet pëlqim »
   ndërsa siti ngarkon Pixel Meta me bandeau — u rishkrua; Web3Forms u deklarua
   si nën-përpunues RGPD; të drejtat u plotësuan (fshirje, kundërshtim,
   portabilitet, ankesë CNIL); seksioni dublikatë në fund u hoq.

## Skedarët

| Skedari | Roli |
|---|---|
| `korrigjo_formulare_prodhim.py` | Zbaton pikat 2–5, **idempotent** (faqet e korrigjuara i kapërcen). I ripërdorshëm nëse gjenerohen faqe të reja me gabaritin e vjetër |
| `verifiko_demande_rapide.py` | **Vegla e përhershme e regresit**: 30 faqet + `/merci` — strukturë, çelës, subjekt, fushë page, stil, event Lead. Për t'u ekzekutuar para çdo deploy-i |

## Përdorimi (mbi një checkout të depos së prodhimit)

```bash
python3 korrigjo_formulare_prodhim.py /rruga/drejt/rushiti-renovation           # simulim
python3 korrigjo_formulare_prodhim.py /rruga/drejt/rushiti-renovation --apply   # zbatim
python3 verifiko_demande_rapide.py /rruga/drejt/rushiti-renovation              # verifikim (exit 0 = konform)
```
