# Change scope and isolation

- Group work by one coherent outcome and keep the blast radius visible.
- For a task that touches multiple independent modules, decompose it before
  editing and state the sequence.
- Work in isolated units where practical: one module, file, function, or
  contract at a time.
- Do not pre-build speculative changes in adjacent modules.
- If the implementation reveals adjacent work, record it as a follow-up
  instead of silently expanding the current scope.
- After each material isolated unit, emit a checkpoint containing changed
  paths, reason, risk, and the next verification step.
- Require explicit user input when the next step changes scope materially,
  creates an irreversible external effect, or resolves a consequential
  ambiguity that the available evidence cannot resolve.
- A user request that already specifies implementation and scope is sufficient
  authorization to implement that scoped work; do not manufacture a second
  approval gate.
