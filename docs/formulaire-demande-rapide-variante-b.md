# Formulaire « Demande rapide » — variante B

Bloc à coller sur les pages service. Deux contextes, deux versions du même
formulaire :

| Où | Envoi | Où trouver le code |
|---|---|---|
| **rushiti-renovation.fr** (dépôt `eurotregu/rushiti-renovation`, Cloudflare Pages) | **Web3Forms** : la demande arrive par e-mail sans dépendre de la messagerie du visiteur, puis redirection vers `/merci` | copier le bloc d'une page existante, par ex. `papier-peint-besancon.html` |
| **Ce dépôt** (copie GitHub Pages, `noindex`) | messagerie pré-remplie (`mailto`) — suffisant pour une copie non indexée | `index.html` + `js/main.js`, ou le bloc autonome ci-dessous |

> **Attention à ne pas se tromper de mécanique.** Les pages en production ne
> passent pas par `mailto` : elles postent vers Web3Forms avec une clé, un
> objet propre à chaque page et une redirection vers `/merci`. Coller le bloc
> `mailto` ci-dessous sur une page de production reviendrait à **dégrader** le
> formulaire existant.

## Mise à niveau préparée pour la production (PR `eurotregu/rushiti-renovation` #10)

Sur les 27 pages à formulaire de rushiti-renovation.fr, en attente de fusion —
un déploiement de prévisualisation Cloudflare Pages permet de la voir avant :

- **Styles créés de zéro** : les formulaires Web3Forms n'avaient aucune règle
  CSS — labels collés à des champs bruts, projet en police à chasse fixe. La
  grille, les champs, les labels, le focus, la case à cocher et le bandeau de
  réassurance sont désormais dans `assets/css/s971fb819.css`.
