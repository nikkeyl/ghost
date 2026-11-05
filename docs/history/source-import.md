# GHOST source import

Date: 2026-10-02. Scope: the user-approved checklist, with interface design, CV,
Whisper transcription, and PDF/DOCX/PPTX/XLSX capabilities excluded by the
user's follow-up. The existing frontend engineering contracts are retained.

Source root: `/Users/nikkeyl/Documents/info-for-ghost/`. Target: the portable
`.agents` core and its source, index, and roadmap records. Local source paths
remain in this research record rather than reusable skills.

## Accepted scope and artifact map

| Accepted material                                                 | Source within the supplied root                                                                                    | Destination or treatment                                                                                |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| Verify a failure before asserting or multiplying repairs          | `agents/rules/verify-before-asserting.md`                                                                          | `rules/10-reasoning-and-evidence.md`                                                                    |
| Intentional staging, concise commit preferences, concurrent edits | `agents/rules/commit-oneline.md`, toolkit Git rules                                                                | `rules/30-git-and-review.md`, optional `knowledge/personal-authoring-preferences.md`                    |
| Requirements, plans, task dependencies, acceptance                | toolkit `refine-ticket`, `create-implementation-plan`, `split-plan-tasks`, `execute-plan-tasks`                    | existing clarification/planning skills, requirements and implementation-plan templates                  |
| Root-cause evidence and bounded fixes                             | Caveman `investigate-first`, `surgical-patch`; Superpowers `systematic-debugging`                                  | `debug-systematically`, implementation and evidence guidance                                            |
| Scoped diff review and grounded findings                          | toolkit `review-code-assistant`, `maintainer-review`, `self-review`; official `feature-dev` agents; Caveman review | `review-code-change`                                                                                    |
| Current-code review feedback and dispositions                     | toolkit `refine-pr-review`; Superpowers `receiving-code-review`                                                    | review procedure; replies remain drafts within task authorization                                       |
| Appropriate test levels, regression signal, mocks, manual checks  | toolkit manual-test and Nx checks; Superpowers TDD and completion verification                                     | `design-test-strategy`, test-signal/overmocking/build detectors, manual-test and verification templates |
| Behavior preservation and staged recovery                         | Caveman `safe-refactor`, `migration`, `lean-build`                                                                 | `refactor-without-behavior-change`, `plan-migration`, preservation knowledge, migration template        |
| Reviewer-facing handover and standalone checkpoints               | toolkit `handover`, self-contained-docs; Caveman `verify-and-stop`                                                 | `write-maintainer-notes`, handover and verification templates                                           |
| Focused retrieval and API uncertainty                             | `agents/skills/ows-open-websearch/` and references                                                                 | `research-unknown-api`, web-research knowledge                                                          |
| Skill quality and durable feedback                                | toolkit compact authoring and self-improvement; official and Superpowers skill-writing material                    | `extract-engineering-lessons`, authoring/evaluation knowledge and template                              |
| Context and memory hygiene                                        | toolkit `context-checkup`, `memory-doctor`, `agentify-project`; context-mode and Caveman                           | context-hygiene knowledge, existing runtime/context guidance                                            |
| Markdown, prose, review comments                                  | `agents/skills/my-md-writing/`, `my-deslopify/`; toolkit prose/comment rules                                       | `update-documentation`, writing/review knowledge                                                        |
| Source mapping and coverage                                       | supplied manifests, licenses, catalogs, and GHOST backlog                                                          | this record, analysis, index, README, roadmap coverage                                                  |
| Integration candidates                                            | `agents/plugins.md`, launch-file references, cached tool docs                                                      | on-demand integration inventory; no setup or runtime configuration imported                             |

The eight new active skills and five passive detectors are indexed in
[`.agents/skills/README.md`](../../.agents/skills/README.md). Seven knowledge
files and seven templates support the procedures. Existing skills were amended
where the source material did not justify an independent capability.

## Source identity and reuse

