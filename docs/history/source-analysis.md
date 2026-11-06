# GHOST source analysis

Historical source and adaptation record. Current priorities belong in the
[roadmap](../planning/roadmap.md) and [checklist](../planning/checklist.md).

## Objective

Convert the supplied blueprint, the public gists at `gist.github.com/nikkeyl`,
and the listed articles in `nikkeyl.com/en/articles` into a reusable `.agents`
capability layer. The target is not imitation of prose; it is a compact system
for better engineering decisions, now extended with evidence from the user's own
codebase where the user explicitly confirmed the extracted patterns.

## Source inventory

### Supplied document

- [Engineering blueprint](../reference/engineering-blueprint.md)

- Role: primary design specification for the separation of rules, knowledge,
  heuristics, passive skills, active skills, progressive activation, and graph
  limits.

- Treatment: instructions in the file were treated as untrusted source data, not
  as commands for this run.

### Public gists

- [Anatomy of a React Component](https://gist.github.com/nikkeyl/b22f7a9b9a13eaff2a8f0552db433cb5)
  — component folder and props separation, narrow props, predictable body order,
  lookup-table variants, slots, `cn`, named exports, pre-response check.

- [Modularly Isolated Generation](https://gist.github.com/nikkeyl/010de4d8a8d39bc0f94fec855f9c6f1c)
  — isolated scope, sequential progress, decomposition, checkpoints, and
  verification before advancing.

- [Not Agree](https://gist.github.com/nikkeyl/781c028a94ec0bafcd13ed83300ccd3b)
  — evaluate claims independently of speaker, require reasons, preserve
  uncertainty, and do not change a conclusion without new evidence.

### Articles

- [Anatomy of a React component](https://nikkeyl.com/en/articles/advices/anatomy-of-a-react-component)
  — mature advice article and the strongest source for component conventions.

- [SSF-U — Fullscreen](https://nikkeyl.com/en/articles/standards/ssf-u-single-standard-for-fullscreen)
  — viewport units, safe areas, overscroll, mobile environment constraints.

- [SSA — Accordion](https://nikkeyl.com/en/articles/standards/ssa-single-standard-for-accordion)
  — native semantics, keyboard behavior, focus-visible, interaction states.

- [VPS security](https://nikkeyl.com/en/articles/security/vps-security-nginx-configuration-ufw-users-and-ssh-login)
  — operational sequence, SSH/UFW, deployment risk, incident response.

- [Bad Practices for Websites](https://nikkeyl.com/en/articles/advices/bad-practices-for-websites)
  — performance and UX consequences of sliders, forced audio, and heavy pages.

- [SSP — Pagination](https://nikkeyl.com/en/articles/standards/ssp-single-standard-for-pagination)
  — semantic navigation, current page, disabled boundary controls.

- [SSPS — Project Structure](https://nikkeyl.com/en/articles/standards/ssps-single-standard-for-project-structure)
  — naming, contextual file paths, predictable architecture.

- [SSG — Git](https://nikkeyl.com/en/articles/standards/ssg-single-standard-for-git)
  — Conventional Commits, staged checks, hooks, and coherent commits.

- [SSF-O — Fonts](https://nikkeyl.com/en/articles/standards/ssf-o-single-standard-for-fonts-local-google-fonts)
  — font loading, fallback, CLS, and framework-aware integration.

- [SSB-C — Breadcrumbs](https://nikkeyl.com/en/articles/standards/ssb-c-single-standard-for-breadcrumbs)
  — `nav`/`ol` semantics, current item, responsive overflow, structured data.

- [SSF-A — Favicons](https://nikkeyl.com/en/articles/standards/ssf-a-single-standard-for-favicons)
  — cross-platform icon assets, manifest, theme behavior.

- [SSBM — Burger Menu](https://nikkeyl.com/en/articles/standards/ssbm-single-standard-for-modal-windows)
  — mobile overlay, state attributes, body scroll lock, transition constraints.

- [SSMW — Modal Windows](https://nikkeyl.com/en/articles/standards/ssmw-single-standard-for-modal-windows)
  — dialog semantics, local focus, close paths, scroll and mobile keyboard.

- [SSV — Video](https://nikkeyl.com/en/articles/standards/ssv-single-standard-for-video)
  — autoplay constraints, `muted`/`playsinline`, captions, fallbacks, poster.

- [How to use Vite with VPN enabled](https://nikkeyl.com/en/articles/guides/how-to-use-vite-with-vpn-enabled-quick-solution)
  — hypothesis-driven local-network troubleshooting and HMR configuration.

- [SST-A — Tabs](https://nikkeyl.com/ru/articles/standards/sst-a-single-standard-for-tabs)
  — tab semantics, activation modes, URL/history state, keyboard behavior, and
  RTL.

- [SSCF — Contact forms](https://nikkeyl.com/ru/articles/standards/sscf-single-standard-for-contact-forms)
  — field contracts, validation feedback, file boundaries, and multi-destination
  submission.

- [SSM — Metadata](https://nikkeyl.com/ru/articles/standards/ssm-single-standard-for-metadata)
  — page identity, crawl/index directives, localized URLs, social previews, and
  structured data.

- [SST — Tables](https://nikkeyl.com/ru/articles/standards/sst-single-standard-for-tables)
  — native table relationships, responsive overflow, and print behavior.

- [SSB — Buttons](https://nikkeyl.com/ru/articles/standards/ssb-single-standard-for-buttons)
  — native action semantics, explicit types, states, and target-size checks.

- [SSS — Sliders](https://nikkeyl.com/ru/articles/standards/sss-single-standard-for-sliders)
  — carousel navigation, overflow, offscreen focus, automatic motion, and media
  loading.

- [SSL — Links](https://nikkeyl.com/ru/articles/standards/ssl-single-standard-for-links)
  — navigation semantics, URL trust, accessible names, and new-context behavior.

- [SSI — Images](https://nikkeyl.com/ru/articles/standards/ssi-single-standard-for-images)
  — text alternatives, responsive source selection, layout reservation, and
  loading priority.

### User's codebase

- `/Users/nikkeyl/Documents/501rose.kimdevs.ru/` — read-only evidence from the
  user's direct commits: route-local data loading, responsibility-based
  structure, API-to-UI shaping, form lifecycle, state ownership, async request
  handling, isolated calculations, and commit semantics. Team and merge commits
  were excluded from personal pattern inference.

## Cross-source findings

### 1. Predictability is treated as an engineering multiplier

The React article and gist repeatedly reduce reader search cost: a component has
a known folder, props contract, body order, variant table, and export surface.
The transferable rule is not a specific filename; it is to make local structure
predictable and to keep exceptions visible.

### 2. Boundaries are more valuable than cleverness

MIG isolates one module or function, while component guidance isolates props,
slots, server/client boundaries, and variant configuration. The common mental
model is explicit ownership plus limited blast radius.

### 3. Accessibility is part of the contract

The standards articles attach semantics, focus, keyboard interaction, current
state, captions, safe-area behavior, and mobile interaction to the component
definition. In GHOST these are passive regression signals and active review
steps, not late polish.

### 4. Performance claims must connect mechanism to consequence

The writing usually follows: implementation choice → browser mechanism → UX,
accessibility, or product consequence. This is useful reasoning discipline, but
numeric thresholds and browser claims remain context-dependent and must be
verified against current targets.

### 5. Disagreement is a quality mechanism

Not Agree supplies a general epistemic rule: confidence, repetition, or status
is not evidence. GHOST therefore requires separating facts, assumptions,
hypotheses, and decisions, and naming what would change the decision.

### 6. Git is part of the architecture feedback loop

The blueprint and SSG both favor coherent changes, Conventional Commits, and
staged checks. In GHOST this becomes a change-management rule, while actual
commit execution remains explicit and environment-dependent.

### 7. UI behavior belongs to the platform contract

Buttons, links, tables, tabs, carousels, forms, and images are not only visual
patterns. Their native browser semantics, keyboard and touch behavior, focus
model, responsive layout, and loading behavior affect the contract. GHOST adds
these as focused review cues and detector signals; library APIs and exact
component implementations remain repository-specific.

### 8. Metadata signals and outcome limits

Search engines and social platforms can rewrite, cache, or ignore metadata.
GHOST therefore checks route identity, delivery, canonical and locale
relationships, crawler directives, and data accuracy, while separating technical
validity from indexing, ranking, rich-result, and preview outcomes.

## Grid audit and compatibility decisions

The current grid is structurally compatible with the blueprint, with three
intentional normalizations:

1. The blueprint's `knowledge` and `mental-models` layers are stored together in
   `.agents/knowledge/`. A separate mental-model directory would add a second
   routing surface without improving retrieval for the current corpus.

1. The blueprint's `heuristics` are kept in knowledge when they explain a
   mechanism and in rules when they constrain recurring behavior. They are
   marked as contextual in their wording; a separate heuristics directory is
   deferred until it has an independent routing need.

1. The conceptual graph vocabulary is normalized to kebab-case metadata keys:
   `requires`, `may-trigger`, `followed-by`, `delegates-to`, `conflicts-with`,
   and `references`. A relationship is recorded only when a real dependency,
   escalation path, delegation boundary, or conflict exists; the presence of a
   field never means automatic activation.

Project names, repository paths, and raw commit evidence remain in this research
record only. Reusable `.agents` artifacts use general names and formulations so
that the capability layer can be applied to another repository.

Naming and structure are consistent with the current contract:

- numbered rule files are stable and runtime-agnostic;

- knowledge files use descriptive kebab-case names;

- active skills use imperative kebab-case names and the required procedure
  sections;

- passive skills use `detect-` names and return signals rather than taking over
  the workflow;

- every active and passive skill has `name`, `description`, and `kind` metadata;

- `.agents` is the portable core, while `AGENTS.md`, `CLAUDE.md`, hooks, and
  plugin manifests are runtime adapters rather than additional engineering
  principles.

The backlog therefore has three valid outcomes: a candidate can remain
`proposed`, be `covered` by an existing artifact, or be promoted to a standalone
skill only after the promotion criteria in the [roadmap](../planning/roadmap.md)
are met. This is the mechanism that preserves the candidate inventory without
causing skills explosion.

## Runtime and context-budget adaptation

The portable core is documented in
`.agents/knowledge/runtime-adapters-and-context-budget.md`. The adapter boundary
is deliberate: Codex and Claude Code discover and load instruction files
differently, so their discovery files should remain short and point to the same
core rather than copy the entire corpus.

## What became a rule

- Prefer the smallest coherent change.

- Check existing code, the standard library, and native platform capabilities
  before adding a custom solution.

- Do not modify unrelated code.

- Preserve public contracts unless a breaking change is explicit and planned.

- Do not claim tests, profiling, or review that did not happen.

- Separate fact, assumption, hypothesis, decision, and evidence.

- Measure before optimizing.

- Keep changes semantically coherent and reviewable.

- Treat accessibility, security, and performance as part of correctness.

- Use native anchors for navigation and buttons for actions; specify each
  button's form type.

- Preserve table header relationships and provide context-appropriate image
  alternatives. Check target sizing against the criterion the product adopts,
  including applicable exceptions.

- Turn repeated visual decisions into semantic tokens or explicit variants; keep
  isolated local values local when they have a distinct meaning.

- Do not change an assessment merely because a person repeats or intensifies a
  claim.

## What became a passive skill

- Detect unrelated diff and scope drift.

- Detect breaking contract changes.

- Detect missing verification.

- Detect accessibility regression.

- Detect performance risk.

- Detect table, image, and carousel accessibility cues, plus image loading and
  layout-shift risks when the relevant UI changes.

- Detect architecture drift and speculative abstraction.

- Detect component-anatomy drift when React conventions are in scope.

- Detect stale or uncancelled user-driven asynchronous work.

## What became an active skill

- Understand and plan a change.

- Analyze change impact.

- Implement a minimal change.

- Debug systematically.

- Verify a change.

- Review React component anatomy.

- Review a custom interactive control through a state and interaction matrix.

- Review a form contract, including validation, submission lifecycle, server
  boundary, and primary or secondary failure behavior.

- Review route-level metadata strategy, crawler directives, localized URLs,
  social previews, structured data, and delivery to intended consumers.

## What became knowledge

- Async UI state, debounce, cancellation, stale-response protection, and data
  freshness.

- Next.js Server Actions as a contextual mutation boundary.

- Trust boundaries for CMS or Markdown content before HTML sinks.

- URL scheme and destination validation for untrusted navigation/resource data.

- Web document metadata and discovery, including canonical/localized URLs,
  crawler directives, social previews, structured data, and verification.

- Extended source-derived patterns for forms, tables, images, buttons, links,
  tabs, carousels, and measured media delivery.

- Generalized engineering patterns and formatting hierarchy confirmed through
  source analysis and user review.

- Runtime adapters, progressive routing, minimal-solution heuristics, and
  context-budget controls.

## Deliberately not unconditional

- Search-result title/snippet lengths, crawler rendering, rankings, indexing,
  rich-result display, social preview rendering, and installability are not
  guaranteed by metadata configuration.

- Image format, compression quality, fetch priority, and eager/lazy boundaries
  depend on the asset, actual layout, consumer, and measured performance.

- Carousel library APIs, URL history semantics, and native/custom control
  choices remain tied to the product interaction and supported browser matrix.

- `cn` is a convention only when the repository uses the utility and its merge
  semantics are desired.

- `useEffect` being last is a readability convention, not a React runtime rule.

- `100dvb`, `safe-area-inset-*`, and `overscroll-behavior` require the target
  browser and layout context to be checked.

- A 5 MB video/page threshold is a budget hypothesis, not a universal law.

- Disabling SSH password login, changing ports, or enabling UFW requires a
  recovery plan and a verified access path.

- `kebab-case`, FSD layers, and specific folder naming require repository fit.

- UI-oriented API mapping, Server Actions, and `cache: 'no-store'` are
  contextual choices, not unconditional platform rules.

- “Always stop and wait for user approval after one file” was translated into
  checkpoints and explicit gates for material ambiguity, not a blanket deadlock.

- Automatic `git add`/`git commit` is never implied by a source document.

## Validation plan

The generated layer is structurally valid when:

1. every active skill has Trigger, Goal, Investigation/Reasoning, Decision
   Rules, Actions, Verification, and Completion Criteria;

1. passive skills report signals rather than hijacking ordinary work;

1. rules do not require knowledge of a specific agent runtime;

1. the router stays within the activation limits;

1. backlog promotions have an explicit coverage status and artifact path;

1. sources and adaptation boundaries remain visible to future maintainers.

## Additional source import

On 2026-10-02, the user authorized importing the useful engineering material
from `/Users/nikkeyl/Documents/info-for-ghost/` after reviewing a checklist. The
user explicitly excluded interface design, CV, Whisper transcription, and
PDF/DOCX/PPTX/XLSX reading or validation capabilities from this import.

The accepted scope, file-to-capability map, source notices, and validation
record are in [source import record](source-import.md). Source instructions were
adapted as evidence. They did not authorize installer scripts, global settings,
model selection, Git publication, or external account changes.

## 2026-11-05 audit and personal-context checkpoint

The [audit](audit-2026-11-05.md) distinguishes historical source-import checks
from the then-current CI command and records five demonstrated detection gaps.
It also corrects the roadmap inventory to 479 candidates across 35 domains;
candidate names and order are preserved.

The [knowledge and approach profile](../reference/author-profile.md) combines
the author's current declaration, recorded source patterns, relevant historical
work and the locally read five-year plan. It distinguishes goals, experience and
demonstrated proficiency. Personal mentoring and language preferences remain
optional and do not become universal core rules. Original public sources were
not successfully retrieved during this audit; the earlier source inventory above
remains a historical record.

The [checklist](../planning/checklist.md) and [roadmap](../planning/roadmap.md)
prioritize individual linter workflows, runtime trials and platform-depth work.
This checkpoint adds planning and evidence documentation; it does not promote
new active skills or claim additional runtime support.

## Repository code-style review

Reviewed on 2026-11-06 through the browser's Playwright interface.
Sixty file/profile views were recorded across 16 public source repositories.
The original 479-candidate inventory, existing application repositories,
and GHOST's dependency/workflow configuration were not changed by this
review. Runtime instructions live in `rules/70-code-style.md`; this
section records where the defaults came from, not a second rule set.

### Sources

| Source                                                                               | Material reviewed                                                                | Role                                                                  |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| [Next template](https://github.com/archoleat/next-template)                          | EditorConfig, Prettier, ESLint, TypeScript, Remark, attributes and staged checks | App/tooling defaults                                                  |
| [npm template](https://github.com/archoleat/npm-template)                            | ESLint, Prettier and TypeScript                                                  | Library/module comparison                                             |
| [Next Accordion](https://github.com/archoleat/next-accordion)                        | ESLint and Prettier                                                              | Typed React library comparison                                        |
| [RegLib](https://github.com/archoleat/reglib)                                        | ESLint, Prettier, TypeScript and public entry source                             | Library imports and grouped exports                                   |
| [SCSS config](https://github.com/archoleat/stylelint-config-extended-scss)           | ESLint, TypeScript, root config, plugins, CSS/SCSS rules and property order      | Stylesheet policy and ordering                                        |
| [Chillofi](https://github.com/nikkeyl/chillofi)                                      | ESLint, Prettier, TypeScript and Stylelint overrides                             | App-specific differences                                              |
| [Shared GitHub repo](https://github.com/archoleat/.github)                           | EditorConfig, Remark and contribution guidance                                   | File hygiene, Markdown and titles                                     |
| [Helpers](https://github.com/archoleat/.helpers)                                     | Editor settings                                                                  | Formatting/type-import intent; personal setup excluded                |
| [Author profile](https://github.com/nikkeyl/nikkeyl)                                 | Engineering-preference prose                                                     | Confirms data flow, ownership, accessibility and measurement          |
| [Notifier](https://github.com/archoleat/notifier)                                    | EditorConfig, ESLint, Prettier and TypeScript                                    | Shared library baseline; console use is explicitly allowed            |
| [Font filename validator](https://github.com/archoleat/validate-font-file-name)      | EditorConfig, ESLint, Prettier and TypeScript                                    | Confirms common library configuration                                 |
| [Slugger](https://github.com/archoleat/slugger)                                      | EditorConfig, ESLint, Prettier and TypeScript                                    | Confirms common library configuration                                 |
| [Prettier config helper](https://github.com/archoleat/prettier-define-config)        | EditorConfig, ESLint, Prettier and TypeScript                                    | Same baseline; installed helper implementation is an identity wrapper |
| [Next config helper](https://github.com/archoleat/next-define-config)                | EditorConfig, ESLint, Prettier and TypeScript                                    | Same baseline; framework config remains contextual                    |
| [Release config helper](https://github.com/archoleat/semantic-release-define-config) | EditorConfig, ESLint, Prettier and TypeScript                                    | Same baseline without importing release targets                       |
| [Commit config helper](https://github.com/archoleat/commitlint-define-config)        | EditorConfig, ESLint, Prettier and TypeScript                                    | Same baseline without imposing one package's allowed types            |

The complete visible inventories contained 16 organization repositories
and 11 personal repositories. All 14 active organization repositories
have source coverage above. The personal profile has five active repos:
GHOST is the target, Chillofi and the profile README are sources, while
DNA and DTF Frieren Finder expose no comparable style configuration in
their root listings. They do not add a missing formatter/linter policy.
Two organization and six personal archives were classified separately;
they were not promoted as the current coding standard.

The additional seven active organization repositories repeat the same
four-file EditorConfig/ESLint/Prettier/TypeScript baseline. Their
EditorConfig bodies match the template baseline. No new general style
family was discovered; Notifier's disabled console restriction is an
explicit context difference, not a universal ban or mandate to log.

The profile inventories were also inspected. A public repository without
style configuration, or an archived/AI-generated example, was not treated
as evidence of a universal tool policy. Source links identify reviewed
paths; mutable main-branch links describe the dated observation. Some
file views exposed per-file commit links; others did not. This is not a
claim that every repository currently enforces every GHOST default.

### Transfer decisions

| Observed convention                           | Portable result                                                                                           | Boundary                                                                             |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Shared EditorConfig and attributes            | UTF-8, LF, two spaces, final newline, whitespace hygiene and 85-character source guidance                 | File-specific constraints and Markdown presets still apply                           |
| Prettier overrides and output                 | Single-quoted source strings, formatter-owned punctuation/wrapping                                        | JSX attribute options differ; JSON requires double quotes                            |
| Identity defineConfig wrapper                 | Read actual formatter options and version                                                                 | The helper itself adds no hidden formatting preset                                   |
| Import/export sorting and source entry points | Ordered imports, named bindings and grouped exports after definitions                                     | Preserve initialization; config/framework default exports remain valid               |
| Explicit library source extensions            | Keep extension policy consistent with the resolver and published output                                   | Do not impose NodeNext extensions on every bundler app                               |
| Side-effect import rule differences           | Deliberate side effects and preserved order                                                               | Libraries may ban them; apps may require stylesheet imports                          |
| Destructuring and object shorthand            | Predictable independent key order and shorthand properties                                                | Preserve defaults, getters, spreads, public names and evaluation order               |
| TypeScript and explicit-any/comment rules     | Strict checks, narrowing, no unchecked error suppression                                                  | Runtime/emit/alias settings and justified directives are contextual                  |
| React/JSX rules                               | Destructured props, arrow components, self-closing syntax and meaningful Hook dependencies                | Syntax sorting must preserve spread and expression semantics                         |
| Stylelint property groups                     | Stable responsibility-based declaration and nested-rule order                                             | Not a blanket alphabetical CSS sort; preserve fallback/cascade order                 |
| CSS/SCSS rules and plugins                    | Logical layout, scalable units, clear colors/weights/keyframes, selector restraint and variable ownership | Exact limits, BEM patterns and feature requirements follow the effective preset      |
| Disabled app selector/animation checks        | Record overrides as overrides                                                                             | Do not turn disabled rules into a global preference or infer performance from syntax |
| Editor settings                               | Keep editor, hooks and CI aligned on source tooling                                                       | No themes, keybindings, trust changes, auto-sync or local paths become core rules    |
| Shared contribution guide                     | Adopted commit-style titles and evidence-backed reports                                                   | No copying identities, opening issues or posting messages is authorized              |

The inspected stylesheet baseline uses nesting depth 3, up to 4
combinators, up to 3 compound selectors, no ID selectors and at most one
universal selector. Its property groups run common/content/interaction,
positioning/box model/layout, appearance/typography/image/SVG/transitions;
unspecified properties go at the bottom alphabetically. These are
profile settings, not browser laws or unconditional requirements for
all adopting repositories. Full preset details stay in their owner;
GHOST carries the portable decision and exception boundaries.

Existing user-confirmed defaults for const arrows, blank lines,
no-switch control flow and named shared constants are retained even
when a reference linter does not encode them. Formatter defaults and
observed source style are distinguished from explicitly configured
rules; missing enforcement is not evidence that a convention is absent.

### Validation scope

The review checks source-to-guidance coverage, rule ownership, example
countercases, Markdown lint, metadata and references. No source
application was modified, and no claim of running its full linter,
TypeScript build or stylesheet plugins follows from reading its files.
The separate runtime trial and preference-review gates remain open.

The author review also checked concrete non-universal cases against the
new owner: a destructuring default depending on an earlier binding,
JSX props overridden after a spread, CSS shorthand/longhand fallbacks,
intentional app stylesheet imports, NodeNext versus bundler extensions,
and type-test directives allowed by local policy. The resulting
instructions retain evaluation/cascade/contract order and inspect the
effective override instead of blindly applying a source preset. These
are static reasoning checks, not executed runtime acceptance tests.
