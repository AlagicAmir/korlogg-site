# Content queue – korlogg.com

Guides are written ahead and go live on a fixed rhythm: **Tuesday and Friday,
07:00 Europe/Stockholm** (the workflow runs at 05:00 UTC, which is 07:00 in summer
and 06:00 in winter). One guide per language per slot: UK (English) and DE every
slot, then SE / NL / AT in turn.

## How it works

- A new guide is `src/guides/<stem>.html` with `<!-- publish: YYYY-MM-DD -->` and an
  entry in `GUIDES` in `tools/build.py` (language, URL).
- A rewrite of a guide that is already live is `src/guides/<stem>@YYYY-MM-DD.html`
  (same `publish` date inside). Until that day the old version stays live at the
  same URL; from that day the new one replaces it. Delete the old file afterwards
  if you like (rename the revision to `<stem>.html` and drop `publish`).
- `tools/build.py` leaves out every guide whose date is in the future: no page, no
  entry in the guide index or the home page, no sitemap line, no hreflang.
- `.github/workflows/publish.yml` builds and deploys on every push to main and on
  the Tuesday/Friday schedule. It uploads only the built site (not `src/`,
  `tools/`, `docs/`), so a queued guide is not reachable on korlogg.com before
  its day. (The GitHub repo itself is public, so the source can be read there.)
- Preview the site as it will look on a day: `python3 tools/build.py --as-of 2026-10-27`,
  serve with `python3 -m http.server 8766 --bind 127.0.0.1`, then rebuild with
  plain `python3 tools/build.py` before committing.
- Google Play links in guides (`{{play}} … {{/play}}`) appear only when
  `PLAY_RELEASED = True` in `tools/config.py`. Flip it the day the Android app is live.

## One-time switch before the first push

Settings → Pages → Build and deployment → Source: **GitHub Actions** (today it is
"Deploy from a branch: main /"). Until this is switched, Pages keeps serving the
whole main branch, including `src/guides/`, and the schedule does nothing.
Order: switch the source, then push.

## Queued

| Live from | Lang | Page | File | Target keyword |
|---|---|---|---|---|
| Fri 2026-10-23 | DE | /de/ratgeber/fahrtenbuch-vorlage-oder-app/ (new) | de-fahrtenbuch-vorlage-oder-app.html | fahrtenbuch vorlage |
| Fri 2026-10-23 | UK | /guides/hmrc-mileage-log/ (rewrite) | en-hmrc-mileage-log@2026-10-23.html | hmrc mileage log |
| Tue 2026-10-27 | DE | /de/ratgeber/was-muss-ein-fahrtenbuch-enthalten/ (rewrite) | de-fahrtenbuch-inhalt@2026-10-27.html | fahrtenbuch führen |
| Tue 2026-10-27 | SE | /se/guider/vad-ska-en-korjournal-innehalla/ (rewrite) | sv-korjournal-innehall@2026-10-27.html | körjournal skatteverket |

If the push happens after a date above, that guide goes live with the push.

## Planned (not written yet)

Slots from Fri 30 Oct to Tue 22 Dec 2026. AT = Austria-specific (Kilometergeld
0,50 €, Sachbezug). DK only if Amir confirms Denmark.

| Slot | UK | DE | Third |
|---|---|---|---|
| Fri 30 Oct | hmrc mileage log template | elektronisches fahrtenbuch anforderungen | NL: rittenregistratie bijhouden |
| Tue 3 Nov | mileage allowance relief (claim the difference) | fahrtenbuch app | SE: körjournal mall |
| Fri 6 Nov | self employed mileage claim (simplified expenses) | fahrtenbuch selbstständige | AT: kilometergeld 2026 |
| Tue 10 Nov | mileage log app uk | fahrtenbuch nachträglich erstellen | NL: rittenregistratie app |
| Fri 13 Nov | advisory fuel rates company car | fahrtenbuch elektroauto (0,25 %) | SE: körjournal app |
| Tue 17 Nov | temporary workplace 24 month rule | dienstwagen 0,03 % oder 0,002 % | AT: sachbezug firmenauto 2026 |
| Fri 20 Nov | limited company director mileage | fahrtenbuch betriebsprüfung | NL: verklaring geen privégebruik |
| Tue 24 Nov | how far back can I claim mileage | entfernungspauschale 2026 | SE: förmånsvärde bil 2026 |
| Fri 27 Nov | mileage vs actual costs self employed | fahrtenbuch mehrere fahrer | AT: fahrtenbuch vorlage österreich |
| Tue 1 Dec | passenger payments 5p | fahrtenbuch kundendienst erleichterungen | NL: bijtelling 2026 |
| Fri 4 Dec | ev mileage rate (advisory electric rate) | 50 % betriebliche nutzung nachweisen | SE: milersättning 2026 |
| Tue 8 Dec | mileage claim form employer | fahrtenbuch umwege reiseroute | DK: kørebog skat krav |
| Fri 11 Dec | what if HMRC checks my mileage | fahrtenbuch aufbewahrungsfrist | AT: pendlerpauschale oder kilometergeld |
| Tue 15 Dec | landlord mileage claim | fahrtenbuch jahreswechsel kilometerstand | NL: rittenregistratie zzp |
| Fri 18 Dec | hmrc mileage rates 2027/28 (update when published) | fahrtenbuch für 2027 vorbereiten | DK: kørebog app |
| Tue 22 Dec | year-end mileage checklist (tax year ends 5 April) | kilometerpauschale 2027 (update) | SE: körjournal årsskifte |
