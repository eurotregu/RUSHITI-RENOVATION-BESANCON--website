#!/usr/bin/env python3
"""Paketa 11 — corrections P1 de l'audit du 03/09/2026 (constats 4, 8, 10, 12).

Usage, sur un checkout du dépôt de production eurotregu/rushiti-renovation :
    python3 fix_p1.py /chemin/vers/rushiti-renovation           # simulation
    python3 fix_p1.py /chemin/vers/rushiti-renovation --apply   # application

Idempotent. Quatre corrections :
  A. JSON-LD : `aggregateRating` retiré de index.html (avis tiers, doctrine du 22/08) ;
     `legalName: "Rushiti"` ajouté au nœud LocalBusiness de toutes les pages (et corrigé sur les
     150 pages où il portait le nom commercial « RUSHITI Rénovation »).
  B. hCaptcha à la demande : le script client Web3Forms (qui charge hCaptcha, ≈ 600 Ko)
     n'est plus appelé au chargement mais quand le formulaire approche du viewport
     (600 px) ou reçoit le focus. 31 pages.
  C. Page À propos réécrite (contenu, FAQ visible + FAQPage, Person Isuf et Yll,
     dimensions des images).
  D. Page Contact : délai de rappel validé, étapes après la demande, lien Google Maps,
     bouton WhatsApp.
"""
import glob, json, os, re, sys

# ---------------------------------------------------------------- A. JSON-LD
AGG_RE = re.compile(r',"aggregateRating":\{[^{}]*\}')
LB_RE = re.compile(r'"@type":\s*\[\s*"LocalBusiness"\s*,\s*"HousePainter"\s*,\s*"HomeAndConstructionBusiness"\s*\]')
NAME_RE = re.compile(r'"name":(\s*)"RUSHITI Rénovation"')


LEGAL_BAD_RE = re.compile(r'"legalName":(\s*)"RUSHITI Rénovation"')


def add_legal_name(h):
    """Insère "legalName":"Rushiti" après le "name" du nœud LocalBusiness (formats compact et espacé) ;
    corrige les 150 pages où legalName portait le nom commercial."""
    h, n = LEGAL_BAD_RE.subn(lambda m: '"legalName":' + m.group(1) + '"Rushiti"', h)
    pos = 0
    while True:
        m = LB_RE.search(h, pos)
        if not m:
            break
        end = h.find("</script>", m.end())
        if end < 0:
            end = len(h)
        if '"legalName"' in h[m.start():end]:
            pos = m.end(); continue
        nm = NAME_RE.search(h, m.end(), end)
        if not nm:
            pos = m.end(); continue
        sp = nm.group(1)  # " " dans le format espacé, "" dans le format compact
        ins = ',' + (' ' if sp else '') + '"legalName":' + sp + '"Rushiti"'
        h = h[:nm.end()] + ins + h[nm.end():]
        n += 1
        pos = nm.end() + len(ins)
    return h, n


# ---------------------------------------------------------------- B. hCaptcha
W3F_OLD = '<script src="https://web3forms.com/client/script.js" async defer></script>'
W3F_NEW = ('<script>/*w3f-lazy*/(function(){var done=false;function charger(){if(done)return;done=true;'
           'var s=document.createElement("script");s.src="https://web3forms.com/client/script.js";'
           's.async=true;s.defer=true;document.body.appendChild(s);}'
           'function armer(){var f=document.querySelector(\'form[action*="api.web3forms.com"]\');'
           'if(!f){return;}f.addEventListener("focusin",charger,{once:true});'
           'f.addEventListener("pointerdown",charger,{once:true});'
           'if("IntersectionObserver" in window){var io=new IntersectionObserver(function(es){'
           'for(var k=0;k<es.length;k++){if(es[k].isIntersecting){charger();io.disconnect();return;}}},'
           '{rootMargin:"600px 0px"});io.observe(f);}else{charger();}}'
           'if(document.readyState==="loading"){document.addEventListener("DOMContentLoaded",armer);}else{armer();}})();</script>')

# ---------------------------------------------------------------- C. À propos
HERE = os.path.dirname(os.path.abspath(__file__))


def read(name):
    return open(os.path.join(HERE, name), encoding="utf-8").read()


