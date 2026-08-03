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
    inventory.add_argument("--named-root", action="append", default=[])
    inventory.add_argument("--redact-absolute-paths", action="store_true")
    inventory.add_argument("--out-json", required=True)
    inventory.add_argument("--out-md", required=True)
    return parser


def _parse_named_roots(values: list[str]) -> dict[str, str]:
    roots: dict[str, str] = {}
    for value in values:
        if "=" not in value:
            raise ValueError("--named-root must use ALIAS=PATH")
        alias, path = value.split("=", 1)
        alias = alias.strip()
        path = path.strip()
        if not alias or not path:
            raise ValueError("--named-root requires a non-empty alias and path")
        if alias in roots:
            raise ValueError(f"duplicate named root alias: {alias}")
        roots[alias] = path
    return roots


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command != "inventory":
        return 2
    try:
        named_roots = _parse_named_roots(args.named_root)
    except ValueError:
        return 2
    if not args.root and not named_roots:
        return 2

    if named_roots:
        roots: list[str] | dict[str, str] = {
            **{f"ROOT_{index}": path for index, path in enumerate(args.root, start=1)},
            **named_roots,
        }
    else:
        roots = args.root

    report = inventory_paths(
        roots,
        repo_root=args.repo_root,
        redact_absolute_paths=args.redact_absolute_paths,
    )
    write_inventory_reports(report, args.out_json, args.out_md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
