# Arbitrage — le playbook « The 10-Skill SEO Engine » (plan du 23/08/2026)

> Réponse au playbook proposant d'installer 11 skills génériques
> (`/seo-onboard`, `/keyword-map`, `/serp-scan`, `/content-brief`,
> `/onpage-audit`, `/citation-gap`, `/geo-writer`, `/schema-smith`,
> `/internal-linker`, `/rank-tracker`, `/content-refresh`) et un skill
> « ultra-master » pour RUSHITI Rénovation.
>
> **Verdict : les trois idées de fond sont justes et déjà appliquées ; les
> 11 skills ne doivent pas être installés — dix de leurs onze rôles sont déjà
> tenus par des agents RUSHITI plus spécialisés. Ce qui manquait vraiment est
> le chef d'orchestre, et le brouillon « ultra-master » fourni contenait
> neuf erreurs factuelles qui l'auraient rendu dangereux tel quel.**
>
> Relevés du 22-23/08/2026 : sitemap de rushiti-renovation.fr,
> roster des agents RUSHITI (une cinquantaine), rapport KPI #1
> (rapport du 21/08/2026, export 12 mois), plan consolidé du 22/08/2026.

## 1. Ce que le plan supposait, et ce qui est vrai

| Hypothèse du playbook | État réel au 23/08/2026 |
|---|---|
| « Installez ces 11 skills, votre site n'en a pas » | Faux. La suite RUSHITI compte **une cinquantaine d'agents**, dont dix couvrent déjà les onze rôles proposés — et couvrent en plus le devis d'assurance IRSI, le mémo de chantier, la prospection B2B, les avis Google, l'indexation, la saisonnalité |
| « Un pilier + 6 à 15 pages par sujet » | La grille a été **volontairement réduite de plus de moitié** parce que le trop-plein se cannibalisait. Appliquer la recette défait un travail payé |
| « Lancez `/keyword-map` en semaine 1 pour construire votre carte » | La carte existe : registre `docs/seo/regjistri-fjale-kyce.csv`, avec une porte de création à 4 contrôles anti-cannibalisation |
| « Lancez `/onpage-audit` en semaine 2 » | L'audit du 13/08/2026 est rendu, et déjà routé en **14 entrées priorisées** dans le plan consolidé du 22/08 |
| « `/citation-gap` : trouvez où les concurrents sont cités » | L'outillage existe (`rushiti-citation-ia`, `rushiti-part-de-voix-ia`, panel figé de 14 requêtes, dictionnaire de colonnes, modèle CSV) — mais **aucune mesure de citation n'a encore été prise**. C'est le seul vrai trou du dispositif |
| « `/rank-tracker` : un tableau, mot-clé → position Google → statut IA » | Deux portes, **deux dénominateurs, trois cadences** : Google se relit en 4-6 semaines, la part de voix IA au mois, le corpus cité en 6-8 semaines. Un tableau unique fait lire un mouvement Google comme un mouvement IA |
| Tableau de prix « 45-75 €/m² TTC » | Aucun prix validé par Isuf. Un tarif publié devient opposable devant un client ou un expert d'assurance |
| « DTU 25.1 et 60.1 comme preuve d'expertise » | Normes réellement applicables : **DTU 59.1** (peinture), **25.41** (plaques de plâtre), **53.2** (sols souples), convention **IRSI**. Une norme fausse décrédibilise devant le lecteur qu'on visait |
| « Téléphone : +33 3 81 XX XX XX (à mettre à jour) » | Le numéro existe : **07 60 27 98 97** · `tel:+33760279897`. Un placeholder qui ressemble à un fixe local est pire qu'un trou déclaré |
| « SARL RUSHITI Rénovation » | **RUSHITI Rénovation** est le nom commercial ; **Rushiti** la dénomination sociale, réservée aux mentions légales |
| « 20+ ans d'expérience » comme fait unique | Deux faits distincts : Isuf exerce **depuis 20 ans**, l'entreprise est née le **04/11/2021**. Les fusionner est faux et vérifiable au RCS |
| « lat/long approximatives : 47.2380, 6.0244 » | Une coordonnée approximée est une **erreur d'entité** que les moteurs recoupent et propagent |
| « taxID : FR + 11 chiffres de contrôle + SIREN » | La TVA est **FR89905214631**, relevée — pas recalculée |
| « Zone : Besançon, Doubs, secteur Montbéliard » avec quartiers « La Boucle, Planoise, Chaprais » | Zone validée : Besançon + communes du **Doubs (25)**. Quartiers canoniques : Battant, Chaprais-**Cras**, **Planoise-Châteaufarine**… « La Boucle » n'est pas un quartier SEO |
| « Services : … ravalement de façade » | `/ravalement-facade-besancon` a été **fusionné en 301** vers `/peinture-exterieure-besancon` (PR #14). Le ravalement seul n'est pas une offre confirmée |
| Mode `--fast` : « saute l'analyse concurrentielle et utilise les manques supposés » | Une hypothèse présentée comme un constat est **une invention avec une étiquette** |

**Ce qui est juste dans le playbook, et qui a été retenu :** les trois idées
de fond — posséder le sujet plutôt que le mot-clé, écrire des pages
extractibles qui répondent dans les deux premières phrases, surveiller les
deux portes. Elles sont vraies, et ce sont elles qui structurent le moteur
livré.

## 2. Ce qui a été livré

- **Skill `rushiti-seo-engine`** (`.claude/skills/rushiti-seo-engine/`) : le
  chef d'orchestre qui manquait. Il ne rédige rien — il décide quel agent
  tourne, sur quoi, dans quel ordre, et il refuse une phase à laquelle le
  dépôt a déjà répondu. Quatre modes (CAMPAGNE, CADENCE, TRIAGE, ÉTAT),
  protocole en **8 phases**, cinq blocs de livrables.
  - `references/protocole-8-phases.md` — entrée exigée, critère de passage,
    motif de blocage et livrable de chaque phase.
  - `references/correspondance-10-skills.md` — les 11 rôles du playbook face
    aux agents RUSHITI, plus ce que RUSHITI a en plus.
  - `references/etat-du-moteur.md` — la ligne de départ datée et sourcée
    (l'équivalent du `seo-brief.md` du playbook, mais mesuré, pas déclaré).
  - `references/cadence-et-campagnes.md` — les 30 premiers jours calés sur
    les vagues du plan consolidé, puis les rituels lundi / mensuel /
    mensuel (dont part de voix IA) / 6-8 semaines (corpus cité) /
    trimestriel, plus le contrôle crawlers à chaque déploiement.
  - `references/pieges-plans-seo-generiques.md` — le catalogue des défauts
    par famille, et ce que ces plans ont **raison** de dire.
- **Prompt maître** (`docs/seo/prompts/prompt-maitre-moteur-seo.md`) :
  version bridée du protocole, pour les outils IA hors dépôt.

## 3. La phase que le playbook n'a pas — et pourquoi elle compte

Le playbook générique enchaîne 7 phases en commençant par l'analyse
concurrentielle. Sur un site de plusieurs centaines d'URL déjà consolidé, commencer là revient
mécaniquement à proposer de créer ce qui existe.

Le moteur livré ajoute donc une **phase 0 — ÉTAT** : qu'avons-nous déjà, et
qu'est-ce qui imprime ? Puis une **phase 1 — PORTE** qui rend un verdict
écrit *renforcer / créer*, infranchissable.

C'est ce qui change la sortie la plus fréquente du moteur. Elle n'est pas
« voici dix pages à créer », elle est : **« ne créez rien : cette page
existe, elle est à trois corrections de la page 1 »**.

Les données du dépôt le confirment : **79 % des clics viennent de l'accueil**
pendant que les piliers restent en pages 2 à 5, le cluster « entreprise de
peinture à besançon » fait **1 343 impressions en position 3,5 pour 0 clic**,
et `/platrerie-besancon` (position 9,1) comme `/ratissage-enduit-besancon`
(10,9) sont à une porte de la page 1 sans qu'aucun pilier voisin ne les
pousse. Le gisement n'est pas dans la création — il est dans la conversion de
ce qui est déjà visible.

## 4. Le seul vrai manque que le playbook a bien vu

Le playbook insiste sur la porte IA, et il a raison : **c'est le seul volet
du dispositif RUSHITI qui est outillé mais dont la citation n'a jamais été
mesurée**.

Au 23/08/2026 : part de voix IA `NM`, relevé de corpus cité `NM`. Le panel de
14 requêtes est figé, le dictionnaire de colonnes est écrit, le modèle CSV est
prêt — aucun relevé n'a été consigné.

Le volet crawlers, lui, n'est pas vierge : un incident réel a déjà été constaté
sur ce site — **le robots.txt managé de Cloudflare bloquait silencieusement
tous les crawlers IA de rushiti-renovation.fr**. C'est un mode de panne connu,
silencieux, et qui revient à chaque changement de configuration : son état
actuel demande une revérification, pas une première découverte.

L'ordre correct pour l'ouvrir, inscrit en semaine 3 de la cadence :

1. `rushiti-visibilite-ia` — les moteurs **peuvent**-ils lire le site ?
2. `rushiti-part-de-voix-ia` — première mesure, elle devient la référence.
3. `rushiti-citation-ia` — quelles sources sont citées à notre place, et par
   quelle porte y entrer.

Mesurer la citation d'un site que les crawlers ne lisent pas ferait perdre la
mesure **et** le temps : c'est pour cela que l'ordre ne se raccourcit pas.

## 5. Décision sur l'installation des skills génériques

**Ne pas installer les 11 skills du playbook.** Motif : dix de leurs rôles
sont déjà tenus par des agents plus spécialisés, déjà bridés sur le NAP, la
zone, les DTU, l'offre confirmée et les interdits Google. Un skill générique
importé tel quel arrive **sans aucun de ces verrous** — et deux agents qui se
contredisent sur un prix ou une zone coûtent plus cher qu'un agent absent.

Si un manque réel apparaît, il se comble par `rushiti-agent-creator`, qui
produit un agent aux normes de la maison.

## 6. Ce qui attend une décision d'Isuf

| Question | Réponse attendue |
|---|---|
| **« devis sous 48 h »** est-il un engagement affichable ? Il figure dans un title live et dans les preuves du registre, mais deux autres agents le classent en promesse à valider | oui / non — en une phrase |
| **Domaine principal** : bascule-t-on `rushiti.fr` et le microsite Localo en 301 vers `rushiti-renovation.fr` ? (audit du 13/08, P0-A) | oui / non — puis fournir le sitemap de `rushiti.fr` |
| **Carrelage** : prestation offerte ou non ? La mention « Carrelage & Sol » figure sur l'accueil héritée sans page ni arbitrage | offerte / non offerte — si non, retirer la mention |
| **`/sol-pvc-besancon` vs `/lino-vinyle-lvt-besancon`** : doublon signalé | → `rushiti-cannibal-check` pour verdict, puis fusion ou différenciation |

## 7. Routage

| Besoin | Agent |
|---|---|
| Lancer une campagne, arbitrer un plan, savoir quoi faire cette semaine | `rushiti-seo-engine` |
| Ouvrir la porte IA (dans l'ordre) | `rushiti-visibilite-ia` → `rushiti-part-de-voix-ia` → `rushiti-citation-ia` |
| Maillage vers `/platrerie-besancon` et `/ratissage-enduit-besancon` | `rushiti-maillage-interne` |
| Renforcer `/degat-des-eaux-besancon` (fenêtre octobre) | `rushiti-brief-seo` → `rushiti-architecte-seo` |
| Fiche Google et cohérence NAP | `rushiti-fiche-google-business` + `rushiti-seo-local` |
| Porte de création d'une page | `rushiti-keyword-map` (mode PORTA) |
