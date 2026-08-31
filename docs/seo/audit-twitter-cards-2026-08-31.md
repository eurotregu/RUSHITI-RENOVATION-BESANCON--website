# Audit et mise à niveau des Twitter Cards — 31/08/2026

| | |
|---|---|
| Déclencheur | Demande d'Isuf : « auditojeni dhe përmirësimi i Twitter Cards » |
| Périmètre | **Dépôt de production** `eurotregu/rushiti-renovation` (757 pages, commit `3317674`) **+ cette copie GitHub Pages** (3 pages) |
| Méthode | Lecture de toutes les balises `<meta>` des 757 pages — pas un échantillon — croisée avec le `<title>`, le `canonical`, et les **dimensions réelles** de chaque fichier image lu en binaire. Contrôle live d'une page servie (Firecrawl) pour confirmer que le déployé correspond au dépôt. |
| Livrables | ce rapport · `korrigjime-prodhim/fix_twitter_cards.py` (correctif idempotent) · `korrigjime-prodhim/verifiko_twitter_cards.py` (régression) · les 2 pages de cette copie corrigées |
| **Statut** | **Open Graph solide, Twitter Cards quasi absentes — correctif prêt, testé, non déployé** |

---

## Réponse courte

Le partage social du site repose entièrement sur Open Graph, et cette partie-là
est bien faite : **756 pages sur 757** portent `og:title`, `og:description`,
`og:url` et `og:site_name`, et l'`og:url` correspond au `canonical` sur
**100 % des pages**. Facebook, LinkedIn et WhatsApp ont donc ce qu'il leur faut.

Les Twitter Cards, elles, sont à l'état de trace :

| Balise | Pages qui la portent |
|---|---:|
| `twitter:card` | **31 / 757** |
| `twitter:title` | **0 / 757** |
| `twitter:description` | **0 / 757** |
| `twitter:image` | **0 / 757** |
| `twitter:image:alt` | **0 / 757** |
| `twitter:site` / `twitter:creator` | 0 / 757 |

X lit `twitter:*` en priorité et retombe sur `og:*` pour le titre, la
description et l'image quand ces balises manquent — donc les 31 pages qui
déclarent `twitter:card` affichent bien une grande vignette. Mais **726 pages
ne déclarent aucun type de carte** : sur celles-là, rien ne garantit autre chose
qu'un lien nu. Et `og:image:alt` n'est **pas** lu par X : sans
`twitter:image:alt`, l'image de la carte n'a aucun texte alternatif, sur
l'intégralité du site.

Deux autres constats, plus lourds de conséquences que les balises elles-mêmes :
**18 pages déclarent de fausses dimensions d'image**, et **aucune image sociale
du site n'atteint le format attendu d'une carte**.

---

## 1. Ce qui est en place (à ne pas casser)

