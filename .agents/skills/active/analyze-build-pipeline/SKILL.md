---
name: analyze-build-pipeline
description: Analyze how source, dependencies, configuration, and build stages
  produce artifacts locally and in CI; propose scoped improvements.
kind: active
---

# Analyze build pipeline

## Trigger

Use when build stages, inputs, generated outputs, local/CI differences,
or release gates need explanation or assessment. Running an existing
check alone belongs to `verify-before-claiming`.

## Goal

Explain the actual path from source to artifact, identify unsupported
assumptions, and recommend only changes justified by the requested task.

## Investigation / reasoning

1. Inspect entry commands, manifests, lockfiles, build configuration,
   generators, environment inputs, and workflow triggers. Identify
   runtime versions and package or workspace boundaries.

1. Trace the dependency graph from install through generation, compile,
   bundle, tests, packaging, and publication where those stages exist.
   Record each stage's inputs, outputs, prerequisites, and consumers.

1. Compare local and CI execution: working directory, installed tools,
   environment, secrets, cache keys, restored outputs, path filters,
   concurrency, and selected revision. Identify undeclared inputs and
   stale or partial outputs that could explain a difference.

1. Inspect logs and artifact contents. Measure stage duration or repeat
   a clean build only when correctness, reproducibility, or build cost
   is part of the question. Do not infer cache safety from a fast run.

1. For publication, read `.agents/rules/60-ci-cd.md` and trace required
   checks, immutable revision, artifact selection, trust, and retries.
   Hook and dependency-update wiring matter when they feed this path.

## Decision rules

- An analysis request produces a model and findings; it does not by
  itself authorize configuration edits, a new provider, or publication.

- Separate build correctness, verification coverage, reproducibility,
  and speed. A successful cached build cannot establish all four.

- Prefer native orchestration and existing repository conventions.
  Resolve uncertain provider or tool semantics through primary sources
  before relying on them. Do not add stages absent from the product.

## Actions

Produce a source-to-artifact stage map with commands, inputs, outputs,
revision, observed failures or costs, and the smallest recommended
correction. Apply a correction through `implement-minimal-change` only
when included in the task. Preserve the selected toolchain and explicit
artifact contract.

## Verification

Cross-check graph edges against scripts, configuration, logs, and files.
For an authorized change, exercise the affected stage and consumer. If
release gating changes, cover missing, pending, failed, and successful
checks plus a duplicate event. Inspect packaged contents when changed.
Report execution unavailable locally or remotely as a limitation.

## Completion criteria

The build path and material inputs are accounted for, each finding has
evidence, and recommendations distinguish observed behavior from
unverified assumptions. Applied changes have scoped proof; analysis
alone does not imply a build or publication occurred.

## Graph

```yaml
may-trigger: [research-unknown-api, estimate-blast-radius]
references: [implement-minimal-change, verify-before-claiming]
```
