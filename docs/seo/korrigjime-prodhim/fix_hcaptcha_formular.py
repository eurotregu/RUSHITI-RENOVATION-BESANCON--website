#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shton verifikimin anti-robot hCaptcha në formularët Web3Forms të depos së
prodhimit (eurotregu/rushiti-renovation) — përgjigje ndaj sulmit të 02/09/2026.

Konteksti: më 02/09/2026 (21h23–21h24) formulari « Demande rapide » i faqes
/peinture-interieure-besancon mori 17 dërgesa automatike (skanim SQL injection:
fushat bosh, kodi i sulmit në fushën « consentement »). Honeypot-i `botcheck`
nuk e kap: roboti nuk e shënon kutinë e fshehur. hCaptcha e Web3Forms (pa çelës
të vetin, pa regjistrim) e bllokon në burim.

Çfarë bën, për secilën nga 31 faqet me POST nativ Web3Forms (30 pilier + /contact):

1. widget-i:  <div class="h-captcha" data-captcha="true" data-lang="fr">
   menjëherë para butonit « Envoyer ma demande »;
2. skripti Web3Forms (async defer) para </body> — ai ngarkon dhe shfaq hCaptcha-n;
3. skript i vogël inline: nëse kutia hCaptcha nuk është shënuar, dërgimi
   ndalet dhe shfaqet një mesazh në frëngjisht (Web3Forms e refuzon gjithsesi
   në server pasi hCaptcha të aktivizohet në panel — mesazhi shmang një faqe
   gabimi të pakuptueshme për klientin).

⚠️ Hapi manual i domosdoshëm, JASHTË këtij skripti: në panelin Web3Forms
(app.web3forms.com → formulari me çelësin 1aee0248-…) aktivizoni « hCaptcha »
si mbrojtje. Pa këtë, widget-i shfaqet por dërgesat pa hCaptcha kalojnë ende.
Aktivizimi vlen për TË GJITHË çelësin, pra edhe për /simulateur-peinture, i cili
poston me fetch (JSON) pa widget: aty dërgesa bie te mailto (fallback ekzistues)
derisa të trajtohet veçmas — shih docs/formulaire-demande-rapide-variante-b.md.

Idempotent: faqet që kanë tashmë class="h-captcha" kapërcehen.

Përdorimi (mbi një checkout të depos së prodhimit):
    python3 fix_hcaptcha_formular.py /rruga/drejt/rushiti-renovation           # simulim
    python3 fix_hcaptcha_formular.py /rruga/drejt/rushiti-renovation --apply   # zbatim
Pas zbatimit: python3 verifiko_demande_rapide.py /rruga/drejt/rushiti-renovation
"""
import re
import sys
from pathlib import Path

from verifiko_demande_rapide import PAGES as PAGES_PILIER

PAGES = sorted(PAGES_PILIER) + ["contact.html"]

# Paragrafi i butonit: <p class="u35"> në 29 faqe + /contact, <p> i thjeshtë në
# peinture-facade-isolation-exterieure (gabarit pak më i vjetër).
ANKORA_BUTONI = re.compile(
    r'<p(?: class="u35")?><button class="btn lg" type="submit">Envoyer ma demande</button></p>')
WIDGET = '<div class="h-captcha" data-captcha="true" data-lang="fr" style="margin-top:16px"></div>'
SKRIPTI_WEB3FORMS = '<script src="https://web3forms.com/client/script.js" async defer></script>'
# Kontroll në anën e klientit — vetëm formularët që postojnë te Web3Forms
# (selektori me *= që të mos dyfishojë vargun action="…" që numëron verifiko).
# Nëse widget-i nuk u ngarkua (skript i bllokuar), textarea nuk ekziston dhe
# POST-i niset normalisht: Web3Forms vendos në server.
SKRIPTI_KONTROLLIT = (
    '<script>/*hcaptcha*/(function(){'
    'var f=document.querySelectorAll(\'form[action*="api.web3forms.com"]\');'
    'for(var i=0;i<f.length;i++){f[i].addEventListener("submit",function(e){'
    'var t=this.querySelector(\'textarea[name="h-captcha-response"]\');'
    'if(!t||t.value){return;}e.preventDefault();'
    'var w=this.querySelector(".h-captcha"),m=this.querySelector(".captcha-msg");'
    'if(!m){m=document.createElement("p");m.className="captcha-msg";m.setAttribute("role","alert");'
    'm.style.cssText="margin:8px 0 0;font-size:.9rem;font-weight:600;color:#EB1C24";'
    'm.textContent="Merci de cocher la case \\u00ab Je suis humain \\u00bb avant d\\u2019envoyer votre demande.";'
    'if(w){w.insertAdjacentElement("afterend",m);}else{this.appendChild(m);}}'
    'if(w){w.scrollIntoView({behavior:"smooth",block:"center"});}'
    '});}})();</script>'
)


def korrigjo(h):
    """Kthen (html_i_ri, lista_e_problemeve). Problemet = ankora të munguara."""
    p = []
    butona = ANKORA_BUTONI.findall(h)
    if len(butona) != 1:
        p.append("butoni Envoyer: %d herë" % len(butona))
    if h.count("</body>") != 1:
        p.append("</body>: %d herë" % h.count("</body>"))
    if p:
        return h, p
    h = ANKORA_BUTONI.sub(lambda m: WIDGET + "\n" + m.group(0), h, count=1)
    h = h.replace("</body>", SKRIPTI_WEB3FORMS + SKRIPTI_KONTROLLIT + "</body>", 1)
    return h, p


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    root = Path(sys.argv[1])
    apply = "--apply" in sys.argv
    ndryshime, gabime = 0, 0

    for fname in PAGES:
        f = root / fname
        if not f.exists():
            print("MUNGON %s" % fname)
            gabime += 1
            continue
        h = f.read_text(encoding="utf-8")
        if 'class="h-captcha"' in h:
            print("KA TASHME %s" % fname)
            continue
        if 'action="https://api.web3forms.com/submit"' not in h:
            print("GABIM  %s: pa formular Web3Forms" % fname)
            gabime += 1
            continue
        h2, p = korrigjo(h)
        if p:
            print("GABIM  %s: %s" % (fname, "; ".join(p)))
            gabime += 1
            continue
        if apply:
            f.write_text(h2, encoding="utf-8")
        print("%s %s" % ("SHTUAR" if apply else "DO SHTOHEJ", fname))
        ndryshime += 1

    print("\n%d ndryshime%s, %d probleme."
          % (ndryshime, "" if apply else " (simulim)", gabime))
    sys.exit(1 if gabime else 0)


if __name__ == "__main__":
    main()
