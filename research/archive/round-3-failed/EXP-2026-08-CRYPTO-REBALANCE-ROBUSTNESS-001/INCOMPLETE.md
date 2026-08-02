# INCOMPLETE — EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-001

**Status:** incomplete / rejected for promotion  
**Date (UTC):** 2026-08-02  
**Harness baseline:** `35e0ac0`  
**Review:** `research/reviews/REV-2026-08-CRYPTO-REBALANCE-001.md`

## Why incomplete

Worker timed out while rate-limited on live Yahoo downloads. Only `config.yaml` and `run.py` exist. No metrics, verdict, checks, data_manifest, or README.

## Do not run

This attempt's universe claim (~26 paper-like tickers) does not match available offline cache (12 survivors). Continuing live downloads will re-trigger rate limits.

## Recovery

Use `EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002` — explicit 12-asset static-survivor long-only proxy from `research/archive/round-1/crypto-rebalance/prices.csv` only.
