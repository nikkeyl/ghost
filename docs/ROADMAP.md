# GHOST roadmap

Reviewed: 2026-11-05, against baseline `6ad5f08`.

Status: the Phase 0 artifacts are authored. The first Phase 1 slice has a
historically recorded repository trial; this audit did not rerun it. Phase 2
procedures are authored, but representative runtime trials remain pending. The scoped
metadata promotion does not establish Phase 3 completion. Discovery and
passive-detector behavior across the six P0 target runtimes remain unverified.

The next project priority is checker coverage and one-host behavioral evidence. The
author's parallel learning priority is JavaScript/Web depth, not catalog size. See
the [audit](./audit-2026-11-05.md),
[knowledge and approach profile](./knowledge-and-approaches.md), and
[actionable checklist](./project-checklist.md) for evidence and acceptance criteria.

## Evidence gates and current priorities

Keep three claims separate: an artifact exists, a structural check passes, and a
procedure produces the expected behavior in a named runtime. None establishes the
author's independent proficiency. Historical trials retain their original scope;
rerun them when a relevant artifact or runtime changes.

| Workstream          | Current evidence                                                         | Next gate                                                                      | Checklist |
| ------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | --------- |
| Core catalog        | 6 rules, 16 knowledge files, 19 active skills, 13 detectors, 8 templates | Enforce authoring contracts in CI; five invalid copies currently pass          | C01–C02   |
| Phase 1/2 behavior  | Phase 1 trial recorded; Phase 2 procedures authored                      | Representative positive, non-trigger and failure cases on one host             | C03       |
| Runtime portability | Six targets named; AGENTS/CLAUDE loaders present                         | Versioned discovery, routing and passive-detector matrix, one host at a time   | C04–C05   |
| Platform depth      | Narrow frontend guidance exists; broader procedures proposed             | JS predictions and browser/network experiments before framework recipes        | C07–C10   |
| Quality / packaging | Existing review cues and historical package-audit leads                  | Consumer, accessibility, performance and trust-boundary evidence               | C11–C12   |
| Systemic judgment   | Reasoning/evidence rules and candidate inventory                         | Apply alternatives, team cost, reversibility and adoption to current decisions | C13–C14   |

The existing CI command checks skill metadata and links in root documents only. The
broader inspection described by the source import was a separate historical check,
not the present CI contract. This audit inspected headings, index coverage and 79
skill/knowledge graph relations without claiming runtime validation.

## Purpose

The attached capability inventory is the long-term backlog for GHOST. It contains 479
candidate procedures across 35 engineering domains, from `map-codebase` and
`trace-data-flow` to `evaluate-systemic-impact`, `critique-own-solution`, and
`research-unknown-api`.

The inventory is a source of candidates, not a command to create 479 isolated skills
immediately. GHOST should grow as a progressive capability graph:

```text
candidate procedure
  → domain family
  → parent skill / checklist
  → evidence-backed promotion
  → standalone skill only when justified
```

The complete imported inventory is preserved in
[`ROADMAP-BACKLOG.md`](./ROADMAP-BACKLOG.md). This document is the prioritized
implementation plan; the appendix is the exhaustive candidate list.

## Current baseline — Phase 0: foundation (authored)

Already implemented in `.agents/`:

- 6 persistent rules for scope, evidence, Git/review, frontend contracts,
  disagreement, and data/failure contracts.
- 16 knowledge files covering activation, source-derived frontend patterns, web
  document metadata, data loading and failure, async UI state, Next.js Server
  Actions, runtime/context adaptation, content trust boundaries, and general
  engineering patterns, plus behavior preservation, research, writing, skill
  authoring, personal preferences, context hygiene, and optional integrations.
- 19 active skills for planning, impact analysis, minimal implementation, debugging,
  verification, codebase understanding, task clarification, React component review,
  custom-control review, form-contract review, and metadata strategy review, plus
  diff review, test strategy, behavior-preserving refactoring, migration planning,
  API research, handover, prose, and lesson capture.
- 13 passive detectors for scope drift, breaking changes, missing verification,
  accessibility, performance, architecture, component drift, async races, weak test
  signal, overmocking, abstraction leaks, complexity creep, and build impact.
