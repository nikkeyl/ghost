# GHOST roadmap

Reviewed: 2026-11-06 against repository baseline `82af2d6`.

Repository tooling, separate push checks, gated releases, English docs,
portable CI/CD guidance, and skill naming/content alignment are
implemented. The catalog contains 8 rules, 16 knowledge files, 24 active
skills, 9 passive checks and 8 templates. All 33 skill names belong to
the original 479-candidate backlog.

All five push checks passed on `82af2d6`. Its published runtime archive
was inspected against the source: exactly 68 files, with matching bytes
and no technical docs or obsolete passive copies. Skill structure was
checked after the content corrections in `1477694`, including index
roles, metadata, 107 graph edges and local references.

Phase 0 artifacts and repository delivery are complete at that scope.
The recorded Phase 1 repository trial remains historical; current
procedures have not passed a fresh representative host trial. The
33-skill content audit and author walkthroughs do not establish host
discovery, routing quality, independent judgment or personal proficiency.

The next project gate is C03: one named host running the current skill
contracts. The author's parallel learning priority is JavaScript/Web
depth. See the [checklist](checklist.md) for completed work and remaining
acceptance gates, the [historical audit](../history/audit-2026-11-05.md)
for its original baseline, and the
[author profile](../reference/author-profile.md) for personal context.

## Evidence gates and current priorities

Keep three claims separate: an artifact exists, a structural check passes, and a
procedure produces the expected behavior in a named runtime. None establishes
the author's independent proficiency. Historical trials retain their original
scope; rerun them when a relevant artifact or runtime changes.

| Workstream          | Current evidence                                                                | Next gate                                                                      | Checklist |
| ------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------- |
| Core catalog        | 33 skills aligned with backlog names and intended outcomes; 24 active/9 passive | Fresh host trial of corrected procedures                                       | C18; C03  |
| Phase 1/2 behavior  | Phase 1 trial recorded; Phase 2 procedures authored                             | Representative positive, non-trigger and failure cases on one host             | C03       |
| Runtime portability | Six native release profiles; Codex and Claude discovery observed                | Versioned discovery, routing and passive-detector matrix, one host at a time   | C04–C05   |
| Platform depth      | Narrow frontend guidance exists; broader procedures proposed                    | JS predictions and browser/network experiments before framework recipes        | C07–C10   |
| Quality / packaging | Scoped reviews authored; runtime ZIP inspected; package leads remain historical | Consumer, accessibility, performance and trust-boundary evidence               | C11–C12   |
| Systemic judgment   | Reasoning/evidence rules and candidate inventory                                | Apply alternatives, team cost, reversibility and adoption to current decisions | C13–C14   |

Repository delivery is completed under C01–C02 and C17–C19. CI uses
separate Editorconfig, Prettier, Remark, Commit Lint and Pre Commit
workflows. Remark includes `.agents`. Husky runs staged formatting and
Markdown linting plus commit-message validation. The standard
pre-commit CLI uses Python; no custom Python utility or aggregate
lint/validate workflow remains.

Semantic PR title checks, Dependabot updates and actor-scoped auto-merge
are configured; their PR-specific outcomes remain unverified (C20).
Release uses `workflow_run` completion events, checks all five required
results for the same immutable commit and publishes the explicit
runtime allowlist as `ghost-{short-commit}`. Publication and archive
inspection are separate evidence from portable skill execution.

## Phase status

| Phase                    | Completed or authored                                                                                   | Remaining gate                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| 0 — Foundation           | Core catalog, naming/content review, repository CI and runtime releases                                 | Maintain checks; behavior is assessed in later gates                |
| 1 — Cognitive core       | Repository mapping, framing, planning, blast-radius and claim/completeness procedures; historical trial | Fresh representative host trial and routing evidence (C03–C05)      |
| 2 — Safe execution       | Implementation, debugging, review, test strategy/signal, refactoring and migration procedures           | Positive, non-trigger and failure cases on a named host (C03)       |
| 3 — Frontend depth       | Scoped React boundaries, native forms, metadata and stale-state guidance                                | Broader JS/browser/network models and observed learning (C07–C10)   |
| 4 — User-facing quality  | Accessibility/performance reviews and component contract/consistency procedures                         | Real quality cases and package-consumer evidence (C11–C12)          |
| 5 — Production evolution | Portable CI/CD rules, build analysis and migration template                                             | Operational cases, runbooks and recovery evidence when needed (C15) |
| 6 — Systemic judgment    | Claim verification, research, documentation, lessons and handover procedures                            | Concrete decision cases and durable evidence refresh (C13–C14)      |

Partial capability coverage does not close an entire phase. Future
standalone skills remain conditional on the promotion policy and C16.

