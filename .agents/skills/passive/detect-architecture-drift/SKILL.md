---
name: detect-architecture-drift
kind: passive
---

# Detect architecture drift

Run during changes that add folders, dependencies, shared abstractions, state,
or cross-layer imports. Look for duplicated ownership, upward/downward layer
violations, consumer-specific flags in shared components, speculative generic
types, and code that bypasses an existing boundary.

Report the violated convention and the smallest evidence-backed correction.
Escalate to `analyze-change-impact` or `review-component-anatomy` when the drift
changes a shared contract.
