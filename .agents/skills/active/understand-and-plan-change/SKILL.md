---
name: understand-and-plan-change
kind: active
---

# Understand and plan a change

## Trigger

Use when a request changes code, architecture, public behavior, or more than
one isolated file.

## Goal

Build a small context model and an implementation sequence before editing.

## Investigation

1. Restate the desired outcome and non-goals.
2. Locate the relevant entry points, contracts, tests, generated files, and
   repository conventions.
3. Identify the smallest unit that can satisfy the request.
4. Trace inputs, outputs, side effects, and ownership boundaries.
5. Record facts, assumptions, hypotheses, constraints, and open risks.
6. Estimate blast radius and list adjacent work that is explicitly out of
   scope.

## Decision rules

- Do not design an abstraction before the variation is visible.
- Prefer an existing extension point over a new parallel mechanism.
- If multiple units are independent, order them by dependency and risk.
- Ask for user input only when scope, authority, or an irreversible decision is
  materially ambiguous. An explicit implementation request is already approval
  for the specified scope.

## Actions

Produce a concise plan with units, changed paths, expected contract, risks, and
verification. Do not write speculative adjacent code.

## Verification

Confirm that every planned unit maps to a concrete file or behavior and that
the plan has a clear completion check.

## Completion criteria

The plan is small enough to review, distinguishes facts from assumptions, and
can be executed without rediscovering the repository structure.

## Graph

```yaml
may-trigger: [analyze-change-impact]
followed-by: [implement-minimal-change]
references: [verify-change]
```
