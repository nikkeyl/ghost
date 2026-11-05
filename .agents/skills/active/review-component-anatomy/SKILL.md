---
name: review-component-anatomy
description:
  Review React component boundaries, props, variants, effects, exports,
  and server/client placement against repository conventions.
kind: active
---

# Review React component anatomy

## Trigger

Use when creating or editing a React/TSX component and the repository
has, or is explicitly adopting, the GHOST component convention.

## Goal

Make the component's contract and local logic predictable without
forcing a style convention that the repository does not use.

## Investigation / reasoning

1. Check the repository's existing component layout, export style,
   styling utility, TypeScript flags, server/client boundaries, and
   generated types.

1. Decide whether the props contract should be separate and whether it
   can be assembled from native or schema-generated types.

1. Check for unrelated optional fields that should be separate component
   contracts or explicit variants.

1. Check whether variants are better represented by a typed lookup
   object and whether shared markup is truly identical in ownership and
   evolution.

1. Check whether finite value mappings, variants, or strategies are data
   that should be represented by a typed map instead of a conditional
   chain. Keep conditionals when they express control flow, predicates,
   sequencing, or dependencies between operations.

1. Inspect global CSS, existing component styles, native browser
   behavior, and the repository's class-composition utility before
   adding Tailwind classes.

1. Review accessibility, state, effects, and JSX readability.

## Decision rules

- `Props` in a separate file is a convention, not a requirement for tiny
  components.

- `cn` is required only when the repository uses it and override
  semantics are intentional.

- A low Tailwind class count is not evidence of missing styling.
  Preserve global, component-level, token-based, and native behavior
  when it already satisfies the visual contract.

- If values and types come from the same module, prefer one named import
  with an inline `type` modifier, following the repository's import
  ordering.

- Slots/composition are preferable to consumer-specific boolean flags
  when the layout is genuinely shared.

- Keep a reusable component's props focused on its stable core. Extend
  it from the outside instead of adding a prop for every
  consumer-specific case.

- Use semantic list elements when the rendered content is a list, even
  when the component provides interaction or custom visual styling.

- Treat animation as an enhancement rather than the component's core
  behavior. Verify the non-animated path and reduced-motion behavior.

- `aria-disabled` must be paired with behavior that actually prevents
  the disabled interaction; ARIA state alone does not disable a control.

- Keeping effects last may aid scanning, but dependency correctness and
  React lifecycle semantics win.

- Named exports are preferred only when consistent with the repository's
  public API and tooling.

## Actions

Review or restructure the component in this order when it helps
readability: props destructuring → hooks → computed values → handlers →
effects → return. Keep static variant configuration at module scope when
it is independent of props/state. Keep external `className` last when
merge semantics require it.

## Verification

Run type checking, relevant tests, and a focused accessibility or
browser check for interactive components. Confirm that server/client
boundaries and public exports still work.

## Completion criteria

The component is locally predictable, its contract is narrow and
accurate, and the chosen conventions are justified by repository context
rather than copied blindly from a source article.

## Graph

```yaml
requires: [understand-and-plan-change]
may-trigger: [analyze-change-impact]
followed-by: [verify-change]
references: [source-derived-patterns]
```
