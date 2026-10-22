# korlogg.com

Static site for Körlogg (plain HTML/CSS, no JS, no cookies). Served by GitHub Pages from `main` (repo root).

- Edit copy: `tools/content.py`, guides `src/guides/`, legal texts `src/legal/<lang>/`.
- Körlogg 2.0 wording: set `KORLOGG_2_0_RELEASED = True` in `tools/config.py` when 2.0 is released.
- Rebuild: `python3 tools/build.py` (writes the HTML into the repo root), then `python3 tools/check.py --external`.
- Scheduled guides: `<!-- publish: YYYY-MM-DD -->`; deployed by `.github/workflows/publish.yml` (push + Tue/Fri 05:00 UTC). See `docs/CONTENT_QUEUE.md`.
- Help/FAQ comes from the app: `python3 tools/extract_help.py <git-ref>`; images: `python3 tools/images.py`.
- Screenshots of the home pages: serve with `python3 -m http.server 8766 --bind 127.0.0.1`, then `python3 tools/screens.py`.
- Search engines: Google Search Console (alagic.se@gmail.com, domain property) and Bing Webmaster Tools (meta tag msvalidate.01) have the sitemap. IndexNow (`tools/indexnow.py`, key file in the root) pings Bing after every deploy: changed pages on push, new guides on their publish day. `--all` resubmits everything.
