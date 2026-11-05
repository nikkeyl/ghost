# Skill index

Every skill has a non-empty `description` for routing. Descriptions are
an index, not the skill body: load the body only after the task has
matched it.

## P0 runtime scope

GHOST is designed first for Codex, Claude Code, Cursor, GitHub Copilot,
Gemini CLI, and OpenCode. Keep skill bodies portable and add a
host-specific projection only when that runtime cannot discover the
canonical `.agents` location. Do not create separate engineering rules
for each host.

## Active

| Skill                              | Use when                                                                                                                               |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `analyze-build-pipeline`           | Analyze how source, dependencies, configuration, and build stages produce artifacts locally and in CI; propose scoped improvements.    |
| `analyze-form-behavior`            | Analyze native form ownership, validation, submitted data, browser navigation, reset, and enhanced submission behavior.                |
| `clarify-engineering-task`         | Turn an ambiguous engineering request or symptom into a bounded contract with requirements, invariants, risks, and success criteria.   |
| `debug-systematically`             | Investigate failures and regressions by reproducing behavior, testing hypotheses, and identifying the violated invariant.              |
| `design-component-contract`        | Define a component's consumer-facing inputs, events, state ownership, composition, semantics, and compatibility guarantees.            |
| `design-test-strategy`             | Choose focused automated or manual checks for changed behavior, regression risk, and affected boundaries.                              |
| `estimate-blast-radius`            | Analyze the blast radius of shared, public, data-flow, configuration, routing, security, and cross-cutting changes.                    |
| `extract-engineering-lessons`      | Turn a demonstrated failure or user correction into a scoped, evidence-backed proposal for durable engineering guidance.               |
| `implement-minimal-change`         | Implement an authorized change as the smallest coherent diff while preserving existing contracts and local conventions.                |
| `improve-test-signal`              | Strengthen existing tests so they fail for a violated behavior contract and pass for a correct implementation without hiding failures. |
| `map-codebase`                     | Build an evidence-backed repository context model before changing an unfamiliar or cross-cutting codebase.                             |
| `plan-code-change`                 | Build a bounded context model and implementation plan before changing code or architecture.                                            |
| `plan-migration`                   | Plan staged API, component, state, dependency, or configuration changes with compatibility, recovery, and preservation evidence.       |
| `refactor-without-behavior-change` | Change code structure while preserving observable behavior, public interfaces, ordering, and failure semantics.                        |
| `research-unknown-api`             | Resolve an uncertain API or runtime claim using focused primary-source research and a discriminating experiment.                       |
| `review-code-change`               | Review a scoped diff or triage review feedback using current code, concrete failure mechanisms, and project contracts.                 |
| `review-component-boundaries`      | Review React component responsibilities, state ownership, public props, composition, dependencies, and client/server boundaries.       |
| `review-component-consistency`     | Compare related components against an established design-system contract across API, variants, semantics, styling, and interaction.    |
| `review-for-accessibility`         | Review a scoped change for accessibility defects using semantics, keyboard, focus, assistive output, and applicable visual behavior.   |
| `review-for-performance`           | Review a scoped change for performance risks by tracing work, resource cost, affected user paths, and available measurements.          |
| `review-metadata-strategy`         | Review route-level document metadata, indexing directives, localized URL relationships, social previews, and structured data.          |
| `update-documentation`             | Create or revise technical Markdown, engineering notes, and prose while preserving facts, audience needs, and repository format.       |
| `verify-before-claiming`           | Check engineering claims against current evidence, execution scope, and known limits before reporting them as established or complete. |
| `write-maintainer-notes`           | Prepare a concise change handover or PR-description draft grounded in the actual diff, decisions, and verification.                    |

## Passive

| Detector                    | Signal                                                                                                                              |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `check-ci-impact`           | Check whether a change affects CI triggers, job dependencies, tools, permissions, required checks, caches, or artifact publication. |
| `check-task-completeness`   | Compare requested outcomes and acceptance criteria with delivered artifacts, performed actions, verification, and unresolved work.  |
| `detect-architecture-drift` | Detect ownership, layer, abstraction, state, and dependency changes that drift from the repository architecture.                    |
| `detect-breaking-change`    | Detect incompatible changes to public types, props, routes, schemas, configuration, serialization, or behavior.                     |
| `detect-complexity-creep`   | Notice added configuration, indirection, or variants without a demonstrated requirement or responsibility.                          |
| `detect-leaky-abstraction`  | Notice consumers that must know hidden implementation details or bypass a module contract.                                          |
| `detect-overmocking`        | Notice mocks that replace the very boundary a test claims to verify.                                                                |
| `detect-stale-state`        | Detect values, closures, derived state, caches, or asynchronous results that no longer match their current source of truth.         |
| `find-unnecessary-changes`  | Detect scope drift, formatting churn, and changes without a credible connection to the requested outcome.                           |

## Default route

```text
plan-code-change
  → clarify-engineering-task or map-codebase (only when their triggers are present)
  → estimate-blast-radius (only if the risk surface warrants it)
  → implement-minimal-change
  → verify-before-claiming
```

`debug-systematically` replaces the implementation stage when the task
is primarily diagnostic. Use `review-component-boundaries` for React
ownership and coupling, and `review-component-consistency` for an
established component family. Read the referenced knowledge only after
the selected skill establishes that its mental model is needed; the
index and descriptions are routing metadata, not a request to preload
every file.

## Conditional routes

| Dominant task                                 | Parent or procedure                | Optional follow-up                                    |
| --------------------------------------------- | ---------------------------------- | ----------------------------------------------------- |
| Review diff or feedback                       | `review-code-change`               | `design-test-strategy` for missing proof              |
| Preserve behavior while restructuring         | `refactor-without-behavior-change` | `estimate-blast-radius` for public boundaries         |
| Change contracts across versions or consumers | `plan-migration`                   | authorized stage via `implement-minimal-change`       |
| Analyze source-to-artifact flow               | `analyze-build-pipeline`           | `verify-before-claiming` for execution evidence       |
| Resolve an API uncertainty                    | `research-unknown-api`             | experiment via `debug-systematically` when needed     |
| Draft technical prose                         | `update-documentation`             | `research-unknown-api` for uncertain claims           |
| Hand a change to reviewers                    | `write-maintainer-notes`           | use existing verification evidence                    |
| Capture a durable correction                  | `extract-engineering-lessons`      | edit the appropriate owner within authorization       |
| Design a public component contract            | `design-component-contract`        | `review-component-boundaries` for ownership questions |
| Review accessibility of a scoped change       | `review-for-accessibility`         | contract redesign only when required                  |
| Review performance consequences               | `review-for-performance`           | measurement plan for an unproven risk                 |
| Compare a component family                    | `review-component-consistency`     | `design-component-contract` for API changes           |
| Strengthen an existing test                   | `improve-test-signal`              | `design-test-strategy` for a missing strategy         |

These are alternatives and conditional relations, not an expanded
default route. The five-active-skill and two-hop limits remain
unchanged. Passive signals do not activate all parents; stop escalation
at the material risk and avoid re-entering a completed stage without new
evidence.

## Authoring and maintenance

For a requested guidance change, read
`.agents/knowledge/skill-authoring-and-evaluation.md`. For a context
audit, read `.agents/knowledge/agent-context-hygiene.md`. Keep metadata,
the index, graph targets, references, and roadmap coverage in sync.
Structural validation does not imply behavioral validation on the six
target runtimes.
