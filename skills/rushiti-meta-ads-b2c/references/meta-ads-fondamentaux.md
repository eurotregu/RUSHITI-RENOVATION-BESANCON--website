# Fondamentaux Meta Ads — artisan local B2C (RUSHITI)

Référence plateforme pour l'agent `rushiti-meta-ads-b2c`. Tout ce qui est décision Ads Manager (objectifs, audiences, formats, Pixel, lecture des chiffres) se prend ici. Les règles de voix et de marque restent dans le `SKILL.md` et `rushiti-defaults.md`.

## 1. Ce qui marche pour un artisan local (et ce qui ne marche pas)

Meta n'a pas de ciblage « propriétaire d'un appartement ancien avec une fuite ». Pour un artisan local, la mécanique gagnante est :

1. **Ciblage large mais géographiquement serré** — la précision vient du lieu, pas des centres d'intérêt.
2. **La créa filtre** — l'accroche nomme le problème ; seuls les gens concernés s'arrêtent.
3. **Une offre vraie et sans risque** — le diagnostic gratuit sur site. Pas de faux « -20 % cette semaine ».
4. **Le retargeting ramasse** — un projet de rénovation mûrit sur des semaines ; rester visible auprès des visiteurs du site coûte très peu et signe des devis.

Ce qui ne marche **pas** : les ciblages détaillés « propriétaires / travaux / immobilier » (approximatifs et restrictifs — Meta les a largement dépréciés), les audiences trop petites (moins de ~100 000 personnes : l'algorithme étouffe), une seule annonce jamais renouvelée (fatigue créative en 3-6 semaines sur une petite zone).

## 2. Choix de l'objectif de campagne par service

| Service | Comportement client | Objectif recommandé | Destination |
|---|---|---|---|
| Dégât des eaux | Urgence, veut parler à quelqu'un | **Prospects → appels/messages** (ou Messages Messenger/WhatsApp) | Téléphone 07 60 27 98 97 ou Messenger |
| Peinture intérieure | Projet à quelques semaines | **Prospects → formulaire instantané** | Formulaire qualifiant |
| Rénovation de pièce (SdB, cuisine) | Projet planifié, panier élevé | **Prospects → formulaire instantané** | Formulaire qualifiant |
| Sols / isolation | Saisonnier, souvent couplé | **Prospects → formulaire** ou trafic vers page service | Formulaire ou page dédiée du site |
| Retargeting (tous) | A déjà visité le site | **Prospects** ou **Trafic** selon volume | Page service visitée / formulaire |

Règle : pour l'urgence, réduire les étapes (bouton Appeler / Envoyer un message). Pour le planifié, accepter la friction d'un formulaire qualifiant — elle fait le tri.

## 3. Audiences locales

### Prospection (froid)
- **Géo** : Besançon + rayon 25 km par défaut (couvre la quasi-totalité des communes de `rushiti-defaults.md`). Option : « personnes vivant dans cette zone » (exclut les gens de passage).
- **Âge** : 28-65+ (avant 28 ans, très peu de propriétaires donneurs d'ordre).
- **Genre, centres d'intérêt** : tous / aucun. On laisse large, la créa filtre.
- **Placements** : Advantage+ (automatiques). Sur un petit budget local, restreindre les placements augmente les coûts.
- Une campagne par service actif. Nommage : `RUSHITI - [Service] - Prospection - [Zone]`.

### Retargeting (chaud) — nécessite le Pixel (§6)
Une seule campagne multi-services suffit au début :
- **Audience** : visiteurs du site 30 derniers jours (élargir à 90 j si volume trop faible) + interactions avec la page Facebook/Instagram 90 j.
- **Exclure** : les personnes ayant déjà contacté (événement Lead/Contact) — on ne paie pas pour reconvaincre un client acquis.
- **Créa** : preuve et réassurance (avant/après, avis Google, « diagnostic gratuit, toujours pas fait ? »), pas la même annonce que la prospection.
- Petit budget (10-20 % du total) : l'audience est petite, la dépasser = matraquage.

### Taille d'audience minimale
Un rayon de 25 km autour de Besançon ≈ 200 000+ adultes : suffisant. Ne jamais descendre à l'échelle d'un seul quartier en prospection (audience trop petite) — le quartier se nomme dans la **créa**, pas dans le ciblage.

## 4. Formats et specs des créas

| Format | Ratio | Usage |
|---|---|---|
| Carré | 1:1 (1080×1080) | Fil Facebook/Instagram |
| Vertical | 4:5 (1080×1350) | Fil mobile (meilleure surface) |
| Story/Reel | 9:16 (1080×1920) | Stories, Reels |

- **Avant/après** : le format roi de la rénovation. En image unique (split vertical AVANT | APRÈS) ou en **carrousel** (carte 1 : avant, carte 2 : après, cartes suivantes : étapes du chantier — le carrousel raconte la méthode, très RUSHITI).
- **Vidéo** : 15-30 s, sous-titrée (lecture sans son), chantier réel > animation.
- **Texte incrusté** : lisible en 2 s, nommer le lieu (« Palente, Besançon »). Meta ne pénalise plus strictement les 20 % de texte mais une image chargée performe moins.
- **Limites de caractères affichés** : texte principal ~125 car. avant troncature (mettre l'accroche en première phrase), titre 40 car., description 30 car.
- Photos de chantier : accord client écrit avant diffusion (RGPD) ; jamais de visage, d'adresse précise ni d'intérieur identifiable sans accord.

## 5. Formulaire instantané qualifiant

Un formulaire Meta pré-rempli produit des contacts qui oublient avoir postulé (« amnésie sociale »). La friction volontaire fait le tri :

1. Type **« Volume de leads supérieur » → non** : choisir **« Higher intent »** (écran de relecture avant envoi).
2. **2-3 questions qualifiantes** (choix multiples, pas de champ libre) :
   - « Quelle pièce est concernée ? » (salon / chambre / SdB / cuisine / autre)
   - « Votre projet démarre… » (dès que possible / sous 3 mois / je me renseigne)
   - Pour un sinistre : « Votre assurance est-elle prévenue ? » (oui / non / en cours)
3. Champs contact : nom, téléphone, code postal (le code postal confirme la zone).
4. Écran de fin : rappeler la suite (« Nous vous rappelons sous PLACEHOLDER pour convenir du diagnostic gratuit sur site ») + lien vers rushiti-renovation.fr.
5. **Rappel opérationnel** : un contact Meta se rappelle dans l'heure si possible — au-delà de 24 h, le taux de réponse s'effondre. À mettre dans la check-list de chaque pack.

## 6. Pixel Meta sur le site (statique, GitHub Pages)

### Consentement d'abord (CNIL — non négociable)
En France, le Pixel Meta est un traceur publicitaire : **consentement préalable obligatoire**. Sur un site statique, la solution simple :
- un bandeau cookies maison (ou une lib légère type tarteaucitron.js) qui ne charge le Pixel **qu'après** clic « Accepter » ;
- le Pixel ne se charge jamais en dur dans le `<head>` sans ce garde ;
- mention du Pixel dans la politique de confidentialité du site.
Livrer le volet Pixel du pack avec ces trois éléments, sinon ne pas le livrer.

### Pose
1. Events Manager → créer le Pixel → récupérer l'ID (`PLACEHOLDER_PIXEL_ID`).
2. Snippet de base chargé **après consentement** sur toutes les pages (`index.html`, pages service).
3. Événements utiles sur un site vitrine sans tunnel :
   - `PageView` (automatique) ;
   - `Contact` sur clic des liens `tel:` et `mailto:` ;
   - `Lead` sur envoi du formulaire de contact.
   Sur ce site (formulaire qui ouvre le client email), accrocher `Contact` au clic du bouton d'envoi.
4. Vérifier avec l'extension Meta Pixel Helper + l'onglet « Test des événements » d'Events Manager.
5. Domaine vérifié dans Business Manager (Paramètres → Sécurité de la marque → Domaines).

### Ce que le Pixel débloque
- Audiences de retargeting (§3).
- Optimisation des campagnes trafic sur les vraies actions (Contact) plutôt que le clic.
- Plus tard : audiences similaires (lookalike) des personnes ayant contacté — utile seulement quand il y a quelques centaines d'événements.

## 7. Budget et montée en charge

- Tous les montants en `PLACEHOLDER` — c'est Isuf qui fixe. Donner la **répartition**, pas les montants : ~80-90 % prospection / 10-20 % retargeting.
- Ordre de grandeur à expliquer sans le promettre : un budget trop éclaté n'apprend pas ; mieux vaut **un service, une campagne** bien dotée que quatre campagnes anémiques. Démarrer avec 1-2 services (dégât des eaux + un planifié), élargir ensuite.
- **Phase d'apprentissage** : Meta se stabilise après ~50 conversions par ensemble ou 1-2 semaines. Aucune décision structurelle (couper, doubler) avant ce cap, sauf dépense sans aucune impression (problème de diffusion, pas de performance).
- Scaling : +20-30 % de budget à la fois, pas de doublement brutal (relance l'apprentissage).

## 8. Lecture des chiffres (grille de diagnostic)

Ordre de lecture, chaque étage expliquant le suivant :

| Symptôme | Cause probable | Action |
|---|---|---|
| Peu ou pas d'impressions | Annonce refusée, budget trop bas, audience trop étroite | Vérifier l'état de l'annonce, élargir la zone |
| CPM très élevé (> ~15-20 € local) | Audience trop petite, créa jugée faible | Élargir le rayon, changer de créa |
| CTR < ~1 % | L'accroche n'arrête personne | Nouveau concept (pas une retouche) : autre angle, autre visuel |
| Clics mais pas de contacts | Décalage annonce/destination, formulaire trop long ou trop court | Aligner la destination sur l'accroche, revoir le formulaire |
| Contacts mais pas de devis sérieux | Formulaire sans friction, offre ambiguë | Ajouter les questions qualifiantes, repréciser l'offre |
| Ça marchait, ça s'essouffle | Fatigue créative (fréquence > 3-4) | Nouvelles créas, pas plus de budget |

Le juge de paix n'est **jamais** le coût par contact seul : c'est le nombre de **diagnostics posés puis de devis signés**. Le noter dans chaque section Suivi.

## 9. Politique publicitaire Meta — pièges pour un artisan

- **Attributs personnels** : interdiction d'affirmer ou de sous-entendre une caractéristique de la personne (situation financière, âge…). « Vous êtes propriétaire ? » est risqué ; « Une auréole au plafond ? » est sûr. Toujours formuler côté problème/logement, jamais côté personne.
- **Avant/après** : autorisé pour la rénovation de bâtiment (l'interdiction vise l'image corporelle). Rester factuel, pas de résultat garanti.
- **Qualité de la page de destination** : la page doit correspondre à l'annonce, coordonnées visibles.
- Une annonce refusée n'est pas une catastrophe : corriger la formulation et demander la révision. Ne jamais contourner (comptes dupliqués, textes trompeurs) — c'est le compte entier qui saute.
