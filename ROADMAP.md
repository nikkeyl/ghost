# GHOST roadmap

Status: Phase 0 complete; Phase 1 is the next implementation target.

## Purpose

The attached capability inventory is the long-term backlog for GHOST. It
contains 444 candidate procedures across 35 engineering domains, from
`map-codebase` and `trace-data-flow` to `evaluate-systemic-impact`,
`critique-own-solution`, and `research-unknown-api`.

The inventory is a source of candidates, not a command to create 444 isolated
skills immediately. GHOST should grow as a progressive capability graph:

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

## Current baseline — Phase 0: foundation (complete)

Already implemented in `.agents/`:

- 6 persistent rules for scope, evidence, Git/review, frontend contracts,
  disagreement, and data/failure contracts.
- 8 knowledge files for activation, source-derived frontend patterns, the
  data-loading/failure model, async UI state, Next.js Server Actions,
  runtime/context adaptation, content trust boundaries, and user-confirmed
  Rose patterns.
- 8 active skills for planning, impact analysis, minimal implementation,
  debugging, verification, React component review, custom-control review, and
  form-contract review.
- 8 passive detectors for scope drift, breaking changes, missing verification,
  accessibility, performance, architecture, component drift, and async races.
- Progressive activation limits: 5 active skills by default, 2 graph hops.
- P0 runtime target set: Codex, Claude Code, Cursor, GitHub Copilot, Gemini
  CLI, and OpenCode. Runtime-specific files remain thin adapters over the
  portable `.agents` core.

Phase 0 exit criteria were met when each active skill had a trigger, goal,
investigation, decision rules, actions, verification, and completion criteria.

## Evidence-backed promotions and backlog coverage

The following capabilities were promoted from the user's confirmed patterns in
`501rose.kimdevs.ru` without creating one skill per observation:

- `review-form-contract` groups form validation, lifecycle, state ownership,
  server-boundary, and primary/secondary failure procedures.
- `detect-async-race` observes debounce, cancellation, freshness, and stale
  response risks during user-driven asynchronous work.
- `async-ui-state-and-cancellation`, `nextjs-server-actions`, and
  `content-trust-boundaries`, and `rose-derived-patterns` preserve the
  underlying mental models and evidence.

These promotions are routed through the existing parent workflow and do not
change the default activation budget.

The following backlog candidates are now represented in GHOST. `covered` means
the candidate is implemented by an existing rule, parent skill, detector, or
knowledge file; it is intentionally not a new standalone skill.

