# Content review queue

The sitemap lists 213 city guides and 19 navigation/editorial pages. The other
HTML files remain reachable from site links but are held out of the sitemap
pending review. Sitemap omission alone does not prevent search indexing.

## Review before promotion

1. **310 podcast proposals:** Several sampled pages say "Verified" and
   "Reviewed July 2026" and describe interviews, although the format is a
   proposal. Confirm each interview took place; otherwise label it as a
   proposed interview and remove unsupported verification claims.
2. **213 short city comparison matrices:** The sampled Bangkok page has only
   116 visible words and presents costs and a safety score without sources.
   Merge useful comparisons into a city guide or expand with dated, sourced
   methodology and a distinct reason to exist.
3. **45 generated city-pair comparisons:** Check source and date for every
   numeric comparison, and add insight specific to the pair before promotion.

Start with pages that have real firsthand reporting or measurable reader
demand. Promote an individual page only after checking its claims, canonical,
unique content, and internal links. Update `generate_sitemap.py` deliberately
to include reviewed pages, rather than reverting to a wildcard of every HTML
file. Never set `lastmod` to the day of sitemap generation unless that page
actually changed.
