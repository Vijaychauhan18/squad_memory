---
source: https://dejan.ai/blog/otsu/
title: Dynamic per-label thresholds for large
scraped: 2026-03-25
published_on: 2025-07-09
tags: live_feed, phase1_ingest, dejan, practitioner, reverse-engineering, grounding, archive_backfill, historical_source
topic: ai_reverse_engineering
intent: research, monitoring, source_selection, ai_selection
role: researcher, seo, pinchy
confidence: high
canonical: false
canonical_group: Archive backfill - DEJAN / Dan Petrovic
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Dynamic per-label thresholds for large

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/otsu/
Published: 2025-07-09
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Solving the “Which Score Is Good Enough?” Puzzle The real-world problem Arbitrary label search-query intent classifiers spit out a confidence score per label.On clean demos you set one global cut-off say 0.50 and move on.In production: Manual tuning per label quickly turns into a never-ending whack-a-mole, especially when the taxonomy is customized client-by-client (e.g., SaaS […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Arbitrary label search-query intent classifiers spit out a confidence score per label. On clean demos you set one global cut-off say 0.50 and move on. In production:

Manual tuning per label quickly turns into a never-ending whack-a-mole, especially when the taxonomy is customized client-by-client (e.g., SaaS today, Gaming tomorrow).

data = [ (“LOCAL”, 0.9697265625), (“PRODUCT”, 0.83837890625), (“CATEGORY”, 0.39892578125), (“TRANSACTIONAL”, 0.09222412109375), (“INFORMATIONAL”, 0.000947475433349609), (“PROMO”, 0.00080108642578125), (“BRANDED”, 0.00034332275390625), (“SUPPORT”, 0.000284671783447266), (“NAVIGATIONAL”, 0.000205039978027344), ]

Well that’s easy you might say. It’s quite obvious we can set threshold to 0.4 and that sets LOCAL, PRODUCT and CATEGORY. We miss TRANSACTIONAL but otherwise keep the floodgates of irrelevant stuff out for other labels at that threshold value.

data = [ (“PRODUCT”, 0.84423828125), (“CATEGORY”, 0.31689453125), (“SUPPORT”, 0.00284576416015625), (“TRANSACTIONAL”, 0.000590801239013672), (“PROMO”, 0.000458240509033203), (“BRANDED”, 0.00039362907409668), (“INFORMATIONAL”, 0.000348806381225586), (“LOCAL”, 0.000211477279663086), (“NAVIGATIONAL”, 0.000198721885681152), ]

We’ll just use the same threshold. Right? Wrong! You now have to lower it to 0.3 to include the CATEGORY label. This is because all labels have different and inconsistent confidence thresholds.

Otsu’s algorithm (1979) was built for image segmentation: find the gray-level that best separates foreground and background by maximizing between-class variance .

Picture your label-scores as a mountain range drawn by a histogram:

Otsu simply slides a vertical ruler across that landscape, computes how well the left side and right side each cluster, and stops at the deepest point of the valley, the most natural dividing line. That valley score becomes the dynamic threshold for that label.

scores are that label’s confidences across the full corpus. Recalculate thresholds every time you re-score so they drift with model upgrades or seasonal traffic changes.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
