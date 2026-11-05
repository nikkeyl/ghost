---
name: detect-unrelated-diff
description:
  Detect scope drift, formatting churn, and changes without a credible
  connection to the requested outcome.
kind: passive
---

# Detect unrelated diff

Run alongside implementation or review. Compare changed paths and hunks
with the stated outcome, plan, and repository conventions. Raise a
signal only when the change has no credible task-relevant reason,
introduces formatting churn, or silently expands scope.

Report: `signal: <path/hunk> / <reason it is unrelated> / <severity>`.
Escalate to `implement-minimal-change` or `analyze-change-impact` when
the unrelated change affects a shared contract or cannot be safely
removed.
