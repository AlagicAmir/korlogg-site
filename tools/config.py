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

SITE = "https://korlogg.com"
APP_ID = "6809322275"

# support@korlogg.com is being set up; the support page also lists the old
# address until SUPPORT_EMAIL_LIVE is True.
SUPPORT_EMAIL = "support@korlogg.com"
FALLBACK_EMAIL = "avelan.sverige@gmail.com"
SUPPORT_EMAIL_LIVE = False
