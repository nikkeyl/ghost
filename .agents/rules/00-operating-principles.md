# Operating principles

These are persistent rules for relevant engineering work.

- Prefer the smallest coherent change.
- Do not modify unrelated files, APIs, behavior, or formatting.
- Preserve existing public contracts unless a breaking change is explicit,
  justified, and accompanied by a migration or compatibility plan.
- Follow repository conventions before importing a convention from GHOST.
- Make ownership and boundaries explicit.
- Start with the minimum necessary solution: add only the code, structure,
  state, dependencies, and component props required by the current contract.
  Let demonstrated variation or complexity justify expansion.
- Avoid speculative abstractions; wait until variation is demonstrated.
- Before adding code, a dependency, or an abstraction, check whether the
  existing code, standard library, or native platform already satisfies the
  contract. Stop at the smallest solution that preserves correctness,
  validation, security, accessibility, and failure handling.
- When a capability is non-trivial, prefer a known and maintained package over
  a bespoke implementation if it fits the repository's constraints. Do not
  add a dependency for small, stable behavior already covered by the platform,
  standard library, or existing project utilities.
- Extract stable shared, configuration, and domain values into named constants.
  Use uppercase names for constants whose identity is meaningful beyond one
  local expression; keep a truly local one-off value local when naming it adds
  no clarity.
- Name new files and directories with lowercase kebab-case by default. Preserve
  required runtime or discovery names such as `AGENTS.md`, `CLAUDE.md`,
  `README.md`, and `SKILL.md`, along with established external paths and the
  existing repository layout; do not rename those compatibility paths merely
  to enforce this convention.
- Represent finite value-to-value, variant, or strategy mappings with a typed
  object or lookup table when the behavior is data. Use `if` for control flow,
  predicates, ordering, or dependent behavior rather than forcing every
  conditional into a map.
- Prefer `??` over `||` for defaults when only `null` and `undefined` mean
  "missing". Use `||` only when every falsy value is intentionally equivalent
  to absence.
- Prefer a ternary expression for a short value choice. Use a block `if` when
  the branch contains multiple statements, side effects, early returns, or
  sequential control flow. Do not use `switch`/`case`; use a typed map for
  finite data mappings or the clearest conditional structure for behavior.
- Do not mark synchronous code as `async` for stylistic uniformity. Add an
  asynchronous boundary only when it reflects a real operation, required API,
  or meaningful consumer contract.
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
