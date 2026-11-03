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
| Fri 2026-10-30 | UK | /guides/hmrc-mileage-log-template/ (new) | en-hmrc-mileage-log-template.html | hmrc mileage log template |
| Fri 2026-10-30 | DE | /de/ratgeber/elektronisches-fahrtenbuch-anforderungen/ (new) | de-elektronisches-fahrtenbuch.html | elektronisches fahrtenbuch anforderungen |
| Fri 2026-10-30 | NL | /nl/gidsen/rittenregistratie-bijhouden/ (new) | nl-rittenregistratie-bijhouden.html | rittenregistratie bijhouden |
| Tue 2026-11-03 | NL | /nl/gidsen/zakelijke-kilometers-zzp/ (new, extra NL slot) | nl-zzp-zakelijke-kilometers.html | zakelijke kilometers zzp |
| Tue 2026-11-03 | SE | /se/guider/milersattning/ (new; Amir OK 2026-10-29) | sv-milersattning.html | milersättning 2026 / milersättning skatteverket |
| Fri 2026-11-06 | US | /guides/irs-mileage-log-requirements/ (new; waits for Amir's review) | en-irs-mileage-log-requirements.html | irs mileage log requirements |
| Tue 2026-11-10 | US | /guides/mileage-log-template/ (new, + /assets/mileage-log-template.csv; waits for Amir's review) | en-mileage-log-template.html | mileage log template irs |
| Fri 2026-11-06 | NO | /no/guider/kjoregodtgjorelse/ (new, first Norwegian guide: also opens /no/guider/ and the Guider link; waits for Amir's review) | no-kjoregodtgjorelse.html | kjøregodtgjørelse 2026 / statens satser |
| Tue 2026-11-10 | DK | /da/guides/korselsgodtgorelse/ (new, first Danish guide: also opens /da/guides/; waits for Amir's review) | da-korselsgodtgorelse.html | kørselsgodtgørelse 2026 |
| Fri 2026-11-13 | FI | /fi/oppaat/kilometrikorvaus/ (new, first Finnish guide: also opens /fi/oppaat/; waits for Amir's review) | fi-kilometrikorvaus.html | kilometrikorvaus 2026 |
| Fri 2026-11-06 | UK | /guides/hmrc-mileage-rates-2027-28/ (new; 55p/35p from 6 Apr 2027 announced at Budget 2026 on 28 Oct; waits for Amir's review) | en-hmrc-mileage-rates-2027-28.html | hmrc mileage rates 2027/28 |
| Tue 2026-11-10 | AT | /de/ratgeber/kilometergeld-2027-oesterreich/ (new; Kilometergeld unchanged 0,50 €, new E-car Sachbezug from 2027 per BGBl. II 272/2026; waits for Amir's review) | de-kilometergeld-2027-oesterreich.html | kilometergeld 2027 |
| Fri 2026-11-13 | FI | /fi/oppaat/kilometrikorvaus-2027/ (new; Verohallinto decided 58 c on 23 Oct 2026; the 2026 guide links to it; waits for Amir's review) | fi-kilometrikorvaus-2027.html | kilometrikorvaus 2027 |
| Tue 2026-11-17 | DE | /de/ratgeber/fahrtenbuch-app-was-das-finanzamt-prueft/ (new; from the competitor audit of 2026-11-03; waits for Amir's review) | de-fahrtenbuch-app-finanzamt-prueft.html | fahrtenbuch app finanzamt |
| Fri 2026-11-20 | NL | /nl/gidsen/rittenregistratie-zonder-keurmerk/ (new; from the competitor audit; waits for Amir's review) | nl-rittenregistratie-zonder-keurmerk.html | rittenregistratie keurmerk |
| Tue 2026-11-24 | DE | /de/ratgeber/kilometerpauschale-2027/ (new; rates fixed by law, JStG 2026 changes nothing; waits for Amir's review) | de-kilometerpauschale-2027.html | kilometerpauschale 2027 |

If the push happens after a date above, that guide goes live with the push.

## Waiting for the 2027 announcements (written, held)

Five rate pages are written and registered in `tools/build.py` with `publish: 2099-12-31`
and every unknown figure marked `⟦…⟧`. `tools/build.py` refuses a live build while a guide
still has a `⟦` (an `--as-of` preview only warns), so nothing can slip out half-filled.
Each file starts with a `<!-- hold: … -->` comment that says what to fill in. On the day:

1. Open the authority page named in the hold comment, fill in every `⟦…⟧` (title and
   description too), set `publish` and `modified` to that day.
2. Add the one-line link to the 2027 page in the 2026 guide named in the hold comment.
3. `python3 tools/build.py && python3 tools/check.py`, commit, push. The push deploys
   and pings IndexNow; no need to wait for the Tue/Fri run.

| Country | Page | File | Who decides, where it appears first | Expected | Evidence |
|---|---|---|---|---|---|
| NO | /no/guider/kjoregodtgjorelse-2027/ | no-kjoregodtgjorelse-2027.html | Skattedirektoratet, "Forskrift om satser mv. … for 2027" § 4 on lovdata.no; statens sats from the særavtale 2026–2027 (5,30 kr) | early–mid Nov 2026 | 2026 forskrift kunngjort 7 Nov 2025 (FOR-2025-11-07-2216) |
| DK | /da/guides/korselsgodtgorelse-2027/ | da-korselsgodtgorelse-2027.html | Skatterådet, "Bekendtgørelse om Skatterådets satser for 2027" on retsinformation.dk; sktst.dk news the same day | ~19–20 Nov 2026 | 2026: BEK 1333 of 20 Nov 2025; 2025: BEK 1189 of 19 Nov 2024 |
| SE | /se/guider/milersattning-2027/ | sv-milersattning-2027.html | Rate is statutory (12 kap. 5 § IL); Skatteverket's "Belopp och procent – inkomstår 2027" page/PDF is the announcement | mid-Dec 2026 | 2026 PDF dated 16 Dec 2025; transitional budget 2027, no change proposed |
| NL | /nl/gidsen/kilometervergoeding-2027/ | nl-kilometervergoeding-2027.html | Eerste Kamer vote on Belastingplan 2027 (37 022): € 0,25 structural; TK vote planned 12 Nov | ~15–16 Dec 2026 | 2025 pattern: TK 27 Nov, EK 16 Dec, Stb. 23 Dec |
| US | /guides/irs-mileage-rate-2027/ | en-irs-mileage-rate-2027.html | IRS newsroom release + Notice 2027-xx; irs.gov/tax-professionals/standard-mileage-rates | 14–31 Dec 2026 | 2024: 14 Dec 2023; 2025: 19 Dec 2024; 2026: 29 Dec 2025 |

Already official, so queued with real figures (table above): UK 2027/28 (Budget 2026, 28 Oct:
25p → 35p above 10,000 miles from 6 Apr 2027, statutory instrument still to come), FI 2027
(Verohallinto 23 Oct 2026: 58 c), AT 2027 (Kilometergeld unchanged by permanent regulation;
E-car Sachbezug BGBl. II 272/2026), DE 2027 (rates in EStG/BRKG, JStG 2026 silent).
Research notes with every URL: Claude Code session of 2026-11-03 (three sub-agent reports),
summarised in the pages' source lists.

## Planned (not written yet)

Slots from Fri 30 Oct to Tue 22 Dec 2026. AT = Austria-specific (Kilometergeld
0,50 €, Sachbezug). DK only if Amir confirms Denmark.

| Slot | UK | DE | Third |
|---|---|---|---|
| Tue 3 Nov | mileage allowance relief (claim the difference) | fahrtenbuch app | SE: körjournal mall |
| Fri 6 Nov | self employed mileage claim (simplified expenses) | fahrtenbuch selbstständige | ~~AT: kilometergeld 2026~~ (kilometergeld 2027 written, queued Tue 10 Nov) |
| Tue 10 Nov | mileage log app uk | fahrtenbuch nachträglich erstellen | NL: rittenregistratie app |
| Fri 13 Nov | advisory fuel rates company car | fahrtenbuch elektroauto (0,25 %) | SE: körjournal app |
| Tue 17 Nov | temporary workplace 24 month rule | dienstwagen 0,03 % oder 0,002 % | AT: sachbezug firmenauto 2026 |
| Fri 20 Nov | limited company director mileage | fahrtenbuch betriebsprüfung | NL: verklaring geen privégebruik |
| Tue 24 Nov | how far back can I claim mileage | entfernungspauschale 2026 | SE: förmånsvärde bil 2026 |
| Fri 27 Nov | mileage vs actual costs self employed | fahrtenbuch mehrere fahrer | AT: fahrtenbuch vorlage österreich |
| Tue 1 Dec | passenger payments 5p | fahrtenbuch kundendienst erleichterungen | NL: bijtelling 2026 |
| Fri 4 Dec | ev mileage rate (advisory electric rate) | 50 % betriebliche nutzung nachweisen | ~~SE: milersättning 2026~~ (live 3 Nov; 2027 page held) |
| Tue 8 Dec | mileage claim form employer | fahrtenbuch umwege reiseroute | DK: kørebog skat krav |
| Fri 11 Dec | what if HMRC checks my mileage | fahrtenbuch aufbewahrungsfrist | AT: pendlerpauschale oder kilometergeld |
| Tue 15 Dec | landlord mileage claim | fahrtenbuch jahreswechsel kilometerstand | NL: rittenregistratie zzp |
| Fri 18 Dec | ~~hmrc mileage rates 2027/28~~ (written, queued Fri 6 Nov) | fahrtenbuch für 2027 vorbereiten | DK: kørebog app |
| Tue 22 Dec | year-end mileage checklist (tax year ends 5 April) | ~~kilometerpauschale 2027~~ (written, queued Tue 24 Nov) | SE: körjournal årsskifte |

## Planned pages (later, approved 2026-10-19; not scheduled yet)

| Page | Languages | Notes |
|---|---|---|
| Feature: iBeacon per car | en, sv, de (then nl) | How a beacon picks the car; links to the existing "Which iBeacon" guides |
| Feature: the PDF/Excel report, with a sample | en, sv, de (then nl) | Downloadable sample PDF made from demo data, one per country format; the "What the exported log contains" table |
| Criteria comparison: "Fahrtenbuch-Apps im Vergleich: worauf es ankommt" | de first, then sv, en, nl | Criteria, not brands (no competitor named, per docs/competitor-notes.md): edits shown in the export, delete vs cancel, odometer read vs calculated, 7-day rule, commute category, account needed, where data is stored, export formats, iBeacon, price model |
