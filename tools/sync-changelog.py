#!/usr/bin/env python3
"""Copie CHANGELOG.md dans index.html (bloc <script id="changelog-src">), pour que le dialogue
« Nouveautés » de l'application fonctionne hors ligne.

Usage : python3 tools/sync-changelog.py          met à jour index.html
        python3 tools/sync-changelog.py --check  échoue si index.html n'est pas à jour
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BLOCK = re.compile(r'(<script type="text/markdown" id="changelog-src">\n)(.*?)(</script>)', re.S)


def main() -> int:
    html_path = ROOT / 'index.html'
    html = html_path.read_text(encoding='utf-8')
    md = (ROOT / 'CHANGELOG.md').read_text(encoding='utf-8').strip() + '\n'
    if '</script' in md.lower():
        print('CHANGELOG.md ne doit pas contenir « </script »', file=sys.stderr)
        return 1
    m = BLOCK.search(html)
    if not m:
        print('Bloc <script id="changelog-src"> introuvable dans index.html', file=sys.stderr)
        return 1
    if '--check' in sys.argv:
        if m.group(2) != md:
            print('Le journal intégré à index.html diffère de CHANGELOG.md : lancez python3 tools/sync-changelog.py',
                  file=sys.stderr)
            return 1
        print('Journal intégré à jour.')
        return 0
    html_path.write_text(html[:m.start(2)] + md + html[m.end(2):], encoding='utf-8')
    print('index.html mis à jour.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
