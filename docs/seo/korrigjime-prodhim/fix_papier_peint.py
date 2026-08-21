#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dé-duplication papier peint / toile de verre — dépôt de production
eurotregu/rushiti-renovation (constat 2 de l'audit mots-clés du 20/08/2026).

Transforme les balises des pages papier-peint-<zone>.html qui visent encore
« toile de verre », sur le modèle vérifié en ligne le 21/08/2026 sur
/papier-peint-besancon et /papier-peint-pontarlier :

  title       : « Papier peint & toile de verre <Zone> | RUSHITI »
              → « Papier peint <Zone> – Pose et raccords | RUSHITI »
                (repli sans « – Pose et raccords » si > 60 caractères)
  h1          : suppression de « et toile de verre »
  description / og:description / twitter:description :
                « Pose de papier peint et toile de verre à <Zone> (<CP>) :
                  préparation des murs, pose soignée, finition. … »
              → « Pose de papier peint à <Zone> (<CP>) :
                  préparation des murs, raccords soignés, finition durable. … »

Le corps de page n'est PAS touché : la toile de verre reste mentionnée dans le
contenu et le lien vers la page toile-de-verre-<zone> est conservé.
Le script est idempotent : une page déjà corrigée est ignorée.

Usage :  python3 fix_papier_peint.py /chemin/vers/checkout [--apply]
         (sans --apply : simulation, rien n'est écrit)
"""
import pathlib
import re
import sys

MAX_TITLE = 60


def new_title(zone: str) -> str:
    full = f"Papier peint {zone} – Pose et raccords | RUSHITI"
    if len(full) <= MAX_TITLE:
        return full
    return f"Papier peint {zone} | RUSHITI"


def fix_file(path: pathlib.Path, apply: bool) -> list[str]:
    html = path.read_text(encoding="utf-8")
    orig = html
    changes: list[str] = []

    # 1. <title>
    m = re.search(
        r"<title>Papier peint (?:&amp;|&) toile de verre (.+?) \| RUSHITI</title>",
        html,
    )
    if m:
        zone = m.group(1).strip()
        nt = new_title(zone)
        html = html.replace(m.group(0), f"<title>{nt}</title>")
        changes.append(f"title -> {nt!r} ({len(nt)} car.)")

    # 2. <h1> — uniquement à l'intérieur de la balise h1
    def h1_sub(mo: re.Match) -> str:
        inner = mo.group(2).replace(" et toile de verre", "")
        return mo.group(1) + inner + mo.group(3)

    new_html = re.sub(
        r"(<h1[^>]*>)(.*?et toile de verre.*?)(</h1>)",
        h1_sub,
        html,
        flags=re.S,
    )
    if new_html != html:
        changes.append("h1 : « et toile de verre » retiré")
        html = new_html

    # 3. description / og:description / twitter:description
    def desc_sub(mo: re.Match) -> str:
        content = mo.group(2)
        content = content.replace(
            "Pose de papier peint et toile de verre à",
            "Pose de papier peint à",
        )
        content = content.replace(
            "pose soignée, finition.", "raccords soignés, finition durable."
        )
        return mo.group(1) + content + mo.group(3)

    pattern = (
        r'(<meta\s+(?:name="(?:description|twitter:description)"|'
        r'property="og:description")\s+content=")([^"]*toile de verre[^"]*)(")'
    )
    new_html = re.sub(pattern, desc_sub, html)
    # attributs dans l'ordre inverse (content avant name/property)
    pattern2 = (
        r'(<meta\s+content=")([^"]*toile de verre[^"]*)("\s+'
        r'(?:name="(?:description|twitter:description)"|property="og:description"))'
    )
    new_html = re.sub(pattern2, desc_sub, new_html)
    if new_html != html:
        changes.append("meta descriptions dé-dupliquées")
        html = new_html

    if changes and apply and html != orig:
        path.write_text(html, encoding="utf-8")
    return changes


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root = pathlib.Path(sys.argv[1])
    apply = "--apply" in sys.argv[2:]
    files = sorted(root.rglob("papier-peint-*.html"))
    if not files:
        print(f"Aucun fichier papier-peint-*.html sous {root}", file=sys.stderr)
        return 1
    touched = 0
    for f in files:
        changes = fix_file(f, apply)
        if changes:
            touched += 1
            print(f"{f.relative_to(root)}:")
            for c in changes:
                print(f"  - {c}")
    mode = "APPLIQUÉ" if apply else "SIMULATION (relancer avec --apply)"
    print(f"\n{touched}/{len(files)} fichier(s) à corriger — {mode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