| Backlog candidates | GHOST artifact | Kind | Status | Routing |
|---|---|---|---|---|
| `implement-cancellation` | `knowledge/async-ui-state-and-cancellation.md`, `skills/passive/detect-async-race` | knowledge + passive | covered | `debug-systematically` or async signal |
| `analyze-module-loading` | `knowledge/data-loading-and-failure-model.md`, `skills/passive/detect-performance-risk` | knowledge + passive | covered | a dependency or renderer may be loaded too broadly |
| `analyze-async-control-flow`, `review-state-transitions`, `detect-stale-state` | `knowledge/async-ui-state-and-cancellation.md`, `skills/passive/detect-async-race` | knowledge + passive | covered | user-driven async state can become obsolete |
| `choose-server-vs-client-component`, `review-server-component-boundaries`, `identify-client-server-boundaries` | `rules/40-frontend-contracts.md`, `skills/active/review-component-anatomy` | rule + active | covered | React/Next.js boundary is in scope |
| `analyze-server-actions` | `knowledge/nextjs-server-actions.md`, `rules/40-frontend-contracts.md` | knowledge + rule | covered | Next.js mutation is in scope |
| `review-data-fetching-strategy`, `optimize-data-fetching`, `optimize-caching` | `rules/50-data-and-failure-contracts.md`, `knowledge/data-loading-and-failure-model.md` | rule + knowledge | covered | data boundary or freshness risk |
| `design-layer-boundaries`, `design-domain-boundaries` | `rules/20-change-scope.md`, `skills/passive/detect-architecture-drift` | rule + passive | covered | ownership or FSD layer is uncertain |
| `identify-state-owner`, `identify-state-ownership`, `classify-state`, `separate-server-and-client-state`, `design-state-architecture` | `knowledge/data-loading-and-failure-model.md`, `knowledge/rose-derived-patterns.md` | knowledge | covered | state ownership is uncertain |
| `design-error-model`, `design-failure-isolation`, `review-partial-failure`, `implement-fallback-behavior` | `rules/50-data-and-failure-contracts.md`, `knowledge/data-loading-and-failure-model.md` | rule + knowledge | covered | primary/partial/secondary outcome exists |
| `review-user-generated-content`, `identify-trust-boundaries` | `knowledge/content-trust-boundaries.md` | knowledge | covered | external content reaches a rendering or behavior sink |
| `design-data-flow`, `design-cache-strategy`, `design-concurrency-model` | `knowledge/data-loading-and-failure-model.md`, `knowledge/async-ui-state-and-cancellation.md` | knowledge | covered | data, freshness, or race behavior needs a model |
| `review-data-shape`, `normalize-api-data`, `design-view-model`, `separate-domain-and-transport-model` | `knowledge/data-loading-and-failure-model.md`, `knowledge/rose-derived-patterns.md` | knowledge | covered | transport and UI ownership need an explicit boundary |
| `review-form-accessibility`, `test-error-paths`, `test-concurrency` | `skills/active/review-form-contract` | active | covered | form or submit pipeline is in scope |
| `design-component-api`, `design-extension-points`, `review-component-boundaries`, `review-hook-design`, `review-variant-model`, `design-slot-api`, `separate-ui-and-domain-logic` | `rules/40-frontend-contracts.md`, `skills/active/review-component-anatomy`, `knowledge/rose-derived-patterns.md` | rule + active + knowledge | covered | component or UI/domain contract is in scope |
| `extract-domain-logic`, `remove-duplication`, `reduce-complexity`, `improve-module-cohesion`, `incremental-refactor` | `rules/20-change-scope.md`, `skills/active/implement-minimal-change` | rule + active | covered | duplication or complexity is demonstrated |
| `split-commit`, `prepare-clean-commit`, `review-commit-history` | `rules/30-git-and-review.md` | rule | covered | commit or review boundary is in scope |
| `review-design-token-usage`, `design-token-architecture` | `rules/40-frontend-contracts.md`, `skills/active/review-component-anatomy` | rule + active | covered | repeated visual meaning is demonstrated |
| `define-verification-plan`, `design-minimal-change` | `skills/active/understand-and-plan-change`, `skills/active/verify-change` | active | covered | a change needs a bounded plan or risk-appropriate check |

Candidates such as `understand-codebase` and the broader platform, security,
and production families remain planned. They have useful names in the backlog,
but the current evidence does not yet justify claiming a complete independent
workflow for them.

## P0 runtime compatibility

Goal: make the same GHOST capability graph usable across the six selected
coding-agent runtimes without maintaining six copies of the rules.

| Runtime | Core entry point | Adapter status | Next validation |
|---|---|---|---|
| Codex | `AGENTS.md` + `.agents/skills/` | implemented | run the representative workflow |
| Claude Code | `CLAUDE.md` + host skills directory | loader implemented; skills projection to validate | run the representative workflow |
| Cursor | `.cursor/rules/` + `.cursor/skills/` | planned thin projection | verify current discovery and invocation controls |
| GitHub Copilot | custom instructions + `.agents/skills/` | planned direct path | verify cloud agent, CLI, and review surfaces |
| Gemini CLI | `GEMINI.md` + `.agents/skills/` | planned direct path | verify workspace discovery and `/skills` behavior |
| OpenCode | `AGENTS.md` + `.agents/skills/` | planned direct path | verify passive-detector handling |

The runtime matrix and token-budget policy live in
`.agents/knowledge/runtime-adapters-and-context-budget.md`. P1 and P2 hosts
are intentionally not part of this slice.

## Phase 1 — cognitive core and repository understanding (P0)

Goal: make the agent able to build a reliable context model before changing
code.

### Capability families

1. **Codebase understanding** — `map-codebase`,
   `identify-module-boundaries`, `trace-data-flow`, `trace-control-flow`,
   `trace-request-lifecycle`, `trace-event-lifecycle`, `trace-state-lifecycle`,
   `find-feature-ownership`, `find-domain-ownership`, `analyze-dependency-graph`,
   `find-coupling-hotspots`, `detect-circular-dependencies`,
   `identify-entry-points`, `identify-runtime-boundaries`,
   `identify-client-server-boundaries`, `identify-state-ownership`,
   `explain-module-responsibility`, `summarize-subsystem`,
   `build-system-mental-model`.
2. **Problem framing** — `clarify-engineering-task`, `extract-requirements`,
   `separate-symptom-from-problem`, `identify-invariants`,
   `identify-assumptions`, `identify-unknowns`, `define-success-criteria`,
   `define-non-goals`, `estimate-blast-radius`, `assess-change-risk`,
   `find-hidden-constraints`, `challenge-task-premise`, `reframe-problem`,
   `identify-source-of-truth`.
