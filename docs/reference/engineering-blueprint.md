# AI Engineering Skills / Neural Blueprint

## 1. Core principle

The engineer defines the architectural foundation, key decisions and direction
of the project.

An AI agent is used primarily for:

- routine tasks;
- implementation within an established direction;
- repetitive changes;
- analysis;
- verification;
- working faster with an existing codebase.

AI should not replace engineering judgment.

Relying on AI for everything under the assumption that this automatically
produces a large productivity gain is a mistake. AI does accelerate some work,
but the benefit is limited when the engineer stops understanding the system and
verifying the result.

---

## 2. The problem of cheap ideas

Generative AI has sharply reduced the cost of producing:

- ideas;
- code;
- alternative solutions;
- architectural proposals;
- written explanations.

The number of ideas grows faster than their average quality.

The scarce resources therefore become:

- filtering;
- verification;
- engineering judgment;
- understanding consequences;
- the ability to reject a poor solution.

This creates the problem of human forwarding proxies: a person passes a request
to AI and forwards its response with little intellectual scrutiny.

Such a workflow scales errors along with productivity.

---

## 3. Organizing changes

Group AI-generated changes into coherent categories.

For example:

```text
form-validation
authentication
error-handling
performance
accessibility
state-management
api
refactoring
testing
```

This makes it easier to:

- review changes;
- understand the blast radius;
- roll back;
- test;
- inspect change history.

---

## 4. Commits

Use Conventional Commits.

```text
feat(validation): add client-side email validation

- add schema validation
- display field-level errors
- prevent invalid submission
- add regression tests
```

A commit should describe the meaningful scope of the work, as well as the change
itself.

---

## 5. Pull Requests

Avoid oversized PRs.

A large PR:

- increases the reviewer's cognitive load;
- is harder to review thoroughly;
- hides errors in a large diff;
- makes architectural consequences harder to assess;
- reduces feedback quality;
- increases the likelihood of a superficial review.

Prefer small, coherent changes with one clear purpose and a bounded blast
radius.

---

## 6. Rules, Passive Skills and Active Skills

Not every capability should be a skill.

Distinguish between:

```text
Rules
Passive Skills
Active Skills
```

They operate at different levels.

---

## 7. Rules

A `Rule` is a persistent constraint or engineering principle.

A rule does not need to be invoked explicitly.

It should influence agent behavior in almost every relevant task.

Examples:

```text
Prefer the smallest coherent change.

Do not modify unrelated code.

Do not create unnecessary abstractions.

Preserve existing public contracts unless explicitly asked otherwise.

Do not claim verification unless verification was actually performed.

Measure before optimizing.

Do not hide uncertainty.

Follow repository conventions.

Avoid large unrelated diffs.
```

For Git:

```text
Use Conventional Commits.

Keep commits semantically coherent.

Do not mix refactoring and behavior changes unnecessarily.
```

For PRs:

```text
Prefer small reviewable changes.

Avoid combining unrelated concerns into one PR.
```

These are not skills.

The agent should not need to ask:

```text
Should I invoke prefer-small-pr?
```

This is simply part of its operating policy.

Conceptually:

```text
Rules
  ↓
constrain every relevant decision
```

---

## 8. Passive Skills

A passive skill operates in the background as part of other work, without
usually becoming the primary task.

Examples:

```text
detect-unnecessary-complexity
detect-breaking-change
detect-security-risk
review-for-accessibility
detect-large-blast-radius
find-unnecessary-changes
detect-missing-tests
detect-architecture-drift
detect-effect-misuse
detect-unsafe-type-assertion
detect-hidden-assumption
```

For example, an agent is implementing a feature.

The main workflow is:

```text
implement-feature
```

Meanwhile, these capabilities operate passively:

```text
detect-breaking-change
detect-unnecessary-complexity
detect-missing-tests
detect-security-risk
```

They should not turn every task into a separate audit.

Their purpose is to raise a signal only when a material issue is found.

The model:

```text
Active task
    │
    ├── passive check
    ├── passive check
    ├── passive check
    │
    ▼
continue normally
```

When a passive skill finds a material issue:

```text
passive detector
      ↓
significant finding
      ↓
activate dedicated skill
```

For example:

```text
review-for-performance
        ↓
possible expensive rerender
        ↓
diagnose-react-rendering-performance
```

