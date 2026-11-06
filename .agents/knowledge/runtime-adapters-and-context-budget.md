# Runtime adapters and context budget

GHOST has a portable engineering core and a thin runtime adapter. The
core contains rules, knowledge, active procedures, passive detectors,
and graph metadata. The adapter explains how a particular coding agent
discovers that core. Do not copy runtime-specific behavior into the
engineering rules.

## Universal core

- Keep always-loaded guidance short, stable, and applicable to most
  tasks.

- Use `description` as routing metadata. It should identify the
  observable trigger and the result of the skill, not repeat the entire
  procedure.

- Load one parent active skill first. Add a child only when
  investigation reveals its trigger, risk, or verification need.

- Keep active skills procedural: trigger, goal, investigation, decision
  rules, actions, verification, completion criteria, and graph.

- Keep detailed explanations, examples, source notes, and platform
  mechanics in knowledge files that are read only when the selected
  workflow needs them.

- Keep passive detectors short. A passive detector should return no
  signal, signal, or escalation rather than injecting a full workflow
  into every task.

## Token and context controls

Use the following order when a task starts:

1. Read only the relevant rules.

1. Use the skill index and descriptions to choose the smallest parent
   skill.

1. Read the selected skill body.

1. Read linked knowledge only when a decision depends on that mechanism.

1. Use focused searches and bounded file reads; summarize large command
   output before carrying it into the next decision.

1. Keep the active set at five skills or fewer and the graph traversal
   at two hops or fewer unless a material risk justifies expansion.

Do not reduce tokens by removing validation, authorization, security,
accessibility, error handling, or evidence. Reduce rediscovery,
irrelevant context, speculative implementation, repeated explanations,
and unfiltered tool output instead.

Stable instruction prefixes should remain unchanged where the host
supports prompt caching. Runtime-supported hooks may filter logs,
extract changed-file summaries, or perform deterministic checks before
their output reaches the model. Independent broad scans may use an
isolated subagent and return a compact evidence summary instead of
duplicating the entire exploration in the main context.

## P0 runtime matrix

GHOST targets coding-agent runtimes, not the underlying model vendor.
The P0 set is deliberately limited to hosts with a native or near-native
path for Agent Skills, scoped project instructions, and on-demand
loading:

| Runtime        | Always-loaded entry point      | Skill discovery                                            | GHOST adapter responsibility                                                             |
| -------------- | ------------------------------ | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Codex          | `AGENTS.md`                    | `.agents/skills/`                                          | Keep the root loader compact; use the canonical tree directly                            |
| Claude Code    | `CLAUDE.md`                    | host skills directory, normally `.claude/skills/`          | Keep `CLAUDE.md` short; project active skills into the host directory when needed        |
| Cursor         | `.cursor/rules/`               | `.cursor/skills/`                                          | Project the portable rules and active skills; do not duplicate their bodies              |
| GitHub Copilot | repository custom instructions | `.agents/skills/`, `.github/skills/`, or `.claude/skills/` | Prefer the canonical `.agents/skills/` location and keep simple global guidance separate |
| Gemini CLI     | `GEMINI.md`                    | `.agents/skills/` or `.gemini/skills/`                     | Keep `GEMINI.md` as a loader and expose the canonical skills directly when supported     |
| OpenCode       | `AGENTS.md`                    | `.agents/skills/` or `.claude/skills/`                     | Use the canonical tree directly and preserve the existing loader contract                |

The exact host directory is an adapter concern and must be rechecked
against the runtime version before adding a projection. The portable
skill body, description, trigger, verification contract, and knowledge
boundaries remain unchanged across hosts.

Passive detectors require special handling. Hosts generally discover
`SKILL.md` files as invocable skills and do not automatically understand
the distinction between GHOST's active procedures and passive signals.
Keep the passive directory separate in the core; expose a detector
through a host hook, CI check, explicit policy, or non-invocable
projection when the host supports one. Never solve this by copying
passive detectors into the active index.

P0 completion means that the same representative workflows can be routed
and verified on every target: understand a change, review a form or
component, and verify a bounded implementation. It does not mean that
every host must have identical hooks, subagents, UI, or tool
permissions.

## Minimal-solution ladder

Before adding a custom solution, check the first rung that satisfies the
contract:

1. the capability is not needed;
1. existing project code already provides it;
1. the standard library provides it;
1. the browser or platform provides it natively;
1. an installed dependency already provides it;
1. a small local implementation is sufficient.

The ladder is a decision aid, not permission to golf code. Stop at the
first adequate rung while preserving the material failure modes and the
verification required by the task.

## Release profiles

The repository keeps active procedures in `.agents/skills/active/` and
passive signals in `.agents/skills/passive/`. Those are authoring paths.
Each release projects this source into six independent ZIP archives.
Install one profile per project; do not combine profiles.

