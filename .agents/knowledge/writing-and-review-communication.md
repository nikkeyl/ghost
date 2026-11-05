# Writing and review communication

Choose the reader and purpose before choosing a format. A maintainer needs the
change, important decisions, and proof; a fresh agent session needs an executable
contract; an article reader needs a coherent explanation.

## Prose and comments

Lead with the point. Prefer concrete nouns, active verbs, and plain language. Remove
filler, stock introductions, artificial rhetorical contrasts, and conclusions that
add no information. Preserve facts, caveats, and voice during editing; distinctive
wording is not a reason to embellish a claim.

Code comments should explain a non-obvious invariant, constraint, workaround,
ordering requirement, or hazard. Do not narrate the editing session, restate obvious
code, or leave references to removed iterations. Move long rationale to a maintained
document or tracker when appropriate. Keep meaningful external references accessible
to a reader with no conversation history.

A review comment needs the location, triggering condition, consequence, and evidence.
Explain an unobvious correction; keep style preferences separate from defects. Drafts
are not posted messages. Sources of stylistic heuristics, including AI-writing lists,
cannot prove authorship.

## Markdown and destinations

Follow the repository's format and language. Keep a coherent heading hierarchy, blank
lines around paragraphs and lists, language-labelled code fences, useful link text,
and a final newline. Use lists and tables when they clarify genuine sequences or
comparisons, not as decoration.

Front matter, callouts, raw HTML, footnotes, and a table of contents depend on the
consumer. A GitHub README and a Pandoc export need different choices. Do not add
conversion metadata or a fixed output directory to every document. Preserve structure
during a style-only pass; restructure only within scope.

## Compact governing documents

Keep each operative rule with its exceptions and evidence requirements. Remove
duplication without deleting constraints, failure handling, or authorization
boundaries. Compare meaning before and after compression; word-count reduction alone
is not success. Descriptions are routing metadata; long examples and runtime details
should load on demand.
