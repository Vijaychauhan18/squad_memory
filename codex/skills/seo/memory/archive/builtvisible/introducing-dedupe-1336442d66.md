---
source: https://builtvisible.com/introducing-dedupe-csv-a-command-line-tool-to-bulk-remove-duplicates/
title: Introducing dedupe
scraped: 2026-03-25
published_on: 2023-07-31
tags: live_feed, phase1_ingest, builtvisible, publication, seo-strategy, content, archive_backfill, historical_source
topic: seo_strategy
intent: research, monitoring, source_selection, strategy
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Builtvisible
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Introducing dedupe

Source: Builtvisible
Homepage: https://builtvisible.com/blog/
Original URL: https://builtvisible.com/introducing-dedupe-csv-a-command-line-tool-to-bulk-remove-duplicates/
Published: 2023-07-31
Strength: search strategy, content, technical SEO, digital PR, and modern search operations

## Summary
What is the dedupe-csv tool? Available on NPM, dedupe-csv is a command line tool that reads a CSV file, scans for duplicates and exports the unique entries to a new CSV. Based on Pandas’ drop_duplicates function, it provides a rich set of features with intuitive syntax and the convenience of a command line utility. How to […]

## Extracted Body
Available on NPM, dedupe-csv is a command line tool that reads a CSV file, scans for duplicates and exports the unique entries to a new CSV.

Based on Pandas’ drop_duplicates function , it provides a rich set of features with intuitive syntax and the convenience of a command line utility.

As with our last NPM module Pivot-Table-JS , make sure you’ve installed Node.js and then add the dedupe-csv package:

Once installed, the command line tool can be used from the terminal of your choosing, such as command prompt, PowerShell or Node.js command prompt on Windows; and iTerm2 or Terminal on Mac/Linux.

Just refer to the package name, followed by CSV file you wish to deduplicate:

It’s important to note that the file parameter must point to the file relative to where you are currently located within the terminal. For example, if your terminal’s root directory is Documents and your CSV file is in a subdirectory called project , you’ll need to specify the full path:

The command will start reading the file, look for identical rows/lines and remove duplicates, leaving you the first duplicate found. When finished, it will output your results to a new file, keeping the original file unedited.

If you want to fine-tune the way the tool finds duplicates, you can use the column option to select a specific header (or headers) for the evaluation.

Here, we have a CSV called data.csv , where the brand header has two duplicates, the style header has duplicates on all entries, and rating has no duplicates.

If we want to check for duplicates within the brand column only, we can run this command:

Which will produce a file called data_deduped.csv containing:

To evaluate based on a sequence of columns, add as many headers as you want, separated by commas.

In all these examples, we’ve been keeping the first entry found out of the duplicates. Instead, if we want to keep the last entry, we can specify the keep option.

It’s my hope that the SEO and wider digital marketing community find this module a useful addition to their toolkit.

If you have any questions about using the module or want to learn more about how Builtvisible build custom solutions to help businesses maximise their marketing spend, please get in touch .
