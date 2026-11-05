---
name: design-test-strategy
description:
  "Choose focused automated or manual checks for changed behavior,
  regression risk, and affected boundaries."
kind: active
---

# Design a test strategy

## Trigger

Use when the verification plan is unclear, a regression needs proof, or
existing tests do not exercise a material failure mode.

## Goal

Map acceptance criteria and failure modes to the smallest sufficient
evidence.

## Investigation / reasoning

1. Name the behavior, affected boundary, relevant consumers, and failure
   cost.

1. Inspect current tests and baseline failures before adding new
   infrastructure.

1. Choose the lowest level that exercises the mechanism. Add
   integration, browser, or manual checks when lower levels cannot cover
   the boundary.

1. Include the relevant success, error, edge, and concurrency paths;
   prefer observable results over implementation details.

1. For a regression, show the check fails for the original defect when
   feasible. Inspect why it fails, then verify the corrected state with
   the same check.

1. Check whether mocks bypass the boundary under test, assertions are
   weak, or retries and snapshots hide the original failure.

## Decision rules

- TDD is a useful technique, not a universal gate for documentation,
  styling, exploratory prototypes, or other changes where it adds no
  relevant proof.

- Avoid tests that mirror the implementation, assert incidental wording,
  or add infrastructure without a demonstrated verification need.

- A test failing from setup or syntax does not prove it detects the
  defect. Explain when pre-fix execution is unavailable and what
  evidence replaces it.

- Mocks are appropriate for controlled boundaries; they cannot prove the
  real integration works. Test that integration separately when it
  carries risk.

- A retry may classify an intermittent failure; it must not erase a
  failed attempt or silently turn it into a clean pass.

- Use affected-project checks only after confirming the base and
  affected set. Preserve repository settings for cache and workers
  unless the task needs a change.

## Actions

Produce a requirement-to-check map, baseline, expected failure/pass
signals, execution order, and residual risk. Use
`.agents/templates/manual-test.md` for human checks and
`.agents/templates/verification-record.md` for results. Run checks or
implement tests only within the authorized task.

## Verification

Check that the chosen evidence can falsify the important failure modes,
that the actual assertions exercise them, and that skips, failures, and
unavailable checks remain visible.

## Completion criteria

Every material acceptance criterion has proportionate evidence or an
explicit limitation; extra tests and broad builds have a task-relevant
reason.

## Graph

```yaml
may-trigger: [debug-systematically]
followed-by: [verify-change]
```
