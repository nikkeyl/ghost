---
description: Strengthen existing tests so they fail for a violated behavior
  contract and pass for a correct implementation without hiding failures.
kind: active
name: improve-test-signal
---

# Improve test signal

## Trigger

Use when existing tests can pass despite a relevant defect, assertions
are misleading, or mocks, snapshots, setup, or retries hide the failure.
An absent test strategy belongs to `design-test-strategy`.

## Goal

Improve the tests' ability to detect a specific incorrect behavior while
keeping them independent of incidental implementation details.

## Investigation / reasoning

1. Name the behavior contract and a realistic violation. Inspect the
   current test, setup, assertions, doubles, and observed execution.

1. Explain why the test could pass for the violation or fail for an
   unrelated reason. Trace the actual boundary exercised by the test.

1. Choose the smallest meaningful correction: observable assertion,
   representative input, proper async completion, restored integration
   boundary, or isolated setup. Do not expand infrastructure by habit.

1. Define a controlled negative case using the original defect, an
   isolated temporary mutation, or another bounded counterexample.
   Preserve unrelated changes and remove temporary mutations afterward.

## Decision rules

- Setup failures, syntax errors, and an assertion that always fails are
  not evidence that the test detects the intended defect.

- Keep useful controlled doubles; replace only those bypassing the
  contract under test. A broader integration test needs a boundary risk.

- A request to assess tests produces a diagnosis and proposed changes.
  A request to improve them authorizes scoped test edits, not production
  refactoring or deletion of inconvenient failures.

## Actions

Apply the authorized assertion or fixture change, explain the behavior
it distinguishes, and record before/after test results. For analysis
alone, provide the precise correction and negative case without edits.
Do not hide intermittent failures behind retries.

## Verification

Run the focused test against the correct implementation and verify it
fails for the intended violation when feasible. Inspect the failure
reason, restore temporary changes, and rerun the final state. If the
negative case cannot run, state the limitation and weaker evidence.

## Completion criteria

The revised test distinguishes the named behavior from its violation,
passes on the intended implementation, and adds no unrelated coupling.
If changes or counterexample execution were out of scope, report only
the assessment completed rather than an implemented improvement.

## Graph

```yaml
may-trigger: [debug-systematically, design-test-strategy]
references: [verify-before-claiming]
```
