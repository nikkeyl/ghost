---
description: "Notice consumers that must know hidden implementation details or
  bypass a module contract."
kind: passive
name: detect-leaky-abstraction
---

# Detect a leaky abstraction

During API, component, hook, or module changes, look for consumers
branching on internal representations, reaching into private state,
repeating hidden invariants, or adapting to consumer-specific flags in
shared interfaces.

Distinguish an intentional extension point from a leak using the actual
contract and callers. Report the exposed detail, dependent consumers,
and consequence. Escalate to `estimate-blast-radius` for a material
contract risk; use `refactor-without-behavior-change` only when
restructuring is authorized.
