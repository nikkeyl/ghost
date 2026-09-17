# User-confirmed patterns from 501rose.kimdevs.ru

This document records patterns extracted from Nikkeyl's direct commits in the
`501rose.kimdevs.ru` repository. It is evidence and rationale, not an
additional instruction layer. Normative constraints belong in `.agents/rules`;
procedures belong in `.agents/skills`.

Primary evidence was limited to the user's authored commits. Team and merge
commits were not used to infer the user's personal engineering principles.

## Confirmed patterns

- Move route-specific data and expensive work out of global boundaries.
- Place code by responsibility and ownership in an FSD-style structure.
- Keep single-use domain logic local; promote it after real reuse rather than
  hypothetical reuse.
- Adapt external data into a UI-oriented model when that removes repeated
  plumbing and preserves a useful boundary.
- Keep reusable components focused on a stable core and extend them from the
  outside.
- Centralize stable repeated form and data contracts while keeping business
  scenarios explicit.
- Use local client state for transient feature interactions and URL query
  parameters for shareable or reloadable state.
- Use debounce for high-frequency input, cancellation for obsolete work, and a
  freshness check when asynchronous responses can race.
- Keep domain calculations separate from UI when they have independent rules
  and edge cases.
- Keep `refactor` commits behavior-preserving; describe behavioral changes with
  an appropriate commit type.
- Compose Tailwind classes through the repository's `cn` utility when base,
  variant, state, and external overrides have to coexist.
- Keep utility-class usage deliberately small when global CSS, existing
  components, design tokens, or browser behavior already provide the needed
  result.
- If values and types come from the same module, use an inline `type` modifier
  in the named import instead of splitting the import without a reason.

## Confirmed formatting hierarchy

Formatting is a toolchain, not one flat rule list. Interpret it in this order:

1. **EditorConfig** provides the file baseline: encoding, line endings,
   indentation, final newline, trailing whitespace, and repository line-length
   guidance.
2. **Prettier** owns syntactic formatting and quote style. Its plugins extend
   that formatting; in these projects `prettier-plugin-tailwindcss` orders
   Tailwind utility tokens.
3. **ESLint** checks code conventions and likely defects around the formatted
   code: imports, exports, naming, destructuring, JSX props, component form,
   unsafe TypeScript escapes, and GraphQL operations.
4. **Hooks and CI** enforce the applicable checks at change and integration
   boundaries. They are verification gates, not a second formatting style.

The hierarchy is a routing model, not permission to duplicate settings. When
two tools overlap, follow the repository's effective configuration and use the
narrowest owner for the decision. A formatter should not silently override a
semantic lint rule, and a lint warning should not justify broad unrelated
reformatting.

## Contextual boundaries

- UI-oriented mapping is a decision, not a universal adapter layer. Direct API
  data can be acceptable when it is already the stable shape the UI needs.
- `cache: 'no-store'` is appropriate for freshness-sensitive data, not for all
  requests.
- Server Actions are a Next.js-specific preference for suitable mutations, not
  a general frontend rule.
- A complex one-use unit may be decomposed locally without being promoted to a
  shared module.

## Evidence index

- `f4a3dff`, `8776b19` — route-local data loading and query boundaries.
- `6c30841`, `75b9528`, `e811365` — responsibility and page/component
  restructuring.
- `4a72038`, `f42de5e`, `259a63f` — transport-to-UI shaping.
- `b48beb5`, `29865f9` — repeated query and form contracts.
- `014b765`, `9516b6f`, `9a972d8` — URL-driven search and filtering.
- `f9c5c42`, `be6a463`, `c3a5b71` — local interaction state and async modal/cart
  behavior.
- `a1562e8` — isolated calculation logic and edge handling.
