---
source: https://developers.google.com/search/docs/specialty/international/localized-versions
title: Tell Google about localized versions of your page
scraped: 2026-05-18
tags: google, official, hreflang, international_seo, localized_versions
topic: international_seo
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: hreflang, alternate language/region handling, and multilingual SEO implementation
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# Tell Google about localized versions of your page

Source type: official_doc
Original URL: https://developers.google.com/search/docs/specialty/international/localized-versions
Page updated label: 2025-12-22 UTC

## Why This Matters
hreflang, alternate language/region handling, and multilingual SEO implementation

## Extracted Passages
- If you have multiple versions of a page for different languages or regions, tell Google about these different variations. Doing so will help Google Search point users to the most appropriate version of your page by language or region.
- Note that even without taking action, Google might still find alternate language versions of your page, but it is usually best for you to explicitly indicate your language- or region-specific pages.
- Localized versions of a page are only considered duplicates if the main content of the page remains untranslated.
- The three methods are equivalent from Google's perspective and you can choose the method that's the most convenient for your site. While you can use all three methods at the same time, there's no benefit in Search (in fact, it maybe be much harder to manage three implementations instead of just picking one).
- Use hreflang to tell Google about the variations of your content, so that we can understand that these pages are localized variations of the same content. Google doesn't use hreflang or the HTML lang attribute to detect the language of a page; instead, we use algorithms to determine the language.
- Add lang_code "... > elements to your page header to tell Google all of the language and region variants of a page. This is useful if you don't have a sitemap or the ability to specify HTTP response headers for your site.
- For each variation of the page, include a set of elements in the element, one link for each page variant including itself . The set of links is identical for every version of the page. See the additional guidelines.
- The tags must be inside a well-formed section of the HTML. If in doubt, paste code from your rendered page into an HTML validator to ensure that the links are inside the element. Additionally, don't combine link tags for alternate representations of the document; for example don't combine hreflang annotations with other attributes such as media in a single tag.
- Example Widgets, Inc has a website that serves users in the USA, UK, and Germany. The following URLs contain substantially the same content, but with regional variations:
- Note that the language-specific subdomains in these URLs ( en , en-gb , en-us , de ) are not used by Google to determine the target audience for the page; you must explicitly map the target audience.
- Here is the HTML that would be in the section of all the pages listed in the URLs with regional variations table . It would direct US, UK, generic English speakers, and German speakers to localized pages, and all others to a generic home page. Google Search returns the appropriate result for the user, according to their browser settings.
- You can return an HTTP header with your page's GET response to tell Google about all of the language and region variants of a page. This is useful for non-HTML files (like PDFs).
- You must specify a set of , rel="alternate" , and hreflang values for every version of the page including the requested version , separated by a comma as shown in the following example. The Link: header returned for every version of a page is identical. See the additional guidelines.
- Here is an example Link: header returned by a site that has three versions of a PDF file: one for English speakers, one for German speakers from Switzerland, and one for all other German speakers:
- You can use an XML sitemap to tell Google all of the language and region variants for each URL. To do so, add a element specifying a single URL, with child entries listing every language/locale variant of the page including itself. Therefore if you have 3 versions of a page, your sitemap will have entries for the URLs of each version, and each entry will have 3 identical child entries.
- Here is an English language page targeted at English speakers worldwide, with equivalent versions of this page targeted at German speakers worldwide and German speakers located in Switzerland. Here are all the URLs present on your site:
- The hreflang attribute's value is comprised of one or optionally two values, separated by a dash. For example, en-US . The first code of the hreflang attribute is the language code (in ISO 639-1 format) followed by an optional second code that represents the region code (in ISO 3166-1 Alpha 2 format) of an alternate URL. Only language codes listed in ISO 639-1 and region codes listed in ISO 3166-1 Alpha 2 are supported; other codes that aren't listed in those standards, such as es-419, aren't supported.
- To target different language speakers in Belgium, you might use the following language and region codes:

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