3. **Planning and self-critique** — `plan-code-change`, `split-large-change`,
   `sequence-dependent-changes`, `define-verification-plan`,
   `design-minimal-change`, `challenge-own-assumptions`,
   `compare-plan-with-implementation`, `check-task-completeness`,
   `identify-confidence-level`.
4. **Repository hygiene** — `inspect-project-guidelines`,
   `preserve-public-contracts`, `avoid-unrelated-changes`, `keep-diff-focused`,
   `check-generated-files`, `check-lockfile-impact`, `check-ci-impact`.

### Deliverables

- Add `understand-codebase` as an active parent skill with a repeatable output:
  module map, ownership map, runtime boundaries, data/control flows, unknowns,
  and evidence links.
- Add `clarify-engineering-task` as a framing skill or integrate it into the
  existing `understand-and-plan-change` skill if the procedures do not have
  independent triggers.
- Extend `verify-change` with a plan-versus-implementation self-critique.
- Add a repository-context checkpoint template.

### Done when

For an unfamiliar repository, the agent can explain where a change belongs,
which boundary it crosses, what it must not touch, and how success will be
verified before editing.

## Phase 2 — safe change execution (P0/P1)

Goal: improve the reliability of implementation, debugging, refactoring, and
review workflows.

### Capability families

- **Debugging:** reproduce/isolate failure, rank hypotheses, find root cause,
  debug async behavior, race conditions, state sync, hydration, network,
  caching, memory, performance, build, type, and test failures.
- **Implementation:** preserve contracts, follow local conventions, extend an
  existing abstraction, handle edge cases, idempotency, retries, cancellation,
  timeouts, error boundaries, and fallbacks.
- **Refactoring:** extract modules/domain logic, reduce coupling and
  complexity, replace boolean flags, simplify state/control flow, remove dead
  code, improve cohesion, and refactor incrementally.
- **Architecture and API:** design module/layer/domain boundaries, public and
  internal APIs, extension points, state architecture, error models, cache
  strategy, and backward-compatible changes.
- **Testing and review:** choose test level, write regression/contract tests,
  test error and concurrency paths, reduce brittleness, review mocks, review
  diffs rather than only files, and assess regression risk.
- **Git/change management:** analyze diffs, split commits, prepare clean
  commits, resolve conflicts, bisect regressions, backport, and review release
  diffs.

### Deliverables

- Promote the current `debug-systematically` and `analyze-change-impact` into
  parent skills with procedure checklists.
- Add `review-code-change` and `design-test-strategy` as active parent skills.
- Add passive detectors for test-signal weakness, overmocking, leaky
  abstraction, complexity creep, and lockfile/CI impact.
- Add explicit migration and rollback sections to API and configuration
  workflows.

### Done when

The agent can move from observed failure or requested change to a bounded plan,
small implementation, regression check, and honest completion report.

## Phase 3 — frontend platform depth (P1)

Goal: prevent React/Next.js fluency from masking gaps in JavaScript, browser,
network, and rendering fundamentals.

### Capability families

- **TypeScript:** domain types, discriminated unions, exhaustiveness, runtime
  validation boundaries, inference, branded types, and library types.
- **JavaScript:** event loop, microtasks, closures, prototypes, module loading,
  garbage collection, identity, mutation, and async control flow.
- **Browser:** layout, paint, compositing, DOM cost, event propagation,
  storage, navigation, scheduling, observers, forms, focus, scroll, and worker
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

### Deliverables

- Add knowledge/mental-model documents before adding many active procedures.
- Create parent active skills for browser rendering, React rendering, and the
  Next.js rendering model.
- Keep framework-specific procedures dependent on platform-level mental models.
- Add passive detectors for effect misuse, duplicated state, unsafe type
  assertions, hydration risk, and client-boundary expansion.

### Done when

The agent can explain the underlying JavaScript/browser mechanism before
proposing a React or Next.js fix, and can identify when a framework abstraction
is hiding a platform problem.

## Phase 4 — quality and user-facing correctness (P1)

Goal: make performance, network behavior, security, CSS, accessibility, and
design-system quality part of the implementation contract.

### Capability families

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
- **Design systems:** component contracts, tokens, variants, composition,
  slots, consistency, duplication, deprecation, and migration.

### Deliverables

