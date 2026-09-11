# Skill index

## Active

| Skill | Use when |
|---|---|
| `understand-and-plan-change` | a change needs scope, context, or sequencing |
| `analyze-change-impact` | a public/shared/cross-cutting contract may change |
| `implement-minimal-change` | the scoped implementation is authorized |
| `debug-systematically` | behavior is failing or unexpected |
| `verify-change` | a completion claim needs evidence |
| `review-component-anatomy` | React component structure is in scope |

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

## Default route

```text
understand-and-plan-change
  → analyze-change-impact (only if the risk surface warrants it)
  → implement-minimal-change
  → verify-change
```

`debug-systematically` replaces the implementation stage when the task is
primarily diagnostic. `review-component-anatomy` is conditional on React work
and repository fit.
