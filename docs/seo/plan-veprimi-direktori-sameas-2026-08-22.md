# Plani i veprimit — direktoritë, `sameAs` dhe orari

| | |
|---|---|
| Data | 22/08/2026 |
| Burimi | Checklist-i i Isufit (3 pika) |
| Vazhdon | `verifikim-sameas-localbusiness-2026-08-22.md` |
| Statusi | Pika 2 dhe 3 të zbatuara në këtë depo; pika 1 kërkon veprim njerëzor (llogari) |

---

## Pika 1 · Regjistrimi në direktori të tjera lokale

Llogaritë nuk i hap dot unë — kërkojnë identitet, e-mail dhe shpesh verifikim
me telefon ose kod postal. Ajo që bëra: **verifikova cila fishë ekziston tashmë**,
që të mos krijohen dublikata, dhe përgatita materialin që plotësohet një herë e
kopjohet kudo.

### Statusi i verifikuar (kërkim live, 22/08/2026)

| Direktoria | Statusi | Veprimi |
|---|---|---|
| **mesTravaux.com** | ✅ **Fishë ekzistuese** — `mestravaux.com/entreprise/rushiti/`, SIRET 90521463100012 i konfirmuar | **Pretendo**, mos krijo (shih paralajmërimin më poshtë) |
| **Houzz.fr** | Nuk u gjet fishë RUSHITI; platforma dhe hyrja pro ekzistojnë (`pro.houzz.fr/pro`) | Krijo profil |
| **NoTravo** | ❌ Nuk u konfirmua dot: `notravo.fr` nuk u hap dhe nuk del në kërkim | Më jepni URL-në e saktë; nuk shpik një platformë që s'e verifikoj dot |
| **Artisans de France** | ❌ Emri nuk çon te një platformë e vetme; kandidati më i afërt është `toutpourvostravaux.fr` («L'annuaire des artisans de France») — **hipotezë, jo fakt** | Konfirmoni cilën keni parasysh |
| *Mappy* (gjetur rrugës) | ✅ Fishë ekzistuese, `fr.mappy.com/poi/622c1993a7aaea2dcb87e998`, 18 r Prof Haag | Pretendo dhe kontrollo NAP-in |
| *MapQuest* (gjetur rrugës) | ✅ Fishë ekzistuese | Kontrollo NAP-in |
| *meilleur-artisan.com* (gjetur rrugës) | ✅ Fishë ekzistuese | Kontrollo NAP-in |

### ⚠️ Para se të pretendoni mesTravaux

Fisha mban **5 avis, nga të cilat 3 negative** (mospërputhje izolimi fonik,
finitura, punë e lënë përgjysmë) dhe nuk shfaq as telefon as adresë të plotë.
Dy pasoja të ndryshme:

* si **citim NAP** vlen pak — nuk ka adresë të plotë për të përputhur;
* si **lidhje `sameAs`** ajo i thotë shprehimisht Google-it «kjo faqe është
  ne» — pra e forcon në rezultate një faqe ku tri nga pesë avis-et janë
  negative dhe ku shfaqen edhe konkurrentët bisontinë.

Rekomandimi im: **pretendojeni fishën** (që të përgjigjeni publikisht në avis-et
negative dhe të plotësoni NAP-in), por **mos e fusni në `sameAs`** derisa
përgjigjet të jenë aty. Vendimi është juaji — një fjalë dhe e shtoj.

### Kit-i i regjistrimit (i njëjti tekst kudo, karakter për karakter)

```
Emri              RUSHITI Rénovation
Adresa            18 rue du Professeur Haag, 25000 Besançon
Telefoni          07 60 27 98 97   (ndërkombëtar: +33 7 60 27 98 97)
E-mail            contact@rushiti-renovation.fr
Siti              https://rushiti-renovation.fr
SIRET             905 214 631 00012        SIREN 905 214 631
TVA               FR89905214631            NAF/APE 43.34Z
Forma juridike    SARL, kapital 1 000 €, krijuar më 04/11/2021
Orari             Hën–Pre 07:00–20:30 · Sht 08:00–20:30 · Die 09:00–17:30
Zona              Besançon, Grand Besançon dhe i gjithë Doubs (25)
Kategoritë        Entreprise de peinture · Plâtrerie-plaquiste ·
                  Revêtements de sols et murs · Isolation thermique et
                  acoustique · Ravalement de façade
```

Rregulli i vetëm: kopjohet **identike** kudo — «rue» me r të vogël, me «du»,
telefoni i shfaqur me hapësira. Çdo variant i vogël dobëson përputhjen që bën
Google mes fishave.

Përshkrimet e gata (750 / 300 shenja) i prodhon `rushiti-fiche-google-business`
— thoni fjalën dhe i nxjerr për secilën direktori.

Sapo një fishë e re të jetë online, URL-ja e saj shtohet në listën kanonike me
një komandë të vetme (skripti i pikës 2 është idempotent).

---

## Pika 2 · Lidhja e citimeve me `sameAs`

### E zbatuar

Blloku është vënë në `<head>` të `index.html` dhe të
`syndic-copropriete-besancon.html` në këtë depo, me të 7 URL-të e verifikuara.
Për prodhimin (740 faqe) skripti është gati dhe i provuar, pret validimin tuaj —
detajet në raportin e mëparshëm dhe në `korrigjime-prodhim/README.md`.

### Tri korrigjime ndaj bllokut që dërguat

Blloku juaj funksionon, por tri gjëra do të kishin bërë dëm; i ndreqa dhe ja
arsyet:

**1. `"@id": "https://rushiti-renovation.fr"` → `".../#business"`**
Siti përdor kudo `@id: https://rushiti-renovation.fr/#business`. Po ta ndryshojmë
vetëm në një faqe, Google sheh **dy entitete të ndryshme** me të njëjtin emër në
të njëjtin domen — e kundërta e asaj që kërkon konsolidimi. `#business` është
fragmenti që identifikon *biznesin*, ndërsa URL-ja e zhveshur identifikon *faqen*.

**2. `"image": ".../logo.png"` → `".../assets/logo.png"`**
`https://rushiti-renovation.fr/logo.png` nuk ekziston; logoja qëndron te
`/assets/logo.png`. Ashtu siç ishte, do të deklaronim një imazh 404.

**3. `sameAs` me 2 URL → 7 URL**
Blloku juaj mban vetëm PagesJaunes dhe Localo. Po të vihej ashtu, do të fshinte
Facebook, Instagram, Google Maps, Annuaire des Entreprises, INPI dhe rushiti.fr
— pra do të hiqte gjashtë lidhje të verifikuara për të shtuar një.

### 🔴 Localo: e vetmja gjë që nuk e vura

`https://rushiti-renovation-peintre.localo.site/` **nuk e fusa**, dhe kjo është e
qëllimshme: `corrections-audit-2026-08.md` e klasifikon atë si sit dublikatë për
t'u **fshirë ose ridrejtuar** (P0-A, rreshti 28). Ai sot renditet i dyti për
«Rushiti Besançon peintre» — pra po konkurron me sitin tuaj kryesor.
Ta deklarojmë në `sameAs` do të thotë t'i themi Google-it se një sit dublikatë,
që kemi vendosur ta heqim, është po ne — kjo forcon dublikatën në vend që ta
shuajë.

Radha e drejtë: **së pari** 301 nga Localo drejt `rushiti-renovation.fr`, dhe
atëherë lidhja s'duhet më — ridrejtimi e bën punën vetë, më mirë. Nëse doni ta
mbani Localo-n si sit aktiv, kjo është vendim tjetër (dhe e ndryshon P0-A-në):
thoni fjalën dhe e shtoj brenda një minute.

### Blloku i saktë

```json
{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness", "HousePainter", "HomeAndConstructionBusiness"],
  "@id": "https://rushiti-renovation.fr/#business",
  "name": "RUSHITI Rénovation",
  "url": "https://rushiti-renovation.fr/",
  "image": "https://rushiti-renovation.fr/assets/logo.png",
  "telephone": "+33760279897",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "18 rue du Professeur Haag",
    "addressLocality": "Besançon",
    "postalCode": "25000",
    "addressCountry": "FR"
  },
  "sameAs": [
    "https://rushiti.fr",
    "https://www.facebook.com/rushiti.renovation/",
    "https://www.instagram.com/rushiti.renovation/",
    "https://www.google.com/maps?cid=10915820577691168567",
    "https://www.pagesjaunes.fr/pros/61325501",
    "https://annuaire-entreprises.data.gouv.fr/entreprise/rushiti-905214631",
    "https://data.inpi.fr/entreprises/905214631"
  ]
}
```

Shtova njëkohësisht në `index.html` të kësaj depoje edhe **`streetAddress`**, që
mungonte — pika e kuqe e `guide-seo-local`-it («ajouter `streetAddress` au bloc
JSON-LD du site»).

---

## Pika 3 · Sinkronizimi i orarit

Orari zyrtar, i vetmi që duhet të qarkullojë:
**Hën–Pre 07:00–20:30 · Sht 08:00–20:30 · Die 09:00–17:30**

| Ku | Gjetja e 22/08 | Statusi |
|---|---|---|
| Prodhimi (JSON-LD) | 153/153 faqet që deklarojnë orar e kanë saktë | ✅ Konform |
| Prodhimi (tekst i dukshëm) | «Lun – Ven : 7h – 20h30 · Sam : 8h – 20h30 · Dim : 9h – 17h30» | ✅ Konform |
| **Kjo depo, `index.html`** | JSON-LD thoshte **07:30–18:00 / Sht 08:00–12:00**, pa të dielën; teksti i dukshëm «Lun - Ven : 7h30 - 18h · Sam : 8h - 12h» | 🔧 **I korrigjuar** (të dyja) |
| Google Maps | Mbyllet 20:30, e shtunë 08:00–20:30 | ✅ Përputhet |
| **PagesJaunes** | **Hën–Sht 08:00–18:30 · Die 09:00–17:00** | 🔴 **Nuk përputhet** |

### PagesJaunes — dallimi konkret

| Dita | Orari juaj | PagesJaunes |
|---|---|---|
| Hën–Pre | 07:00–20:30 | 08:00–18:30 |
| E shtunë | 08:00–20:30 | 08:00–18:30 |
| E diel | 09:00–17:30 | 09:00–17:00 |

Domethënë PagesJaunes ju mbyll **një orë më herët në mëngjes dhe dy orë më
herët në mbrëmje**. Një klient që kërkon një peinture urgjente pas orës 18:30
ju sheh «të mbyllur». Korrigjohet nga Solocal Manager (fisha shfaq lidhjen
«Pour mettre à jour mes informations»), s'e prek dot unë.

### Mbrojtje nga rikthimi

`verifiko_sameas.py` tani kontrollon edhe orarin: çdo nyje biznesi që deklaron
`openingHoursSpecification` duhet ta ketë saktësisht atë zyrtar, përndryshe
dalja është jo-zero. Ekzekutohet para çdo deploy-i, njësoj si verifikuesit e
tjerë të dosjes.

---

## Përmbledhje e veprimeve

| # | Veprimi | Kush |
|---|---|---|
| 1 | `sameAs` + `@id` + `streetAddress` + orari në këtë depo | ✅ i bërë |
| 2 | Kontroll orari në `verifiko_sameas.py` | ✅ i bërë |
| 3 | 740 faqet e prodhimit | Skripti gati — **pret fjalën tuaj** |
| 4 | Korrigjimi i orarit në PagesJaunes (Solocal Manager) | Isuf |
| 5 | Pretendimi i fishave ekzistuese: mesTravaux, Mappy, MapQuest, meilleur-artisan | Isuf |
| 6 | Krijimi i profilit Houzz.fr | Isuf |
| 7 | URL-ja e saktë e NoTravo dhe e «Artisans de France» | Isuf → pastaj unë |
| 8 | Vendimi Localo: 301 (rekomandimi im) apo `sameAs` | Isuf |

Këto janë punë konsolidimi entiteti: ndihmojnë Google-in dhe motorët IA të
kuptojnë se siti, fisha lokale dhe personi juridik janë i njëjti biznes. Ndihma
është reale, por nuk është faktor renditjeje i drejtpërdrejtë — asnjë pozicion
nuk premtohet.
