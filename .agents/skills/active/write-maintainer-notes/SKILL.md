---
name: write-maintainer-notes
description: "Prepare a concise change handover or PR-description draft grounded in
  the actual diff, decisions, and verification."
kind: active
---

# Write maintainer notes

## Trigger

Use when a completed change needs a review guide, handover, or
PR-description draft.

## Goal

Let a reviewer understand the outcome, important decisions, and
verification without session history.

## Investigation / reasoning

1. Resolve the change scope, target, reviewed state, and relevant local
   task artifacts.

1. Match requirements and planned units to the actual diff in both
   directions. Identify missing work, deliberate deviations, and
   unplanned changes.

1. Read the decisions and check results that support the explanation. Do
   not rebuild unrelated history or assume a plausible rationale is
   recorded.

1. Identify the few files where reviewer judgment matters and known
   limitations.

## Decision rules

- Lead with the problem and resulting behavior. Explain material
  trade-offs, not the conversation chronology.

- State a rationale only when evidence supports it; label missing
  reasons.

- Link only resources the intended reviewer can access. Incorporate
  essential context from private planning documents without pointing
  readers to them.

- Describe checks actually performed and bind them to the relevant
  state. A handover is not an independent review or proof of
  correctness.

- Drafting does not authorize creating a PR, posting a comment, or
  pushing code.

## Actions

Use `.agents/templates/change-handover.md`, omitting empty sections.
Follow the repository's PR template when present. Read
`.agents/knowledge/writing-and-review-communication.md` for
reviewer-facing prose. Save only when requested or when a persistent
handover is part of the task.

## Verification

Check the draft against the diff and evidence. Confirm every material
claim, accessible link, decision, gap, and verification result is
accurate.

## Completion criteria

The handover stands alone, is concise, and does not overstate
implementation or verification.

## Graph

```yaml
references: [verify-before-claiming, review-code-change, update-documentation]
```
