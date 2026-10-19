# korlogg.com vs vaultaire.app

Written 2026-10-19. Ideas only: nothing here is implemented. Visible homepage changes are Amir's decision.

Sources: vaultaire.app home, /features/, /features/duress-mode/, /compare/, /compare/vaultaire-vs-keepsafe/, /guides/, /guides/hide-photos-iphone/, /scenarios/, /scenarios/partner-knows-iphone-passcode/ and /de/, fetched 2026-10-19. For korlogg.com: the built `index.html`, `de/index.html`, `de/ratgeber/kilometerpauschale-2026/index.html`, `assets/site.css`, and the live site via curl. Everything below is what I saw. Claims I could not confirm are marked.

## What the brief said vs what I saw on Vaultaire

| Claim in the brief | Seen |
|---|---|
| 12-feature grid | Yes. 12 cards, each linking to /features/<slug>/ (two marked Pro) |
| /features/ pages | Yes. One index page plus 12 long pages (Duress Mode is about 3,400 words, with Article, FAQPage and Speakable schema) |
| /compare/ pages | Yes. The index lists 16 competitors and the footer links 10. Each page has a feature table, a pricing table, "What X users complain about", references and an FAQ |
| Guides, scenarios | Yes. About 16+ guides (the "2026" how-to articles) and about 16+ first-person scenarios ("A coworker swiped into my private photos") |
| 32 languages | Yes. 31 language paths plus English, with 97 hreflang tags on the home page |
| CTAs in header, hero, mid-page and footer | Yes. `ct=web_header_nav`, `web_home` (hero and mid-page), `web_footer`, plus a per-page ct on every subpage (`web_f_duress_mode`, `web_c_vaultaire_vs_keepsafe`, `web_gb_…`) |
| QR code for desktop | Yes. A small "Vaultaire is an iPhone app" card with a QR code and an "or text me the link" `sms:` link. It is `hidden` by default and shown by JS, presumably on desktop |
| ct= tracking | Yes, through their own redirect `/go/app-store?ct=…&src=/`, which 302s to apps.apple.com with `pt=128498067` |
| Home FAQ | Yes. 11 questions, with FAQPage JSON-LD |

Also seen: a hero line with ★★★★★ "**4.7** on the App Store", plus `AggregateRating` 4.7 from **34 ratings** in the JSON-LD. Eight "featured on" badges from launch directories (toolfame, BigKr, ScrollLaunch, …), loaded as images from those other domains. No Smart App Banner meta tag. No testimonials, press quotes or user counts.

## Section by section

### Hero
- **Vaultaire:** the social-proof line comes first (rating and tech chips). Then a provocative headline that names the problem ("Your Hidden album isn't actually hidden"), a two-line subhead, one button, a trust line ("Free · No account · …") and an animated phone mockup made of SVG thumbnails.
- **Körlogg:** a plain promise headline ("Your mileage log for taxes – kept automatically."), the App Store badge and a real WebP screenshot with `fetchpriority="high"` and srcset. The headline is clearer about what the app does. It has no social-proof line and no problem framing.

### CTA placement
- **Vaultaire:** header "Get App" button, hero, mid-page after the emotional "Someone takes your phone" section, footer, and a closing CTA on every subpage.
- **Körlogg:** hero, end-of-page band and footer (`web_en_hero`, `web_en_end`, `web_en_footer`; DE adds `web_de_at`). Guides carry `ct=guide_<slug>`.
- **What Körlogg lacks:** a header button (the nav is Features, Help, Guides, Support) and a CTA in the middle of the page, between "What the exported log contains" and Pro.
- The Smart App Banner partly covers the header-button gap on iPhone Safari.

### Social proof
- **Vaultaire:** shows 4.7 / 34 ratings and launch-directory badges. The badges add little trust and cost eight third-party image requests.
- **Körlogg:** shows nothing, which is correct today. The iTunes lookup on 2026-10-19 returned:
  - SE: averageUserRating 5, userRatingCount **2**
  - DE: 0 ratings
- Two ratings are too few to show honestly. Displaying "5.0 ★" would mislead, and an AggregateRating built on 2 ratings invites a Google rich-result penalty if it looks curated.
- **Honest options now:** "Made in Sweden", "No account – your trips stay on your phone" (already on the page), "Rules for eight countries", "Updated for 2026 rates". Add a rating line only when one storefront has a meaningful count (for example 20 or more), filled in at build time from the lookup API, per storefront.

