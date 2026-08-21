# Plan éditorial — rushiti-renovation.fr — Automne 2026 (septembre → novembre)

> Produit par `rushiti-architecte-seo` le 21/08/2026 (mode plan éditorial).
> **Sources** : registre canonique `docs/seo/regjistri-fjale-kyce.csv`
> (synchronisé GSC 12 mois, 21/08/2026) · rapport KPI #1
> (`docs/seo/raporte/raport-fjale-kyce-2026-08.md`) · opportunités GSC
> (`docs/seo/opportunites-gsc-2026-08.md`, export du 20/08) · doctrine
> saisonnière maison (isolation à l'automne, sinistres en hiver, façades au
> printemps). **Limite déclarée** : le sitemap en ligne n'était pas accessible
> depuis l'environnement de travail (proxy) — l'état du site est celui du
> registre, vérifié dans le HTML de production le 21/08/2026.
> **Garde-fous** : chaque ligne repasse la porte PORTA avant rédaction (les
> lignes déjà consignées citent leur date de verdict) ; les fenêtres sont des
> repères de travail, jamais des promesses ; aucun chiffre hors sources
> citées ; rien n'est publié sans validation d'Isuf.

## Pourquoi ce plan a cette forme

L'automne bisontin est la saison où les problèmes d'humidité redeviennent
visibles : premier chauffage → condensation sur les murs nord, moisissures en
salle de bains, et l'hiver qui suit est la haute saison des dégâts des eaux.
Le registre montre que la demande est déjà là (le cluster moisissure est la
2e visibilité du site ; « mur froid » est consigné « à créer — octobre
2026 ») et que le silo le plus rentable — dégât des eaux — est quasi
invisible (33 impressions en 12 mois, position 16). Le plan renforce donc
d'abord ce qui imprime déjà, puis crée peu mais au bon moment — publier 6 à
8 semaines avant le pic, pas pendant.

## Roadmap automne 2026

