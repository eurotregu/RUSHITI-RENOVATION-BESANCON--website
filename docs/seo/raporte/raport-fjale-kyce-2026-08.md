# Raporti i fjalëve kyçe #1 — rushiti-renovation.fr — 21/08/2026

*Prodhuar nga `rushiti-keyword-map` (mënyra SINKRONIZIMI + RAPORTI), mbi tre eksportet Search Console të ngarkuara nga Isufi më 21/08/2026: (1) i përgjithshëm Web 12 muaj, (2) kryqëzimi «isolation besançon», (3) kryqëzimi «isolation intérieure besançon». Asnjë shifër e shpikur; çdo vlerë vjen nga eksportet ose nga burimet e mëparshme të datuara.*

## 1. KPI — fotografia 12-mujore

⚠️ **Shënim metodologjik:** baseline-i i propozimit ishte 3-mujor (17/05–16/08). Eksporti i sotëm është **12-mujor**, pra i pakrahasueshëm rresht për rresht me të; nga raporti #2 e tutje krahasimi bëhet periudhë me periudhë. Të dyja fotografitë:

| Tregues | 12 muaj (deri 21/08/2026) | 3 muaj (17/05–16/08, referencë) |
|---|---|---|
| Klikime | **281** | 52 |
| Impresione | **24 868** | 5 670 |
| CTR | 1,13 % | 0,9 % |
| Pozicioni (i peshuar me impresione) | 10,4 | 14,3 |
| Faqe me impresione | **394** nga ~755 të sitemap-it aktual | 217 nga 1 395 |
| Kërkesa të regjistruara | 779 | 238 |

**Përqendrimi ekstrem i dukshmërisë:** faqja kryesore mbart **222 nga 281 klikime (79 %)** dhe 19 770 impresione me pozicion 9,2. Artikulli i moisissure-s shton 1 385 impresione. Faqet e shërbimeve, të gjitha së bashku, mbeten të varrosura në faqet 2–5 të Google — kjo është saktësisht ajo që regjistri dhe plani i forcimit synojnë të ndryshojnë.

## 2. ✅ Kontrolli i sigurisë së konsolidimit — I KALUAR

Pyetja kritike e planit («a fshiu konsolidimi ndonjë faqe që printonte?») tani ka përgjigje të matur:

- **645 URL burime** të ridrejtimeve 301 në `_redirects` u kryqëzuan me 394 faqet që kishin impresione në 12 muaj;
- vetëm **9 URL të ridrejtuara kishin ndonjë të dhënë**: **0 klikime, 10 impresione gjithsej**, të gjitha në pozicione 43–89 (praktikisht të padukshme; kryesuesja: `/vitrification-parquet-chaudefontaine`, 2 impresione, poz. 61);
- **verdikt: konsolidimi nuk dogji asnjë faqe me vlerë.** Kushti i planit («asnjë faqe që printon nuk fshihet») rezulton i respektuar. Asnjë ridrejtim nuk kërkon kthim mbrapsht.

## 3. Verdikti isolation / ITI — kanibalizim jo, padukshmëri po

Nga dy kryqëzimet e dedikuara (12 muaj):

| Kërkesa | Faqet që printojnë realisht | Impresione / pozicion |
|---|---|---|
| isolation besançon | vetëm `/isolation-besancon` | 29 impr., poz. 36,7, 0 klikime |
| isolation intérieure besançon | `/isolation-besancon` + `/` (accueil) | 23 impr. poz. 25,7 + 12 impr. poz. 23,5 |

- **Nuk ka kanibalizim aktiv** mes dy faqeve të izolimit: `/isolation-interieure-besancon` **nuk shfaqet fare** — as për kërkesën e saj ekzakte, as njëherë të vetme në 12 muaj (mungon nga lista e 394 faqeve me impresione).
- Skorimi sipas formulës (P = 1,0 — të gjitha impresionet e kërkesës ITI bien mbi URL jo-kanonike; T i ulët — balizat të diferencuara në kod; R = 0): **SKOR ≈ 40 → 🟠**.
- **Veprimi**: jo kirurgji balizash (konfirmohet addendum-i i auditit), por **forcim + maillage me ankora ekzakte** «isolation intérieure (ITI) à Besançon» nga accueil, platrerie, doublage dhe artikulli ITI/ITE drejt faqes së dedikuar. → `rushiti-maillage-interne` + `rushiti-brief-seo`.

## 4. Modeli i përsëritur: faqja kryesore eklipson faqet e dedikuara

E njëjta strukturë shfaqet në tre vende — dhe është gjetja qendrore e raportit:

| Kërkesa (12m) | Impresione | Poz. | Klikime | Faqja e dedikuar | Gjendja e saj |
|---|---|---|---|---|---|
| entreprise de peinture à besançon | **1 343** | **3,5** | **0** | `/peinture-interieure-besancon` | 198 impr., poz. 25,6 |
| entreprise de peinture besançon | 324 | 2,3 | 2 | po ajo | — |
| plaquiste besancon (pa theks) | 899 | 3,3 | 15 | `/plaquiste-besancon` | **0 impresione 12m** |
| plaquiste besançon (me theks) | 252 | 6,0 | 6 | po ajo | — |
| isolation intérieure besançon | 35 | ~25 | 0 | `/isolation-interieure-besancon` | **0 impresione 12m** |

