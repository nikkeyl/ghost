---
name: review-form-contract
description: Review a form's validation, submission lifecycle, state ownership, server boundary, and primary or secondary failure behavior.
kind: active
---

# Review a form contract

## Trigger

Use when creating, changing, extracting, or debugging a user-facing form or
its submit pipeline.

## Goal

Make the form's input constraints, state transitions, primary outcome, and
failure behavior explicit without turning every form into one universal
component.

## Investigation / reasoning

1. Identify the form's fields, native constraints, domain validation, consent
   requirements, and server-side trust boundary.
2. Build a state matrix covering idle, editing, invalid, consent missing,
   submitting, duplicate submission, primary success, primary failure, retry,
   and any relevant mobile or keyboard behavior.
3. Separate the primary user-visible operation from secondary effects such as
   notifications, analytics, logging, or enrichment.
4. Decide which state is local, which data is server-owned, and whether a URL
   query parameter is actually appropriate.
5. In a Next.js repository, assess whether a Server Action is a suitable
   boundary for the mutation without hiding a needed client lifecycle.
6. Check whether shared form infrastructure contains only a stable core and
   leaves scenario-specific fields and business rules with the form owner.

## Decision rules

- Do not submit while required fields are empty or invalid, or while required
  consent is missing.
- Prefer native form constraints where they express the contract, then add
  accessible domain validation and repeat authoritative validation on the
  server.
- Reset fields and consent only after the primary operation is confirmed as
  successful. Preserve input after a primary failure so the user can correct it.
- Do not report a secondary notification or telemetry failure as a failed form
  submission when the primary operation succeeded; log it separately.
- Extract shared form infrastructure only for a stable repeated lifecycle. Keep
  business-specific fields and rules outside the shared core.
- Prefer a suitable Server Action for a Next.js server-side mutation, but do
  not move browser-only interaction or high-frequency input handling there.

## Actions

Produce a compact form contract with field constraints, state transitions,
primary and secondary outcomes, chosen server boundary, and the smallest
implementation change needed to preserve it.

## Verification

Check native and custom validation, missing consent, invalid fields, pending and
duplicate submission, primary success and reset, primary failure and preserved
input, secondary side-effect failure, keyboard behavior, and the relevant
server response paths. Verify that the chosen shared abstraction has no
consumer-specific prop accumulation.

## Completion criteria

The form has an explicit validation and state contract, a justified server
boundary, correct reset and failure behavior, and evidence for each material
state that was claimed as verified.

## Graph

```yaml
requires: [understand-and-plan-change]
may-trigger: [analyze-change-impact]
followed-by: [verify-change]
references: [data-loading-and-failure-model, nextjs-server-actions]
```
