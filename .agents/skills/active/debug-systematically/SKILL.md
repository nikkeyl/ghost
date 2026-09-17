---
name: debug-systematically
description: Investigate failures and regressions by reproducing behavior, testing hypotheses, and identifying the violated invariant.
kind: active
---

# Debug systematically

## Trigger

Use for a failure, regression, unexpected runtime behavior, flaky test, or
incorrect technical claim.

## Goal

Find a root cause supported by evidence rather than guessing and patching
symptoms.

## Investigation / reasoning

1. Reproduce the problem and capture the exact input, environment, output, and
   timing.
2. Separate observed facts from assumptions.
3. Form one or more falsifiable hypotheses.
4. Choose the smallest discriminating experiment for each hypothesis.
5. Trace the relevant data flow, control flow, browser lifecycle, network
   request, cache, or state propagation.
6. Identify the violated invariant or boundary.

## Decision rules

- Do not patch a symptom before a hypothesis explains the observed behavior.
- Prefer a small experiment that distinguishes competing hypotheses over broad
  speculative changes.
- Treat cancellation, stale state, cache behavior, and environment differences
  as separate possible causes until evidence connects them.
- Keep unrelated cleanup out of the fix.

## Actions

Apply the smallest fix that restores the invariant. Avoid unrelated cleanup.
If a hypothesis fails, discard it explicitly rather than bending the evidence.

## Verification

Reproduce the original failure, run the regression check, and test the most
important adjacent edge case. State what was not tested.

## Completion criteria

The root cause explains the observed behavior, the fix addresses that cause,
and the original failure no longer reproduces under the stated conditions.

## Graph

```yaml
requires: [understand-and-plan-change]
may-trigger: [analyze-change-impact]
followed-by: [verify-change]
```