Leximi: kërkesat komerciale më të mëdha të sitit i shërben **faqja kryesore** (title-i i saj «Peintre & plaquiste à Besançon»), ndërsa faqet e dedikuara nuk hyjnë fare në SERP. **1 343 impresione në pozicionin 3,5 me zero klikime** te «entreprise de peinture à besançon» është gisement-i më i madh i vetëm i sitit — dymbëdhjetëfishi i asaj që tregonte fotografia 3-mujore.

**Veprimet** (pa prekur faqen kryesore, që sjell 79 % të klikimeve):
1. Matja e efektit të title-ve të rinj CTR të shpërndarë sot (4–6 javë) → `rushiti-regression-seo`;
2. Maillage i brendshëm me ankora ekzakte drejt `/peinture-interieure-besancon` dhe `/plaquiste-besancon` → `rushiti-maillage-interne`;
3. Në eksportin e ardhshëm: kryqëzimi kërkesë × faqe për «entreprise de peinture à besançon» (15 min në GSC), për të parë me saktësi cila faqe printon dhe si lëviz pas maillage-it.

## 5. Porta e krijimit — verdiktet me dëshmi për faqet e reja

| Faqja | Dëshmia 12m | Verdikti i portës |
|---|---|---|
| `/renovation-salle-de-bain-besancon` (P1) | «artisan rénovation salle de bain» 130 impr. poz. 19,1 · «artisan salle de bain» 119 impr. poz. 20,1 · 54 kërkesa «salle de bain» gjithsej, të shërbyera sot nga artikulli i moisissure-s dhe accueil | **LEJOHET** — kërkesë reale, e pashërbyer nga asnjë faqe e dedikuar |
| `/entreprise-renovation-besancon` (P2) | «entreprise de rénovation besançon» 17 impr. poz. 13,2 · «entreprise de rénovation maison» 18 impr. poz. 20,7 · «rénovation maison besançon» 2 impr. | **LEJOHET** — kërkesë e provuar, faqja mungon |
| `/renovation-cuisine-besancon` (P3) | **0 kërkesa** me «cuisine» në 779 kërkesat e 12 muajve | **LEJOHET ME KUSHTE** — s'ka dëshmi kërkese (normale: s'ka as përmbajtje që të printonte); kalon **pas** P1 dhe P2, me volum për t'u validuar në Keyword Planner |

## 6. Dëshmi të tjera që hynë në regjistër (12m)

peintre besançon 187 impr. poz. 6,0 · marka shëndoshë: «rushiti besancon» 443 impr. poz. 2,4 (26 klik.), «rushiti rénovation - peintre plaquiste besançon» 412 impr. (13 klik.) — anomalia mbetet vetëm te vargu i domenit · enduit à la chaux 41 impr. poz. 5,0 · renov bois 58 impr. poz. 6,2 · faqet pilar: platrerie 504/21,8 · ratissage 413/18,4 · papier-peint 201/14,0 · revetements-sol 197/30,5 · toile-de-verre 115/29,7 · cloisons 91/35,8 · degat-des-eaux 33/16,0 · faux-plafonds 33/48,0 · peinture-exterieure 76/17,4 · renovation-appartement **2 impr.** (i dobët — për forcim para se t'i shtohen motra) · contact 183/6,5 · `/ravalement-facade-besancon` pa asnjë të dhënë 12m — **fusion-i 301 konfirmohet i drejtë**.

## 7. Radha e veprimeve (e peshuar me vlerë biznesi)

1. 🔴 **Krijimi i `/renovation-salle-de-bain-besancon`** (porta LEJOHET) — PR në depon e prodhimit për miratim.
2. 🔴 **Maillage ankora-ekzakte** drejt peinture-interieure, plaquiste dhe ITI (gjetja § 4) → `rushiti-maillage-interne`.
3. 🟠 Forcimi i `/degat-des-eaux-besancon` (33 impr./12m — silo më fitimprurëse, ende e padukshme) → `rushiti-brief-seo`.
4. 🟠 Krijimi i `/entreprise-renovation-besancon` (P2, LEJOHET).
5. 🟡 Matja e efektit të korrigjimeve të shpërndara sot: rishikim më ~1 tetor → `rushiti-regression-seo`.
6. 🟡 P3 cuisine pas validimit të vëllimit në Keyword Planner.

**Përditësim i mbrëmjes (21/08):** veprimi 2 u ekzekutua — PR maillage [eurotregu/rushiti-renovation#19](https://github.com/eurotregu/rushiti-renovation/pull/19) me ankorat ekzakte drejt tri faqeve të eklipsuara — **MERGED nga Isufi më 21/08 në 18:37 UTC**, pas verifikimit tim të parapamjes Cloudflare (CI i gjelbër, paragrafi i renderuar saktë). Verifikuar gjithashtu live: trashëgimia WordPress trajtohet me ridrejtime — `/rafraichissement-piscines-besancon/` → 301 → `/peinture-interieure-besancon`.

*Raporti #2 (fund shtatori 2026) do të krahasojë periudhë me periudhë dhe do të masë efektin e dé-duplikimit, të title-ve të rinj dhe të maillage-it. Asnjë pozicion nuk premtohet.*
