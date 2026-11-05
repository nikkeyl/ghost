---
name: refactor-without-behavior-change
description:
  "Change code structure while preserving observable behavior, public interfaces,
  ordering, and failure semantics."
kind: active
---

# Refactor without behavior change

## Trigger

Use for an authorized extraction, consolidation, ownership move, or structural
simplification.

## Goal

Improve the requested structure with evidence that the behavior-preservation boundary
holds.

## Investigation / reasoning

1. Define what must remain stable, including callers, outputs, errors, state,
   ordering, and side effects. Record existing defects separately.
2. Establish checks for those invariants on the current state.
3. Locate the owner of the responsibility and the smallest useful sequence of moves.
   Keep intermediate states runnable.
4. Read `.agents/knowledge/behavior-preservation-and-migration.md` when the change
   crosses ownership or compatibility boundaries.

## Decision rules

- Separate intentional behavior changes from structural work; report any discovered
  behavior difference before calling it a refactor.
- Do not equate fewer lines with lower complexity. Prefer clear ownership, fewer
  competing sources of truth, and a smaller public surface.
- Preserve unrelated user changes. Avoid dependency or configuration growth unless
  the behavior-preservation contract requires it.
- A move that affects consumers unable to update together is a migration; use
  `plan-migration` rather than assuming atomic compatibility.

## Actions

Move one responsibility boundary at a time within the authorized scope. Re-run the
baseline checks after material moves and record deviations. Checkpointing does not
require stopping after every file.

## Verification

Compare the same pre- and post-change evidence and inspect public exports, failure
behavior, ordering, and affected consumers. Explain any baseline failure.

## Completion criteria

The intended structure is achieved and behavior matches the stated preservation
boundary.

## Graph

```yaml
may-trigger: [analyze-change-impact, design-test-strategy, plan-migration]
followed-by: [verify-change]
```
