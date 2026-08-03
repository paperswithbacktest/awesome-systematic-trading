# Handoff — Round-4 Data Acquisition + Independent Review

**Date (UTC):** 2026-08-02  
**Session purpose:** Close Round-3 offline recovery; open Round-4 as a **data lake / source registry / independent review** phase.  
**Do not:** re-run or rewrite Round-3 `.002` runners, promote vault strategy status, or start bulk blind Yahoo downloads in the first hour of the next session.

---

## 1. Frozen starting state (authoritative)

| Item | Value |
|------|--------|
| Branch | `research/validation-round-3` |
| Tip (start here) | `e85d5e091e7b9483b42d1ae88a46a619298a8bdf` |
| Harness baseline | `35e0ac0a96da66cec194eeaf3eda4016554d8748` |
| Source freeze **S** (`.002` runners/configs body) | `8104683e74be96f53f2564d7aa24908ea0687dc4` |
| Provenance stamp **P** (`code_commit` stamped to S) | `2fcd7415605e9af8758237b85a957126823e4dcd` |
| BTC output commit | `ebab7bf52c28eb320f2cfe1b6a461756a69fee31` |
| Crypto output commit (= tip before this handoff) | `e85d5e091e7b9483b42d1ae88a46a619298a8bdf` |
| Harness tests | **25/25** passed |
| Both `.002` mechanical validators | **OK** |
| Working tree at Round-3 close | clean |
| Local bot git identity | removed after Round-3 commits; re-set only for this handoff commit then unset again |

### Round-3 experiment outcomes

| Experiment | Path | Disposition |
|------------|------|-------------|
| BTC hourly `.001` | `research/archive/round-3-failed/EXP-2026-08-BTC-OVERNIGHT-HOURLY-001/` | **Rejected** — B&H fee churn, false dates, soft clock, wrong URL |
| Crypto rebalance `.001` | `research/archive/round-3-failed/EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-001/` | **Incomplete** — Yahoo rate-limit → 0 instruments → empty DF crash |
| Asset-trend monthly `.001` | `research/archive/round-3-failed/EXP-2026-08-ASSET-TREND-MONTHLY-001/` | **Blocked** — offline cache missing **EFA** and **GSG**; no silent GLD/DBC substitution |
| BTC hourly `.002` | `research/experiments/EXP-2026-08-BTC-OVERNIGHT-HOURLY-002/` | **Candidate E2** — integrator audit PASS; independent review **pending** |
| Crypto rebalance `.002` | `research/experiments/EXP-2026-08-CRYPTO-REBALANCE-ROBUSTNESS-002/` | **Candidate E2** — integrator audit PASS; independent review **pending** |

### Reviews

- `research/reviews/REV-2026-08-BTC-HOURLY-001.md` (rejected `.001`)
- `research/reviews/REV-2026-08-BTC-HOURLY-002.md` (integrator audit `.002`)
- `research/reviews/REV-2026-08-CRYPTO-REBALANCE-001.md` (incomplete `.001`)
- `research/reviews/REV-2026-08-CRYPTO-REBALANCE-002.md` (integrator audit `.002`)
- `research/reviews/REV-2026-08-ASSET-TREND-001.md` (blocked `.001`)

### `.002` governance (do not “fix” without a separate reviewer)

Both candidate experiments currently carry:

- `evidence_level: E2` (artifact class ceiling for this run)
- `reviewer_status: pending` (**same-agent audit ≠ independent approval**)
- `result_verdict: inconclusive` (runner-default; keep unless independent review changes it under a new policy)
- `reproduction_status: partial`
- BTC `code_commit` = **S**; `run_git_commit` = **P** (`2fcd741…`)
- Crypto `code_commit` = **S**; `run_git_commit` = BTC-output commit (`ebab7bf…`)
- `git_dirty_at_start: false` on both runs

### Local point estimates (integrator reading only — not vault promotion)

**BTC `.002`** (exact 22:00→00:00 UTC open-to-open; n=697; Yahoo hourly post-paper proxy):