- Custom files under `agents/` are supplied local material; no universal
  external behavior or authorship claim is inferred from them.

- `home_config/agent-toolkit` identifies its materials as MIT, with the notice
  `Copyright (c) 2026 Engineering in the age of AI`.

- Cached Caveman is in `claude/plugins/cache/caveman/caveman/2.7.0/`. Its
  license scopes MIT separately from Engine-linked BSL material. Only
  engineering procedure concepts are adapted; Engine implementations are not
  bundled.

- Superpowers is cached under a `6.3.0` directory while its plugin manifest
  reports `6.4.2`. These identify the supplied snapshot, not a verified current
  release. Its MIT notice identifies Jesse Vincent, 2025.

- context-mode is cached under `1.0.169` and identifies Elastic License 2.0. CC
  Safety Net is cached under `2.4.12` and identifies MIT. Their roles are
  documented as integration candidates; source code and hooks are not bundled.

- Official marketplace examples were read from the supplied local checkout,
  especially feature exploration/review and skill-authoring material. Their host
  tooling and confidence scores are not transplanted into portable rules.

The GHOST text and templates are new, scoped formulations. No vendor skill body,
executable helper, reference cache, or implementation is copied wholesale.
Source names and notices are retained here for provenance. Actual third-party
code reuse would require preserving the applicable notices and license terms.

## Adaptation decisions

- Preserve the five-active-skill and two-hop routing budget. Catalog growth does
  not imply loading every procedure or spawning agents automatically.

- Replace mandatory per-file stops with scoped checkpoints and existing user
  authorization. A clear implementation request remains sufficient for its
  scope.

- Keep TDD, worktrees, fresh-context review, Nx, and multi-engine search
  conditional on actual risk, host support, and authorization.

- Replace exclusive web-provider routing with the available approved path.
  Separate retrieval from setup, activation, proxy, and browser failures.

- Preserve relevant context rather than requiring all memory to be drained.
  Persistent user-level changes need their own authorization and ownership.

- Treat short commit wording and absence of unsolicited AI footers as an
  optional personal profile. Source attribution is preserved independently.

- Keep Markdown conventions consumer-specific. No fixed Claude output path,
  mandatory front matter, or automatic external style-list refresh is imported.

- Report confidence limits in words and evidence. Do not invent numeric
  certainty or carry vendor savings claims into GHOST as measured results.

- Keep tests, assertions, and recovery checks proportional to material failure
  modes. A structural pass does not mean an agent procedure works in a host.

## Excluded material

The user's four exclusions are not promoted or added to the backlog by this
import: interface-design principles from frontend-design, developer CV, Whisper
processing, and office/PDF document reading or validation. Existing
accessibility and frontend correctness guidance is unaffected.

Also excluded: credentials and `env`, account/machine identifiers, backups, logs
and transcripts as durable instructions, databases, cache and marketplace
duplicates, installation scripts, self-healing plugin patches, fixed model
settings, permission bypasses, and global MCP/client configuration. Unsupported
guarantees, fabricated personal experience, and fabricated metrics are not
useful evidence and are not imported.

## Validation status

The staged import passes YAML/schema, procedure-heading, index, graph-target,
file-reference, portability, and exclusion checks. The resulting catalog has 19
active skills, 13 passive detectors, 16 knowledge files, and 8 templates. The
check resolves 79 graph edges, 10 local Markdown links, and 57 inline paths.
Four deliberately invalid copies confirm detection of an empty description,
dangling graph target, missing index entry, and missing file reference.

A manual routing walkthrough covers diff review, diagnosis without fixing,
behavior-preserving refactoring, migration planning without execution, and
Markdown editing without external research. Their conditional selections stay
within the unchanged five-skill/two-hop policy. This is author inspection, not
an independent agent run or a runtime discovery test.

These checks do not establish behavioral quality, external integration, or phase
completion. No installer, vendor executable, or external service was exercised.

Representative host trials remain pending and are the next roadmap step.
