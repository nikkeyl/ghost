# User-generated content and trust boundaries

Content received from a CMS, Markdown source, editor, URL, or user input is untrusted
at the rendering boundary. Types describe program expectations; they do not make
external content safe.

## Rendering rule

Sanitize untrusted content before inserting it into an HTML sink such as
`dangerouslySetInnerHTML`. The sanitizer policy must match the content's required
features and the application's threat model. Prefer a safe renderer or plain text
when rich HTML is not required.

## URL behavior

Treat a URL from a CMS, editor, external API, or user input as untrusted when placing
it in a navigation or resource attribute. Parse and validate it at the boundary
against the schemes and destinations the feature actually needs. Reject unexpected
schemes rather than assuming that an escaped or type-checked string is a safe URL. If
a feature only permits same-origin destinations, validate the resolved origin as well
as the syntax.

## Review questions

1. Where does the content cross from transport data into trusted application behavior
   or HTML?
2. Is sanitization performed before the sink, with a reviewed configuration?
3. Are URL schemes and destinations constrained to what the feature needs?
4. Can attributes, embeds, styles, or event-handler payloads bypass the intended
   policy?
5. Is sanitization and URL validation performed at the authoritative boundary rather
   than only in a convenient UI path?
6. Are allowed tags, attributes, schemes, and destinations tested against malicious
   and valid examples?

This is a reusable security mental model, not evidence that a particular sanitizer or
CMS integration is safe. Verify the actual library, configuration, version, and sink
before making a security claim.
