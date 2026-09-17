# Next.js Server Actions

This is a framework-specific mental model. Apply it only in a Next.js
repository that supports the relevant Server Actions behavior.

## Appropriate use

Prefer a Server Action for a server-side mutation when it gives the operation
a clear server boundary and avoids an unnecessary hand-written endpoint. It is
especially suitable for form submissions and mutations that need server-side
validation, authorization, and access to private resources.

## Boundaries

Server Actions do not make client interaction state disappear. The client may
still need pending, optimistic, validation, retry, and success states. Keep
browser APIs, high-frequency input handling, and rich local interaction logic
on the client when the user experience requires them.

Validate and authorize inside the action. A client-side constraint or a typed
payload is a UX aid, not a trust boundary.

## Decision rule

Use the simplest server boundary that preserves the operation's contract. A
Server Action is a preference for suitable mutations, not a reason to move
browser-only work or every read operation to a server action.
