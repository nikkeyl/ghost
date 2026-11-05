---
name: review-for-accessibility
description: Review a scoped change for accessibility defects using semantics,
  keyboard, focus, assistive output, and applicable visual behavior.
kind: active
---

# Review for accessibility

## Trigger

Use for a requested accessibility review or a material accessibility
risk in changed UI. A full product conformance audit is a separate scope.

## Goal

Produce evidenced accessibility findings for affected user paths and
state what the review did and did not exercise.

## Investigation / reasoning

1. Identify changed interactions, content, states, supported platforms,
   and the repository's accessibility requirements. Trace affected user
   tasks rather than checking isolated markup alone.

1. Inspect semantic structure, accessible names, roles, states, labels,
   relationships, errors, status messages, and media alternatives.

1. Exercise keyboard reachability and operation, visible focus, focus
   entry/return, reading order, and escape behavior where applicable.
   Inspect zoom/reflow, contrast, target visibility, and motion against
   the applicable requirements and actual interface.

1. Use automated checks for covered rules and inspect the accessibility
   tree or assistive output for material interactions. Read relevant
   patterns from `.agents/knowledge/source-derived-patterns.md` only
   when the component requires them.

## Decision rules

- An automated pass does not prove accessible behavior or conformance.
  Report untested assistive technologies and platforms explicitly.

- Prefer native semantics. Do not prescribe an ARIA pattern from visual
  resemblance without checking the actual interaction contract.

- Separate an observed barrier from a plausible risk and an optional
  enhancement. A scoped review does not authorize implementation.

## Actions

Report location, affected user/task, triggering state, observed barrier,
evidence, severity, and a proportionate correction. Include changed
paths checked without findings and unresolved evidence gaps. Route a
contract redesign to `design-component-contract` only when needed.

## Verification

Reproduce each reported barrier through the relevant keyboard, focus,
semantic, visual, or assistive path. For an authorized fix, repeat that
path and inspect adjacent states. Record checks not performed instead
of turning a static inspection into a claim of user acceptance.

## Completion criteria

The requested paths were reviewed, findings have concrete consequences
and evidence, and coverage limits are explicit. No broad audit or
conformance claim exceeds the review actually performed.

## Graph

```yaml
may-trigger: [design-component-contract, design-test-strategy]
references: [source-derived-patterns, verify-before-claiming]
```
