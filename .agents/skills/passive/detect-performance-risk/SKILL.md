---
name: detect-performance-risk
description: Detect plausible performance regressions from client work, data loading, rendering, assets, effects, caching, or critical-path expansion.
kind: passive
---

# Detect performance risk

Run alongside UI, data-loading, media, or rendering changes. Look for new
client work, route-specific data or dependencies loaded from global boundaries,
repeated allocations in hot paths, unbounded lists, blocking resources, large
assets, forced layout, unnecessary effects, cache invalidation expansion,
uncached reads without a freshness requirement, high-frequency requests without
debounce, or work moved above the first useful render.

Raise a hypothesis, not a verdict: include the suspected mechanism and the
measurement needed. Escalate to a performance diagnosis only when impact is
plausible and measurable.
