# Operating principles

These are persistent rules for relevant engineering work.

- Prefer the smallest coherent change.
- Do not modify unrelated files, APIs, behavior, or formatting.
- Preserve existing public contracts unless a breaking change is explicit,
  justified, and accompanied by a migration or compatibility plan.
- Follow repository conventions before importing a convention from GHOST.
- Make ownership and boundaries explicit.
- Avoid speculative abstractions; wait until variation is demonstrated.
- Before adding code, a dependency, or an abstraction, check whether the
  existing code, standard library, or native platform already satisfies the
  contract. Stop at the smallest solution that preserves correctness,
  validation, security, accessibility, and failure handling.
- Treat accessibility, security, performance, maintainability, and UX as part
  of correctness, not as optional polish.
- Measure before optimizing. Choose optimization effort proportionally to the
  project's size, business urgency, delivery constraints, and measured impact;
  prioritize the critical path and avoid optimization by habit.
- Do not hide uncertainty or silently convert an assumption into a fact.
- Do not claim a test, profile, review, browser check, or deployment check that
  was not actually performed.

## Decision language

Use precise labels in plans and reports:

- **Fact** — observed in code, output, documentation, or a reproducible test.
- **Assumption** — adopted temporarily because evidence is incomplete.
- **Hypothesis** — explanation that still needs a discriminating check.
- **Decision** — selected action and its reason.
- **Risk** — plausible adverse outcome, with severity and mitigation.
