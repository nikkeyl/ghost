# Change scope and isolation

- Group work by one coherent outcome and keep the blast radius visible.
- For a task that touches multiple independent modules, decompose it before editing
  and state the sequence.
- Work in isolated units where practical: one module, file, function, or contract at
  a time.
- Do not pre-build speculative changes in adjacent modules.
- If the implementation reveals adjacent work, record it as a follow-up instead of
  silently expanding the current scope.
- After each material isolated unit, emit a checkpoint containing changed paths,
  reason, risk, and the next verification step.
- Require explicit user input when the next step changes scope materially, creates an
  irreversible external effect, or resolves a consequential ambiguity that the
  available evidence cannot resolve.
- A user request that already specifies implementation and scope is sufficient
  authorization to implement that scoped work; do not manufacture a second approval
  gate.
- Separate settled requirements from implementation choices. Give each work unit an
  outcome, dependencies, and a verification condition; keep intermediate states
  runnable. Use checkpoints according to risk, not an arbitrary file count.
- Preserve unrelated user changes and re-check relevant state before applying a
  prepared edit; another session may have changed the same file or index.
- Use the adopting repository's planning location when a saved plan is useful. Keep
  handoffs self-contained and bind factual context to its observed state.

- In an FSD repository, place code by ownership and responsibility, not only by reuse
  count. Keep single-use domain logic near its owner. Extract a local function or
  module when that improves a complex unit, but promote code to `shared` only after a
  second real consumer or an explicitly stable cross-domain contract exists.
- Treat duplicated behavior and growing component complexity as refactoring signals.
  Extract a unit when it has a distinct responsibility or reduces demonstrated
  duplication or complexity; do not create abstractions only for hypothetical reuse.
