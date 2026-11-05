---
name: clarify-engineering-task
description: Turn an ambiguous engineering request or symptom into a bounded
  contract with requirements, invariants, risks, and success criteria.
kind: active
---

# Clarify an engineering task

## Trigger

Use when the requested outcome, problem statement, source of truth,
success criteria, non-goals, or constraints are materially ambiguous;
when a symptom may be confused with its underlying problem; or when
different interpretations would lead to different implementations.

## Goal

Convert the request into an explicit, evidence-backed change contract
without inventing requirements or creating an unnecessary approval gate.

## Investigation / reasoning

1. Restate the requested outcome in observable terms and separate it
   from the reported symptom or proposed solution.

1. Extract required behavior, invariants, affected users or consumers,
   source of truth, constraints, and explicit non-goals.

1. Classify each statement as fact, assumption, hypothesis, decision, or
   risk. Identify which assumptions can be checked cheaply before
   implementation.

1. Define success and failure criteria, including relevant edge, error,
   accessibility, performance, security, and operational behavior.

1. Estimate blast radius and identify decisions that would materially
   change scope, compatibility, or reversibility.

1. Resolve ambiguities from repository evidence when possible. Ask the
   user only when the remaining ambiguity changes authority, scope, or
   an irreversible/consequential outcome.

## Decision rules

- Treat an explicit implementation request as authorization for that
  stated scope; clarification is for the contract, not a second
  permission gate.

- Do not turn a preferred implementation into a requirement unless the
  request or repository evidence establishes it.

- Preserve existing behavior and public contracts unless a behavior
  change is explicit or the current behavior is the identified defect.

- Prefer a discriminating check over a long speculative discussion.

- If multiple interpretations remain viable, state the alternatives,
  their consequences, and the smallest question that distinguishes them.

- Keep adjacent improvements and future design ideas as non-goals or
  follow-up items rather than silently expanding the task.

## Actions

Produce a task contract with:

- desired outcome and problem statement;
- observable requirements and invariants;
- source of truth and affected consumers;
- assumptions, unknowns, hypotheses, and risks;
- success, failure, and non-goal criteria;
- bounded implementation scope and any required user decision;
- verification evidence that would support the completion claim.

Use the repository's terminology and link each material claim to
evidence when the task is based on existing behavior.

When a persistent requirements artifact is needed, use
`.agents/templates/requirements.md` and the repository's planning
location. Related tickets provide context, not automatic scope. Verify
existing or reusable capability claims before proposing a parallel
implementation.

## Verification

Check that the implementation plan can be evaluated against observable
criteria, that every requirement has a verification method, that
non-goals exclude the likely adjacent work, and that no unresolved
ambiguity can change the selected implementation without being surfaced.

## Completion criteria

The task has a bounded contract, explicit invariants and non-goals,
named unknowns and risks, and a verification plan. Any remaining user
question is small, consequential, and clearly phrased.

## Graph

```yaml
requires: [plan-code-change]
may-trigger: [estimate-blast-radius]
followed-by: [implement-minimal-change, verify-before-claiming]
```