- Progressive activation limits: 5 active skills by default, 2 graph hops.
- P0 runtime target set: Codex, Claude Code, Cursor, GitHub Copilot, Gemini CLI, and
  OpenCode. Runtime-specific files remain thin adapters over the portable `.agents`
  core.

The artifact-level Phase 0 criteria are present: each active skill has a trigger,
goal, investigation, decision rules, actions, verification, and completion criteria.
That is structural evidence; host discovery and procedure outcomes have separate
gates above.

## Phase 1 checkpoint — first implementation slice (historically trialled)

The first Phase 1 slice is implemented and trialled on the real `time-to-your-hair`
repository:

- `understand-codebase` builds a scoped module, ownership, runtime-boundary, flow,
  source-of-truth, unknowns, and evidence model.
- `clarify-engineering-task` turns materially ambiguous requests or symptoms into a
  bounded contract with invariants, non-goals, and success criteria.
- `.agents/templates/repository-context.md` provides the durable checkpoint output
  shape.
- `verify-change` compares the plan with the implementation and records challenged
  assumptions or counterexamples.
- The trial preserved the prototype/production boundary and exposed existing
  repository state as a risk instead of treating it as a clean baseline.

The trial also confirmed that a repository without `AGENTS.md` or `CLAUDE.md` can
still be modelled from its project brief, package/build configuration, entry points,
and runtime configuration, but the missing adapter guidance must remain an explicit
uncertainty.

## Evidence-backed promotions and backlog coverage

The following capabilities were promoted from user-confirmed cross-project patterns
without creating one skill per observation:

- `review-form-contract` groups form validation, lifecycle, state ownership,
  server-boundary, and primary/secondary failure procedures.
- `detect-async-race` observes debounce, cancellation, freshness, and stale response
  risks during user-driven asynchronous work.
- `async-ui-state-and-cancellation`, `nextjs-server-actions`,
  `content-trust-boundaries`, and `engineering-patterns` preserve the underlying
  mental models and evidence.
- `review-metadata-strategy` and `web-document-metadata` promote the route-level
  metadata, indexing, localization, social-preview, and structured-data review from
  the candidate backlog.

These promotions are routed through the existing parent workflow and do not change
the default activation budget.

The following backlog candidates are now represented in GHOST. `covered` means the
candidate is implemented by an existing rule, parent skill, detector, or knowledge
file; it is intentionally not a new standalone skill.

