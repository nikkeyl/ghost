---
name: analyze-build-pipeline
description: Analyze and improve CI/CD, repository hooks, dependency automation,
  and release artifacts. Use verify-change to run existing checks alone.
kind: active
---

# Analyze build pipeline

## Trigger

Use when a request changes automation, hook behavior, dependency-update
policy, release gates, or artifact contents.

## Goal

Analyze the pipeline and make scoped improvements that follow repository
conventions. Publish the intended contents only after relevant
verification.

## Investigation / reasoning

1. Read `.agents/rules/60-ci-cd.md`. Inspect existing configuration,
   manifests, lockfiles, hooks, branch policies, and user-selected
   references. Identify the actual provider, runtime, and consumers.

1. Map events to checks and publication. Identify required checks, the
   revision each step evaluates, permission boundaries, and retry
   behavior. Resolve uncertain provider semantics through primary
   documentation or a bounded experiment before changing the gate.

1. Identify the effective formatter and linter configuration, shared
   commands, and generated files. Separate portable conventions from
   application-specific steps in reference repositories.

1. Define the artifact contract: included paths, required layout,
   naming, license notices, and the verified source revision.

## Decision rules

- Adapt established configuration before inventing a new mechanism.
  Do not migrate providers or package managers merely to match an
  example. Install only tooling relevant to the repository's files.

- Prefer native dependencies and events. Treat fan-in, skipped checks,
  retries, and privileged triggers as behavior to verify rather than
  infer from workflow names.

- Keep rules in their owning configuration and make content comply.
  Do not disable a rule or add an exception merely to retain existing
  formatting. Follow explicit repository exceptions when present.

- Respect current authorization for remote changes. Preparing a
  workflow does not itself authorize deployment or publication.

## Actions

Implement the bounded configuration and connect it to existing local
commands. Keep linter workflows separate and hooks compatible with
staged edits. Configure update and merge automation only when requested.
Preserve unrelated user changes and avoid project-specific names,
versions, or publishing targets in reusable guidance.

## Verification

Run relevant formatters, linters, and configuration validators. For
changed release logic, exercise successful, missing, pending, and failed
check outcomes for the same revision, plus a retry or duplicate event.
Inspect the built artifact's paths and contents when packaging changes.

Within the authorized scope, inspect actual remote checks and published
artifacts. Report local validation separately when remote execution or
publication was not performed. Do not claim portability across providers
or agent hosts from structural validation alone.

## Completion criteria

The configuration follows repository conventions, required checks gate
the intended revision, and verification evidence covers the changed
contract. Artifact contents and any unexecuted remote behavior are
explicitly accounted for.

## Graph

```yaml
may-trigger: [research-unknown-api, analyze-change-impact, design-test-strategy]
followed-by: [verify-change]
```
