# Git and review

- Prefer small, reviewable changes with one clear purpose.
- Keep commits semantically coherent.
- A `refactor` commit must preserve externally observable behavior. If a change
  alters a user flow, business rule, public contract, or other behavior, use a type
  that describes that effect even when restructuring is part of the work.
- Do not mix behavior changes, broad refactors, formatting churn, and generated
  output without a reason.
- Use Conventional Commits when the repository uses them:
  `type(scope): imperative description`.
- Keep the diff explainable: every changed line should have a task-relevant reason.
- Review the diff for unrelated changes before staging or committing.
- Run staged-file checks when the repository provides them, but do not assume hooks
  are safe or lossless; inspect the result before continuing.
- Before an authorized staging operation, inspect current working-tree and index
  state. Stage only the intended change; select hunks when a file mixes it with
  unrelated edits, then inspect the staged diff. Do not overwrite or unstage someone
  else's work to make the index look clean.
- Bind review and verification claims to their actual source/target and state.
  Recheck stale feedback against current code before implementing it.
- Personal commit wording is an optional profile in
  `.agents/knowledge/personal-authoring-preferences.md`; it does not authorize Git or
  publishing actions and does not override repository requirements.

- Never imply that a commit, push, merge, or deployment happened unless it did.
- Do not run commit or push commands merely because a source document suggests them;
  explicit task scope and repository policy decide that action.
