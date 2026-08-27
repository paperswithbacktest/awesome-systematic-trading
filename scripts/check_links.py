#!/usr/bin/env python3
"""Flag entries in README.md whose GitHub repository is gone, archived or dormant.

An awesome list decays quietly: projects get archived, accounts disappear, and the
list keeps recommending them. This checks every GitHub link and prints a report.

    GITHUB_TOKEN=... python scripts/check_links.py           # report only
    GITHUB_TOKEN=... python scripts/check_links.py --annotate # also mark the README

Exit code is 1 when anything is dead or archived, so CI can open an issue.
"""
import argparse
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
DORMANT_AFTER = timedelta(days=730)
LINK = re.compile(r"https://github\.com/([\w.-]+/[\w.-]+?)(?=[)\s#]|$)")


def fetch(repo: str, token: str | None):
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-systematic-trading-link-check",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            import json

            return json.load(response)
    except urllib.error.HTTPError as error:
        if error.code in (404, 451):
            return None
        raise


def classify(data) -> str:
    if data is None:
        return "missing"
    if data.get("archived"):
        return "archived"
    pushed = datetime.strptime(data["pushed_at"], "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=timezone.utc
    )
    if datetime.now(timezone.utc) - pushed > DORMANT_AFTER:
        return f"dormant since {pushed:%Y-%m}"
    return "ok"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--annotate", action="store_true")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    text = README.read_text()
    repos = sorted(set(LINK.findall(text)))
    print(f"checking {len(repos)} repositories", file=sys.stderr)

    findings = {}
    for repo in repos:
        state = classify(fetch(repo, token))
        if state != "ok":
            findings[repo] = state
            print(f"{state:24} {repo}")

    if args.annotate:
        for repo, state in findings.items():
            label = "no longer available" if state == "missing" else state
            text = re.sub(
                rf"(\[[^\]]+\]\(https://github\.com/{re.escape(repo)}\))(?! `)",
                rf"\1 `{label}`",
                text,
            )
        README.write_text(text)
        print(f"annotated {len(findings)} entries", file=sys.stderr)

    broken = sum(1 for s in findings.values() if s in ("missing", "archived"))
    print(
        f"\n{len(repos) - len(findings)} healthy, {len(findings)} flagged "
        f"({broken} dead or archived)",
        file=sys.stderr,
    )
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