| Backlog candidates                                                                                                                                                                | GHOST artifact                                                                                                  | Kind                      | Status      | Routing                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------- | ----------- | ------------------------------------------------------------------------------- |
| `review-metadata-strategy`                                                                                                                                                        | `skills/active/review-metadata-strategy`, `knowledge/web-document-metadata.md`                                  | active + knowledge        | implemented | page metadata, indexability, locale, social preview, or structured data changes |
| `implement-cancellation`                                                                                                                                                          | `knowledge/async-ui-state-and-cancellation.md`, `skills/passive/detect-async-race`                              | knowledge + passive       | covered     | `debug-systematically` or async signal                                          |
| `analyze-module-loading`                                                                                                                                                          | `knowledge/data-loading-and-failure-model.md`, `skills/passive/detect-performance-risk`                         | knowledge + passive       | covered     | a dependency or renderer may be loaded too broadly                              |
| `analyze-async-control-flow`, `review-state-transitions`, `detect-stale-state`                                                                                                    | `knowledge/async-ui-state-and-cancellation.md`, `skills/passive/detect-async-race`                              | knowledge + passive       | covered     | user-driven async state can become obsolete                                     |
| `choose-server-vs-client-component`, `review-server-component-boundaries`, `identify-client-server-boundaries`                                                                    | `rules/40-frontend-contracts.md`, `skills/active/review-component-anatomy`                                      | rule + active             | covered     | React/Next.js boundary is in scope                                              |
| `analyze-server-actions`                                                                                                                                                          | `knowledge/nextjs-server-actions.md`, `rules/40-frontend-contracts.md`                                          | knowledge + rule          | covered     | Next.js mutation is in scope                                                    |
| `review-data-fetching-strategy`, `optimize-data-fetching`, `optimize-caching`                                                                                                     | `rules/50-data-and-failure-contracts.md`, `knowledge/data-loading-and-failure-model.md`                         | rule + knowledge          | covered     | data boundary or freshness risk                                                 |
| `design-layer-boundaries`, `design-domain-boundaries`                                                                                                                             | `rules/20-change-scope.md`, `skills/passive/detect-architecture-drift`                                          | rule + passive            | covered     | ownership or FSD layer is uncertain                                             |
| `identify-state-owner`, `identify-state-ownership`, `classify-state`, `separate-server-and-client-state`, `design-state-architecture`                                             | `knowledge/data-loading-and-failure-model.md`, `knowledge/engineering-patterns.md`                              | knowledge                 | covered     | state ownership is uncertain                                                    |
| `design-error-model`, `design-failure-isolation`, `review-partial-failure`, `implement-fallback-behavior`                                                                         | `rules/50-data-and-failure-contracts.md`, `knowledge/data-loading-and-failure-model.md`                         | rule + knowledge          | covered     | primary/partial/secondary outcome exists                                        |
| `review-user-generated-content`, `identify-trust-boundaries`                                                                                                                      | `knowledge/content-trust-boundaries.md`                                                                         | knowledge                 | covered     | external content reaches a rendering or behavior sink                           |
| `design-data-flow`, `design-cache-strategy`, `design-concurrency-model`                                                                                                           | `knowledge/data-loading-and-failure-model.md`, `knowledge/async-ui-state-and-cancellation.md`                   | knowledge                 | covered     | data, freshness, or race behavior needs a model                                 |
| `review-data-shape`, `normalize-api-data`, `design-view-model`, `separate-domain-and-transport-model`                                                                             | `knowledge/data-loading-and-failure-model.md`, `knowledge/engineering-patterns.md`                              | knowledge                 | covered     | transport and UI ownership need an explicit boundary                            |
| `review-form-accessibility`, `test-error-paths`, `test-concurrency`                                                                                                               | `skills/active/review-form-contract`                                                                            | active                    | covered     | form or submit pipeline is in scope                                             |
| `design-component-api`, `design-extension-points`, `review-component-boundaries`, `review-hook-design`, `review-variant-model`, `design-slot-api`, `separate-ui-and-domain-logic` | `rules/40-frontend-contracts.md`, `skills/active/review-component-anatomy`, `knowledge/engineering-patterns.md` | rule + active + knowledge | covered     | component or UI/domain contract is in scope                                     |
| `extract-domain-logic`, `remove-duplication`, `reduce-complexity`, `improve-module-cohesion`, `incremental-refactor`                                                              | `rules/20-change-scope.md`, `skills/active/implement-minimal-change`                                            | rule + active             | covered     | duplication or complexity is demonstrated                                       |
| `split-commit`, `prepare-clean-commit`, `review-commit-history`                                                                                                                   | `rules/30-git-and-review.md`                                                                                    | rule                      | covered     | commit or review boundary is in scope                                           |
| `review-design-token-usage`, `design-token-architecture`                                                                                                                          | `rules/40-frontend-contracts.md`, `skills/active/review-component-anatomy`                                      | rule + active             | covered     | repeated visual meaning is demonstrated                                         |
| `define-verification-plan`, `design-minimal-change`                                                                                                                               | `skills/active/understand-and-plan-change`, `skills/active/verify-change`                                       | active                    | covered     | a change needs a bounded plan or risk-appropriate check                         |

Broader platform, security, and production families remain planned.
`understand-codebase` is implemented in the Phase 1 slice described above. The
remaining families have candidate names in the backlog, but the current evidence does
not yet justify claiming complete independent workflows for them.

## Scoped source import checkpoint

The user-approved `info-for-ghost` import implements portable procedures and
structural checks, not completion of a roadmap phase. Review, test strategy,
refactoring, migration planning, handover, research, documentation, and lesson
capture have authored artifacts. Five new passive detectors cover the planned Phase 2
signals. Representative runtime trials and outcome evaluation are pending.

