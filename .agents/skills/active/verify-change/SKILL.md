---
name: verify-change
description: Verify an implemented change with risk-appropriate evidence and keep
  completion claims within what was actually checked.
kind: active
---

# Verify a change

## Trigger

Use after implementation, debugging, configuration changes, or any
report that claims completion.

## Goal

Establish what is actually verified and prevent false completion claims.

## Investigation / reasoning

1. Read the diff and compare it with the requested contract and plan.

1. Select checks by risk: type/build, unit/integration, browser
   behavior, accessibility, performance, security, migration, or
   operational recovery.

1. Run the narrowest useful checks first, then expand only when evidence
   justifies it.

1. Inspect outputs for warnings, skipped tests, environment assumptions,
   and generated-file changes.

1. Compare the plan with the implementation: mark each planned unit as
   implemented, intentionally changed, omitted, or blocked; identify
   every unplanned changed path; and challenge at least the material
   assumptions or edge cases that could falsify the result.

## Verification ladder

Do not build the entire project after every change. A full build is
expensive and often adds no evidence for a local change.

Use the narrowest check that can falsify the relevant failure mode:

1. diff and affected-file inspection;

1. formatter, linter, or focused type check;

1. focused unit, integration, browser, or accessibility test;

1. package or application build only when the change crosses a
   build/runtime boundary or a lower-level check cannot cover the risk;

1. full release-level build when explicitly requested or when release,
   deployment, dependency, routing, environment, generated-output, or
   server/client-boundary risk makes it necessary.

## Decision rules

- A check is evidence only for the behavior it actually exercises.

- A successful type check does not prove browser, UX, performance, or
  security correctness.

- Linting is useful evidence for style and selected static rules, but it
  does not replace an explicit TypeScript check when type correctness
  matters.

- Verification depth may be proportional to project size, delivery
  constraints, and business risk, but a shorter verification path must
  still cover the material failure modes.

- For deterministic regex, validation, and transformation utilities,
  focused unit tests covering valid, invalid, and edge cases are
  sufficient unless the change also affects packaging, runtime
  integration, or generated output.

- Disabling type checking during a production build is a delivery
  trade-off, not evidence that the code is type-correct or otherwise
  verified.

- Do not run a full project build by habit or use it as a generic
  substitute for choosing the relevant check.

- Escalate to a full build when the change affects build configuration,
  dependency resolution, bundling, routing, environment variables,
  generated artifacts, server/client boundaries, or release behavior.

- If a full build was not run, state that explicitly; this is not a
  failure when the selected checks adequately cover the changed risk.

- If a required check cannot run, report the blocker and its
  consequence.

- Never replace missing verification with confidence or code inspection
  alone.

- A plan-versus-implementation review is evidence of scope alignment,
  not proof that runtime behavior is correct. Verify the changed
  behavior with the narrowest check that can falsify its material
  failure modes.

- Bind reused results to the repository state, configuration, and
  environment they exercised. New relevant edits invalidate old
  completion evidence.

- Preserve failed attempts and distinguish pass, fail, skipped,
  unavailable, and blocked. Retrying a flaky check does not erase its
  earlier failure.

- Once sufficient evidence covers acceptance, stop; do not add unrelated
  cleanup or repeatedly broaden checks without a new risk or failure.

## Actions

Produce a verification record: command or method, result, scope covered,
plan-versus-implementation status, challenged assumptions or
counterexamples, remaining uncertainty, and follow-up.

Use `.agents/templates/verification-record.md` when a persistent record
is needed. Use `design-test-strategy` when a material failure mode has
no clear proof; keep structural validation distinct from a real runtime
trial.

## Verification

Check that the verification record matches the actual commands or
observations, that every planned unit and unplanned path is accounted
for, skipped checks are named, and the completion claim does not exceed
the evidence.

## Completion criteria

The claim of completion is no broader than the evidence, and all
material risks are either checked, mitigated, or explicitly left open.

## Graph

```yaml
requires: [implement-minimal-change]
may-trigger: [design-test-strategy]
references: [analyze-change-impact]
followed-by: []
```
