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
- `delegates-to` — an explicitly isolated subtask or subagent boundary; use only when
  the runtime supports delegation and the separation reduces context or risk.
- `conflicts-with` — do not activate both without resolving the conflict.

## Progressive activation

Start with the task's nouns and verbs, not with every available file. Load no more
than five active skills by default and traverse no more than two related skills.
Passive detectors should be short and return one of:

```text
no material signal
signal: <finding> / <evidence> / <severity>
escalate: <active skill> because <reason>
```

## Routing policy

Use `understand-and-plan-change` as the default routing point instead of creating a
standalone skill for every backlog item.

1. Classify the request by its dominant nouns and verbs: understand, frame, plan,
   implement, debug, review, verify, or operate.
2. Match the request to the smallest existing parent skill that can complete the
   procedure. Treat similarly named backlog items as sub-procedures until they prove
   they need an independent trigger, workflow, and verification.
3. Add at most the active skills needed by the actual risk surface. Prefer one parent
   skill that covers a capability family over several narrow leaf skills.
4. Let passive detectors observe adjacent risks without automatically loading a full
   active workflow. Escalate only when their signal is material.
5. Expand the active set only when investigation discovers a new contract, boundary,
   failure mode, or verification need that the current set cannot cover.

The backlog is a candidate registry, not an activation list. A candidate can remain
documented there, be covered by a parent skill, or be promoted to a standalone skill
after repeated value and an independent procedure are demonstrated.

## Completion model

A task is not complete when code was generated. It is complete when:

1. the intended contract is implemented;
2. the diff stays within scope;
3. relevant checks were run or their absence is explicit;
4. remaining uncertainty and follow-up work are named.

## Additional task families

The skill index contains conditional routes for review, test strategy, refactoring,
migration, API research, documentation, handover, and lesson capture. Choose their
parent according to the task's dominant outcome. Receiving review feedback does not
imply publishing replies; a diagnostic request does not imply implementation;
drafting a migration does not imply performing its stages.

Graph relations can point back to a previously completed stage. Re-enter it only when
new evidence invalidates its result, and stay within the traversal budget. The size
of the catalog is not the size of the active context.
