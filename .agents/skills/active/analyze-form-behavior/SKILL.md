---
description: Analyze native form ownership, validation, submitted data,
  browser navigation, reset, and enhanced submission behavior.
kind: active
name: analyze-form-behavior
---

# Analyze form behavior

## Trigger

Use when creating, changing, extracting, or debugging a user-facing form
or its submit pipeline.

## Goal

Make the form's input constraints, state transitions, primary outcome,
and failure behavior explicit without turning every form into one
universal component.

## Investigation / reasoning

1. Identify each field's purpose, visible label, stable id, submitted
   name, native type, applicable autocomplete token, native constraints,
   domain validation, consent requirements, and server-side trust
   boundary.

1. Establish the browser baseline: form owner, action, method,
   submitter, implicit submission, native constraint validation, and
   the submitted data. Inspect control names, disabled or unchecked
   controls, duplicate names, and submitter-specific behavior rather
   than assuming UI state equals the request payload.

1. Trace the submit and reset paths, event handlers, default behavior,
   navigation, and progressive enhancement. Distinguish a browser
   submission from a programmatic or framework interception; verify
   the actual path before attributing validation or event behavior.

1. Build a state matrix covering idle, editing, invalid, consent
   missing when required, submitting, duplicate submission, primary
   success, primary failure, retry, and relevant mobile/keyboard behavior.

1. Separate the primary user-visible operation from secondary effects
   such as notifications, analytics, logging, or enrichment.

1. Decide which state is local, which data is server-owned, and whether
   a URL query parameter is actually appropriate.

1. In a Next.js repository, assess whether a Server Action is a suitable
   boundary for the mutation without hiding a needed client lifecycle.

1. Check whether shared form infrastructure contains only a stable core
   and leaves scenario-specific fields and business rules with the form
   owner.

1. For file inputs, identify the accepted types, size and count limits,
   displayed attachment state, and the server-side validation and
   storage boundary.

## Decision rules

- Do not submit while required fields are empty or invalid, or while
  required consent is missing.

- Prefer native form constraints where they express the contract, then
  add accessible domain validation and repeat authoritative validation
  on the server.

- Give each field a persistent visible label; use placeholder text only
  as an optional example or hint. Set required only when the user task
  truly requires the value, and use native input types and autocomplete
  tokens that match it.

- Show validation errors after a relevant interaction or submission
  attempt. Associate a field error with that field, expose invalid state
  only while the error is present, and make multi-field failure
  understandable without requiring the user to search the form.

- Keep submission available by default so the user can request
  validation. If product behavior disables it before submission, explain
  the unmet conditions and keep errors and correction paths available.

- Announce pending and completed submission through a status area
  separate from a disabled submit button; busy state alone is not a
  status message.

- Treat a file input's accept attribute as a chooser hint, not a
  security check. Validate file content and applicable size/count limits
  on the server.

- When two controls edit one value (for example, a range and numeric
  input), keep one canonical state and define one unambiguous submitted
  value.

- Reset fields and consent only after the primary operation is confirmed
  as successful. Preserve input after a primary failure so the user can
  correct it.

- Do not report a secondary notification or telemetry failure as a
  failed form submission when the primary operation succeeded; log it
  separately.

- Extract shared form infrastructure only for a stable repeated
  lifecycle. Keep business-specific fields and rules outside the shared
  core.

- Evaluate a Server Action only when the Next.js architecture and
  mutation contract support it. Keep browser-only interaction and
  high-frequency input at the boundary that owns them.

## Actions

Produce a form behavior trace from user action through validation,
submitted data, transport or navigation, response, and reset. Include
field ownership, enhancement boundaries, state transitions, and failure
outcomes. Recommend a correction from this trace; implement it only when
the task includes a fix.

## Verification

Inspect actual submitted data and browser navigation using relevant
submitters, Enter-key submission, reset, and enhanced versus native
paths. Check native and custom validation, missing consent, invalid fields,
pending and duplicate submission, primary success and reset, primary
failure and preserved input, secondary side-effect failure, keyboard
behavior, associated and announced error/status messages, autocomplete,
and the relevant server response paths. For file fields, test invalid
and oversized uploads against server validation. Verify that the chosen
shared abstraction has no consumer-specific prop accumulation.

## Completion criteria

The analysis explains the browser and enhancement paths, actual payload,
validation and reset behavior, and failure outcomes. Findings have
observed evidence or explicit limits; server/framework advice is
conditional on the repository rather than the core of the procedure.

## Graph

```yaml
followed-by: [verify-before-claiming]
may-trigger: [estimate-blast-radius]
references: [data-loading-and-failure-model, nextjs-server-actions]
requires: [plan-code-change]
```
