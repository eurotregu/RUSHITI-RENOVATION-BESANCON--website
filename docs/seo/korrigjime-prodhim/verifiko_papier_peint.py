#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérification post-correction des pages papier-peint-<zone>.html.

Contrôles (sur un checkout du dépôt de production) :
  1. Aucune occurrence de « toile de verre » dans <title>, <h1>,
     meta description, og:description, twitter:description.
  2. Longueur du <title> ≤ 60 caractères (entités HTML décodées).
  3. Le lien vers la page toile-de-verre-<zone> est toujours présent dans le
     corps (avertissement seulement : certaines zones consolidées n'ont plus
     de page toile de verre dédiée).

Usage :  python3 verifiko_papier_peint.py /chemin/vers/checkout
Code retour 0 = tout est conforme ; 1 = au moins une erreur bloquante.
"""
import html as htmllib
import pathlib
import re
import sys

MAX_TITLE = 60


def check_file(path: pathlib.Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    doc = path.read_text(encoding="utf-8")

    m = re.search(r"<title>(.*?)</title>", doc, flags=re.S)
    title = htmllib.unescape(m.group(1).strip()) if m else ""
    if not m:
        errors.append("pas de <title>")
    else:
        if "toile de verre" in title.lower():
            errors.append(f"title vise encore la toile de verre : {title!r}")
        if len(title) > MAX_TITLE:
            errors.append(f"title de {len(title)} car. (> {MAX_TITLE}) : {title!r}")

    for m in re.finditer(r"<h1[^>]*>(.*?)</h1>", doc, flags=re.S):
        if "toile de verre" in m.group(1).lower():
            errors.append("h1 vise encore la toile de verre")

    for m in re.finditer(r"<meta\s+[^>]*>", doc):
        tag = m.group(0)
        if re.search(
            r'(?:name="(?:description|twitter:description)"|property="og:description")',
            tag,
        ):
            c = re.search(r'content="([^"]*)"', tag)
            if c and "toile de verre" in c.group(1).lower():
                errors.append(f"meta vise encore la toile de verre : {tag[:80]}…")

    if not re.search(r'href="[^"]*toile-de-verre-', doc):
        warnings.append("aucun lien vers la page toile-de-verre (zone consolidée ?)")

    return errors, warnings


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    root = pathlib.Path(sys.argv[1])
    files = sorted(root.rglob("papier-peint-*.html"))
    if not files:
        print(f"Aucun fichier papier-peint-*.html sous {root}", file=sys.stderr)
        return 2
    bad = 0
    for f in files:
        errors, warnings = check_file(f)
        for e in errors:
            print(f"ERREUR  {f.relative_to(root)} : {e}")
        for w in warnings:
            print(f"avert.  {f.relative_to(root)} : {w}")
        bad += bool(errors)
    print(f"\n{len(files)} fichier(s) contrôlé(s), {bad} en erreur.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