| Backlog candidates                                                                                                                                                                                           | GHOST artifact                                                                                                                                                 | Kind               | Status      | Routing                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------- | ---------------------------------------------- |
| `review-code-change`, `review-pull-request`, `review-diff-not-files`, `review-for-correctness`, `review-for-overengineering`                                                                                 | `skills/active/review-code-change`                                                                                                                             | active             | implemented | scoped review or received feedback             |
| `design-test-strategy`, `choose-test-level`, `write-regression-test`, `test-edge-cases`, `test-error-paths`, `test-concurrency`, `reduce-test-brittleness`, `improve-test-signal`, `review-mocking-strategy` | `skills/active/design-test-strategy`, `templates/manual-test.md`                                                                                               | active + template  | covered     | unclear proof or material regression risk      |
| `refactor-without-behavior-change`, `incremental-refactor`, `reduce-coupling`, `reduce-complexity`                                                                                                           | `skills/active/refactor-without-behavior-change`                                                                                                               | active             | implemented | authorized structural change                   |
| `plan-migration`, `design-backward-compatible-migration`, `track-migration-progress`, `write-migration-guide`, `write-runbook`                                                                               | `skills/active/plan-migration`, `templates/migration-plan.md`                                                                                                  | active + template  | covered     | overlap, state preservation, or recovery needs |
| `research-unknown-api`, `read-library-source`, `compare-docs-with-runtime`, `create-minimal-reproduction`, `verify-library-api`                                                                              | `skills/active/research-unknown-api`, `knowledge/web-research-and-source-evaluation.md`                                                                        | active + knowledge | covered     | decision-relevant API uncertainty              |
| `write-maintainer-notes`, `explain-code-decision`                                                                                                                                                            | `skills/active/write-maintainer-notes`, `templates/change-handover.md`                                                                                         | active + template  | covered     | review handover or PR-description draft        |
| `update-documentation`, `write-architecture-note`, `write-adr`, `document-invariants`                                                                                                                        | `skills/active/update-documentation`, `knowledge/writing-and-review-communication.md`                                                                          | active + knowledge | covered     | requested technical Markdown or prose          |
| `extract-engineering-lessons`, `challenge-own-assumptions`, `find-counterexample`                                                                                                                            | `skills/active/extract-engineering-lessons`, `knowledge/skill-authoring-and-evaluation.md`                                                                     | active + knowledge | covered     | requested durable guidance from evidence       |
| `detect-overmocking`, `detect-leaky-abstraction`, `detect-complexity-creep`, `check-lockfile-impact`, `check-ci-impact`                                                                                      | `skills/passive/detect-overmocking`, `skills/passive/detect-leaky-abstraction`, `skills/passive/detect-complexity-creep`, `skills/passive/detect-build-impact` | passive            | covered     | material signal during existing work           |

`covered` denotes the bounded procedures represented by these artifacts; it does not
claim a complete general security, production, or test-design system. See
[`info-for-ghost-import.md`](./info-for-ghost-import.md) for the accepted scope,
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

Goal: make the agent able to build a reliable context model before changing code.

### Capability families

1. **Codebase understanding** — `map-codebase`, `identify-module-boundaries`,
   `trace-data-flow`, `trace-control-flow`, `trace-request-lifecycle`,
   `trace-event-lifecycle`, `trace-state-lifecycle`, `find-feature-ownership`,
   `find-domain-ownership`, `analyze-dependency-graph`, `find-coupling-hotspots`,
   `detect-circular-dependencies`, `identify-entry-points`,
   `identify-runtime-boundaries`, `identify-client-server-boundaries`,
   `identify-state-ownership`, `explain-module-responsibility`,
   `summarize-subsystem`, `build-system-mental-model`.
2. **Problem framing** — `clarify-engineering-task`, `extract-requirements`,
   `separate-symptom-from-problem`, `identify-invariants`, `identify-assumptions`,
   `identify-unknowns`, `define-success-criteria`, `define-non-goals`,
   `estimate-blast-radius`, `assess-change-risk`, `find-hidden-constraints`,
   `challenge-task-premise`, `reframe-problem`, `identify-source-of-truth`.
