# Repository context checkpoint

Use this template for the smallest repository model needed to plan a change. Replace
placeholders with evidence; omit sections that are genuinely out of scope, but do not
omit an unresolved risk silently.

## Scope and desired outcome

- Requested outcome:
- In scope:
- Explicit non-goals:

## Module and ownership map

| Area / path | Responsibility | Owner / source of truth | Relevant consumers |
| ----------- | -------------- | ----------------------- | ------------------ |
|             |                |                         |                    |

## Runtime boundaries

- Entry points:
- Client/server or process boundaries:
- Build/runtime or generated-artifact boundaries:
- External services, persistence, or host APIs:

## Relevant flows

### Data flow

`entry point → transformation → state/storage → consumer`

Evidence:

### Control or event flow

`trigger → handler → side effect → observable result`

Evidence:

## Contracts and source of truth

- Public or shared contracts:
- Schemas, generated files, adapters, or compatibility layers:
- Behavioral source of truth:

## Path semantics

- Established file and directory naming convention:
- Does the parent path communicate domain, layer, or slice ownership?
- Does any filename redundantly repeat context already supplied by its path?
- Does the repository use FSD or an equivalent layer/slice convention?
- Naming exceptions required by a framework, generator, public contract, or existing
  repository layout:

## Unknowns, assumptions, and risks

- Fact:
- Assumption:
- Hypothesis:
- Risk and mitigation:
- Follow-up investigation:

## Placement and verification

- Planned owner and change location:
- Files or behaviors that must not change:
- Verification commands or observations:
- Evidence links:
