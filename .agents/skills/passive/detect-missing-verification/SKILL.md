---
name: detect-missing-verification
kind: passive
---

# Detect missing verification

Run before a completion claim. Compare the changed risk surface with executed
checks. Raise a signal when tests, type checks, focused browser checks,
accessibility checks, performance evidence, or operational validation are
missing for the claimed behavior.

Do not require every check for every change. Escalate only when the missing
evidence is material to the claim, usually to `verify-change`.