### Feature pages
- **Vaultaire:** every feature has its own indexable URL with long-form explanation, FAQ and CTA. Each URL is a landing page for a search query ("duress mode iphone").
- **Körlogg:** six feature cards in one homepage section (`/#features`). The only deep feature page is the iBeacon guide.
- **Natural candidates:**
  - automatic trip logging (how it detects driving, battery)
  - iBeacon per car
  - export (what the PDF/Excel contains)
  - odometer check
  - several cars and drivers
  - privacy (no account, own iCloud)
- The two highest-value ones are the exported log and beacons. People search "körjournal pdf" and "Fahrtenbuch Excel Vorlage".

### Comparison pages
- **Vaultaire:** 16 "Vaultaire vs X" pages. This is their biggest SEO surface.
- **Conflict for Körlogg:** `docs/competitor-notes.md` (2026-10-10) records the decision "no competitor named on our site". Named "vs" pages would reverse that. That is Amir's call, and the pages also carry legal and accuracy upkeep: their prices and features change.
- **Honest alternative that does not name anyone:** method comparisons, which are also what people actually search:
  - "Körjournal i app, Excel eller papper"
  - "Fahrtenbuch-App vs. Excel vs. Papier"
  - "Fahrtenbuch vs. 1-%-Regelung" (exists as a guide)
  - "Rittenregistratie app vs. Excel"
  - "Mileage app vs spreadsheet"

### FAQ
- **Vaultaire:** 11 questions, with FAQPage schema.
- **Körlogg:** 6 `<details>` questions plus a link to the full Help page. The built home page carries **no FAQPage JSON-LD**: its only JSON-LD types are SoftwareApplication and Person. FAQPage exists on the guides.
- Adding FAQPage to the home pages (all 8 languages) is invisible and cheap. Google shows FAQ rich results mostly for authoritative sites now, but the markup still helps other search engines and AI answers parse the page.

### Navigation
- **Vaultaire:** the header has Features, How it works, Security, Compare and Tools, plus a CTA, a language picker and a theme toggle. The footer is a large sitemap: 12 feature links, 10 compare links and all languages.
- **Körlogg:** a sticky header with four links and a language picker. The footer has legal, support, help and guides links. Fine for today's page count. A larger footer link block only pays off once feature or method pages exist.

### Mobile layout
- Both are single-column on phones.
- **Körlogg:**
  - sticky blurred header
  - breakpoints at 600 to 1000px
  - responsive screenshot srcsets
  - dark-mode badges through `<picture>`
  - `prefers-reduced-motion` respected
  - Smart App Banner, which Vaultaire does not have
- **Vaultaire on phones:** the canvas animation and 18-thumbnail mockup are heavier. Its QR handoff only matters on desktop.
- **Desktop gap on Körlogg:** a desktop visitor (common for "Fahrtenbuch" searches made at work) gets an App Store badge that opens a web page, with no QR code or "send to my phone".

### Page-speed basics (home, measured 2026-10-19)

| | korlogg.com | vaultaire.app |
|---|---|---|
| HTML | 24.7 KB raw / 7.2 KB transferred | 88 KB raw |
| CSS | 1 file, 14 KB raw / 4.3 KB transferred | 2 files, 67 KB raw (preloaded) |
| JS | TelemetryDeck (0.7 KB) + stats.js (0.9 KB) | app.js 45 KB + Alpine 45 KB + an "openai-ads" script 2 KB, all `defer` |
| Fonts | system fonts, none loaded | Plus Jakarta Sans woff2 27 KB, preloaded |
| Images | WebP with srcset, lazy below the fold, hero 24 KB at 360w | SVG/PNG, plus 8 third-party badge images |
| Hosting | GitHub Pages, `max-age=600` | Cloudflare, `max-age=0, must-revalidate`, CSP/HSTS headers |

- **Körlogg is much lighter.**
- **One flaw:** the TelemetryDeck `<script>` in `<head>` has no `defer` or `async`. It is tiny but loaded from a third-party origin, so it blocks rendering until cdn.telemetrydeck.com answers. Adding `defer`/`async` is an invisible fix, but check that the `stats.js` events still fire after the SDK loads.

### Structured data

