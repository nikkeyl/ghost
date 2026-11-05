---
name: detect-component-anatomy-drift
description: Detect React component structure that drifts from the adopted
  component contract or creates consumer-specific complexity.
kind: passive
---

# Detect component anatomy drift

Run only for React component work in a repository that uses the GHOST
convention. Check for bloated optional props, scattered variant
conditionals, consumer-specific flags in shared markup, misplaced client
boundaries, unclear exports, and JSX that hides complex decisions.

This detector reports a signal; it does not demand a rewrite. Escalate
to `review-component-anatomy` when the drift materially increases
cognitive load, blast radius, or contract ambiguity.
