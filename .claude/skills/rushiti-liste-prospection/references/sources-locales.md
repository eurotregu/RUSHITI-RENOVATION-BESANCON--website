# Sources de sourçage — où trouver chaque famille en France

> Ordre par défaut : **registre ou annuaire public français de la famille → outil de prospection connecté → recherche web ciblée pour les trous.** Les petites structures locales (un syndic de quartier, un cabinet d'architecte de trois personnes) échappent souvent aux bases internationales : le registre français est la source de vérité, l'outil connecté sert à compléter et à enrichir.
> Le même outil interrogé avec d'autres filtres ne compte pas comme une deuxième source.

## Par famille

| Famille | Sources primaires (publiques, gratuites) | Compléments |
|---|---|---|
| Syndics de copropriété | Registre national des copropriétés (data.gouv.fr — chaque copropriété immatriculée nomme son syndic), annuaires FNAIM / UNIS, Pages Jaunes « syndic de copropriété » + ville | Sites des cabinets (portefeuille, équipe), presse locale (AG, programmes) |
| Gestionnaires de biens | Pages Jaunes « gestion locative » / « administrateur de biens », annuaires FNAIM / UNIS, portails d'annonces (agences publiant des locations sur la zone) | Annonces « travaux à prévoir » = signal en plus de la structure |
| Experts / réseaux d'assurance | Annuaires des cabinets d'expertise construction, réseaux déjà approchés (voir fichier de contexte du skill prospection) | LinkedIn des cabinets, plateformes de gestion de sinistres |
| Architectes / maîtres d'œuvre | Annuaire de l'Ordre des architectes (architectes.org — filtre par département), Pages Jaunes « maître d'œuvre » | Permis de construire publiés (rénovations en cours), sites des agences |
| Bailleurs / logement social | Liste des bailleurs sociaux du département (USH / fédérations régionales), sites des OPH et ESH du Doubs | Avis d'appels d'offres (BOAMP, marchés publics) = signal fort |
| Santé, commerces, bureaux | Pages Jaunes par activité + zone, annuaire-entreprises.data.gouv.fr (SIRENE par code NAF et commune) | Presse locale (ouvertures, reprises), annonces immobilières commerciales |

Transverse, toutes familles : **annuaire-entreprises.data.gouv.fr / Pappers** (base SIRENE) donne SIREN, adresse exacte, code NAF, effectif déclaré — c'est la clé de dédoublonnage et la confirmation de zone la moins chère qui existe.

## Outil de prospection connecté (MCP « Vibe Prospecting » ou équivalent)

Quand la session dispose d'un outil de prospection connecté, règles d'usage :

1. **Autocomplete d'abord.** Toute valeur de filtre à choix fermé (catégorie d'activité, intitulé de poste, ville) se valide par l'outil d'autocomplete et se recopie **telle quelle** dans la recherche. Une valeur devinée produit zéro résultat en silence.
2. **Jauge avant extraction.** Premier appel avec un petit nombre de résultats demandés ; le volume réel est le champ `records_matching_filters` de la réponse — pas le nombre de lignes retournées, qui n'est que l'échantillon.
3. **Entreprises d'abord** (`entity_type: businesses`, pays `FR`, filtre de zone le plus fin disponible), personnes ensuite, restreintes aux structures retenues.
4. **Aperçus gratuits, exports payants.** Les recherches et aperçus ne coûtent rien ; l'enrichissement de contacts et l'export CSV consomment des crédits. Afficher l'estimation de coût fournie par l'outil et attendre l'accord explicite d'Isuf ou Yll avant tout export — même si le solde le permet.
5. **Couverture locale à vérifier.** Si la jauge outil retourne beaucoup moins que l'annuaire français (fréquent sur les TPE locales), la source primaire redevient le registre ; l'outil ne sert alors qu'aux structures qu'il connaît.

Sans outil connecté : tout se fait par registres + recherche web ; la colonne contacts se limite à ce qui est publié publiquement (site de la structure, annuaire professionnel), et c'est un résultat valide.

## Règles RGPD du sourçage (prospection B2B française)

- Coordonnées **professionnelles** uniquement, en **lien avec la fonction** de la personne (on écrit au gestionnaire de copropriété à propos de copropriétés).
- **Source licite et notée** pour chaque donnée : site de la structure, registre public, annuaire professionnel. Jamais d'adresse ou de téléphone personnels, jamais de source douteuse (fichier acheté non vérifiable, scraping de profils privés).
- La personne doit pouvoir comprendre **comment on a eu ses coordonnées** — la colonne `Source` de la liste sert aussi à ça, et le premier email en aval mentionne la source de l'accroche.
- **Liste d'opposition** croisée avant livraison ; toute demande de ne plus être contacté s'y ajoute immédiatement.
- Email générique de la structure (contact@, agence@) : repli acceptable pour un envoi individuel et relu — le marquer `générique` dans la liste.
