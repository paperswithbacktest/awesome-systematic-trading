"""Provenance capture: hashes, git state, run context, data manifests."""

from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def file_sha256(path: str | Path) -> str:
    p = Path(path)
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def hash_dataframe(df: pd.DataFrame) -> str:
    """Stable content hash of a DataFrame (CSV bytes, index included)."""
    payload = df.to_csv().encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def git_state(repo_root: str | Path) -> dict[str, Any]:
    root = Path(repo_root)
    out: dict[str, Any] = {
        "repo_root": str(root),
        "commit": None,
        "branch": None,
        "dirty": None,
        "error": None,
    }
    try:
        def _run(args: list[str]) -> str:
            r = subprocess.run(
                args,
                cwd=root,
                capture_output=True,
                text=True,
                check=False,
            )
            if r.returncode != 0:
                raise RuntimeError(r.stderr.strip() or r.stdout.strip())
            return r.stdout.strip()

        out["commit"] = _run(["git", "rev-parse", "HEAD"])
        out["branch"] = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
        status = _run(["git", "status", "--porcelain"])
        out["dirty"] = bool(status)
        out["status_porcelain"] = status
    except Exception as exc:  # noqa: BLE001
        out["error"] = str(exc)
    return out


def package_versions(names: list[str] | None = None) -> dict[str, str]:
    names = names or ["pandas", "numpy", "yfinance", "matplotlib"]
    vers: dict[str, str] = {}
    for name in names:
        try:
            mod = __import__(name)
            vers[name] = getattr(mod, "__version__", "unknown")
        except Exception as exc:  # noqa: BLE001
            vers[name] = f"unavailable: {exc}"
    return vers


def run_context(repo_root: str | Path) -> dict[str, Any]:
    return {
        "timestamp_utc": utc_now_iso(),
        "python": sys.version.replace("\n", " "),
        "executable": sys.executable,
        "platform": platform.platform(),
        "packages": package_versions(),
        "git": git_state(repo_root),
    }


def write_data_manifest(
    path: str | Path,
    *,
    provider: str,
    instruments: list[str],
    frequency: str,
    timezone: str,
    start: str | None,
    end: str | None,
    files: dict[str, dict[str, Any]],
    query: dict[str, Any] | None = None,
    notes: list[str] | None = None,
    retrieved_at_utc: str | None = None,
) -> dict[str, Any]:
    manifest = {
        "retrieved_at_utc": retrieved_at_utc or utc_now_iso(),
        "provider": provider,
        "instruments": instruments,
        "frequency": frequency,
        "timezone": timezone,
        "start": start,
        "end": end,
        "query": query or {},
        "files": files,
        "notes": notes or [],
    }
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest
