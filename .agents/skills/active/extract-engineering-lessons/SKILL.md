---
name: extract-engineering-lessons
description: "Turn a demonstrated failure or user correction into a scoped,
  evidence-backed proposal for durable engineering guidance."
kind: active
---

# Extract engineering lessons

## Trigger

Use when the user requests durable guidance from a correction,
investigation, or completed change. A correction alone is a signal to
offer capture at a natural breakpoint, not authorization to rewrite
persistent guidance.

## Goal

Preserve a useful general lesson without turning one incident into an
unconditional rule.

## Investigation / reasoning

1. Identify the observed outcome, violated assumption, causal evidence,
   and circumstances in which the lesson should apply.

1. Separate a persistent principle from a project convention, personal
   preference, temporary state, or unsupported inference.

1. Find the existing owner: rule, parent procedure, knowledge, project
   document, or explicit user preference. Prefer a narrow amendment over
   a parallel copy.

1. Read `.agents/knowledge/skill-authoring-and-evaluation.md`; consider
   a counterexample and how to test the proposed trigger and result.

## Decision rules

- Finish the current authorized task before proposing unrelated
  persistent work.

- Apply a guidance change only within explicit user authorization.
  Existing authorization for the concrete change does not need a second
  approval gate.

- Do not silently modify user-level memory, settings, or another
  repository. A proposed destination must respect its access and
  ownership constraints.

- State exceptions and evidence that would revise the lesson. Avoid
  catchall triggers, mandatory tool brands, and arbitrary thresholds.

## Actions

Present or apply the scoped guidance change as authorized, with source
evidence, intended behavior, boundary, and verification. Update the
relevant index and coverage record when a capability's routing changes.

## Verification

Check the positive case, a plausible non-trigger or counterexample, and
whether the revised guidance preserves existing contracts. Separate
structural checks from behavioral trials.

## Completion criteria

The lesson has an appropriate owner and bounded applicability; the
report clearly distinguishes proposed, implemented, and behaviorally
trialled guidance.

## Graph

```yaml
references: [update-documentation, verify-change]
```
