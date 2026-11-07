---
description: "Review a scoped diff or triage review feedback using current
  code, concrete failure mechanisms, and project contracts."
kind: active
name: review-code-change
---

# Review a code change

## Trigger

Use for a requested review of a PR, branch, working-tree change, or
received review comments. A review request authorizes analysis;
implementation depends on the user's stated scope.

## Goal

Produce actionable findings while separating defects, material risks,
and optional preferences.

## Investigation / reasoning

1. Resolve the intended outcome, source, target, and reviewed state.
   Record a commit or working-tree baseline, including relevant
   untracked files.

1. For a branch or PR, compare from the merge base with its actual
   target. Use current refs when available; report stale or missing
   refs. If there is no common ancestor, resolve that limitation before
   attributing changes.

1. Read the diff, relevant conventions, callers, and checks. Separate
   introduced problems from pre-existing issues and changes already
   present in the target.

1. Test each finding's premise against current code, including the
   input, transition, or consumer that makes the consequence possible.

1. For received feedback, check whether the concern remains current;
   propose address, partial, push back, or already resolved with a
   concrete reason.

## Decision rules

- A finding needs a reproducible failure, a named violated contract, or
  an evidence-backed risk with its preconditions. A hypothetical
  possibility is not a confirmed defect.

- Assess severity separately from confidence. Do not invent numeric
  certainty or treat an absence of findings as proof of correctness.

- Keep stylistic preferences distinct from merge blockers. For code-style
  findings, use `.agents/rules/code-style.md` with the effective local
  configuration. Respect severity, language contracts, import side
  effects, JSX spreads and CSS cascade behavior; sorting alone does not
  justify changing runtime semantics.

- Bind the report to the reviewed state; later edits can invalidate it.

- Draft replies for the human. Posting, resolving threads, voting, and
  fixing code require authorization for those actions.

## Actions

Report each material finding as location, problem, triggering condition,
consequence, evidence, and a proportionate correction. Group received
comments by disposition and extract accepted work into requirements when
requested. For a handover, use `write-maintainer-notes`; for prose
style, read `.agents/knowledge/writing-and-review-communication.md` only
when drafting.

## Verification

Recheck locations and premises against the recorded state. Confirm the
report covers the requested diff and accounts for actionable feedback.
State checks performed, unavailable evidence, and excluded areas.

## Completion criteria

The review scope and state are explicit, every finding has a defensible
mechanism or contract, and no publishing or implementation is implied.

## Graph

```yaml
may-trigger:
  [
    design-test-strategy,
    estimate-blast-radius,
    review-for-accessibility,
    review-for-performance,
  ]
references: [write-maintainer-notes]
```