| # | Sujet | Silo → pilier | Famille | Protocoles | Priorité | Fenêtre | Statut |
|---|---|---|---|---|---|---|---|
| 1 | **Enrichir l'article moisissure** : H2 « Moisissure au plafond malgré la VMC : pourquoi ça revient » (réponse directe extractible), bloc conversion « à partir de quand il faut un professionnel » + diagnostic gratuit, 2 liens vers `/degat-des-eaux-besancon` et `/peinture-interieure-besancon` | Transverse → DDE + Peinture | Pathologie (enrichissement) | DÉGÂT DES EAUX · AEO | 🔴 1 | **Septembre** — avant le premier chauffage ; preuve : « …malgré vmc » = 1re requête du site (137 impr, pos. 11,2), cluster ≈ 620 impr avec 2 clics, article 1 385 impr/12 m (registre + opportunités GSC) | Porte passée → **vérifié live le 21/08 (soir)** : H2 « malgré la VMC », bloc conversion et maillage **déjà déployés en production** ; compléments restants (FAQ, photos avant/après RGPD, pied d'article) livrés dans `docs/seo/contenus/moisissure-plafond-enrichissement.md` — en validation |
| 2 | **Enrichir le pilier `/degat-des-eaux-besancon`** : section assèchement (mesures à l'humidimètre), déroulé du chantier avec l'assurance (langage IRSI, sans promesse de prise en charge), maillage renforcé depuis les 3 satellites DDE existants du blog | 5. Dégât des eaux | Enrichissement pilier | DÉGÂT DES EAUX · PRIX (facteurs) · AEO | 🔴 2 | **Octobre** — 6-8 semaines avant la haute saison hivernale des sinistres (doctrine maison, à affiner via rushiti-google-trends) ; preuve : « PRIORITETI 1 i forcimit », 33 impr/12 m pos. 16 (registre 21/08) | Porte passée (renfort d'existant + sous-cible assèchement consignée le 20/08) |
| 3 | **Article « Mur froid et condensation : que faire ? »** — murs nord, premier chauffage, pièces peu ventilées ; quand l'isolation intérieure devient la vraie réponse | 4. Isolation → `/isolation-interieure-besancon` | Pathologie | BÂTI ANCIEN · AEO | 🟠 3 | **Octobre** — fenêtre fixée par le registre (« artikull blogu — tetor 2026 ») ; symptôme très recherché en saison froide | Porte passée (verdict « për krijim » consigné le 20/08) → prochain pas : Briefé (rushiti-brief-seo) |
| 4 | **Enrichir le pilier `/isolation-besancon`** : sections combles perdus et condensation de saison froide — la requête combles est attribuée à cette page (pas de nouvel article), l'ITI vient d'être re-maillée depuis l'accueil (PR #19 mergé) | 4. Isolation | Enrichissement pilier | BÂTI ANCIEN · AEO | 🟠 4 | **Octobre-novembre** ; preuve : 184 impr pos. 28,3 avec 0 clic (12 m), ITI 0 impression — forcim décidé au registre, pas de chirurgie de balises | Porte passée (renfort d'existant, registre 21/08) |
| 5 | **Article « Prix du placo au m² à Besançon »** — sur le modèle de l'article prix peinture ; fourchettes `[À VALIDER PAR ISUF]`, pédagogie des facteurs de prix | 2. Plâtrerie-placo → `/platrerie-besancon` | Budget & décision | PRIX · AEO | 🟡 5 | **Rédaction novembre → publication début décembre** (fenêtre fixée par le registre : « dhjetor 2026 ») | Porte passée (verdict « për krijim » consigné le 20/08) → Briefé le moment venu |
| 6 | **Candidat : « Peut-on repeindre en hiver ? »** — température, humidité, séchage : la saison intérieure expliquée (les chantiers peinture ne s'arrêtent pas au froid, ils changent de règles) | 1. Peinture → `/peinture-interieure-besancon` | Méthode & pédagogie | AEO | 🟢 6 | **Novembre**, si la demande se confirme | **Idée** — preuve de demande absente (PV) : valider volume (Keyword Planner / Trends) puis verdict PORTA avant tout brief |

## Écarté de ce plan, et pourquoi

- **Enduit à la chaux** (30-41 impr, pos. ≈ 5) et **rénovation boiseries /
  bois** (58 impr, pos. 6,2) : **arbitrage rendu le 21/08 au soir — Isuf :
  prestations non offertes.** Classés sans suite au registre (REFUZOHET) ;
  aucune page ne sera créée, la demande observée reste sciemment non servie
  car hors offre.
- **Moquette** : arbitrage d'offre toujours en attente.
- **Nouvel article « isolation des combles »** : refusé — la requête est
  attribuée au pilier `/isolation-besancon` (registre, ligne combles) ; un
  article séparé fabriquerait la cannibalisation que la ligne 4 évite en
  enrichissant le pilier.
- **Sujets façade / crépi / peinture extérieure** : hors saison (pic au
  printemps). Exception à surveiller : la demande crépi (191 impr) — décision
  conditionnelle au re-export GSC du ~1er octobre (voir ci-dessous), et c'est
  une page service, pas un article de blog.
- **Pages quartier/commune** : hors périmètre de ce plan — grille gouvernée
  par `rushiti-keyword-map`, production par `rushiti-page-locale`,
  consolidation en cours (63 pages qui impriment épargnées).

## Les 3 prochaines actions, routées

1. ✅ 21/08 (soir) — **Ligne 1 traitée** : accord d'Isuf reçu ; la lecture
   live a révélé les trois actions du brief **déjà déployées en production**.
   Le paquet A-B-C-D livre les compléments restants — FAQ, photos RGPD, pied
   d'article — en validation dans `docs/seo/contenus/`.
2. **Briefs des lignes 2 et 3** → `rushiti-brief-seo` (le pilier DDE mérite
   une analyse SERP dédiée ; « mur froid » a besoin de son angle
   différenciant), puis rédaction ici.
3. **Caler les fenêtres au réel** → `rushiti-google-trends` (saisonnalité
   fine de « condensation », « dégât des eaux », « isolation ») et
   **re-export GSC vers le 1er octobre** → `rushiti-regression-seo` /
   rapport #2 — il tranche aussi la décision crépi et mesure l'effet des
   corrections déployées en août.

## Journal du plan

| Date | Événement |
|---|---|
| 21/08/2026 | Création du plan automne 2026 (6 lignes : 3 enrichissements, 2 créations consignées au registre, 1 candidat à valider). Aucune ligne rédigée à ce jour. |
| 21/08/2026 (soir) | **Arbitrages rendus par Isuf** : enduit à la chaux — non offert ; rénovation boiseries — non couverte. Registre mis à jour (REFUZOHET, lignes chaux et bois). |
| 21/08/2026 (soir) | **Ligne 1** : lecture live de l'article moisissure — les 3 actions du brief (H2 VMC, bloc conversion, maillage) déjà déployées en production ; paquet A-B-C-D des compléments (FAQ, photos RGPD, pied d'article) livré dans `docs/seo/contenus/moisissure-plafond-enrichissement.md`, en validation. |
