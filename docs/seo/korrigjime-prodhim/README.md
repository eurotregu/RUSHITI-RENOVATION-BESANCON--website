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
| Depoja e synuar | `eurotregu/rushiti-renovation` — kësaj radhe me **akses direkt**: PR [#20](https://github.com/eurotregu/rushiti-renovation/pull/20), degë `claude/demande-rapide-web3forms-mentions` |

## Çfarë u konstatua

Formulari « Demande rapide » rezultoi **tashmë i shpërndarë** në 29 faqe pilier
`-besancon` me POST nativ Web3Forms (i njëjti çelës me `/contact`) — pra vendimi
« mailto apo server » ishte de facto i marrë. Për më tepër, **PR #10** (draft,
20-21/08, «mise en forme et variante B») mbart tashmë: stilimin e formularit në
CSS-në globale (`?v=8`), kutinë e detyrueshme të pëlqimit RGPD, bandën e
risigurimit dhe **eventin Lead në `/merci`** — i verifikuar në Chromium, me
parapamje Cloudflare. Pyetja e vetme e hapur aty: e-mail-i bëhet i detyrueshëm.

**Ndarja e punës**, që asgjë të mos mbivendoset e as të numërohet dyfish:

| Pjesa | Kush e mbart |
|---|---|
| Stilimi i formularit (CSS globale), kutia e pëlqimit, eventi Lead në `/merci` | **PR #10** (paraekzistues — për t'u bashkuar) |
| Fusha `page` (atribuim për faqe), formulari për `prix-travaux`, `</main></main>` ×11, mentions-legales RGPD | **PR #20** (kjo paketë) |

## Çfarë korrigjon PR #20

1. **Pa atribuim për faqe** — fushë e fshehtë `page` me URL-në në 30 formularët
   (subjekti dallon vetëm shërbimin; tani çdo lead tregon edhe faqen e saktë);
2. **`prix-travaux-renovation-besancon`** ishte e vetmja faqe pilier pa formular
   — iu transplantua nga gabariti live i `toile-de-verre-besancon`;
3. **`</main></main>` i dyfishuar** në 11 faqe — u normalizua;
4. **`mentions-legales.html`**: §7 thoshte « asnjë cookie, s'duhet pëlqim »
   ndërsa siti ngarkon Pixel Meta me bandeau — u rishkrua; Web3Forms u deklarua
   si nën-përpunues RGPD; të drejtat u plotësuan (fshirje, kundërshtim,
   portabilitet, ankesë CNIL); seksioni dublikatë në fund u hoq.

## Skedarët

| Skedari | Roli |
|---|---|
| `korrigjo_formulare_prodhim.py` | Zbaton pikat 1–3, **idempotent**. I ripërdorshëm nëse gjenerohen faqe të reja me gabaritin e vjetër |
| `verifiko_demande_rapide.py` | **Vegla e përhershme e regresit**: 30 faqet — strukturë, çelës, subjekt, fushë page; plus dy kontrolle KUJDES (stili global, eventi Lead në `/merci`) që kthehen OK pasi PR #10 të bashkohet. Për t'u ekzekutuar para çdo deploy-i |

## Përdorimi (mbi një checkout të depos së prodhimit)

```bash
python3 korrigjo_formulare_prodhim.py /rruga/drejt/rushiti-renovation           # simulim
python3 korrigjo_formulare_prodhim.py /rruga/drejt/rushiti-renovation --apply   # zbatim
python3 verifiko_demande_rapide.py /rruga/drejt/rushiti-renovation              # verifikim (exit 0 = konform)
```

## Radha e bashkimit të rekomanduar

1. **PR #10** — stilimi + pëlqimi + Lead në `/merci` (arbitrazhi për e-mail-in e
   detyrueshëm: **mbahet i detyrueshëm** — varianti B e parasheh, devis-i i
   shkruar kërkon e-mail; hiqet me një fjalë nëse Isuf vendos ndryshe);
2. **PR #20** — plotësimet e kësaj pakete (të pavarura, pa konflikt përmbajtjeje).

---

# Paketa 3 — `sameAs` i nyjeve LocalBusiness (22/08/2026)

