# Code style

These are the GHOST authoring defaults for relevant source files. An
explicit user choice, established public contract, or adopting
repository configuration takes precedence. Name a conflict instead of
silently mixing styles. Do not reformat unrelated code or install every
mentioned tool into a project that does not use its language.

## Files and formatting

- Use UTF-8, LF, two-space indentation, a final newline, and no trailing
  whitespace. Respect required file formats and generated output.

- Use 85 characters as source line-length guidance when no stronger
  file-specific rule exists. Let the formatter wrap code; Markdown,
  URLs, tables, and generated files follow their effective rules.

- Use semicolons, parenthesized arrow parameters, normal object-brace
  spacing, and trailing commas in supported multiline syntax. Let the
  formatter decide wrapping and punctuation rather than recreating its
  complete settings in prose or a competing linter configuration.

- Use single quotes for JavaScript/TypeScript strings and quoted YAML
  scalars. In TSX, apply this to JavaScript strings; JSX attribute quotes
  follow the explicit JSX formatter option. JSON keeps its required
  double quotes. Escaping and language syntax remain formatter-owned.

- Separate logical statement groups with one blank line. Put a blank
  line before `return`, `throw`, control-flow statements and loops, and
  after completed blocks before another statement. Separate declaration
  groups from executable statements and independent multiline
  declarations or callback registrations. Consecutive short declarations
  for one purpose may stay together; do not pad a lone statement.

- Keep formatting, lint rules, type checking, and verification distinct.
  A formatter pass cannot prove import validity, function form, Hook
  correctness, or semantic statement spacing. Fix code to the selected
  rules instead of adding exceptions merely to preserve old formatting.

## File boundaries

- Keep one primary standalone function per handwritten implementation
  file. Put each independent module-level helper in its own colocated
  file and import it, even when it is small or has only one consumer.
  Apply this convention within the authorized change; leave unrelated
  existing files alone.

- Keep short callbacks and owner-bound handlers or closures inside the
  function that owns their state and lifecycle. A local name or a simple
  conditional does not by itself require a separate file. Extract
  independent parsing, formatting, validation, date, storage, and
  calculation logic instead of embedding it in an entry point or mixing
  it with unrelated responsibilities.

- Declare types and interfaces in separate files and import them, using
  type-only imports where supported. Group related types by domain or
  contract. Keep schemas, configuration objects, lookup tables, and
  standalone constants in dedicated files and import them. Keep local
  calculation variables inside their owning function.

- Let filenames communicate the file's role. Follow existing conventions
  such as `.props`, `.type`, `.schema`, and `.config` when the project
  uses them; do not impose language-specific suffixes universally.
  Type-only and configuration-only files do not need a function.

- Keep files near the feature or module that owns them. A single
  consumer does not justify combining standalone functions, and
  extraction does not require promotion into a shared layer. Do not
  gather unrelated entities into generic utils, helpers, types, or
  constants files.

- Preserve required language and platform structures, generated output,
  and explicit project conventions. Entry-point adapters may retain
  required exports while delegating substantive logic to imported
  functions. Retain an existing public import path when compatibility
  requires it; do not add wrappers or barrels merely to split code.
  Tests may group related scenarios in one file. Explain necessary
  exceptions; a small demo or a passing formatter is not an exception.

## Functions, values and names

- Declare named functions and components as `const` arrow functions and
  use arrow callbacks. Retain another form only for a real contract such
  as overloads, generators, constructors, dynamic `this`, or intentional
  hoisting. Check initialization order before converting declarations.

- Prefer immutable bindings and do not mark synchronous work `async` for
  style. Keep `if`/ternary/map choices and nullish defaults consistent
  with `.agents/rules/00-operating-principles.md`.

- Prefer object property shorthand when key and binding have the same
  name. Do not rename a public key or change a method's `this` behavior
  just to achieve shorthand or arrow syntax.

- Sort independent named elements alphabetically within an appropriate
  existing group, such as data-object keys, dependency names, or values
  in an enumeration-style list. Preserve the established document
  structure and semantic grouping of configuration files. Do not reorder
  workflow, job, or step fields, package manifest sections, or other
  configuration blocks merely to alphabetize their keys. For example,
  sort the workflow-name list without moving `name`, `on`, `permissions`,
  or `jobs`. Preserve meaningful execution, evaluation, override,
  enumeration, and cascade order; do not sort arbitrary arrays or
  procedural steps mechanically. Explicit project configuration and
  conventions take precedence.

- In object literals, place shorthand properties before properties with
  explicit values. Within each group, sort properties alphabetically by
  key name. Preserve the existing order when reordering changes behavior,
  including evaluation order, property overrides through spreads, or
  meaningful key enumeration order. Explicit project configuration takes
  precedence.

- Follow role-based naming: camelCase for ordinary bindings/callables,
  PascalCase for types/components, and uppercase for stable named shared
  constants. Preserve snake_case or other external field spellings when
  they are part of a contract. Do not treat a linter's list of allowed
  cases as permission to mix them arbitrarily for equivalent roles.

- Use descriptive lowercase kebab-case paths by default, preserving
  required discovery names and public paths. Let parent folders supply
  domain context; avoid repeating it in every leaf name without a reason.

- Sort independent destructured keys with the configured rule. Preserve
  rest placement, getter access, and default-initializer dependencies;
  mechanical sorting must not change evaluation behavior.

## Imports and exports

