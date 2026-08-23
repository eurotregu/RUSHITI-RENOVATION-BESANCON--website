# Le catalogue des défauts des plans SEO génériques

> À relire **avant** de rendre un triage (mode 3). Chaque entrée a été vue au
> moins une fois dans un plan réellement reçu par RUSHITI : plans de
> consultants, playbooks anglo-saxons, sorties d'IA non bridées.
>
> Ils ne sont pas malveillants. Ils sont écrits pour un éditeur de logiciel
> qui vend en ligne, puis appliqués à un artisan du bâtiment qui vend un
> chantier à Besançon. La plupart des défauts viennent de là.

---

## A. Inventions de chiffres

Un plan générique remplit tout trou de donnée par une valeur crédible. C'est
le défaut le plus coûteux : la valeur a l'air d'une mesure, elle survit aux
relectures, et elle finit sur une page publique.

| # | Ce que dit le plan | Pourquoi c'est faux ici | La version correcte |
|---|---|---|---|
| 1 | « peintre à Besançon ~720 recherches/mois » | Aucun outil n'a été interrogé. Le chiffre est décoratif et il **fausse la priorisation** — on travaille la mauvaise page en premier | Search Console, Keyword Planner ou NeuronWriter, avec la période. Sinon `PV` / `[À SOURCER]` |
| 2 | Un tableau de prix « 45-75 €/m² TTC » par niveau de sinistre | Aucun prix n'est validé par Isuf. Un tarif publié devient une référence opposable devant un client ou un expert | **Ce qui fait le prix** s'explique (surface, état du support, couches, finition, hauteur, accès) ; le prix ne s'affiche pas |
| 3 | « intervention sous 4 h », « devis sous 24 h » | Promesse **contractuelle**, pas argument marketing. Un délai affiché engage l'entreprise | Aucun délai non validé. Le diagnostic gratuit sur place se dit **sans délai annoncé** |
| 4 | « 80 % de citations IA à trois mois », « +30 % de trafic » | Promesse de classement, et invérifiable : les réponses IA varient d'une session à l'autre | Effet **fort / moyen / faible**, avec son motif |

---

## B. Erreurs d'entité

Les moteurs de réponse recoupent les sources entre elles. Une incohérence
d'entité ne reste pas sur la page : elle se propage dans les annuaires, puis
dans les réponses IA, et elle se corrige beaucoup plus lentement qu'elle ne
s'écrit.

| # | Ce que dit le plan | La version correcte |
|---|---|---|
| 5 | « SARL RUSHITI Rénovation » | **RUSHITI Rénovation** est le nom commercial ; **Rushiti** la dénomination sociale (SARL), réservée aux mentions légales et aux documents contractuels. Jamais les deux collés |
| 6 | « 20 ans d'expérience » fondu en « 20 ans d'existence » | **Deux faits distincts** : Isuf exerce depuis 20 ans, l'entreprise est née le 04/11/2021. Les fusionner est faux et vérifiable au RCS |
| 7 | Un téléphone à compléter du type « 03 81 XX XX XX » | Le numéro **existe** : 07 60 27 98 97 · `tel:+33760279897` · WhatsApp `wa.me/33760279897`. Un placeholder inventé qui ressemble à un fixe local est pire qu'un trou déclaré |
| 8 | « lat/long approximatives de Besançon : 47.2380, 6.0244 » | Une coordonnée **approximée** est une erreur d'entité que les moteurs propagent. On relève celles de la fiche Google réelle, ou on écrit `[À COMPLÉTER]` |
| 9 | Un `taxID` reconstruit « FR + clé + SIREN » | La TVA est **FR89905214631**, relevée. Une clé de contrôle recalculée à la volée peut être fausse — et le numéro apparaîtra dans des données structurées publiques |

**Le NAP au caractère près** : « 18 rue du Professeur Haag, 25000 Besançon »
— « rue » en minuscules, avec « du ». Le RCS et la Base Adresse Nationale
écrivent sans « du » : écart connu, on ne s'aligne pas dessus.

---

## C. Erreurs de périmètre

| # | Ce que dit le plan | La version correcte |
|---|---|---|
| 10 | Zone élargie à Vesoul, Belfort, Dole, Dijon, ou « rayon de 50 km » | La zone validée s'arrête au **Doubs (25)**. Écrire un rayon ne crée aucune pertinence locale : ça dilue celle qui existe |
| 11 | Une page pour un service non confirmé — carrelage, ravalement seul, enduit à la chaux, boiseries | **Refusé par Isuf le 21/08/2026** pour la chaux et les boiseries : la demande existe en Search Console et reste **sciemment non servie**. Carrelage : non tranché, donc aucune page |
| 12 | Un lien de `rushiti-renovation.fr` vers `rushiti.fr`, ou une mention de `rushiti-peinture.fr` | Un seul site par campagne, **jamais de lien croisé**. `rushiti-peinture.fr` est **éteint** : ne jamais l'écrire, et le faire retirer des agrégateurs qui le publient encore |

---

## D. Erreurs d'architecture

