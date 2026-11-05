---
name: detect-accessibility-regression
description:
  Detect material accessibility regressions in semantics, focus,
  keyboard, media, responsive, and motion behavior.
kind: passive
---

# Detect accessibility regression

Run when markup, interactive states, focus, keyboard behavior, media, or
responsive layout changes. Look for lost semantics, missing names or
state, unreachable focus, mouse-only behavior, missing captions or image
alternatives, poor contrast or focus indication, scroll traps, and
reduced-motion regressions. For data tables, inspect programmatic header
relationships and keyboard access to a horizontally scrolling region.
For carousels, check offscreen focusable content, current-position
semantics, and whether automatic motion can be stopped.

Raise a signal with the affected interaction and evidence. Escalate to
an active review or `verify-change` only when the finding is material or
the component is user-facing.