| Metric | Value |
|--------|-------|
| Primary Sharpe (0 bps) | −0.089 |
| CAGR | −1.74% |
| Mean | −0.29 bps/day |
| B&H Sharpe (gross) | 0.315 |
| Placebo rank (0 bps) | 9/12 |

Integrator reading: **unfavorable** on this frozen proxy. Does **not** reject SSRN `4081000`.

**Crypto `.002`** (12-asset Yahoo static-survivor long-only; primary `full_common_12` 2020-08-21→2026-08-01, n=2172):

| Variant (0 bps) | Sharpe | vs B&H CAGR |
|-----------------|--------|-------------|
| B&H drift | 0.710 | — |
| Daily EW | 0.761 | +5.88 pp |
| Monthly EW | 0.815 | +11.65 pp |

At 20 bps on primary: monthly still beats daily and B&H.  
Integrator reading: **favorable proxy-only**. **Not** paper PIT / 27-coin Bitfinex / 70% short leg.

### Input cache SHAs (raw files gitignored; local copies required for re-audit)

| Dataset | SHA-256 |
|---------|---------|
| BTC hourly Yahoo cache (source for BTC `.002`) | `417e6b4a96c0b2c31daca1905eeae56b5789a11e90f55b57df8284d0bfd4ce72` |
| Crypto daily Round-1 prices (source for crypto `.002`) | `84a1db1b2e703dc4fb12b664d058024e3e440fb7c61296fa5f71686317d68a57` |

Paths (local, ignored):

- `research/archive/round-3-failed/EXP-2026-08-BTC-OVERNIGHT-HOURLY-001/data/btc_usd_hourly_yfinance.csv`
- `research/archive/round-1/crypto-rebalance/prices.csv`
- Experiment copies under `research/experiments/**/data/` (also gitignored)

### Vault state (must remain until independent review)

Vault root (this machine): `C:\Users\Kyle\OneDrive\Documents\Obsidian Vault`

| Strategy note | status | evidence_level | best_experiment | notes |
|---------------|--------|----------------|-----------------|-------|
| Overnight Seasonality in Bitcoin | `researched` | E1 | null | candidate `.002` linked; local Sharpe not promoted into `local_sharpe_ratio` |
| Rebalancing Premium in Cryptocurrencies | `researched` | E1 | null | candidate `.002` linked; source Sharpe separate |
| Asset Class Trend-Following | `researched` | E1 | null | `.001` blocked; no substitute universe |

- `85-Index/Strategy Implementation Pipeline.md` — **`experimented` empty**
- Source-reported Sharpes (0.892 / 0.698 / 0.502) remain E0/E1 table claims
- Local-only vault snapshots (gitignored):  
  - `research/checkpoints/2026-08-02-vault-pre-closure/`  
  - `research/checkpoints/2026-08-02-vault-post-closure/` (+ `SHA256SUMS.txt`)

---

## 2. Round-4 mission (two workstreams)

### Workstream A — Independent review (can run in parallel with data infra)

A **different** agent or human reviews frozen `.002` artifacts **without modifying runners, configs, metrics, or trades**.

**BTC checklist**

- Exact 22:00 open → 00:00 open; hold always 2h  
- B&H gross-only (no daily fee churn)  
- Fee arithmetic `2 × fee_bps`  
- Sample honesty (cache end vs last entry date)  
- Placebo interpretation = descriptive only  
- Venue mismatch explicit (Yahoo ≠ Gemini/Bitfinex)  
- Provenance: S / P / dirty=false / SHA match  

**Crypto checklist**

- Prior-close decision; earn next close-to-close  
- `risky_traded_notional` cash-excluded; establishment = 1.0  
- Four cohorts; primary sample starts when DOT joins  
- Contiguous-segment rule disclosed (post-hoc cleaning ≠ PIT)  
- Comparisons match metrics deltas  
- Survivorship + missing short leg explicit  
- Provenance + SHA  

**Approval semantics**

- Independent approval of an experiment = **artifact trustworthy**  
- Still **not** “strategy validated / live-candidate”  
- Only after that: consider vault `status: experimented` + strategy-level E2 **max**  
- Never overwrite `reported_sharpe_ratio` with local Sharpe  

