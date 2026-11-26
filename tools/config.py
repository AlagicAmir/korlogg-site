"""Site-wide switches. Edit here, run `python3 tools/build.py`, commit, push."""

# ---------------------------------------------------------------------------
# Körlogg 2.0 (iBeacon) wording.
# False: iBeacon sections say "New in Körlogg 2.0 – coming soon" and the
#        iBeacon screenshots stay out of the main gallery.
# True:  they say "New in Körlogg 2.0 – available now" and the iBeacon
#        screenshots join the gallery.
# Flip to True the day Amir releases 2.0 in App Store Connect.
# ---------------------------------------------------------------------------
KORLOGG_2_0_RELEASED = True
# The UK edition ships in 2.0.2. Until then the English pages keep the 2.0
# screenshots (the 2.0.2 English set shows the UK edition).
UK_RELEASED = True

SITE = "https://korlogg.com"
APP_ID = "6809322275"
# App Store Connect provider ID: campaign links (pt=…&ct=…) count downloads per
# button in App Analytics → Acquisition → Campaigns. Not secret.
PROVIDER_ID = "127865703"

# Custom product pages in the App Store (own screenshots and promotional text for
# Switzerland and Austria; ids from App Store Connect, Körlogg docs/CUSTOM_PRODUCT_PAGES.md).
# Sent to App Review on 2026-11-26. Flip PRODUCT_PAGES_APPROVED to True the day Apple
# has approved both (Amir 2026-11-26: "Yes, link them"): the App Store links of the
# guides below, and the "In Österreich" link of the German home page, then open that
# country's page (apps.apple.com/ch|at/…?ppid=…). Until then nothing changes.
PRODUCT_PAGES = {"ch": "add026ea-4f63-4598-a3c8-33e1eef599b7",
                 "at": "44434dea-1c5e-484b-8db6-1dbc71ea86dc"}
PRODUCT_PAGES_APPROVED = False
PRODUCT_PAGE_GUIDES = {
    "ch": ["de-fahrtenbuch-schweiz-privatanteil", "de-korlogg-vs-driversnote-schweiz"],
    "at": ["de-fahrtenbuch-oesterreich", "de-korlogg-vs-driversnote-oesterreich",
           "de-kilometergeld-2027-oesterreich", "de-fahrtenbuch-vorlage-oesterreich"],
}

# support@korlogg.com is being set up; the support page also lists the old
# address until SUPPORT_EMAIL_LIVE is True.
SUPPORT_EMAIL = "support@korlogg.com"
FALLBACK_EMAIL = "avelan.sverige@gmail.com"
SUPPORT_EMAIL_LIVE = True

# Anonymous, cookieless visitor statistics (Amir 2026-10-11). TelemetryDeck web
# app "korlogg.com", namespace se.avelan. Page views come from TelemetryDeck's
# Web SDK; App Store badge clicks from assets/stats.js.
TELEMETRYDECK_APP_ID = "22120ED7-73AC-47F1-8E16-CAF4203EE530"

# Körlogg for Android (Google Play). Guides show their Play link ({{play}}…{{/play}})
# only when this is True. Flip it the day the Play listing is live.
PLAY_PACKAGE = "se.mobix.korlogg"
PLAY_RELEASED = True

# Real App Store reviews shown on the home pages ("What users say"), newest first.
# Copy each one verbatim from App Store Connect / the store, in its own language;
# never edit, translate or shorten the reviewer's words. `country` is the App Store
# country code, `date` the day Apple shows. No review JSON-LD (self-serving reviews
# are not eligible for rich results).
REVIEWS = [
    dict(author="bösches501", country="at", rating=5, date="2026-10-08", lang="en",
         title="Fantastic!",
         text="Great app for company car drivers in Austria! Easy to use, affordable compared to "
              "alternatives, and the developer really listens to user feedback. Looking forward to "
              "the new beacon feature. Highly recommended! 👍"),
]
INDEXNOW_KEY = "9f1c02629638730410e41824c4d32468"   # IndexNow (Bing, Yandex, Seznam…): key file /9f1c02629638730410e41824c4d32468.txt in the repo root
