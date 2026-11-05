# Nikkeyl: knowledge, approaches, and learning priorities

Reviewed: 2026-11-05. This is a source-backed working profile, not a competency
certification or an always-loaded agent instruction. Personalization is
optional; the reusable GHOST core should remain useful to other engineers.

## Evidence boundaries

- **Declared**: the author's instructions in the 2026-11-05 audit request.

- **Recorded**: material already preserved in GHOST at commit `6ad5f08`,
  especially the blueprint, source analysis, rules, and source-derived
  knowledge. Original articles and gists were not successfully retrieved during
  this audit; their descriptions below rely on the checked-in analysis, not a
  fresh article review.

- **Historical**: earlier project/audit records. These establish involvement and
  decisions, not independent mastery, current deployment state, or personal
  authorship of every AI-assisted implementation.

- **Plan**: the locally read five-year plan, November 2026–October 2031. Its
  future milestones are intentions, not completed achievements or guaranteed
  promotions.

- **Unknown**: requires an explanation, unfamiliar example, experiment, or
  measured project outcome. Missing evidence is not proof of missing ability.

## Direction and constraints

The author identifies as a Middle Frontend Developer working primarily with
TypeScript and Next.js. The long-term goal is Principal Frontend Engineer while
remaining in frontend. The declared main obstacle is technical depth.

Mentoring should be intellectually demanding, roughly 8/10: require reasons,
challenge weak assumptions, and distinguish agreement from compliance. Give a
quick working answer when needed; otherwise explain the platform mechanism,
alternatives, scaling limits, and consequences for maintainers, team, product,
and business. Keep answers concise and deepen them when the problem warrants it.
AI should strengthen understanding; generated code does not establish learning.

The plan allocates **5 hours per week to frontend study**: Tuesday 2 hours,
Thursday 1 hour, Saturday 2 hours. This is a planned budget, not tracked
attendance. Advance by demonstrated understanding; move dates rather than
increasing load.

## Knowledge map

| Area                                | Available evidence                                                                             | What remains to establish                                                                                   | GHOST consequence                                                          |
| ----------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| TypeScript / Next.js                | Declared primary stack; component, data, and server-boundary guidance                          | Type-system depth, runtime validation, rendering and cache reasoning on unfamiliar cases                    | Platform explanations before framework recipes                             |
| JS values and identity              | Explicit first priority in the current study plan                                              | Predict aliasing, mutation, equality, shallow-copy and state-update behavior without hints                  | First learning experiments; do not mark complete from stack usage          |
| Scope, closures, prototypes, `this` | Planned foundation topics                                                                      | Explain lexical capture, stale closures, call-site behavior and property lookup                             | Short experiments tied to real bugs                                        |
| Async runtime                       | Async-race knowledge and cancellation guidance; planned event-loop study                       | Predict tasks/microtasks and failure propagation; distinguish concurrency from parallelism                  | Bridge runtime behavior to UI state                                        |
| Browser / rendering                 | Recorded standards for semantic controls, layout, media and focus                              | Explain parsing, event propagation, layout, paint, compositing and scheduling experimentally                | Browser model and DevTools evidence                                        |
| HTTP / caching                      | Recorded route-local loading and freshness rules                                               | Trace a request and identify browser/CDN/framework cache ownership and invalidation                         | Request trace before cache policy changes                                  |
| Component architecture              | Recorded React anatomy, narrow contracts, slots, typed variants and ownership                  | Show where those conventions lose value or need exceptions                                                  | Preserve local fit; avoid universal structure mandates                     |
| Forms / state / failures            | Recorded validation, input preservation on failure, cancellation, primary vs secondary effects | Retry, stale-response, duplicate-submit and partial-failure behavior under real conditions                  | Existing form and async workflows are trial candidates                     |
| Accessibility                       | Recorded native semantics, keyboard/focus, reduced motion, tables, media and controls          | Browser and assistive-technology verification of complete journeys                                          | Existing cues do not establish a full accessibility audit capability       |
| Performance                         | Recorded mechanism-to-UX reasoning and scoped loading                                          | Baseline/after traces, bottleneck attribution and representative user impact                                | Profile before optimizing; no invented savings                             |
| Security / operations               | Historical dependency/CI work and AI-assisted OAuth/MCP integration                            | Independently explain threat boundaries and verify deployed behavior                                        | Learn frontend trust boundaries without redirecting career into full-stack |
| Libraries / packaging               | Historical npm audit of public packages                                                        | Published consumer behavior, exports, ESM/CJS, client boundaries, peer compatibility                        | Add an artifact-consumer checklist before another standalone skill         |
| Git / delivery                      | Recorded coherent commits, scoped changes, explicit production constraints                     | Release/rollback evidence on a particular change                                                            | Separate local check, commit, push, and deployed acceptance                |
| Staff / Principal judgment          | Explicit career goal and blueprint's systemic decision inventory                               | Demonstrated cross-team adoption, measured outcomes, maintenance cost, reversibility and technical strategy | Start decision analysis now; titles are not implied by documentation       |

