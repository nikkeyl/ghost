---
name: review-for-performance
description: Review a scoped change for performance risks by tracing work,
  resource cost, affected user paths, and available measurements.
kind: active
---

# Review for performance

## Trigger

Use for a requested performance review or a material performance risk
introduced by a change. Broad optimization without a scoped question
requires a separate profiling plan.

## Goal

Identify credible performance consequences and distinguish measured
regressions from hypotheses that still require profiling.

## Investigation / reasoning

1. Identify the changed user path, relevant metric or resource budget,
   execution environment, and before/after state. Use the product's
   device and network context rather than universal thresholds.

1. Trace changed work on the critical path: network, JavaScript,
   rendering, layout, assets, state/effects, cache behavior, and memory
   lifetime. Consider input frequency and data volume where relevant.

1. Inspect moved imports, client boundaries, route-specific resources,
   repeated work, unbounded lists, and synchronous blocking. For images
   and motion, use relevant guidance from
   `.agents/knowledge/source-derived-patterns.md`.

1. Compare available traces, request data, timings, bundle output, or
   memory observations under matching conditions. If measurements are
   absent, specify the smallest experiment that can falsify the risk.

## Decision rules

- Code shape and bundle size alone do not establish a user-visible
  regression. Connect the mechanism, frequency, and affected path.

- Do not optimize by adding caches or memoization without identifying
  cost, invalidation, and memory trade-offs.

- A review may end with a hypothesis and measurement plan. Do not claim
  faster behavior from inspection alone or make unsolicited fixes.

## Actions

Report each finding as changed work, triggering scale or interaction,
affected outcome, evidence, confidence limits, and a proportionate next
step. Separate measured regressions from unmeasured risks and explicitly
retain changes whose costs are acceptable for the product.

## Verification

Check that comparisons use equivalent inputs, environments, and states.
For an authorized optimization, repeat the measurement and correctness
checks; account for noise and shifted costs. When measurement cannot
run, record the missing evidence instead of a performance verdict.

## Completion criteria

Findings explain a credible cost mechanism and its user impact, measured
claims are reproducible within stated limits, and remaining hypotheses
have a bounded validation plan. Review completion is not optimization
completion.

## Graph

```yaml
may-trigger: [design-test-strategy, research-unknown-api]
references: [verify-before-claiming, source-derived-patterns]
```
