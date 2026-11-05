---
name: detect-async-race
description: Detect stale asynchronous UI updates, missing cancellation, and
  freshness or loading contracts in user-driven requests.
kind: passive
---

# Detect async race risk

Run alongside search, filtering, load-more, modal data fetching, or
other user-driven asynchronous work.

Look for high-frequency input without debounce, obsolete requests
without cancellation, responses applied without an identity or freshness
check, and intentional cancellation treated as a user-visible failure.
Check whether freshness and caching choices match the business contract.

Report a signal with the suspected ordering or resource problem and the
narrowest useful verification. Do not demand cancellation when the
operation is idempotent, cheap, and cannot produce a stale state.
