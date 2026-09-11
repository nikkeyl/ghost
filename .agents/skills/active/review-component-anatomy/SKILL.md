---
name: review-component-anatomy
kind: active
---

# Review React component anatomy

## Trigger

Use when creating or editing a React/TSX component and the repository has, or
is explicitly adopting, the GHOST component convention.

## Goal

Make the component's contract and local logic predictable without forcing a
style convention that the repository does not use.

## Investigation / reasoning

1. Check the repository's existing component layout, export style, styling
   utility, TypeScript flags, server/client boundaries, and generated types.
2. Decide whether the props contract should be separate and whether it can be
   assembled from native or schema-generated types.
3. Check for unrelated optional fields that should be separate component
   contracts or explicit variants.
4. Check whether variants are better represented by a typed lookup object and
   whether shared markup is truly identical in ownership and evolution.
5. Review accessibility, state, effects, and JSX readability.

## Decision rules

- `Props` in a separate file is a convention, not a requirement for tiny
  components.
- `cn` is required only when the repository uses it and override semantics are
  intentional.
- Slots/composition are preferable to consumer-specific boolean flags when the
  layout is genuinely shared.
- Keeping effects last may aid scanning, but dependency correctness and React
  lifecycle semantics win.
- Named exports are preferred only when consistent with the repository's public
  API and tooling.

## Actions

Review or restructure the component in this order when it helps readability:
props destructuring → hooks → computed values → handlers → effects → return.
Keep static variant configuration at module scope when it is independent of
props/state. Keep external `className` last when merge semantics require it.

## Verification

Run type checking, relevant tests, and a focused accessibility or browser check
for interactive components. Confirm that server/client boundaries and public
exports still work.

## Completion criteria

The component is locally predictable, its contract is narrow and accurate, and
the chosen conventions are justified by repository context rather than copied
blindly from a source article.

## Graph

```yaml
requires: [understand-and-plan-change]
may-trigger: [analyze-change-impact]
followed-by: [verify-change]
references: [source-derived-patterns]
```
