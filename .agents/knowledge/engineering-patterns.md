# Engineering patterns

This document records reusable engineering patterns confirmed through source analysis
and user review. It is knowledge and rationale, not an additional instruction layer.
Normative constraints belong in `.agents/rules`, and procedures belong in
`.agents/skills`.

## Confirmed engineering patterns

- Start with the minimum necessary code, structure, state, dependencies, and
  component props. Expand the solution only when the current contract, demonstrated
  variation, or measured complexity requires it.
- Prefer a known and maintained package over a bespoke implementation for a
  non-trivial capability when it fits the repository's constraints. Keep small,
  stable behavior local or native when adding a dependency would create more
  complexity than it removes.
- Extract stable shared, configuration, and domain values into named uppercase
  constants when their identity matters beyond one expression. Keep genuinely local
  one-off values local when naming would not improve understanding.
- Prefer a typed map or lookup table for finite data mappings, variants, and
  strategies. Keep conditionals when they express control flow, predicates,
  sequencing, or dependencies between operations.
- Prefer `??` for nullish defaults and reserve `||` for cases where all falsy values
  intentionally represent the same fallback condition. Use a ternary for a short
  value choice and a block `if` for multi-step behavior.
- `switch`/`case` is not part of the preferred style. Represent finite data mappings
  as typed objects and express behavioral branches with the simplest readable
  conditional structure.
- Keep synchronous code synchronous. An `async` marker is justified by a real
  asynchronous operation, required API, or meaningful consumer contract, not by
  stylistic consistency.
- Load route-specific data and expensive work at the narrowest boundary that needs
  them.
- Place code by responsibility and ownership. Keep single-use domain logic local and
  promote it only after real reuse appears.
- Make local paths predictable. Let parent directories provide domain, layer, or
  slice context, and name the leaf file after its local responsibility instead of
  repeating the path context. Keep repetition when a framework, generator, public
  contract, frequent relocation, or import readability gives it a concrete reason.
- When a repository has adopted FSD or an equivalent layer/slice structure, preserve
  its established path semantics: layer groups may be plural, slices may be singular,
  and internal segments such as `ui`, `model`, and `api` may remain stable. Verify
  the repository convention before applying it; this is not a universal folder
  taxonomy.
- Adapt transport data to a UI-oriented model when that removes repeated plumbing and
  preserves a useful boundary. Direct transport data is valid when it already has the
  stable shape the UI needs.
- Keep reusable components focused on a stable core and extend them from the outside
  through composition, slots, children, or narrow callbacks.
- Centralize stable repeated form and data contracts while keeping business scenarios
  explicit.
- Keep transient feature interactions in local client state. Use URL query parameters
  for state that should be shareable, reloadable, or represented in navigation.
- Use debounce for high-frequency input, cancellation for obsolete work, and a
  freshness check when asynchronous responses can race.
- Keep domain calculations separate from UI when they have independent rules and edge
  cases.
- For deterministic regex, validation, and transformation utilities, focused unit
  tests covering valid, invalid, and edge cases are the primary evidence. Add
  integration or build checks when the risk crosses a package, runtime, or
  generated-output boundary.
- Separate pure computation from reporting and other side effects by default. A small
  utility may combine them when reducing consumer complexity is the explicit goal and
  the side effect is part of the documented contract.
- Keep `refactor` commits behavior-preserving; describe behavioral changes with an
  appropriate commit type.
- Compose Tailwind classes through the repository's `cn` utility when base, variant,
  state, and external overrides have to coexist.
- Keep utility-class usage deliberately small when global CSS, existing components,
  design tokens, or browser behavior already provide the needed result.
- If values and types come from the same module, use an inline `type` modifier in the
  named import instead of splitting the import without a reason.

## Formatting hierarchy

Formatting is a toolchain, not one flat rule list. Interpret it in this order:

1. **EditorConfig** provides the file baseline: encoding, line endings, indentation,
   final newline, trailing whitespace, and repository line-length guidance.
2. **Prettier** owns syntactic formatting and quote style. Its plugins extend that
   formatting; a Tailwind plugin may order utility tokens.
3. **ESLint** checks code conventions and likely defects around the formatted code:
   imports, exports, naming, destructuring, JSX props, component form, unsafe
   TypeScript escapes, and GraphQL operations.
4. **Hooks and CI** enforce the applicable checks at change and integration
   boundaries. They are verification gates, not a second formatting style.

The hierarchy is a routing model, not permission to duplicate settings. When two
tools overlap, follow the repository's effective configuration and use the narrowest
owner for the decision. A formatter should not silently override a semantic lint
rule, and a lint warning should not justify broad unrelated reformatting.

## Contextual boundaries

- UI-oriented mapping is a decision, not a universal adapter layer.
- `cache: 'no-store'` is appropriate for freshness-sensitive data, not for all
  requests.
- Server Actions are a framework-specific preference for suitable mutations, not a
  general frontend rule.
- A complex one-use unit may be decomposed locally without being promoted to a shared
  module.
