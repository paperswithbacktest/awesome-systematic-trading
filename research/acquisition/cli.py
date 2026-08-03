"""Command line entry points for deterministic acquisition operations."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from research.acquisition.inventory import inventory_paths, write_inventory_reports


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="research-acquisition")
    subparsers = parser.add_subparsers(dest="command")
    inventory = subparsers.add_parser("inventory")
    inventory.add_argument("--repo-root", required=True)
    inventory.add_argument("--root", action="append", default=[])
    inventory.add_argument("--out-json", required=True)
    inventory.add_argument("--out-md", required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command != "inventory" or not args.root:
        return 2

    report = inventory_paths(args.root, repo_root=args.repo_root)
    write_inventory_reports(report, args.out_json, args.out_md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
