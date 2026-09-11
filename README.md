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

## Entry points

- Start with `AGENTS.md`.
- Use `.agents/rules/00-operating-principles.md` and
  `.agents/rules/10-reasoning-and-evidence.md` for every engineering task.
- For a code change, route through `understand-and-plan-change`,
  `implement-minimal-change`, and `verify-change` as needed.
- Load `review-component-anatomy` only for React component work.
- Let passive detectors raise signals; do not turn every warning into a full
  audit.

See `GHOST-ANALYSIS.md` for the source inventory, evidence quality, and
decisions that were deliberately not promoted to unconditional rules.

The long-term capability backlog and implementation sequence are tracked in
[`ROADMAP.md`](./ROADMAP.md). It intentionally groups the 444 candidate
procedures into domain families before promoting individual procedures to
standalone skills.
