# Skill index

Every skill has a non-empty `description` for routing. Descriptions are an
index, not the skill body: load the body only after the task has matched it.

## P0 runtime scope

GHOST is designed first for Codex, Claude Code, Cursor, GitHub Copilot,
Gemini CLI, and OpenCode. Keep skill bodies portable and add a host-specific
projection only when that runtime cannot discover the canonical `.agents`
location. Do not create separate engineering rules for each host.

## Active

| Skill | Use when |
|---|---|
| `understand-and-plan-change` | a change needs scope, context, or sequencing |
| `understand-codebase` | repository ownership, boundaries, or relevant flows are unclear |
| `clarify-engineering-task` | the request, symptom, contract, or success criteria are materially ambiguous |
| `analyze-change-impact` | a public/shared/cross-cutting contract may change |
| `implement-minimal-change` | the scoped implementation is authorized |
| `debug-systematically` | behavior is failing or unexpected |
| `verify-change` | a completion claim needs evidence |
| `review-component-anatomy` | React component structure is in scope |
| `review-custom-control` | a custom interactive control or its state contract is in scope |
| `review-form-contract` | a form or its submission lifecycle is in scope |
| `review-metadata-strategy` | page metadata, indexability, localized URLs, or structured data are in scope |
| `review-code-change` | a scoped diff or received review feedback needs evidence-based assessment |
| `design-test-strategy` | a change needs a risk-appropriate automated or manual verification plan |
| `refactor-without-behavior-change` | structure must change while preserving observable behavior |
| `plan-migration` | consumers, state, versions, or configuration need a staged transition |
| `research-unknown-api` | an uncertain API or runtime claim affects an engineering decision |
| `write-maintainer-notes` | a completed change needs a handover or PR-description draft |
| `update-documentation` | technical Markdown or engineering prose needs drafting or revision |
| `extract-engineering-lessons` | requested durable guidance must capture an evidenced lesson |

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
| `detect-async-race` | stale or uncancelled user-driven asynchronous work |
| `detect-test-signal-weakness` | tests can pass without exercising the claimed behavior |
| `detect-overmocking` | mocks bypass the boundary the test claims to verify |
| `detect-leaky-abstraction` | consumers depend on hidden details or bypass module contracts |
| `detect-complexity-creep` | new surface lacks a demonstrated responsibility or requirement |
| `detect-build-impact` | manifest, lockfile, generated output, or CI risk lacks relevant evidence |

## Default route

```text
understand-and-plan-change
  → clarify-engineering-task or understand-codebase (only when their triggers are present)
  → analyze-change-impact (only if the risk surface warrants it)
  → implement-minimal-change
  → verify-change
```

`debug-systematically` replaces the implementation stage when the task is
primarily diagnostic. `review-component-anatomy` is conditional on React work
and repository fit. Read the referenced knowledge only after the selected
skill establishes that its mental model is needed; the index and descriptions
are routing metadata, not a request to preload every file.


## Conditional routes

| Dominant task | Parent or procedure | Optional follow-up |
|---|---|---|
| Review diff or feedback | `review-code-change` | `design-test-strategy` for missing proof |
| Preserve behavior while restructuring | `refactor-without-behavior-change` | `analyze-change-impact` for public boundaries |
| Change contracts across versions or consumers | `plan-migration` | authorized stage via `implement-minimal-change` |
| Resolve an API uncertainty | `research-unknown-api` | experiment via `debug-systematically` when needed |
| Draft technical prose | `update-documentation` | `research-unknown-api` for uncertain claims |
| Hand a change to reviewers | `write-maintainer-notes` | use existing verification evidence |
| Capture a durable correction | `extract-engineering-lessons` | edit the appropriate owner within authorization |

These are alternatives and conditional relations, not an expanded default route.
The five-active-skill and two-hop limits remain unchanged. Passive signals do
not activate all parents; stop escalation at the material risk and avoid
re-entering a completed stage without new evidence.

## Authoring and maintenance

For a requested guidance change, read
`.agents/knowledge/skill-authoring-and-evaluation.md`. For a context audit,
read `.agents/knowledge/agent-context-hygiene.md`. Keep metadata, the index,
graph targets, references, and roadmap coverage in sync. Structural validation
does not imply behavioral validation on the six target runtimes.
