# Native skill discovery trial

## Scope and expected outcomes

This trial addresses native discovery and per-host distribution, not
completion of the broader C03/C04 behavioral suite. The source baseline
was `c9eeed7`; the tested working changes add loaders, UI metadata and
release profiles without renaming the 33 canonical procedures/signals.

Before the native calls, the expected outcomes were: expose the intended
active catalog without metadata errors; resolve an explicitly named
planning skill; preserve read-only scope; return module ownership and
verification conditions. A second prompt omitted skill names to exercise
implicit selection from the extracted Codex profile. The fixture was a
hypothetical 470-line frontend entry mixing task state/localStorage with
a skill catalog and journal. No application implementation was supplied.

## Observed hosts

| Host           | Version         | Discovery                                                                                                                                                  | Execution                                                                                      |
| -------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Codex CLI      | 0.166.0-alpha.6 | Native app-server `skills/list`: 33 source skills, 24 UI records, no GHOST errors; extracted profile: 24 active skills, no passive entries or GHOST errors | Explicit `plan-code-change` and implicit planning/refactor prompts completed in read-only mode |
| Claude Code    | 2.1.319         | Native stream initialization listed all 24 GHOST active skills/commands from checkout symlinks and the extracted flat profile; no GHOST passive commands   | Unavailable: no account/login; invocation stopped with the host's authentication error         |
| Cursor         | Not installed   | Native paths checked against official documentation; profile structure checked locally                                                                     | Unavailable                                                                                    |
| GitHub Copilot | Not installed   | Native paths checked against official documentation; profile structure checked locally                                                                     | Unavailable                                                                                    |
| Gemini CLI     | Not installed   | Native paths checked against official documentation; profile structure checked locally                                                                     | Unavailable                                                                                    |
| OpenCode       | Not installed   | Native paths checked against official documentation; profile structure checked locally                                                                     | Unavailable                                                                                    |

Claude also listed its own bundled skills; those are not counted as GHOST
procedures. The user confirmed that they do not have Claude. No login,
account setup or model execution was simulated. Desktop skill selectors,
green badges and implicit Claude selection were not observed.

## Codex behavior

The explicit source-checkout request selected `plan-code-change`, read its
body and relevant rules, and returned a bounded plan with state/storage,
catalog and journal ownership. It named preserved contracts, verification
conditions and the absence of actual application source. It did not edit,
install, delegate or run builds. It slightly exceeded the requested
250-word plan budget; this is a routing/execution trial, not perfect
instruction compliance.

The extracted-profile prompt did not name a skill. Codex read
`plan-code-change` and `refactor-without-behavior-change`, identified the
refactor procedure as the main workflow, and proposed owned modules,
behavior-preservation checks and unresolved source assumptions. This
supports native availability and one observed implicit selection path.
It does not establish routing accuracy over other tasks or reduced cost.

Reported token usage was 62,846 input / 819 output for the explicit run,
and 81,155 input / 944 output for the implicit run. These are total host
turn usage, including inherited context and cached input, not GHOST-only
text or a comparable efficiency baseline. C05 remains open.

## Archive checks

The release workflow builds six assets named
`ghost-{agent}-{short-commit}.zip` under one `ghost-{short-commit}` release.
Each ZIP has the matching top-level folder, a flat native catalog with 24
active skills, nine passive references outside native discovery, and the
required shared rules, knowledge, templates, index and loader.

Local checks execute the workflow's actual build block against a staged
Git tree. They inspect every ZIP entry, metadata, local operational
paths, Markdown links and counts. Archives contain ordinary files rather
than symlinks, exclude maintainer docs/workflows, and retain Codex UI YAML
only in the Codex profile. Published artifacts require separate CI and
post-publication inspection for the resulting immutable commit.

The portable runtime reference intentionally describes all hosts and the
source checkout; its illustrative cross-host paths need not exist in an
individual profile. Operational skill/rule/template paths are rewritten
to the selected installation layout.

## Failures and limits

The first Codex execution attempt could not open its local service state
under restricted filesystem access. The same read-only test completed
with access to the CLI's own service state. Its model-list refresh timed
out once; the turn still completed. Existing third-party plugin metadata
produced warnings unrelated to the GHOST catalog; discovery errors for
GHOST itself were empty.

The first archive path check found a remaining bare `.agents/skills`
reference in a non-Codex profile. The build now rewrites that form as well
as directory-prefixed paths. Initial Markdown list spacing, YAML line
length and the new `.mdc` formatter mapping were corrected before final
checks. These failed attempts are not passing evidence.

## Sources

- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Codex project instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Cursor skills](https://prod.cursor.com/docs/skills)
- [GitHub Copilot skills](https://docs.github.com/en/copilot/concepts/customizations/agent-skills)
- [Gemini CLI skills](https://geminicli.com/docs/cli/skills/)
- [OpenCode skills](https://docs.opencode.ai/docs/skills/)
