---
name: improve-test-signal
description: "Notice changed behavior whose tests can pass without exercising the
  relevant failure mechanism."
kind: passive
---

# Improve test signal

During test changes or completion checks, look for missing assertions,
swallowed failures, snapshots that miss the behavioral contract,
regressions never demonstrated, or retries presented as a clean first
pass.

Report the specific behavior the test cannot falsify and evidence from
its setup and assertions. Missing tests alone are not proof of a defect.
Escalate to `design-test-strategy` when a material acceptance criterion
lacks effective evidence; otherwise emit no material signal.
