# Que reprendre d'uesas.fr pour rushiti-renovation.fr — plan détaillé

**02/09/2026 · brouillon d'analyse, lecture seule.** Complète
`docs/seo/audit-uesas-prescripteur-2026-09-02.md`. Aucune page de production modifiée
par ce document.

**Méthode.** Le site d'Union d'Experts a été lu en direct (Firecrawl sur le code source :
accueil, `/nos-metiers/gestion-des-sinistres/`, `/annuaire/`, `/tiers-de-confiance/`,
`/robots.txt`). L'état de rushiti-renovation.fr n'est pas estimé : il est **compté dans le
dépôt de production** au commit `2a451c6` (757 pages HTML). Chaque chiffre ci-dessous est
reproductible par un `grep`.

---

## 0. Deux constats trouvés en vérifiant — ils passent avant tout le reste

### 0.1 « Qualification RGE » est affiché sur 93 pages

Relevé : `grep -rl "Qualification RGE" --include=*.html` → **93 fichiers**, tous du silo
isolation (`isolation-*.html`, `isolation-interieure-*.html`). Le libellé apparaît dans le
bandeau de réassurance du hero, au même rang que des faits vérifiables :

> **20 ans** d'expérience · **Diagnostic** gratuit sur site · **Travaux selon DTU 25.41** ·
> **Artisan** local · **Qualification RGE**

Ce n'est pas une nuance de rédaction. RGE (Reconnu Garant de l'Environnement) est un signe
de qualité encadré, et c'est lui qui conditionne l'accès du client aux aides publiques sur
des travaux d'isolation. L'afficher alors qu'il n'est pas détenu expose l'entreprise, et
surtout : le client qui choisit RUSHITI pour cette raison découvrira le problème au moment
de sa demande d'aide.

**Deux issues, une seule à choisir :**

- **La qualification est détenue** → ajouter à côté le numéro de qualification, l'organisme
  et la date de validité. Un badge nu n'est pas une preuve ; un numéro en est une.
- **Elle ne l'est pas** → retirer la mention des 93 pages. Le remplacement naturel existe
  déjà dans le bandeau des autres silos : « Décennale & RC pro » ou « Devis détaillé,
  sans engagement ».

Correction mécanique et idempotente, un seul bloc HTML répété. **Décision d'Isuf requise
avant toute intervention.**

### 0.2 Les pages isolation citent le DTU des plaques de plâtre

Comptage des DTU cités sur l'ensemble du site :

| DTU cité | Occurrences | Objet réel |
|---|---|---|
| 25.41 | 816 | Ouvrages en plaques de plâtre |
| 59.1 | 588 | Travaux de peinture |
| 58.1 | 115 | Plafonds suspendus (38 pages `faux-plafonds-*`) |
| 25.42 | 18 | Doublage isolant (pages `doublage-murs-*` uniquement) |
| 59.4 | 2 | Papier peint |

Les **278 occurrences de DTU 25.41 sur les pages isolation** posent question : la page
annonce « doublage isolant des murs par l'intérieur » et « isolation des combles et des
rampants », travaux qui relèvent du **25.42** (doublage isolant) et du **45.10** (combles).
Le 25.41 ne couvre que la mise en œuvre des plaques.

Relevé complémentaire : **DTU 45.10, 53.12, 51.11 et 42.1 ne sont cités nulle part**, alors
que le site vend combles, sols souples collés, parquet flottant et ravalement.

À traiter comme une question technique, pas comme une faute de frappe : c'est à Isuf de
dire quel DTU s'applique à chaque prestation telle qu'elle est réellement exécutée. À
défaut de certitude, la règle du dépôt s'applique — « selon les règles de l'art ».

Le DTU 58.1 (plafonds suspendus) ne figure pas dans la table de vérité des instructions :
à valider avant de le conserver sur les 38 pages faux-plafonds.

---

## 1. Ce qu'est uesas.fr, et ce que ça change

**Union d'Experts** — groupe national d'expertise d'assurance, de gestion de sinistres et
de prévention. 79 cabinets, dont **École-Valentin (25480), Pontarlier (25300) et
Montbéliard (25200)**. Ce n'est pas un concurrent : c'est un **prescripteur**.

Conséquence directe sur la lecture de leur site : il n'est pas conçu pour capter la demande
d'un particulier sinistré. Il est conçu pour rassurer un assureur qui délègue. On ne
transpose donc pas leur *forme*, on transpose leur *langue* et leurs *engagements*.

### Leur site, mesuré

| Constat | Détail |
|---|---|
| 4 balises H1 sur l'accueil | Blocs Elementor dupliqués par point de rupture |
| ~150 mots de texte visible sur l'accueil | Le message est porté par des images cliquables |
| Aucune meta description servie | Vérifié sur 4 pages |
| Extrait social pollué | L'URL brute `…/Video_AMRAE-2026-VF.mp4` apparaît dans la description |
| Aucun bloc JSON-LD détecté | 79 établissements, zéro entité structurée |
| Annuaire sous consentement | « Pour afficher l'annuaire, acceptez les cookies […] puis actualisez » |
| Actualités = communication corporate | Salons, interviews ; aucune question d'assuré |

