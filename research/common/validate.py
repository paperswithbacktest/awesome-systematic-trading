"""Validate an experiment directory against the contract (content-level)."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

REQUIRED_FILES = [
    "README.md",
    "config.yaml",
    "run.py",
    "requirements-lock.txt",
    "data_manifest.json",
    "metrics.csv",
    "checks.json",
    "verdict.json",
]

REQUIRED_CONFIG_KEYS = [
    "experiment_id",
    "strategy_id",
    "strategy_title",
    "experiment_class",
    "hypothesis",
    "source_paper_url",
    "source_repo_path",
    "source_repo_commit",
    "code_commit",
    "run_timestamp_utc",
    "data",
    "universe",
    "signal",
    "costs",
    "metrics",
    "known_limitations",
]

REQUIRED_DATA_KEYS = [
    "provider",
    "instruments",
    "frequency",
    "timezone",
    "start",
    "end",
    "adjusted",
]

REQUIRED_VERDICT_KEYS = [
    "experiment_id",
    "strategy_id",
    "hypothesis",
    "experiment_class",
    "evidence_level",
    "result_verdict",
    "reproduction_status",
    "summary",
    "promotion_blockers",
    "reviewer_status",
    "reproduction_command",
]

REQUIRED_CHECK_NAMES = [
    "no_lookahead",
    "timezone_explicit",
    "data_hash_verified",
    "cost_units_verified",
    "annualization_verified",
    "incomplete_bar_excluded",
]

VALID_EVIDENCE = {"E0", "E1", "E2", "E3", "E4", "E5"}
VALID_CLASS = {"replication", "proxy", "diagnostic", "robustness"}
VALID_RESULT = {"supported", "unsupported", "inconclusive"}
VALID_REPRO = {"not-attempted", "partial", "faithful", "failed"}
VALID_REVIEW = {"pending", "approved", "rejected"}

METRICS_REQUIRED_COLS = {"variant", "sharpe", "cagr", "max_dd"}

FORBIDDEN_CLAIM_WORDS = [
    "validated",
    "dead on arrival",
    "confirmed edge",
    "production ready",
]


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_yaml(path: Path) -> Any:
    try:
        import yaml  # type: ignore
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError(
            "PyYAML is required to validate config.yaml. "
            "Install with: pip install pyyaml"
        ) from exc
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _file_sha256(path: Path) -> str:
    import hashlib

    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_experiment_dir(exp_dir: str | Path) -> dict[str, Any]:
    root = Path(exp_dir)
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        return {
            "ok": False,
            "errors": [f"not a directory: {root}"],
            "warnings": [],
        }

    for name in REQUIRED_FILES:
        if not (root / name).exists():
            errors.append(f"missing required file: {name}")

    # --- config.yaml ---
    config: dict[str, Any] = {}
    config_path = root / "config.yaml"
    if config_path.exists():
        try:
            loaded = _load_yaml(config_path)
            if not isinstance(loaded, dict):
                errors.append("config.yaml must parse to a mapping")
            else:
                config = loaded
                for k in REQUIRED_CONFIG_KEYS:
                    if k not in config:
                        errors.append(f"config missing key: {k}")
                data = config.get("data")
                if isinstance(data, dict):
                    for k in REQUIRED_DATA_KEYS:
                        if k not in data:
                            errors.append(f"config.data missing key: {k}")
                else:
                    errors.append("config.data must be a mapping")
                if config.get("experiment_class") not in VALID_CLASS:
                    errors.append(
                        f"config.experiment_class invalid: {config.get('experiment_class')}"
                    )
                lim = config.get("known_limitations")
                if not isinstance(lim, list) or len(lim) == 0:
                    warnings.append("config.known_limitations is empty")
                # ID format
                eid = str(config.get("experiment_id", ""))
                if not re.match(r"^EXP-", eid):
                    errors.append(f"experiment_id must start with EXP-: {eid!r}")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"config.yaml not parseable: {exc}")

    # --- data_manifest.json + hash verify ---
    manifest_path = root / "data_manifest.json"
    if manifest_path.exists():
        try:
            man = _load_json(manifest_path)
            if "files" not in man or not isinstance(man["files"], dict):
                errors.append("data_manifest.json missing 'files' object")
            else:
                for fname, meta in man["files"].items():
                    if not isinstance(meta, dict) or "sha256" not in meta:
                        errors.append(f"manifest file entry missing sha256: {fname}")
                        continue
                    # Resolve path: relative to experiment dir unless absolute
                    candidate = Path(fname)
                    if not candidate.is_absolute():
                        # try as-is under exp, then under exp/data
                        p1 = root / fname
                        p2 = root / "data" / Path(fname).name
                        path = p1 if p1.exists() else p2 if p2.exists() else p1
                    else:
                        path = candidate
                    if not path.exists():
                        # allow missing if marked external/not_cached
                        if meta.get("external") or meta.get("not_cached"):
                            warnings.append(
                                f"manifest references external/uncached file: {fname}"
                            )
                        else:
                            errors.append(f"manifest file missing on disk: {fname}")
                        continue
                    actual = _file_sha256(path)
                    expected = str(meta["sha256"]).lower()
                    if actual.lower() != expected:
                        errors.append(
                            f"sha256 mismatch for {fname}: "
                            f"manifest={expected[:12]}… actual={actual[:12]}…"
                        )
        except Exception as exc:  # noqa: BLE001
            errors.append(f"data_manifest.json not parseable: {exc}")

    # --- checks.json ---
    checks_path = root / "checks.json"
    checks: dict[str, Any] = {}
    if checks_path.exists():
        try:
            checks = _load_json(checks_path)
            if not isinstance(checks, dict):
                errors.append("checks.json must be an object")
            else:
                if "passed" not in checks:
                    errors.append("checks.json missing top-level 'passed' bool")
                block = checks.get("checks")
                if not isinstance(block, dict):
                    errors.append("checks.json missing 'checks' object")
                else:
                    for name in REQUIRED_CHECK_NAMES:
                        if name not in block:
                            errors.append(f"checks.checks missing: {name}")
                        else:
                            item = block[name]
                            if not isinstance(item, dict) or "passed" not in item:
                                errors.append(
                                    f"checks.checks.{name} must be object with 'passed'"
                                )
                # If any sub-check failed, top-level passed must be false
                if isinstance(block, dict) and checks.get("passed") is True:
                    for name, item in block.items():
                        if isinstance(item, dict) and item.get("passed") is False:
                            errors.append(
                                f"checks.passed=true but {name}.passed=false"
                            )
        except Exception as exc:  # noqa: BLE001
            errors.append(f"checks.json not parseable: {exc}")

    # --- verdict.json ---
    verdict_path = root / "verdict.json"
    verdict: dict[str, Any] = {}
    if verdict_path.exists():
        try:
            verdict = _load_json(verdict_path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"verdict.json not parseable: {exc}")
            verdict = {}
        if isinstance(verdict, dict):
            for k in REQUIRED_VERDICT_KEYS:
                if k not in verdict:
                    errors.append(f"verdict missing key: {k}")
            if verdict.get("evidence_level") not in VALID_EVIDENCE:
                errors.append(
                    f"invalid evidence_level: {verdict.get('evidence_level')}"
                )
            if verdict.get("experiment_class") not in VALID_CLASS:
                errors.append(
                    f"invalid experiment_class: {verdict.get('experiment_class')}"
                )
            if verdict.get("result_verdict") not in VALID_RESULT:
                errors.append(
                    f"invalid result_verdict: {verdict.get('result_verdict')}"
                )
            if verdict.get("reproduction_status") not in VALID_REPRO:
                errors.append(
                    f"invalid reproduction_status: {verdict.get('reproduction_status')}"
                )
            if verdict.get("reviewer_status") not in VALID_REVIEW:
                errors.append(
                    f"invalid reviewer_status: {verdict.get('reviewer_status')}"
                )
            # Workers may not self-approve
            if verdict.get("reviewer_status") == "approved":
                warnings.append(
                    "reviewer_status=approved — only independent reviewer should set this"
                )
            blockers = verdict.get("promotion_blockers")
            if not isinstance(blockers, list) or len(blockers) == 0:
                warnings.append("promotion_blockers is empty")
            summary = str(verdict.get("summary", "")).lower()
            for word in FORBIDDEN_CLAIM_WORDS:
                if word in summary and verdict.get("evidence_level") in {
                    "E0",
                    "E1",
                    "E2",
                }:
                    warnings.append(
                        f"summary contains strong claim '{word}' at "
                        f"{verdict.get('evidence_level')}"
                    )
            if verdict.get("evidence_level") in {"E3", "E4", "E5"} and verdict.get(
                "experiment_class"
            ) in {"proxy", "diagnostic"}:
                warnings.append(
                    "high evidence_level on proxy/diagnostic class — justify carefully"
                )
            # Cross-check IDs
            if config and verdict.get("experiment_id") != config.get("experiment_id"):
                errors.append(
                    "verdict.experiment_id != config.experiment_id "
                    f"({verdict.get('experiment_id')!r} vs {config.get('experiment_id')!r})"
                )
            if config and verdict.get("experiment_class") != config.get(
                "experiment_class"
            ):
                errors.append("verdict.experiment_class != config.experiment_class")
        else:
            errors.append("verdict.json must be an object")

    # --- metrics.csv schema ---
    metrics_path = root / "metrics.csv"
    if metrics_path.exists():
        try:
            import csv

            with metrics_path.open("r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                if not reader.fieldnames:
                    errors.append("metrics.csv has no header")
                else:
                    cols = {c.strip().lower() for c in reader.fieldnames}
                    missing = METRICS_REQUIRED_COLS - cols
                    # allow aliases
                    aliases = {
                        "max_dd": {"maxdd", "max_drawdown", "max dd"},
                        "cagr": {"cagr"},
                        "sharpe": {"sharpe", "sharpe_ratio"},
                        "variant": {"variant", "name", "strategy"},
                    }
                    still_missing = set()
                    for req in METRICS_REQUIRED_COLS:
                        if req in cols:
                            continue
                        if any(a in cols for a in aliases.get(req, set())):
                            continue
                        still_missing.add(req)
                    if still_missing:
                        errors.append(
                            f"metrics.csv missing columns: {sorted(still_missing)} "
                            f"(have={sorted(cols)})"
                        )
                    rows = list(reader)
                    if len(rows) == 0:
                        errors.append("metrics.csv has no data rows")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"metrics.csv not readable: {exc}")

    return {
        "ok": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "path": str(root),
    }


def main(argv: list[str] | None = None) -> int:
    import sys

    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print("usage: python -m research.common.validate <exp_dir> [<exp_dir>...]")
        return 2
    exit_code = 0
    for a in args:
        result = validate_experiment_dir(a)
        status = "OK" if result["ok"] else "FAIL"
        print(f"[{status}] {result['path']}")
        for e in result["errors"]:
            print(f"  ERROR: {e}")
        for w in result["warnings"]:
            print(f"  WARN:  {w}")
        if not result["ok"]:
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
