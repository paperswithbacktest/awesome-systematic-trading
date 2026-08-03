# GTAA Local-Cache Gap — 2026-08-02

## Finding

The pre-network Round-4 inventory confirms that the local asset-trend caches contain:

- `SPY`
- `IEF`
- `VNQ`
- `GLD`
- `DBC`

They do **not** contain:

- `EFA`
- `GSG`

The inventory also confirms the frozen Round-3 input hashes:

- BTC hourly `.002`: `417e6b4a96c0b2c31daca1905eeae56b5789a11e90f55b57df8284d0bfd4ce72`
- Crypto daily `.002`: `84a1db1b2e703dc4fb12b664d058024e3e440fb7c61296fa5f71686317d68a57`

## Consequence

Round-3 asset-trend `.001` remains blocked. `GLD` and `DBC` are not substitutes for `EFA` and `GSG`, and they must not be used to revive or relabel that experiment.

Round 4 must acquire and QA the complete frozen GTAA universe—`SPY`, `EFA`, `IEF`, `VNQ`, and `GSG`—under a new dataset ID. A new asset-trend experiment ID may be minted only after the data recipes, manifests, adjustment semantics, cross-source checks, and experiment spec are frozen.

## Scope note

`local-cache-inventory-2026-08-02.{json,md}` is a hash and coverage inventory of the selected local cache/backtest-artifact roots. It is **not** a normalized market-data manifest and does not establish provider, adjustment, session-close, timezone, license, or original retrieval-time semantics. Those fields remain unknown until separately evidenced; the inventory deliberately records `retrieved_at_utc: null`.
