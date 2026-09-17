# Skill index

Every skill has a non-empty `description` for routing. Descriptions are an
index, not the skill body: load the body only after the task has matched it.

## P0 runtime scope

GHOST is designed first for Codex, Claude Code, Cursor, GitHub Copilot,
Gemini CLI, and OpenCode. Keep skill bodies portable and add a host-specific
projection only when that runtime cannot discover the canonical `.agents`
location. Do not create separate engineering rules for each host.

## Active

| Skill | Use when |
|---|---|
| `understand-and-plan-change` | a change needs scope, context, or sequencing |
| `analyze-change-impact` | a public/shared/cross-cutting contract may change |
| `implement-minimal-change` | the scoped implementation is authorized |
| `debug-systematically` | behavior is failing or unexpected |
| `verify-change` | a completion claim needs evidence |
| `review-component-anatomy` | React component structure is in scope |
| `review-custom-control` | a custom interactive control or its state contract is in scope |
| `review-form-contract` | a form or its submission lifecycle is in scope |

## Passive

| Detector | Signal |
|---|---|
| `detect-unrelated-diff` | scope drift or formatting churn |
| `detect-breaking-change` | incompatible public behavior or contract |
| `detect-missing-verification` | claim broader than executed evidence |
| `detect-accessibility-regression` | semantics, focus, keyboard, media, or responsive risk |
| `detect-performance-risk` | plausible but unmeasured performance regression |
| `detect-architecture-drift` | ownership, layer, or abstraction drift |
| `detect-component-anatomy-drift` | React convention drift in an adopting repository |
| `detect-async-race` | stale or uncancelled user-driven asynchronous work |

## Default route

```text
understand-and-plan-change
  → analyze-change-impact (only if the risk surface warrants it)
  → implement-minimal-change
  → verify-change
```

`debug-systematically` replaces the implementation stage when the task is
primarily diagnostic. `review-component-anatomy` is conditional on React work
and repository fit. Read the referenced knowledge only after the selected
skill establishes that its mental model is needed; the index and descriptions
are routing metadata, not a request to preload every file.
