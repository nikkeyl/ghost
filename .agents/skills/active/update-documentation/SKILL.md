---
name: update-documentation
description:
  "Create or revise technical Markdown, engineering notes, and prose while preserving
  facts, audience needs, and repository format."
kind: active
---

# Update documentation

## Trigger

Use for requested technical Markdown, READMEs, guides, architecture notes, or prose
editing. Keep ordinary chat answers inline unless a saved artifact is needed.

## Goal

Produce clear, accurate documentation whose structure and detail serve its reader.

## Investigation / reasoning

1. Identify audience, purpose, destination, output format, and the required change.
2. Read the document, repository conventions, and factual sources before drafting.
   Route uncertain technical claims through `research-unknown-api` when needed.
3. For new documents, outline only the necessary structure. For an editing pass,
   preserve the existing outline and formatting unless restructuring is in scope.
4. For an architecture note, explain the decision, alternatives, consequences,
   invariants, reversibility, and evidence without inventing rationale.

## Decision rules

- Read `.agents/knowledge/writing-and-review-communication.md` for prose and Markdown
  guidance. Match the target renderer; Pandoc conventions are conditional.
- Keep facts, uncertainty, URLs, code, and quotations intact during style edits.
  Style heuristics cannot establish whether a human or AI wrote a passage.
- Remove filler and formulaic phrasing without forcing novelty or deleting necessary
  caveats. Compact wording must preserve operative meaning.
- Follow the project's language, filename, and destination conventions. Front matter,
  callouts, tables of contents, and conversion metadata depend on the document's
  consumer, not a universal Markdown rule.
- Read external style references only when the task needs them; fetching a writing
  checklist is not a mandatory step for every document.

## Actions

Write or edit the requested document. Use meaningful headings, concrete wording, and
parallel lists only where they aid reading. For governing documentation, also consult
`.agents/knowledge/skill-authoring-and-evaluation.md`.

## Verification

Compare facts and meaning before and after; check links, fenced code, headings, and
rendering-specific syntax. Report renderer checks only if performed.

## Completion criteria

The requested document is complete, facts and caveats are preserved, and formatting
suits its consumer.

## Graph

```yaml
may-trigger: [research-unknown-api]
references: [write-maintainer-notes]
```
