# GHOST

![AI](https://img.shields.io/badge/AI-red)

Portable engineering rules and skills for coding agents, created entirely with AI
assistance from Nikkeyl's writing and the supplied blueprint.

## Use

Start with `AGENTS.md`, then the relevant rules and `.agents/skills/README.md`. This
repository has no application server or package installation step. Use the
[roadmap](docs/ROADMAP.md) and [completion checklist](docs/project-checklist.md) for
planned work; the [2026-11-05 audit](docs/audit-2026-11-05.md) records evidence and
current limitations.

```sh
bun ci
bun run lint
```

`bun run prettier:fix` formats Markdown, YAML, JSON and JavaScript.
`bun run remark:check` lints Markdown, including the hidden `.agents` tree and skill
front matter. Prettier owns formatting; remark adds structural rules. The remark
presets follow `archoleat/next-accordion`, with overrides for Prettier list
formatting, discovery filenames and existing phase headings.

EditorConfig uses UTF-8, LF, two-space indentation and an 85-column target. Python
uses four spaces; Markdown tables and generated lockfiles may exceed the target.
GitHub Actions runs checks without rewriting files. Dependabot checks Bun
dependencies and pinned Actions twice a year.

## Release

```sh
bun run release:archive
bun run release:archive v1.0.0
```

The builder writes `dist/ghost-<version>.zip` and `dist/SHA256SUMS`. It includes all
tracked and non-ignored untracked `.md` files, including `.agents`, plus `LICENSE`,
under a single `ghost-<version>/` directory. Directory structure and file bytes are
preserved. Dependencies, build output and non-Markdown assets are excluded. Local
snapshots include current edits; tag releases use the tagged checkout.

Pushing a version tag such as `v1.0.0` runs all checks, builds the archive and
publishes a GitHub Release with generated notes and the checksum. Tags with a
prerelease suffix, such as `v1.0.0-beta.1`, produce prereleases. Publishing uses the
repository's built-in `GITHUB_TOKEN`; no npm token or GitHub App is needed. Create
the tag on the intended main-branch commit after its checks pass.

## Decisions

- `.agents/` is the source of truth; `AGENTS.md` and `CLAUDE.md` are thin discovery
  adapters rather than duplicated rule sets.

- Rules constrain decisions; active skills execute procedures; passive skills raise
  signals. Knowledge and templates load when needed.

- Default activation is at most five active skills and two graph hops to limit
  context growth. `understand-and-plan-change` routes engineering tasks.

- The catalog encodes procedures, not complete human judgment. Structural checks do
  not establish skill quality or compatibility with every runtime.

## License

[MIT](LICENSE).
