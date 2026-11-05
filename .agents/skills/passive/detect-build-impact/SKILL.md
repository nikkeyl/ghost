---
name: detect-build-impact
description: "Notice dependency, lockfile, generated-output, and CI changes outside
  the verified change boundary."
kind: passive
---

# Detect build impact

During changes to manifests, lockfiles, generators, build configuration,
or CI, compare their effect with the requested contract and verification
scope. Look for unexplained lockfile churn, generated output without its
source, new required environment inputs, and affected packages omitted
from checks.

Confirm what changed before calling it broken. Report the affected
boundary, consumers, and missing evidence. Escalate to
`analyze-change-impact` or `verify-change` when the build or release
guarantee is materially affected; otherwise emit no material signal.
