#!/usr/bin/env python3
"""Rewrite the "N libraries", "N books" and "N videos" counters from the tables.

Those numbers were maintained by hand, one contributor at a time, and they had
come apart: the English README announced 103 in its opening list and 97 in the
section body while the section held 111 entries, and all three translations
claimed 23 videos against 22 rows.

    python scripts/update_counts.py            # rewrite them in place
    python scripts/update_counts.py --check    # exit 1 if any is stale

Each file is counted on its own, because the translations are behind the
English one by a few entries and a shared number would hide that. The gap is
reported.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Where each counted section starts and ends, per file, and the phrasings that
# carry its number. The digits in group 1 are what gets rewritten.
FILES = {
    "README.md": {
        "libraries": {
            "bounds": ("# Libraries and packages", "# Strategies"),
            "patterns": [r"- \[(\d+) libraries and packages\]",
                         r"\*List of \*\*(\d+) libraries and packages\*\*"],
        },
        "books": {
            "bounds": ("# Books", "# Videos"),
            "patterns": [r"- \[(\d+) books\]",
                         r"A comprehensive list of \*\*(\d+) books\*\*"],
        },
        "videos": {
            "bounds": ("# Videos", "# Blogs"),
            "patterns": [r"- \[(\d+) videos\]"],
        },
    },
    "README_zh.md": {
        "libraries": {
            "bounds": ("# 库和包", "# 策略"),
            "patterns": [r"- \[(\d+) 个\]\(#库和包\)",
                         r"\*(\d+)个实现交易机器人"],
        },
        "books": {
            "bounds": ("# 书籍", "# 视频"),
            "patterns": [r"- \[(\d+)本\]\(#书籍\)",
                         r"为量化交易者提供的(\d+)本书"],
        },
        "videos": {
            "bounds": ("# 视频", "# 博客"),
            "patterns": [r"- \[(\d+)个视频\]"],
        },
    },
    "README_ja.md": {
        "libraries": {
            "bounds": ("# ライブラリとパッケージ", "# 戦略"),
            "patterns": [r"\[(\d+)のライブラリ・パッケージ\]",
                         r"\*\*(\d+)のライブラリ・パッケージ\*\*"],
        },
        "books": {
            "bounds": ("# 書籍", "# 動画"),
            "patterns": [r"- 初心者からプロ向けの \[(\d+)冊の書籍\]",
                         r"\*\*(\d+)冊\*\* の総合リスト"],
        },
        "videos": {
            "bounds": ("# 動画", "# ブログ"),
            "patterns": [r"- \[(\d+)本の動画\]"],
        },
    },
}


def count(text: str, bounds: tuple[str, str]) -> int:
    start, end = (f"\n{h}\n" for h in bounds)
    block = text[text.index(start):text.index(end)]
    return sum(1 for line in block.splitlines() if line.startswith("| ["))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true",
                        help="report stale counters instead of rewriting them")
    args = parser.parse_args()

    stale, totals = [], {}
    for name, sections in FILES.items():
        path = ROOT / name
        text = original = path.read_text()
        for key, spec in sections.items():
            try:
                measured = count(text, spec["bounds"])
            except ValueError:
                print(f"{name}: cannot find the {key} section", file=sys.stderr)
                return 1
            totals.setdefault(key, {})[name] = measured

            for pattern in spec["patterns"]:
                match = re.search(pattern, text)
                if not match:
                    print(f"{name}: no counter matches {pattern!r}", file=sys.stderr)
                    return 1
                if match.group(1) == str(measured):
                    continue
                stale.append(f"{name}: {key} says {match.group(1)}, the section holds {measured}")
                text = (text[:match.start(1)] + str(measured) + text[match.end(1):])

        if text != original and not args.check:
            path.write_text(text)

    for line in stale:
        print(line)

    # The three files list the same entries, so a gap between them is a missing
    # translation rather than a counting mistake, and it is worth naming.
    for key, per_file in totals.items():
        if len(set(per_file.values())) > 1:
            print("mismatch across languages, "
                  + ", ".join(f"{n} {v}" for n, v in per_file.items())
                  + f" ({key})")

    if args.check and stale:
        print("run: python scripts/update_counts.py")
        return 1
    if not stale:
        print("counters are up to date")
    else:
        print(f"rewrote {len(stale)} counters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