| Balise | Couverture |
|---|---|
| `og:title`, `og:description`, `og:url`, `og:site_name`, `og:type` | 756 / 757 (seule `404.html` n'en a pas — normal) |
| `og:locale` = `fr_FR` | 755 / 757 (manque sur `blog.html`) |
| `og:image` | 753 / 757 |
| `og:url` **identique au `canonical`** | **757 / 757 — aucun écart** |
| `og:type` = `article` sur les 11 articles | correct |

`og:title` diffère volontairement du `<title>` sur 580 pages, avec une
formulation plus complète pour le partage — « Pose de cloisons et aménagement à
Battant – RUSHITI » là où le `<title>` dit « Cloisons & aménagement Battant –
Devis | RUSHITI ». C'est du bon travail, pas un défaut : à conserver tel quel.

---

## 2. Constats

### P1-1 — 726 pages sans aucune déclaration de carte

`twitter:card` n'est présent que sur les 31 pages piliers Besançon
(`peinture-interieure-besancon`, `degat-des-eaux-besancon`, `plaquiste-besancon`…)
plus `merci.html`. **La page d'accueil n'en fait pas partie** — c'est pourtant
l'URL la plus partagée du site.

Sur ces 31 pages, seule `twitter:card` est déclarée : titre, description et
image proviennent du repli sur Open Graph. Ça fonctionne, mais ça rend la carte
dépendante d'un comportement de repli plutôt que d'une déclaration explicite, et
ça laisse `twitter:image:alt` vide partout.

### P1-2 — 18 pages déclarent de fausses dimensions d'image

Les 31 pages qui déclarent `og:image:width` / `og:image:height` sont 18 à
annoncer des dimensions qui ne correspondent pas au fichier. Le cas le plus net :

> `devis-assurance-degat-des-eaux-besancon.html` déclare **1104 × 828**
> (paysage) pour `peinture-porte.jpg`, qui fait en réalité **517 × 710**
> (portrait).
>
> `cloisons-besancon.html` déclare **900 × 1200** pour un fichier **828 × 1104**.
> `entreprise-renovation-besancon.html` déclare **1104 × 828** pour un fichier
> **413 × 224**.

Ces deux balises servent au robot à réserver la place de la vignette avant
d'avoir téléchargé l'image. Une déclaration fausse produit un cadrage faux, et
une orientation inversée est le pire cas.

Même défaut dans cette copie : la page syndic annonçait 1104 × 828 pour un
fichier 828 × 621. **Corrigé dans cette PR.**

### P1-3 — Aucune image du site n'a le format d'une carte

12 images distinctes servent d'`og:image` à 753 pages. Le format recommandé pour
une grande carte est **1200 × 630** (ratio 1,91:1). Aucune n'y arrive :

| Situation | Pages concernées | Exemples |
|---|---:|---|
| **Portrait** — recadré de force dans une carte horizontale | **483** | `peinture-porte.jpg` 517×710 (240 pages), `cloisons-placo.jpg` 828×1104 (117), `isolation-pare-vapeur.jpg` 828×1104 (76) |
| **Trop petite** — sous 600 × 315, vignette réduite | **229** | `peinture-finition.jpg` 413×224 (190 pages), `faux-plafond-led.jpg` 500×375 (38), `logo.png` 128×128 (1) |
| Paysage exploitable (828 × 621, 4:3) | 41 | `doublage-placo-1.jpg`, `isolation-combles-1.jpg`, `platrerie-peinture.jpg` |

C'est le vrai plafond du sujet : on peut poser les balises parfaitement, une
photo portrait de 517 × 710 donnera toujours une carte mal cadrée — sur X comme
sur LinkedIn ou WhatsApp. **Un jeu de visuels 1200 × 630 est le seul correctif
qui vaille**, et il ne s'automatise pas.

### P2-1 — 3 pages sans aucune image sociale

`blog.html`, `contact.html` et `mentions-legales.html` n'ont pas d'`og:image` :
partagées, elles n'affichent aucune vignette. `blog.html` n'a pas non plus
d'`og:locale`. Le choix du visuel revient à Isuf — le correctif ne l'invente pas.

### P2-2 — Les 11 articles n'ont pas les balises `article:*`

Les 11 pages en `og:type="article"` ne déclarent ni `article:published_time`, ni
`article:modified_time`, ni `article:author`, ni `article:section` — alors que
les dates existent déjà dans leur JSON-LD (`datePublished`, `dateModified`) et
l'auteur aussi (Isuf Rushiti). Données disponibles, simplement pas reportées.

### P2-3 — `twitter:site` : rien à déclarer, et c'est à assumer

`twitter:site` et `twitter:creator` attribuent la carte à un compte X. RUSHITI
n'a **aucun compte X** dans son `sameAs` (Facebook, Instagram, PagesJaunes,
Google Maps, Annuaire des Entreprises, INPI, rushiti.fr). Un identifiant inventé
attribuerait les cartes à quelqu'un d'autre : **les balises restent absentes**
tant qu'il n'y a pas de compte. Si Isuf en ouvre un, une ligne à ajouter.

---

## 3. Ce qui est livré

### `korrigjime-prodhim/fix_twitter_cards.py` — correctif idempotent

Ce qu'il fait, sans jamais rien inventer :

- ajoute `twitter:card = summary_large_image` là où `og:title` existe ;
- ajoute `twitter:title`, `twitter:description`, `twitter:image` **dérivés des
  `og:*` de la page elle-même** ;
- ajoute `twitter:image:alt` en reprenant l'`og:image:alt` de la page ; si elle
  n'en a pas, **l'alt que le site déclare déjà en ligne pour le même fichier
  image** sur une autre page. Quand un même texte sert à plusieurs images
  différentes, c'est un alt générique recopié : le script préfère l'alt propre à
  l'image. Sans source dans le site, la balise n'est pas ajoutée ;
- corrige `og:image:width` / `og:image:height` d'après les dimensions réelles du
  fichier.

Ce qu'il ne fait pas, volontairement : aucun `twitter:site`, aucun `og:image`
choisi à la place d'Isuf, aucune réécriture des `og:title` / `og:description`
existantes, aucune touche à `404.html`.

