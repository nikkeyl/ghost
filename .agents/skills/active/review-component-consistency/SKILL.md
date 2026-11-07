---
description: Compare related components against an established design-system
  contract across API, variants, semantics, styling, and interaction.
kind: active
name: review-component-consistency
---

# Review component consistency

## Trigger

Use when reviewing consistency across a component family or a change to
an established design-system component. Do not impose a design system
on unrelated components merely because they share markup.

## Goal

Identify deviations that make equivalent components harder to use or
maintain while preserving differences justified by their user tasks.

## Investigation / reasoning

1. Identify the reference contract, tokens, documented patterns, and
   representative sibling components. Establish which similarities
   consumers should actually be able to rely on.

1. Compare prop names, defaults, event payloads, controlled state,
   variants, slots, styling extension points, and exports.

1. Compare semantic roles, keyboard and focus behavior, disabled/loading
   states, errors, responsive behavior, and token usage where relevant.

1. Trace caller expectations and distinguish accidental drift from a
   deliberate product exception or required native behavior.

## Decision rules

- Existing inconsistency is evidence to investigate, not a reason to
  copy a defect into another component.

- Equivalent responsibilities should have predictable contracts; visual
  similarity alone does not justify shared behavior or implementation.

- Avoid forced uniformity that adds flags or weakens accessibility.
  Document legitimate exceptions. Review does not imply a rewrite.

## Actions

Produce a compact reference-versus-component matrix, justified
exceptions, and findings with affected consumers and consequences.
Propose standardization or a contract change only where the benefit is
concrete; route redesign to `design-component-contract` when required.

## Verification

Validate each discrepancy against the reference and actual callers.
For applied corrections, exercise representative sibling scenarios and
public compatibility. State whether visual, keyboard, and type-level
comparisons were performed or remain open.

## Completion criteria

Relevant components have been compared on agreed dimensions, material
drift is evidenced, and retained differences have a reason. Consistency
is not reduced to React hook order, filenames, or identical markup.

## Graph

```yaml
may-trigger: [design-component-contract, estimate-blast-radius]
references: [review-component-boundaries, verify-before-claiming]
```
