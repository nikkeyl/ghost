---
name: plan-migration
description: "Plan staged API, component, state, dependency, or configuration
  changes with compatibility, recovery, and preservation evidence."
kind: active
---

# Plan a migration

## Trigger

Use when contracts or persistent state must change across consumers,
versions, deployments, or configuration boundaries that cannot safely
move atomically.

## Goal

Define a bounded transition with explicit compatibility and recovery
conditions.

## Investigation / reasoning

1. Map current readers, writers, consumers, versions, data, and
   operational owners.

1. Identify the overlap window and which old/new combinations must
   remain valid.

1. Define the forward path, restart behavior, preserved invariants, and
   rollback or recovery path. Read
   `.agents/knowledge/behavior-preservation-and-migration.md`.

1. Sequence expand, migrate, verify, and contract where appropriate.
   Give each stage its own entry conditions, evidence, and stop
   condition.

1. Define how partial failure is detected and retries avoid duplicate
   effects.

1. State when rollback becomes impossible and what recovery then
   requires.

## Decision rules

- Planning does not authorize deployment, data mutation, or destructive
  cleanup. Apply only the stage and effects included in the user's
  authorization.

- Validate both old and new consumers during the required compatibility
  window. Removing an old path needs evidence that its consumers have
  migrated.

- A backup alone is not a rollback plan; name how restoration or forward
  recovery is verified and who owns it.

- Do not promise reversibility after irreversible external effects or
  data loss.

## Actions

Use `.agents/templates/migration-plan.md` to record stages, consumer
matrix, ownership, observability, preservation proof, rollback triggers,
and recovery steps. For an authorized implementation, route to
`implement-minimal-change` for the selected stage and checkpoint before
further contraction.

## Verification

Check the plan against actual consumers and configuration. Ensure each
stage has evidence that can detect loss or incompatibility, and recovery
is feasible under its stated assumptions. Report untested recovery
explicitly.

## Completion criteria

The requested transition stage is defined, compatibility and recovery
have named evidence, and later destructive stages are not implicitly
authorized.

## Graph

```yaml
requires: [analyze-change-impact]
may-trigger: [design-test-strategy]
followed-by: [implement-minimal-change, verify-change]
```
