---
name: detect-missing-verification
description:
  Detect completion claims whose verification does not cover the changed
  behavior or risk surface.
kind: passive
---

# Detect missing verification

Run before a completion claim. Compare the changed risk surface with
executed checks. Raise a signal when tests, explicit type checks,
focused browser checks, accessibility checks, performance evidence, or
operational validation are missing for the claimed behavior.

Raise an additional signal when a production build bypasses type
checking and no separate type check covers the changed type risk. A
linter is not a replacement for TypeScript verification.

Do not require every check for every change. Escalate only when the
missing evidence is material to the claim, usually to `verify-change`.
