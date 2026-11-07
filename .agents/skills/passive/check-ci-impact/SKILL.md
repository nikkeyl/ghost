---
description: Check whether a change affects CI triggers, job dependencies,
  tools, permissions, required checks, caches, or artifact publication.
kind: passive
name: check-ci-impact
---

# Check CI impact

During changes to source paths, scripts, manifests, lockfiles, generated
files, build configuration, or workflows, trace whether CI still runs
the relevant commands for the affected revision and events.

Inspect path and branch filters, working directories, renamed commands,
runtime/tool versions, environment inputs, job dependencies, required
status names, cache inputs, permissions, and artifact paths. A source
rename can bypass a path filter even when no workflow file changed.
Distinguish local build impact from an actual CI execution consequence.

Report the changed input, affected event/job/check, consequence, and
missing or observed evidence. Escalate to `analyze-build-pipeline` for
an unclear pipeline path, `estimate-blast-radius` for affected consumers,
or `verify-before-claiming` for missing execution evidence. A lockfile
diff alone is not a CI defect; emit no material signal when the pipeline
contract remains covered.
