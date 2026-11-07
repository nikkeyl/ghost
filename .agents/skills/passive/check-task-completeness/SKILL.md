---
description: Compare requested outcomes and acceptance criteria with delivered
  artifacts, performed actions, verification, and unresolved work.
kind: passive
name: check-task-completeness
---

# Check task completeness

Run before a completion report or handover. Reconstruct the requested
outcomes and acceptance criteria from the current task, including later
corrections. Map each requirement to its delivered file, behavior, or
external action and mark it done, partial, blocked, or explicitly
excluded by the user.

Look for omitted deliverables, placeholders, disconnected wiring,
missing error paths, stale documentation, and actions described but
never performed. Distinguish a completed plan from an implemented
change, a local fix from a pushed one, and a workflow definition from a
successful publication when those outcomes were requested.

Compare claimed verification with the changed risk surface. Passing
lint cannot stand in for a required type check or observed behavior.
Do not demand every possible check or add unstated requirements.

Report the unmet criterion, current evidence, and smallest remaining
step. Route missing implementation to `implement-minimal-change`,
missing proof to `verify-before-claiming`, and material scope ambiguity
to `clarify-engineering-task`. Emit no material signal only when the
requested outcomes and evidence are accounted for; never silently mark
partial or blocked work complete.
