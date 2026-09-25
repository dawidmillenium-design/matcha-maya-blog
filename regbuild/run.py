#!/usr/bin/env python3
"""Regenerate regional pages with: python -m regbuild.run"""
import json
from pathlib import Path
from .common import build


def main():
    regions = json.loads((Path(__file__).parent / 'regions.json').read_text(encoding='utf-8'))
    for key, region in regions.items():
        print(f'{key}: {build(key, region)} linked city guides')


if __name__ == '__main__':
    main()
