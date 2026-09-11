---
name: verify-change
kind: active
---

# Verify a change

## Trigger

Use after implementation, debugging, configuration changes, or any report that
claims completion.

## Goal

Establish what is actually verified and prevent false completion claims.

## Investigation

1. Read the diff and compare it with the requested contract and plan.
2. Select checks by risk: type/build, unit/integration, browser behavior,
   accessibility, performance, security, migration, or operational recovery.
3. Run the narrowest useful checks first, then expand only when evidence
   justifies it.
4. Inspect outputs for warnings, skipped tests, environment assumptions, and
   generated-file changes.

## Decision rules

- A check is evidence only for the behavior it actually exercises.
- A successful type check does not prove browser, UX, performance, or security
  correctness.
- If a required check cannot run, report the blocker and its consequence.
- Never replace missing verification with confidence or code inspection alone.

## Actions

Produce a verification record: command or method, result, scope covered,
remaining uncertainty, and follow-up.

## Verification

Check that the verification record matches the actual commands or observations,
that skipped checks are named, and that the completion claim does not exceed
the evidence.

## Completion criteria

The claim of completion is no broader than the evidence, and all material
risks are either checked, mitigated, or explicitly left open.

## Graph

```yaml
requires: [implement-minimal-change]
references: [analyze-change-impact]
followed-by: []
```
