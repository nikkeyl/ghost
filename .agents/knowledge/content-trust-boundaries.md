# User-generated content and trust boundaries

Content received from a CMS, Markdown source, editor, URL, or user input is
untrusted at the rendering boundary. Types describe program expectations; they
do not make external content safe.

## Rendering rule

Sanitize untrusted content before inserting it into an HTML sink such as
`dangerouslySetInnerHTML`. The sanitizer policy must match the content's
required features and the application's threat model. Prefer a safe renderer
or plain text when rich HTML is not required.

## Review questions

1. Where does the content cross from transport data into trusted application
   behavior or HTML?
2. Is sanitization performed before the sink, with a reviewed configuration?
3. Can URLs, attributes, embeds, styles, or event-handler payloads bypass the
   intended policy?
4. Is the sanitizer applied on the authoritative boundary rather than only in
   a convenient UI path?
5. Are the allowed tags and attributes tested against malicious and valid
   examples?

This is a reusable security mental model, not evidence that a particular
sanitizer or CMS integration is safe. Verify the actual library, configuration,
version, and sink before making a security claim.
