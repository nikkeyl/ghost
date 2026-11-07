---
description: Review route-level document metadata, indexing directives,
  localized URL relationships, social previews, and structured data.
kind: active
name: review-metadata-strategy
---

# Review a metadata strategy

## Trigger

Use when creating or changing page metadata, route indexability,
canonical URLs, localized page relationships, social previews,
structured data, site icons, or web-app manifests.

## Goal

Make each page's identity and metadata delivery explicit for its
intended consumers without promising search ranking, indexing, rich
results, or a particular social preview.

## Investigation / reasoning

1. Enumerate affected page types, route patterns, locale variants, and
   which pages are intended to be indexable.

1. Find the source of truth for route data and metadata generation.
   Inspect the HTTP response, redirects, server/static output, and
   post-render document.

1. Build a route/locale matrix for title, description, canonical,
   document language, alternate-language URLs, crawler directives, Open
   Graph data, structured data, and icons/manifests where applicable.

1. Identify the intended search engines, social platforms, browsers, and
   app installation scenarios. Their metadata support and rendering
   behavior may differ.

## Decision rules

- Make titles and descriptions descriptive, page-specific, and
  consistent with visible content. Do not prescribe a universal
  character limit.

- Point canonical URLs to accessible pages with equivalent primary
  content. Keep translated pages canonical to their own language version
  and connect true variants with the target search engine's supported
  alternate-language mechanism.

- Do not confuse crawl permission with index exclusion. A crawler must
  be able to fetch a page to read a page-level noindex directive;
  robots.txt is not a privacy boundary.

- Set document language for the actual page content and assistive
  technology. Do not treat lang as a substitute for localized URL
  annotations.

- Deliver metadata at a boundary that the target consumer can read.
  Verify the actual response and rendered result instead of assuming
  client JavaScript will be executed by every crawler or preview
  generator.

- Keep social metadata accurate for the page and use only
  platform-specific fields required by the target. Preview behavior and
  caching are not guaranteed.

- Add structured data only for a fitting type and facts that are current
  and visible to users. Syntax validity does not guarantee a rich
  result.

- Add manifests and platform-specific icons only for supported
  application scenarios; do not imply that a manifest guarantees
  installability.

## Actions

Produce a compact route/locale metadata matrix, identify conflicting or
missing values and the delivery boundary, and implement only the
smallest route-aware change. Separate consumer-specific metadata from
framework-neutral rules.

## Verification

Inspect representative HTTP responses and final rendered documents.
Check status and redirects, uniqueness and accuracy of
titles/descriptions, canonical destinations, reciprocal localized
alternates, crawler directives, and sitemap consistency. Validate
structured data and inspect social previews and icons in the intended
target tools/platforms. Report technical validity separately from
indexing, ranking, and preview outcomes.

## Completion criteria

Affected routes and locales have an explicit metadata contract, values
are delivered to their intended consumers, verification covers response
and rendered output, and no platform outcome is claimed beyond the
observed evidence.

## Graph

```yaml
followed-by: [verify-before-claiming]
may-trigger: [estimate-blast-radius]
references: [web-document-metadata]
requires: [plan-code-change]
```
