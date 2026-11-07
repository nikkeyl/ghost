# CI/CD

## Repository conventions

- Inspect existing configuration and user-selected reference repositories
  before adding automation. Reuse their standard names and structure,
  adapting only what the current repository needs.

- Preserve the chosen runtime, package manager, lockfile, and supported
  environments. Prefer reproducible installs and native platform or
  maintained ecosystem tools over custom wrappers and extra runtimes.

- Keep each linter's workflow independently named and observable. Share
  the underlying commands between local tooling, hooks, and CI rather
  than maintaining different rule sets for each execution environment.

- Use the repository's commit and pull-request title conventions. Add
  hooks, dependency updates, and automatic merging only within the
  requested scope; automatic merging must respect required checks and
  the intended dependency-update actor.

## Hooks and verification

- Keep staged-file hooks scoped to staged files and preserve unrelated
  unstaged edits. Sequence tasks that write and then inspect the same
  files. Inspect the resulting diff before committing.

- Hooks may format files locally. CI checks must report violations
  without silently modifying the proposed change. Passing a local hook
  does not establish that remote CI passed.

- Give automation only the permissions and credentials needed by its
  job. Keep untrusted contributions outside privileged execution paths.
  Apply the repository's dependency and action pinning policy, including
  transitive action references where the provider enforces it.

## Release contract

- Publish only after all required checks succeed for the same immutable
  revision used to build the artifact. Missing, pending, failed, or
  cancelled checks do not satisfy the gate.

- Prefer native workflow dependencies or completion events. Verify their
  actual dependency semantics: completion of one independent workflow
  does not imply success of the others. Add coordination only when the
  provider cannot express the required gate directly.

- Build from the verified revision rather than a moving branch. Follow
  repository conventions for tags, release names, archive names, and
  archive roots. Keep repeated events and retries from producing
  duplicate publications or overwriting a different revision.

- Select artifact contents explicitly for their downstream consumers.
  Preserve required discovery paths and license notices. Include
  planning documents, reports, and tooling only when they belong to the
  distributed product.

- Distinguish local checks, remote workflow results, and published
  artifact inspection in completion reports. Guidance does not grant
  permission to publish; the current task and existing authorization
  determine which external actions are in scope.
