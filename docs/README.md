# Documentation

GHOST runtime instructions live in [`.agents/`](../.agents/skills/README.md).
This directory contains maintainer documentation and is excluded from release
archives. The checkout stores a single portable loader at `.agents/AGENTS.md`.
Release builds generate each agent's native paths from this source, with
Claude/Gemini/Cursor/Copilot loaders defined in the workflow. No native
projections or
skill symlinks are maintained in the checkout.

## Contributing

Run `bun run init` to install dependencies and enable Husky. The pre-commit
hook formats staged files and lints Markdown; the commit-msg hook checks
Conventional Commits.

## Planning

- [Roadmap](planning/roadmap.md): capability phases, sequencing and promotion
  criteria.

- [Backlog](planning/backlog.md): the preserved inventory of 479 candidate
  procedures.

- [Checklist](planning/checklist.md): completed work, remaining actions and
  acceptance criteria.

The roadmap owns direction, the backlog owns candidate names, and the checklist
owns actionable work. Keep completed tasks separate from remaining gates.

## Reference

- [Engineering blueprint](reference/engineering-blueprint.md): the design model
  for rules, knowledge and skills.

- [Author profile](reference/author-profile.md): optional personal context,
  evidence boundaries and learning priorities.

Reference material explains the design; it does not certify runtime behavior or
the author's proficiency.

## History

- [Native discovery trial](history/runtime-discovery-2026-11-06.md): host
  versions, archive profiles, observed discovery and execution limits.

- [Source analysis](history/source-analysis.md): provenance and adaptation
  decisions.

- [Source import](history/source-import.md): accepted inputs, exclusions and
  original checks.

- [2026-11-05 audit](history/audit-2026-11-05.md): findings against its recorded
  baseline.

History preserves evidence. Its paths, commands and findings may describe an
older repository state and do not create current implementation requirements.
