---
name: detect-accessibility-regression
kind: passive
---

# Detect accessibility regression

Run when markup, interactive states, focus, keyboard behavior, media, or
responsive layout changes. Look for lost semantics, missing names or state,
unreachable focus, mouse-only behavior, missing captions, poor contrast or
focus indication, scroll traps, and reduced-motion regressions.

Raise a signal with the affected interaction and evidence. Escalate to an
active review or `verify-change` only when the finding is material or the
component is user-facing.
