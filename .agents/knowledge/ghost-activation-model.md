# GHOST activation model

## Layers

```text
Rules
  ↓ constrain reasoning, routing, and action
Knowledge / mental models
  ↓ explain mechanisms
Router
  ↓ selects the smallest relevant procedure
Active skill
  ↘ passive detectors
Action
  ↓
Verification → self-critique → final report
```

## Graph vocabulary

- `requires` — prerequisite understanding or evidence.
- `may-trigger` — conditional follow-up, not automatic execution.
- `followed-by` — normal next stage after completion.
- `references` — useful context, not a launch condition.
- `conflicts-with` — do not activate both without resolving the conflict.

## Progressive activation

Start with the task's nouns and verbs, not with every available file. Load no
more than five active skills by default and traverse no more than two related
skills. Passive detectors should be short and return one of:

```text
no material signal
signal: <finding> / <evidence> / <severity>
escalate: <active skill> because <reason>
```

## Completion model

A task is not complete when code was generated. It is complete when:

1. the intended contract is implemented;
2. the diff stays within scope;
3. relevant checks were run or their absence is explicit;
4. remaining uncertainty and follow-up work are named.
