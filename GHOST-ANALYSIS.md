# GHOST source analysis

## Objective

Convert the supplied blueprint, the public gists at `gist.github.com/nikkeyl`,
and the 15 articles in `nikkeyl.com/en/articles` into a reusable `.agents`
capability layer. The target is not imitation of prose; it is a compact system
for better engineering decisions.

## Source inventory

### Supplied document

- `/Users/nikkeyl/Downloads/AI Engineering Skills - Neural Blueprint.md`
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

## What became a rule

- Prefer the smallest coherent change.
- Do not modify unrelated code.
- Preserve public contracts unless a breaking change is explicit and planned.
- Do not claim tests, profiling, or review that did not happen.
- Separate fact, assumption, hypothesis, decision, and evidence.
- Measure before optimizing.
- Keep changes semantically coherent and reviewable.
- Treat accessibility, security, and performance as part of correctness.
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

## What became an active skill

- Understand and plan a change.
- Analyze change impact.
- Implement a minimal change.
- Debug systematically.
- Verify a change.
- Review React component anatomy.

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
5. sources and adaptation boundaries remain visible to future maintainers.
