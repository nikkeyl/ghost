# GHOST capability backlog

This file preserves the complete candidate inventory from the user-provided
attachment. It is a roadmap backlog, not a prompt to activate every capability
at once and not an instruction that overrides AGENTS.md.

Each candidate starts as proposed. Promote it according to the policy in
ROADMAP.md: first group related candidates into a parent
domain skill or checklist, then create a standalone skill only when it has an
independent trigger, mental model, verification method, and repeated value.

During a task, the router selects the smallest relevant parent skill from this
registry. Candidates are not activated individually just because their names
match the request, and inactive candidates remain available for later
promotion.

## Imported candidate inventory

Codebase understanding- map-codebase
- identify-module-boundaries
- trace-data-flow
- trace-control-flow
- trace-request-lifecycle
- trace-event-lifecycle
- trace-state-lifecycle
- find-feature-ownership
- find-domain-ownership
- analyze-dependency-graph
- find-coupling-hotspots
- detect-circular-dependencies
- identify-entry-points
- identify-runtime-boundaries
- identify-client-server-boundaries
- identify-state-ownership
- explain-module-responsibility
- summarize-subsystem
- build-system-mental-model

Problem framing- clarify-engineering-task
- extract-requirements
- separate-symptom-from-problem
- identify-invariants
- identify-assumptions
- identify-unknowns
- define-success-criteria
- define-non-goals
- estimate-blast-radius
- assess-change-risk
- find-hidden-constraints
- challenge-task-premise
- reframe-problem
- identify-source-of-truth

Planning- plan-code-change
- plan-refactor
- plan-migration
- plan-feature-implementation
- plan-bugfix
- plan-api-change
- plan-state-migration
- plan-dependency-upgrade
- plan-performance-work
- plan-progressive-rollout
- split-large-change
- sequence-dependent-changes
- define-verification-plan
- design-minimal-change

Debugging- debug-systematically
- reproduce-bug
- isolate-failure
- form-debugging-hypotheses
- rank-debugging-hypotheses
- find-root-cause
- trace-runtime-error
- debug-async-behavior
- debug-race-condition
- debug-state-sync
- debug-render-loop
- debug-hydration
- debug-network-failure
- debug-cache-invalidation
- debug-memory-leak
- debug-performance-regression
- debug-build-failure
- debug-type-error
- debug-test-failure
- debug-production-only-issue

Implementation- implement-minimal-change
- implement-feature-safely
- preserve-existing-contracts
- follow-local-conventions
- extend-existing-abstraction
- avoid-unnecessary-abstraction
- write-defensive-code
- handle-edge-cases
- implement-idempotent-operation
- implement-retry-safe-operation
- implement-cancellation
- implement-timeout-handling
- implement-error-boundaries
- implement-fallback-behavior

Refactoring- refactor-without-behavior-change
- extract-module
- extract-domain-logic
- reduce-coupling
- reduce-complexity
- remove-duplication
- simplify-control-flow
- simplify-state-model
- replace-boolean-flags
- replace-conditionals-with-model
- collapse-unnecessary-abstraction
- remove-dead-code
- normalize-api-surface
- improve-module-cohesion
- refactor-large-component
- refactor-legacy-code
- incremental-refactor

Architecture- review-architecture
- design-module-boundaries
- design-layer-boundaries
- design-domain-boundaries
- design-public-api
- design-internal-api
- design-plugin-architecture
- design-extension-points
- design-state-architecture
- design-data-flow
- design-error-model
- design-cache-strategy
- design-concurrency-model
- design-progressive-enhancement
- design-failure-isolation
- design-for-change
- evaluate-architectural-fit
- detect-architecture-drift
- detect-leaky-abstraction
- assess-architectural-debt

API design- review-api-design
- design-function-api
- design-component-api
- design-hook-api
- design-library-api
- design-rest-api-consumer
- design-graphql-consumer
- design-event-contract
- design-versioned-contract
- design-backward-compatible-change
- detect-breaking-change
- minimize-api-surface
- improve-api-consistency
- design-error-contract

TypeScript- model-domain-types
- improve-type-safety
- remove-unsafe-any
- replace-type-assertions
- design-discriminated-union
- design-generic-api
- reduce-generic-complexity
- infer-types-from-source
- enforce-exhaustiveness
- model-impossible-states
- separate-runtime-and-static-validation
- design-branded-types
- review-type-boundaries
- debug-type-inference
- improve-library-types