En face, rushiti-renovation.fr : **756 pages sur 757 portent du JSON-LD**, **746 portent un
bloc FAQPage**, meta descriptions et canoniques présentes, barre d'appel mobile sur
745 pages, images en WebP avec `loading="lazy"`, plus lourde image du site à 168 Ko.

**Le rapport de force est inversé par rapport à ce qu'on attend d'un groupe de 700
personnes : sur la structure technique, c'est nous qui sommes devant.** Rien de leur
modèle de page n'est à copier.

---

## 2. Ce qui est transférable, par ordre de valeur

### 2.1 Leur lexique — fait le 02/09/2026

Intégré dans `/expert-assurance-sinistre-besancon` (PR #34 du dépôt de production,
fusionnée) : missionnement, gré à gré, réparation en nature, règlement direct du
prestataire, dossier contradictoire, dossier de faible enjeu, expertise à distance.

Reste à décider : les plateformes de missionnement (Sinapps, Darva). Rien n'est écrit tant
que le raccordement n'est pas confirmé — **[À COMPLÉTER]**.

### 2.2 La page « À propos » — 405 mots aujourd'hui

Union d'Experts consacre deux pages à son identité (« Présentation », « Équipe
dirigeante »). C'est le seul endroit où leur site est plus riche que le nôtre, et ce n'est
pas un hasard : c'est la page qu'un donneur d'ordre lit avant de confier un dossier, et
celle qu'un moteur IA cite quand on lui demande « qui fait ça à Besançon ».

Notre `/a-propos` fait **405 mots** — moins que la moindre page de commune du site.

À écrire, sans rien inventer :

1. **Le parcours d'Isuf et de Yll** — où le métier a été appris, sur quels types de bâti,
   depuis quand à Besançon. Ce sont des faits, ils ne demandent qu'à être écrits.
2. **Un paragraphe canonique de 60 à 80 mots**, repris mot pour mot dans le JSON-LD
   `description` et dans la fiche Google Business. C'est le bloc que les moteurs de réponse
   recopient.
3. **La méthode**, dans la trame maison : ce qu'on refuse de faire (peindre sur un support
   qui n'est pas sain), pourquoi le diagnostic précède le devis.
4. **Les faits d'entité** rassemblés au même endroit : SIRET 905 214 631 00012,
   RCS Besançon, TVA FR89905214631, décennale ERGO (n° **[À COMPLÉTER]**), co-gérants.
5. **Une photo des deux gérants**, pas seulement des chantiers.

Ce que nous ne copions pas : leur page « Équipe dirigeante » façon organigramme. Deux
artisans, ce n'est pas un conseil d'administration.

### 2.3 Le formulaire absent de la page d'accueil

Relevé : `index.html` ne contient **aucune balise `<form>`**, aucune ancre
`#demande-rapide`. Seules **33 pages sur 746** portent le formulaire.

L'accueil est pourtant la page la plus exposée du site : le registre de mots-clés y note
1 343 impressions en position 3,5 pour « entreprise de peinture à Besançon », **avec zéro
clic**, décrit comme le plus gros gisement du site. Le visiteur qui arrive n'a qu'un
téléphone et un lien vers `/contact`.

Le bloc existe déjà, testé, avec son garde-fou RGPD et son champ « Société / cabinet ».
Le poser sur l'accueil est un copier-coller, pas un développement.

### 2.4 La FAQ absente de la page d'accueil

Relevé : `grep -c "faq-item" index.html` → **0**, alors que 746 pages du site en portent
une. L'accueil est la seule page importante sans FAQ, donc sans bloc `FAQPage`.

Cinq à six questions, dans la langue du client : combien de temps sans pouvoir utiliser la
pièce, faut-il quitter le logement, qui protège les meubles, que se passe-t-il si on
découvre un support abîmé sous le revêtement, comment se passe le diagnostic gratuit.
Parité stricte question visible / JSON-LD, comme partout ailleurs sur le site.

Aucune réponse ne comporte de prix, de délai ferme ni de taux de TVA.

### 2.5 Le bloc « 5 engagements » de leur page « Tiers de confiance »

Format repérable : cinq promesses courtes, chacune avec un sous-titre d'une ligne, sans un
seul chiffre. C'est efficace parce que c'est vérifiable.

Transposition possible sur les pages B2B (syndics, experts, commerces) :

- **Un seul interlocuteur** — de la préparation à la finition, la même équipe.
- **Le diagnostic avant le devis** — gratuit, sur site.
- **Un devis au format attendu** — postes en unités d'œuvre, métrés pièce par pièce.
- **Un chantier annoncé** — phasage convenu, protections, découvertes signalées le jour même.
- **Une remise en état à l'identique** — supports traités avant réfection.

