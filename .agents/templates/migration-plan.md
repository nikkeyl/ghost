# Migration plan

## Scope, ownership, and preserved state

Record the authorized stage, readers/writers, consumers, versions, owners,
invariants, and effects that require separate authorization.

## Compatibility window

| Old/new combination | Required behavior | Evidence | Exit condition |
| ------------------- | ----------------- | -------- | -------------- |

## Transition stages

| Stage | Entry conditions | Action | Preservation check | Stop/exit condition |
| ----- | ---------------- | ------ | ------------------ | ------------------- |

Include expand, migrate, verify, and contract only where they fit the actual change.
Define restart behavior, retry semantics, and partial-failure signals.

## Recovery procedure

State rollback triggers, retained state, restoration or forward recovery steps,
owner, and recovery verification. Mark the irreversible boundary.

## Evidence and outstanding work

Record actual checks and untested recovery assumptions. Closing an overlap window
requires evidence of consumer migration, not just a new implementation.