### Workstream B — Data acquisition layer + free-source lake

Build infrastructure **before** bulk downloads. Yahoo is allowed as a **secondary / convenience** source, not the sole dependency and not with unconstrained ticker-by-ticker swarms.

---

## 3. Provider strategy (free-first ladder)

### Critical rule

“Live Yahoo and other free sources” means:

1. Inventory existing local caches first  
2. Build rate-limit-aware, resumable acquisition with empty-response guards  
3. Prefer **venue-official** or **documented** free archives for crypto bars  
4. Use Yahoo for ETF dailies and cross-checks — with backoff, batching, and hard failure on empty frames  
5. Never blend vendors inside one comparison unless declared as a multi-vendor robustness design  

### BTC / crypto intraday (UTC candles)

| Priority | Source | Best use | Risks |
|----------|--------|----------|-------|
| 1 | Official exchange downloadable archives (e.g. Binance public data) | Long UTC 1h/1m OHLCV | BTCUSDT ≠ BTCUSD; venue mismatch must be explicit |
| 2 | Coinbase Exchange public candles | BTC-USD spot venue | Pagination + rate limits |
| 3 | Kraken public OHLC | BTC/USD spot | Retention/page limits |
| 4 | Gemini / Bitfinex public endpoints or archives | Closer to paper/repo venues | Availability/history limits |
| 5 | CryptoCompare free historical | Cross-check / breadth | Keys, credits, param recording |
| 6 | Yahoo Finance hourly | Secondary proxy / short window | ~730d intraday cap; rate limits; composite venue |

Required metadata for every BTC bar set:

```yaml
instrument: BTC-USD | BTC-USDT
venue: ...
frequency: 1h
timezone: UTC
candle_label: open-time   # or close-time — pick one and never mix silently
price_type: trade | mid | composite
start: ...
end: ...
retrieved_at_utc: ...
provider_url: ...
request_parameters: {}
pagination: ...
sha256: ...
missing_bar_policy: ...
```

Do **not** call 22:00→00:00 “identical” across BTCUSD/BTCUSDT/Gemini/Bitfinex/Coinbase/Kraken/Binance without labeling a **venue robustness** comparison.

### Crypto cross-section (rebalancing)

Keep three datasets distinct:

1. **Frozen Round-3 proxy cache** (immutable input to crypto `.002`)  
2. **Broad historical membership panel** (first-obs / delist where possible)  
3. **Venue-specific tradability panel** (Bitfinex-aligned if paper fidelity is the goal)

Next scientific question:

> Can a point-in-time eligible, historically available universe be constructed with membership fixed **before** each rebalance date?

Not:

> Can another static survivor table look better?

### ETFs (asset-class trend unblock)

Required symbols (no substitutes under the frozen paper-like design):

```text
SPY  EFA  IEF  VNQ  GSG
```

| Source | Use | Caution |
|--------|-----|---------|
| Yahoo Finance | Adjusted daily OHLC | Rate limits; document auto_adjust / adj close semantics |
| Stooq | Redundant daily cross-check | Verify symbol mapping + adjustment |
| Alpha Vantage free tier | Small fallback | Strict caps; API key from env only |
| Nasdaq Data Link free sets | Supplementary | Coverage/license varies |
| FRED | RF/macro only | Not ETF prices |

Before marking ETF data experiment-eligible, answer:

- Split-adjusted? Dividend/distribution-adjusted?  
- Price return vs total-return proxy?  
- Exchange sessions vs calendar days?  
- Full common history start for **all five**?  
- GSG commodity exposure matches the strategy definition?

When EFA+GSG are acquired and QA-passed, mint a **new** asset-trend experiment ID. **Never** revive `.001`.

### Other free sources (later)

- SEC EDGAR — fundamentals (identified requests, rate limits)  
- CFTC — positioning (report dates + revisions)  
- US Treasury / ECB — rates  

---

## 4. Architecture to build first (before broad network pulls)

### Branch