| | |
|---|---|
| Data | 22/08/2026 |
| Objekti | Verifikimi i `sameAs`: a lidh JSON-LD-ja LocalBusiness sitin me PagesJaunes, Google Maps dhe regjistrat tregtarë? |
| Raporti | `../verifikim-sameas-localbusiness-2026-08-22.md` |
| Depoja e synuar | `eurotregu/rushiti-renovation` — **e zbatuar** me autorizimin e Isufit: PR [#24](https://github.com/eurotregu/rushiti-renovation/pull/24), degë `claude/sameas-localbusiness-citimet`, 743 faqe |

## Çfarë u konstatua

**Jo.** 736 nga 757 faqet e prodhimit deklarojnë vetëm `["https://rushiti.fr"]`.
Google Maps figuron në 1 faqe të vetme (`index.html`); PagesJaunes dhe
regjistrat tregtarë nuk figurojnë askund. 4 faqe s'kanë fare `sameAs`, 14 s'kanë
nyje biznesi. Sintaksa JSON është e pastër në të 756 blloqet.

Të katër profilet u hapën live më 22/08 dhe u kryqëzuan me SIRET-in/telefonin
para se të futeshin në listën kanonike (PagesJaunes `pros/61325501`, Google Maps
`cid=10915820577691168567`, Annuaire des Entreprises, INPI/RNE).

## Skedarët

| Skedari | Roli |
|---|---|
| `fix_sameas_localbusiness.py` | Plotëson `sameAs` (bashkim, jo zëvendësim), pa rishkruar JSON-in — formatimi ekzistues mbetet. **Idempotent** |
| `verifiko_sameas.py` | **Vegla e përhershme e regresit**: JSON i vlefshëm + 7 URL-të kanonike në çdo nyje me `@id`; nyjet e ngulitura pa `@id` raportohen si KUJDES. Për t'u ekzekutuar para çdo deploy-i |

## Përdorimi (mbi një checkout të depos së prodhimit)

```bash
python3 fix_sameas_localbusiness.py /rruga/drejt/rushiti-renovation           # simulim
python3 fix_sameas_localbusiness.py /rruga/drejt/rushiti-renovation --apply   # zbatim
python3 verifiko_sameas.py          /rruga/drejt/rushiti-renovation           # verifikim (exit 0 = konform)
```

## Prova e testimit

Mbi checkout-in real të prodhimit (`abcdd34`) dhe mbi këtë depo:

- simulim mbi prodhimin: **740 faqe / 740 vargje**, asnjë skedar tjetër i prekur;
- zbatuar mbi këtë depo (`index.html`, `syndic-copropriete-besancon.html`):
  JSON i rivalidhuar, formatimi i ruajtur, rileximi jep **0 ndryshime**
  (idempotencë e provuar);
- `verifiko_sameas.py` mbi këtë depo: **exit 0**.

## Zbatimi (22/08, mbrëmje)

Me autorizimin e Isufit skripti u zbatua mbi prodhimin: **743 faqe**. Tri nyje
biznesi anonime (`contact.html`, `simulateur-peinture.html`,
`blog/calcul-rouleaux-papier-peint.html`) morën `@id`-në kanonike me dorë —
skripti nuk ua vë vetë, sepse t'i japësh identitet një nyjeje anonime është
vendim redaktorial.

Dy përmirësime të vogla dolën nga zbatimi:

- `fix_sameas_localbusiness.py` e fut `sameAs` pas `"priceRange"` ose, kur ai
  mungon, pas `"taxID"` — rasti i `contact.html`;
- `verifiko_sameas.py` kontrollon tani që `@id`-ja të jetë kanonikja (një
  `@id` i dytë = entitet i dytë me të njëjtin emër) dhe nuk e kërkon më
  `sameAs` te nyjet referencë — JSON-LD i bashkon sipas `@id`, pra përsëritja
  do të ishte dyfishim.

Verifikimi para push-it: 758 blloqe JSON-LD, 0 të pavlefshme; krahasim
strukturor bllok për bllok para/pas mbi të 743 skedarët — të vetmit çelësa të
ndryshuar `sameAs[]` dhe `@id`, asnjë ndryshim jashtë JSON-LD-së; idempotencë e
provuar; `verifiko_sameas.py` exit 0.
