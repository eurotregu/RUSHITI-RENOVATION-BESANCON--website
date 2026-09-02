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

---

# Paketa 4 — forcimi i silos «dégât des eaux» (24/08/2026)

| | |
|---|---|
| Data | 24/08/2026 |
| Objekti | Auditi i faqes pilier `/degat-des-eaux-besancon` — PRIORITETI 1 i regjistrit të fjalëve kyçe |
| Raporti | `../audit-degat-des-eaux-besancon-2026-08-24.md` |
| Depoja e synuar | `eurotregu/rushiti-renovation` — **e zbatuar** me autorizimin e Isufit: PR [#26](https://github.com/eurotregu/rushiti-renovation/pull/26), degë `claude/forcement-silo-degat-des-eaux`, 77 skedarë |
| Baza e leximit | prodhimi në commit `3793684` (24/08/2026) + kodi HTML i faqes live |

## Çfarë u konstatua

Tri hipotezat e briefit fillestar **nuk qëndrojnë** në kod: JSON-LD-ja ekziston
(`Service` + `BreadcrumbList` + `FAQPage` me 13 pyetje + `LocalBusiness` me 7
`sameAs`), sticky CTA-ja ekziston (`.callbar`, 756/757 faqe), dhe ana teknike
është e shëndetshme (CSS e jashtme e versionuar, fontet async, webp me përmasa,
GTM me Consent Mode, canonical/robots/sitemap/llms.txt në rregull).

Problemi i vërtetë është tjetërkund — **faqja pilier është hallka më e dobët e
silos së vet**:

- **75/75 faqet e grilës** kanë `hasOfferCatalog` dhe bllokun e avis-eve Google
  (4,7/5 · 34 avis); **pilieri s'ka asnjërën**;
- një zëvendësim global «recherche de fuite» → «mesure d'humidité» ka lënë
  **tri dëme**: një kundërthënie e dukshme në trupin e pilierit («prestation
  jashtë perimetrit: la mesure d'humidité de la fuite», ndërsa metoda fillon
  pikërisht me matjen e lagështisë), një dublim në JSON-LD-në e **76/76** faqeve,
  dhe një rresht të pasaktë në `llms.txt`;
- meta description-i i pilierit është **fjali e prerë** («devis conforme»);
- maillage-i: **757/757 faqe** lidhen drejt pilierit, por thuajse vetëm me ankora
  navigimi. Deficit i vërtetë është **dalës**: brenda `<main>` pilieri lidh
  kontekstualisht vetëm **1** faqe, dhe **0** drejt `/devis-assurance-degat-des-eaux-besancon`,
  `/expert-assurance-sinistre-besancon`, `/renovation-syndic-gestionnaire-besancon`,
  `/remise-en-etat-logement-locatif-besancon`, blogut IRSI dhe atij «réparer un mur»;
- GEO: chapeau-ja fillon me paralajmërimin, jo me përgjigjen direkte.

## Skedarët

| Skedari | Roli |
|---|---|
| `fix_degat_des_eaux.py` | Korrigjimi, **idempotent**: dublimi JSON-LD (76 faqe), kundërthënia, description-i, `hasOfferCatalog`, blloku i avis-eve, 6 ankorat e maillage-it, chapeau-ja GEO, `llms.txt`. Opsioni `--cta` prek vetëm libelin e barrës mobile të pilierit |
| `verifiko_degat_des_eaux.py` | **Vegla e përhershme e regresit** e silos: JSON i vlefshëm, pa dublim, pa kundërthënie, description ≤ 155 dhe fjali e mbyllur, `hasOfferCatalog` ≥ 4 oferta, blloku i avis-eve me `cid`-in kanonik, 6 ankorat, pariteti FAQ e dukshme ↔ `FAQPage`, canonical, `.callbar`. Për t'u ekzekutuar para çdo deploy-i |

## Përdorimi (mbi një checkout të depos së prodhimit)

```bash
python3 fix_degat_des_eaux.py /rruga/drejt/rushiti-renovation                 # simulim
python3 fix_degat_des_eaux.py /rruga/drejt/rushiti-renovation --apply         # zbatim
python3 fix_degat_des_eaux.py /rruga/drejt/rushiti-renovation --apply --cta   # + libeli i barrës mobile
python3 verifiko_degat_des_eaux.py /rruga/drejt/rushiti-renovation            # verifikim (exit 0 = konform)
```

## Prova e testimit

Mbi një kopje të checkout-it real të prodhimit (76 faqe + `llms.txt`):

- verifikim **para**: 86 gabime (76 dublime + 10 konstate të pilierit), 1 KUJDES;
- simulim: 77 skedarë të listuar, asnjë shkrim;
- zbatim: 77 skedarë, pilieri +2 275 shenja;
- verifikim **pas**: **CONFORME — 0 gabime, 0 alerta**;
- riekzekutim i fix-it: **0 skedarë të ndryshuar** (idempotencë e provuar);
- 76 blloqe JSON-LD të rilexuara me `json.loads`: **0 të pavlefshme**;
- diff-i i tekstit të dukshëm: vetëm 3 ndryshimet e synuara — 6 ankorat nuk
  prekin asnjë fjalë.

## Të pavendosura (i mbeten Isufit)

Premtimi «devis sous 48 h» (ekziston në 9 faqe të tjera, kurrë në këtë silo),
rishkrimi i `<title>`, H2-të në formë pyetjeje, formulari që mungon në 75 faqet
e zonës, dhe harmonizimi i libelit të barrës mobile. Arsyet: §4 e raportit.

## Zbatimi (24/08)

Me autorizimin e Isufit skripti u zbatua mbi prodhimin: **77 skedarë**
(76 faqe të silos + `llms.txt`), +83 / −82 rreshta. Arbitrazhet mbetën të hapura
siç ishin rekomanduar: **pa «48 h»**, `<title>` i paprekur, `--cta` i pazbatuar.

Kontrollet para push-it, mbi checkout-in real të prodhimit:

- `verifiko_degat_des_eaux.py`: **86 gabime → 0** (exit 0);
- riekzekutim i fix-it: **0 skedarë** (idempotencë);
- **758 blloqe JSON-LD të gjithë sitit** të rilexuara me `json.loads`: **0 të pavlefshme**;
- krahasim strukturor bllok për bllok: të vetmit çelësa të ndryshuar `description`
  (76 faqe) dhe `hasOfferCatalog` (1) — asnjë ndryshim tjetër në JSON-LD;
- **75 faqet e zonës**: asnjë ndryshim jashtë JSON-LD-së;
- balanca e tageve HTML të pilierit **identike** para/pas;
- **rendering i verifikuar në Chromium**: blloku i avis-eve i stiluar saktë,
  i vendosur para FAQ-së si në faqet e grilës.

Një përmirësim i vogël doli nga zbatimi: guardi i idempotencës së maillage-it
kontrollon ankorën e plotë (`<a href=…>teksti</a>`), jo vetëm praninë e URL-së —
përndryshe lidhjet e menusë drejt të njëjtave faqe do ta bllokonin futjen e
ankorave kontekstuale.

## Kalimi i dytë (24/08) — H2-të GEO dhe barra e apelit

Pas relektimit, dy nga arbitrazhet e mbetura u vendosën dhe u zbatuan
(commit `eb52bd5`, e njëjta PR #26):

- **gjashtë H2 seksionesh** kaluan në formë pyetjeje (« Quels sont les signes
  d'un dégât des eaux ? », « Combien coûte la réparation d'un dégât des eaux à
  Besançon ? »…) — asnjë paragraf i prekur, vetëm titujt;
- **dublimi i pyetjes së çmimit** u shmang: pyetja e FAQ-së u riformulua në
  « De quoi dépend le montant d'une réparation après dégât des eaux ? », duke
  ndryshuar `<summary>` **dhe** nyjen `FAQPage` bashkë — pariteti 13/13 i ruajtur;
- **barra e apelit mobile e pilierit**: « Devis gratuit » → « Devis assurance »
  (`--cta`). Grila mbetet me « Diagnostic gratuit ».

Skriptet u zgjeruan: `fix_degat_des_eaux.py` mban hapin B7, dhe
`verifiko_degat_des_eaux.py` ka dy kontrolle të reja — prania e gjashtë H2-ve
pyetëse dhe mungesa e dublimit të pyetjes së çmimit.

Provat: 7 gabime → **0** (exit 0); riekzekutim **0 skedarë**; **758 blloqe
JSON-LD** të sitit të rilexuara, 0 të pavlefshme; pariteti FAQ **13/13 identik**;
diff-i i tekstit të dukshëm i kufizuar në 7 tituj; rendering i verifikuar në
Chromium.

Pse u shmang dublimi: pa këtë, faqja do të mbante dy herë të njëjtën pyetje
(H2 + FAQ), gjë që dobëson pikërisht sinjalin GEO që kërkohej.

## ✅ Bashkuar dhe verifikuar në prodhim (24/08, 11:34 UTC)

PR #26 u bashkua nga Isufi (`main` = `60da3fa`). Kontrolli **live mbi
rushiti-renovation.fr** (jo mbi parapamje) konfirmoi të gjitha:

6 H2-të pyetëse ✅ · « la recherche de la fuite » ✅ · blloku i avis-eve
4,7/5 · 34 avis ✅ · `hasOfferCatalog` me 5 oferta ✅ · description-i
« devis assurance. » ✅ · barra mobile « Devis assurance » ✅ · pariteti FAQ
13/13 ✅ · 6 ankorat ✅ · dublimi JSON-LD i hequr edhe në grilë
(`/degat-des-eaux-planoise` i kontrolluar) ✅.

Asnjë korrigjim i nevojshëm pas deploy-it. `verifiko_degat_des_eaux.py` mbetet
vegla e regresit e silos — të ekzekutohet para çdo deploy-i të ardhshëm.

---

# Paketa 5 — koherenca e orarit (NAP) (24/08/2026)

| | |
|---|---|
| Data | 24/08/2026 |
| Objekti | Siti deklaronte **dy orare kontradiktore**, madje në të njëjtën faqe |
| Depoja e synuar | `eurotregu/rushiti-renovation` — PR [#27](https://github.com/eurotregu/rushiti-renovation/pull/27), degë `claude/horaires-nap-coherence`, 587 skedarë |
| Vendimi | Orari i vërtetë, i konfirmuar nga Isufi më 24/08: **Hën–Pre 7:00–20:30 · Sht 8:00–20:30 · Die 9:00–17:30** (7 ditë/javë) |

## Çfarë u konstatua

| Vendi | Para |
|---|---|
| `/contact`, blloku « Horaires » | Lundi – Vendredi : **8h – 18h** |
| Fundfaqja (755 faqe, përfshirë `/contact`) | Lun–Ven **7h – 20h30** · Sam 8h – 20h30 · Dim 9h – 17h30 |
| JSON-LD | 153 faqe me variantin e gjatë · **586 nyje pa asnjë orar** |

Vizitori i `/contact` lexonte «8h – 18h» lart dhe «7h – 20h30, e diel përfshirë»
poshtë. Meqë grafi JSON-LD bashkohet sipas `@id`, entiteti kishte orar të
ndryshëm sipas faqes së hyrjes. Për një sinistër të dielën në mbrëmje, kjo është
pikërisht e dhëna që konsultohet.

## Skedarët

| Skedari | Roli |
|---|---|
| `fix_horaires_nap.py` | Korrigjimi, **idempotent**: teksti i `/contact`, `openingHoursSpecification` në 586 nyjet e plota (futje me regex — prodhimi ka dy formate hapësire), plus `url` + `availableChannel` te nyja `Service` e pilierit. Shkruan vetëm nëse JSON-i mbetet i vlefshëm |
| `verifiko_horaires_nap.py` | **Vegla e përhershme e regresit NAP**: JSON i vlefshëm, çdo nyje biznesi me orar, **një variant i vetëm orari në gjithë sitin**, orari konform vendimit të 24/08, teksti i vjetër «Lun–Ven 8h–18h» i zhdukur, telefoni dhe adresa identike kudo |

## Përdorimi (mbi një checkout të depos së prodhimit)

```bash
python3 fix_horaires_nap.py /rruga/drejt/rushiti-renovation           # simulim
python3 fix_horaires_nap.py /rruga/drejt/rushiti-renovation --apply   # zbatim
python3 verifiko_horaires_nap.py /rruga/drejt/rushiti-renovation      # verifikim (exit 0 = konform)
```

## Prova e testimit

Mbi checkout-in real të prodhimit (`60da3fa`):

- verifikim **para**: 587 gabime; **pas**: **CONFORME — 0 gabime** (exit 0);
- riekzekutim i fix-it: **0 skedarë** (idempotencë e provuar);
- **758 blloqe JSON-LD** të rilexuara, **0 të pavlefshme**;
- **739 nyje biznesi, 1 variant i vetëm orari**;
- krahasim çelës për çelës: vetëm `openingHoursSpecification` (586),
  `url` dhe `availableChannel` (1) — asgjë tjetër;
- asnjë skedar i prekur jashtë JSON-LD-së, **përveç `contact.html`**;
- regresi i silos DDE mbetet **CONFORME**;
- rendering i `/contact` i verifikuar në Chromium (tre rreshtat e orarit).

## Të shmangura me qëllim

- **`geo`** — koordinatat e 18 rue du Professeur Haag duhen marrë nga fisha
  Google, jo të hamendësuara;
- **`aggregateRating`** — politika e Google për të dhënat e strukturuara i
  përjashton avis-et e vetëpublikuara për `LocalBusiness`: nuk do të jepte yje;
- **diversifikimi i ankorave** drejt pilierit — u propozua, pastaj u tërhoq pas
  leximit të markup-it: nga 150 lidhje, **75 janë fil d'Ariane** (duhet të
  pasqyrojnë `BreadcrumbList`) dhe **75 janë çipa të shkurtër** në një rresht
  etiketash lagjesh. Zgjatja e njërës ose tjetrës prish strukturën.

## Radhë për Isufin (jashtë kodit)

Të përputhet **fisha Google** dhe **PagesJaunes** me të njëjtin orar — koherenca
NAP luhet po aq jashtë sitit sa brenda tij.

---

# Paketa 5 — koherenca e orarit (NAP) (24/08/2026)

| | |
|---|---|
| Data | 24/08/2026 |
| Objekti | Siti deklaronte dy orare kontradiktore; 586 nyje biznesi s'deklaronin fare orar |
| Depoja e synuar | `eurotregu/rushiti-renovation` — **e zbatuar dhe e bashkuar** me autorizimin e Isufit: PR [#27](https://github.com/eurotregu/rushiti-renovation/pull/27), degë `claude/horaires-nap-coherence`, 587 skedarë |

## Çfarë u konstatua

Në **të njëjtën faqe** `/contact`: blloku « Horaires » shkruante « Lundi – Vendredi :
8h – 18h », ndërsa fundi i faqes (i pranishëm në 755 faqe) shkruante 7 h – 20 h 30,
7 ditë në javë. Në JSON-LD: 153 faqe e deklaronin variantin e gjatë, **586 nyje
`LocalBusiness` të plota nuk deklaronin asnjë orar**. Meqë grafi bashkohet sipas
`@id`, entiteti kishte orar të ndryshueshëm sipas faqes nga hynte motori.

Varianti i vërtetë, i konfirmuar nga Isufi më 24/08: **Hën–Pre 7 h – 20 h 30,
Sht 8 h – 20 h 30, Die 9 h – 17 h 30**.

## Skedarët

| Skedari | Roli |
|---|---|
| `fix_horaires_nap.py` | Korrigjimi, **idempotent**: teksti i `/contact`, `openingHoursSpecification` në 586 nyje, plus `url` + `availableChannel` te nyja `Service` e pilierit DDE |
| `verifiko_horaires_nap.py` | **Vegla e përhershme e regresit NAP**: JSON i vlefshëm, çdo nyje biznesi me orar, **një variant i vetëm orari** në gjithë sitin, përputhje me variantin e validuar, mungesë e tekstit të vjetër « 8h–18h », plus koherenca e telefonit dhe e adresës. Për t'u ekzekutuar para çdo deploy-i |

## Çfarë u shmang me vetëdije

- **`geo`**: koordinatat e 18 rue du Professeur Haag duhen lexuar nga fisha Google, jo hamendësuar;
- **`aggregateRating`**: politika e Google për të dhënat e strukturuara i përjashton avis-et e vetëpublikuara për `LocalBusiness` — nuk do të jepte yje;
- **diversifikimi i ankorave** drejt pilierit: nga 150 lidhje, **75 janë fill i Arianës** (duhet të pasqyrojnë `BreadcrumbList`) dhe **75 janë puleza të shkurtra** në një rresht etiketash lagjeje. Zgjatja do të prishte njërën ose tjetrën. Rekomandimi i mëparshëm u tërhoq pasi u lexua kodi.

## Prova e testimit dhe verifikimi pas bashkimit

- `verifiko_horaires_nap.py`: **587 gabime → 0** (exit 0);
- riekzekutim: **0 skedarë** (idempotencë);
- **758 blloqe JSON-LD** të rilexuara, 0 të pavlefshme; **739 nyje biznesi, një variant i vetëm orari**;
- krahasim çelës për çelës: vetëm `openingHoursSpecification` (586), `url` dhe `availableChannel` (1);
- asnjë skedar i prekur jashtë JSON-LD-së, përveç `contact.html`;
- regresi i silos DDE mbeti **CONFORME**;
- **verifikim pas bashkimit, në prodhim** (24/08): `/contact` shërben tri rreshtat e sakta,
  dhe `/cloisons-besancon` — faqe jashtë silos DDE — mban `openingHoursSpecification`
  me variantin e validuar në JSON-LD-në e saj live.

**Shënim metodologjik**: nxjerrja me LLM mbi përmbajtjen e faqes ktheu « pa orar »
për `/cloisons-besancon`, sepse firecrawl-i i heq tag-et `<script>` nga teksti që
i jep nxjerrësit. Verifikimi u bë mbi **rawHtml**-in e papërpunuar. Kur kontrollohet
JSON-LD live, lexohet kodi — kurrë përmbledhja.

## Çfarë i mbetet Isufit

Përputhja e **fishës Google** dhe e **PagesJaunes** me të njëjtin orar: koherenca
NAP luhet po aq jashtë sitit sa brenda tij.

---

# Paketa 6 — shëndeti i JSON-LD schema.org (31/08/2026)

| | |
|---|---|
| Data | 31/08/2026 |
| Objekti | Auditi i plotë i balisimit Schema.org — `docs/seo/audit-schema-org-2026-08-31.md` |
| Depoja e synuar | `eurotregu/rushiti-renovation` (prodhimi, 757 faqe, commit `3317674`) |

## Çfarë u konstatua

Baza është e shëndoshë (758 bllok JSON-LD, **0 gabime sintaksore**, `@id` i vetëm,
NAP i pandryshuar, 748 `BreadcrumbList` konforme). Tri konstate bllokuese:

- **766 pyetje FAQ të balisuara por të padukshme** në faqe (një pyetje zone për
  çdo faqe grile; te 10 artikujt e blogut e gjithë FAQ-ja mungon në HTML) dhe
  **99 përgjigje** që ndryshojnë nga teksti i shfaqur;
- **`zones-intervention.html`** deklaron `aggregateRating` 4,7/34 pa shfaqur as
  notë as avis; `index.html` e balison atë notë ndonëse doktrina e 22/08 e kishte
  përjashtuar shprehimisht;
- **15 URL imazhesh** të deklaruara në JSON-LD kthejnë 404 (dosja `assets/blog/`
  s'ekziston: 9 nga 11 artikujt).

## Skedarët

| Skedari | Roli |
|---|---|
| `verifiko_schema_org.py` | **Vegla e përhershme e regresit** për këto pesë kontrolle. Plotëson `verifiko_sameas.py` (`@id`, `sameAs`, orari) — të dyja duhet të kalojnë para çdo deploy-i |

## Përdorimi

```bash
python3 verifiko_schema_org.py /rruga/drejt/rushiti-renovation   # 0 = konform
```

Kontrolli i imazheve kapërcehet automatikisht mbi një checkout pa dosjen
`assets/` (p.sh. kopja GitHub Pages), për të mos dhënë gabime false.

## Prova e testimit

- mbi prodhimin: 756 faqe të lexuara, përmbledhja nxjerr saktësisht 766 / 99 / 15
  / 2 / 1 — të njëjtat shifra si auditi i pavarur i të njëjtës ditë;
- mbi këtë depo pas korrigjimit të dy faqeve: `✔ Konform`, dalje 0.

## Çfarë i mbetet Isufit

Arbitrazhi i doktrinës së avis-eve (heqje e `aggregateRating` në prodhim apo
rishikim i relevës së 22/08), dënominacioni social i saktë për `legalName`,
koordinatat GPS të adresës, dhe vendimi për pyetjen e zonës: të shfaqet apo të
hiqet nga balisimi.

---

# Paketa 7 — korrigjimet Schema.org pa arbitrazh (02/09/2026)

| | |
|---|---|
| Data | 02/09/2026 |
| Objekti | Zbatimi i pikave të auditit të 31/08 që **nuk presin asnjë vendim** nga Isufi (`../audit-schema-org-2026-08-31.md`, §7) |
| Depoja e synuar | `eurotregu/rushiti-renovation` (prodhimi, 757 faqe, commit `b7e42cb`) |
| Statusi | **Skript i shkruar dhe i provuar mbi prodhimin — i pazbatuar**, pret autorizimin e Isufit |

## Ndarja: çfarë hyn, çfarë pret

Auditi i 31/08 la 10 veprime dhe 6 arbitrazhe. Paketa 7 merr **vetëm** ato ku
korrigjimi është i pakundërshtueshëm — një shkelje e rregullave të Google, një
e dhënë faktikisht e gabuar, ose një veti falas. Çdo gjë që kërkon një vendim
mbetet jashtë, e paprekur.

| §7 | Veprimi | Paketa 7 |
|---|---|---|
| 1 | `aggregateRating` mbi `zones-intervention.html` | ✔ hapi **A** |
| 2 | doktrina e avis-eve mbi `index.html` | ⏸ **arbitrazh i Isufit** |
| 3 | vetia `image` e 9 artikujve pa vizual | ⏸ **arbitrazh i Isufit** |
| 4 | FAQ-ja e padukshme e 10 artikujve të blogut | ⏸ punë redaktoriale |
| 5 | pyetja e zonës e ~736 faqeve të grilës | ⏸ **arbitrazh i Isufit** |
| 6 | 99 përgjigje që ndryshojnë nga teksti | ✔ hapi **G** |
| 7 | `addressRegion` mbi `index.html` dhe `a-propos.html` | ✔ hapi **B** |
| 8 | `publisher` i blogut → `@id` kanonike | ✔ hapi **C** |
| 9 | `LocalBusiness` mbi `mentions-legales.html` | ✔ hapi **D** |
| 10 | `vatID`, `knowsAbout`, `url` mbi `Service` | ✔ hapat **E** dhe **F** |
| 10 | `geo` i unifikuar | ⏸ presin koordinatat e sakta |

Dy zgjedhje meritojnë shpjegim:

- **Hapi A nuk e prek `index.html`.** Skripti heq notën **vetëm nga faqet që
  s'e shfaqin** — aty ku balisimi është shkelje e qartë. Faqja e pritjes e
  shfaq notën 4,7/34 dhe të tre avis-et fjalë për fjalë: aty pyetja nuk është
  konformiteti por doktrina e 22/08, dhe vendimi i takon Isufit. Skripti e
  raporton këtë rast si `A~` («i ruajtur») pa e ndryshuar.
- **Hapi G shkon nga faqja drejt JSON-LD-së, kurrë e kundërta.** Përgjigjja e
  balisuar zëvendësohet me tekstin e `<div class="ans">` të vetë faqes. Asnjë
  fjalë nuk shkruhet: teksti i dukshëm mbetet i pandryshuar, prova më poshtë.
- **`legalName` nuk preket**, dhe nyja e re e `mentions-legales.html` nuk e
  mban: dënominacioni social pret K-bis-in (§8 e auditit).

## Skedarët

| Skedari | Roli |
|---|---|
| `fix_schema_org.py` | Korrigjimi në shtatë hapa, **idempotent**. Ndërhyrje tekstuale të synuara mbi JSON-LD-në: formatimi i bllokut ruhet, çelësat nuk rirenditen. Shkruan vetëm nëse çdo bllok mbetet JSON i vlefshëm |
| `verifiko_schema_org.py` | Vegla e regresit e paketës 6, e papërdorur ndryshe — mbetet kontrolli para çdo deploy-i |

## Përdorimi (mbi një checkout të depos së prodhimit)

```bash
python3 fix_schema_org.py /rruga/drejt/rushiti-renovation           # simulim
python3 fix_schema_org.py /rruga/drejt/rushiti-renovation --apply   # zbatim
python3 verifiko_schema_org.py /rruga/drejt/rushiti-renovation      # verifikim
```

## Prova e testimit (mbi një kopje të checkout-it real, `b7e42cb`)

Simulimi dhe zbatimi japin të njëjtat shifra — **755 skedarë**:

```
       1  A — notë/avis të vetëshpallur të hequr (faqe që s'i shfaq)
       2  B — addressRegion i korrigjuar
      12  C — publisher i lidhur me entitetin
       1  D — nyje identiteti e shtuar (mentions-legales)
    1480  E — vatID / knowsAbout të shtuar
     733  F — url i shtuar mbi nyje Service
      99  G — përgjigje FAQ e rigjeneruar nga faqja
```

Kontrollet pas zbatimit:

- **idempotencë e provuar**: riekzekutimi prek **0 skedarë**;
- **758 blloqe JSON-LD** të rilexuara me `json.loads`: **0 të pavlefshme**;
- **teksti i dukshëm i të 757 faqeve: identik bit për bit** para/pas —
  asnjë fjalë e shkruar, asnjë e fshirë;
- **asnjë skedar i ndryshuar jashtë JSON-LD-së**: HTML-ja me blloqet e
  maskuara është identike para/pas mbi të gjitha faqet;
- **krahasim çelës për çelës** mbi të 758 blloqet: të vetmet vlera të
  ndryshuara janë `addressRegion` (2) dhe `text` i përgjigjeve (99). Gjithçka
  tjetër është shtim ose heqje e pritur — `knowsAbout` (741 nyje), `vatID`
  (741), `url` (736), `@id` i publisher-it (12), nyja e `mentions-legales`,
  dhe të katër fushat e `aggregateRating` të `zones-intervention`;
- `verifiko_schema_org.py`: **99 përgjigje divergjente → 0**, `aggregateRating`
  2 → 1 dhe `review` 1 → 1 (të dyja mbi `index.html`, të ruajtura me qëllim).
  Mbeten 766 pyetjet e padukshme dhe 15 imazhet — të dyja në pritje të
  arbitrazhit, siç ishte parashikuar;
- **të pesë veglat e tjera të regresit** (`verifiko_sameas`,
  `verifiko_horaires_nap`, `verifiko_degat_des_eaux`, `verifiko_demande_rapide`,
  `verifiko_papier_peint`) japin **exit 0 para dhe pas** — asnjë fitim i
  mëparshëm i prishur;
- mbi **këtë depo** (kopja GitHub Pages): **0 skedarë të prekur**. Dy faqet e
  korrigjuara me dorë më 31/08 janë tashmë konforme — skripti konvergjon me to,
  provë e kryqëzuar që rregullat e tij janë të njëjtat.

## Çfarë pret Isufi

1. **Autorizimin e zbatimit** mbi prodhimin (755 skedarë, vetëm JSON-LD).
2. Gjashtë arbitrazhet e §8 të auditit, të pandryshuara.

---

# Paketa 8 — 766 pyetjet FAQ të padukshme (02/09/2026)

| | |
|---|---|
| Data | 02/09/2026 |
| Objekti | Konstati **P1-1** i auditit të 31/08, i vetmi konstat bllokues që mbetej pa vegël |
| Depoja e synuar | `eurotregu/rushiti-renovation` (prodhimi, 757 faqe, commit `b7e42cb`) |
| Statusi | **Skript i shkruar dhe i provuar — i pazbatuar**, pret arbitrazhin dhe autorizimin e Isufit |

## Problemi

Google e kërkon shprehimisht: përmbajtja e një `FAQPage` duhet të jetë e
dukshme për vizitorin mbi faqen që e balison. Përmbajtje që jeton vetëm në
JSON-LD është shkelje e rregullave, e ndëshkueshme me veprim manual.

Auditi numëroi **766 pyetje** të tilla, në dy familje:

- **grila, 681 faqe** — gabariti shton në balisim një pyetje zone që nuk jepet
  kurrë në HTML: « Vous déplacez-vous à Avanne-Aveney ? », ose për lagjet
  « Intervenez-vous dans le quartier Velotte ? » ;
- **blogu, 9 artikuj (29 pyetje)** — i gjithë seksioni FAQ mungon nga trupi i
  artikullit. Artikulli i dhjetë, `blog/reparer-plafond-degat-des-eaux-besancon.html`,
  e shfaq të vetin — **ai është gabariti i ndjekur këtu, fjalë për fjalë**.

## Dy rrugë, arbitrazhi i Isufit

`fix_faq_dukshme.py` i mban të dyja dhe nuk vendos në vend të tij:

| Mënyra | Çfarë bën | Kosto |
|---|---|---|
| `--afisho` *(parazgjedhje, rekomandimi i auditit)* | E bën të dukshme pyetjen që tashmë ekziston në balisim | Faqja fiton një pyetje-përgjigje të vërtetë |
| `--hiq` | Heq nga JSON-LD pyetjet që faqja nuk i shfaq | Faqja humbet përmbajtje |

**Asnjë fjalë nuk shkruhet në asnjërën mënyrë.** Në `--afisho` teksti vjen
fjalë për fjalë nga `acceptedAnswer`, i shkruar dhe i validuar më parë. I
vetmi tekst që nuk vjen nga balisimi është titulli i seksionit
« Questions fréquentes » i 9 artikujve — i kopjuar nga gabariti i faqes së
dhjetë, jo i shpikur.

Rekomandimi mbetet ai i auditit: **`--afisho`**. « Vous déplacez-vous à X ? »
është pyetja që klienti bën vërtet, dhe përgjigjja — deplasim i përfshirë,
diagnostikë falas pa angazhim — është pikërisht ajo që e bind. Fshehja e saj
humbet një përgjigje të mirë dhe nuk fiton asgjë.

## Përdorimi (mbi një checkout të depos së prodhimit)

```bash
python3 fix_faq_dukshme.py /rruga/drejt/rushiti-renovation                    # simulim
python3 fix_faq_dukshme.py /rruga/drejt/rushiti-renovation --afisho --apply
python3 fix_faq_dukshme.py /rruga/drejt/rushiti-renovation --hiq --apply
```

## Prova e testimit (mbi kopje të checkout-it real, `b7e42cb`)

Të dyja mënyrat: **690 skedarë, 766 pyetje** (681 grilë + 9 blog), dhe të dyja
e kthejnë kontrollin e pyetjeve të padukshme në **0**.

- **idempotencë e provuar** në të dyja mënyrat: 2ᵉ passe → 0 skedarë;
- **simetri e provuar**: `--afisho` nuk prek asnjë bllok JSON-LD (0 faqe) dhe
  pasuron tekstin e dukshëm (690); `--hiq` nuk prek asnjë fjalë të tekstit të
  dukshëm (0) dhe lehtëson balisimin (690);
- **balanca e tageve** `details`, `summary`, `section`, `article`, `div`,
  `main`: e mbyllur mbi të 757 faqet, në të dyja mënyrat;
- **prova që asgjë nuk është shpikur**: mbi të 681 faqet e grilës, **çdo fjalë
  e shtuar** gjendet në JSON-LD-në e vetë faqes. Mbi 9 artikujt, e njëjta gjë
  plus titulli i seksionit i gabaritit;
- **rendering i verifikuar në Chromium**: pyetja e zonës del si `<details>` i
  fundit i FAQ-së ekzistuese; seksioni FAQ i blogut del para CTA-së, si te
  gabariti;
- **të pesë veglat e tjera të regresit**: exit 0.

### Zinxhiri paketa 7 + paketa 8

Të dy urdhrat e zbatimit (7→8 dhe 8→7) japin një rezultat **identik bit për
bit**. Bashkë, ato e ulin auditin nga **883 konstate në 17** — dhe të 17-tat
janë saktësisht dy arbitrazhet e mbetura:

```
      15  imazh i deklaruar që s'ekziston     → vizualet e 9 artikujve
       1  aggregateRating mbi biznesin        → doktrina e avis-eve (index.html)
       1  review mbi biznesin                 → e njëjta doktrinë
```

758 blloqe JSON-LD të rilexuara pas zinxhirit: **0 të pavlefshme**.

## Çfarë pret Isufi

1. **Arbitrazhi**: `--afisho` apo `--hiq` ?
2. **Autorizimi i zbatimit** mbi prodhimin, për paketën 7 dhe këtë.

---

## ✅ Zbatimi i paketave 7 dhe 8 në prodhim (02/09/2026, 15:44 UTC)

Me autorizimin e Isufit dhe arbitrazhin e tij `--afisho`, të dyja paketat u
zbatuan mbi prodhimin: PR [#30](https://github.com/eurotregu/rushiti-renovation/pull/30),
degë `claude/paketat-7-8-schema-org-faq`, **755 skedarë**, e bashkuar nga Isufi
(`main` = `19079d8`).

Auditi i 31/08 ra nga **883 konstate në 17** — dhe të 17-tat janë saktësisht
dy arbitrazhet e mbetura (15 imazhe, 2 rreshta avis-esh).

### Verifikimi live mbi `rushiti-renovation.fr` (jo mbi parapamje)

Lexuar mbi **rawHtml**-in e papërpunuar, kurrë mbi përmbledhjen e LLM-së —
metoda e vendosur që nga paketa 5. Një provë e parë me nxjerrje LLM ktheu
tekstin e dukshëm në vend të balisimit: prandaj lexohet kodi.

| Faqja | Konstati |
|---|---|
| `/cloisons-avanne-aveney` | « Vous déplacez-vous à Avanne-Aveney ? » shfaqet në `<summary>` — pyetja del **2 herë** në burim (JSON-LD + HTML i dukshëm), 6 `<details>` në vend të 5 ✔ |
| `/mentions-legales` | nyja `LocalBusiness` e plotë: `@graph`, `taxID`, `vatID`, `founder` Isuf & Yll, orari, `sameAs`, `knowsAbout` ✔ · `legalName` **mungon**, siç ishte parashikuar (pret K-bis-in) ✔ |
| `/zones-intervention` | `aggregateRating` i hequr ✔ |

### ⚠️ Konstat i papritur: Worker-i e mbishkruan hapin B

**`addressRegion` shërbehet si « Doubs », jo si « Bourgogne-Franche-Comté ».**

Depoja e bashkuar mban « Bourgogne-Franche-Comté » në **741 faqe**, asnjë
« Doubs ». Por Worker-i `image-license-jsonld` (i modifikuar më 02/09 në 11:05
UTC, pra **para** zbatimit të paketave) e rishkruan në fluturim, rreshti 450:

```js
// --- Ajout 2026-09-02 (autorisé par Isuf) : uniformisation addressRegion + bloc avis ---
html = html.split('"addressRegion":"Bourgogne-Franche-Comté"').join('"addressRegion":"Doubs"');
```

Pra hapi **B** i paketës 7 është i anuluar në prodhim. Dy burime të vërtete
që divergojnë: depoja thotë një gjë, faqja e shërbyer një tjetër.

**Fakti i schema.org**: `addressRegion` pret « the first-level Administrative
division ». Në Francë kjo është **rajoni** (Bourgogne-Franche-Comté);
departamenti (Doubs) është i nivelit të dytë. Auditi i 31/08 e konstatoi
pikërisht këtë (§P2-2), dhe PR #51 — që propozonte « Doubs » — u rekomandua
për mbyllje po për këtë arsye.

**Vendimi i takon Isufit.** Worker-i nuk u prek. Dy dalje të mundshme:
heqja e rreshtit 450 (depoja bëhet burimi i vetëm), ose kthimi i depos në
« Doubs » (Worker-i bëhet i panevojshëm për këtë pikë). Të mbeten të dyja
siç janë do të thotë që një audit i ardhshëm do ta rihapë sigurisht çështjen.

### Çfarë NUK preket nga Worker-i

Kontroll i të ~60 rishkrimeve të Worker-it: **asnjë nuk prek `<details>` as
`acceptedAnswer`** → **paketa 8 është e paprekur**, e provuar live.

Worker-i injekton edhe një bllok « Avis clients » mbi faqet jashtë blogut që
s'e kanë (kushti: përmban « Questions fréquentes » dhe jo « Avis clients »).
`zones-intervention` s'ka asnjërën → nota nuk shfaqet aty → **heqja e
`aggregateRating` mbetet e drejtë** edhe duke marrë parasysh Worker-in.

### Radhë për Isufin

1. **Arbitrazhi `addressRegion`**: Worker-i apo depoja?
2. Imazhet e 9 artikujve · doktrina e avis-eve te faqja e pritjes ·
   `legalName` në K-bis · koordinatat GPS të adresës.

---

# Paketa 9 — përmasat e imazheve sociale (02/09/2026)

| | |
|---|---|
| Data | 02/09/2026 |
| Objekti | Konstati **P1-2** i auditit të Twitter Cards (31/08): 18 faqe deklarojnë përmasa imazhi që s'përputhen me skedarin |
| Depoja e synuar | `eurotregu/rushiti-renovation` — PR [#32](https://github.com/eurotregu/rushiti-renovation/pull/32), **18 skedarë** |
| Arbitrazhi i Isufit (02/09) | **vetëm përmasat** — jo blloku i balizave twitter |

## Pse vetëm përmasat

Open Graph — që e lexojnë Facebook, Instagram, WhatsApp dhe LinkedIn — është
tashmë i pranishëm në **756 nga 757 faqe**. RUSHITI **nuk ka llogari X**
(sameAs: Facebook, Instagram, Google, PagesJaunes, Annuaire, INPI, rushiti.fr).

Balizat `twitter:*` nuk do të ndryshonin asgjë të dukshme mbi kanalet reale;
përmasat e gabuara po. Prandaj `fix_twitter_cards.py` mori opsionin
**`--vetem-permasat`**, që kapërcen bllokun A–C.

Pa opsion: **756 faqe**. Me opsion: **18 faqe**, saktësisht ato me defekt.

## Çfarë ishte e gabuar

**Përmbysje portret / peizazh** — pamja shpallej e shtrirë ndërsa imazhi është
në këmbë:

| Faqja | Deklaruar | Real |
|---|---|---|
| `amenagement-commerce-bureau-besancon` | 1104×828 | **828×1104** |
| `cloisons-besancon` | 900×1200 | **828×1104** |
| `degat-des-eaux-besancon` | 900×1200 | **828×1104** |

**Devijime të forta** — shtatë faqe shpallnin 1104×828 për një imazh
**413×224**: `entreprise-renovation`, `expert-assurance-sinistre`,
`prix-travaux-renovation`, `renovation-appartement`, `renovation-cuisine`,
`renovation-salle-de-bain`, `renovation-syndic-gestionnaire`.

Përmasat e deklaruara vijnë tani nga **leximi binar i çdo skedari imazh**,
kurrë nga një vlerësim.

## Përdorimi

```bash
python3 fix_twitter_cards.py /rruga/drejt/rushiti-renovation --vetem-permasat           # simulim
python3 fix_twitter_cards.py /rruga/drejt/rushiti-renovation --vetem-permasat --apply   # zbatim
# hapat A–C (shtimi i kartave) janë të pensionuar — shih paketën 10
```

## Prova e testimit

Mbi një kopje të checkout-it të prodhimit, para zbatimit:

- **idempotencë e provuar**: kalimi i dytë → 0 skedarë;
- **teksti i dukshëm identik** mbi të 757 faqet;
- **asnjë balizë `twitter:` e shtuar** — modaliteti i kufizuar u respektua;
- **krahasim çelës për çelës**: të vetmet vlera të ndryshuara janë
  `og:image:width` dhe `og:image:height`, **nga 18 herë secila**;
- pesë veglat e regresit të mëparshme: **exit 0**; `verifiko_schema_org`
  mbetet me 17 konstatet e veta në pritje arbitrazhi, të pandryshuara.

## Çfarë i mbetet Isufit

1. **Tri faqe pa imazh social** — `blog.html`, `contact.html`,
   `mentions-legales.html`. Skripti i sinjalizon pa i prekur: zgjedhja e
   vizualit është vendim redaktorial.
2. **Shtatë imazhe shumë të vogla** — korrigjimi i përmasës e bën atë të
   saktë, jo më të madhe. Një imazh 413×224 do të mbetet miniaturë e vogël.
   Për një pamje me gjerësi të plotë duhen vizuale rreth **1200×630**.

## Shënim mbi PR #61

Skedari i versionuar këtu tani mban opsionin `--vetem-permasat`. PR #61 mbetet
i dobishëm për auditin dhe vegëlën e verifikimit, por versioni i tij i
skriptit është i mëparshëm: në rast bashkimi, mbahet ky.


---

# Paketa 10 — heqja e plotë e kartave Twitter (02/09/2026)

`fix_hiq_twitter.py`

## Vendimi

Auditi i 31/08 e kishte nxjerrë mungesën e kartave Twitter si mangësi, dhe
inventari i 02/09 e kishte renditur atë të parën « sipas vlerës ». Ai renditje
ishte i saktë vetëm në një kuptim shumë të ngushtë — e vetmja paketë e
mjetuar dhe kurrë e zbatuar — dhe **mashtrues mbi interesin real**: RUSHITI
nuk ka llogari X, ndërsa Facebook, WhatsApp, Instagram dhe LinkedIn lexojnë
të gjitha Open Graph, i cili është i plotë mbi 756 nga 757 faqe.

Isufi vendosi: heqje e plotë.

## Çfarë u hoq

31 faqe mbanin secila një balizë të vetme, `<meta name="twitter:card"
content="summary_large_image">`, gjithnjë midis `og:image:alt` dhe
`og:site_name`. Asnjë `twitter:title`, `twitter:description`,
`twitter:image` apo `twitter:image:alt` nuk ekzistonte askund në sit.

Skripti i mbulon të shtatë çelësat `twitter:*`, jo vetëm `card`: një gabarit
i vjetër ose një degë e vjetër mund ta rifusë ndonjërin, dhe kalimi i
ardhshëm duhet ta kapë.

## Kushti i sigurisë

X-i, kur nuk gjen `twitter:*`, **bie prapa mbi Open Graph**. Prandaj heqja
nuk humbet asgjë — as mbi X-in vetë — sa kohë faqja ka `og:title` dhe
`og:image`. Skripti e verifikon këtë para çdo shkrimi dhe e lë të paprekur
çdo faqe që nuk i ka të dyja. Mbi të 31 faqet, kushti ishte i plotësuar.

## Prova e testimit

Mbi një kopje të checkout-it të prodhimit (`7a22e0a`):

- **31 skedarë të prekur, 31 baliza të hequra**, të gjitha `twitter:card`;
- **idempotencë**: kalimi i dytë → 0 skedarë;
- **asnjë ndryshim tjetër**: për secilin nga 31 skedarët, heqja e balizës nga
  versioni i mëparshëm jep **saktësisht** versionin e ri, bajt për bajt;
- **asnjë balizë `og:*` e ndryshuar** në asnjë skedar;
- **teksti i dukshëm identik** mbi të 757 faqet;
- **758 blloqe JSON-LD**, të gjitha të vlefshme;
- gjashtë veglat e regresit: exit 0, përveç `verifiko_schema_org` që kthen
  **saktësisht të njëjtat 17 konstate** si para heqjes (15 imazhe bloge që
  mungojnë + 2 fusha avisi mbi faqen e nisjes) — pra heqja nuk prek asgjë
  nga balisimi.

## Veglat e prekura

- `verifiko_twitter_cards.py` → **`verifiko_apercus_sociaux.py`**. Kontrolli
  u përmbys: në vend që të kërkojë praninë e `twitter:*`, ai tani sinjalizon
  **rikthimin** e ndonjërës. Pjesa tjetër — `og:url` == kanonike, ekzistenca
  e `og:image`, saktësia e përmasave, cilësia e vizualit — mbeti e paprekur,
  sepse ajo kurrë nuk kishte të bënte me X-in.
- `fix_twitter_cards.py` → hapat A–C **refuzojnë të ekzekutohen** pa
  `--vetem-permasat`. Skedari nuk u fshi: hapi D (korrigjimi i përmasave
  `og:image:*`) mbetet i vlefshëm dhe i pavarur nga X-i.

## Kopja GitHub Pages

`syndic-copropriete-besancon.html` e kësaj depoje mbante të njëjtën balizë.
E hequr në të njëjtin kalim, me të njëjtin skript.

## Çfarë i mbetet Isufit — i pandryshuar

Heqja e kartave **nuk e zgjidh** çështjen e vizualeve: `og:image` mbetet
burimi i vetëm i paraqitjes sociale mbi të gjitha rrjetet, dhe asnjë imazh i
sitit nuk arrin 1200 px gjerësi. `verifiko_apercus_sociaux.py` numëron 712
paralajmërime mbi këtë — imazhe portret ose nën 600×315. Prodhimi i vizualeve
rreth **1200×630** mbetet arbitrazhi i vetëm i hapur mbi këtë temë.

## Verifikimi live pas bashkimit

PR e prodhimit u bashkua nga Isufi më 02/09 në 17:25 UTC. Tri faqe të lexuara
live mbi **rawHtml** të papërpunuar (`/isolation-besancon`, `/merci`,
`/degat-des-eaux-besancon`): **asnjë balizë `twitter:`**, dhe të dhjetë çelësat
`og:*` të paprekur. Mbi `/isolation-besancon`, `og:image:alt` ndiqet tani
drejtpërdrejt nga `og:site_name` — pikërisht vendi ku ishte baliza.

⚠ **Kurth i ambientit, i verifikuar më 02/09.** `curl` drejt
`rushiti-renovation.fr` nuk kalon: proxy-ja e ambientit i përgjigjet `403` çdo
CONNECT, dhe curl kthen **0 bajt me kod 000**. Një `grep` mbi një përgjigje të
zbrazët nuk gjen asgjë — pra një kontroll i tipit « a ka mbetur baliza? » del
**i suksesshëm rrejshëm**, dhe një kontroll i tipit « a ka ende `og:title`? »
del **i dështuar rrejshëm**. Verifikimi live bëhet vetëm përmes Firecrawl-it,
i cili e merr faqen nga ana e vet. Kjo shtohet te kurthi tashmë i njohur i
paketës 5: lexoni **rawHtml**, kurrë përmbledhjen e LLM-së.

---

# Paketa 11 — mbrojtja anti-robot hCaptcha e formularëve (02/09/2026)

| | |
|---|---|
| Data | 02/09/2026 |
| Objekti | 17 dërgesa automatike në një minutë (21h23–21h24) mbi formularin e `/peinture-interieure-besancon`: skanim SQL injection, fushat bosh, kodi i sulmit në fushën `consentement`. Asnjë dëm i mundshëm (Web3Forms, pa bazë të dhënash), 17 e-mailet klasifikuar spam |
| Depoja e synuar | `eurotregu/rushiti-renovation` — **klon vetëm-lexim** në këtë seancë; skripti testuar mbi HTML-në reale, zbatimi në prodhim pret autorizimin e Isufit |
| Dokumenti | `../../formulaire-demande-rapide-variante-b.md` (« Mise à jour du 02/09/2026 ») |

## Pse honeypot-i nuk mjaftoi

`botcheck` kap robotët që plotësojnë çdo fushë. Një skaner dobësish e rimerr
formularin siç është dhe ndryshon **një fushë në herë**: kutinë e fshehur nuk e
shënon kurrë. Duhet një provë që roboti nuk e kalon dot: hCaptcha e Web3Forms
(pa çelës të vetin, pa regjistrim, çelësi i përbashkët i planit falas
injektohet nga skripti i tyre).

## Skedarët

| Skedari | Roli |
|---|---|
| `fix_hcaptcha_formular.py` | Shton në 31 faqe (30 pilier + `contact.html`) widget-in `h-captcha` para butonit « Envoyer », skriptin Web3Forms dhe kontrollin inline (mesazh në frëngjisht nëse kutia s'është shënuar) para `</body>`. **Idempotent** |
| `verifiko_demande_rapide.py` | Zgjeruar: kontrollon tre elementët hCaptcha mbi 30 faqet pilier dhe mbi `/contact` (kontroll i ri) |

## Prova e testimit (02/09, mbi kopjen e klonit të prodhimit, commit `b838f92`)

- `verifiko` para: 31 GABIM (hCaptcha mungon kudo) — pritej;
- `fix` simulim: 31 DO SHTOHEJ, 0 probleme; `--apply`: 31 SHTUAR;
- `verifiko` pas: **0 probleme** (30 pilier + `/contact` + `/merci`);
- rizbatim: **0 ndryshime** (idempotencë e provuar);
- `node --check` mbi skriptin inline: OK.

Dy kurthe të kapura gjatë testimit: (1) `peinture-facade-isolation-exterieure`
mban `<p><button…>` pa `class="u35"` — ankora u bë regex; (2) selektori i
skriptit inline nuk duhet të përmbajë vargun e plotë `action="…/submit"`, se
`verifiko` e numëron dhe gjen 2 formularë.

## Çfarë i mbetet Isufit — i domosdoshëm

1. **Aktivizimi i hCaptcha në panelin Web3Forms** (app.web3forms.com →
   formulari me çelësin `1aee0248-…`). Pa të, widget-i shfaqet por dërgesat pa
   captcha kalojnë ende. Radha: **së pari kodi në prodhim, pastaj aktivizimi**
   — e kundërta do t'i bllokonte të gjitha dërgesat.
2. `/simulateur-peinture` poston me fetch JSON pa widget: pas aktivizimit bie
   te fallback-u `mailto:`. Trajtim i veçantë ose çelës i dytë — [À COMPLÉTER].
3. Mentions légales: hCaptcha (Intuition Machines) si nën-përpunues — [À COMPLÉTER].

## Përdorimi (mbi një checkout të depos së prodhimit)

```bash
python3 fix_hcaptcha_formular.py /rruga/drejt/rushiti-renovation           # simulim
python3 fix_hcaptcha_formular.py /rruga/drejt/rushiti-renovation --apply   # zbatim
python3 verifiko_demande_rapide.py /rruga/drejt/rushiti-renovation         # 0 probleme = konform
```

## Kopja GitHub Pages

`index.html`, `js/main.js`, `css/style.css` të kësaj depoje: i njëjti widget,
i njëjti skript Web3Forms, kontrolli në `main.js` (mesazh te `.form-status`).