```text
git checkout -b research/data-acquisition-round-4 e85d5e091e7b9483b42d1ae88a46a619298a8bdf
```

(If this handoff commit is tip, branch from the **new tip** after handoff lands — still include Round-3 tip `e85d5e0` as parent lineage.)

### Suggested layout

```text
research/data/
  registry/                 # committed catalogs
  manifests/                # committed retrieval manifests
  recipes/                  # committed acquisition recipes
  quality-reports/          # committed QA summaries
  raw/<provider>/...        # gitignored
  normalized/<dataset_id>/  # gitignored unless tiny public fixtures
  quarantine/               # gitignored partial/bad batches
  acquisition-logs/         # gitignored or redacted

research/acquisition/
  providers/                # yahoo, stooq, gemini, bitfinex, kraken, coinbase, binance, coingecko, ...
  schemas/
  tests/                    # empty-response regression is mandatory
  download.py
  normalize.py
  audit.py

research/specs/round-4/
  DATA_ACQUISITION_CONTRACT.md
  PROVIDER_POLICY.md
```

### Registry row (CSV or YAML)

```text
dataset_id,asset_class,instrument,venue,provider,frequency,timezone,candle_label,adjusted,start,end,status,license_note,recipe_path,manifest_path
```

Example IDs:

```text
DATA-CRYPTO-BTCUSD-COINBASE-1H-001
DATA-CRYPTO-BTCUSDT-BINANCE-1H-001
DATA-CRYPTO-CROSSSECTION-DAILY-001
DATA-ETF-GTAA-DAILY-001
```

### Recipe requirements (committed)

- Source URL / API base  
- Symbol mapping  
- Fixed request parameters  
- Pagination + resume  
- Rate limit + exponential backoff + jitter  
- Max retries (bounded)  
- Empty-result = hard fail (no empty DataFrame downstream)  
- Expected schema  
- TZ + candle-label policy  
- Raw/normalized paths  
- Validation rules  
- Terms/license note  

### Manifest requirements (committed per retrieval)

```json
{
  "dataset_id": "...",
  "provider": "...",
  "retrieved_at_utc": "...",
  "raw_file_sha256": "...",
  "normalized_file_sha256": "...",
  "instrument": "...",
  "venue": "...",
  "frequency": "...",
  "timezone": "UTC",
  "candle_label": "open-time",
  "adjusted": null,
  "start": "...",
  "end": "...",
  "row_count": 0,
  "missing_intervals": [],
  "query_parameters": {},
  "rate_limit_events": 0,
  "known_limitations": [],
  "license_note": "..."
}
```

For **pre-existing** Round-1/3 caches: do **not** invent original `retrieved_at`. State original Yahoo retrieval timestamp **unknown** (BTC `.002` pattern).

### QA gates (dataset not experiment-eligible until all pass)

- Duplicate timestamps  
- Monotonic index  
- TZ awareness  
- Expected cadence / gap report  
- Zero/negative prices  
- Extreme returns  
- Split/adjustment discontinuities  
- First/last valid by symbol  
- Membership timeline (cross-section)  
- Raw↔normalized hash link  
- Empty download rejected before any strategy code  
- Cross-provider spot check where feasible  

### Regression that must exist

Yahoo/empty download → **controlled acquisition error** before cohort/date logic.  
The Round-3 crypto `.001` empty-DF crash is the failure mode this prevents.

---

## 5. Execution order (next session)

1. Read this handoff + Round-3 reviews for BTC/crypto `.002`.  
2. Confirm tip/branch; create `research/data-acquisition-round-4` from current tip (or `e85d5e0` if handoff not yet merged — prefer tip that contains this file).  
3. Inventory local caches (Round-1 crypto prices, BTC hourly archive, vault Round-1 scratchpads) — **no network yet**.  
4. Implement provider interface, empty-response tests, rate limiter, resume, quarantine.  
5. Acquire **EFA + GSG** (+ SPY/IEF/VNQ if missing) with a **second-source cross-check**.  
6. Acquire venue-specific BTC hourly (Gemini preferred; Bitfinex/Coinbase/Kraken/Binance robustness; Yahoo secondary).  
7. Build crypto membership/listing metadata inventory before proposing a less survivorship-biased universe.  
8. Only after specs frozen: mint **new** experiment IDs (never edit `.002`).  
9. Independent review of Round-3 `.002` before any vault `experimented` promotion.  
10. Secrets only via env; never commit keys, tokens, or raw dumps by default.

