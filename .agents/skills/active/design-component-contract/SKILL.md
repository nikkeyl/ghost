---
description: Define a component's consumer-facing inputs, events, state
  ownership, composition, semantics, and compatibility guarantees.
kind: active
name: design-component-contract
---

# Design component contract

## Trigger

Use when designing or changing a component's public contract, including
presentational components and interactive controls. Internal refactoring
with an unchanged contract belongs to `review-component-boundaries` or
`refactor-without-behavior-change`.

## Goal

Define the smallest complete contract that consumers can use without
knowing the component's implementation.

## Investigation / reasoning

1. Identify consumers, user tasks, supported scenarios, non-goals, and
   existing APIs. Distinguish product requirements from one caller's
   incidental markup or framework choice.

1. Define inputs, defaults, valid combinations, events and payloads,
   slots or children, refs when required, and styling extension points.
   State which behavior is guaranteed and which remains caller-owned.

1. Assign state ownership. For controlled and uncontrolled use, define
   initialization, updates, reset, and switching constraints. Avoid two
   independent owners for the same value.

1. Describe rendering semantics, responsive constraints, and relevant
   loading, empty, error, disabled, and interaction states. Specify
   keyboard, focus, and accessible naming for interactive components;
   do not invent interaction requirements for a static component.

1. Compare composition, variants, and separate components. Identify
   compatibility consequences for existing callers and runtime or data
   dependencies exposed through the proposed contract.

## Decision rules

- Prefer native semantics and existing repository primitives. Do not
  introduce custom controls merely to demonstrate an API.

- Keep props focused on supported scenarios. Use explicit variants or
  composition instead of unrelated booleans and hidden combinations.

- Keep internal fetching, caching, and framework details out of the
  public surface unless consumers need that responsibility explicitly.

- Define behavior before implementation. Contract design does not
  authorize a rewrite or require client-side rendering or server use.

## Actions

Produce a compact contract: purpose, props/defaults/constraints, events,
state ownership, composition and styling boundaries, semantics, failure
states, compatibility, and representative consumer examples. Cover a
static example and an interactive example only when both are required.
For custom control patterns, load the relevant guidance from
`.agents/knowledge/source-derived-patterns.md`.

## Verification

Check examples against real consumers and required scenarios. Ensure
invalid combinations are rejected or documented, event payloads and
ownership are unambiguous, and consumers need no private internals.
For implemented contracts, verify types and relevant behavior, including
controlled updates, reset, keyboard, and focus when applicable.

## Completion criteria

The contract is usable and testable by consumers, its supported states
and extension points are explicit, and compatibility is addressed.
Design completion is separate from implementation or runtime proof.

## Graph

```yaml
may-trigger: [design-test-strategy, estimate-blast-radius]
references: [review-component-boundaries, source-derived-patterns]
```
