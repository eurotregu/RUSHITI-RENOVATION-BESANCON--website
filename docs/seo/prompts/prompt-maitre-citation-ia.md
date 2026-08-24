# Prompt maître — citation IA (entrer dans le corpus des moteurs de réponse)

> **Version 1.0 — 22/08/2026.** Prompt de référence pour faire produire par un
> outil IA externe (ChatGPT, Perplexity, Gemini, Copilot, consultant) un audit
> de citation IA de RUSHITI Rénovation conforme aux règles de la maison.
>
> **Le chemin recommandé reste le skill `rushiti-citation-ia`** (Claude Code) :
> il lit le socle de données, les fichiers d'annuaires déjà vérifiés du dépôt
> et l'état réel des pages tout seul, et il refuse de proposer une action qui
> fabriquerait une source. Ce prompt sert quand on passe par un autre outil —
> remplir les variables, coller le bloc, puis **contrôler la sortie avec la
> liste de la dernière section** avant d'agir.

## Pourquoi ce prompt est construit ainsi

Un plan de visibilité IA générique produit pour RUSHITI en août 2026 contenait
seize erreurs, dont plusieurs auraient coûté cher : un `aggregateRating`
auto-déclaré contraire aux consignes Google, une date de création fausse, un
rayon d'intervention de 50 km qui sort du Doubs, une promesse de devis sous
48 h jamais validée, un journal de Dijon pris pour la presse de Besançon, et
des objectifs chiffrés d'apparition dans les réponses IA. Le détail complet est
dans `.claude/skills/rushiti-citation-ia/references/pieges-plans-ia-generiques.md`.

Trois partis pris en découlent, et ils structurent tout le bloc ci-dessous.

**Premier parti pris : relever les sources, pas seulement l'absence.** Savoir
que ChatGPT ne cite pas RUSHITI ne dit rien de ce qu'il faut faire. Savoir
**quels domaines il cite à sa place** donne directement la liste des portes à
pousser. Le livrable central est donc le corpus, pas le score.

**Deuxième parti pris : distinguer trois surfaces de citation.** Être listé
comme source, être nommé sans lien, et voir ses faits repris sans être nommé
sont trois situations différentes qui appellent trois corrections différentes.
La troisième est la plus fréquente et la plus vite corrigée.

**Troisième parti pris : les données sont fournies, l'invention est interdite,
l'inconnu s'écrit `[À COMPLÉTER]`.** Et un moteur non interrogé s'écrit `NM`,
jamais `0` : confondre « pas vu » et « pas cité » fabrique une fausse chute au
relevé suivant.

## Variables à remplir avant usage

| Variable | Valeur à coller |
|---|---|
| `{{SITE}}` | `rushiti-renovation.fr` **ou** `rushiti.fr` — un seul site par audit |
| `{{MOTEURS}}` | les plateformes réellement interrogées, avec leur date de relevé |
| `{{RELEVES}}` | les réponses collées : moteur, date, requête, réponse intégrale **et liste des sources** |
| `{{PANEL}}` | les quatorze requêtes du panel `rushiti-part-de-voix-ia`, recopiées sans en changer un mot |
| `{{ETAT_SOURCES}}` | pour chaque source déjà connue : présence de RUSHITI, exactitude du NAP, date de vérification |
| `{{RELEVE_PRECEDENT}}` | le CSV du relevé précédent, ou « première mesure » |
| `{{ARBITRAGES}}` | ce qu'Isuf a validé : labels réellement détenus, adhésions, budget d'inscription, contacts presse existants |

---

## Le prompt (bloc à copier tel quel)

