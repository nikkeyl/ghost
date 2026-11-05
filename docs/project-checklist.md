# GHOST completion checklist

Updated: 2026-11-05. Only unfinished actions are listed. P0 gates reliability claims;
P1 adds depth from concrete use; P2 follows demonstrated need. The 479 backlog
candidates are a registry, not a target number of files to create.

## P0 — make current claims reviewable

- [ ] **C01 — Confirm separate linter workflows.** EditorConfig, Prettier and remark
      should each report their own result for pushes and pull requests, including
      configuration changes. Do not add an aggregate lint or validate workflow.
- [ ] **C02 — Verify a tagged archive release when a release is requested.** Confirm
      the GitHub Release contains `.agents/`, root `AGENTS.md` and `CLAUDE.md`,
      plus LICENSE, with no roadmaps, audit reports or repository tooling. No custom archive builder or Python dependency is needed.
- [ ] **C03 — Run a representative single-host behavioral trial.** Pin repository
      state, runtime version, task input and permitted effects. Exercise
      understanding, diff review, form/component review, bounded change and
      verification, a behavior-preserving refactor and a compatibility plan. Include
      diagnosis without fixing, review without posting, migration planning without
      execution, and a trivial documentation edit that should avoid broad activation.
      Acceptance: record expected vs actual behavior with
      `.agents/templates/skill-evaluation.md`, failures and selected routes; no
      invented or retrospective expected outcomes.
- [ ] **C04 — Validate remaining target runtimes incrementally.** Start after C03;
      use the same representative contracts on Claude Code, Cursor, Copilot, Gemini
      CLI and OpenCode as applicable, including Codex if it was not the first host.
      Check nested skill discovery and passive/active separation. Acceptance: a dated
      matrix distinguishes observed support, unsupported behavior and unavailable
      tests; thin adapters have one source of truth and a refresh/removal procedure.
- [ ] **C05 — Measure activation cost and routing quality.** Record active skills,
      graph hops, loaded text and routing failures for C03/C04. Acceptance: normal
      cases respect the five-skill/two-hop default or explain an observed exception;
      no savings percentage without a comparable baseline and stated measurement
      method.

## P1 — deepen the frontend core and preserve personal context correctly

- [ ] **C06 — Separate optional preferences from invariant contracts.** Review
      no-`switch`, constant naming, component structure and unconditional form reset.
      Acceptance: each retained global rule has a reason and exception boundary;
      search/autosave/multi-step forms and adopting team conventions remain valid.
- [ ] **C07 — Trial an optional mentoring profile.** Build from
      `knowledge-and-approaches.md`, enabled only for personal learning. Acceptance:
      concise answer when urgency requires it; otherwise prediction before AI
      feedback, mechanism, counterexample and transfer check. RU/EN/JA conversational
      preferences do not leak into other users' code, commits or shared
      documentation. Use knowledge under an existing learning parent until
      independent routing is justified.
- [ ] **C08 — Author and trial JS/runtime mental models.** Start with
      values/references/identity/mutation/scope; follow with
      closures/`this`/prototypes, tasks/microtasks/Promises, module loading and
      memory reachability. Acceptance: each topic has an unfamiliar prediction,
      runnable observation, common failure and link to a working frontend decision.
      Use the existing 5-hour weekly study budget.
- [ ] **C09 — Author and trial browser/network/rendering models.** Cover DOM/events,
      document/resource loading, HTTP/cache/CORS/cookies and
      layout/paint/compositing. Acceptance: one DevTools Network trace and one
      Performance trace explain a real issue, alternative and falsifying observation.
      Only then promote a distinct profiling workflow if repeated tasks justify it.
- [ ] **C10 — Connect TypeScript, React and Next.js to those models.** Cover static
      vs runtime validation, identity/closures, render vs commit vs paint,
      server/client ownership, hydration and cache freshness. Acceptance:
      version-bound reproduction and consumer-visible check; framework familiarity
      alone does not mark learning complete. Prefer existing component/form/async
      parents over extra leaf skills.
- [ ] **C11 — Add published-package consumer verification to the existing test and
      impact workflows.** Use historical npm findings as hypotheses to recheck, not
      current defects. Acceptance: consumer fixture exercises actual packed exports,
      ESM/CJS where claimed, Next.js client/SSR boundary where relevant, peer
      compatibility, documented positive/negative inputs and library types. No
      package changes implied.
- [ ] **C12 — Trial quality-specific verification.** Select real accessibility,
      performance and frontend trust-boundary cases. Acceptance: keyboard/focus
      journey, reproducible before/after profile, and source-to-render/auth boundary
      analysis as applicable. Native semantics, linters and generic advice alone do
      not prove a full audit capability. Expand parent workflows only from observed
      recurring gaps.
- [ ] **C13 — Practice systemic judgment now.** Extend planning/review questions with
      the option to do nothing, users affected, team cost, precedent, adoption,
      owner, reversibility and what would change the recommendation. Acceptance: two
      concrete decisions with alternatives and evidence, including a case where
      standardization or abstraction is rejected. A separate
      `evaluate-systemic-impact` skill still requires the promotion policy; do not
      postpone this reasoning until Phase 6.
- [ ] **C14 — Establish an evidence ledger and refresh policy.** Link runtime trials
      and learning demonstrations to exact states, versions, dates and limitations.
      Acceptance: `covered`, `implemented`, structural pass and behavioral
      verification cannot be confused; stale evidence is retained with a clear
      recheck trigger. Confirm or revise the personal profile from demonstrations
      rather than titles.

## P2 — expand only from operating needs

- [ ] **C15 — Add production-evolution checklists when a real change needs them.**
      Cover frontend telemetry, failure isolation, dependency rollout and recovery
      using existing migration/handover parents. Acceptance: a scoped case records
      owner, user-visible degradation, compatibility window, rollback and deployed
      acceptance. Extending GHOST here does not require changing the author's
      frontend career goal.
- [ ] **C16 — Reassess standalone promotions.** After C03–C14, promote only
      candidates with distinct triggers, repeated need and a useful verification
      contract. Acceptance: explain why an existing parent/checklist is insufficient,
      update graph/index/coverage together, and retain a positive case plus
      non-trigger.

## Suggested sequence

Project reliability: C01 → C02 → C03 → C04, with C05/C14 capturing the evidence.
Personal depth can proceed alongside that work: C07 → C08 → C09 → C10, applying C13
to current decisions. C06, C11 and C12 fit real review tasks. C15/C16 wait for
demonstrated need. Do not turn project maintenance into extra study hours on top of
the existing schedule.
