---
source: https://developers.google.com/search/docs/crawling-indexing/special-tags
title: meta tags and attributes that Google supports
scraped: 2026-05-18
tags: google, official, meta_tags, snippets, notranslate
topic: meta_tags
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: Google-supported meta tags and presentation controls
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# meta tags and attributes that Google supports

Source type: official_doc
Original URL: https://developers.google.com/search/docs/crawling-indexing/special-tags
Page updated label: 2025-12-10 UTC

## Why This Matters
Google-supported meta tags and presentation controls

## Extracted Passages
- This page explains what meta tags are, which meta tags and HTML attributes Google supports to control indexing, and other important points to note when implementing meta tags on your site.
- meta tags are HTML tags used to provide additional information about a page to search engines and other clients. Clients process the meta tags and ignore those they don't support. meta tags are added to the section of your HTML page and generally look like this:
- If you use a CMS, such as Wix, WordPress, or Blogger , you might not be able to edit your HTML directly, or you might prefer not to. Instead, your CMS might have a search engine settings page or some other mechanism to tell search engines about meta tags.
- If you want to add a meta tag to your website, search for instructions about modifying the of your page on your CMS (for example, search for "wix add meta tags").
- In the case of conflicting robots (or googlebot ) meta tags, the more restrictive tag applies. For example, if a page has both the max-snippet:50 and nosnippet tags, the nosnippet tag will apply.
- The default values are index, follow and don't need to be specified. For a full list of values that Google supports, see the list of valid rules .
- You can also specify this information in the header of your pages using the X-Robots-Tag HTTP header rule. This is particularly useful if you wish to limit indexing of non-HTML files like graphics or other kinds of documents. More information about robots meta tags .
- When Google recognizes that the contents of a page aren't in the language that the user likely wants to read, Google may provide a translated title link and snippet in search results. If the user clicks the translated title link, all further user interaction with the page is through Google Translate, which will automatically translate any links followed. In general, this gives you the chance to provide your unique and compelling content to a much larger group of users. However, there may be situations where this is not desired. This meta tag tells Google that you don't want us to provide a translation for this page.
- Prevents various Google text-to-speech services from reading aloud web pages using text-to-speech (TTS).
- You can use this tag on the top-level page of your site to verify ownership for Search Console . Note that while the values of the name and content attributes must match exactly what is provided to you (including upper and lower case), it doesn't matter if you change the tag from XHTML to HTML or if the format of the tag matches the format of your page.
- These tags define the page's content type and character set respectively. Make sure that you surround the value of the content attribute in the http-equiv meta tag with quotes—otherwise the charset attribute may be interpreted incorrectly. We recommend using Unicode/UTF-8 where possible.
- This tag, commonly called meta-refresh, sends the user to a new URL after a certain amount of time, and is sometimes used as a simple form of redirection. However, it is not supported by all browsers and can be confusing to the user . We recommend using a server-side 301 redirect instead.
- This tag tells the browser how to render a page on a mobile device. Presence of this tag indicates to Google that the page is mobile friendly. Read more about how to configure the viewport meta tag.
- Labels a page as containing sexually-explicit adult content, to signal that it be filtered by SafeSearch results. Learn more about labeling SafeSearch pages.
- HTML tag attributes are additional values of HTML tags that configure the parent tag. For example, the href attribute of the tag configures the resource the anchor tag points to: href="https://example.com/" ...> .
- Google Search supports a limited number of HTML attributes for indexing purposes. Attributes like src and href are used for discovering resources such as images and URLs. Google also supports various rel attributes that allow site owners to qualify outbound links.
- The data-nosnippet attribute of div , span , and section tags allow you to exclude parts of an HTML page from snippets.
- The following tags and attributes aren't supported by Google Search and are ignored. We're including them here because they're either very common in HTML or we used to support them.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

