---
name: understand-and-plan-change
description: Build a bounded context model and implementation plan before changing
  code or architecture.
kind: active
---

# Understand and plan a change

## Trigger

Use when a request changes code, architecture, public behavior, or more
than one isolated file.

## Goal

Build a small context model and an implementation sequence before
editing.

## Investigation / reasoning

1. Restate the desired outcome and non-goals.

1. Locate the relevant entry points, contracts, tests, generated files,
   and repository conventions.

1. Identify the smallest unit that can satisfy the request.

1. Trace inputs, outputs, side effects, and ownership boundaries.

1. Record facts, assumptions, hypotheses, constraints, and open risks.

1. Estimate blast radius and list adjacent work that is explicitly out
   of scope.

1. Route the task to the smallest existing parent skill that covers its
   dominant capability and risk. Use `clarify-engineering-task` when the
   contract is materially ambiguous and `understand-codebase` when
   repository ownership or boundaries are not established. Inspect the
   candidate backlog for coverage, but do not activate every matching
   leaf procedure.

For work handed to a fresh session, use
`.agents/templates/requirements.md` and
`.agents/templates/implementation-plan.md` as needed. Keep the desired
behavior separate from the selected implementation, record dependency
order, and give each runnable unit a completion check. A source snapshot
or prior plan supplies leads whose drift-prone facts need rechecking.

Choose `review-code-change` for a review;
`refactor-without-behavior-change` for structural work; `plan-migration`
for overlapping contracts; `research-unknown-api` for material API
uncertainty; and `design-test-strategy` when the proof is unclear.
`analyze-build-pipeline` handles automation, hooks, and release contracts.
`update-documentation`, `write-maintainer-notes`, and
`extract-engineering-lessons` handle requested artifacts or guidance.
Select these conditionally, never as a full checklist to preload.

## Decision rules

- Do not design an abstraction before the variation is visible.

- Prefer an existing extension point over a new parallel mechanism.

- Prefer a parent skill or checklist that covers several related
  candidates over creating or activating a separate skill for each
  narrow procedure.

- Activate no more than five active skills by default and traverse no
  more than two related skills. Expand only when investigation exposes a
  material risk or contract that the current set cannot cover.

- Keep passive detectors lightweight; escalate to an active skill only
  when the detector produces a material signal.

- If multiple units are independent, order them by dependency and risk.

- Ask for user input only when scope, authority, or an irreversible
  decision is materially ambiguous. An explicit implementation request
  is already approval for the specified scope.

## Actions

Produce a concise plan with units, changed paths, expected contract,
risks, and verification. Do not write speculative adjacent code.

## Verification

Confirm that every planned unit maps to a concrete file or behavior and
that the plan has a clear completion check.

## Completion criteria

The plan is small enough to review, distinguishes facts from
assumptions, and can be executed without rediscovering the repository
structure.

## Graph

```yaml
may-trigger:
  [
    clarify-engineering-task,
    understand-codebase,
    analyze-change-impact,
    review-code-change,
    design-test-strategy,
    refactor-without-behavior-change,
    plan-migration,
    research-unknown-api,
    analyze-build-pipeline,
    update-documentation,
    write-maintainer-notes,
    extract-engineering-lessons,
  ]
followed-by: [implement-minimal-change]
references: [verify-change]
```