3. **Planning and self-critique** — `plan-code-change`, `split-large-change`,
   `sequence-dependent-changes`, `define-verification-plan`, `design-minimal-change`,
   `challenge-own-assumptions`, `compare-plan-with-implementation`,
   `check-task-completeness`, `identify-confidence-level`.
4. **Repository hygiene** — `inspect-project-guidelines`,
   `preserve-public-contracts`, `avoid-unrelated-changes`, `keep-diff-focused`,
   `check-generated-files`, `check-lockfile-impact`, `check-ci-impact`.

### Deliverables

Authored in the recorded first slice; retain these as acceptance contracts. Repeat
the trial when relevant guidance or runtime changes, rather than adding duplicate
skills.

- Maintain `understand-codebase` as an active parent skill with a repeatable output:
  module map, ownership map, runtime boundaries, data/control flows, unknowns, and
  evidence links.
- Maintain `clarify-engineering-task` as the existing framing skill; its routing
  remains conditional on material ambiguity.
- Maintain the authored plan-versus-implementation self-critique in `verify-change`.
- Maintain the existing repository-context checkpoint template.

### Done when

For an unfamiliar repository, the agent can explain where a change belongs, which
boundary it crosses, what it must not touch, and how success will be verified before
editing.

## Phase 2 — safe change execution (P0/P1)

Goal: improve the reliability of implementation, debugging, refactoring, and review
workflows.

### Capability families

- **Debugging:** reproduce/isolate failure, rank hypotheses, find root cause, debug
  async behavior, race conditions, state sync, hydration, network, caching, memory,
  performance, build, type, and test failures.
- **Implementation:** preserve contracts, follow local conventions, extend an
  existing abstraction, handle edge cases, idempotency, retries, cancellation,
  timeouts, error boundaries, and fallbacks.
- **Refactoring:** extract modules/domain logic, reduce coupling and complexity,
  replace boolean flags, simplify state/control flow, remove dead code, improve
  cohesion, and refactor incrementally.
- **Architecture and API:** design module/layer/domain boundaries, public and
  internal APIs, extension points, state architecture, error models, cache strategy,
  and backward-compatible changes.
- **Testing and review:** choose test level, write regression/contract tests, test
  error and concurrency paths, reduce brittleness, review mocks, review diffs rather
  than only files, and assess regression risk.
- **Git/change management:** analyze diffs, split commits, prepare clean commits,
  resolve conflicts, bisect regressions, backport, and review release diffs.

### Deliverables

The parent procedures, review/test skills, five passive signals and migration
guidance listed below are authored. Their remaining gate is representative runtime
evidence, not another implementation pass.

- Trial `debug-systematically` and `analyze-change-impact` procedure checklists.
- Trial `review-code-change` and `design-test-strategy`, including non-triggers.
- Exercise test-signal, overmocking, abstraction, complexity and build-impact
  detectors on positive and no-signal cases.
- Exercise compatibility and rollback planning through `plan-migration`, while
  preserving the boundary between a plan and authorized execution.
- Capture the selected route, actual result and friction before narrowly revising
  existing artifacts (C03–C05).

### Done when

The agent can move from observed failure or requested change to a bounded plan, small
implementation, regression check, and honest completion report.

## Phase 3 — frontend platform depth (P1)

Personal learning can start alongside Phase 2 validation. Begin with values,
references, identity, mutation and scope, then closures and async execution. Use the
planned five weekly study hours and advance on unfamiliar-example understanding.
GHOST capability promotion and human learning have separate evidence records; an
authored model does not mark the learner as proficient (C07–C10).

Goal: prevent React/Next.js fluency from masking gaps in JavaScript, browser,
network, and rendering fundamentals.

### Capability families

- **TypeScript:** domain types, discriminated unions, exhaustiveness, runtime
  validation boundaries, inference, branded types, and library types.
- **JavaScript:** event loop, microtasks, closures, prototypes, module loading,
  garbage collection, identity, mutation, and async control flow.
