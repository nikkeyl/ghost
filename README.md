# GHOST

GHOST is a reusable engineering cognition layer derived from the public
technical writing and gists of Nikkeyl, plus the supplied `AI Engineering
Skills - Neural Blueprint.md`.

The name is a codename, not a claim that an agent can reproduce a human
engineer's complete judgment. The system encodes repeatable constraints,
diagnostics, procedures, and mental models while keeping engineering decisions
with the human and the evidence.

## Model

```text
Rules       = always constrain relevant decisions
Heuristics  = context-sensitive defaults
Passive     = notice material risk during another task
Active      = execute a complete engineering procedure
Knowledge   = reusable facts and mental models
```

The source material was translated into this model rather than copied
literally. A fixed component layout is useful as a consistency convention; it
is not a universal React law. A safe-change protocol is useful as a workflow;
it must not force a user-confirmation deadlock or unsafe automatic commits.

## Progressive activation

Use the smallest relevant set:

```text
all capabilities → relevant candidates → 2–5 active skills → verified result
                                  ↘ lightweight passive checks
```

Default graph constraints are five active skills and two traversal levels.
Increase them only when the task is genuinely cross-cutting and state why.
The default router is `understand-and-plan-change`: it selects a parent skill
from the candidate families, keeps leaf procedures grouped, and expands only
when investigation exposes a material uncovered risk.

Runtime-specific loading and context-budget guidance lives in
`.agents/knowledge/runtime-adapters-and-context-budget.md`; it is read on
demand and is not part of the always-loaded core.

## Entry points

- Start with `AGENTS.md`.
- Use `.agents/rules/00-operating-principles.md` and
  `.agents/rules/10-reasoning-and-evidence.md` for every engineering task.
- For a code change, route through `understand-and-plan-change`,
  `implement-minimal-change`, and `verify-change` as needed.
- Load `review-component-anatomy` only for React component work.
- Load `review-custom-control` when a custom interactive control or its state
  matrix is in scope.
- Load `review-form-contract` when a form or its submission lifecycle is in
  scope.
- Let passive detectors raise signals; do not turn every warning into a full
  audit.

See `GHOST-ANALYSIS.md` for the source inventory, evidence quality, and
decisions that were deliberately not promoted to unconditional rules.

The long-term capability backlog and implementation sequence are tracked in
[`ROADMAP.md`](./ROADMAP.md). It intentionally groups the 444 candidate
procedures into domain families before promoting individual procedures to
standalone skills.
