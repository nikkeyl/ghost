---
description: Detect values, closures, derived state, caches, or asynchronous
  results that no longer match their current source of truth.
kind: passive
name: detect-stale-state
---

# Detect stale state

Run during changes to state, props, effects, subscriptions, cached data,
entity identity, or asynchronous UI work. Identify the authoritative
value, when a snapshot was captured, and which update should invalidate
or replace it.

Look for copied props that stop tracking their source, derived values
stored without a synchronization contract, callbacks or subscriptions
reading obsolete snapshots, state retained after an entity changes, and
optimistic or cached values not reconciled with authoritative results.
For requests, check response identity, ordering, invalidation, and
whether an obsolete result can replace newer data.

A deliberate historical snapshot, uncontrolled initial value, or stale
cache with an explicit freshness contract is not automatically a bug.
Missing debounce or cancellation alone does not prove stale state.

Report the source of truth, obsolete value, triggering sequence, and
user-visible consequence. Escalate to `debug-systematically` for a
material mismatch or `design-test-strategy` for an unproven transition.
Emit no material signal when ownership and freshness are intentional.