## Purpose

The attached capability inventory is the long-term backlog for GHOST. It
contains 479 candidate procedures across 35 engineering domains, from
`map-codebase` and `trace-data-flow` to `evaluate-systemic-impact`,
`critique-own-solution`, and `research-unknown-api`.

The inventory is a source of candidates, not a command to create 479 isolated
skills immediately. GHOST should grow as a progressive capability graph:

```text
candidate procedure
  → domain family
  → parent skill / checklist
  → evidence-backed promotion
  → standalone skill only when justified
```

The complete imported inventory is preserved in [backlog](backlog.md). This
document owns priorities and implementation status; the backlog preserves the
exhaustive candidate list.

## Current baseline — Phase 0: foundation (authored)

Already implemented in `.agents/`:

- 8 persistent rules for scope, evidence, Git/review, frontend contracts,
  disagreement, data/failure contracts, CI/CD and source-code style.
  The code-style owner records portable authoring defaults and explicit
  adopting-repository exceptions.

- 16 knowledge files covering activation, source-derived frontend patterns, web
  document metadata, data loading and failure, async UI state, Next.js Server
  Actions, runtime/context adaptation, content trust boundaries, and general
  engineering patterns, plus behavior preservation, research, writing, skill
  authoring, personal preferences, context hygiene, and optional integrations.

- 24 active skills for planning, impact analysis, minimal implementation,
  debugging, verification, codebase understanding, task clarification, React
  boundary, contract and consistency review, browser form behavior, metadata,
  accessibility and performance review, plus diff review, test strategy,
  test-signal improvement, behavior-preserving refactoring, migration planning,
  API research, handover, prose, lesson capture, and build-pipeline analysis.

- 9 passive detectors for unnecessary changes, breaking contracts, task
  completeness, architecture drift, stale state, overmocking, abstraction
  leaks, complexity creep, and CI impact.

- Progressive activation limits: 5 active skills by default, 2 graph hops.

- P0 runtime target set: Codex, Claude Code, Cursor, GitHub Copilot, Gemini CLI,
  and OpenCode. Runtime-specific files remain thin adapters over the portable
  `.agents` core.

The artifact-level Phase 0 criteria are present: each active skill has a
trigger, goal, investigation, decision rules, actions, verification, and
completion criteria. That is structural evidence; host discovery and procedure
outcomes have separate gates above.

## Phase 1 checkpoint — historically trialled slice

The first Phase 1 slice is implemented and trialled on the real
`time-to-your-hair` repository:

- `map-codebase` builds a scoped module, ownership, runtime-boundary,
  flow, source-of-truth, unknowns, and evidence model.

- `clarify-engineering-task` turns materially ambiguous requests or symptoms
  into a bounded contract with invariants, non-goals, and success criteria.

- `.agents/templates/repository-context.md` provides the durable checkpoint
  output shape.

- `verify-before-claiming` compares the plan with the implementation and records
  challenged assumptions or counterexamples.

- The trial preserved the prototype/production boundary and exposed existing
  repository state as a risk instead of treating it as a clean baseline.

The trial also confirmed that a repository without `AGENTS.md` or `CLAUDE.md`
can still be modelled from its project brief, package/build configuration, entry
points, and runtime configuration, but the missing adapter guidance must remain
an explicit uncertainty.

## Evidence-backed promotions and backlog coverage

The following capabilities were promoted from user-confirmed cross-project
patterns without creating one skill per observation:

- `analyze-form-behavior` traces native ownership, payload, validation,
  submit/reset and navigation before framework enhancements and failure paths.

- `detect-stale-state` compares current sources of truth with snapshots,
  closures, derived state, cache and asynchronous results.

- `async-ui-state-and-cancellation`, `nextjs-server-actions`,
  `content-trust-boundaries`, and `engineering-patterns` preserve the underlying
  mental models and evidence.

- `review-metadata-strategy` and `web-document-metadata` promote the route-level
  metadata, indexing, localization, social-preview, and structured-data review
  from the candidate backlog.

These promotions are routed through the existing parent workflow and do not
change the default activation budget.

The following backlog candidates are now represented in GHOST. `covered` means
the candidate is implemented by an existing rule, parent skill, detector, or
knowledge file; it is intentionally not a new standalone skill.