| # | Ce que dit le plan | Pourquoi c'est faux ici | La version correcte |
|---|---|---|---|
| 13 | Créer `/peinture`, `/placo`, `/isolation`, `/renovation-complete` | Ces pages **existent déjà** sous la forme `service-besancon` et récoltent des impressions. Une URL sans zone perd le signal local et divise le signal | Renforcer l'existante. Si Isuf tient aux URL courtes : **301 de la courte vers l'existante**, jamais une seconde page |
| 14 | « Un pilier + 6 à 15 pages par sujet » | La grille a été **réduite de 644 à 301 pages** précisément parce que le trop-plein se cannibalisait. Appliquer la recette défait un travail payé | Toute création passe par la porte `rushiti-keyword-map` |
| 15 | Ajouter un palier à la grille locale, ou une page par commune du département | Même motif. La grille est consolidée par paliers A/B/C | Ne jamais proposer de la regonfler |
| 16 | Une page livrée avec des trous (« [insérer le paragraphe sur…] ») | Ce n'est pas un livrable, c'est un plan déguisé | Contenu rédigé en entier, ou phase déclarée bloquée |

---

## E. Erreurs de balisage

| # | Ce que dit le plan | La version correcte |
|---|---|---|
| 17 | Un balisage `Review` ou `aggregateRating` sur les pages de service | **Interdit par Google** pour les avis qu'une entreprise collecte sur elle-même. Risque de pénalité manuelle. La preuve sociale va dans le **texte visible** |
| 18 | Une `FAQPage` construite sur des questions que la page n'affiche pas — ou une FAQ visible sans balisage | Le JSON-LD ne dit **rien que la page ne montre**. Les deux doivent correspondre exactement |

Les DTU aussi se vérifient : un plan générique cite volontiers « DTU 25.1 »
ou « DTU 60.1 » (plafonds suspendus, plomberie). Les normes réellement
applicables ici sont **DTU 59.1** (travaux de peinture), **DTU 25.41**
(plaques de plâtre), **DTU 53.2** (revêtements de sol PVC), plus la
convention **IRSI** pour les sinistres. Une norme fausse citée comme preuve
d'expertise décrédibilise devant un expert d'assurance — exactement le
lecteur qu'on visait.

Autre détail que les plans écrasent : les **quartiers canoniques** de
Besançon sont Battant, Centre / Chapelle des Buis, Chaprais-Cras, Bregille,
Velotte, Butte-Grette, Saint-Ferjeux-Rosemont, Montrapon-Montboucons,
Saint-Claude-Torcols, Palente-Orchamps-Saragosse, Vaîte-Clairs Soleils,
Planoise-Châteaufarine, Les Tilleroyes. « La Boucle » n'est pas un quartier
SEO : c'est une description géographique (« la boucle du Doubs », « le centre
ancien »), utilisable en texte, jamais comme signal géo.

---

## F. Erreurs de mesure

| # | Ce que dit le plan | La version correcte |
|---|---|---|
| 19 | Un tableau unique « mot-clé → position Google → statut IA » | Deux portes, **deux dénominateurs, deux cadences** (4-6 semaines vs 6-8). Un tableau unique fait lire un mouvement Google comme un mouvement IA. Côte à côte, datés séparément |
| 20 | Un moteur non interrogé compté comme « absent » | `NM`, toujours. Confondre « pas vu » et « pas cité » fabrique une fausse chute au relevé suivant |
| 21 | Conclure d'un seul relevé que « les IA nous ignorent » | Le premier relevé **est** la référence. C'est la tendance qui fait signal |
| 22 | Reformuler les requêtes du panel « pour voir » | La comparabilité meurt. Le panel de 14 requêtes est figé ; les essais libres vont dans une section exploratoire séparée |

---

## G. Tactiques à écarter

| # | Ce que propose le plan | Pourquoi on n'y va pas |
|---|---|---|
| 23 | Un mode « rapide » qui saute l'analyse et **suppose** les manques du marché | Une hypothèse présentée comme un constat est une invention avec une étiquette. Un mode rapide acceptable annonce ses hypothèses comme telles et n'écrit rien de chiffré |
| 24 | Publier son propre « Top 10 des artisans de Besançon » | Auto-classement : ni citable par un moteur qui privilégie les tiers, ni tenable devant des confrères voisins. Un comparatif de **solutions techniques**, oui ; d'entreprises, non |
| 25 | Créer une page Wikipédia | Les critères d'admissibilité excluent une SARL artisanale créée en 2021. Le temps est mieux placé sur huit fiches d'annuaire exactes |
| 26 | Publier un `llms.txt` et le compter comme action de citation | Convention émergente ; aucun des moteurs suivis ne l'utilise publiquement comme source. Coût nul, effet non démontré : à publier éventuellement, **jamais à compter comme action** |
| 27 | Acheter un placement présenté comme une citation gagnée | Se déclare (`rel="sponsored"`) et se compte comme publicité. On achète de la visibilité, jamais un signal de confiance |

---

## Ce que les plans génériques ont raison de dire

Un triage honnête ne rejette pas tout. Ce qui survit presque toujours :

- **L'anatomie de page** : H1 local, contenu long et structuré, FAQ, données
  structurées, CTA visible, maillage. C'est ce qui a été retenu du plan du
  22/08/2026 et formalisé en doctrine.
- **La réponse dans les deux premières phrases.** Vrai, et c'est le levier
  GEO le plus rentable.
- **Un fait par phrase, avec un chiffre, une date ou une norme.** Vrai — à
  condition que le chiffre existe.
- **Posséder le sujet plutôt que le mot-clé.** Vrai, et déjà appliqué.
- **Surveiller les deux portes.** Vrai, avec la correction de mesure ci-dessus.

La règle du triage : **on garde les principes, on jette les chiffres et les
URL.** Les principes d'un bon playbook sont transférables ; ses données ne le
sont jamais, parce qu'elles ont été écrites pour un autre site.
