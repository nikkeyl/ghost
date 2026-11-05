---
name: detect-performance-risk
description: Detect plausible performance regressions from client work, data
  loading, rendering, assets, effects, caching, or critical-path
  expansion.
kind: passive
---

# Detect performance risk

Run alongside UI, data-loading, media, or rendering changes. Look for
new client work, route-specific data or dependencies loaded from global
boundaries, repeated allocations in hot paths, unbounded lists, blocking
resources, large assets, forced layout, unnecessary effects, cache
invalidation expansion, uncached reads without a freshness requirement,
high-frequency requests without debounce, or work moved above the first
useful render.

Raise a hypothesis, not a verdict: include the suspected mechanism and
the measurement needed. Escalate to a performance diagnosis only when
impact is plausible and measurable.

For images, check whether intrinsic dimensions or an aspect ratio
reserve layout space, responsive source selection matches the rendered
slot, and offscreen content is deferred without delaying an initially
visible critical image. Treat elevated fetch priority as a scarce hint,
not a default for every large image. For animated controls, treat
transform, will-change, or a library choice as hypotheses; verify layout
movement and frame cost on the target device rather than inferring
performance from the property name.