| Backlog candidates                                                                                                                                                                | GHOST artifact                                                                                                                                             | Kind                      | Status      | Routing                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ----------- | ------------------------------------------------------------------------------- |
| `review-metadata-strategy`                                                                                                                                                        | `skills/active/review-metadata-strategy`, `knowledge/web-document-metadata.md`                                                                             | active + knowledge        | implemented | page metadata, indexability, locale, social preview, or structured data changes |
| `implement-cancellation`                                                                                                                                                          | `knowledge/async-ui-state-and-cancellation.md`, `skills/passive/detect-stale-state`                                                                        | knowledge + passive       | covered     | `debug-systematically` or async signal                                          |
| `analyze-module-loading`                                                                                                                                                          | `knowledge/data-loading-and-failure-model.md`, `skills/active/review-for-performance`                                                                      | knowledge + active        | covered     | a dependency or renderer may be loaded too broadly                              |
| `analyze-async-control-flow`, `review-state-transitions`, `detect-stale-state`                                                                                                    | `knowledge/async-ui-state-and-cancellation.md`, `skills/passive/detect-stale-state`                                                                        | knowledge + passive       | covered     | derived, captured, cached or async state may become obsolete                    |
| `choose-server-vs-client-component`, `review-server-component-boundaries`, `identify-client-server-boundaries`                                                                    | `rules/frontend-contracts.md`, `skills/active/review-component-boundaries`                                                                                 | rule + active             | covered     | React/Next.js boundary is in scope                                              |
| `analyze-server-actions`                                                                                                                                                          | `knowledge/nextjs-server-actions.md`, `rules/frontend-contracts.md`                                                                                        | knowledge + rule          | covered     | Next.js mutation is in scope                                                    |
| `review-data-fetching-strategy`, `optimize-data-fetching`, `optimize-caching`                                                                                                     | `rules/data-and-failure-contracts.md`, `knowledge/data-loading-and-failure-model.md`                                                                       | rule + knowledge          | covered     | data boundary or freshness risk                                                 |
| `design-layer-boundaries`, `design-domain-boundaries`                                                                                                                             | `rules/change-scope.md`, `skills/passive/detect-architecture-drift`                                                                                        | rule + passive            | covered     | ownership or FSD layer is uncertain                                             |
| `identify-state-owner`, `identify-state-ownership`, `classify-state`, `separate-server-and-client-state`, `design-state-architecture`                                             | `knowledge/data-loading-and-failure-model.md`, `knowledge/engineering-patterns.md`                                                                         | knowledge                 | covered     | state ownership is uncertain                                                    |
| `design-error-model`, `design-failure-isolation`, `review-partial-failure`, `implement-fallback-behavior`                                                                         | `rules/data-and-failure-contracts.md`, `knowledge/data-loading-and-failure-model.md`                                                                       | rule + knowledge          | covered     | primary/partial/secondary outcome exists                                        |
| `review-user-generated-content`, `identify-trust-boundaries`                                                                                                                      | `knowledge/content-trust-boundaries.md`                                                                                                                    | knowledge                 | covered     | external content reaches a rendering or behavior sink                           |
| `design-data-flow`, `design-cache-strategy`, `design-concurrency-model`                                                                                                           | `knowledge/data-loading-and-failure-model.md`, `knowledge/async-ui-state-and-cancellation.md`                                                              | knowledge                 | covered     | data, freshness, or race behavior needs a model                                 |
| `review-data-shape`, `normalize-api-data`, `design-view-model`, `separate-domain-and-transport-model`                                                                             | `knowledge/data-loading-and-failure-model.md`, `knowledge/engineering-patterns.md`                                                                         | knowledge                 | covered     | transport and UI ownership need an explicit boundary                            |
| `review-form-accessibility`, `test-error-paths`, `test-concurrency`                                                                                                               | `skills/active/analyze-form-behavior`                                                                                                                      | active                    | covered     | form or submit pipeline is in scope                                             |
| `design-component-api`, `design-extension-points`, `review-component-boundaries`, `review-hook-design`, `review-variant-model`, `design-slot-api`, `separate-ui-and-domain-logic` | `rules/frontend-contracts.md`, `skills/active/review-component-boundaries`, `skills/active/design-component-contract`, `knowledge/engineering-patterns.md` | rule + active + knowledge | covered     | component or UI/domain contract is in scope                                     |
| `extract-domain-logic`, `remove-duplication`, `reduce-complexity`, `improve-module-cohesion`, `incremental-refactor`                                                              | `rules/change-scope.md`, `skills/active/implement-minimal-change`                                                                                          | rule + active             | covered     | duplication or complexity is demonstrated                                       |
| `split-commit`, `prepare-clean-commit`, `review-commit-history`                                                                                                                   | `rules/git-and-review.md`                                                                                                                                  | rule                      | covered     | commit or review boundary is in scope                                           |
| `review-design-token-usage`, `design-token-architecture`                                                                                                                          | `rules/frontend-contracts.md`, `skills/active/review-component-boundaries`                                                                                 | rule + active             | covered     | repeated visual meaning is demonstrated                                         |
| `define-verification-plan`, `design-minimal-change`                                                                                                                               | `skills/active/plan-code-change`, `skills/active/verify-before-claiming`                                                                                   | active                    | covered     | a change needs a bounded plan or risk-appropriate check                         |

