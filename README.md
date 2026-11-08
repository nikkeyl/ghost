# GHOST

![AI](https://img.shields.io/badge/AI-red)

Engineering rules and skills for coding agents. Use them to investigate a
codebase, plan a change, review a diff or debug a failure.

The project was created entirely with AI assistance from Nikkeyl's writing
and an engineering blueprint.

## Install

Download your agent's archive from the
[latest release](https://github.com/nikkeyl/ghost/releases/latest). Archives
are available for Codex, Claude Code, Cursor, GitHub Copilot, Gemini CLI and
OpenCode.

> [!IMPORTANT]
>
> Extract the archive into the project, including hidden folders. If the
> project already has agent instructions, merge the relevant content instead
> of replacing the existing files.

Open the project in your agent and check its skill list. Discovery and
automatic selection depend on the host and its version; an extracted folder
alone does not confirm that a skill is active.

## Use

Ask the agent to apply a skill to a specific task, for example:

```text
Use debug-systematically to investigate why this form submits twice.
Use review-for-accessibility to review keyboard behavior in this dialog.
```

The [skill index](.agents/skills/README.md) lists available procedures and
their triggers. Rules describe constraints, skills describe tasks, and
knowledge files supply background when a task needs it. Keep
project-specific instructions in the project that owns them.

GHOST cannot establish that a change works or that an agent followed its
instructions. Review the resulting diff and the evidence for the changed
behavior.

## Maintain

The checkout keeps the shared instructions in `.agents/`; the release
workflow generates each agent's directory layout and loader. It excludes
maintainer docs from the archives.

```sh
bun run init
```

See the [documentation](docs/README.md) for authoring, runtime discovery
records and the roadmap.

## License

[MIT](LICENSE).