## Recurring approaches worth preserving

1. **Predictability reduces reading cost.** Component structure and naming
   should help a maintainer locate responsibility. A particular filename is a
   convention, not a platform requirement.

1. **Boundaries before cleverness.** Modularly Isolated Generation, small diffs,
   ownership, route-local dependencies and minimal client boundaries recur
   across the checked-in sources. Isolation should still follow coherent
   outcomes.

1. **Reasons before agreement.** The Not Agree source and current instructions
   require evidence, counterexamples, uncertainty and willingness to revise a
   claim.

1. **Native platform before custom behavior.** Semantics, forms, focus and
   browser behavior belong to correctness. Custom behavior needs a concrete
   requirement.

1. **Proportionate proof.** Earlier requests rejected unnecessary test/DB setup
   in specific projects. This supports selecting meaningful checks by risk; it
   does not support a general rule against tests or integration environments.

1. **Protect the stated operational boundary.** Earlier work explicitly
   preserved production ports while fixing local configuration. Preserve each
   task's actual invariants; do not turn particular port values into global
   policy.

1. **Concise technical documentation.** Earlier README work favored decisions,
   commands and configuration and removed redundant file inventories.

Preference requires context: the current rules banning `switch`, requiring
certain constant naming, or resetting every successful form are not universal
engineering truths. A library, search form, autosave flow or team convention may
justify a different choice. Evaluate the invariant and consumer before enforcing
a style.

## Recent experience: useful lessons, limited claims

- Repository maintenance records through 2026-11-04 show work on README,
  Actions, dependency findings, metadata and licenses. They show attention to
  scope and delivery; they do not quantify reliability or business impact.

- The 2026-10-14 npm audit recorded ESM behavior, client/SSR boundaries,
  peer-range conflicts and README/regex mismatches as follow-ups. These are
  historical leads, not a fresh assertion that those packages remain broken
  today.

- The OAuth/MCP work records the choice to extend an existing service and
  preserve existing authentication rather than maintain parallel
  implementations. Its live third-party authentication acceptance remained
  unverified in the supplied record. This illustrates migration and evidence
  boundaries, not independent backend expertise.

## Learning loop and progression

For one concept: **predict → explain → run → compare → apply → explain again**.
Record the initial prediction before AI feedback. Test transfer with a new
example; reciting the explanation of the example just shown is insufficient.

Start with values/references/identity/mutation/scope, then
closures/`this`/prototypes and async execution. Follow with DOM/events,
HTTP/cache/CORS, rendering/performance, then explain React and Next.js through
those mechanisms. Infrastructure breadth is not the immediate priority.
TypeScript runtime boundaries can be studied alongside these topics when a
working task exposes them.

For career evidence, capture a problem, constraints, alternatives including
doing nothing, decision, baseline, result, adoption, maintenance cost and
follow-up. Senior responsibility, Staff scope and Principal strategy require
real effects; the five-year calendar does not establish any of those levels.

## Personal context: keep optional

The author studies English and Japanese and requests natural English and
Japanese versions of each question. This is a conversational preference, not a
requirement for shared repository code, commits or team documentation. Interests
include philosophy, evidence-based psychology, calisthenics, basketball, travel
and Japan. The long-term cultural goal is deep understanding and eventually
teaching or guiding others; avoid romanticizing Japan or treating planned
language levels as current proficiency. These interests need no new engineering
skill by themselves.

## Source ledger and limitations

- Current author instructions: 2026-11-05, in the requesting conversation.

- Checked-in primary records: [blueprint](engineering-blueprint.md),
  [source analysis](../history/source-analysis.md), and
  [import record](../history/source-import.md). The analysis catalogs 3 gists,
  23 articles, and a historical codebase review; those are existing source
  records, not 27 freshly reviewed sources.

- Five-year plan: `pyatiletka.html`, locally inspected on 2026-11-05. Summarized
  only for engineering goals and study method; the original remains personal.

- Earlier repository, npm and OAuth audit records: dated 2026-10-14 through
  2026-11-04. Historical conclusions are explicitly bounded above.

- Available active/archived Codex chat listings and the relevant personal-brand
  chat were inspected for source discovery. This was not an exhaustive export of
  all conversations or a review of every personal document.

Do not import private account notes, credentials, financial details, employer
data, or raw conversation logs into the reusable project. Update this profile
from demonstrations and explicit corrections, not inferred seniority.