```text
[RÔLE]
Tu es consultant en visibilité des entités dans les moteurs de réponse,
spécialisé dans les artisans du bâtiment en France. Tu ne rédiges pas un plan
d'inspiration : tu produis un audit de citation exploitable lundi matin par un
gérant d'entreprise artisanale qui a deux heures par semaine à y consacrer.

[CE QUE TU AUDITES]
Le site {{SITE}}, pour l'entreprise RUSHITI Rénovation, à Besançon (Doubs).
Question directrice, la seule : quelles sources les moteurs de réponse citent-
ils sur les requêtes de rénovation à Besançon, et comment RUSHITI entre-t-il
dans ces sources ?

[CONTEXTE VÉRIFIÉ — utilise EXCLUSIVEMENT ces données, jamais tes souvenirs]
- Nom commercial : RUSHITI Rénovation. Dénomination sociale : Rushiti.
  N'écris JAMAIS « SARL RUSHITI Rénovation ».
- SARL au capital de 1 000 €, créée le 04/11/2021 (RCS Besançon 905 214 631).
  Code APE 43.34Z.
- SIRET : 90521463100012 en données structurées ; 905 214 631 00012 dans un
  formulaire ou un texte. TVA FR89905214631.
- Adresse, au caractère près : « 18 rue du Professeur Haag, 25000 Besançon » —
  « rue » en minuscules, avec « du ».
- Téléphone affiché 07 60 27 98 97 · technique +33760279897 ·
  contact@rushiti-renovation.fr.
- Co-gérants : Isuf et Yll Rushiti. Isuf exerce le métier depuis vingt ans et
  a créé l'entreprise en 2021 : ces deux faits se disent ensemble et
  distinctement, jamais fondus en « 20 ans d'existence ».
- Prestations : peinture intérieure et extérieure, papier peint et toile de
  verre, plâtrerie et placo, faux plafonds, isolation intérieure et combles,
  revêtements de sol, ragréage, remise en état après dégât des eaux,
  rénovation de pièces, aménagement de bureaux et commerces.
- Garantie décennale et RC pro (ERGO). Références de mise en œuvre : DTU 59.1,
  DTU 25.41, DTU 53.12, convention IRSI pour les sinistres.
- Différenciateur validé : diagnostic technique gratuit sur place avant devis.
  SANS délai annoncé.
- Zone VALIDÉE : Besançon et ses quartiers, Grand Besançon, communes du Doubs
  (25) dont Pontarlier et Montbéliard. Vesoul, Belfort, Dole, Dijon,
  Lons-le-Saunier sont HORS PÉRIMÈTRE : ne les écris nulle part.
- Presse locale réelle : L'Est Républicain (édition Besançon), macommune.info,
  France 3 Bourgogne-Franche-Comté. « Le Bien Public » est le quotidien de
  Dijon : ne le cite jamais comme presse bisontine.
- Moteurs interrogés et dates : {{MOTEURS}}
- Panel de requêtes, à reprendre au mot près : {{PANEL}}
- Relevés bruts à dépouiller : {{RELEVES}}
- État connu des sources : {{ETAT_SOURCES}}
- Relevé précédent : {{RELEVE_PRECEDENT}}
- Arbitrages d'Isuf applicables : {{ARBITRAGES}}

[INTERDICTIONS — une seule violation rend la sortie inutilisable]
1. N'invente aucune donnée : ni citation non présente dans {{RELEVES}}, ni
   URL, ni volume de recherche, ni autorité de domaine, ni nombre d'avis, ni
   prix, ni délai. Tout élément non fourni s'écrit « [À COMPLÉTER] ».
2. Ne compte JAMAIS un moteur non interrogé comme zéro citation : il s'écrit
   « NM » et la raison est donnée.
3. Ne promets aucune citation, aucun classement, aucun pourcentage
   d'apparition à une échéance. Les effets se qualifient fort / moyen /
   faible, avec leur motif.
4. Ne propose aucune action qui fabrique une source : faux avis, faux
   témoignage, communiqué déguisé, profil créé au nom d'un tiers, intervention
   sous pseudonyme dans un forum ou un groupe local.
5. Ne propose ni achat de liens, ni échange de liens, ni emplacement payant
   présenté comme une citation gagnée.
6. Ne propose pas de publier un classement d'entreprises concurrentes où
   RUSHITI figurerait en tête. Un comparatif de solutions techniques, oui ;
   d'entreprises, non.
7. Ne propose pas de créer une page Wikipédia : les critères d'admissibilité
   excluent cette entreprise, et la tentative coûte des semaines.
8. Ne produis aucun balisage Review ni aggregateRating auto-déclaré, et
   n'écris jamais « siret » comme propriété schema.org : la forme correcte est
   identifier / PropertyValue.
9. N'écris aucun label, aucune certification, aucune adhésion (RGE, Qualibat,
   CAPEB, FFB) qui ne figure pas dans {{ARBITRAGES}}.
10. N'annonce aucun délai (« devis sous 48 h », « intervention sous 24 h »).
11. Ne dis pas que débloquer Google-Extended influe sur les aperçus IA de
    Google : c'est faux, ils relèvent de l'index Googlebot.
12. Ne présente pas llms.txt comme un levier de citation : aucun moteur suivi
    n'en documente l'usage comme source.
13. N'utilise ni nom, ni adresse, ni photo de client.

[MÉTHODE — dans cet ordre]
1. Dépouille {{RELEVES}}. Pour chaque couple requête × moteur, classe la
   présence de RUSHITI en une seule valeur :
   S  = une URL de RUSHITI figure dans les sources citées ;
   M  = « RUSHITI Rénovation » est nommé dans le texte, sans lien vers le site ;
   F  = un fait ou une formulation propre au site est repris, sans que RUSHITI
        soit nommé ;
   Ø  = ni source, ni mention, ni reprise ;
   NM = moteur non interrogé.
   Le cas F est le plus important : il signifie que le contenu nourrit la
   réponse mais que l'entité ne s'y accroche pas.
2. Extrais TOUTES les URL citées, y compris celles qui ne concernent pas
   RUSHITI. C'est le corpus, et c'est l'objet de l'audit.
3. Classe chaque URL par famille : fiche d'établissement, annuaire généraliste,
   registre public, plateforme de mise en relation, institutionnel ou
   professionnel, presse locale, comparatif tiers, forum ou communauté, site
   concurrent, domaine RUSHITI.
4. Compte les occurrences par domaine et calcule, sur le mesuré uniquement :
   la concentration (combien de domaines couvrent la moitié des citations),
   la part de citation propre (citations vers un domaine RUSHITI ÷ citations
   mesurées), le taux de présence dans le corpus (sources où RUSHITI a une
   fiche exacte ÷ sources où il pourrait en avoir une).
5. Pour chaque domaine du corpus, rends un verdict d'entrée :
   ✅ présent et exact · ⚠️ présent mais faible · 🎯 absent et accessible ·
   🚪 absent, accès éditorial · ⛔ hors d'atteinte. Dis-le franchement quand
   c'est ⛔.
6. Priorise par : fréquence de citation × facilité d'entrée (3 = moins d'une
   heure ; 2 = dossier ou échange ; 1 = relation longue ; 0 = fermé). Donne le
   produit brut, sans pondération inventée.
7. Traite à part le bloc marque : liste toute erreur que les moteurs répètent
   sur l'entreprise (domaine éteint, horaire faux, service non proposé, forme
   juridique inexacte) et dis à quelle source la corriger.

[SORTIE ATTENDUE — cinq blocs, dans cet ordre]
1. EN-TÊTE DE MESURE : site, date, moteurs mesurés et méthode, moteurs non
   mesurés et raison, conditions de session.
2. VERDICT EN TROIS LIGNES : état du corpus, source la plus citée où RUSHITI
   est absent, action qui rapporte le plus vite.
3. GRILLE DES CITATIONS : tableau requête × moteur avec S / M / F / Ø / NM, et
   les URL citées en regard. Grille brute, sans interprétation.
4. CORPUS ET PLAN D'ENTRÉE : tableau domaine / famille / occurrences /
   présence RUSHITI / verdict / porte d'entrée exacte (URL d'inscription, nom
   du service, pièce à fournir) / priorité calculée. Trié par priorité.
5. PLAN DE MESURE : ce qu'il faut re-relever, quand (six à huit semaines), et
   le CSV daté à conserver.

[STYLE]
Français, vouvoiement, phrases de 15 à 20 mots. Chaque constat porte sa preuve
— URL et date — et chaque action dit où cliquer. Une action sans « où » restera
non faite. Test final de chaque ligne : Isuf pourrait-il l'exécuter lundi matin
sans te reposer une question ?
```

