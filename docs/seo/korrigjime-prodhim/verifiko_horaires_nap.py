#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Outil de régression NAP / horaires — dépôt de production.

À exécuter avant chaque déploiement. Contrôle que l'entreprise déclare
partout les mêmes horaires, en JSON-LD comme dans le texte visible :

  1. tous les blocs JSON-LD sont du JSON valide ;
  2. chaque nœud LocalBusiness complet (adresse ou téléphone) porte
     openingHoursSpecification ;
  3. il n'existe qu'UNE seule version des horaires sur tout le site — un
     second jeu signifie qu'une page a été régénérée avec un ancien gabarit ;
  4. les horaires déclarés sont ceux validés par Isuf le 24/08/2026 :
     Lun–Ven 07:00–20:30, Sam 08:00–20:30, Dim 09:00–17:30 ;
  5. aucune page n'affiche encore l'ancien texte « Lundi – Vendredi : 8h – 18h » ;
  6. le NAP reste cohérent : téléphone et adresse identiques partout.

Sortie : 0 = conforme, 1 = au moins une erreur.

Usage :  python3 verifiko_horaires_nap.py /chemin/vers/checkout
"""
import json
import pathlib
import re
import sys

ATTENDU = [
    (["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "07:00", "20:30"),
    ("Saturday", "08:00", "20:30"),
    ("Sunday", "09:00", "17:30"),
]
TEL = "+33760279897"
RUE = "18 rue du Professeur Haag"
ANCIEN_TEXTE = re.compile(r"Lundi\s*[–-]\s*Vendredi\s*:\s*8h\s*[–-]\s*18h")


def normalise(spec) -> list:
    out = []
    for o in spec or []:
        d = o.get("dayOfWeek")
        out.append((d if isinstance(d, str) else tuple(d), o.get("opens"), o.get("closes")))
    return out


def attendu_norm() -> list:
    return [(d if isinstance(d, str) else tuple(d), o, c) for d, o, c in ATTENDU]


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    racine = pathlib.Path(sys.argv[1])
    pages = sorted(racine.rglob("*.html"))
    if not pages:
        print("Aucune page HTML sous %s" % racine)
        return 2

    erreurs, alertes = [], []
    variantes, nb_biz, nb_bloc = {}, 0, 0

    for p in pages:
        t = p.read_text(encoding="utf-8", errors="ignore")

        for i, b in enumerate(re.findall(
                r'<script type="application/ld\+json">(.*?)</script>', t, re.S), 1):
            nb_bloc += 1
            try:
                d = json.loads(b)
            except json.JSONDecodeError as e:
                erreurs.append("%s : JSON-LD bloc %d invalide (%s)" % (p.name, i, e))
                continue
            for n in (d.get("@graph", [d]) if isinstance(d, dict) else d):
                if not isinstance(n, dict):
                    continue
                if "LocalBusiness" not in str(n.get("@type", "")):
                    continue
                if not ("address" in n or "telephone" in n):
                    continue  # nœud référence : rien à contrôler
                nb_biz += 1
                spec = n.get("openingHoursSpecification")
                if not spec:
                    erreurs.append("%s : nœud LocalBusiness sans horaires" % p.name)
                    continue
                variantes.setdefault(str(normalise(spec)), []).append(p.name)
                if n.get("telephone") not in (None, TEL):
                    erreurs.append("%s : téléphone divergent (%s)" % (p.name, n["telephone"]))
                adr = n.get("address", {})
                if isinstance(adr, dict) and adr.get("streetAddress") not in (None, RUE):
                    erreurs.append("%s : adresse divergente (%s)"
                                   % (p.name, adr.get("streetAddress")))

        if ANCIEN_TEXTE.search(t):
            erreurs.append("%s : texte visible encore en « Lun–Ven 8h–18h »" % p.name)

    if len(variantes) > 1:
        erreurs.append("%d versions d'horaires coexistent sur le site" % len(variantes))
        for v, files in variantes.items():
            erreurs.append("   %3d page(s) : %s (ex. %s)" % (len(files), v, files[0]))
    elif variantes:
        seule = list(variantes)[0]
        if seule != str(attendu_norm()):
            erreurs.append("horaires uniques mais NON conformes à la validation "
                           "du 24/08 : %s" % seule)

    print("NAP / horaires : %d pages, %d blocs JSON-LD, %d nœuds d'entreprise"
          % (len(pages), nb_bloc, nb_biz))
    for a in alertes:
        print("  KUJDES  %s" % a)
    for e in erreurs:
        print("  ERREUR  %s" % e)
    print("\n%s — %d erreur(s)"
          % ("CONFORME" if not erreurs else "NON CONFORME", len(erreurs)))
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