### 2.6 Les études de cas — `/realisations` fait 259 mots

Ici, Union d'Experts n'a rien à nous apprendre : ils n'ont aucun cas concret publié. C'est
précisément le terrain où un artisan les dépasse sans effort.

Structure d'une étude de cas, en quatre temps :

1. **Le problème vécu** — ce que le client constatait (auréole qui revient, cloison qui
   sonne creux, sol qui bouge).
2. **Ce que le diagnostic a révélé** — la cause, pas le symptôme.
3. **L'intervention** — préparation, traitement de la cause, finition.
4. **Le résultat** — photos avant / après.

Garde-fous : accord écrit du client avant toute photo ou tout témoignage identifiable,
aucune adresse précise, **aucun prix, aucune durée** qui n'aurait pas été réellement
constatée. L'agent `rushiti-etudes-de-cas` couvre déjà ce format.

### 2.7 Chantier propre et déchets — la version artisan de leur « RSE »

Leur rapport RSE et leur médaille EcoVadis n'ont pas d'équivalent utile pour une entreprise
de deux gérants. La version qui parle au client est concrète : protection des sols et du
mobilier, aspiration à la source lors des ponçages, tri et évacuation des déchets de
chantier, peintures à faible teneur en COV quand le chantier s'y prête.

À n'écrire **que si c'est la pratique réelle**, et sans jamais nommer un label
(Écolabel, NF Environnement) qui ne serait pas détenu.

---

## 3. Verdict sur le rapport que vous avez reçu

| Recommandation reçue | Verdict vérifié |
|---|---|
| Ajouter le balisage Schema / LocalBusiness | **Déjà fait** — 756 pages sur 757 |
| Créer des pages par quartier et commune | **Déjà fait** — c'est la majeure partie des 757 pages |
| Ajouter un formulaire de contact sur l'accueil | **Juste** — `index.html` n'en a aucun |
| Ajouter une FAQ sur l'accueil | **Juste** — 0 `faq-item` sur l'accueil |
| Développer « Qui sommes-nous » | **Juste** — 405 mots |
| Études de cas détaillées | **Juste** — `/realisations` : 259 mots |
| Ajouter un en-tête collant avec le téléphone | **Déjà fait** — barre d'appel sur 745 pages |
| Compresser les images, WebP, lazy loading | **Déjà fait** — 17 WebP, `loading="lazy"`, plus gros fichier 168 Ko |
| Démarrer un blog | **Déjà fait** — 11 articles, 880 à 1 740 mots |
| Enrichir le pied de page | **Partiellement** — services, pros et contact déjà présents |
| Slider avant / après | **À faire**, sous réserve d'accord RGPD sur les photos |
| Garanties détaillées (parfait achèvement, biennale) | **À faire** — aucune des deux n'est mentionnée sur le site |
| Lister les certifications et « certifications DTU » | **À écarter** — un DTU est une norme de mise en œuvre, pas une certification ; et aucune certification ne s'affiche sans être détenue |
| Adhésion CAPEB | **À écarter sauf adhésion réelle** — aucune trace sur le site |
| Lister fournisseurs et partenaires (Tollens, Placo, Isover…) | **À écarter en l'état** — citer une marque comme partenaire suppose son accord |
| Prix approximatif dans les études de cas | **À écarter** — aucun prix ne s'écrit sans votre décision |
| FAQ « TVA réduite à 10 % » | **À reformuler** — la TVA ne s'affirme jamais, elle reste sous condition d'éligibilité |
| Témoignage client par quartier | **Sous condition** — accord écrit préalable, RGPD |

Le rapport reçu décrit un site que RUSHITI a déjà dépassé sur la moitié des points, et
propose sur l'autre moitié des mentions qui ne peuvent pas être écrites sans preuve. Les
six lignes marquées « juste » restent, elles, entièrement valables.

---

## 4. Ordre d'exécution proposé

| Rang | Action | Portée | Décision requise |
|---|---|---|---|
| 0 | Trancher « Qualification RGE » sur 93 pages | 93 fichiers | **Isuf** |
| 0 bis | Trancher les DTU du silo isolation | 93 fichiers | **Isuf** |
| 1 | Formulaire sur la page d'accueil | 1 fichier | technique |
| 2 | FAQ + FAQPage sur la page d'accueil | 1 fichier | relecture |
| 3 | Réécriture de `/a-propos` | 1 fichier | faits à fournir |
| 4 | Deux études de cas | 2 blocs | accord RGPD |
| 5 | Bloc « engagements » sur les pages B2B | 4 fichiers | relecture |
| 6 | Garanties détaillées | pages services | relecture |

Rien n'est déployé sans validation. Sur ce dépôt, fusionner revient à publier.
