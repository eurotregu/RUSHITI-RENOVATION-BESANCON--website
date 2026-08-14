# LE PROMPT — Création du skill « rushiti-copywriting »

> Un seul prompt, prêt à coller dans Claude (ou tout outil IA équivalent).
> Objectif : créer UN skill de copywriting adapté à rushiti-renovation.fr,
> avec boucle d'excellence intégrée (brouillon → audit → version finale)
> et identification systématique des points d'amélioration.

---

## PROMPT (copier tout le bloc ci-dessous)

```markdown
# MISSION

Crée un skill nommé `rushiti-copywriting` : le rédacteur officiel de
RUSHITI Rénovation pour tout texte du site rushiti-renovation.fr
(pages services, pages locales, accueil, à-propos, sections de
conversion). Le skill doit produire des textes qui sonnent comme un
artisan de 20 ans de métier — jamais comme une agence, jamais comme
une IA — et doit intégrer une boucle d'auto-amélioration obligatoire
avant chaque livraison.

Livre le skill au format SKILL.md (frontmatter `name` + `description`
avec déclencheurs en français ET en albanais, comme les autres skills
RUSHITI), suivi du corps complet.

# SOURCE DE VÉRITÉ (faits entreprise — seuls faits utilisables)

- SARL RUSHITI Rénovation — SIRET 905 214 631 00012
- Dirigeants : Isuf et Yll Rushiti
- Adresse : 18 rue du Professeur Haag, 25000 Besançon
- Téléphone : 07 60 27 98 97 — Email : contact@rushiti-renovation.fr
- Expérience : 20 ans sur le bâti bisontin et franc-comtois
- Assurances : décennale + RC pro (ERGO France)
- Conformité : DTU 59.1 (peinture), DTU 25.41 (plaques de plâtre)
- Offre d'entrée : diagnostic technique gratuit sur place, devis
  détaillé sans engagement, interlocuteur unique du diagnostic à la
  réception de chantier
- Cibles : particuliers propriétaires et locataires, syndics de
  copropriété, gestionnaires de biens, bailleurs, experts d'assurance
  (dégât des eaux)
- Zone : Besançon tous quartiers (Boucle, Battant, Planoise, Palente,
  Montrapon, secteur Vauban…) + communes du Doubs (25)
- Services : peinture intérieure et extérieure, papier peint, toile de
  verre, ratissage/enduit, plâtrerie et placo (cloisons, doublage,
  faux plafonds), revêtements de sol (parquet flottant, vitrification,
  PVC, lino/LVT, ragréage), remise en état après dégât des eaux,
  isolation intérieure
- Second domaine : rushiti.fr — ne JAMAIS créer de lien croisé entre
  les deux sites
- Mention « RGE » présente dans le pied de page du site : statut
  [À CONFIRMER] auprès d'Isuf — interdiction de l'utiliser dans un
  texte tant qu'il n'est pas confirmé
- Note Google, nombre d'avis, témoignages : [À CONFIRMER] — jamais de
  chiffre de mémoire

Tout fait absent de cette liste (prix, délai, chantier, témoignage,
certification, chiffre) est INTERDIT : le skill écrit `[À CONFIRMER]`
et pose la question à Isuf au lieu d'inventer.

# VOIX DE MARQUE (à graver dans le skill)

| Attribut | Application concrète |
|---|---|
| Artisanal, pas corporate | Parle comme un artisan qui explique son métier à la cuisine, avec un café. Jamais de jargon managérial. |
| Le support avant la finition | On ne dit pas « on repeint » : on nomme le support (plâtre ancien, placo, fonds farinés), le geste (ratissage, impression, deux couches) et la norme (DTU) quand c'est pertinent. |
| La cause avant la solution | On explique POURQUOI ça cloque, pourquoi ça jaunit, pourquoi le mur nord condense — puis ce qu'on fait. C'est ça qui prouve les 20 ans de métier. |
| Ancré à Besançon | Bâti franc-comtois, plâtre traditionnel, pierre calcaire, hauteurs sous plafond de la Boucle, collectifs années 60-70 de Planoise et Palente, climat humide du Doubs. Un texte réutilisable par un peintre de Lyon est un texte raté. |
| Vouvoiement, toujours | « Vous » pour tous les publics. Ton direct, phrases courtes, lisible sur mobile (paragraphes de 2-3 lignes). |

## Lexique

INTERDITS (et leurs équivalents) : « solutions clés en main »,
« accompagnement personnalisé », « de A à Z », « excellence »,
« premium », « artisan passionné », « votre satisfaction est notre
priorité », « n'hésitez pas à nous contacter », tout superlatif sans
preuve (« les meilleurs peintres de Besançon »).

À PRIVILÉGIER : diagnostic gratuit sur place, préparation du support,
devis détaillé sans engagement, délai tenu, interlocuteur unique,
chantier propre, réception de chantier, murs froids, condensation,
dégât des eaux, remise en état, DTU en vigueur.

# STRUCTURES QUE LE SKILL DOIT SAVOIR PRODUIRE

1. **Page service** : le problème vécu (contextualisé quartier/bâti) →
   la cause technique → notre méthode en 4 étapes (diagnostic gratuit,
   préparation du support, mise en œuvre conforme DTU, finition et
   chantier propre) → pour qui / dans quel cas → preuve (uniquement
   faits confirmés) → appel à l'action concret.
2. **Page locale** (service × commune ou quartier) : même trame, mais
   le contexte bâti local porte le texte — jamais une page service
   avec le nom de la ville substitué.
3. **Section de conversion** (héros, bandeau, CTA) : bénéfice concret
   + réassurance vérifiable + action précise. CTA type : « Décrivez
   votre chantier au 07 60 27 98 97. On passe voir sur place, vous
   repartez avec un devis détaillé, sans engagement. » Jamais
   « envoyer » ni « en savoir plus ».
4. **Réécriture** d'un texte existant trop générique (mode
   avant → après).

Chaque texte : un seul objectif de conversion, au moins un détail
technique qui prouve l'expertise, aucune promesse invérifiable,
adapté au public (particulier = pédagogie et réassurance ; syndic,
gestionnaire ou assurance = process, conformité, traçabilité,
délais tenus).

# BOUCLE D'EXCELLENCE (obligatoire, cœur du skill)

Le skill ne livre JAMAIS un premier jet. À chaque demande :

**Temps 1 — Brouillon** rédigé selon les règles ci-dessus.

**Temps 2 — Audit interne** sur 6 critères notés /5, en tableau :
| Critère | /5 | Point faible identifié | Correction appliquée |
|---|---|---|---|
| Spécificité locale (Besançon/Doubs, bâti) | | | |
| Concrétude technique (support, geste, norme) | | | |
| Zéro jargon corporate / zéro tic d'IA | | | |
| Conformité aux faits (rien d'inventé, [À CONFIRMER] posés) | | | |
| Force de l'appel à l'action | | | |
| Différenciation RUSHITI (impossible à réutiliser ailleurs) | | | |

**Temps 3 — Version finale** intégrant chaque correction. Tout
critère sous 4/5 impose une réécriture du passage concerné avant
livraison. Seule la version finale est livrée, avec le tableau
d'audit en annexe.

**Temps 4 — Points d'amélioration** : chaque livraison se termine par
« 3 pistes pour aller plus loin » (fait à confirmer auprès d'Isuf,
preuve à collecter — photo de chantier, avis client —, page liée à
créer ou à mailler). C'est le mécanisme d'amélioration continue : ces
pistes nourrissent la demande suivante.

# GARDE-FOUS (non négociables, à recopier dans le skill)

1. Aucun prix, délai, chiffre, témoignage, certification ou chantier
   inventé — `[À CONFIRMER]` + question à Isuf.
2. Aucune promesse de résultat ni de classement Google.
3. RGPD : jamais de nom, d'adresse ou de photo de client sans accord.
4. Lecture seule : le skill propose, rien n'est publié sans
   validation d'Isuf.
5. Jamais de lien entre rushiti-renovation.fr et rushiti.fr.
6. Périmètre : textes du site uniquement. Le skill route vers les
   skills existants au lieu de les doublonner : structure de titres →
   rushiti-h1-h6 ; title/meta → seo-title-meta ; page locale complète
   → rushiti-page-locale ; texte qui « sonne IA » → rushiti-humanisateur ;
   posts sociaux → rushiti-reseaux-sociaux ; emails et courriers →
   rushiti-courriers-clients ; études de cas → rushiti-etudes-de-cas ;
   pages de prix → rushiti-pages-donnees.

# EXEMPLE DE TRANSFORMATION (à inclure dans le skill)

AVANT (interdit) : « RUSHITI Rénovation vous accompagne dans tous vos
projets de rénovation intérieure à Besançon. Nous mettons notre
expertise et notre savoir-faire au service de votre satisfaction. »

APRÈS (validé) : « Un mur qui s'écaille dans un appartement de la
Boucle, un plafond qui jaunit à Planoise ? On vient voir l'état réel
du support avant de dire quoi que ce soit. Sur du plâtre ancien
franc-comtois, la préparation fait l'essentiel du résultat : on
traite les fonds, on rebouche, on ratisse, puis on peint — et le mur
tient des années. »

# LIVRAISON ET AUTO-CRITIQUE DU SKILL

Après avoir rédigé le skill complet :
1. Applique-lui sa propre boucle d'excellence : audite le skill sur
   les 6 critères et corrige ce qui est sous 4/5.
2. Termine par « Points d'amélioration du skill lui-même » : la liste
   des `[À CONFIRMER]` à trancher avec Isuf (RGE ? note Google ?
   témoignages utilisables ?) et 3 évolutions possibles (banque
   d'exemples avant/après par service, variantes A/B de CTA à tester,
   enrichissement du contexte bâti par quartier).
3. Ne livre rien d'autre que : le SKILL.md final + le tableau d'audit
   + les points d'amélioration.
```

---

## Pourquoi ce prompt est construit ainsi

| Choix | Raison |
|---|---|
| Faits vérifiés dans le dépôt (Besançon, Doubs, peinture/plâtrerie) | Les versions précédentes inventaient Île-de-France, cuisines, MaPrimeRénov' — hors sujet pour ce métier. |
| RGE marqué `[À CONFIRMER]` | Mentionné dans le footer du site mais absent de la source de vérité des autres skills : le prompt en fait un point à trancher, pas un fait. |
| Boucle brouillon → audit → final → pistes | C'est le mécanisme « Refining to Excellence » + « Identifying Points for Improvement » demandé, rendu obligatoire et outillé (tableau, seuil 4/5). |
| Routage vers les skills existants | L'écosystème RUSHITI compte déjà h1-h6, seo-title-meta, page-locale, humanisateur… Le skill copywriting doit s'y emboîter, pas les doublonner. |
| Auto-critique finale du skill | Le prompt s'applique à lui-même la discipline qu'il impose : le skill est livré déjà audité, avec ses questions ouvertes listées. |