JavaScript fundamentals- analyze-event-loop
- analyze-microtask-ordering
- analyze-closure-behavior
- analyze-prototype-behavior
- analyze-module-loading
- analyze-garbage-collection
- analyze-object-identity
- analyze-coercion
- analyze-async-control-flow
- analyze-memory-retention
- reason-about-mutation
- reason-about-referential-equality

Browser platform- analyze-browser-rendering-pipeline
- analyze-layout
- analyze-paint
- analyze-compositing
- analyze-event-propagation
- analyze-dom-cost
- analyze-web-storage
- analyze-history-navigation
- analyze-focus-management
- analyze-form-behavior
- analyze-scroll-behavior
- analyze-browser-scheduling
- analyze-intersection-observer
- analyze-resize-observer
- analyze-worker-architecture

React- analyze-react-rendering
- trace-react-rerenders
- find-state-colocation-opportunities
- review-component-boundaries
- review-hook-design
- detect-effect-misuse
- reduce-effect-usage
- detect-derived-state
- stabilize-component-api
- analyze-react-concurrency
- analyze-suspense-boundaries
- analyze-context-cost
- optimize-react-rendering
- refactor-large-react-component
- separate-ui-and-domain-logic
- review-react-key-usage

Next.js- analyze-next-rendering-model
- choose-server-vs-client-component
- review-server-component-boundaries
- review-route-architecture
- analyze-next-caching
- debug-next-caching
- analyze-revalidation
- analyze-server-actions
- review-data-fetching-strategy
- review-streaming-strategy
- review-route-handler
- debug-hydration-next
- optimize-next-bundle
- review-metadata-strategy
- analyze-edge-runtime-fit

State management- identify-state-owner
- classify-state
- reduce-global-state
- separate-server-and-client-state
- normalize-state-shape
- design-state-machine
- review-state-transitions
- detect-duplicated-state
- detect-stale-state
- design-optimistic-update
- design-event-driven-state
- review-cache-as-state

Performance- profile-before-optimizing
- find-performance-bottleneck
- analyze-main-thread-work
- analyze-long-tasks
- analyze-bundle-size
- analyze-code-splitting
- analyze-network-waterfalls
- optimize-critical-render-path
- optimize-lcp
- optimize-inp
- optimize-cls
- reduce-javascript-cost
- reduce-render-cost
- reduce-layout-thrashing
- optimize-image-loading
- optimize-font-loading
- optimize-data-fetching
- optimize-caching
- analyze-memory-usage
- verify-performance-regression

Networking- analyze-http-request
- analyze-cache-headers
- analyze-cors
- analyze-cookies
- analyze-auth-request-flow
- analyze-request-waterfall
- design-retry-policy
- design-timeout-policy
- design-request-deduplication
- analyze-http2-behavior
- analyze-http3-behavior
- analyze-cdn-behavior
- analyze-browser-cache
- analyze-service-worker-cache

Security- review-frontend-security
- review-xss-risk
- review-csrf-risk
- review-cors-policy
- review-content-security-policy
- review-token-storage
- review-cookie-security
- review-auth-flow
- review-open-redirect-risk
- review-url-handling
- review-user-generated-content
- review-third-party-script-risk
- review-dependency-risk
- identify-trust-boundaries
- review-client-side-secrets

Testing- design-test-strategy
- choose-test-level
- write-unit-test
- write-integration-test
- write-e2e-test
- write-regression-test
- test-edge-cases
- test-error-paths
- test-concurrency
- test-accessibility
- reduce-test-brittleness
- improve-test-signal
- debug-flaky-test
- review-mocking-strategy
- detect-overmocking
- design-contract-test

Code review- review-code-change
- review-pull-request
- review-for-correctness
- review-for-maintainability
- review-for-performance
- review-for-security
- review-for-accessibility
- review-for-testability
- review-for-api-quality
- review-for-architecture-fit
- review-for-overengineering
- review-for-hidden-complexity
- review-for-regression-risk
- review-diff-not-files

Git / change management- analyze-git-diff
- split-commit
- prepare-clean-commit
- review-commit-history
- resolve-merge-conflict
- plan-safe-rebase
- identify-regression-commit
- bisect-regression
- prepare-backport
- review-release-diff

Dependency management- review-dependency-addition
- evaluate-library
- compare-library-options
- assess-dependency-risk
- assess-dependency-lock-in
- plan-dependency-removal
- plan-major-upgrade
- review-transitive-dependencies
- detect-duplicate-dependencies
- reduce-dependency-footprint
- evaluate-build-vs-buy

