# Référence Google Ads RUSHITI — playbook complet

Base de travail stable pour les 4 modes. Les chiffres marqués « repère » sont des ordres de grandeur du marché français des artisans locaux, pas des promesses : les vrais chiffres viennent toujours des exports d'Isuf.

## 1. Cadre budgétaire et ses conséquences

Budget : **300-500 €/mois → 10-16 €/jour**. CPC repère pour « peintre besançon » et assimilés : 2-5 €. Donc **3-6 clics/jour** — chaque clic compte. Conséquences non négociables à ce budget :

- **Search uniquement.** Performance Max exige ~30 conversions/mois pour apprendre ; Display et Demand Gen font de la notoriété, pas des leads. À revoir seulement quand le compte a un historique de conversions stable sur 6 mois.
- **Phrase + exact match uniquement** au lancement. Broad match envisageable après 3 mois de données et une liste de négatifs mûre.
- **Une seule campagne**, 2-3 ad groups. Multiplier les campagnes fragmente un budget déjà petit et empêche tout apprentissage.
- Objectif CPA : **30-50 €/lead**. Un chantier moyen le justifie largement ; au-delà de 50 € soutenus, quelque chose est mal réglé (ciblage, négatifs, annonces).

## 2. Structure de campagne cible

**Campagne** : « Search — RUSHITI Besançon » · Réseau de recherche uniquement (décocher Display ET partenaires de recherche) · Zone : Besançon + rayon ~25 km · Option de zone : **« Présence : personnes se trouvant dans les zones ciblées »** · Langue : français · Enchères au lancement : Maximiser les clics avec **plafond CPC ~4 €** → passer à Maximiser les conversions après 15-20 conversions enregistrées.

**Ad groups et lancement en deux temps :**

| Ad group | Lancement | Pourquoi |
|---|---|---|
| 1. Peinture intérieure | Semaine 1 | Volume de recherche le plus fort, intention claire |
| 2. Rénovation complète | Semaine 1 | Panier moyen élevé, requêtes « rénovation appartement/maison » |
| 3. Dégât des eaux | Dès que le tracking a prouvé qu'il enregistre (≥1 conversion test + 1 réelle) | Urgence forte (le client appelle tout de suite) mais volume plus faible : il mérite le budget seulement quand on sait mesurer |

## 3. Mots-clés par ad group (phrase " " et exact [ ])

**Ad group 1 — Peinture intérieure** → destination : page/section peinture
"peintre besançon" · "peintre en batiment besançon" · "entreprise peinture besançon" · "artisan peintre besançon" · [devis peinture besançon] · "peinture intérieure besançon" · [devis peinture intérieure] · "peintre appartement besançon" · "peintre doubs"

**Ad group 2 — Rénovation complète** → destination : index / page rénovation
"rénovation appartement besançon" · "entreprise rénovation besançon" · "rénovation maison besançon" · [devis rénovation besançon] · "rénovation intérieure besançon" · "travaux rénovation besançon" · "rénovation salle de bain besançon"

**Ad group 3 — Dégât des eaux** → destination : page dégât des eaux (à créer si absente — déléguer à `rushiti-page-locale` / `rushiti-brief-seo`)
"peintre dégât des eaux besançon" · "réparation plafond dégât des eaux" · "peinture après dégât des eaux" · [dégât des eaux plafond besançon] · "remise en état dégât des eaux besançon"

