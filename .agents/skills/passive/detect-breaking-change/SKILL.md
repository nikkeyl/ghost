---
description: Detect incompatible changes to public types, props, routes,
  schemas, configuration, serialization, or behavior.
kind: passive
name: detect-breaking-change
---

# Detect breaking change

Run when a public type, prop, route, exported symbol, schema, config, or
behavior changes. Compare before/after contracts and enumerate known
consumers. Raise a signal for removed/narrowed fields, changed defaults,
incompatible serialization, changed keyboard semantics, or
migration-free state changes.

Do not decide that a change is breaking from naming alone. Escalate
material signals to `estimate-blast-radius`.
