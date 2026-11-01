#!/usr/bin/env python3
"""Pin runnable examples and documentation to a published Display release."""
import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def update(version, archive):
    if not re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-[0-9A-Za-z.-]+)?', version):
        raise ValueError('Invalid release version')
    if not re.fullmatch(r'[1-9A-HJ-NP-Za-km-z]+\.tar\.zst', archive):
        raise ValueError('Expected a content-addressed archive')
    pin = ROOT / 'package-url.txt'
    old = pin.read_text().strip()
    url = f'https://github.com/ageron/roclet-display/releases/download/{version}/{archive}'
    paths = [ROOT / 'README.md', *sorted((ROOT / 'examples').glob('*.roc'))]
    changes = {}
    for path in paths:
        source = path.read_text()
        if old not in source:
            raise ValueError(f'{path} does not contain the current pin')
        changes[path] = source.replace(old, url)
    for path, source in changes.items():
        path.write_text(source)
    pin.write_text(url + '\n')
    return url


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', required=True)
    parser.add_argument('--archive', required=True)
    args = parser.parse_args()
    print(update(args.version, args.archive))