- Use ES modules for authored modules in an ESM repository. Prefer named
  imports to namespace imports and avoid CommonJS there. Preserve
  required interop, generated code, and third-party contracts.

- Keep imports at the top in the configured groups and order; sort
  named imports and exports through the repository's sorter. Preserve
  intentional side-effect order and module initialization behavior.

- Keep named exports grouped after local definitions. Re-export entry
  points may list their public exports directly. Do not add a default
  export merely because a module has one value; preserve default exports
  required by configuration, routing, framework, or existing API use.

- Imports must resolve to real modules and exported symbols. Respect the
  effective path-alias and extension policy. Explicit source extensions
  in one toolchain are not permission to emit unresolvable imports in
  another runtime or published package.

- Keep imports used only for types type-only. When values and types come
  from the same module, prefer an inline `type` modifier in the named
  import rather than a redundant second import, subject to local rules.

- A library may prohibit side-effect-only imports while an application
  needs global styles or initialization. Keep such imports deliberate,
  preserve their order, and follow the actual repository rule; do not
  invent a universal ban on stylesheet imports.

## TypeScript contracts

- Use strict type checking for new typed code. Preserve checks for
  implicit `any`, indexed-access uncertainty, exact optional properties,
  return paths, unused locals/parameters, unreachable code and labels,
  plus override/index-signature checks where applicable.

- Prefer concrete or inferred types and `unknown` with narrowing at
  untrusted boundaries over explicit `any`. Do not replace a type error
  with an unchecked assertion or a non-null assertion as a style fix.

- Avoid `@ts-ignore` and `@ts-nocheck` as shortcuts. An intentional
  negative type test or unavoidable external typing gap needs the
  narrowest documented directive permitted by the effective rules.

- Remove genuinely unused bindings and properties after checking public,
  serialized and dynamically accessed contracts. Do not add dummy reads
  or rename fields solely to silence a diagnostic.

- Match module resolution, output, target, libraries and global names to
  the actual consumer. Browser/bundler and Node/package configurations
  are different contracts; do not copy aliases, emit settings or runtime
  globals from an unrelated template.

## React and JSX

- Destructure props and relevant inputs rather than scattering repeated
  property access throughout a component. Keep state ownership and
  component boundaries explicit.

- Sort independent JSX props with the configured rule. Preserve spreads,
  overriding order and expression evaluation. Use self-closing syntax
  when there are no children, and omit unnecessary braces around literal
  strings when the JSX rule calls for that form.

- Follow Hook call and dependency contracts. Do not hide dependency
  warnings to preserve an intended-looking effect order; validate the
  closure and lifecycle behavior instead. Component body order remains
  a readability convention, not proof of correctness.

- Use the project's class-composition utility and canonical utility
  spellings when those tools are adopted. Resolve classes against the
  actual design tokens and stylesheet; no particular CSS path, utility
  framework or component directory is a portable requirement.

## CSS and SCSS

- Follow the configured declaration groups and nested-rule order rather
  than alphabetizing all CSS. Keep variables/custom properties before
  their dependent declarations. Preserve deliberate fallback, prefix,
  shorthand/longhand and cascade ordering when applying a sorter.

- Prefer low-specificity class selectors to IDs, qualifying type
  selectors, unnecessary universal selectors and deep nesting. Enforce
  actual nesting/combinator limits from the selected config. Apply BEM
  only where the class contract uses it; CSS Modules and other systems
  must not inherit an unrelated selector regex.

- Prefer logical properties and units for direction-aware layout and
  rem for scalable lengths. Keep fixed-pixel or physical-coordinate
  requirements explicit. Do not substitute units mechanically where it
  changes the layout contract.

- Prefer design tokens or explicit color values to named colors. Use
  numeric font weights, percentage keyframe selectors and lowercase
  keywords where syntax permits. Validate color gamut and feature
  support for the intended targets; use explicit URL schemes.

- Avoid `!important`; resolve ownership and cascade conflicts first.
  An unavoidable override needs a bounded reason. Do not emit debug
  at-rules, unknown properties/animations, ignored declarations or
  duplicated variables as normal source style.

- Preserve configured blank lines around declaration groups and
  at-rules. Group selectors only when their declarations and cascade
  responsibilities are actually equivalent.

- For SCSS, avoid redundant nesting, aliases and `@at-root`; keep quoted
  map keys, flat property declarations and standalone `//` comments.
  Preserve license comments. Follow the module's variable ownership and
  breakpoint-variable convention; do not assign into another namespace.

- Defensive CSS checks should cover hover capabilities, wrapping,
  background repeat, fallbacks, scrolling and scrollbar stability where
  relevant. Animation-property warnings identify a risk to measure, not
  proof that an implementation is fast or slow.

## Enforcement and boundaries

- Inspect effective configuration, overrides, inherited presets and
  affected file globs before claiming that a rule is enforced. Preserve
  warning/error distinctions and justified exceptions; disabling a rule
  in one repository is not a general authoring convention.

- Keep reusable configuration small and language-appropriate. Identity
  wrappers around config objects do not supply hidden defaults. Ensure
  editor fixes, hooks and CI use compatible tools and the same rules.

- Markdown follows its active Remark presets and formatter. Maintain
  coherent headings, fenced code, lists and tables; adapt documents to
  those checks rather than accumulating blanket rule suppressions.

- Editor themes, keybindings, local paths, workspace-trust settings and
  automatic Git actions are personal setup, not code-style requirements
  or authorization to change the adopting environment.
