# Frontend contracts

- Treat semantic HTML, keyboard behavior, focus, visible state, responsive
  layout, loading behavior, and reduced-motion behavior as part of a UI
  component's contract.
- Prefer native platform behavior before recreating it with JavaScript or ARIA.
- Keep a component's props narrow and derived from existing platform or schema
  types where that improves contract accuracy.
- Keep shared components ignorant of consumer-specific business concepts;
  prefer explicit slots/composition when the structure is genuinely shared.
- Keep visual variants represented by a typed configuration table when that
  reduces duplicated conditional markup.
- Apply a framework-specific convention only when the repository already uses
  the relevant tool or the task explicitly adopts it.
- Place client-only behavior at the smallest file boundary that needs it.
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