---

## Pack de relevé — les prompts à poser dans chaque plateforme

À remettre tel quel à Isuf. Règles communes, valables pour les cinq
plateformes :

- **Une session neuve par requête**, en navigation privée, hors compte connecté
  quand c'est possible — un compte qui connaît déjà RUSHITI personnalise la
  réponse et fausse la mesure ;
- **coller la formulation exacte**, sans rien ajouter ni reformuler ;
- **copier la réponse entière et la liste des sources** ;
- **ne pas relancer** une requête dont la réponse déplaît : le relevé
  enregistre ce qui s'est passé ;
- noter moteur, date, heure et conditions.

### Les requêtes

**Panel non-marque** : les quatorze requêtes de `rushiti-part-de-voix-ia`,
recopiées au mot près. C'est ce qui rend les deux mesures superposables.

**Bloc marque** — tenu séparé, jamais mélangé au dénominateur du panel :

```text
Rushiti Rénovation Besançon, qu'est-ce que c'est ?
```
```text
avis sur Rushiti Rénovation à Besançon
```
```text
qui sont les gérants de Rushiti Rénovation ?
```

### La relance qui fait apparaître les sources

À poser systématiquement après la réponse, sur ChatGPT, Gemini et Claude, dès
qu'aucune source n'est affichée :

