# Source-derived frontend patterns

This file records heuristics distilled from the articles. Verify against
the current project before applying them.

## Components

- Separate a component implementation from a large props contract when
  that reduces import weight and improves navigation.

- Compose props from native or generated types when the external
  contract is already defined there.

- Avoid a universal component type whose optional fields represent
  unrelated product variants.

- Use a typed module-level lookup for static visual variants when it
  keeps JSX declarative and complete.

- Use slots or composition when the shared layout is real and consumers
  should own their content.

- Keep effects near the end of a component only as a readability
  convention; dependency correctness and lifecycle semantics remain
  primary.

## Semantic UI

- Use anchors for navigation and buttons for actions; do not recreate
  their browser behavior with a clickable generic element.

- Give inline links a persistent visual distinction from surrounding
  text. Communicate a new-tab behavior before activation; use noopener
  when a new browsing context is intentionally opened, and add
  noreferrer only when suppressing the referrer is also a requirement.

- Use table markup for data that has row-and-column relationships.
  Associate simple headers with their scope; use explicit header ids and
  cell references when a complex header structure needs them. Put
  responsive overflow on a named, keyboard-accessible wrapper rather
  than changing the table's display model.

- For tabs, use the tab pattern only for same-page panels. Keep
  tablist/tab/ tabpanel roles, ids and references, selected state,
  roving focus, and keyboard behavior coherent. Choose automatic or
  manual activation according to interaction latency. If tab selection
  is URL-addressable, support direct loading and history navigation; do
  not assume pushState/replaceState emits hashchange.

- Give a carousel an accessible name and useful slide-position
  information. Base navigation on actual scroll positions and overflow,
  not merely slide count. Keep offscreen content out of focus
  navigation; use a polite live region for user-driven changes and
  disable live announcements during automatic rotation. Make automatic
  rotation controllable and stop it on focus or hover; do not restart it
  without a user request.

- Prefer `nav`/`ol` for breadcrumb and pagination navigation.

- Expose current state with the appropriate semantic or ARIA state.

- Prefer native `details`/`summary` or `dialog` when their behavior
  matches the component contract; add only the missing behavior.

- Check focus, keyboard, escape, backdrop, scroll-lock, reduced motion,
  and mobile viewport behavior for overlays and menus.

- Provide captions, transcript/description, poster, and fallback content
  for meaningful video.

## Performance and platform

- Choose image alternatives by meaning and context: empty alt for
  decorative images, purposeful text for meaningful images, and a text
  equivalent for important information conveyed only by a complex
  graphic.

- Reserve image layout space with intrinsic dimensions or a known aspect
  ratio. Use responsive sources and sizes that reflect the rendered
  slot; defer offscreen images without deferring a critical image
  already in view.

- Treat formats, quality, and eager/high-priority loading as per-asset
  choices to verify; do not apply one size, quality, or priority budget
  universally.

- Treat crawler and social metadata as signals to consuming platforms,
  not promises of indexing, rankings, rich results, or a particular
  preview.

- Map an implementation choice to a browser mechanism and then to a user
  or product consequence.

- Treat budgets such as page weight, video size, CLS, LCP, and TTI as
  measured targets tied to a device/network profile, not universal
  constants.

- Check viewport units, safe-area insets, font loading, HMR sockets,
  proxies, and browser-specific media policies against the supported
  matrix.
