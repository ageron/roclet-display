#!/usr/bin/env python3
"""Test the content-addressed archive that will be published."""
import argparse
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MODULES = ('main.roc', 'Display.roc', 'Input.roc', 'InputValues.roc')


def run(*args, cwd=ROOT):
    result = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    return result.stdout


def test(roc):
    roc = shutil.which(roc) or str(Path(roc).resolve())
    output = ROOT / 'dist'
    output.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='roclet-display-') as directory:
        temp = Path(directory)
        run(roc, 'bundle', str(ROOT / 'package/main.roc'), '--output-dir', str(temp))
        archives = list(temp.glob('*.tar.zst'))
        if len(archives) != 1:
            raise RuntimeError('Expected exactly one package archive')
        archive = archives[0]
        run(roc, 'unbundle', str(archive), cwd=temp)
        extracted = temp / archive.name.removesuffix('.tar.zst')
        for name in MODULES:
            if (extracted / name).read_bytes() != (ROOT / 'package' / name).read_bytes():
                raise RuntimeError(f'Archive differs from source: {name}')
        result = run(roc, '--replace-dep', '../package/main.roc', str(extracted / 'main.roc'), str(ROOT / 'tests/smoke.roc'), cwd=ROOT / 'tests')
        if 'Chart' not in result or 'hello' not in result:
            raise RuntimeError('Smoke test did not produce expected output')
        for example in sorted((ROOT / 'examples').glob('*.roc')):
            result = run(roc, '--replace-dep', (ROOT / 'package-url.txt').read_text().strip(), str(extracted / 'main.roc'), str(example), cwd=example.parent)
            if not result.strip():
                raise RuntimeError(f'Example produced no output: {example.name}')
            print(f'PASS example: {example.name}')
        shutil.copy2(archive, output / archive.name)
        (output / 'archive.txt').write_text(archive.name + '\n')
        print(f'PASS extracted package and constructors: {archive.name}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--roc', default='roc')
    test(parser.parse_args().roc)
