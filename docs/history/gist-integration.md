# Gist integration

Date: 2026-11-12. Baseline: `ccd1039`. Scope: the owner's four engineering
gists, excluding Kaiten Task Delivery. This import extends existing owners;
it does not add tracker integration, active skills, or automatic updates.

## Source and ownership map

| Source                                   | Revision  | Portable owner and treatment                                                                                                                                                                                       |
| ---------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Anatomy of a React Component             | `444f507` | `rules/code-style.md`: narrow existing-type props, component layout, body order, variant configuration and class composition. Existing module rules own exports and file boundaries.                               |
| Modularly Isolated Generation            | `139a3d8` | Existing `rules/change-scope.md`, `plan-code-change`, `implement-minimal-change` and `verify-before-claiming` already cover decomposition, checkpoints, scope isolation and proof. No parallel MIG skill is added. |
| Not Agree                                | `8757a08` | `rules/reasoning-and-evidence.md`: equal evidence standards, recovery from conversational drift, contextual explanations and unresolved technical objections.                                                      |
| Developer Verification Before Submission | `d8291d8` | `verify-before-claiming` and `design-test-strategy` route to `knowledge/developer-verification.md`; `templates/verification-record.md` owns the compact evidence record.                                           |

The owner authorized integration and subsequent removal of the source gists.
The formulations here are self-contained; runtime guidance does not depend on
their continued availability. Secret-gist URLs and personal paths are not
published. The immutable source snapshots were read before adaptation.

## Adaptation boundaries

- React's body order is a readability default, not proof of Hook correctness
  or safe initialization. Native/generated props are reused only when their
  semantics fit. Configuration remains in its dedicated owning file. Slots
  and class-merging overrides require a real consumer contract; GHOST does
  not mandate a particular utility library or unsupported public prop.

- MIG's blanket plan approvals, per-file stops and mandatory commits are not
  imported. Existing user authorization and repository delivery rules govern
  execution. A coherent change can cross files; unrelated changes remain
  excluded. Material checkpoints do not require manufacturing another gate.

- Not Agree's evidence standard applies equally to the user, third parties
  and the agent's prior output. Expertise can shape an explanation, but not
  correctness. A remaining material objection stays visible without requiring
  the same warning in every later response.

- Developer verification stays under existing parent skills. Requirement
  coverage, versioned evidence, actual roles, integration outcomes, recovery,
  retests and cleanup determine readiness; broad builds and extra tests do
  not replace missing proof. Ordinary research and small documentation tasks
  do not acquire an unrelated acceptance suite.

## Evidence boundaries

The catalog remains 8 rules, 24 active skills, 9 passive detectors and
8 templates; knowledge grows from 16 to 17 files. Structural checks, Markdown
checks, generated runtime archives and native discovery establish their
respective boundaries. Content review does not establish behavior on every
host, independent acceptance, or the author's proficiency. C03–C05 remain
separate runtime gates; no behavioral gate is closed by this import.
