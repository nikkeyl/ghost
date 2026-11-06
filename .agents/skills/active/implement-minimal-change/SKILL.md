---
name: implement-minimal-change
description: Implement an authorized change as the smallest coherent diff while
  preserving existing contracts and local conventions.
kind: active
---

# Implement a minimal change

## Trigger

Use after scope and impact are understood and the request authorizes the
implementation.

## Goal

Change only the smallest coherent unit that satisfies the contract.

## Investigation / reasoning

1. Re-read the target file and its local conventions immediately before
   editing.

1. Check the effective formatter and linter rules against
   `.agents/rules/00-operating-principles.md`: function form, quotes,
   statement spacing, naming, and explicit repository exceptions. Do not
   assume a successful formatter run enforces every style convention.

1. Select the narrowest extension point.

1. Preserve existing naming, exports, error behavior, and public
   contracts unless the plan explicitly changes them.

1. Prefer composition and local configuration over flags, duplication,
   or a new global abstraction.

1. Keep framework-specific behavior at the smallest boundary that needs
   it.

## Decision rules

- Implement only what the authorized contract requires; record adjacent
  ideas as follow-up work.

- Start with the minimum necessary code, structure, state, dependencies,
  and component props. Expand the implementation only when the contract
  or demonstrated complexity requires it.

- Prefer an existing stable extension point over a new abstraction.

- For a non-trivial capability, prefer a known and maintained package
  over a bespoke implementation when it fits the repository's
  constraints. Do not add a package for small, stable behavior already
  covered by the platform, standard library, or existing project
  utilities.

- Use a typed map or lookup table for finite data mappings, variants,
  and strategies when the behavior is data. Keep `if` for control flow,
  predicates, sequencing, or dependent behavior.

- Prefer `??` for nullish defaults and reserve `||` for intentional
  falsy coalescing. Use a ternary for a short value choice, a block `if`
  for multi-step behavior, and do not introduce `switch`/`case`.

- Keep one-use domain logic near its owner and promote it only after
  real reuse or an explicitly stable cross-domain contract appears.

- Preserve externally observable behavior during a refactor. If behavior
  must change, make that change explicit in the plan and verification.

- Keep a coherent outcome across the layers that own its invariants; the
  narrowest responsible fix is not necessarily the smallest file edit.

- Use `refactor-without-behavior-change` when preservation needs an
  explicit baseline, and `plan-migration` for non-atomic consumer or
  state transitions.

## Actions

Implement one isolated unit. After the edit, report changed paths,
behavior, risk, and the next verification step before moving to another
independent unit. Record newly discovered adjacent work as follow-up
work.

## Verification

Run the narrowest relevant formatter, type check, lint, unit test, or
focused browser check. Inspect the diff for unrelated changes and
accidental contract drift.

## Completion criteria

The intended behavior exists, the diff is coherent and minimal, and the
next step is either verified or explicitly blocked by evidence.

## Graph

```yaml
requires: [plan-code-change]
may-trigger:
  [
    debug-systematically,
    refactor-without-behavior-change,
    plan-migration,
    design-test-strategy,
  ]
followed-by: [verify-before-claiming]
```
