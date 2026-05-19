---
source: https://developers.google.com/search/docs/appearance/title-link
title: Influencing your title links in search results
scraped: 2026-05-18
tags: google, official, title_links, snippets, search_appearance
topic: title_links
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: title-link generation, rewrite behavior, and title control guidance
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# Influencing your title links in search results

Source type: official_doc
Original URL: https://developers.google.com/search/docs/appearance/title-link
Page updated label: 2025-12-10 UTC

## Why This Matters
title-link generation, rewrite behavior, and title control guidance

## Extracted Passages
- A title link is the title of a search result on Google Search and other properties (for example, Google News) that links to the web page. Google uses a number of different sources to automatically determine the title link, but you can indicate your preferences by following our best practices for influencing title links .
- Title links are critical to giving users a quick insight into the content of a result and why it's relevant to their query. It's often the primary piece of information people use to decide which result to click, so it's important to use high-quality title text on your web pages.
- One solution is to dynamically update the element to better reflect the actual content of the page. For example, include the words "video" and "lyrics" only if that particular page contains video or lyrics.
- Google's generation of title links on the Google Search results page is completely automated and takes into account both the content of a page and references to it that appear on the web. The goal of the title link is to best represent and describe each result.
- Keep in mind that Google has to recrawl and reprocess the page to notice updates to these sources, which may take a few days to a few weeks. If you've made changes, you can request that Google recrawl your pages .
- While we can't manually change title links for individual sites, we're always working to make them as relevant as possible. You can help improve the quality of the title link that's displayed for your page by following the best practices .
- Here are the most common issues we see with title links in search results. To avoid these issues, follow the best practices for influencing title links .
- Google Search looks at information in header elements or other large and prominent text on the page to produce a title link:
- When the same page is used year-after-year for recurring information, but the element didn't get updated to reflect the latest date. For example:
- In this example, the page has a large, visible title that says "2021 admissions criteria", and the element wasn't updated to the current date. Google Search may detect this inconsistency and uses the right date from the visible title on the page in the title link:
- When the elements don't accurately reflect what the page is about. For example, the page could have dynamic content with the following element:
- Google Search tries to determine if the element isn't accurately showing what a page is about. Google Search might modify the title link to better help users if it determines that the page title doesn't reflect the page content. For example:
- When there are repeated boilerplate text in elements for a subset of pages within a site. For example, a television website has multiple pages that share the same element that omits the season numbers, and it's not clear which page is for what season. That produces duplicate elements like this:
- Google Search can detect the season number used in large, prominent title text and insert the season number in the title link:
- When there's more than one large, prominent heading, and it isn't clear which text is the main title of the page. For example, a page has two or more headings that use the same styling or heading level. If Google Search detects that there are multiple large, prominent headings, it may use the first heading as the text for the title link. Consider ensuring that your main heading is distinctive from other text on a page and stands out as being the most prominent on the page (for example, using a larger font, putting the title text in the first visible element on the page, etc).
- When the writing system or language of the text in elements doesn't match the writing system or language of the primary text on a page. For example, when a page is in written in Hindi, but the title includes text in English or is transliterated into Latin characters. If Google detects a mismatch, it may generate a title link that better matches the primary content. Consider ensuring that the script and language matches what is most prominent on the page.
- In the case of domain-level site names, Google may omit the site name from the title link, if it's repetitive with the site name that's already shown in the search result .
- If you're seeing your pages appear in the search results with modified title links, check whether your page has one of the issues that Google adjusts for. If not, consider whether the title link in search results is a better fit for the query. To discuss your pages' title links and get feedback about your pages from other site owners, join our Google Search Central Help Community .

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

