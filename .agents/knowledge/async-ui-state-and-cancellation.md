# Async UI state and cancellation

This mental model covers user-driven asynchronous work such as search,
filtering, load-more, and modal data fetching. It explains the mechanisms; it
does not require one framework or one request library.

## Debounce

Debounce delays work until calls stop for a defined interval. It is useful for
high-frequency input such as search because it avoids starting one request per
keystroke. The delay is a UX trade-off: a longer delay reduces request volume
but makes results feel less immediate.

## AbortController

`AbortController` provides a cancellation signal that can be passed to
`fetch`. Aborting causes the client-side fetch promise to reject, commonly with
an `AbortError`, so the caller can stop waiting for work that is no longer
relevant. It may save client and network resources, but it does not guarantee
that a server has stopped processing a request that already reached it.

Handle intentional cancellation separately from a real failure, and do not
assume that cancellation alone prevents every stale update. A request identity,
sequence number, or equivalent freshness check may still be needed when
multiple operations can complete out of order.

## Freshness and caching

An uncached read can be appropriate when stale data breaks behavior, such as a
current availability or a mutation-sensitive modal. It also increases latency
and server load, so freshness should be an explicit contract rather than a
reflexive setting.

## Review questions

1. Can repeated input be debounced without harming the interaction?
2. Can obsolete work be cancelled, and is cancellation distinguished from
   failure?
3. Can responses arrive out of order, and what prevents a stale response from
   replacing newer state?
4. Does the operation require fresh data, or would a cache provide a better
   latency and load profile?
