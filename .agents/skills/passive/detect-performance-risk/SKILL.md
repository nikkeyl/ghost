---
name: detect-performance-risk
kind: passive
---

# Detect performance risk

Run alongside UI, data-loading, media, or rendering changes. Look for new
client work, repeated allocations in hot paths, unbounded lists, blocking
resources, large assets, forced layout, unnecessary effects, cache invalidation
expansion, or work moved above the first useful render.

Raise a hypothesis, not a verdict: include the suspected mechanism and the
measurement needed. Escalate to a performance diagnosis only when impact is
plausible and measurable.