A passive skill is therefore closer to a detector, guard or observer.

---

## 9. Active Skills

An active skill is a complete engineering procedure.

It has:

```text
Trigger
→ Goal
→ Investigation
→ Reasoning
→ Decision
→ Action
→ Verification
→ Completion Criteria
```

For example:

```text
debug-systematically
```

Workflow:

```text
reproduce
→ collect evidence
→ separate facts from assumptions
→ formulate hypotheses
→ test hypotheses
→ identify root cause
→ implement fix
→ verify
```

Other active skills:

```text
map-codebase
estimate-blast-radius
trace-data-flow
plan-code-change
debug-systematically
review-architecture
diagnose-performance-problem
design-public-api
implement-minimal-change
verify-before-claiming
```

Active skills cost more than passive skills because they initiate a complete
reasoning workflow.

Activate them only when they are needed.

---

## 10. The difference between the three levels

```text
RULE
"Prefer the smallest coherent change."

PASSIVE SKILL
"Detect whether the current change has unnecessary scope."

ACTIVE SKILL
"Analyze the change and redesign it to minimize blast radius."
```

Another example:

```text
RULE
"Do not optimize without evidence."

PASSIVE SKILL
"Detect suspicious performance-sensitive code."

ACTIVE SKILL
"Profile and diagnose the performance bottleneck."
```

One more example:

```text
RULE
"Preserve backward compatibility unless explicitly allowed to break it."

PASSIVE SKILL
"Detect a potential breaking API change."

ACTIVE SKILL
"Analyze API compatibility and design a safe migration."
```

This is an important architectural distinction.

---

## 11. Skills

A skill is more than knowledge or a general prompt.

A skill describes a repeatable engineering procedure.

A useful structure:

```text
Trigger
→ Goal
→ Investigation / Reasoning
→ Decision Rules
→ Actions
→ Verification
→ Completion Criteria
```

A weak skill:

```text
understand-event-loop
```

when its content is merely a lecture about the event loop.

A better alternative:

```text
diagnose-async-ordering-bug
```

with this procedure:

```text
observe ordering
→ reconstruct task/microtask scheduling
→ create hypothesis
→ reproduce
→ compare expected vs actual
→ identify violated assumption
→ verify fix
```

---

## 12. File structure

Keep reusable agent capabilities separate from a specific runtime.

```text
project/
│
├── AGENTS.md
│
├── .agents/
│   ├── rules/
│   ├── skills/
│   └── knowledge/
│
└── .codex/
```

For example:

```text
.agents/
  rules/
    engineering.md
    git.md
    reviews.md

  skills/
    active/
      debug-systematically/
        SKILL.md

      estimate-blast-radius/
        SKILL.md

      verify-before-claiming/
        SKILL.md

    passive/
      detect-breaking-change/
        SKILL.md

      detect-unnecessary-complexity/
        SKILL.md

      detect-security-risk/
        SKILL.md

  knowledge/
    javascript-event-loop.md
    browser-rendering.md
    react-rendering.md
```

This exact file structure is not mandatory, but the conceptual separation is
useful.

---

## 13. Reusing `.agents`

Treat `.agents` as a layer of reusable agent capabilities.

```text
             .agents/
                │
       ┌────────┼────────┐
       │        │        │
     Codex   Agent B   Agent C
```

A skill should not be tied to Codex when its logic applies across runtimes.

For example, the following skills:

```text
debug-systematically
estimate-blast-radius
review-api-design
verify-before-claiming
```

can be used by different coding agents.

The `.codex` directory remains the place for Codex-specific configuration.

Conceptually:

```text
AGENTS.md
    ↓
project-level behavior

.agents/
    ↓
reusable cognition and capabilities

.codex/
    ↓
Codex-specific runtime configuration
```

---

## 14. Engineering Neural Blueprint

The system should not load every skill at once.

It should operate as a network of related cognitive capabilities.

```text
                              trace-data-flow
                                    ▲
                                    │
Task
 │
 ▼
understand-problem
 │
 ▼
skill router
 │
 ▼
debug-systematically ───────► analyze-event-loop
 │
 ├──────────────────────────► analyze-next-caching
 │
 ▼
find-root-cause
 │
 ▼
implement-minimal-change
 │
 ▼
verify-before-claiming
```

Rules constrain the entire system:

```text
                    RULES
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   reasoning      skill routing    actions
```

Passive skills operate alongside the main workflow:

```text
                   Active workflow
                        │
              ┌─────────┼─────────┐
              │         │         │
            detect    detect    detect
            risk      scope     regression
              │
              └──────► signal
```

---

## 15. Skill graph

Skills can have relationships:

```text
requires
may_trigger
followed_by
delegates_to
conflicts_with
references
```

For example:

```yaml
name: debug-systematically

requires:
  - understand-problem

may-trigger:
  - trace-data-flow
  - trace-control-flow
  - analyze-event-loop
  - analyze-cache-behavior

followed-by:
  - implement-minimal-change
  - verify-before-claiming
```

A relationship does not imply automatic execution.

Avoid:

```text
A related to B
→ always run B
```

Use:

```text
A
+
observed condition X
+
relationship with B
→ activate B
```

---

## 16. Progressive Activation

```text
200 total capabilities
        ↓
10–20 relevant candidates
        ↓
2–5 active skills loaded
        ↓
1–4 active workflows executed
```

Lightweight passive checks can operate alongside the active workflow.

```text
Active skills: expensive
Passive skills: lightweight
Rules: always available
```

The total number of skills in the repository is not the main concern.

The main cost factors are:

```text
number of loaded active skills
×
skill size
×
reasoning depth
×
number of transitions
```

---

## 17. Limiting propagation

To avoid graph explosion:

```text
max active skills: 5
max traversal depth: 2
```

It is also useful to limit passive escalation:

```text
passive finding
    ↓
severity threshold
    ↓
activate active skill only if justified
```

Not every warning should start a complete reasoning workflow.

---

## 18. Layers of the engineering model

The complete model:

```text
engineering-mind/
│
├── rules/
├── knowledge/
├── mental-models/
├── heuristics/
├── passive-skills/
└── active-skills/
```

### Rules

Persistent constraints on behavior.

```text
Don't modify unrelated code.
Prefer small coherent changes.
Verify before claiming success.
```

### Knowledge

What the engineer knows.

```text
HTTP caching semantics
JavaScript event loop
React reconciliation
browser rendering pipeline
```

### Mental Models

How the engineer models the system.

```text
browser rendering pipeline
React state propagation
network request lifecycle
Next.js caching model
```

### Heuristics

Decision-making guidelines that are not always absolute.

```text
Prefer local state until sharing is required.

Measure before optimizing.

Prefer explicit ownership.

Avoid abstraction before variation is understood.
```

The difference between a rule and a heuristic:

```text
Rule:
Do not claim tests passed if they were not run.

Heuristic:
Prefer integration tests over excessive mocking.
```

A rule is nearly absolute.

A heuristic depends on context.

### Passive Skills

What the agent can notice while doing other work.

```text
detect-breaking-change
detect-architecture-drift
review-for-performance
detect-unnecessary-complexity
```

### Active Skills

What the agent can deliberately do.

```text
debug-systematically
estimate-blast-radius
plan-code-change
review-architecture
verify-before-claiming
```

---

## 19. Overall cognitive architecture

```text
                         Rules
                           │
                           ▼
Knowledge ───────► Mental Models
                         │
                         ▼
Task ─────────────► Context Model
                         │
                         ▼
                      Router
                         │
                  ┌──────┴──────┐
                  │             │
             Active Skill   Passive Skills
                  │             │
                  │        detect signals
                  │             │
                  └──────┬──────┘
                         ▼
                      Action
                         │
                         ▼
                    Verification
                         │
                         ▼
                    Self-Critique
                         │
                         ▼
                 Updated Context
```

---

## 20. The central idea

The goal is not to create AI that generates more code.

The goal is an engineering cognitive architecture that determines:

```text
what counts as a fact
what is an assumption
what to investigate
when a separate skill is needed
what to check passively
what the rules prohibit
which risks to consider
what to change
what to leave unchanged
how to assess the blast radius
when to escalate an issue
how to verify the result
when to consider a task complete
```

This system comes closest to a reusable model of an engineer's technical
reasoning.

A compact formulation:

```text
Rules        = how work must or must not be done
Heuristics   = how decisions are usually best made
Passive      = what to notice
Active       = what to do deliberately
Knowledge    = what to know
Mental Model = how to understand the system
```