La carte des alt reconstituée depuis la production :

| Image | Alt repris |
|---|---|
| `peinture-porte.jpg` | Porte rénovée et repeinte, finition propre |
| `peinture-finition.jpg` | Pièce peinte, finition soignée, RUSHITI Rénovation |
| `cloisons-placo.jpg` | Cloison placo sur ossature métallique, isolation intégrée |
| `isolation-pare-vapeur.jpg` | Pare-vapeur posé et marouflé sous toiture |
| `papier-peint-motifs.jpg` | Pose de papier peint décoratif à motifs |
| `faux-plafond-led.jpg` | Faux plafond avec corniche lumineuse LED, finition moderne |
| `doublage-placo-1.jpg` | Doublage placo BA13 sur ossature, chantier RUSHITI Rénovation à Besançon |
| `isolation-combles-1.jpg` | Isolation de combles sous rampants avec pare-vapeur |
| `renovation-couloir.jpg` | Couloir rénové, pose de sol et reprise des murs |
| `platrerie-peinture.jpg` | Pièce rénovée, plâtrerie puis peinture intérieure |
| `renovation-plafond.jpg` | Plafond rénové après reprise et mise en peinture |
| `logo.png` | *aucun alt déclaré nulle part → à écrire par Isuf* |

### `korrigjime-prodhim/verifiko_twitter_cards.py` — outil de régression

Contrôle les 5 balises, `og:url` = `canonical`, l'existence du fichier image,
l'exactitude des dimensions déclarées, et signale en KUJDES les images portrait
ou sous 600 × 315.

### Preuve de test

Exécuté sur une **copie** du dépôt de production (jamais sur la production) :

| Étape | Résultat |
|---|---|
| État initial | **3 770 erreurs** (756 × 5 balises manquantes, 18 dimensions fausses, 3 sans image) |
| `fix_twitter_cards.py --apply` | 756 pages modifiées |
| Après correctif | **10 erreurs** — les 3 pages sans `og:image` et l'alt du logo, tous en attente d'Isuf |
| Deuxième passe | **0 page modifiée** — idempotence prouvée |
| Diff sur une page | une seule ligne touchée, 4 balises insérées après la dernière `og:`, rien d'autre modifié |

### Les 2 pages de cette copie

| | `index.html` | `syndic-copropriete-besancon.html` |
|---|---|---|
| Avant | **aucune balise og: ni twitter:** | og: complet + `twitter:card` seul, dimensions fausses |
| Après | bloc complet og: + twitter: (titre, description, image, alt, dimensions réelles) | dimensions corrigées (828 × 621), 4 balises twitter: ajoutées |

`exemples-formulaires-demande-rapide.html` reste sans balises : page de démo
interne en `noindex`, jamais partagée.

---

## 4. À arbitrer par Isuf

- [ ] **Visuels sociaux 1200 × 630** — le seul correctif qui change vraiment le
      rendu des cartes. Au minimum un visuel générique ; l'idéal, un par silo
      (peinture, placo, sols, isolation, dégât des eaux, copropriété). Sans eux,
      les cartes resteront mal cadrées quelles que soient les balises.
- [ ] **Compte X** : à ouvrir (et alors `twitter:site` à renseigner), ou sujet
      classé — auquel cas les cartes restent utiles pour les partages faits par
      des tiers, mais le gain reste modeste face à Facebook et LinkedIn.
- [ ] **`og:image` de `blog.html`, `contact.html`, `mentions-legales.html`** :
      quel visuel ?
- [ ] **Alt du logo** (`a-propos.html`).
- [ ] **Déploiement du correctif en production** : le dépôt de production n'est
      accessible qu'en lecture dans cette session. Pour l'appliquer, ouvrir
      l'accès en écriture, puis :

```bash
python3 fix_twitter_cards.py /chemin/vers/rushiti-renovation           # simulation
python3 fix_twitter_cards.py /chemin/vers/rushiti-renovation --apply   # écriture
python3 verifiko_twitter_cards.py /chemin/vers/rushiti-renovation      # 0 = conforme
```

---

## 5. Test

Après déploiement, contrôler le rendu réel des cartes sur une URL en ligne :

- X : <https://cards-dev.twitter.com/validator>
- Facebook / LinkedIn (mêmes balises og:) :
  <https://developers.facebook.com/tools/debug/> et
  <https://www.linkedin.com/post-inspector/>

Aucun gain de trafic n'est promis ici : une carte correcte améliore le rendu
d'un partage, elle ne crée pas le partage.
