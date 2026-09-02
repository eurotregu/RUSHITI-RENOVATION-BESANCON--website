# Audit uesas.fr (Union d'Experts) — 02/09/2026

**Statut : brouillon d'analyse, lecture seule.** Aucune modification de production, aucun
contact engagé. Relevé fait le 02/09/2026 par lecture directe du site (Firecrawl sur le
code source live), pages : accueil, `/nos-metiers/gestion-des-sinistres/`, `/annuaire/`,
`/tiers-de-confiance/`, `/robots.txt`.

---

## 1. Ce qu'est réellement ce site

`www.uesas.fr` = **Union d'Experts**, groupe national d'**expertise d'assurance, de gestion
de sinistres et de prévention des risques**. Siège : 14 rue du Pont de l'Arche, 37550
Saint-Avertin · 02 47 74 16 20 · contact@uesas.fr. Texte de présentation relevé sur
l'accueil : « *Au plus près des assurés sinistrés depuis bientôt 30 ans […] 700
collaborateurs organisés en pôles de compétences, interviennent auprès des particuliers et
des entreprises victimes de sinistres* ». Annuaire : **79 cabinets** déclarés.

**Ce n'est donc pas un concurrent de RUSHITI Rénovation.** C'est un **prescripteur** :
un cabinet d'expertise qui instruit les dossiers sinistres que nos chantiers de remise en
état viennent clore. Il relève de la famille « experts d'assurance » de la grille
`rushiti-prospection-b2b`, et il croise directement le silo dégât des eaux
(`/degat-des-eaux-besancon`, `/devis-assurance-degat-des-eaux-besancon`,
`/expert-assurance-sinistre-besancon`).

### Implantations dans notre zone (relevé annuaire du 02/09/2026)

| Cabinet | Adresse | Téléphone | E-mail |
|---|---|---|---|
| UNION D'EXPERTS BESANÇON | 10D rue de Franche-Comté, 25480 École-Valentin | 03 81 52 23 44 | jacquemet.besancon@uesas.fr |
| UNION D'EXPERTS PONTARLIER | 27 rue Jeanne d'Arc, 25300 Pontarlier | 03 81 46 52 80 | jacquemet.pontarlier@uesas.fr |
| UNION D'EXPERTS MONTBÉLIARD | 9 av. du Maréchal Joffre, 25200 Montbéliard | 03 81 90 49 16 | jacquemet.montbeliard@uesas.fr |
| UNION D'EXPERTS VESOUL (70) | 8 rue Victor Dolle – Le Galaxy 2, 70000 Vesoul | 03 84 74 32 55 | jacquemet.vesoul@uesas.fr |
| UNION D'EXPERTS LONS-LE-SAUNIER (39) | 330 bd Jules Ferry, 39001 Lons-le-Saunier | 03 84 43 49 94 | jacquemet.lonslesaunier@uesas.fr |

Les cinq partagent le préfixe e-mail `jacquemet.` : ils forment vraisemblablement un même
pôle Franche-Comté au sein du groupe. **Trois d'entre eux sont dans le Doubs (25)**, et
celui de Besançon est domicilié à **École-Valentin**, commune déjà couverte par une page
locale du site.

> Nom du responsable du pôle, périmètre exact des cabinets, existence d'un référencement
> prestataire ouvert : **[À COMPLÉTER]** — non publiés sur le site.

---

## 2. Audit du site lui-même

### Ce qui est solide

- **Architecture claire** : Le Groupe / Talent / Nos métiers (Expertise, Prévention,
  Gestion des sinistres) / Spécialités (7 pôles) / Annuaire / Partenariats / RSE.
- **Annuaire des 79 cabinets** avec adresse, téléphone et e-mail nominatif par site : le
  meilleur actif du domaine, et de loin le plus utile pour nous.
- **Langue métier maîtrisée** : la page « Gestion des sinistres » parle assureur, pas
  grand public — TPA, front/back office, gré à gré, **réparation en nature directe**,
  dossiers contradictoires, dossiers de faible enjeu, expertise à distance, gestion des
  prestataires, gestion des recours.
- **Preuves institutionnelles** : logos partenaires (CNRS, CNPP, CFEC, Darva, FSE),
  rapport RSE, médaille EcoVadis, école interne (UE Académie).
- `robots.txt` propre, sitemap déclaré (`sitemap_index.xml`), pages en `index, follow`.

### Ce qui est faible (à ne surtout pas copier)

