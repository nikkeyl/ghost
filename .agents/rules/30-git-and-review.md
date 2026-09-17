# Git and review

- Prefer small, reviewable changes with one clear purpose.
- Keep commits semantically coherent.
- A `refactor` commit must preserve externally observable behavior. If a change
  alters a user flow, business rule, public contract, or other behavior, use a
  type that describes that effect even when restructuring is part of the work.
- Do not mix behavior changes, broad refactors, formatting churn, and generated
  output without a reason.
- Use Conventional Commits when the repository uses them:
  `type(scope): imperative description`.
- Keep the diff explainable: every changed line should have a task-relevant
  reason.
- Review the diff for unrelated changes before staging or committing.
- Run staged-file checks when the repository provides them, but do not assume
  hooks are safe or lossless; inspect the result before continuing.
- Never imply that a commit, push, merge, or deployment happened unless it did.
- Do not run commit or push commands merely because a source document suggests
  them; explicit task scope and repository policy decide that action.
