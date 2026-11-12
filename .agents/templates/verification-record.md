# Verification record

## Contract and checked state

State acceptance criteria, baseline, changed paths, and relevant
environment. For implementation handover, include the specification and
user decisions, source commit/uncommitted changes, build or deployed SHA
(explicitly unknown if unavailable), migrations, role, synthetic inputs
and date. Record authorized temporary changes and their restoration plan.

## Results

| Criterion / scenario ID and source | Preconditions, role and inputs | Actions / method | Expected / actual result | Status | Versioned evidence and limits | Defect / blocker ID |
| ---------------------------------- | ------------------------------ | ---------------- | ------------------------ | ------ | ----------------------------- | ------------------- |

Include every mandatory criterion, splitting compound scenarios under its
source ID. Keep additional checks separate. Use PASS, FAIL, BLOCKED or
NOT_RUN with concrete reasons for missing evidence. Distinguish checks run
directly from reused records; never include secrets or unnecessary personal
data. A check is valid only for the state it exercised.

## Project checks and retests

Record commands, conditions, outcomes and significant skips. Preserve failed
attempts, fixes and versioned retests with shared defect IDs where relevant.

## Restoration

Record original state, cleanup action, read-back evidence, remaining work
and fixtures retained by agreement. Omit fixture details when none were used.

## Plan versus implementation

Account for implemented, intentionally changed, omitted, and blocked
units, plus unplanned paths. State the material assumptions or
counterexamples checked.

## Completion claim

State exactly what the evidence supports, remaining uncertainty, and
follow-up. Separate structural validation, manual walkthroughs, and real
runtime trials. For implementation submission, use the readiness conditions
in `.agents/knowledge/developer-verification.md`: ready for independent
acceptance, defects remain, or verification incomplete. Other technical
claims need only their relevant evidence and limitations.
