# Tool integration candidates

This is an on-demand inventory derived from a supplied setup, not evidence that these
tools are installed, current, or compatible in an adopting host. The engineering core
must continue to work without them.

| Candidate         | Potential role                                                     | Evidence needed before adoption                                                       |
| ----------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| context-mode      | bounded execution, indexed retrieval, session continuity           | supported host, actual routing, output fidelity, recovery and retention behavior      |
| CC Safety Net     | deterministic checks around risky tool effects                     | supported tool surfaces, active policy, false positives, bypass and failure behavior  |
| RTK               | compact CLI output                                                 | supported commands and preservation of exit codes, errors, and relevant evidence      |
| code-review-graph | repository relationships for exploration and review                | language coverage, graph freshness, caller accuracy, and incremental cost             |
| open-websearch    | external search and retrieval through an available CLI or MCP path | actual tool availability, retrieval, source attribution, network and activation state |

## Adoption checklist

1. Name the problem and compare the tool with existing host or project capability.
2. Inspect the current version, license, support matrix, and configuration contract.
3. Define the smallest integration, permitted effects, and reversal procedure.
4. Verify the relevant operation, not merely installation or written settings.
5. Report active, configured but awaiting activation, unavailable, or failed.

Hooks, MCP transport, deferred tools, and projections belong in runtime adapters.
They do not replace evidence-based engineering decisions or an OS-enforced isolation
boundary. An integration's security claim needs its own verification.

Do not import account state, permission-bypass settings, fixed model choices,
container paths, credentials, or runtime databases as portable defaults. Copied
self-healing hooks need a separately reviewed state and failure model; their presence
in a setup is not reason to patch a plugin automatically.