---

## 6. Hard stops

1. Do **not** modify Round-3 `.002` runners, configs, metrics, trades, or reviews.  
2. Do **not** promote vault to `experimented` / E2 strategy-level without a **separate** reviewer.  
3. Do **not** set `reviewer_status: approved` from the same agent that wrote the runner.  
4. Do **not** overwrite source-reported Sharpes with local Sharpes.  
5. Do **not** substitute GLD/DBC for EFA/GSG under asset-trend `.001` or any “same ID” continuation.  
6. Do **not** swarm Yahoo ticker-by-ticker without backoff; one bounded worker at a time.  
7. Do **not** forward-fill prices or silently drop assets without a manifest note.  
8. Do **not** claim crypto `.002` is paper reproduction.  
9. Do **not** commit raw vendor data unless license explicitly allows and a deliberate exception is documented.  
10. Do **not** blend BTCUSD and BTCUSDT (or venues) inside one “faithful” claim.

---

## 7. Suggested next-session prompt (paste-ready)

```text
Continue from awesome-systematic-trading branch research/validation-round-3
(or research/data-acquisition-round-4 if already created).

Read first:
  research/HANDOFF-2026-08-02-ROUND4-DATA.md

Frozen Round-3 anchors:
  tip lineage through e85d5e091e7b9483b42d1ae88a46a619298a8bdf (crypto .002 outputs)
  harness baseline 35e0ac0
  source freeze S 8104683
  provenance stamp P 2fcd741
  BTC outputs ebab7bf
  both .002 validators OK; harness 25/25
  both reviewer_status pending (integrator audit only)
  vault strategies researched/E1; experimented empty; do not promote
  asset-trend .001 blocked (missing EFA/GSG); no GLD/DBC swap
  raw caches gitignored; SHA:
    BTC 417e6b4a96c0b2c31daca1905eeae56b5789a11e90f55b57df8284d0bfd4ce72
    Crypto 84a1db1b2e703dc4fb12b664d058024e3e440fb7c61296fa5f71686317d68a57

Round-4 goals:
1) Independent review of frozen BTC + crypto .002 without modifying runners/outputs.
2) Build provider-agnostic, resumable, rate-limited free-data acquisition layer:
   immutable raw files, SHA-256 manifests, UTC + candle-label semantics,
   empty-response guards, gap reports, quarantine, no silent substitutions.
3) Inventory local caches before network.
4) Acquire EFA/GSG (+ SPY/IEF/VNQ) with second-source cross-check for asset-trend unblock.
5) Acquire venue-specific BTC hourly (Gemini first; Bitfinex/Coinbase/Kraken/Binance robustness; Yahoo secondary only).
6) Inventory crypto listing/delisting metadata before a less survivorship-biased universe.
7) Yahoo allowed but not sole dependency; bounded retries + backoff; never empty-DF crash.
8) No secrets in git. No vault promotion. No Round-3 artifact mutation.
9) New data or methodology ⇒ new experiment IDs only after specs are frozen.
```

---

## 8. What “done” looks like for early Round-4

- [ ] New branch cut from frozen tip  
- [ ] Data registry + recipe/manifest schemas committed  
- [ ] Empty-response + rate-limit tests green  
- [ ] Local cache inventory written  
- [ ] EFA/GSG (and full GTAA five) acquired + QA report  
- [ ] At least one venue BTC 1h history longer/cleaner than Yahoo 730d proxy  
- [ ] Independent review notes filed for both `.002`s (approve artifact or list defects)  
- [ ] Still no vault `experimented` without that independent review  
- [ ] Still no edits under Round-3 experiment IDs  

---

*End of handoff. Round-3 research results are frozen. Round-4 is data governance + independent review first, experiments second.*
