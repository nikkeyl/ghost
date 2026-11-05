# Web document metadata and discovery

This is a framework-neutral review aid for page identity, crawler
directives, localized URLs, social previews, structured data, and site
icons. Consumers interpret these signals differently; follow the current
documentation for the specific search engine, social platform, browser,
or application.

## Page identity

- Give each indexable page a descriptive title and a page-specific
  description that matches its visible content. Avoid keyword lists and
  invented facts.

- Do not impose a universal character limit. Search products can
  truncate, rewrite, or select title and snippet text from other page
  content; metadata does not guarantee a particular result, ranking, or
  click-through rate.

- A canonical URL identifies the preferred URL among duplicate or
  equivalent content. It is a signal to the consumer, not an
  access-control mechanism or an unconditional directive. Ensure it
  resolves successfully and represents equivalent primary content.

- Give a translated page its own canonical URL. Use language/region
  alternates only for real equivalent translations, with valid URLs and
  the reciprocal set required by the target consumer.

## Language, crawling, and access

- Set the document language with the appropriate lang value for
  assistive technologies and other user agents. This does not replace
  search-engine alternate-language annotations; some search engines
  identify language from page content rather than the lang attribute.

- Distinguish crawl permission from index directives. A robots.txt
  disallow can prevent a crawler from seeing a page-level noindex
  directive and does not reliably remove a known URL from search
  results.

- Use a supported noindex directive when a page should be excluded from
  a search index, and allow the target crawler to fetch the page so it
  can read that directive. Do not use metadata or robots.txt to protect
  confidential content; use authentication and authorization.

- Return appropriate HTTP status and redirect behavior for available,
  moved, and removed resources. A sitemap can aid discovery but does not
  guarantee crawling or indexing.

## Delivery and sharing

- Verify metadata in the actual response and rendered document for the
  consumers that matter. Do not assume every crawler or link-preview
  client runs the page's JavaScript. Use server or static delivery when
  the target consumer needs metadata before client rendering.

- Keep Open Graph values specific to the page being shared. Use
  `og:description` for a page summary and `og:image:alt` to describe the
  image itself. Use absolute, externally reachable image and page URLs.
  Preview caching and rendering vary by platform.

- Treat platform-specific card metadata as an adapter, not a universal
  social standard. Confirm current support with the target platform.

## Structured data and icons

- Add structured data only when its type fits the page and its
  properties accurately describe current, user-visible content. Do not
  invent optional values to satisfy a template. Valid syntax can
  establish eligibility, not guarantee a rich result.

- Treat a web app manifest, browser favicon, and platform-specific
  home-screen icon as distinct mechanisms. Add install-related
  configuration only when that application scenario is supported; test
  the icon selection on the target platforms.

## Verification

For representative routes and locales, inspect the HTTP response, final
rendered head, status/redirect behavior, canonical and alternate URL
graph, robots directives, and sitemap entries. Validate structured data
against the consumer's current tool and content policies. Inspect social
previews and icons in the platforms the product actually supports.
Record that these checks show technical configuration, not guaranteed
indexing or presentation.

## Primary references

- [Google title links](https://developers.google.com/search/docs/appearance/title-link)
- [Google snippets and meta descriptions](https://developers.google.com/search/docs/appearance/snippet)
- [Google canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google robots meta directives](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
- [Google multilingual sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)
- [Google structured-data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- [Google favicon guidance](https://developers.google.com/search/docs/appearance/favicon-in-search)
- [Open Graph protocol](https://ogp.me/)
- [WHATWG HTML image requirements](https://html.spec.whatwg.org/multipage/embedded-content.html)

Last checked against the linked platform guidance: 2026-09-26.