| Profile        | Native procedures   | Instruction entry                 |
| -------------- | ------------------- | --------------------------------- |
| Codex          | `.agents/skills/`   | `AGENTS.md`                       |
| Claude Code    | `.claude/skills/`   | `CLAUDE.md` imports `AGENTS.md`   |
| Cursor         | `.cursor/skills/`   | `.cursor/rules/ghost.mdc`         |
| GitHub Copilot | `.github/skills/`   | `.github/copilot-instructions.md` |
| Gemini CLI     | `.gemini/skills/`   | `GEMINI.md` imports `AGENTS.md`   |
| OpenCode       | `.opencode/skills/` | `AGENTS.md`                       |

Every profile contains ordinary files, a flat native active catalog,
shared rules/knowledge/templates under `.agents`, an index at
`.agents/skills.md` and passive references at `.agents/detectors/`.
The build rewrites authoring paths in operational files to installed
paths. This cross-host reference retains its authoring examples.
Codex alone receives `agents/openai.yaml` UI metadata. UI appearance
and skill execution remain host behavior, not a guarantee from YAML.

In a checkout, Claude's per-skill symlinks point to the canonical active
folders. Update those links when adding/removing an active procedure;
never edit a second copy of its body. Release builds use the immutable
Git commit and materialize fresh ordinary files, so ZIP extraction does
not require symlink support. Upgrades replace the selected profile's
previous GHOST-owned files; preserve unrelated local skills and merge
existing instruction entries. Remove the installed GHOST skill folders
and loader entries to uninstall; retain other project instructions.

A host must list the intended skills before activation is claimed.
Explicit selection and automatic description matching need separate
observations. A file read, status text or archive inspection does not
prove a native UI badge or correct execution. Maintainer evidence lives
in `docs/history/runtime-discovery-2026-11-06.md`; full C03/C04 trials
remain separate gates.

## Codex adapter

Codex discovers `AGENTS.md` by scope and applies closer guidance later.
Its project instruction budget is finite, so the root `AGENTS.md` should
stay a compact loader and contract. It should point to relevant
`.agents` files without inlining the whole corpus. Nested `AGENTS.md`
files are appropriate only when a subtree truly needs different
guidance.

## Claude Code adapter

Claude Code keeps `CLAUDE.md` as always-loaded project guidance and
loads skill bodies on demand using their descriptions. A Claude adapter
should map the portable rules that are genuinely global into a short
`CLAUDE.md`, map path-specific rules to scoped rule files when
supported, and expose the portable active skills through the host's
skills directory. Detailed reference material belongs in knowledge files
or skill references, not in the always-on file.

## Cursor adapter

Cursor has separate project rules and skills locations. A Cursor adapter
should translate only the compact always-on rules into `.cursor/rules/`
and expose portable active skills through `.cursor/skills/`. Treat the
`.agents` tree as the source of truth and validate the host's current
discovery behavior before using a symlink or generated projection.

## GitHub Copilot adapter

GitHub Copilot supports the Agent Skills layout, including
`.agents/skills/`, across its supported agent surfaces. Keep simple
repository-wide guidance in custom instructions and let the skill
descriptions route deeper procedures. Do not put the full GHOST corpus
into always-on custom instructions.

## Gemini CLI adapter

Gemini CLI supports hierarchical `GEMINI.md` context files and on-demand
Agent Skills. Use `GEMINI.md` as a compact loader and prefer
`.agents/skills/` when the current CLI discovers it; otherwise project
the active skills to the runtime's native skills directory without
changing their bodies.

## OpenCode adapter

OpenCode can discover `AGENTS.md` and `.agents/skills/` and loads skill
bodies on demand. It should therefore need little more than the portable
loader and the passive-detector policy described above. Keep
OpenCode-specific settings about permissions or invocation out of the
engineering rules.

## Portability rule

If a runtime supports hooks, subagents, deferred MCP/tool definitions,
or automatic compaction, use those mechanisms only for context transport
and deterministic preprocessing. The engineering decision remains in the
portable core. If a runtime lacks them, the same core must still work
through the router, focused reads, and explicit verification.

## Optional integrations and context audit

Read `.agents/knowledge/agent-context-hygiene.md` for a requested audit
of actual loading cost and durable context. Read
`.agents/knowledge/tool-integration-candidates.md` only when considering
a tool that could solve an observed transport, retrieval, or guard
problem. The supplied setup is source evidence, not a working adapter or
a current support matrix. Verify the selected host and operation before
adoption.

## Sources

- [OpenAI AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code feature overview](https://code.claude.com/docs/en/features-overview)
- [Claude Code cost management](https://code.claude.com/docs/en/costs)
- [Cursor Agent Skills](https://prod.cursor.com/docs/skills)
- [Cursor rules](https://docs.cursor.com/context/rules-for-ai)
- [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [Gemini CLI Agent Skills](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md)
- [Gemini CLI context files](https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html)
- [OpenCode Agent Skills](https://opencode.ai/docs/skills)
- [Ponytail README](https://github.com/DietrichGebert/ponytail/blob/main/README.md)

These sources describe host behavior and an external minimal-solution
plugin; they do not override GHOST rules or repository-specific
constraints.