def fix_apropos(h):
    main_new = read("a-propos-main.html").strip()
    ld_new = read("a-propos-jsonld.json").strip()
    n = 0
    if 'id="isuf"' not in h:
        h = re.sub(r"<main>.*?</main>", lambda m: main_new, h, count=1, flags=re.S); n += 1
    ld_re = re.compile(r'<script type="application/ld\+json">.*?</script>', re.S)
    if '"@id":"https://rushiti-renovation.fr/a-propos#isuf"' not in h:
        h = ld_re.sub('<script type="application/ld+json">' + ld_new + "</script>", h, count=1); n += 1
    return h, n


# ---------------------------------------------------------------- D. Contact
CONTACT_REPL = [
    ('<p class="u12">Renseignez le formulaire : nous revenons vers vous rapidement.</p>',
     '<p class="u12">Renseignez le formulaire : nous vous rappelons sous 24 à 48 h ouvrées pour convenir du diagnostic gratuit sur place.</p>'),
    ('<div><b>Adresse</b>18 rue du Professeur Haag<br>25000 Besançon</div>',
     '<div><b>Adresse</b>18 rue du Professeur Haag<br>25000 Besançon<br><a href="https://www.google.com/maps?cid=10915820577691168567" target="_blank" rel="noopener">Voir sur Google Maps</a></div>'),
    ('<div class="info-card u35">\n<h3>Diagnostic gratuit</h3>\n<p class="u14">Avant tout devis, nous nous déplaçons gratuitement pour examiner votre chantier et vous conseiller.</p>\n<a class="btn" href="tel:+33760279897">Appeler maintenant</a>\n</div>',
     '<div class="info-card u35">\n<h3>Ce qui se passe après votre demande</h3>\n'
     '<ol class="u13" style="padding-left:20px;margin:0 0 12px">'
     '<li><b>Nous vous rappelons</b> sous 24 à 48 h ouvrées pour préciser votre besoin.</li>'
     '<li><b>Diagnostic gratuit sur place</b> : état réel des supports, origine du problème, ce qui doit être fait et ce qui peut attendre.</li>'
     '<li><b>Devis détaillé</b>, poste par poste, sans engagement.</li></ol>\n'
     '<p class="u14">Une urgence, un dégât des eaux en cours ? Appelez-nous directement, ou envoyez vos photos sur WhatsApp pour un premier avis.</p>\n'
     '<a class="btn" href="tel:+33760279897">Appeler maintenant</a>\n'
     '<a class="btn ghost" href="https://wa.me/33760279897?text=Bonjour%2C%20j%27ai%20des%20travaux%20%C3%A0%20pr%C3%A9voir.%20Puis-je%20vous%20envoyer%20des%20photos%20pour%20un%20premier%20avis%20%3F" target="_blank" rel="noopener noreferrer">Écrire sur WhatsApp</a>\n</div>'),
]


def fix_contact(h):
    n = 0
    for old, new in CONTACT_REPL:
        if old in h:
            h = h.replace(old, new); n += 1
    return h, n


# ---------------------------------------------------------------- main
def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    root = sys.argv[1]; apply = "--apply" in sys.argv
    pages = sorted(glob.glob(os.path.join(root, "*.html")) + glob.glob(os.path.join(root, "blog", "*.html")))
    st = {"agg": 0, "legal": 0, "w3f": 0, "apropos": 0, "contact": 0}
    touched = 0
    for p in pages:
        name = os.path.basename(p)
        h = open(p, encoding="utf-8").read(); h0 = h
        if name == "index.html":
            h, k = AGG_RE.subn("", h); st["agg"] += k
        h, k = add_legal_name(h); st["legal"] += k
        if W3F_OLD in h:
            h = h.replace(W3F_OLD, W3F_NEW); st["w3f"] += 1
        if name == "a-propos.html":
            h, k = fix_apropos(h); st["apropos"] += k
        if name == "contact.html":
            h, k = fix_contact(h); st["contact"] += k
        if h != h0:
            touched += 1
            if apply:
                open(p, "w", encoding="utf-8").write(h)
    print(("APPLIQUÉ" if apply else "SIMULATION") + f" — {touched} fichier(s) à modifier")
    print(f"  A. aggregateRating retiré : {st['agg']} ; legalName ajouté : {st['legal']} nœud(s)")
    print(f"  B. script Web3Forms/hCaptcha différé : {st['w3f']} page(s) (attendu 31)")
    print(f"  C. À propos : {st['apropos']} bloc(s) remplacé(s) (attendu 2)")
    print(f"  D. Contact : {st['contact']} remplacement(s) (attendu 3)")


if __name__ == "__main__":
    main()
