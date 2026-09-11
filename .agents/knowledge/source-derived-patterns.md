# Source-derived frontend patterns

This file records heuristics distilled from the articles. Verify against the
current project before applying them.

## Components

- Separate a component implementation from a large props contract when that
  reduces import weight and improves navigation.
- Compose props from native or generated types when the external contract is
  already defined there.
- Avoid a universal component type whose optional fields represent unrelated
  product variants.
- Use a typed module-level lookup for static visual variants when it keeps JSX
  declarative and complete.
- Use slots or composition when the shared layout is real and consumers should
  own their content.
- Keep effects near the end of a component only as a readability convention;
  dependency correctness and lifecycle semantics remain primary.

## Semantic UI

- Prefer `nav`/`ol` for breadcrumb and pagination navigation.
- Expose current state with the appropriate semantic or ARIA state.
- Prefer native `details`/`summary` or `dialog` when their behavior matches the
  component contract; add only the missing behavior.
- Check focus, keyboard, escape, backdrop, scroll-lock, reduced motion, and
  mobile viewport behavior for overlays and menus.
- Provide captions, transcript/description, poster, and fallback content for
  meaningful video.

## Performance and platform

- Map an implementation choice to a browser mechanism and then to a user or
  product consequence.
- Treat budgets such as page weight, video size, CLS, LCP, and TTI as measured
  targets tied to a device/network profile, not universal constants.
- Check viewport units, safe-area insets, font loading, HMR sockets, proxies,
  and browser-specific media policies against the supported matrix.