- Add active parent skills `profile-before-optimizing`, `review-frontend-security`,
  `audit-accessibility`, and `review-design-system-component`.
- Connect existing passive detectors to these parents only at a severity
  threshold.
- Add risk-specific verification templates for browser, accessibility,
  performance, and security claims.

### Done when

The agent can identify the relevant user-facing quality dimension, explain its
mechanism, choose a proportionate check, and avoid declaring a contextual rule
as a universal platform guarantee.

## Phase 5 — production and system evolution (P2)

Goal: extend GHOST from local code changes to long-lived system behavior.

### Capability families

- **Dependency management:** evaluate libraries, risk and lock-in, upgrades,
  removal, transitive dependencies, duplicate dependencies, footprint, and
  build-vs-buy.
- **Build tooling:** bundler output, module resolution, tree shaking, chunking,
  build time, transpilation, source maps, environment variables, and monorepo
  graphs.
- **Observability:** error logging, client metrics, structured events,
  tracing context, telemetry analysis, production triage, client/server
  correlation, debuggable features, and signal-to-noise.
- **Reliability:** fallback/recovery paths, failure-mode analysis, idempotency,
  timeout/retry behavior, partial failure, and offline behavior.
- **Data modeling:** view models, transport/domain separation, cache keys,
  identity, nullability, transitions, and data duplication.
- **Migration and technical debt:** framework/component/state/routing/design
  system migrations, strangler migration, debt classification, hotspots,
  paydown, maintenance cost, and complexity creep.

### Deliverables

- Add runbook and migration templates before adding specialized skills.
- Require rollback, observability, and operational ownership in production
  change plans.
- Add passive detectors for dependency lock-in, build graph expansion, missing
  fallback paths, and unowned telemetry.

### Done when

Material changes include operational consequences, recovery behavior, ownership,
and migration state—not only local code correctness.

## Phase 6 — Principal-level judgment and learning loop (P1/P2)

Goal: encode the reasoning that distinguishes senior implementation from
principal-level system judgment.

### Capability families

- **Systemic decisions:** challenge requirements, evaluate systemic and
  organizational impact, long-term cost, cognitive load, operational
  complexity, reversibility, optionality, standardization, local/global
  optima, pattern proliferation, and scaling limits.
- **Self-critique:** challenge assumptions, find counterexamples and missed
  edge cases, verify claims and library APIs, distinguish known from assumed,
  check completeness, perform pre-submit review, and identify confidence.
- **Documentation:** architecture notes, ADRs, public API docs, complex
  behavior, decisions, migrations, debugging guides, runbooks, maintainer
  notes, and invariants.
- **Learning:** research unknown APIs, read library/framework source, compare
  docs with runtime, create minimal reproductions, derive behavior
  experimentally, validate mental models, study patterns, and extract lessons.

### Deliverables

- Add `evaluate-systemic-impact` and `critique-own-solution` as active parent
  skills with explicit evidence and counterexample steps.
- Add `write-architecture-note` and `research-unknown-api` as knowledge-facing
  workflows.
- Make every active skill emit confidence, unresolved assumptions, and what
  evidence would change the decision.

### Done when

The agent can explain not only whether a solution works, but what precedent it
creates, what complexity it adds, who will maintain it, how reversible it is,
and what would falsify the recommendation.

## Promotion policy for the 444 candidates

A candidate becomes a standalone `SKILL.md` only if at least two of these are
true:

1. it has a distinct trigger and completion condition;
2. it recurs across repositories or tasks;
3. it requires a different mental model or verification method;
4. it is useful as a separately routable capability;
5. a passive detector can escalate to it with a clear threshold.

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
coverage: standalone | parent | rule | knowledge | detector
artifact: <relative path or list of paths>
```

## Next implementation slice

The next coherent slice is intentionally small:

1. implement `understand-codebase`;
2. implement `clarify-engineering-task`;
3. add a repository-context checkpoint template;
4. extend `verify-change` with plan-versus-implementation comparison;
5. run the workflow on one real repository and record friction before adding
   the next family.

The slice is complete only after a real-repository trial, not after writing
the files.

## Source boundary

The canonical backlog is this repository's
[`ROADMAP-BACKLOG.md`](./ROADMAP-BACKLOG.md). Its initial inventory comes from
the user-provided attachment:

`/Users/nikkeyl/.codex/attachments/67062245-ee1b-4681-9702-506aca0cd323/pasted-text.txt`

Its labels and candidate names are treated as design input. They do not
override `AGENTS.md`, repository conventions, user scope, safety constraints,
or evidence-based verification.
