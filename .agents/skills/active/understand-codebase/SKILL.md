---
name: understand-codebase
description:
  Build an evidence-backed repository context model before changing an unfamiliar or
  cross-cutting codebase.
kind: active
---

# Understand a codebase

## Trigger

Use when the repository is unfamiliar, ownership is unclear, the change crosses
module or runtime boundaries, or the existing context model is too weak to plan the
requested work safely.

## Goal

Produce the smallest useful repository context model that explains where the change
belongs, which contracts it crosses, what it must not touch, and how the result will
be verified.

## Investigation / reasoning

1. Establish the scoped entry points, repository instructions, package/build
   boundaries, and relevant tests or generated artifacts.
2. Map only the modules and domains relevant to the requested change. Record each
   module's responsibility, owner, inputs, outputs, and important consumers.
3. Trace the relevant data and control flow from entry point to side effects. Include
   request, event, state, or rendering transitions when they affect the contract.
4. Identify runtime boundaries such as client/server, build/runtime, browser/host,
   process/service, persistence, and external APIs.
5. Identify the source of truth for behavior, data, configuration, and public
   contracts. Search for adapters, generated files, schemas, and compatibility layers
   that may encode the same contract.
6. Check path semantics: whether parent directories communicate ownership, whether
   filenames redundantly repeat that context, and whether an existing FSD or
   equivalent layer/slice convention is being followed.
7. Record unknowns, assumptions, hypotheses, risks, and explicit exclusions. Stop
   when the model is sufficient to place and verify the change; do not inventory
   unrelated repository areas.

## Decision rules

- Start from the requested behavior and follow evidence outward; do not map the
  entire repository by habit.
- Prefer repository evidence over generic framework conventions. Label an inference
  when the repository does not establish it directly.
- Treat a shared module, public export, generated artifact, runtime boundary, or
  source-of-truth conflict as a material risk that needs explicit impact analysis.
- Distinguish a module's ownership from its reuse count. A one-consumer domain module
  can still be the correct owner of its logic.
- Let the path provide context and the leaf name provide local responsibility. Treat
  duplicated context as a signal to investigate, not an automatic error; framework,
  generated, public, or relocation contracts may justify it.
- Apply FSD-style plural layer groups, singular slices, and conventional internal
  segments only when the repository already demonstrates that convention.
- Do not infer data or control flow from names alone. Confirm it through imports,
  call sites, types, tests, configuration, or runtime evidence.
- If evidence is insufficient to place the change or define verification, surface the
  smallest unresolved question instead of inventing a boundary.

## Actions

Produce a repository-context checkpoint using
`.agents/templates/repository-context.md` or the same section order:

- scope and desired outcome;
- module and ownership map;
- runtime boundaries;
- relevant data and control flows;
- source-of-truth and contract map;
- path semantics and naming exceptions;
- unknowns, assumptions, risks, and exclusions;
- evidence links with file paths, line references, commands, or observations;
- placement decision and verification plan.

Keep the checkpoint concise. Include only the context needed for the current change
and name follow-up investigation rather than expanding the active scope.

## Verification

Check that every planned change has an identified owner and entry point, every
crossed boundary has a named contract or risk, path names communicate the observed
repository convention or have an explicit exception, the important flows have
evidence, and the verification plan can falsify the material failure modes. Re-check
the exact files and line references before reporting the checkpoint.

## Completion criteria

The repository context is sufficient to explain where the change belongs, what it
depends on, which consumers or boundaries may be affected, what remains unknown, and
how success will be verified without rediscovering the same structure during
implementation.

## Graph

```yaml
requires: [understand-and-plan-change]
may-trigger: [analyze-change-impact]
followed-by: [implement-minimal-change, verify-change]
```
