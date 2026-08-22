# Verifikim — `sameAs` në JSON-LD LocalBusiness

| | |
|---|---|
| Data | 22/08/2026 |
| Pyetja | A e lidh `sameAs` i bllokut JSON-LD LocalBusiness URL-në e faqes me profilin e **PagesJaunes**, **Google Maps** dhe **regjistrat tregtarë**? |
| Perimetri | `eurotregu/rushiti-renovation` (prodhimi, 757 faqe HTML, commit `abcdd34`) + kjo depo (kopja GitHub Pages, 3 faqe) |
| Metoda | Parsim JSON i çdo blloku `application/ld+json` në të 757 faqet, jo mostër; pastaj hapje live e çdo URL-je kandidate për të verifikuar entitetin |
| Statusi | 🔴 **JO** — asnjë nga të tri lidhjet nuk është e pranishme sistematikisht |

---

## Përgjigja e shkurtër

**Jo.** Në 736 nga 757 faqet e prodhimit, `sameAs` përmban një URL të vetme —
`https://rushiti.fr` — pra as PagesJaunes, as Google Maps, as ndonjë regjistër
tregtar. Google Maps shfaqet në **1 faqe të vetme** (`index.html`). PagesJaunes
dhe regjistrat tregtarë **nuk shfaqen askund** në sit, megjithëse të tri
profilet ekzistojnë dhe u verifikuan sot si të entitetit tonë.

---

## 1. Gjendja e gjetur në prodhim (të 757 faqet)

| Vlera e `sameAs` | Faqe | Shembull |
|---|---:|---|
| `["https://rushiti.fr"]` | **736** | `revetements-sol-roche-lez-beaupre.html` |
| Facebook + Instagram + Google Maps | 1 | `index.html` |
| rushiti.fr + Facebook + Instagram | 1 | `revetements-sol-besancon.html` |
| Facebook + Instagram | 1 | `a-propos.html` |
| **`sameAs` mungon plotësisht** | 4 | `zones-intervention.html`, `contact.html`, `simulateur-peinture.html`, `blog/calcul-rouleaux-papier-peint.html` |
| Pa asnjë nyje LocalBusiness | 14 | `mentions-legales.html`, `realisations.html`, `404.html`, 11 artikuj blogu |

Pika pozitive: **0 gabime sintaksore JSON** në të 756 blloqet — baza është e
shëndoshë, i mungon vetëm përmbajtja.

### Përkthimi i konstatimit sipas pyetjes

| Lidhja e kërkuar | Prezente? | Detaj |
|---|---|---|
| **PagesJaunes** | ❌ 0/757 | Profili ekziston, s'është deklaruar kurrë |
| **Google Maps** | ⚠️ 1/757 | Vetëm faqja e parë; e pranishme edhe si `hasMap` po aty |
| **Regjistra tregtarë** | ❌ 0/757 | As Annuaire des Entreprises, as INPI/RNE |

Shënim: SIRET-i deklarohet tashmë si e dhënë (`taxID` / `identifier` /
`vatID`), por një numër i shkruar nuk është lidhje — `sameAs` është e vetmja
fushë që i thotë motorit «kjo faqe dhe ai profil janë i njëjti entitet».

---

## 2. Profilet e verifikuara live (22/08/2026)

Asnjë URL nuk u shtua pa u hapur dhe pa u kryqëzuar me SIRET-in ose telefonin.

| Profili | URL | Prova e përputhjes |
|---|---|---|
| PagesJaunes | `https://www.pagesjaunes.fr/pros/61325501` | Faqja shfaq **SIRET 90521463100012**, SIREN 905 214 631, tel. 07 60 27 98 97, 18 rue Prof Haag, sit `rushiti-renovation.fr` |
| Google Maps (fisha GBP) | `https://www.google.com/maps?cid=10915820577691168567` | Fisha «RUSHITI Rénovation», 18 Rue du Professeur Haag, 4,7, +33 7 60 27 98 97 |
| Annuaire des Entreprises (INSEE/RNE, zyrtar) | `https://annuaire-entreprises.data.gouv.fr/entreprise/rushiti-905214631` | Dënominacioni RUSHITI, SIREN 905 214 631, SIRET 905 214 631 00012, TVA FR89905214631, NAF 43.34Z |
| INPI — Registre National des Entreprises | `https://data.inpi.fr/entreprises/905214631` | Imatrikulim RNE 16/11/2021, SARL, kapital 1 000 €, gjerantët Yll dhe Isuf Rushiti |

**Për regjistrat tregtarë** propozohen këto dy dhe jo `societe.com` /
`pappers.fr`: të parat janë burime publike zyrtare (INSEE, INPI), të dytat
ri-botues privatë — një lidhje drejt burimit zyrtar peshon më shumë si sinjal
besueshmërie dhe nuk rrezikon të vjetërohet.

### Të mbetura për konfirmim nga Isufi

* **LinkedIn**: `https://fr.linkedin.com/company/rushiti-rénovation` u gjet në
  kërkim, por URL-ja qarkullon e enkoduar (`rushiti-r%C3%A9novation`) — më
  duhet forma e saktë nga vetë faqja para se ta fus, që të mos deklarohet një
  URL që kthen 404.
* **Apple Plans, Bing Places, Houzz, Travaux.com**: sipas `corrections-audit-2026-08.md`
  ende `[À VÉRIFIER]` — nuk shtohen dot pa ekzistuar.

