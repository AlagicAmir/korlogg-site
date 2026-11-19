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
| Fri 2026-11-06 | US | /guides/irs-mileage-log-requirements/ (new; Amir OK 2026-11-17) | en-irs-mileage-log-requirements.html | irs mileage log requirements |
| Tue 2026-11-10 | US | /guides/mileage-log-template/ (new, + /assets/mileage-log-template.csv; Amir OK 2026-11-17) | en-mileage-log-template.html | mileage log template irs |
| Fri 2026-11-06 | NO | /no/guider/kjoregodtgjorelse/ (new, first Norwegian guide: also opens /no/guider/ and the Guider link; Amir OK 2026-11-17) | no-kjoregodtgjorelse.html | kjøregodtgjørelse 2026 / statens satser |
| Tue 2026-11-10 | DK | /da/guides/korselsgodtgorelse/ (new, first Danish guide: also opens /da/guides/; Amir OK 2026-11-17) | da-korselsgodtgorelse.html | kørselsgodtgørelse 2026 |
| Fri 2026-11-13 | FI | /fi/oppaat/kilometrikorvaus/ (new, first Finnish guide: also opens /fi/oppaat/; Amir OK 2026-11-17) | fi-kilometrikorvaus.html | kilometrikorvaus 2026 |
| Fri 2026-11-06 | UK | /guides/hmrc-mileage-rates-2027-28/ (new; 55p/35p from 6 Apr 2027 announced at Budget 2026 on 28 Oct; Amir OK 2026-11-03) | en-hmrc-mileage-rates-2027-28.html | hmrc mileage rates 2027/28 |
| Tue 2026-11-10 | AT | /de/ratgeber/kilometergeld-2027-oesterreich/ (new; Kilometergeld unchanged 0,50 €, new E-car Sachbezug from 2027 per BGBl. II 272/2026; Amir OK 2026-11-03) | de-kilometergeld-2027-oesterreich.html | kilometergeld 2027 |
| Fri 2026-11-13 | FI | /fi/oppaat/kilometrikorvaus-2027/ (new; Verohallinto decided 58 c on 23 Oct 2026; the 2026 guide links to it; Amir OK 2026-11-03) | fi-kilometrikorvaus-2027.html | kilometrikorvaus 2027 |
| Tue 2026-11-17 | DE | /de/ratgeber/fahrtenbuch-app-was-das-finanzamt-prueft/ (new; Amir OK 2026-11-03) | de-fahrtenbuch-app-finanzamt-prueft.html | fahrtenbuch app finanzamt |
| Fri 2026-11-20 | CH (de) | /de/ratgeber/fahrtenbuch-schweiz-privatanteil/ (new; first Swiss page, rule-set shipped in 2.6; Wegleitung/FAQ 2026, 75 Rappen since 1.1.2026; Amir OK 2026-11-17) | de-fahrtenbuch-schweiz-privatanteil.html | privatanteil geschäftsfahrzeug / fahrtenbuch schweiz |
| Tue 2026-11-10 | HU | /hu/utmutatok/utnyilvantartas/ (new; first Hungarian guide, with the Hungarian home/help/support pages that went live 3 Nov; NAV prices Nov 2026; Amir OK 2026-11-17) | hu-utnyilvantartas.html | útnyilvántartás / kiküldetési rendelvény / költségtérítés |
| Tue 2026-11-24 | DE | /de/ratgeber/kilometerpauschale-2027/ (new; rates fixed by law, JStG 2026 changes nothing; Amir OK 2026-11-03) | de-kilometerpauschale-2027.html | kilometerpauschale 2027 |
| Tue 2026-11-17 | UK | /guides/temporary-workplace-24-month-rule/ (new, refill 2026-11-15; Amir OK 2026-11-17) | en-temporary-workplace-24-month-rule.html | temporary workplace 24 month rule |
| Fri 2026-11-20 | UK | /guides/limited-company-director-mileage/ (new, refill 2026-11-15; Amir OK 2026-11-17) | en-director-mileage-limited-company.html | limited company director mileage |
| Tue 2026-11-24 | UK | /guides/how-far-back-can-you-claim-mileage/ (new, refill 2026-11-15; Amir OK 2026-11-17) | en-how-far-back-mileage-claim.html | how far back can I claim mileage |
| Fri 2026-11-27 | UK | /guides/simplified-mileage-vs-actual-costs/ (new, refill 2026-11-15; Amir OK 2026-11-17) | en-mileage-vs-actual-costs.html | mileage vs actual costs self employed |
| Fri 2026-11-27 | DE | /de/ratgeber/fahrtenbuch-mehrere-fahrer/ (new, refill 2026-11-15; Amir OK 2026-11-17) | de-fahrtenbuch-mehrere-fahrer.html | fahrtenbuch mehrere fahrer |
| Fri 2026-11-27 | AT | /de/ratgeber/fahrtenbuch-vorlage-oesterreich/ (new, refill 2026-11-15; Amir OK 2026-11-17) | de-fahrtenbuch-vorlage-oesterreich.html | fahrtenbuch vorlage österreich |
| Tue 2026-12-01 | UK | /guides/passenger-payments-5p/ (new, refill 2026-11-15; Amir OK 2026-11-17) | en-passenger-payments-5p.html | passenger payments 5p |
| Tue 2026-12-01 | DE | /de/ratgeber/fahrtenbuch-erleichterungen-kundendienst-handelsvertreter/ (new, refill 2026-11-15; Amir OK 2026-11-17) | de-fahrtenbuch-erleichterungen-aussendienst.html | fahrtenbuch erleichterungen |
| Tue 2026-12-01 | NL | /nl/gidsen/bijtelling-2026/ (new, refill 2026-11-15; Amir OK 2026-11-17) | nl-bijtelling-2026.html | bijtelling 2026 |
| Fri 2026-12-04 | UK | /guides/advisory-electric-rate/ (new, refill 2026-11-15; Amir OK 2026-11-17) | en-advisory-electric-rate.html | advisory electric rate |
| Fri 2026-12-04 | DE | /de/ratgeber/50-prozent-betriebliche-nutzung-nachweisen/ (new, refill 2026-11-15; Amir OK 2026-11-17) | de-50-prozent-betriebliche-nutzung.html | 50 % betriebliche nutzung nachweisen |
| Fri 2026-11-20 | SE | /se/guider/starta-resan-med-carplay-eller-bluetooth/ (new; Shortcuts automation, written after a customer's mail; Amir 2026-11-19: schedule it) | sv-starta-resan-carplay-bluetooth.html | körjournal carplay / starta resa automatiskt |
| Tue 2026-11-24 | EN | /guides/start-trips-with-carplay-or-bluetooth/ (new; same guide in English) | en-start-trips-carplay-bluetooth.html | mileage log carplay / start trip automatically bluetooth |
| Tue 2026-12-01 | DE | /de/ratgeber/fahrtenbuch-automatisch-starten-carplay-bluetooth/ (new; same guide in German) | de-fahrtenbuch-starten-carplay-bluetooth.html | fahrtenbuch carplay / fahrtenbuch bluetooth automatisch starten |
| Fri 2026-11-27 | SE | /se/guider/milersattning/ (rewrite: calculator at the top, new title and H1; Amir 2026-11-19 "do the same for sweden and germany … some other day") | sv-milersattning@2026-11-27.html | räkna ut milersättning 2026 |

If the push happens after a date above, that guide goes live with the push.

## No comparison pages (Amir 2026-11-17)

Amir 2026-11-17: korlogg.com never publishes pages that compare Körlogg with competitors, name them, or say what Körlogg does not do. Guides say Körlogg is built to the tax authority's rules, never that the authority approves no app. Do not write or queue such pages.

## Comparison pages (live 2026-11-17)

/korlogg-vs-…/ pages for SE, UK (vs Driversnote), DE (vs Vimcar), NO, DK, FI, AT, CH (vs Driversnote). Only where Körlogg wins; App Store prices checked 2026-11-17 — recheck prices every quarter. After 20 Nov, link the Swiss vs page to /de/ratgeber/fahrtenbuch-schweiz-privatanteil/.

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

## US queue (from 2026-11-18; each guide goes live only after Amir's OK)

Amir 2026-11-18: one or two US guides a week that answer what people type into Google ("how to save money",
"how to export"), because the US store search gives nothing yet (0 downloads 8–17 Nov, ranked only for the name).
The first two were approved on 2026-11-18 and carry their publish dates; later drafts wait with `publish: 2099-12-31`.
Rules as everywhere: IRS sources only, amounts written as "dollars" (the checker blocks `$` + digit), no competitor
names, no doubt lines, the app paragraph at the end sells.

| Proposed day | Page | File | Question it answers | State |
|---|---|---|---|---|
| Tue 24 Nov | /guides/how-to-track-mileage-for-taxes/ | en-track-mileage-for-taxes.html | how to track mileage for taxes (1099, self-employed) | queued for 24 Nov (Amir OK 2026-11-18) |
| Tue 1 Dec | /guides/forgot-to-track-mileage/ | en-forgot-to-track-mileage.html | forgot to track mileage; reconstruct mileage log | queued for 1 Dec (Amir OK 2026-11-18) |
| Fri 27 Nov | /guides/mileage-deduction-how-much-money/ | en-mileage-deduction-money-back.html | how much money do I get back for mileage; mileage deduction 2026 | queued (Amir OK 2026-11-18) |
| Fri 4 Dec | /guides/korlogg-vs-mileiq-everlance/ | en-korlogg-vs-mileiq-everlance.html | mileiq alternative; everlance alternative; comparison chart (US App Store prices of 18 Nov – recheck on the publish day) | queued (Amir OK 2026-11-18) |
| Tue 8 Dec | /guides/standard-mileage-rate-vs-actual-expenses/ | – | standard mileage rate vs actual expenses: which saves more | to write |
| on the IRS announcement (14–31 Dec) | /guides/irs-mileage-rate-2027/ | en-irs-mileage-rate-2027.html | irs mileage rate 2027 | held, placeholders |
| Tue 15 Dec | /guides/doordash-uber-mileage-deduction/ | – | which gig miles count as business | to write |
| Tue 29 Dec | /guides/new-year-mileage-checklist/ | – | odometer on January 1, what to set up for 2027 | to write |
| Tue 5 Jan | /guides/mileage-log-for-your-accountant/ | – | how to export a mileage log for Schedule C / your accountant | to write |
| Tue 12 Jan | /guides/employer-mileage-reimbursement/ | – | accountable plan: 60 days, IRS rate, what is taxed | to write |
| Tue 19 Jan | /guides/medical-and-charity-mileage/ | – | medical and charity miles and their rates | to write |
| Tue 26 Jan | /guides/can-i-deduct-my-commute/ | – | commuting vs business miles, home office, temporary work site | to write |

## "Money back" pages (live 2026-11-19)
Amir 2026-11-19: pages that answer a money question with a title an everyday reader would type are the best kind.
Each answers "my employer pays less than the official rate, or nothing: how do I get tax back on the rest, and how many
years back?" Published the same day on his word ("I trust you … please do it"), linked from each country's rate page.
- `sv-milersattning-skillnaden.html` → `/se/guider/arbetsgivaren-betalar-mindre-an-25-kr-per-mil/` (six years back; 18,50 kr per mil 2020–2022).
- `de-arbeitgeber-zahlt-weniger-als-30-cent.html` → `/de/ratgeber/arbeitgeber-zahlt-weniger-als-30-cent/` (four years; 2022 closes on 31 Dec 2026).
- `de-kilometergeld-arbeitgeber-zahlt-weniger.html` → `/de/ratgeber/kilometergeld-arbeitgeber-zahlt-weniger/` (Austria, five years; 2021 closes on 31 Dec 2026).
The UK has this page already (`en-how-far-back-mileage-claim`, 24 Nov). Denmark: the difference cannot be deducted
(`da-korselsgodtgorelse.html`). Netherlands, Norway, Finland: not checked yet.
In January 2027 the deadline sentences and year tables in all three move on by one year.
The Danish 2027 page (`da-korselsgodtgorelse-2027.html`) went live the same day.

## Calculator test on a rate page (live 2026-11-19)

Search Console on 2026-11-19: `/de/ratgeber/kilometergeld-2027-oesterreich/` had 89 impressions and 0 clicks; 26 of the
impressions were as a source in Google's AI answer, which states the rate itself, and the page was not among the ten
normal results for "kilometergeld 2027" on Google Austria, where pages with a calculator rank. Amir 2026-11-19: add a
calculator as a test. The page now opens with a Kilometergeld-Rechner (vehicle, km, passengers, what the employer pays;
30 000 km limit, bicycle 3 000 km) and has "Rechner" in the title and H1. Read the page's clicks and position again
around 10 December 2026; if they moved, do the same on the other rate pages (SE, DE, DK, NO, FI, NL, UK).

Amir 2026-11-19: the same for Sweden and Germany, on another day. Germany: `de-kilometerpauschale-2027.html` (goes live
Tue 2026-11-24) has a Kilometerpauschale-Rechner (Dienstreise 0,30/0,20 € with what the employer pays, and the
Entfernungspauschale 0,38 € × full km × days). Sweden: `sv-milersattning@2026-11-27.html` replaces the live page on
Fri 2026-11-27 (25 / 12 / 9,50 kr per mil, mil or km, what the employer pays). From 27 November any edit to the Swedish
rate page is made in the `@2026-11-27` file, which is the live one.
