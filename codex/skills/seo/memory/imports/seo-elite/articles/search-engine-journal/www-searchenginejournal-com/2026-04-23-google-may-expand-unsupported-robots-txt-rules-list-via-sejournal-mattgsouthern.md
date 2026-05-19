---
source: https://www.searchenginejournal.com/google-may-expand-unsupported-robots-txt-rules-list/572866/
title: Google May Expand Unsupported Robots.txt Rules List
scraped: 2026-04-24
tags: elite_article, seo, search-engine-journal, article_snapshot
topic: seo_article
intent: research, synthesis, source_selection
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Elite article harvest
use_for: article-level context, synthesis, deeper retrieval
avoid_for: exact verbatim quoting
---

# Google May Expand Unsupported Robots.txt Rules List

Source expert/publication: search-engine-journal
Source homepage: https://www.searchenginejournal.com/
Original URL: https://www.searchenginejournal.com/google-may-expand-unsupported-robots-txt-rules-list/572866/
Published: 2026-04-23

## Why This Matters
Google may expand its unsupported robots.txt rules list using HTTP Archive data and could broaden how it handles common misspellings of disallow. The post Google May Expand Unsupported Robots.txt Rules List appeared first on Search Engine Journal .

## Extracted Article Passages
- Google may expand its unsupported robots.txt rules list using HTTP Archive data and could broaden how it handles common misspellings of disallow.
- Google may expand the list of unsupported robots.txt rules in its documentation based on analysis of real-world robots.txt data collected through HTTP Archive.
- Gary Illyes and Martin Splitt described the project on the latest episode of Search Off the Record . The work started after a community member submitted a pull request to Google’s robots.txt repository proposing two new tags be added to the unsupported list.
- Illyes explained why the team broadened the scope beyond the two tags in the PR:
- Rather than add only the two tags proposed, the team decided to look at the top 10 or 15 most-used unsupported rules. Illyes said the goal was “a decent starting point, a decent baseline” for documenting the most common unsupported tags in the wild.
- The team used HTTP Archive to study what rules websites use in their robots.txt files. HTTP Archive runs monthly crawls across millions of URLs using WebPageTest and stores the results in Google BigQuery.
- The first attempt hit a wall. The team “quickly figured out that no one is actually requesting robots.txt files” during the default crawl, meaning the HTTP Archive datasets don’t typically include robots.txt content.
- After consulting with Barry Pollard and the HTTP Archive community, the team wrote a custom JavaScript parser that extracts robots.txt rules line by line. The custom metric was merged before the February crawl, and the resulting data is now available in the custom_metrics dataset in BigQuery.
- The parser extracted every line that matched a field-colon-value pattern. Illyes described the resulting distribution:
- Beyond those three fields, rule usage falls into a long tail of less common directives, plus junk data from broken files that return HTML instead of plain text.
- Google currently supports four fields in robots.txt. Those fields are user-agent, allow, disallow, and sitemap. The documentation says other fields “aren’t supported” without listing which unsupported fields are most common in the wild.
- Google has clarified that unsupported fields are ignored. The current project extends that work by identifying specific rules Google plans to document.
- The top 10 to 15 most-used rules beyond the four supported fields are expected to be added to Google’s unsupported rules list. Illyes did not name specific rules that would be included.
- Illyes said the analysis also surfaced common misspellings of the disallow rule:
- His phrasing implies the parser already accepts some misspellings. Illyes didn’t commit to a timeline or name specific typos.
- Search Console already surfaces some unrecognized robots.txt tags. If Google documents more unsupported directives, that could make its public documentation more closely reflect the unrecognized tags people already see surfaced in Search Console.

## Retrieval Use
- Use when the task maps to `search-engine-journal` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

