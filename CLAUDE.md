# GHOST Claude Code adapter

GHOST's portable engineering layer lives in `.agents/`; this file is
only a short discovery adapter for Claude Code.

## Loading order

1. Read only the `.agents/rules/` files relevant to the task.

1. Use `.agents/skills/README.md` and skill descriptions to select the
   smallest active parent skill.

1. Load at most five active skills and traverse at most two graph hops
   by default.

1. Read linked `.agents/knowledge/` files only when the selected
   workflow needs their mental model.

1. Keep passive detectors lightweight and escalate only on a material
   signal.

1. Finish with evidence-backed verification and an explicit uncertainty
   report.

Do not copy the contents of `.agents/` into this always-loaded file.
Runtime behavior belongs in the adapter; engineering rules and
procedures belong in the portable core.