| Type | korlogg.com | Vaultaire |
|---|---|---|
| Home: SoftwareApplication | Yes | Yes |
| Home: Person | Yes | Yes |
| Home: FAQPage | No | Yes |
| Home: Offer | No | Yes |
| Home: AggregateRating | No | Yes |
| Home: HowTo | No | Yes |
| Home: WebSite | No | Yes |
| Home: Organization | No | Yes |
| Home: BreadcrumbList | No | Yes |
| Guides: Article, FAQPage, BreadcrumbList | Yes | Same, plus Speakable on feature and compare pages |

The worthwhile honest additions for Körlogg are FAQPage, WebSite and Organization. HowTo is no longer shown by Google and is optional. Offer needs care, because prices differ by storefront and subscription.

## What they do better
1. **Many entry points:** 12 feature pages, 16 compare pages, guides and scenarios. Each is a search landing page with its own CTA and per-page `ct=`.
2. **Their own redirect** (`/go/app-store?ct=…&src=<page>`) logs the source page and campaign in one place and allows server-side counting.
3. **Desktop-to-phone handoff:** a QR code plus "text me the link".
4. **A CTA in the header and in the middle of the page.**
5. **An emotional, problem-first hero and a "what if" section** ("Someone takes your phone. Now what?").
6. **Scenario pages** that answer real situations, not keywords.
7. **Home FAQ with FAQPage markup**, and a visible rating once they had 34 ratings.

## What we do better
1. **Speed:** about 7 KB of compressed HTML, no web fonts, no framework, WebP with srcset, and a real screenshot as the hero instead of an illustration.
2. **Smart App Banner** on every page. Vaultaire has none.
3. **Honesty:**
   - no directory badges
   - no claims we cannot back up
   - a sentence saying the tax office decides acceptance
   - sources on guides
4. **Tighter localisation:** each language shows its own rules, screenshots and campaign IDs (`web_de_*`), and the DE page addresses Austria.
5. **Cookieless analytics** with no third-party ad script. Vaultaire loads an "openai-ads" script and allows bzr.openai.com in its CSP.
6. **Guides tied to real tax numbers**, for example "Kilometerpauschale 2026 – 0,30 €/0,38 €" with sources.

## Prioritised changes (proposals only)

"Visible" means it changes what visitors see on a page that exists today and needs Amir's OK, per CLAUDE.md. "New pages" do not change existing screens but are still public and need his OK.

| # | Change | Effort | Impact | Visible? |
|---|---|---|---|---|
| 1 | Add FAQPage JSON-LD to all 8 home pages, built from the existing FAQ items in content.py | S | Med | No (markup only) |
| 2 | Add `defer`/`async` to the TelemetryDeck SDK script, then check that events still fire | S | Low–Med | No |
| 3 | Method-comparison pages without competitor names: "app vs Excel vs paper" in SE, DE, NL and EN, each with a per-page `ct=` | M | High | New pages |
| 4 | Feature pages for the exported log (with a sample PDF) and iBeacon per car, then automatic logging and privacy | M–L | High | New pages |
| 5 | Desktop-only QR card next to the hero badge ("Körlogg is an iPhone app – scan to install") | S | Med | **Yes, homepage** |
| 6 | "Get the app" button in the header (hidden when the Smart App Banner shows on iOS) | S | Med | **Yes, every page** |
| 7 | Mid-page CTA after "What the exported log contains" (`ct=web_xx_mid`) | S | Med | **Yes, homepage** |
| 8 | Scenario-style guides from real questions ("Skatteverket asks for my körjournal – what now?", "Finanzamt verwirft Fahrtenbuch", "500 km privé bewijzen", which already exists in NL) | M | Med–High | New pages |
| 9 | Build-time rating line, per storefront, shown only when the count passes a threshold (≥20), using real lookup data | S | Med later (nothing to show now: SE 2 ratings, DE 0) | **Yes, homepage**, when it triggers |
| 10 | WebSite and Organization JSON-LD ("Made in Sweden"; no indie wording) | S | Low | No |
| 11 | A `/go/app-store` redirect is not possible on GitHub Pages without JS. Keep direct links with `ct=` and `pt=` | — | — | — |
| 12 | Named "Körlogg vs X" pages: only if Amir reverses the 2026-10-10 "no competitor named" decision | L | Med | New pages |

**Not recommended:**
- directory "featured" badges
- star rows without a meaningful rating count
- an AggregateRating on 2 ratings
- copying Vaultaire's fear-led headline style. Körlogg's tax-saving angle ("What your business kilometres are worth") is already a stronger hook for this audience.