- **Browser:** layout, paint, compositing, DOM cost, event propagation, storage,
  navigation, scheduling, observers, forms, focus, scroll, and worker architecture.
- **React:** render tracing, state colocation, component boundaries, hook design,
  effect misuse, derived state, concurrency, Suspense, context cost, keys, and
  separation of UI/domain logic.
- **Next.js:** server/client boundaries, route architecture, caching, revalidation,
  data fetching, streaming, route handlers, hydration, bundles, metadata, and runtime
  fit.
- **State management:** state classification, server/client separation,
  normalization, state machines, transitions, stale/duplicated state, optimistic
  updates, events, and cache-as-state.

### Deliverables

- Add knowledge/mental-model documents before adding many active procedures.
- Create parent active skills for browser rendering, React rendering, and the Next.js
  rendering model.
- Keep framework-specific procedures dependent on platform-level mental models.
- Add passive detectors for effect misuse, duplicated state, unsafe type assertions,
  hydration risk, and client-boundary expansion.

### Done when

The agent can explain the underlying JavaScript/browser mechanism before proposing a
React or Next.js fix, and can identify when a framework abstraction is hiding a
platform problem.

## Phase 4 — quality and user-facing correctness (P1)

Goal: make performance, network behavior, security, CSS, accessibility, and
design-system quality part of the implementation contract.

### Capability families

- **Performance:** profile before optimizing, bottlenecks, main-thread work, long
  tasks, bundle/code splitting, waterfalls, critical rendering, LCP/INP/ CLS, memory,
  images, fonts, data fetching, caching, and regression checks.
- **Networking:** HTTP lifecycle, cache headers, CORS, cookies, auth flow, request
  waterfalls, retries, timeouts, deduplication, HTTP/2/3, CDN, browser cache, and
  service workers.
- **Security:** XSS, CSRF, CORS, CSP, token/cookie storage, auth, redirects, user
  content, third-party scripts, dependencies, trust boundaries, and client secrets.
- **CSS/UI:** layout, stacking, overflow, container queries, responsiveness, tokens,
  specificity, animation performance, layout contracts, and fragility.
- **Accessibility:** semantic HTML, keyboard/focus flow, screen readers, ARIA, forms,
  modals, live regions, color-independent state, and end-to-end flows.
- **Design systems:** component contracts, tokens, variants, composition, slots,
  consistency, duplication, deprecation, and migration.

### Deliverables

- Add active parent skills `profile-before-optimizing`, `review-frontend-security`,
  `audit-accessibility`, and `review-design-system-component`.
- Connect existing passive detectors to these parents only at a severity threshold.
- Add risk-specific verification templates for browser, accessibility, performance,
  and security claims.

### Done when

The agent can identify the relevant user-facing quality dimension, explain its
mechanism, choose a proportionate check, and avoid declaring a contextual rule as a
universal platform guarantee.

## Phase 5 — production and system evolution (P2)

Goal: extend GHOST from local code changes to long-lived system behavior.

### Capability families

- **Dependency management:** evaluate libraries, risk and lock-in, upgrades, removal,
  transitive dependencies, duplicate dependencies, footprint, and build-vs-buy.
- **Build tooling:** bundler output, module resolution, tree shaking, chunking, build
  time, transpilation, source maps, environment variables, and monorepo graphs.
- **Observability:** error logging, client metrics, structured events, tracing
  context, telemetry analysis, production triage, client/server correlation,
  debuggable features, and signal-to-noise.
- **Reliability:** fallback/recovery paths, failure-mode analysis, idempotency,
  timeout/retry behavior, partial failure, and offline behavior.
- **Data modeling:** view models, transport/domain separation, cache keys, identity,
  nullability, transitions, and data duplication.
- **Migration and technical debt:** framework/component/state/routing/design system
  migrations, strangler migration, debt classification, hotspots, paydown,
  maintenance cost, and complexity creep.

### Deliverables

- Add runbook and migration templates before adding specialized skills.
- Require rollback, observability, and operational ownership in production change
  plans.
