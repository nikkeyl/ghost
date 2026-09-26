# Data loading and failure model

This mental model separates loading locality from failure criticality. It is a
decision aid, not a requirement to use one specific framework or data client.

## Loading locality

Load a data source or dependency at the narrowest boundary that owns its use.
A library used only to render article Markdown belongs to the article route or
its local rendering boundary; importing it from the root layout expands the
cost of every route and hides the real dependency relationship.

The same principle applies to API requests, parsers, syntax highlighters,
analytics, and other expensive work. Route-level or component-level loading is
preferable when it preserves ownership and keeps unrelated pages out of the
critical path.

## Criticality classes

- **Essential** — without it, the page or operation cannot fulfil its primary
  purpose. Missing it should produce the established error or not-found result.
- **Partial** — one content block or field is missing, but the rest of the page
  remains meaningful. Render what is available and omit the missing part.
- **Secondary** — useful enrichment such as ratings, counters, telemetry,
  notifications, or recommendations. Use a meaningful fallback or render
  nothing when the value is unavailable.

## Pipeline outcomes

Model a multi-step operation around its primary user-visible outcome. Persistence
of a lead is primary; a Telegram notification after persistence is secondary.
The notification may be retried or logged independently without converting a
successful persistence result into a failed form submission.

Promise combinators coordinate asynchronous results; they do not create a
transaction across destinations or roll back completed side effects. When one
user action writes to multiple systems, define which persisted outcome counts
as accepted, how partial delivery is reported and recovered, and where retries
and duplicate prevention are owned. Retrying a side effect is safe only when
its idempotency or deduplication contract is understood.

The failure message should describe the failed user-visible outcome, not every
internal step that encountered an error. Observability still needs the internal
failure with enough context to diagnose it.

## Transport and UI models

Whether to adapt transport data into a UI-oriented model is contextual. Choose
the boundary that best preserves ownership, change isolation, composability,
and the stability of the external contract. A mapper is useful when the API
shape is noisy or unstable; direct use can be reasonable when the backend shape
is already the stable model the UI needs.

## Abstraction and ownership

Keep a one-use domain concept near the feature or route that owns it. A local
extraction can still improve readability or complexity without making the code
shared. Promote it only when another real consumer appears or when a stable
cross-domain contract has been deliberately established.

## State ownership

Choose the state boundary by semantics rather than by the fact that an operation
makes a request:

- **Local client state** — transient interaction state owned by one feature,
  such as an open modal, draft selection, or a cart interaction.
- **URL state** — filters, search, pagination, and other state that should be
  reloadable, navigable, or shareable through a link.
- **Server state** — persisted business facts whose authoritative value belongs
  to the backend and may require reconciliation with client state.
