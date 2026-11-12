# Developer verification

Use with `verify-before-claiming` for implementation submission and review
fixes, and with `design-test-strategy` when choosing evidence. Ordinary
research or a documentation correction does not require a full application
acceptance suite. Scale execution to the actual mandatory criteria.

## Requirements and checked state

Preserve the current specification, user decisions and unresolved review
feedback. Split compound criteria into scenarios retaining their source ID;
assign local IDs and quote requirements when no IDs exist. Keep additional
checks separate. Do not rewrite requirements around the implementation.

Record source commit and uncommitted changes, application build or deployed
SHA, environment, migrations, role and synthetic inputs as relevant. Mark
unknown versions explicitly. Local edits are not deployed changes. Reused
evidence applies only to behavior reasonably established as unchanged and
must retain its original version and limitations.

Before temporary changes, record original state and restoration steps. Use
authorized fixtures and complete available setup before declaring a scenario
unavailable. Honor prohibitions; an unavailable check is not a product defect.

## Observable execution

- Exercise UI paths through real interface actions using the required role;
  otherwise use the actual API, integration or background entry point. Wait
  for completion, inspect feedback, and reread persisted state through the
  relevant reload, reopen, navigation or new-session path.

- For permissions, use the actual restricted role and a positive control
  for an allowed action. Administrator success cannot prove restricted-role
  behavior. Do not bypass tenant isolation to obtain evidence.

- Check affected consumers, stored relationships, assignment and exposed
  data where required. Trace integration delivery to its intended recipient;
  a success toast, intermediate record or HTTP 200 is insufficient.

- Distinguish retrying one request identifier from a fresh submission with
  the same data. For promised safe retries after an unknown write outcome,
  arrange an authorized case where the write may succeed without its result
  reaching the caller, then exercise the actual recovery path. Verify final
  state and absence of duplicate effects; a definite pre-write failure does
  not test this guarantee.

- Choose relevant boundaries, invalid or expired links, failures,
  concurrency, cancellation, time, layout, accessibility and performance
  cases from the requirements. Preserve required measurement conditions;
  do not add unrelated load tests or change service limits without scope.

Match test actions and assertions to the criterion. Mocks and existing CI
records establish only what their boundaries exercised. Correct locator,
authentication and malformed-request failures before claiming a reproducible
product discrepancy. Evidence may be a sanitized response, assertion log,
screenshot or reproducible test; exclude secrets and unnecessary personal
data. Distinguish directly collected evidence from reused primary records.

## Failure, retest and restoration

After a failure, complete available independent checks and mark dependent
scenarios blocked by the shared cause. Fix only within authorized scope;
verification-only requests end with findings. Restore unexpected data changes
within authorization before continuing.

Preserve failed attempts and versioned retests. Reuse a defect ID for a shared
cause; fixing one symptom does not close every related criterion. Repeat the
original reproduction, affected journey and related consumer checks. Retain
unaffected evidence unless new changes cast doubt on it; unverified criteria
remain open.

Restore temporary data and settings through supported actions and reread
final state. Preserve required history, identify fixtures retained by
agreement, and state incomplete cleanup and the action needed.

## Readiness for independent acceptance

Use `.agents/templates/verification-record.md` or the project's equivalent.
Every mandatory scenario needs PASS, FAIL, BLOCKED or NOT_RUN, with expected
and actual results, versioned evidence and defect/blocker references. PASS
requires applicable evidence; BLOCKED and NOT_RUN need concrete reasons.

| Outcome                          | Condition                                                                                                            |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Ready for independent acceptance | Every mandatory scenario has evidence, required checks passed, no defects remain and authorized cleanup is verified. |
| Defects remain                   | A reproducible failure remains; report all findings and other scenario statuses.                                     |
| Verification incomplete          | No failure remains, but a mandatory scenario, project check or cleanup is unfinished; state what is needed.          |

Provide the verified version and report/evidence location. An authorized
incomplete handover does not turn missing checks into PASS. A tracker's
In Review status does not establish acceptance or Done. These checks do not
authorize release, publication, status changes or messages.
