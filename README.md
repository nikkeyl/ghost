# GHOST

![AI](https://img.shields.io/badge/AI-red)

Portable engineering rules and skills for coding agents, created entirely with
AI assistance from Nikkeyl's writing and the supplied blueprint.

## Use

Start with `AGENTS.md`, then the relevant rules and skill index. This repository
has no application server or package installation step.

```sh
python3 utilities/check-docs.py
```

## Decisions

- `.agents/` is the source of truth; `AGENTS.md` and `CLAUDE.md` are thin
  discovery adapters rather than duplicated rule sets.

- Rules constrain decisions; active skills execute procedures; passive skills
  raise signals. Knowledge and templates load when needed.

- Default activation is at most five active skills and two graph hops to limit
  context growth. `understand-and-plan-change` routes engineering tasks.

- The catalog encodes procedures, not complete human judgment. Structural checks
  do not establish skill quality or compatibility with every runtime.

## Files

- `.agents/rules/` — constraints; `.agents/skills/README.md` — skill index.

- `.agents/knowledge/`, `.agents/templates/` — references and working formats.

- [Runtime adapters](.agents/knowledge/runtime-adapters-and-context-budget.md).

- [Source analysis](docs/GHOST-ANALYSIS.md),
  [import decisions](docs/info-for-ghost-import.md) and
  [roadmap](docs/ROADMAP.md).

## License

[MIT](LICENSE).