- Add passive detectors for dependency lock-in, build graph expansion, missing
  fallback paths, and unowned telemetry.

### Done when

Material changes include operational consequences, recovery behavior, ownership, and
migration state—not only local code correctness.

## Phase 6 — Principal-level judgment and learning loop (P1/P2)

This phase is a capability family, not a requirement to postpone systemic reasoning.
Apply alternatives including doing nothing, team/product consequences, maintenance
cost, reversibility, adoption and falsification in current planning and review (C13).
Standalone promotion still needs repeated evidence.

Goal: encode the reasoning that distinguishes senior implementation from
principal-level system judgment.

### Capability families

- **Systemic decisions:** challenge requirements, evaluate systemic and
  organizational impact, long-term cost, cognitive load, operational complexity,
  reversibility, optionality, standardization, local/global optima, pattern
  proliferation, and scaling limits.
- **Self-critique:** challenge assumptions, find counterexamples and missed edge
  cases, verify claims and library APIs, distinguish known from assumed, check
  completeness, perform pre-submit review, and identify confidence.
- **Documentation:** architecture notes, ADRs, public API docs, complex behavior,
  decisions, migrations, debugging guides, runbooks, maintainer notes, and
  invariants.
- **Learning:** research unknown APIs, read library/framework source, compare docs
  with runtime, create minimal reproductions, derive behavior experimentally,
  validate mental models, study patterns, and extract lessons.

### Deliverables

- Add `evaluate-systemic-impact` and `critique-own-solution` as active parent skills
  with explicit evidence and counterexample steps.
- Trial the existing `research-unknown-api`; it is already authored.
- Cover architecture notes through `update-documentation` first; promote
  `write-architecture-note` only when independent routing is justified.
- Make every active skill emit confidence, unresolved assumptions, and what evidence
  would change the decision.

### Done when

The agent can explain not only whether a solution works, but what precedent it
creates, what complexity it adds, who will maintain it, how reversible it is, and
what would falsify the recommendation.

## Promotion policy for the 479 candidates

A candidate becomes a standalone `SKILL.md` only if at least two of these are true:

1. it has a distinct trigger and completion condition;
2. it recurs across repositories or tasks;
3. it requires a different mental model or verification method;
4. it is useful as a separately routable capability;
5. a passive detector can escalate to it with a clear threshold.

Otherwise keep it as a checklist under a domain skill or as knowledge. This prevents
graph explosion and keeps progressive activation meaningful.

## Backlog metadata

Every promoted capability should record:

Standalone skills use the full record below. A candidate covered by an existing rule,
parent skill, detector, or knowledge file uses the compact coverage table above and
inherits that artifact's graph and verification contract.

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
evidence:
  <record binding checks/trials to artifact state, runtime version, date, and limits>
coverage: standalone | parent | rule | knowledge | detector
artifact: <relative path or list of paths>
```

## Next implementation slice

1. Strengthen the existing standard-library checker and add focused invalid fixtures.
   Close the five demonstrated detection gaps before broadening its claims (C01–C02).
2. Trial the authored Phase 2 workflows on one real repository and one named host,
   including non-triggers and explicit action boundaries (C03).
3. Record routing cost and failures, make narrow corrections, then extend the
   evidence matrix to the remaining target hosts (C04–C05, C14).
4. Run the personal fundamentals learning loop in parallel within the existing study
   budget; apply systemic decision questions to current work (C07–C10, C13).

This slice is complete only when the checker rejects the targeted invalid cases and
representative workflows have observed outcomes. Documentation authorship is not
behavioral acceptance. The [checklist](./project-checklist.md) owns unfinished
actions; this roadmap owns sequencing and promotion policy.

## Source boundary

The canonical backlog is this repository's
[`ROADMAP-BACKLOG.md`](./ROADMAP-BACKLOG.md). Its initial inventory comes from the
user-provided attachment:

`/Users/nikkeyl/.codex/attachments/67062245-ee1b-4681-9702-506aca0cd323/pasted-text.txt`

Its labels and candidate names are treated as design input. They do not override
`AGENTS.md`, repository conventions, user scope, safety constraints, or
evidence-based verification.
