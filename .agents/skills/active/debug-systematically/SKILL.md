---
name: debug-systematically
description: Investigate failures and regressions by reproducing behavior, testing
  hypotheses, and identifying the violated invariant.
kind: active
---

# Debug systematically

## Trigger

Use for a failure, regression, unexpected runtime behavior, flaky test,
or incorrect technical claim.

## Goal

Find a root cause supported by evidence rather than guessing and
patching symptoms.

## Investigation / reasoning

1. Reproduce the problem and capture the exact input, environment,
   output, and timing.

1. Separate observed facts from assumptions.

1. Form one or more falsifiable hypotheses.

1. Choose the smallest discriminating experiment for each hypothesis.

1. Trace the relevant data flow, control flow, browser lifecycle,
   network request, cache, or state propagation.

1. Identify the violated invariant or boundary.

1. Rank hypotheses by supporting evidence and the cost of a
   discriminating check. Compare with a working case where it can
   expose the relevant difference.

1. For multi-layer failures, capture inputs and outputs at the
   suspected boundary. Separate environment, timing, state, and
   implementation causes.

A diagnostic-only request ends with the cause and evidence; it does not
authorize a fix. If no cause can be established, report the precise
evidence gap instead of repeatedly trying unrelated edits.

## Decision rules

- Do not patch a symptom before a hypothesis explains the observed
  behavior.

- Prefer a small experiment that distinguishes competing hypotheses over
  broad speculative changes.

- Treat cancellation, stale state, cache behavior, and environment
  differences as separate possible causes until evidence connects them.

- Keep unrelated cleanup out of the fix.

## Actions

When implementation is authorized, apply the smallest fix that restores
the invariant. Avoid unrelated cleanup. If a hypothesis fails, discard
it explicitly rather than bending the evidence.

## Verification

For an authorized fix, exercise the original failure and regression
check, including the important adjacent edge case. Establish pre-fix
failure when feasible and explain alternative evidence when it is not.
For diagnosis alone, verify that the proposed mechanism explains the
observed evidence. State what was not tested.

## Completion criteria

The diagnosis explains the observed behavior or names the unresolved
evidence gap. When a fix is in scope, it addresses the cause and the
original failure no longer reproduces under the stated conditions.

## Graph

```yaml
requires: [plan-code-change]
may-trigger: [estimate-blast-radius, design-test-strategy, research-unknown-api]
followed-by: [verify-before-claiming]
```
