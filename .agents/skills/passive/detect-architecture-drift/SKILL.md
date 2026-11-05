---
name: detect-architecture-drift
description: Detect ownership, layer, abstraction, state, and dependency changes
  that drift from the repository architecture.
kind: passive
---

# Detect architecture drift

Run during changes that add, rename, or move folders and files,
dependencies, shared abstractions, state, or cross-layer imports. Look
for duplicated ownership, upward/downward layer violations,
consumer-specific flags in shared components, speculative generic types,
code that bypasses an existing boundary, and path names that obscure
responsibility.

When the repository already uses FSD or an equivalent layer/slice
convention, also check whether layer groups, slices, and internal
segments follow the existing plural/singular and naming patterns. Do not
introduce this taxonomy into a repository that has not adopted it.

Flag a filename that repeats its parent domain or slice without a
concrete reason only when the repetition makes ownership, routing, or
change isolation less clear. Framework-required names, generated files,
public contracts, and files designed for relocation are explicit
exceptions.

Report the violated convention and the smallest evidence-backed
correction. Escalate to `estimate-blast-radius` or
`review-component-boundaries` when the drift changes a shared contract.
