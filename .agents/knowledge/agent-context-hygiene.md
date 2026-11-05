# Agent context hygiene

Context cost depends on what the host actually loads. Inventory
instruction chains, skill descriptions, server instructions, tool
schemas, memory, and command output before recommending a reduction.
Host discovery and deferred tools are runtime-dependent; do not infer
their state from a source snapshot.

## Audit method

Record source, observed loading mode, size, relevance, and uncertainty.
Distinguish eager text from deferred schemas and merely linked
references. Measure bytes or words; label a token estimate unless the
actual tokenizer was used. A disabled deferred-loading mechanism can
change the cost order.

Rank changes by meaningful context saved, lost information, and
reversibility. Prefer a bounded read, focused query, compact output, or
on-demand reference before removing a useful capability. Preserve
authorization, validation, security, accessibility, and failure evidence
when reducing text.

Process large logs, structured files, and independent searches outside
the active context when tools permit. Return the selected facts with
source paths and scope. A summary cannot justify facts excluded from its
evidence. Delegate only when authorized, supported, and useful for
isolation or context.

## Durable knowledge and memory

Separate stable rules, source-derived knowledge, project conventions,
personal preferences, temporary state, and session history. Verify
drift-prone facts before promoting them. Propose the appropriate
user-controlled home and a scoped diff; keep useful context rather than
treating all memory as garbage.

Memory relocation, deletion, global settings, and plugin changes require
the relevant user authorization and access. An audit request by itself
authorizes analysis, not silent modification. Preserve a recovery path
for approved changes.

## Checkpoint contract

A fresh session should be able to recover the intended outcome, relevant
repository state, decisions, evidence, next step, and open risks. Use
the requirements, plan, and verification templates when that handoff is
needed; do not save raw session history or preload every linked
document.
