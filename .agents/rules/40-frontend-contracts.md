# Frontend contracts

- Treat semantic HTML, keyboard behavior, focus, visible state, responsive
  layout, loading behavior, and reduced-motion behavior as part of a UI
  component's contract.
- Prefer native platform behavior before recreating it with JavaScript or ARIA.
- Keep a component's props narrow and derived from existing platform or schema
  types where that improves contract accuracy.
- Keep shared components ignorant of consumer-specific business concepts;
  prefer explicit slots/composition when the structure is genuinely shared.
- Keep reusable components focused on a stable core contract. Let consumers
  extend that core through composition, slots, children, or narrowly scoped
  callbacks instead of adding a prop for every consumer-specific case.
- Keep visual variants represented by a typed configuration table when that
  reduces duplicated conditional markup.
- Turn repeated visual decisions into semantic tokens or explicit variants.
  Keep a local value when it carries a distinct local meaning; do not create a
  token merely to remove one isolated literal.
- When the repository uses Tailwind with a `cn` utility, use `cn` to compose
  base, variant, state, and consumer class names. Inspect the utility's merge
  semantics before relying on override order.
- Treat a small number of Tailwind classes as potentially intentional. Check
  global CSS, existing component styles, design tokens, and native browser
  behavior before adding a utility class that duplicates an already-established
  rule.
- When a module supplies both values and types, keep them in one named import
  and mark the type specifier inline, for example
  `import { Button, type ButtonProps } from '@/ui/button'`, unless the
  repository has a stronger local convention.
- Apply a framework-specific convention only when the repository already uses
  the relevant tool or the task explicitly adopts it.
- Place client-only behavior at the smallest file boundary that needs it.
- Treat the server as the default execution boundary. Add client code only when
  interaction, browser APIs, or a material UX requirement makes it necessary.
- In a Next.js repository, prefer Server Actions for authorized server-side
  mutations when they fit the operation and do not obscure a needed client
  lifecycle or browser-only behavior. Validate inputs and handle failures on
  the server regardless of the transport.
- Validate claims about browser behavior against the supported browser matrix;
  do not promote a blog convention into a platform guarantee.
- Use text smaller than `14px` only in rare, explicitly justified cases; it is
  not a default size for body text, controls, labels, or important metadata.
- A form must not be submitted while required fields are empty or invalid, or
  while a required consent checkbox is not selected. Use native constraints and
  clear accessible error feedback where possible, and validate again on the
  server when the form crosses a trust boundary.
- After a successful form submission has been confirmed, reset the form fields
  and consent state. Preserve the user's input when submission fails so that
  they can correct the error without re-entering the form.
