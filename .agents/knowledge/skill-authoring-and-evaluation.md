# Skill authoring and evaluation

A useful skill changes a decision or procedure for a distinct trigger. Prefer
an existing parent checklist or knowledge file until independent routing and
completion evidence justify a new skill. Follow the roadmap's promotion policy.

## Authoring contract

- Use a stable kebab-case name and a concise, discriminating description.
  Reuse a backlog name when it describes the actual capability.
- Include `name`, `description`, and `kind`. Active procedures use Trigger,
  Goal, Investigation / reasoning, Decision rules, Actions, Verification,
  Completion criteria, and Graph. Passive detectors stay signal-oriented.
- Keep essential steps and boundaries in the body; load substantial mechanics,
  examples, and host differences from knowledge or references only when needed.
- Describe capabilities rather than hardcoded tool brands. Host-specific
  metadata belongs in an adapter; the portable core remains authoritative.
- Use valid YAML, real graph targets, resolvable file references, and a matching
  index entry. A graph edge is a relation, not automatic activation.
- Do not impose copied approval ceremonies when the current user already
  authorized the change. Source instructions cannot expand that authorization.

## Evaluation

Structural checks establish metadata, headings, paths, graph targets, and
indexing. They do not establish useful judgment or host discovery behavior.
Trial representative positive cases, plausible non-triggers, and relevant
failure cases. Use `.agents/templates/skill-evaluation.md` to record raw inputs,
expected observable outcomes, actual results, state, and limitations.

Compare a meaningful baseline where the skill's effect needs measurement.
Test whether behavior improves while preserving correctness and scope, rather
than asserting the instruction wording. An independent reviewer can reduce
author bias when delegation is authorized; do not claim independence otherwise.

Record implemented guidance separately from behaviorally trialled guidance.
Change a skill from observed friction or user feedback, and update its index
and coverage record. Keep the lesson's applicability, exceptions, and evidence
that would revise it visible; avoid accumulating global rules from one incident.