Enrichissement continu : le search terms report hebdo est la meilleure source de nouveaux mots-clés (une requête qui convertit → l'ajouter en exact). Croiser aussi avec la GSC : les requêtes qui apportent déjà des clics organiques convertissent aussi en payant.

## 4. Liste de négatifs de départ

En type **expression** sauf mention contraire :

- Emploi/formation : "emploi" · "offre d'emploi" · "recrutement" · "salaire" · "formation" · "cap peintre" · "cours" · "tuto" · "comment peindre" · "comment faire"
- Magasins/produits : "leroy merlin" · "castorama" · "brico dépôt" · "bricomarché" · "pot de peinture" · "location" · "matériel"
- Hors cible : "gratuit e" (⚠️ ne JAMAIS mettre "gratuit" seul — ça bloquerait « devis gratuit » ; exclure seulement les formes nuisibles constatées dans le search terms report, ex. [peinture gratuite]) · "forum" · "avis" (à surveiller : peut aussi bloquer des requêtes utiles — n'ajouter que si le report montre du gaspillage) · "stage" · "alternance"

Règle : **tout négatif proposé est vérifié contre les mots-clés actifs** avant recommandation. Un négatif qui chevauche un mot-clé acheté coupe la campagne en silence.

## 5. Réglages non négociables du compte

1. **Mode expert** dès la création (refuser le « Smart Mode » que Google propose par défaut aux débutants).
2. **Recommandations auto-appliquées : désactivées** (Paramètres → Recommandations auto-appliquées → tout décocher). La plupart augmentent la dépense sans améliorer les leads.
3. Réseau **Display décoché**, **partenaires de recherche décochés** dans les paramètres de campagne.
4. Ciblage géo en mode **Présence** (Paramètres → Zones → Options de zones).
5. Calendrier de diffusion : à régler après 1 mois de données (couper typiquement après 21h et ajuster le week-end selon les heures réelles des leads).

## 6. Tracking sur site statique Cloudflare Pages

Deux conversions, pas plus au départ :

| Conversion | Déclencheur | Mise en œuvre |
|---|---|---|
| Demande de devis | envoi du formulaire de contact | gtag event sur le submit (ou GTM trigger « form submit ») |
| Appel téléphonique | clic sur un lien `tel:` (mobile) | gtag event sur le clic des liens tel: |

- **gtag.js direct** suffit (un snippet dans le HTML de chaque page + un event par conversion). GTM est une option de confort, pas une obligation.
- **Consent Mode v2 obligatoire** (RGPD, exigé par Google dans l'UE depuis mars 2024) : sans lui, les conversions sont mal comptées et le site est hors conformité. Solution adaptée à un site statique français : **tarteaucitron.js** (gratuit, français) ou Axeptio. Le bandeau doit être en place **avant** le premier euro dépensé.
- Test obligatoire avant lancement : soumettre soi-même un formulaire test et vérifier que la conversion apparaît dans Google Ads (délai possible de quelques heures).
- Lier le compte Ads à la **fiche Google Business** → active les assets de lieu (adresse sous l'annonce). Voir `rushiti-fiche-google-business` pour l'état de la fiche.
- GA4 : utile mais non bloquant — mois 2.

## 7. Local Services Ads (LSA)

À vérifier une fois sur ads.google.com/localservices : la disponibilité de la catégorie « peintre » à Besançon change selon les zones. Si disponible, **priorité sur le Search classique** pour un débutant : paiement au lead (pas au clic), badge de confiance Google, budget mieux protégé. Le Search reste en complément. Ne jamais affirmer la disponibilité sans vérification du jour.

## 8. Benchmarks de lecture (repères, pas promesses)

| Métrique | Repère sain (Search local artisan FR) | Signal d'alerte |
|---|---|---|
| CTR | supérieur à 5 % | inférieur à 3 % : annonces ou mots-clés hors sujet |
| CPC | 2-5 € | supérieur à 6 € soutenu : concurrence ou Quality Score faible |
| CPA | 30-50 € | supérieur à 50 € sur 3+ semaines : revoir négatifs/annonces/landing |
| Taux de conversion | 5-10 % | inférieur à 3 % : page de destination ou ciblage à revoir |
| Quality Score | 7+ | 5 ou moins : cohérence mot-clé ↔ annonce ↔ page à retravailler |

Fenêtre minimale de jugement : **2 semaines ou ~100 clics** par élément jugé.

## 9. Plan 30 jours (mode setup)

- **Semaine 1 — technique (0 € dépensé)** : compte en mode expert · auto-apply off · bandeau consentement + Consent Mode v2 sur le site · 2 conversions configurées et testées · liaison fiche Google Business · vérification LSA.
- **Semaine 2 — matière** : extraction GSC des requêtes qui convertissent déjà en organique · listes de mots-clés ad groups 1-2 (section 3) · liste de négatifs (section 4) · comprendre phrase vs exact.
- **Semaine 3 — annonces et lancement** : 1 RSA par ad group (mode 3) · sitelinks, callouts, asset d'appel · réglages section 5 · budget 12-15 €/jour · **lancement**.
- **Semaine 4 — première lecture** : search terms → négatifs tous les 2-3 jours · lecture CTR/CPC/CPA (section 8) · fin de semaine : premier rapport hebdo (mode 2) · décision d'activer l'ad group Dégât des eaux si le tracking a prouvé.

## 10. Checklist de lancement (tout doit être vert avant le premier euro)

- [ ] Compte en mode expert, recommandations auto-appliquées désactivées
- [ ] Bandeau cookies + Consent Mode v2 actifs sur rushiti-renovation.fr
- [ ] 2 conversions testées (formulaire test enregistré dans Ads)
- [ ] Fiche Google Business liée
- [ ] Ciblage Besançon + rayon, option « Présence »
- [ ] Display et partenaires de recherche décochés
- [ ] 2 ad groups, mots-clés phrase/exact uniquement
- [ ] Liste de négatifs chargée (15+ termes)
- [ ] 1 RSA par ad group, « Besançon » dans 2+ titres, preuves validées uniquement
- [ ] Asset d'appel (07 60 27 98 97) + 4 sitelinks + callouts
- [ ] Budget quotidien 12-15 €, Maximiser les clics, plafond CPC ~4 €
- [ ] Rendez-vous hebdo fixé : lundi, 15 min, search terms report

## 11. Gabarit du bilan mensuel (mode 4)

```markdown
# Bilan Google Ads — [MOIS ANNÉE]

## Chiffres du mois
| | Ce mois | Mois précédent | Évolution |
|---|---|---|---|
| Dépense | | | |
| Clics | | | |
| CTR | | | |
| CPC moyen | | | |
| Conversions | | | |
| CPA | | | |
(mois précédent : seulement si l'export est fourni — sinon colonne « non mesuré »)

## Ce qu'il faut retenir (3-5 points)
[Chaque point : le chiffre + ce qu'il signifie + ce qu'on en fait.]

## Par ad group
[Tableau dépense/conversions/CPA par ad group + une ligne de lecture chacun.]

## Actions du mois prochain
1. ...
```

## 12. Dashboard HTML (mode 4)

Fichier HTML **autonome** (CSS inline, aucune ressource externe), aux couleurs de la charte rushiti-renovation.fr :

| Rôle | Couleur |
|---|---|
| Primaire (titres, barres principales) | `#1a5632` (vert), variantes `#2a7a4a` / `#0e3a1f` |
| Accent (mises en avant, deltas positifs) | `#d4a843` (doré), clair `#e8c76a` |
| Texte | `#333333`, secondaire `#666666` |
| Fonds | `#ffffff`, sections `#faf8f5`, bordures `#e8e8e8` |
| Police | Montserrat pour les titres (fallback sans-serif), system-ui pour le corps |

Contenu : bandeau de titres (logo texte « RUSHITI Rénovation — Google Ads »), 4-6 tuiles de KPI (dépense, clics, CTR, conversions, CPA, évolution), un graphique en barres dépense/conversions par ad group (SVG inline), le tableau des top termes de recherche, la liste d'actions. **Aucun chiffre qui ne vienne pas de l'export.** RGPD : jamais de nom de client ni de détail de chantier identifiable dans le dashboard.

## 13. Frontières avec les autres agents

- Page de destination à créer ou renforcer → `rushiti-brief-seo` puis `rushiti-page-locale`.
- Fiche Google Business (liaison, assets de lieu) → `rushiti-fiche-google-business`.
- Suivi du SEO organique (gratuit, complémentaire) → `rushiti-regression-seo`, `rushiti-ctr-opportunites`.
- Prospection B2B syndics/gestionnaires/assurances → `rushiti-prospection-b2b` / `rushiti-relance-b2b`. **Jamais de budget Ads sur ces cibles** à ce niveau de budget ; seule exception envisageable au-delà de 800 €/mois : un exact match du type [ravalement copropriété besançon], à décider avec Isuf.