---

## 3. Blloku kanonik i rekomanduar

```json
"sameAs": [
  "https://rushiti.fr",
  "https://www.facebook.com/rushiti.renovation/",
  "https://www.instagram.com/rushiti.renovation/",
  "https://www.google.com/maps?cid=10915820577691168567",
  "https://www.pagesjaunes.fr/pros/61325501",
  "https://annuaire-entreprises.data.gouv.fr/entreprise/rushiti-905214631",
  "https://data.inpi.fr/entreprises/905214631"
]
```

Ky varg vendoset **një herë**, në nyjen `@id: https://rushiti-renovation.fr/#business`.
Faqet e tjera nuk duhet ta përsërisin përmbajtjen e biznesit — duhet ta
referojnë atë nyje me `{"@id": "https://rushiti-renovation.fr/#business"}`.
Pikërisht kështu një `sameAs` i vetëm mbulon të gjithë sitin dhe s'ka më rrezik
divergjence si sot (5 variante të ndryshme në 757 faqe).

---

## 4. Çfarë u bë tashmë

**Në këtë depo (kopja GitHub Pages, `noindex`)** — i zbatuar, i verifikuar:

* `index.html` dhe `syndic-copropriete-besancon.html`: `sameAs` i plotësuar me
  të 7 URL-të; JSON i rivalidhuar; formatimi i secilit skedar i ruajtur.

**Paketa e korrigjimit për prodhimin** — e shkruar dhe e provuar, **e pazbatuar**:

| Skedari | Roli |
|---|---|
| `korrigjime-prodhim/fix_sameas_localbusiness.py` | Plotëson `sameAs`; bashkim jo zëvendësim; nuk rishkruan JSON-in (formatimi ekzistues mbetet); **idempotent** |
| `korrigjime-prodhim/verifiko_sameas.py` | Vegël regresi: JSON i vlefshëm + 7 URL-të kanonike në çdo nyje me `@id`. Dalje 0 = konform. Për t'u ekzekutuar para çdo deploy-i |

Provat e kryera sot mbi checkout-in real të prodhimit (`abcdd34`):

* simulim: **740 faqe, 740 vargje** për t'u korrigjuar (739 me `sameAs` +
  futje te `zones-intervention.html`), 0 skedarë të tjerë të prekur;
* zbatuar mbi këtë depo → rileximi jep **0 ndryshime** (idempotencë e provuar);
* `verifiko_sameas.py` mbi këtë depo: **exit 0**.

Prodhimi **nuk u prek** — 740 faqe janë ndryshim që kalon nga validimi i Isufit.
Kur të jepet leja:

```bash
python3 fix_sameas_localbusiness.py /rruga/drejt/rushiti-renovation           # simulim
python3 fix_sameas_localbusiness.py /rruga/drejt/rushiti-renovation --apply   # zbatim
python3 verifiko_sameas.py         /rruga/drejt/rushiti-renovation            # exit 0 = konform
```

---

## 5. Mbetet punë me dorë (skripti nuk i prek)

Këto janë vendime redaktoriale, jo zëvendësime automatike:

1. **3 nyje LocalBusiness të ngulitura pa `@id`** — `contact.html`
   (`mainEntity`), `simulateur-peinture.html` (`provider`),
   `blog/calcul-rouleaux-papier-peint.html`. Zgjidhja e drejtë nuk është
   kopjimi i `sameAs`-it aty, por kthimi i tyre në referencë
   `{"@id": "https://rushiti-renovation.fr/#business"}`.
2. **14 faqe pa asnjë nyje biznesi** — 11 artikuj blogu plus `realisations.html`,
   `mentions-legales.html`, `404.html`. Për artikujt, `publisher` duhet të
   referojë nyjen `#business` në vend të një `Organization` të thatë.
3. **Fisha Google mban `rushiti.fr` si sit zyrtar**, ndërsa siti kanonik është
   `rushiti-renovation.fr` — kontradiktë me arbitrazhin e domenit (P0-A i
   `corrections-audit-2026-08.md`). Të rregullohet së bashku me atë vendim, jo
   veçmas.
4. **Fisha PagesJaunes thotë «Entreprise Rushiti SARL»**, ndërsa emri tregtar i
   përdorur kudo tjetër është «RUSHITI Rénovation». Pa qenë gabim ligjor,
   është mospërputhje NAP-i — të harmonizohet nga llogaria Solocal.

Jashtë perimetrit të kësaj pyetjeje, por i konstatuar rrugës: faqja e parë e
prodhimit mban `aggregateRating` + `review` të ushqyera nga avis-et Google,
ndërsa doktrina jonë (`guide-seo-local-pages-service-ville-2026-08.md`) e
ndalon këtë. Trajtohet veçmas.

---

## Ndikimi i pritshëm — dhe kufiri i tij

`sameAs` është sinjal konsolidimi entiteti: ndihmon Google-in dhe motorët IA të
lidhin sitin, fishën lokale dhe personin juridik në një entitet të vetëm. Kjo
punon në favor të paketës lokale dhe të citimeve nga motorët IA. Nuk është
faktor renditjeje i drejtpërdrejtë dhe **nuk premton asnjë pozicion** — është
higjienë e domosdoshme, jo levë.
