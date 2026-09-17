# Data and failure contracts

These rules apply when a page or operation depends on multiple data sources,
libraries, or side effects.

- Load data and dependencies only where they are needed. Keep route-specific
  data, parsers, renderers, and heavy libraries out of global layouts and shared
  entry points when only a narrower route uses them.
- Use `cache: 'no-store'` or an equivalent fresh-read policy only when stale data
  can violate the user-visible or business contract. Do not make uncached reads
  a default without evidence that freshness requires them.
- Classify each dependency as essential, partial, or secondary before choosing
  its failure behavior.
- If essential page content is absent entirely, fail the page with the
  repository's not-found or error behavior. Do not render a misleading shell
  without the content that gives the page its purpose.
- If only part of the content is absent, render the available content and omit
  the unavailable part. Do not invent placeholder values or expose an empty
  block as if it contained real data.
- If secondary data such as a rating, counter, or aggregate is unavailable,
  use a defined fallback or render nothing when no meaningful fallback exists.
- Separate the primary outcome of a pipeline from secondary side effects. If
  the primary operation succeeds but a secondary notification, telemetry, or
  enrichment step fails, preserve the successful result and log the secondary
  failure for diagnosis.
- Report a user-facing failure when the primary outcome did not complete or the
  user-visible contract was materially violated; do not expose an incidental
  secondary failure as if the main operation failed.