- Case de consentement RGPD obligatoire (`consentement=oui` part dans l'e-mail).
- E-mail et code postal / commune obligatoires.
- `inputmode="tel"` : clavier numérique sur mobile.
- Bandeau de réassurance sous le bouton.
- `merci.html` : l'événement Meta `Lead` se déclenche à l'arrivée sur la page
  de remerciement — auparavant, une demande réellement envoyée n'était comptée
  nulle part.

## Version `mailto` autonome (copie GitHub Pages, maquettes, tests)

Le reste de ce document décrit la version indépendante de tout service tiers.

## Ce que la variante B contient

- 6 champs : nom et prénom, téléphone, e-mail, code postal / commune, service souhaité, description du projet.
- Case de consentement RGPD obligatoire.
- Champ piège anti-spam invisible (`entreprise_hp`) : si un robot le remplit, l'envoi est ignoré sans message d'erreur.
- Attributs `autocomplete`, `inputmode` et `type` corrects — le clavier numérique s'ouvre sur téléphone, les champs se remplissent tout seuls.
- Bandeau de réassurance sous le bouton et retour d'état annoncé aux lecteurs d'écran (`aria-live`).
- Envoi par messagerie pré-remplie vers `contact@rushiti-renovation.fr`.

## 1. À coller avant `</head>`

```html
<style>
.dr{background:#fff;border:1px solid #e8e8e8;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,.08);padding:28px;max-width:620px;width:100%;margin:0 auto}
.dr h2{font-size:22px;margin-bottom:8px}
.dr .dr-intro{font-size:15px;color:#666;margin-bottom:20px}
.dr .dr-intro a{font-weight:600;white-space:nowrap;color:#1a5632}
.dr-row{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.dr-field{margin-bottom:16px;display:flex;flex-direction:column}
.dr-field label{font-weight:600;font-size:14px;color:#1a1a2e;margin-bottom:6px}
.dr-field input,.dr-field select,.dr-field textarea{font:inherit;font-size:15px;color:#333;padding:12px 14px;border:1px solid #e8e8e8;border-radius:8px;background:#fff;width:100%;transition:border-color .3s,box-shadow .3s}
.dr-field textarea{resize:vertical;min-height:110px}
.dr-field input:focus,.dr-field select:focus,.dr-field textarea:focus{outline:0;border-color:#2a7a4a;box-shadow:0 0 0 3px rgba(42,122,74,.15)}
.dr-btn{width:100%;font-weight:600;font-size:16px;color:#fff;background:#1a5632;border:0;border-radius:8px;padding:15px 24px;cursor:pointer;transition:background .3s,transform .3s}
.dr-btn:hover{background:#2a7a4a;transform:translateY(-1px)}
.dr-btn:disabled{background:#999;cursor:progress;transform:none}
.dr-consent{display:flex;gap:10px;align-items:flex-start;font-size:13.5px;color:#666;line-height:1.6;margin-bottom:16px;cursor:pointer}
.dr-consent input{width:18px;height:18px;flex:0 0 auto;margin-top:3px;accent-color:#1a5632}
.dr-status{margin-top:12px;font-size:14px;color:#1a5632;text-align:center;min-height:1.2em}
.dr-note{font-size:13px;color:#999;margin-top:12px;text-align:center}
.dr-hp{position:absolute;left:-9999px;width:1px;height:1px;opacity:0}
.dr-reassure{display:flex;flex-wrap:wrap;gap:14px;margin-top:18px;padding-top:16px;border-top:1px solid #e8e8e8}
.dr-reassure span{display:flex;align-items:center;gap:6px;font-size:13px;color:#666}
.dr-reassure svg{flex:0 0 auto;color:#2a7a4a}
@media(max-width:640px){.dr-row{grid-template-columns:1fr}.dr{padding:22px}}
</style>
```

## 2. À coller à l'endroit du formulaire

Adaptez trois choses par page : le `data-subject` (objet de l'e-mail que vous recevrez),
le titre, et le service présélectionné dans la liste.

```html
<form class="dr" data-dr data-subject="Demande rapide — projet papier peint">
  <h2>Demande rapide : décrivez votre projet papier peint</h2>
  <p class="dr-intro">Laissez-nous l'essentiel en une minute : nous vous rappelons pour convenir du diagnostic gratuit sur place, puis vous recevez un devis précis. Vous pouvez aussi nous appeler directement au <a href="tel:+33760279897">07 60 27 98 97</a>.</p>

  <div class="dr-row">
    <div class="dr-field">
      <label for="dr-nom">Nom et prénom</label>
      <input type="text" id="dr-nom" name="nom" required autocomplete="name" placeholder="Votre nom">
    </div>
    <div class="dr-field">
      <label for="dr-tel">Téléphone</label>
      <input type="tel" id="dr-tel" name="telephone" required autocomplete="tel" inputmode="tel" placeholder="06 00 00 00 00">
    </div>
  </div>

  <div class="dr-row">
    <div class="dr-field">
      <label for="dr-email">E-mail</label>
      <input type="email" id="dr-email" name="email" required autocomplete="email" placeholder="vous@exemple.fr">
    </div>
    <div class="dr-field">
      <label for="dr-lieu">Code postal / commune</label>
      <input type="text" id="dr-lieu" name="lieu" required autocomplete="postal-code" placeholder="25000 Besançon">
    </div>
  </div>

  <div class="dr-field">
    <label for="dr-service">Service souhaité</label>
    <select id="dr-service" name="service">
      <option>Papier peint / toile de verre</option>
      <option>Peinture intérieure</option>
      <option>Peinture extérieure / façade</option>
      <option>Plâtrerie &amp; placo</option>
      <option>Isolation</option>
      <option>Revêtements de sol</option>
      <option>Dégât des eaux</option>
      <option>Rénovation complète</option>
      <option>Autre</option>
    </select>
  </div>

  <div class="dr-field">
    <label for="dr-projet">Votre projet</label>
    <textarea id="dr-projet" name="projet" rows="4" placeholder="Pièces concernées, surfaces approximatives, état actuel, délais souhaités…"></textarea>
  </div>

  <input type="text" name="entreprise_hp" class="dr-hp" tabindex="-1" autocomplete="off" aria-hidden="true">

  <label class="dr-consent">
    <input type="checkbox" required>
    <span>J'accepte que mes coordonnées soient utilisées pour me recontacter au sujet de cette demande. Elles ne sont ni revendues ni utilisées à d'autres fins.</span>
  </label>

  <button type="submit" class="dr-btn">Envoyer ma demande</button>
  <p class="dr-status" role="status" aria-live="polite"></p>

  <div class="dr-reassure">
    <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg> Diagnostic gratuit sur place</span>
    <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> Décennale &amp; RC pro</span>
    <span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> Devis détaillé, sans engagement</span>
  </div>
</form>
```

## 3. À coller avant `</body>`

Le script gère tous les formulaires `[data-dr]` de la page : le libellé de chaque champ
dans l'e-mail est repris de son `<label>`, donc renommer un champ suffit.

```html
<script>
(function () {
  document.querySelectorAll('[data-dr]').forEach(function (form) {
    var status = form.querySelector('.dr-status');

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var piege = form.querySelector('.dr-hp');
      if (piege && piege.value) { return; }

      var lignes = [];
      form.querySelectorAll('input[id], select[id], textarea[id]').forEach(function (champ) {
        if (champ.type === 'checkbox' || !champ.value.trim()) { return; }
        var label = form.querySelector('label[for="' + champ.id + '"]');
        lignes.push((label ? label.textContent.trim() : champ.name) + ' : ' + champ.value.trim());
      });

      var sujet = form.getAttribute('data-subject') || 'Demande de devis';
      var corps = lignes.join('\n') + '\n\nDemande envoyée depuis rushiti-renovation.fr';

      window.location.href = 'mailto:contact@rushiti-renovation.fr'
        + '?subject=' + encodeURIComponent(sujet)
        + '&body=' + encodeURIComponent(corps);

      /* Conversion Meta, si le pixel est chargé et le consentement cookies donné */
      if (typeof fbq === 'function') { fbq('track', 'Lead', { content_name: 'demande-rapide' }); }

      var btn = form.querySelector('button[type="submit"]');
      var texte = btn.textContent;
      btn.disabled = true;
      btn.textContent = 'Ouverture de votre messagerie…';
      if (status) { status.textContent = 'Votre messagerie s’ouvre avec la demande pré-remplie. Il ne reste qu’à l’envoyer.'; }
      setTimeout(function () { btn.disabled = false; btn.textContent = texte; }, 3000);
    });
  });
})();
</script>
```

## Points restés ouverts

1. **Texte du consentement et mentions légales.** Le texte de la case est un
   point de départ : la page mentions légales doit indiquer qui traite les
   données, pour quelle finalité, combien de temps elles sont conservées et
   comment les faire supprimer. À valider par Isuf.
2. **E-mail obligatoire.** La variante B rend l'e-mail obligatoire alors qu'il
   était facultatif : un devis écrit se transmet par e-mail, mais cela peut
   coûter quelques demandes de visiteurs qui ne laissaient qu'un numéro.
   Retirer le `required` du champ `name="email"` suffit à revenir en arrière.
3. **Suivi des conversions.** L'événement `Lead` ne part qu'après acceptation
   des cookies (pixel Meta chargé). À vérifier dans Events Manager après le
   déploiement en production.
