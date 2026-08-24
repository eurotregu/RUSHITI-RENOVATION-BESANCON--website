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