Broader platform, security, and production families remain planned.
`map-codebase` is implemented in the Phase 1 slice described above. The
remaining families have candidate names in the backlog, but the current evidence
does not yet justify claiming complete independent workflows for them.

## Code-style clarification

The earlier function/quote/spacing clarification is now part of
`rules/code-style.md`. A Playwright review of 60 file/profile views across 16
public reference repositories compared configuration, source examples,
editor settings and profile principles. General agreements now include
file formatting, modules and type-only imports, grouped exports,
destructuring, TypeScript safety, JSX, and CSS/SCSS conventions.

The core contains no reference-project names, paths, aliases, versions,
IDE settings or copied framework configuration. Contradictory JSX quote,
side-effect import, selector and animation overrides remain contextual.
Implementation and review procedures point to the same style owner.
See the [source review](../history/source-analysis.md#repository-code-style-review)
for provenance and transfer boundaries. This is source inspection and
instruction validation, not proof of host discovery or a completed C06.

The catalog remains 33 skills with 24 active/9 passive roles. The new
rule adds one distributed Markdown file; the next runtime archive has
69 intended files. Previous archive observations retain their original
68-file scope and source revision.

## Skill naming

All skill identifiers use existing names from the original 479-candidate
[backlog](backlog.md). The [skill index](../../.agents/skills/README.md)
records the current 24 active procedures and 9 passive detectors.
Directories, metadata, graph targets, and references use the same names.
Reviews and improvements have active procedures with their own output
and verification. Passive checks remain lightweight signals; `kind`
reflects actual execution rather than compensating for a mismatched
name. Naming alignment alone does not establish capability coverage.

## Skill semantics checkpoint

All 33 skills were reviewed against their names, backlog domains,
triggers, procedures, and completion criteria. Fourteen needed content
or contract corrections: build analysis, component boundaries and
contracts, browser form behavior, four active review/improvement
procedures, CI impact, completeness, stale state, blast radius,
claim verification, and test-strategy completion. The remaining 19
retain their existing scoped procedures.

Build analysis now traces inputs and stages before recommending changes;
component contract design covers static and interactive consumers;
component boundaries concern responsibility and state ownership rather
than formatting. Accessibility, performance, component consistency, and
test-signal improvement are active procedures rather than renamed
passive warnings. Browser forms and stale state cover native and
synchronous behavior as well as enhanced or asynchronous paths.

Evidence is content inspection, author walkthroughs of representative
positive, non-trigger, and failure cases, and structural/lint checks.
This is not an independent evaluation or cross-host behavioral trial.
The original candidate inventory remains unchanged.

## Portable CI/CD checkpoint

`rules/ci-cd.md` and `skills/active/analyze-build-pipeline` cover repository
inputs, build stages, local/CI differences, release gates, and artifact
contracts. Hooks and dependency automation are inspected when relevant
to that build path. Route pipeline analysis through this parent;
running existing checks alone remains the responsibility of
`verify-before-claiming`.

This provides bounded coverage for `analyze-build-pipeline`,
`check-ci-impact`, and `review-release-diff`. It does not implement a
provider adapter or a production deployment strategy. The guidance is
authored and structurally checked; cross-host behavioral trials remain
pending.

## Scoped source import checkpoint

The user-approved `info-for-ghost` import implements portable procedures and
structural checks, not completion of a roadmap phase. Review, test strategy,
refactoring, migration planning, handover, research, documentation, and lesson
capture have authored artifacts. The import originally added five passive
signals. The current catalog promotes `improve-test-signal` to an active
procedure, retains four of those checks as passive, and separately promotes
accessibility, performance and component-consistency review. Representative
runtime trials and outcome evaluation remain pending.

| Backlog candidates                                                                                                                                                                                           | GHOST artifact                                                                                                                                             | Kind               | Status      | Routing                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------- | ---------------------------------------------- |
| `review-code-change`, `review-pull-request`, `review-diff-not-files`, `review-for-correctness`, `review-for-overengineering`                                                                                 | `skills/active/review-code-change`                                                                                                                         | active             | implemented | scoped review or received feedback             |
| `design-test-strategy`, `choose-test-level`, `write-regression-test`, `test-edge-cases`, `test-error-paths`, `test-concurrency`, `reduce-test-brittleness`, `improve-test-signal`, `review-mocking-strategy` | `skills/active/design-test-strategy`, `skills/active/improve-test-signal`, `templates/manual-test.md`                                                      | active + template  | covered     | unclear proof or material regression risk      |
| `refactor-without-behavior-change`, `incremental-refactor`, `reduce-coupling`, `reduce-complexity`                                                                                                           | `skills/active/refactor-without-behavior-change`                                                                                                           | active             | implemented | authorized structural change                   |
| `plan-migration`, `design-backward-compatible-migration`, `track-migration-progress`, `write-migration-guide`, `write-runbook`                                                                               | `skills/active/plan-migration`, `templates/migration-plan.md`                                                                                              | active + template  | covered     | overlap, state preservation, or recovery needs |
| `research-unknown-api`, `read-library-source`, `compare-docs-with-runtime`, `create-minimal-reproduction`, `verify-library-api`                                                                              | `skills/active/research-unknown-api`, `knowledge/web-research-and-source-evaluation.md`                                                                    | active + knowledge | covered     | decision-relevant API uncertainty              |
| `write-maintainer-notes`, `explain-code-decision`                                                                                                                                                            | `skills/active/write-maintainer-notes`, `templates/change-handover.md`                                                                                     | active + template  | covered     | review handover or PR-description draft        |
| `update-documentation`, `write-architecture-note`, `write-adr`, `document-invariants`                                                                                                                        | `skills/active/update-documentation`, `knowledge/writing-and-review-communication.md`                                                                      | active + knowledge | covered     | requested technical Markdown or prose          |
| `extract-engineering-lessons`, `challenge-own-assumptions`, `find-counterexample`                                                                                                                            | `skills/active/extract-engineering-lessons`, `knowledge/skill-authoring-and-evaluation.md`                                                                 | active + knowledge | covered     | requested durable guidance from evidence       |
| `detect-overmocking`, `detect-leaky-abstraction`, `detect-complexity-creep`, `check-lockfile-impact`, `check-ci-impact`                                                                                      | `skills/passive/detect-overmocking`, `skills/passive/detect-leaky-abstraction`, `skills/passive/detect-complexity-creep`, `skills/passive/check-ci-impact` | passive            | covered     | material signal during existing work           |

`covered` denotes the bounded procedures represented by these artifacts; it does
not claim a complete general security, production, or test-design system. See
[source import record](../history/source-import.md) for the accepted scope,
exclusions, source records, and actual validation evidence.

## P0 runtime compatibility

Goal: make the same GHOST capability graph usable across the six selected
coding-agent runtimes without maintaining six copies of the rules.

| Runtime        | Core entry point                        | Adapter status                                    | Next validation                                   |
| -------------- | --------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| Codex          | `AGENTS.md` + `.agents/skills/`         | implemented                                       | run the representative workflow                   |
| Claude Code    | `CLAUDE.md` + host skills directory     | loader implemented; skills projection to validate | run the representative workflow                   |
| Cursor         | `.cursor/rules/` + `.cursor/skills/`    | planned thin projection                           | verify current discovery and invocation controls  |
| GitHub Copilot | custom instructions + `.agents/skills/` | planned direct path                               | verify cloud agent, CLI, and review surfaces      |
| Gemini CLI     | `GEMINI.md` + `.agents/skills/`         | planned direct path                               | verify workspace discovery and `/skills` behavior |
| OpenCode       | `AGENTS.md` + `.agents/skills/`         | planned direct path                               | verify passive-detector handling                  |

The runtime matrix and token-budget policy live in
`.agents/knowledge/runtime-adapters-and-context-budget.md`. P1 and P2 hosts are
intentionally not part of this slice.

## Phase 1 — cognitive core and repository understanding (P0)

Goal: make the agent able to build a reliable context model before changing
code.

### Phase 1: capability families

1. **Codebase understanding** — `map-codebase`, `identify-module-boundaries`,
   `trace-data-flow`, `trace-control-flow`, `trace-request-lifecycle`,
   `trace-event-lifecycle`, `trace-state-lifecycle`, `find-feature-ownership`,
   `find-domain-ownership`, `analyze-dependency-graph`,
   `find-coupling-hotspots`, `detect-circular-dependencies`,
   `identify-entry-points`, `identify-runtime-boundaries`,
   `identify-client-server-boundaries`, `identify-state-ownership`,
   `explain-module-responsibility`, `summarize-subsystem`,
   `build-system-mental-model`.

1. **Problem framing** — `clarify-engineering-task`, `extract-requirements`,
   `separate-symptom-from-problem`, `identify-invariants`,
   `identify-assumptions`, `identify-unknowns`, `define-success-criteria`,
   `define-non-goals`, `estimate-blast-radius`, `assess-change-risk`,
   `find-hidden-constraints`, `challenge-task-premise`, `reframe-problem`,
   `identify-source-of-truth`.

1. **Planning and self-critique** — `plan-code-change`, `split-large-change`,
   `sequence-dependent-changes`, `define-verification-plan`,
   `design-minimal-change`, `challenge-own-assumptions`,
   `compare-plan-with-implementation`, `check-task-completeness`,
   `identify-confidence-level`.

1. **Repository hygiene** — `inspect-project-guidelines`,
   `preserve-public-contracts`, `avoid-unrelated-changes`, `keep-diff-focused`,
   `check-generated-files`, `check-lockfile-impact`, `check-ci-impact`.

### Phase 1: deliverables

Authored in the recorded first slice; retain these as acceptance contracts.
Repeat the trial when relevant guidance or runtime changes, rather than adding
duplicate skills.

- Maintain `map-codebase` as an active parent skill with a repeatable
  output: module map, ownership map, runtime boundaries, data/control flows,
  unknowns, and evidence links.

- Maintain `clarify-engineering-task` as the existing framing skill; its routing
  remains conditional on material ambiguity.

- Maintain the authored plan-versus-implementation self-critique in
  `verify-before-claiming`.

- Maintain the existing repository-context checkpoint template.

### Phase 1: done when

For an unfamiliar repository, the agent can explain where a change belongs,
which boundary it crosses, what it must not touch, and how success will be
verified before editing.

## Phase 2 — safe change execution (P0/P1)

Goal: improve the reliability of implementation, debugging, refactoring, and
review workflows.

### Phase 2: capability families

- **Debugging:** reproduce/isolate failure, rank hypotheses, find root cause,
  debug async behavior, race conditions, state sync, hydration, network,
  caching, memory, performance, build, type, and test failures.

- **Implementation:** preserve contracts, follow local conventions, extend an
  existing abstraction, handle edge cases, idempotency, retries, cancellation,
  timeouts, error boundaries, and fallbacks.

- **Refactoring:** extract modules/domain logic, reduce coupling and complexity,
  replace boolean flags, simplify state/control flow, remove dead code, improve
  cohesion, and refactor incrementally.

- **Architecture and API:** design module/layer/domain boundaries, public and
  internal APIs, extension points, state architecture, error models, cache
  strategy, and backward-compatible changes.

- **Testing and review:** choose test level, write regression/contract tests,
  test error and concurrency paths, reduce brittleness, review mocks, review
  diffs rather than only files, and assess regression risk.

- **Git/change management:** analyze diffs, split commits, prepare clean
  commits, resolve conflicts, bisect regressions, backport, and review release
  diffs.

### Phase 2: deliverables

The parent procedures, active reviews/test improvement, scoped passive
checks and migration guidance are authored. Their remaining gate is
representative runtime evidence, not another implementation pass.

- Trial `debug-systematically` and `estimate-blast-radius` procedure checklists.

- Trial `review-code-change` and `design-test-strategy`, including non-triggers.

- Exercise active `improve-test-signal` on a weak assertion and a meaningful
  negative case. Check overmocking, abstraction, complexity and CI-impact
  detectors on positive and no-signal cases.

- Exercise compatibility and rollback planning through `plan-migration`, while
  preserving the boundary between a plan and authorized execution.

- Capture the selected route, actual result and friction before narrowly
  revising existing artifacts (C03–C05).

### Phase 2: done when

The agent can move from observed failure or requested change to a bounded plan,
small implementation, regression check, and honest completion report.

## Phase 3 — frontend platform depth (P1)

Personal learning can start alongside Phase 2 validation. Begin with values,
references, identity, mutation and scope, then closures and async execution. Use
the planned five weekly study hours and advance on unfamiliar-example
understanding. GHOST capability promotion and human learning have separate
evidence records; an authored model does not mark the learner as proficient
(C07–C10).

Goal: prevent React/Next.js fluency from masking gaps in JavaScript, browser,
network, and rendering fundamentals.

### Phase 3: capability families

- **TypeScript:** domain types, discriminated unions, exhaustiveness, runtime
  validation boundaries, inference, branded types, and library types.

- **JavaScript:** event loop, microtasks, closures, prototypes, module loading,
  garbage collection, identity, mutation, and async control flow.

- **Browser:** layout, paint, compositing, DOM cost, event propagation, storage,
  navigation, scheduling, observers, forms, focus, scroll, and worker
  architecture.

- **React:** render tracing, state colocation, component boundaries, hook
  design, effect misuse, derived state, concurrency, Suspense, context cost,
  keys, and separation of UI/domain logic.

- **Next.js:** server/client boundaries, route architecture, caching,
  revalidation, data fetching, streaming, route handlers, hydration, bundles,
  metadata, and runtime fit.

- **State management:** state classification, server/client separation,
  normalization, state machines, transitions, stale/duplicated state, optimistic
  updates, events, and cache-as-state.

### Phase 3: deliverables

Already authored: `review-component-boundaries`,
`analyze-form-behavior`, `review-metadata-strategy` and
`detect-stale-state`, supported by existing knowledge. Their scope does
not establish a complete platform curriculum or close C07–C10.
Remaining work:

- Add knowledge/mental-model documents before adding many active procedures.

- Consider `analyze-browser-rendering-pipeline`, `analyze-react-rendering`
  and `analyze-next-rendering-model` only when the models and repeated tasks
  justify standalone procedures under C16.

- Keep framework-specific procedures dependent on platform-level mental models.

- Add passive detectors for effect misuse, duplicated state, unsafe type
  assertions, hydration risk, and client-boundary expansion.

### Phase 3: done when

The agent can explain the underlying JavaScript/browser mechanism before
proposing a React or Next.js fix, and can identify when a framework abstraction
is hiding a platform problem.

## Phase 4 — quality and user-facing correctness (P1)

Goal: make performance, network behavior, security, CSS, accessibility, and
design-system quality part of the implementation contract.

### Phase 4: capability families

- **Performance:** profile before optimizing, bottlenecks, main-thread work,
  long tasks, bundle/code splitting, waterfalls, critical rendering, LCP/INP/
  CLS, memory, images, fonts, data fetching, caching, and regression checks.

- **Networking:** HTTP lifecycle, cache headers, CORS, cookies, auth flow,
  request waterfalls, retries, timeouts, deduplication, HTTP/2/3, CDN, browser
  cache, and service workers.

- **Security:** XSS, CSRF, CORS, CSP, token/cookie storage, auth, redirects,
  user content, third-party scripts, dependencies, trust boundaries, and client
  secrets.

- **CSS/UI:** layout, stacking, overflow, container queries, responsiveness,
  tokens, specificity, animation performance, layout contracts, and fragility.

- **Accessibility:** semantic HTML, keyboard/focus flow, screen readers, ARIA,
  forms, modals, live regions, color-independent state, and end-to-end flows.

- **Design systems:** component contracts, tokens, variants, composition, slots,
  consistency, duplication, deprecation, and migration.

### Phase 4: deliverables

Already authored: `review-for-accessibility`, `review-for-performance`,
`design-component-contract` and `review-component-consistency`. The first,
second and fourth now have full active review procedures. They produce
scoped findings; they do not establish a whole-product audit capability.
Remaining work:

- Exercise current procedures on real user paths and measurements (C12),
  plus packed-package consumers where relevant (C11).

- Consider `profile-before-optimizing`, `review-frontend-security`,
  `audit-accessibility` or `review-design-system-component` only if the
  existing procedure cannot cover a repeated need and C16 is satisfied.

- Connect material signals conditionally; add a risk-specific template
  only when existing verification/manual-test templates omit needed proof.

### Phase 4: done when

The agent can identify the relevant user-facing quality dimension, explain its
mechanism, choose a proportionate check, and avoid declaring a contextual rule
as a universal platform guarantee.

## Phase 5 — production and system evolution (P2)

Goal: extend GHOST from local code changes to long-lived system behavior.

### Phase 5: capability families

- **Dependency management:** evaluate libraries, risk and lock-in, upgrades,
  removal, transitive dependencies, duplicate dependencies, footprint, and
  build-vs-buy.

- **Build tooling:** bundler output, module resolution, tree shaking, chunking,
  build time, transpilation, source maps, environment variables, and monorepo
  graphs.

- **Observability:** error logging, client metrics, structured events, tracing
  context, telemetry analysis, production triage, client/server correlation,
  debuggable features, and signal-to-noise.

- **Reliability:** fallback/recovery paths, failure-mode analysis, idempotency,
  timeout/retry behavior, partial failure, and offline behavior.

- **Data modeling:** view models, transport/domain separation, cache keys,
  identity, nullability, transitions, and data duplication.

- **Migration and technical debt:** framework/component/state/routing/design
  system migrations, strangler migration, debt classification, hotspots,
  paydown, maintenance cost, and complexity creep.

### Phase 5: deliverables

Already authored: portable CI/CD rules, `analyze-build-pipeline`,
`check-ci-impact`, `plan-migration` and the migration-plan template.
The GHOST release path is exercised; this does not establish deployment
or recovery evidence for an adopting product. Remaining work:

- Trial these procedures on a real operational change (C15). Add a runbook
  when that case needs one; do not recreate the existing migration template.

- Require rollback, observability, and operational ownership in production
  change plans.

- Add passive detectors for dependency lock-in, build graph expansion, missing
  fallback paths, and unowned telemetry.

### Phase 5: done when

Material changes include operational consequences, recovery behavior, ownership,
and migration state—not only local code correctness.

## Phase 6 — Principal-level judgment and learning loop (P1/P2)

This phase is a capability family, not a requirement to postpone systemic
reasoning. Apply alternatives including doing nothing, team/product
consequences, maintenance cost, reversibility, adoption and falsification in
current planning and review (C13). Standalone promotion still needs repeated
evidence.

Goal: encode the reasoning that distinguishes senior implementation from
principal-level system judgment.

### Phase 6: capability families

- **Systemic decisions:** challenge requirements, evaluate systemic and
  organizational impact, long-term cost, cognitive load, operational complexity,
  reversibility, optionality, standardization, local/global optima, pattern
  proliferation, and scaling limits.

- **Self-critique:** challenge assumptions, find counterexamples and missed edge
  cases, verify claims and library APIs, distinguish known from assumed, check
  completeness, perform pre-submit review, and identify confidence.

- **Documentation:** architecture notes, ADRs, public API docs, complex
  behavior, decisions, migrations, debugging guides, runbooks, maintainer notes,
  and invariants.

- **Learning:** research unknown APIs, read library/framework source, compare
  docs with runtime, create minimal reproductions, derive behavior
  experimentally, validate mental models, study patterns, and extract lessons.

### Phase 6: deliverables

Already authored: `verify-before-claiming`, `check-task-completeness`,
`research-unknown-api`, `extract-engineering-lessons`,
`update-documentation` and `write-maintainer-notes`. Claim verification
now applies to research/review as well as implemented changes. Remaining work:

- Practice decision and counterexample checks through existing planning/review
  procedures (C13). Promote `evaluate-systemic-impact` or
  `critique-own-solution` only when independent value satisfies C16.

- Trial the existing `research-unknown-api`; it is already authored.

- Cover architecture notes through `update-documentation` first; promote
  `write-architecture-note` only when independent routing is justified.

- Make every active skill emit confidence, unresolved assumptions, and what
  evidence would change the decision.

### Phase 6: done when

The agent can explain not only whether a solution works, but what precedent it
creates, what complexity it adds, who will maintain it, how reversible it is,
and what would falsify the recommendation.

## Promotion policy for the 479 candidates

A candidate becomes a standalone `SKILL.md` only if at least two of these are
true:

1. it has a distinct trigger and completion condition;
1. it recurs across repositories or tasks;
1. it requires a different mental model or verification method;
1. it is useful as a separately routable capability;
1. a passive detector can escalate to it with a clear threshold.

Otherwise keep it as a checklist under a domain skill or as knowledge. This
prevents graph explosion and keeps progressive activation meaningful.

## Backlog metadata

Every promoted capability should record:

Standalone skills use the full record below. A candidate covered by an existing
rule, parent skill, detector, or knowledge file uses the compact coverage table
above and inherits that artifact's graph and verification contract.

```yaml
name: <stable name>
description: <one-sentence routing description>
kind: rule | active | passive | knowledge
priority: P0 | P1 | P2 | P3
trigger: <observable condition>
requires: [<capability>]
may-trigger: [<capability>]
verification: <evidence required>
owner: <human or team, when applicable>
status: proposed | designed | covered | implemented | verified | deprecated
evidence: <record binding checks/trials to artifact state, runtime version, date, and
  limits>
coverage: standalone | parent | rule | knowledge | detector
artifact: <relative path or list of paths>
```

## Next implementation slice

1. Keep completed tooling, archive and catalog checks green (C01–C02,
   C17–C19). Do not reimplement or reopen these without relevant changes.

1. Trial the authored Phase 2 workflows on one real repository and one named
   host, including non-triggers and explicit action boundaries (C03).

1. Record routing cost and failures, make narrow corrections, then extend the
   evidence matrix to the remaining target hosts (C04–C05, C14). Exercise
   PR/dependency automation on the next eligible event (C20).

1. Run the personal fundamentals learning loop in parallel within the existing
   study budget; apply systemic decision questions to current work (C07–C10,
   C13).

The repository CI/archive gate is already met. The remaining slice closes
when representative agent workflows have observed outcomes for the current
contracts. Documentation authorship is not behavioral acceptance. The
[checklist](checklist.md) owns completed work and remaining actions; this
roadmap owns sequencing and promotion policy.

## Source boundary

The canonical backlog is this repository's [backlog](backlog.md). Its initial
inventory comes from the user-provided attachment:

`/Users/nikkeyl/.codex/attachments/67062245-ee1b-4681-9702-506aca0cd323/pasted-text.txt`

Its labels and candidate names are treated as design input. They do not override
`AGENTS.md`, repository conventions, user scope, safety constraints, or
evidence-based verification.
