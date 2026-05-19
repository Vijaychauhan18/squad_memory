---
source: https://www.seroundtable.com/google-ads-api-version-24-41204.html
title: Google Ads API Version 24 Now Available
scraped: 2026-04-27
tags: elite_article, seo, seroundtable, article_snapshot
topic: seo_article
intent: research, synthesis, source_selection
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Elite article harvest
use_for: article-level context, synthesis, deeper retrieval
avoid_for: exact verbatim quoting
---

# Google Ads API Version 24 Now Available

Source expert/publication: seroundtable
Source homepage: https://www.seroundtable.com/
Original URL: https://www.seroundtable.com/google-ads-api-version-24-41204.html
Published: 2026-04-23

## Why This Matters
Google has released version 24 of the Google Ads API, this is a major release with dozens of updates. This update includes changes to Demand Gen, travel feeds, conversion types, shopping, reporting, videos, and much more.

## Extracted Article Passages
- Google has released version 24 of the Google Ads API, this is a major release with dozens of updates. This update includes changes to Demand Gen, travel feeds, conversion types, shopping, reporting, videos, and much more.
- Before this release was version 23.2 in March, then v23.1 in February and then 23 at the end of January, then version 22 on October 15, 2025, then version 21 on August 6, 2025 , then 20 on June 5, 2025, 19.1 in April 2025, then 19 in February 2025, then version 18 in October 2024. Before that was 17.1 in August 2024 and then before that was version 17.0 in June 2024 and then before that was version 16.1 and then Version 16 in February 2024. Before that was version 15 back in October 2023. Then before that was version 14.1 which was released in August. Version 13.1 preceded this new version, which was released in April 2023. Version 13 was released in February 2023. Version 12.0 was released in October 2022, Version 11.0 of the Google Ads API was released in June, and version 11.1 was in August. Also Version 10.1 was released on April 27, 2022 and version 10.0 was released on February 9, 2022. And Google has sunset the AdWords API on April 27th which will completely stop working at the end of July .
- Ads: The following fields are now required: In the DemandGenVideoResponsiveAdInfo object: videos, logo_images In the VideoResponsiveAdInfo object: videos, business_name, logo_images The VideoResponsiveAdInfo is now mutable.
- Added the field travel_feed_data to the AssetSet resource. This new field allows reading travel feed data from a travel feed asset set, exposing read-only information such as hotel_center_account_id, merchant_center_id, partner_center_id, subset_id, and travel_feed_vertical_type.
- Removed the Campaign.video_brand_safety_suitability field. The control is still available on the Customer level. See Customer.video_brand_safety_suitability. Added the Campaign.view_through_conversion_optimization_enabled field, which is false by default, to allow enabling VTC (View-Through Conversion) Optimization in Demand Gen and App Campaigns. Enabled gender exclusions for Performance Max campaigns. This exclusion is now available for Performance Max campaigns on all Google Ads API versions.
- Added support for Lead Gen conversion types. These are the new ConversionActionType. enums in v24: Removed the LOYALTY_SIGN_UPS user list customer type category.
- Added UserListErrorEnum.DUPLICATE_LOOKALIKE, which is returned when attempting to create a lookalike UserList that is identical to an existing one.
- Changed the InsightsAudience.topic_audience_combinations type definition from InsightsAudienceAttributeGroup to common.InsightsAudienceAttributeGroup. For typed client libraries, this is a breaking change and requires updates to existing integrations. Removed the youtube_select_lineups field from the ReachPlanService.ListPlannableProducts service. Users should switch to using lineups from youtube_select_lineup_targeting. Removed the is_brand_connect_creator field from the ContentCreatorInsightsService.GenerateCreatorInsights and ContentCreatorInsightsService.GenerateTrendingInsights services. Users should instead look for a creator to have the CREATOR_PARTNERSHIPS option available instead in partnership_opportunities. Added new fields to the ReachPlanService.ListPlannableProducts response to include more details about each plannable product. Most of these fields are returned in the new ProductCoreAttributes field within ListPlannableProductsResponse. New response fields are... Removed various fields from KeywordPlanIdeaService.GenerateKeywordForecastMetrics:
- Removed the ad_sub_network_type segment for the campaign_budget resource. Removed the click_type segment from the AdGroupAsset, CampaignAsset, and CustomerAsset views. Added a new resource CartDataSalesView. It allows segmenting conversion metrics not only by the product clicked, but also by the product sold, with segments like product_sold_brand. Added non-biddable metrics, which are metrics that also include the conversions your campaigns are not actively optimizing towards, for example all_cost_of_goods_sold_micros. The new metrics are added to all resources supporting corresponding biddable metrics. Added the conversion_attribution_event_type segment to the ShoppingPerformanceView resource.
- Added support for App campaigns in the ShoppingProduct resource. Note that the status and issues fields are not supported for App campaigns. Introduced tag-based product filtering using logical expressions for Shopping Campaigns.
- Updated ShareablePreviewService.GenerateShareablePreviews to not use partial failure anymore. Requests will throw an error if they fail for any ID. Returning new error codes for asset groups to align with ad group ad errors:
- The content at the Search Engine Roundtable are the sole opinion of the authors and in no way reflect views of RustyBrick ®, Inc Copyright © 1994-2026 RustyBrick ® , Inc. Web Development All Rights Reserved. This work by Search Engine Roundtable is licensed under a Creative Commons Attribution 3.0 United States License. Creative Commons License and YouTube videos under YouTube's ToS .

## Retrieval Use
- Use when the task maps to `seroundtable` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