| Constat relevé | Conséquence |
|---|---|
| **4 balises H1 sur l'accueil** (« Nos Métiers », « Nos Spécialités », « Nos formations », « Notre RSE ») — blocs Elementor dupliqués pour chaque taille d'écran | Aucune hiérarchie lisible ; le sujet de la page n'est nulle part |
| **~150 mots de texte visible sur l'accueil**, l'essentiel du message porté par des images cliquables | Rien à extraire pour Google ni pour les moteurs IA |
| **Pas de meta description servie** (vérifié sur 4 pages) | Google et LinkedIn composent eux-mêmes l'extrait |
| Extrait social généré incluant l'URL brute d'une vidéo : `…/Video_AMRAE-2026-VF.mp4` en plein milieu de la description | Partage LinkedIn dégradé |
| **Aucun bloc JSON-LD détecté** sur les pages relevées | 79 établissements, zéro balisage `Organization`/`LocalBusiness` : le groupe n'existe pas comme entité structurée |
| Annuaire **conditionné au consentement cookies** (« *Pour afficher l'annuaire, acceptez les cookies […] puis actualisez la page* ») | Le contenu le plus utile du site est derrière un bandeau |
| Bandeau cookies = premier bloc de texte rencontré par un robot | Dilue l'extraction IA sur toutes les pages |
| « Actualités » = communication corporate (salons AMRAE, interviews, sponsoring) | Aucun contenu répondant à une question d'assuré ou de gestionnaire |
| Empilement WordPress 7.1 + Elementor Pro + store locator + Font Awesome + 4 familles Google Fonts | Risque Core Web Vitals — non mesuré ici |

**Verdict technique : notre site est devant.** Sur JSON-LD, meta descriptions, densité de
contenu utile, parité FAQ et extractibilité IA, `rushiti-renovation.fr` fait mieux que ce
site de groupe national. Il n'y a rien à reprendre de leur modèle de mise en page.

---

## 3. Ce qui est réellement transférable chez nous

### 3.1 Leur lexique — la vraie valeur de cet audit (priorité 1)

Notre page `/expert-assurance-sinistre-besancon` est déjà bien construite (devis en unités
d'œuvre, métrés pièce par pièce, séparation sinistre / hors sinistre, réserves écrites,
photos datées, relevés d'humidité, refus explicite de se prononcer sur la prise en charge).
Il lui manque les mots que le cabinet emploie lui-même :

| Mot du cabinet (relevé chez UE) | Présent chez nous | À faire |
|---|---|---|
| **missionnement / être missionné** | non | à intégrer : « artisan missionné par le cabinet » |
| **réparation en nature (REN)** | non | section dédiée : le mode où l'assureur fait réaliser les travaux au lieu d'indemniser |
| **règlement direct du prestataire** | non | à citer comme modalité connue, sans engagement de notre part |
| **gré à gré** | non | à citer dans la FAQ |
| **dossier contradictoire / de faible enjeu** | non | utile pour montrer qu'on connaît la typologie |
| **expertise à distance, visio-expertise** | non | on peut préparer un devis sur cette base |
| plateformes de missionnement (Sinapps, Darva) | non | **[À COMPLÉTER]** — n'écrire qu'après confirmation d'Isuf que nous y sommes raccordés ou non |

Un gestionnaire de sinistres qui lit une page d'artisan cherche ses propres repères.
C'est le seul vrai apport de ce site : **le vocabulaire**, pas le design.

Agents à mobiliser : `rushiti-page-service` (enrichissement de la page existante), puis
`rushiti-faq` pour deux questions supplémentaires. Pas de page neuve : le registre
`docs/seo/regjistri-fjale-kyce.csv` attribue déjà la cible « expert d'assurance cabinet de
sinistres » à `/expert-assurance-sinistre-besancon` — en créer une seconde serait de la
cannibalisation.

### 3.2 Leur format « 5 engagements » (priorité 3)

La page « Tiers de confiance » aligne cinq promesses courtes, chacune avec un sous-titre
d'une ligne. Format simple, lisible, sans chiffre. Transposable sur nos pages B2B :
interlocuteur unique, diagnostic gratuit sur site, devis au format attendu par l'expert,
phasage annoncé, remise en état à l'identique. À écrire sans aucun chiffre ni délai.

### 3.3 Ce qu'ils ne prennent pas et que nous prenons déjà

Aucune page de leur site ne répond aux questions réelles d'un assuré sinistré
(« mon plafond goutte », « qui paie quoi », « combien de temps pour sécher un mur »).
Ce terrain-là reste entièrement à nous, et nos articles blog l'occupent déjà.

---

## 4. L'opportunité commerciale (à arbitrer par Isuf)

Leur page « Gestion des sinistres » décrit explicitement une **gestion des prestataires**
avec « *Règlement du Prestataire REN et Expertise* » : le groupe fait réaliser des travaux
de remise en état par des entreprises, pour le compte des assureurs. Nos métiers
— plâtrerie, plafonds, peinture, sols après fuite — sont exactement ceux que la réparation
en nature consomme.

**Piste : se faire connaître des trois cabinets du Doubs comme artisan de remise en état
après dégât des eaux**, avec la page `/expert-assurance-sinistre-besancon` comme carte de
visite.

Ce qu'il faut vérifier avant tout contact — je ne le décide pas :

1. **Capacité** : combien de dossiers sinistres simultanés pouvons-nous absorber sans
   dégrader les chantiers particuliers ? → **[À COMPLÉTER]**
2. **Conditions tarifaires** : un référencement prestataire s'accompagne généralement de
   bordereaux ou de grilles imposées. **Décision purement commerciale : elle vous
   appartient**, je ne fournis que le cadre d'analyse.
3. **Pièces administratives** : attestation décennale ERGO (n° de contrat
   **[À COMPLÉTER]**), attestation RC pro, Kbis, RIB, URSSAF — le dossier classique de
   référencement.
4. **Délais d'intervention** : un cabinet demandera un engagement de prise de contact.
   Aucun délai ne sera écrit sans votre accord.

Agent à mobiliser le moment venu : `rushiti-prospection-b2b` (fiche cible + premier e-mail
de 120 mots), puis `rushiti-relance-b2b`. **Aucun e-mail ne part sans votre validation.**

---

## 5. Ce que je ne recommande pas

- Copier leur modèle de page (titres en images, H1 multiples, contenu sous consentement).
- Se présenter comme « partenaire », « agréé » ou « référencé » Union d'Experts : c'est
  faux tant qu'aucun référencement n'existe.
- Écrire quoi que ce soit sur une prise en charge assurance : notre page dit déjà, à
  raison, que nous ne nous prononçons jamais dessus.
