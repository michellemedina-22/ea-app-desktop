"""Ea App Desktop — Keep Ea App library folders on disk: dated copies of screenshot and workshop files before a patch."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='ea_app_desktop',
        description='Keep Ea App library folders on disk: dated copies of screenshot and workshop files before a patch.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Ea App Desktop')
    print('Archive Ea App files on this machine before you change the install.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
