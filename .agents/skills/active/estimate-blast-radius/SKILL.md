---
name: estimate-blast-radius
description: Analyze the blast radius of shared, public, data-flow, configuration,
  routing, security, and cross-cutting changes.
kind: active
---

# Estimate blast radius

## Trigger

Use when a change touches a public contract, shared component, data
flow, configuration, routing, security boundary, or cross-cutting
concern.

## Goal

Predict what can break and reduce surprises before implementation.

## Investigation / reasoning

1. Identify the changed contract and its consumers.

1. Trace data flow and control flow from the entry point to side
   effects.

1. Search for tests, schemas, generated types, adapters, and
   documentation that encode the existing behavior.

1. Enumerate direct consumers and follow shared dependencies to
   indirect consumers, routes, packages, environments, and deployments
   when relevant. Separate known affected paths from plausible paths
   and explain where dynamic behavior limits enumeration.

1. Classify effects as compile-time, runtime, visual, accessibility,
   performance, security, operational, and migration impact.

1. Compare the proposed change with repository conventions and supported
   browser/runtime versions.

## Decision rules

- Treat shared code as high blast radius until consumers are enumerated.

- Treat a renamed, narrowed, removed, or newly required field as a
  potential breaking change.

- Prefer compatibility layers or staged migration when consumers cannot
  move atomically.

- Do not infer safety from a passing unit test if the risk is
  integration, browser, network, or operational.

## Actions

Write an impact map: owner → contract → consumers → failure mode →
mitigation → verification. Keep unrelated refactors out of the
implementation.

For a contract or configuration transition, also map readers/writers,
the compatibility window, preserved state, recovery owner, and rollback
limits. Route material overlap or recovery needs to `plan-migration`.

## Verification

Check that the highest-severity risks have a concrete test, inspection,
or rollback step, and that the proposed diff matches the impact map.

## Completion criteria

The estimate names affected consumers and propagation paths, ranks
material consequences, and records uncertainty or excluded areas. It
does not present an incomplete consumer search as a guarantee of safety.

## Graph

```yaml
requires: [plan-code-change]
may-trigger: [debug-systematically, plan-migration]
followed-by: [implement-minimal-change, verify-before-claiming]
```