```text
Liste uniquement les sources web que tu as réellement consultées pour cette
réponse, en URL complètes, une par ligne, sans commentaire. Si tu as répondu
sans consulter de source, dis-le explicitement.
```

La réponse à cette relance est une donnée en soi : elle distingue une réponse
ancrée sur des documents d'une réponse produite sans source, et les deux
n'appellent pas le même travail.

### Ordre de passage recommandé

Perplexity d'abord : c'est la plateforme qui affiche la liste de sources la
plus complète, donc le meilleur relevé du corpus, et le plus rapide à
collecter. Puis les aperçus IA de Google et AI Mode, puis Copilot, puis
ChatGPT et Gemini.

### Prompt de dépouillement (transformer un relevé collé en lignes de CSV)

```text
Voici une réponse de moteur IA, sa requête, son moteur et sa date.
Transforme-la en lignes CSV au format exact ci-dessous, séparateur point-
virgule, une ligne par source citée. Si aucune source n'est citée, produis une
seule ligne avec les champs de source vides.

date_releve;moteur;bloc;requete;surface;rang_source;url_citee;domaine_cite;famille_source;conditions_session;observation

Règles :
- surface = S (une URL de rushiti-renovation.fr ou rushiti.fr est citée),
  M (RUSHITI Rénovation nommé sans lien), F (un fait du site repris sans que
  RUSHITI soit nommé), Ø (rien) — la même valeur est répétée sur toutes les
  lignes du même couple requête × moteur ;
- bloc = « panel » ou « marque » ;
- famille_source = fiche d'établissement | annuaire | registre public |
  plateforme de devis | institutionnel | presse locale | comparatif tiers |
  forum | concurrent | domaine RUSHITI ;
- n'invente aucune URL : ne reporte que celles réellement présentes ;
- observation : toute erreur factuelle sur l'entreprise repérée dans la
  réponse, en une proposition.
Ne produis rien d'autre que les lignes CSV.
```

Le fichier de destination et le dictionnaire des colonnes :
`docs/seo/citations-ia/releve-citations-ia-MODELE.csv`.

---

## Après la sortie : ce qu'il faut vérifier à la main

1. **Chaque URL citée dans le rapport s'ouvre.** Une URL inventée est l'échec
   le plus fréquent de ce type de sortie, et le plus discret.
2. **Chaque chiffre remonte à une source datée.** Sans source, il saute.
3. **Chercher les mots interdits** : « Vesoul », « Dijon », « Belfort »,
   « Dole », « 50 km », « sous 48 h », « sous 24 h », « meilleur », « n°1 »,
   « Le Bien Public », « garantit », « garantie de citation ».
4. **Chercher `aggregateRating`, `Review`, `"siret":`** — aucun ne doit
   apparaître.
5. **Vérifier qu'aucun moteur non interrogé n'est compté 0** : il doit être
   `NM`, avec sa raison.
6. **Vérifier qu'aucun label non détenu** (RGE, Qualibat, adhésion CAPEB ou
   FFB) n'est écrit comme acquis.
7. **Vérifier qu'aucune action ne fabrique une source** : relire la colonne
   « porte d'entrée » ligne à ligne.
8. **Passer le rapport au mode 3 du skill `rushiti-citation-ia`** avant
   d'engager la moindre inscription ou prise de contact.
