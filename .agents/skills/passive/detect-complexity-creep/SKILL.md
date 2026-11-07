---
description: "Notice added configuration, indirection, or variants without a
  demonstrated requirement or responsibility."
kind: passive
name: detect-complexity-creep
---

# Detect complexity creep

During implementation or refactoring, compare new providers, modes,
flags, public methods, dependencies, and duplicate sources of truth with
acceptance criteria and demonstrated variation.

Name the added surface and missing purpose; line count alone is not
evidence. A required boundary or reliability mechanism is not needless
complexity. Escalate to `review-code-change` or `estimate-blast-radius`
only when the maintenance or contract cost is material; otherwise emit
no material signal.