Build tooling- analyze-build-pipeline
- analyze-bundler-output
- debug-build-configuration
- debug-module-resolution
- analyze-tree-shaking
- analyze-chunking
- optimize-build-time
- review-transpilation-target
- review-source-maps
- review-environment-variables
- review-monorepo-build-graph

CSS / UI engineering- review-css-architecture
- debug-layout
- debug-stacking-context
- debug-overflow
- debug-container-query
- analyze-responsive-layout
- review-design-token-usage
- reduce-css-specificity
- review-css-performance
- review-animation-performance
- design-component-layout-contract
- detect-layout-fragility

Accessibility- audit-accessibility
- review-semantic-html
- review-keyboard-navigation
- review-focus-order
- review-screen-reader-flow
- review-aria-usage
- review-form-accessibility
- review-modal-accessibility
- review-live-region
- review-color-independent-state
- test-accessibility-flow

Design systems- review-design-system-component
- design-component-contract
- design-token-architecture
- review-variant-model
- review-composition-model
- design-slot-api
- review-component-consistency
- detect-component-duplication
- design-deprecation-path
- design-component-migration

Observability- design-frontend-observability
- review-error-logging
- review-client-metrics
- design-structured-events
- design-tracing-context
- analyze-production-telemetry
- triage-production-error
- correlate-client-server-failure
- design-debuggable-feature
- review-log-signal-to-noise

Reliability- design-graceful-degradation
- design-fallback-path
- design-recovery-path
- review-failure-modes
- perform-failure-mode-analysis
- design-idempotency
- review-timeout-behavior
- review-retry-behavior
- review-partial-failure
- design-offline-behavior

Data modeling- model-frontend-domain
- review-data-shape
- normalize-api-data
- design-view-model
- separate-domain-and-transport-model
- design-cache-key
- design-entity-identity
- review-nullability
- model-state-transition
- detect-data-duplication

Migration- plan-api-migration
- plan-component-migration
- plan-state-management-migration
- plan-framework-migration
- plan-routing-migration
- plan-design-system-migration
- plan-typescript-migration
- plan-css-migration
- design-strangler-migration
- design-backward-compatible-migration
- track-migration-progress

Technical debt- identify-technical-debt
- classify-technical-debt
- estimate-debt-impact
- prioritize-technical-debt
- find-debt-hotspots
- distinguish-debt-from-style-preference
- design-debt-paydown
- quantify-maintenance-cost
- detect-complexity-creep

Principal-level decision making
Вот здесь начинается наиболее ценный слой.- challenge-requirements
- evaluate-systemic-impact
- evaluate-long-term-cost
- evaluate-organizational-impact
- evaluate-team-cognitive-load
- evaluate-operational-complexity
- evaluate-reversibility
- evaluate-optionality
- evaluate-standardization-value
- evaluate-local-vs-global-optimum
- detect-accidental-complexity
- detect-essential-complexity
- assess-architecture-precedent
- assess-pattern-proliferation
- assess-maintenance-trajectory
- assess-scaling-limit
- identify-next-order-effects
- identify-second-order-effects
- make-build-vs-buy-decision
- make-standardize-vs-customize-decision
- choose-boring-technology
- minimize-system-complexity

Agent self-critique
Особенно важная категория для Codex.- critique-own-solution
- challenge-own-assumptions
- find-counterexample
- search-for-missed-edge-case
- verify-before-claiming
- distinguish-known-from-assumed
- detect-hallucinated-api
- verify-library-api
- verify-runtime-behavior
- compare-plan-with-implementation
- check-task-completeness
- perform-pre-submit-review
- find-unnecessary-changes
- find-missing-changes
- identify-confidence-level

Repository hygiene- follow-repository-conventions
- inspect-project-guidelines
- preserve-public-contracts
- avoid-unrelated-changes
- keep-diff-focused
- update-documentation
- update-tests-with-change
- update-types-with-change
- check-generated-files
- check-lockfile-impact
- check-ci-impact

Documentation- write-architecture-note
- write-adr
- document-public-api
- document-complex-behavior
- explain-code-decision
- write-migration-guide
- write-debugging-guide
- write-runbook
- write-maintainer-notes
- document-invariants

Learning / knowledge acquisition
Это полезно, если хочешь агента, который не просто пишет код, а исследует неизвестное.- research-unknown-api
- read-library-source
- read-framework-internals
- compare-docs-with-runtime
- create-minimal-reproduction
- derive-behavior-experimentally
- validate-mental-model
- study-existing-pattern
- extract-repository-conventions
- extract-engineering-lessons
