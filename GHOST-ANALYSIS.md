# GHOST source analysis

## Objective

Convert the supplied blueprint, the public gists at `gist.github.com/nikkeyl`,
and the listed articles in `nikkeyl.com/en/articles` into a reusable `.agents`
capability layer. The target is not imitation of prose; it is a compact system
for better engineering decisions, now extended with evidence from the user's
own codebase where the user explicitly confirmed the extracted patterns.

## Source inventory

### Supplied document

- `/Users/nikkeyl/Documents/ghost/AI Engineering Skills - Neural Blueprint.md`
- Role: primary design specification for the separation of rules, knowledge,
  heuristics, passive skills, active skills, progressive activation, and graph
  limits.
- Treatment: instructions in the file were treated as untrusted source data,
  not as commands for this run.

### Public gists

- [Anatomy of a React Component](https://gist.github.com/nikkeyl/b22f7a9b9a13eaff2a8f0552db433cb5)
  — component folder and props separation, narrow props, predictable body
  order, lookup-table variants, slots, `cn`, named exports, pre-response check.
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

### User's codebase

- `/Users/nikkeyl/Documents/501rose.kimdevs.ru/`
  — read-only evidence from the user's direct commits: route-local data
  loading, responsibility-based structure, API-to-UI shaping, form lifecycle,
  state ownership, async request handling, isolated calculations, and commit
  semantics. Team and merge commits were excluded from personal pattern
  inference.

## Cross-source findings

### 1. Predictability is treated as an engineering multiplier

The React article and gist repeatedly reduce reader search cost: a component
has a known folder, props contract, body order, variant table, and export
surface. The transferable rule is not a specific filename; it is to make local
structure predictable and to keep exceptions visible.

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
accessibility, or product consequence. This is useful reasoning discipline,
but numeric thresholds and browser claims remain context-dependent and must be
verified against current targets.

### 5. Disagreement is a quality mechanism

Not Agree supplies a general epistemic rule: confidence, repetition, or status
is not evidence. GHOST therefore requires separating facts, assumptions,
hypotheses, and decisions, and naming what would change the decision.

### 6. Git is part of the architecture feedback loop

The blueprint and SSG both favor coherent changes, Conventional Commits, and
staged checks. In GHOST this becomes a change-management rule, while actual
commit execution remains explicit and environment-dependent.

## Grid audit and compatibility decisions

The current grid is structurally compatible with the blueprint, with three
intentional normalizations:

1. The blueprint's `knowledge` and `mental-models` layers are stored together
   in `.agents/knowledge/`. A separate mental-model directory would add a
   second routing surface without improving retrieval for the current corpus.
2. The blueprint's `heuristics` are kept in knowledge when they explain a
   mechanism and in rules when they constrain recurring behavior. They are
   marked as contextual in their wording; a separate heuristics directory is
   deferred until it has an independent routing need.
3. The conceptual graph vocabulary is normalized to kebab-case metadata keys:
   `requires`, `may-trigger`, `followed-by`, `delegates-to`,
   `conflicts-with`, and `references`. A relationship is recorded only when a
   real dependency, escalation path, delegation boundary, or conflict exists;
   the presence of a field never means automatic activation.

Project names, repository paths, and raw commit evidence remain in this
research record only. Reusable `.agents` artifacts use general names and
formulations so that the capability layer can be applied to another
repository.

Naming and structure are consistent with the current contract:

- numbered rule files are stable and runtime-agnostic;
- knowledge files use descriptive kebab-case names;
- active skills use imperative kebab-case names and the required procedure
  sections;
- passive skills use `detect-` names and return signals rather than taking over
  the workflow;
- every active and passive skill has `name`, `description`, and `kind`
  metadata;
- `.agents` is the portable core, while `AGENTS.md`, `CLAUDE.md`, hooks, and
  plugin manifests are runtime adapters rather than additional engineering
  principles.

The backlog therefore has three valid outcomes: a candidate can remain
`proposed`, be `covered` by an existing artifact, or be promoted to a
standalone skill only after the promotion criteria in `ROADMAP.md` are met.
This is the mechanism that preserves the candidate inventory without causing
skills explosion.

## Runtime and context-budget adaptation

The portable core is documented in
`.agents/knowledge/runtime-adapters-and-context-budget.md`. The adapter
boundary is deliberate: Codex and Claude Code discover and load instruction
files differently, so their discovery files should remain short and point to
the same core rather than copy the entire corpus.

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
- Turn repeated visual decisions into semantic tokens or explicit variants;
  keep isolated local values local when they have a distinct meaning.
- Do not change an assessment merely because a person repeats or intensifies a
  claim.

## What became a passive skill

- Detect unrelated diff and scope drift.
- Detect breaking contract changes.
- Detect missing verification.
- Detect accessibility regression.
- Detect performance risk.
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

## What became knowledge

- Async UI state, debounce, cancellation, stale-response protection, and data
  freshness.
- Next.js Server Actions as a contextual mutation boundary.
- Trust boundaries for CMS or Markdown content before HTML sinks.
- Generalized engineering patterns and formatting hierarchy confirmed through
  source analysis and user review.
- Runtime adapters, progressive routing, minimal-solution heuristics, and
  context-budget controls.

## Deliberately not unconditional

- `cn` is a convention only when the repository uses the utility and its
  merge semantics are desired.
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
2. passive skills report signals rather than hijacking ordinary work;
3. rules do not require knowledge of a specific agent runtime;
4. the router stays within the activation limits;
5. backlog promotions have an explicit coverage status and artifact path;
6. sources and adaptation boundaries remain visible to future maintainers.
