---
description: Review React component responsibilities, state ownership, public
  props, composition, dependencies, and client/server boundaries.
kind: active
name: review-component-boundaries
---

# Review component boundaries

## Trigger

Use when a React component mixes responsibilities, its ownership or
public surface is unclear, or a split, merge, extraction, or dependency
move could affect consumers. A formatting-only edit is not a trigger.

## Goal

Determine whether responsibilities and dependencies belong together and
identify the smallest boundary correction supported by actual use.

## Investigation / reasoning

1. Read the component, callers, children, hooks, and data dependencies.
   Map rendering, interaction, domain decisions, data access, and state
   ownership. Identify public props and exports relied on by consumers.

1. Trace which state changes together, which values are derived, and
   which consumers need each value. Look for duplicated sources of
   truth, unnecessary lifting, and effects that conceal data flow.

1. Compare reasons to change and reuse patterns. Identify flags for
   unrelated scenarios, children coupled through hidden assumptions,
   or a split that would add more cross-boundary coordination.

1. Inspect imports and runtime placement. Determine what requires a
   browser, what can stay on the server in supported frameworks, and
   whether route-specific data or dependencies became global.

## Decision rules

- Component size, hook order, file count, and a preferred props-file
  layout do not establish a bad boundary. Use responsibility, ownership,
  change coupling, and consumer contracts as evidence.

- Extract when independent responsibility or useful isolation outweighs
  coordination cost. Keep cohesive one-use logic near its owner while
  following the file-boundary convention in
  `.agents/rules/code-style.md`. Put standalone helpers in separate
  colocated files; retain short callbacks and owner-bound closures
  locally. Local ownership does not require sharing one file.

- Prefer composition for independently owned content; avoid exposing
  internal implementation details just to make an extraction possible.

- Follow existing runtime conventions. A review does not authorize a
  rewrite or impose a particular framework or component style.

## Actions

Report the current responsibility and dependency map, each material
boundary issue, affected consumers, and keep/split/merge/move options
with trade-offs. Use `design-component-contract` for a changed public
contract and `refactor-without-behavior-change` for an authorized move.
Read `.agents/knowledge/engineering-patterns.md` only for relevant local
structure conventions.

## Verification

Check each finding against callers, state transitions, and imports.
For an applied correction, compare behavior before and after, including
public props, effects, render placement, and relevant interaction paths.
A review without edits ends with findings and evidence limits.

## Completion criteria

The review explains ownership and coupling, identifies defensible
boundary issues or reasons to retain the structure, and accounts for
consumer compatibility. It does not equate style conformity with sound
component design.

## Graph

```yaml
may-trigger: [design-component-contract, estimate-blast-radius]
references: [refactor-without-behavior-change, verify-before-claiming]
```
