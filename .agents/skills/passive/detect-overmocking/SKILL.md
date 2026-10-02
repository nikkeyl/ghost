---
name: detect-overmocking
description: "Notice mocks that replace the very boundary a test claims to verify."
kind: passive
---

# Detect overmocking

During test or integration work, check whether the system under test is
mocked, a real transport or serialization contract is replaced with hand-built
values, or every assertion checks mock calls rather than relevant outcomes.

Name the bypassed boundary and claimed guarantee. Mocks for controlled,
expensive, or nondeterministic collaborators are not inherently a problem.
Escalate to `design-test-strategy` only when the missing boundary proof is
material; otherwise emit no material signal.
