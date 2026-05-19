---
source: https://developers.google.com/search/docs/appearance/google-images
title: Google image SEO best practices
scraped: 2026-05-18
tags: google, official, image_seo, images, search_appearance
topic: image_seo
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: image discoverability, image SEO, and image-search presentation guidance
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# Google image SEO best practices

Source type: official_doc
Original URL: https://developers.google.com/search/docs/appearance/google-images
Page updated label: 2026-03-02 UTC

## Why This Matters
image discoverability, image SEO, and image-search presentation guidance

## Extracted Passages
- Google provides several Search features and products that help users visually discover information on the web, such as the text result images , Google Discover, and Google Images. While each feature and product looks different, the general recommendations for getting images to appear in them is the same.
- You can optimize your images to appear in Google's search results by following these best practices:
- The technical requirements for getting your content in Google's search results applies to images too. Since images are a substantially different format compared to HTML, it means there are additional requirements for getting images indexed; for example, finding the images on your site is different, and the presentation of the images also influences whether an image is indexed at all, and for the right keywords.
- Using standard HTML image elements helps crawlers find and process images. Google can find images in src attribute of element (even when it's a child of other elements, such as the element). Google doesn't index CSS images.
- You can provide the URL of images we might not have otherwise discovered by submitting an image sitemap .
- Unlike regular sitemaps, you can include URLs from other domains in the elements of the image sitemaps. This lets you use CDNs (content delivery networks) to host images. If you're using a CDN, we encourage you to verify ownership of the CDN's domain name in Search Console so that we can inform you of any crawl errors that we may find.
- Designing responsive web pages leads to better user experience, since people can access them across a plethora of device types. Refer to our guide to responsive images to learn about the best practices for handling images on your website.
- Web pages use the element or the srcset attribute of an img element to specify responsive images. However, some browsers and crawlers don't understand these attributes. We recommend that you always specify a fallback URL using the src attribute.
- The srcset attribute allows specifying different versions of the same image, specifically for different screen sizes. For example:
- The element is a container that is used to group different versions of the same image. It offers a fallback approach so the browser can choose the right image depending on device capabilities, like pixel density and screen size. The picture element also comes in handy for using new image formats with built-in graceful degradation for clients that may not yet support the new formats.
- Per section 4.8.1 of the HTML Standard , make sure that you provide an img element as a fallback with a src attribute when using the picture element using the following format:
- Google Search supports images referenced in the src attribute of img in the following file formats: BMP, GIF, JPEG, PNG, WebP, SVG, and AVIF. It's also a good idea to have the extension of your filename match with the file type.
- You can also inline images as Data URIs. Data URIs provide a way to include a file, such as an image, inline by setting the src attribute of an img element as a Base64-encoded string using the following format:
- While inlining images can reduce HTTP requests, carefully judge when to use them since it can considerably increase the size of the page. For more on this, refer to the section on the advantage and disadvantages of inlining images on our web.dev page .
- High-quality photos appeal to users more than blurry, unclear images. Also, sharp images are more appealing to users in the result thumbnail and can increase the likelihood of getting traffic from users. That said, images are often the largest contributor to overall page size, which can make pages slow and expensive to load. Make sure to apply the latest image optimization and responsive image techniques to provide a high quality and fast user experience.
- Analyze your site speed with PageSpeed Insights and visit our Why does speed matter? to learn about best practices and techniques to improve website performance.
- While not immediately obvious, the content and metadata of the pages where an image is embedded can have a great influence on how and where the image may appear in Google's search results.
- Google's selection of an image preview is completely automated and takes into account a number of different sources to select which image on a given page is shown on Google (for example, a text result image or the preview image in Discover).

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

