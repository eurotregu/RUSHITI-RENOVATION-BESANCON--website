# Google Ads — Fjalët kyçe negative / Mots-clés négatifs

Lista përfundimtare e fjalëve kyçe negative për llogarinë Google Ads të RUSHITI Rénovation
(rushiti-renovation.fr), e ndërtuar sipas checklist-ës së Igor Ivitskiy ("Doctor Ads") dhe
e përshtatur me shërbimet reale të sitit.

## Si përdoret

1. Hapni skedarin `liste-mots-cles-negatifs.txt` dhe kopjojeni të gjithë përmbajtjen.
2. Në Google Ads shkoni te **Admin → Account settings → Negative keywords**
   (fjalë negative në nivel llogarie — vlejnë për të gjitha fushatat, edhe Performance Max).
3. Klikoni **+**, ngjitni listën, ruani. (Kufiri i Google: 1 000 fjalë; kjo listë ka ~215.)

Formati: fjalët pa thonjëza = broad match negative, frazat me thonjëza = phrase match
negative. Google **nuk** mbulon variantet e afërta (shumës, thekse) te fjalët negative —
prandaj lista përmban të dyja format ku duhet (école/ecole, tuto/tutos…).

## Çfarë NUK duhet shtuar kurrë si negative

Këto duken joshëse por bllokojnë klientë realë:

- `gratuit` — do të bllokonte **"devis gratuit"**, kërkimi nr. 1 i klientëve
- `prix`, `tarif`, `devis`, `pas cher` — kërkime me qëllim blerjeje
- `aide`, `prime`, `maprimerénov`, `anah` — klientë që duan punime me subvencione
- `urgence`, `urgent` — kritike për dégât des eaux
- `carrelage`, `faience`, `carreleur` — **shërbim që RUSHITI e ofron** (carrelage mural et sol)
- `rushiti` — emri juaj, kurrë negative

## Municion rezervë — konkurrentët e Besançon (MOS i shtoni tani)

Kërkuesit e këtyre emrave janë klientë të nxehtë që po zgjedhin artizan — prandaj nuk
bllokohen paraprakisht. Shtojini VETËM nëse pas 3–4 javësh raporti *Insights → Search terms*
tregon klikime të rregullta mbi ta pa asnjë telefonatë a formular:

```
"centaure isolation"
gmh
hintzy
"mb peinture"
"nuances et décoration"
"nuances et decoration"
"bisontine de peinture"
"bourgogne peinture"
"pateu robert"
laborier
"reno pro"
doras
"comptoir de l'ours"
"ideal parquet"
"espace renovation"
```

Qytete kufitare (`dijon`, `belfort`, `mulhouse`) nuk janë në listë — shtojini vetëm nëse
vendosni që nuk pranoni chantier atje.

## Mirëmbajtja

Çdo 2 javë pas nisjes së fushatave: **Insights → Search terms** → shtoni çdo kërkim të ri
parazit në listën e llogarisë dhe përditësojeni edhe skedarin këtu, që repo të mbetet
burimi i vërtetës.
