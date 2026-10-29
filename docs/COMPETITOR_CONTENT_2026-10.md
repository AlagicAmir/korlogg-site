# Competitor content study – korlogg.com (2026-10-29)

Purpose: learn which **subjects, page types and titles** the established mileage-log
companies use to win search traffic, then pick a few pages per country where
korlogg.com can be the best page on the web. Subjects can be borrowed. Text,
tables, layouts and claims are never copied. Every fact on our pages comes from the
tax authority and carries a "checked YYYY-MM-DD" line (see docs/competitor-notes.md).

## Method and limits

- **Page lists** come from each site's `robots.txt` → `sitemap.xml`, fetched on
  2026-10-29. They are complete for Driversnote (all country sites), MileIQ,
  Everlance, Vimcar (product and guide sections) and FleetGO.
- **Page anatomy** (headings, tables, FAQ, dates, sources, word count) comes from
  reading the strongest pages: Driversnote SE/DK/FI/DE rate pages, Driversnote US
  "mileage log requirements" and MileIQ "current IRS mileage rates".
- **Ranking signals** come from WebSearch, which searches from the US. For US/UK
  terms that is close to real Google. For Nordic, DE, NL, PL and HU terms it only
  shows **which domains Google finds relevant**, not local positions. Before
  committing a slot, check the real position in Search Console, or with a local
  incognito search from the country.
- Markers used below: **[borrowed subject]** = a competitor has this subject and we
  would write our own better version. **[own idea]** = no competitor page found.

## What the competitors publish – overview

| Site | Country sites with guides | Size of guide content | Pattern |
|---|---|---|---|
| Driversnote | US (.com, ~150 URLs), UK (~100), DE (~30), SE, DK, NL, FI (~20 each) | **None** on .no, .pl; .at and .ch redirect to an English page | Per country: a "tax-authority guide" hub with 6–12 chapters, a blog with a yearly rate post, template, "best app" post, enskild firma / self-employed deductions. Big hubs in US/UK: gig drivers, small-business tax, grey fleet, glossary ("dictionary") |
| MileIQ | US (+ a little UK/CA) | ~1,100 URLs, ~1,000 of them generic small-business blog posts | `/mileage-guide/` hub (~45 pages): rates, history, commuting, medical/charity, car allowance, per-state reimbursement. Separate 1099 calculator |
| Everlance | US | ~800 URLs | `/business-mileage-hub/` (rate, template), occupation pages (`/mileage-deductions/real-estate-agents` …), per-state "2025 IRS rate for Ohioans" pages, calculators (tax, savings, deduction finder), glossary |
| TripLog | US | Product-led, little editorial | B2B demo pages; not a content threat |
| Vimcar | DE + AT mirror (`/at/…`) | Product pages + a small Ratgeber | Firmenwagenrechner, Fahrtenbuch-Vorlage, "Rechtssicherheit", Ratgeber on geldwerter Vorteil and electronic Fahrtenbuch; webinars |
| FleetGO | NL | ~60 rittenregistratie posts | A long series of short Q&A posts (one question per URL: "Hoe lang moet je een rittenregistratie bewaren?", "Kan de Belastingdienst een rittenregistratie afkeuren?", "Keurmerk RRS" …). Thin, FAQ-farm style |
| Local generalists | all | – | Accounting/expense SaaS out-rank the app makers on rate terms: Fortnox, Bokio, Spiris (SE); Dinero, Pleo (DK); Sticos, Smarte Penger, NAF (NO); Summarum, Veronmaksajat, Taloustaito (FI); Lexware, sevdesk, Pleo (DE); freefinance, everbill (AT); bexio, pfeffersack (CH); fakturownia, infor (PL); adozona (HU); SparkReceipt runs translated "2026" rate posts in SE/FI/US |

## Structure of the best pages (what makes them work)

**Driversnote rate posts** (SE "Skatteverkets milersättning 2026", DK "Taksterne for
skattefri kørselsgodtgørelse stiger i 2026", FI "Verohallinnon kilometrikorvaukset
2026", DE "Kilometerpauschale 2026"):
- **A new URL every year** (`…-2023`, `…-2024`, `…-2025`, `…-2026`). Older years stay
  live as an archive. DK/FI 2026 posts were dated 20–24 Nov **2025**, DE on 22 Dec
  2025: they publish the day the authority announces, weeks before people search.
- **Short**: 330 words (DE) to ~1,000 words (FI). One rate table (vehicle → rate),
  sometimes previous year beside it. Sections by audience: employee, employer,
  sole trader / light entrepreneur, company car, commuting.
- **No official source links** on SE, DK and DE pages; FI links once to vero.fi. No
  worked examples, no FAQ, no author. Four to five sign-up/app CTAs per page.
- **Lesson**: they win on timing, yearly URLs, domain age and internal links, not on
  quality. A page with the authority's link, a worked example per audience and a
  small calculator can beat them on usefulness. It still has to be live on the day
  the new rate is announced.

**Driversnote US "IRS mileage log requirements"** (updated 25 Mar 2026): table of
contents, a breadcrumb into the "IRS Mileage Guide" hub, a sidebar listing all 16
chapters, one table of the four required elements, a vague-vs-specific example,
cites IRS Pub 463, a 4-question FAQ, links to a PDF/Excel/Sheets template. ~1,000 words.

**MileIQ "Current mileage rates for the US (2026)"**: "Key points" box first, then
sections by use (business, medical, charity, employer reimbursement), one worked
example, a 5-question FAQ, one link to irs.gov, a sidebar with ~45 guide links.
Updated January 2026: it still shows only 72.5¢, with no mid-year 76¢. **Our IRS
calculator already covers both rates. That is a freshness advantage worth a
dedicated rate page.**

**Everlance**: programmatic pages per US state and per occupation. Same template,
little substance. Not our quality bar. Do not copy the pattern.

**FleetGO (NL)**: one question per URL, ~300 words each. It shows which questions
people ask (retention period, rejection by the Belastingdienst, Keurmerk RRS, lease
vs own car, reconstruction afterwards). Answer them as FAQ sections inside a few
strong pages, not as 40 thin pages.

## What korlogg.com has today (2026-10-29)

Live or queued (src/guides + GUIDES in tools/build.py):
- **SE**: vad ska en körjournal innehålla · förmånsbil ringa omfattning · körjournal
  enskild firma · automatisk körjournal · milersättning 2026 (3 Nov) · iBeacon
- **DE**: Fahrtenbuch Pflichtangaben · elektronisches Fahrtenbuch · Fahrtenbuch oder
  1 % · Vorlage oder App · Kilometerpauschale 2026 · iBeacon
- **AT**: Fahrtenbuch in Österreich (Sachbezug + Kilometergeld), one combined page
- **UK**: HMRC mileage log · HMRC rates 2026/27 (55p/25p) · commuting vs business ·
  HMRC log template
- **US**: IRS calculator 2026 (72.5¢/76¢) · IRS log requirements (6 Nov) · mileage log
  template + CSV (10 Nov)
- **NL**: wat moet erin · 500 km privé · kilometervergoeding 2026 · bijhouden · zzp ·
  automatische rittenregistratie
- **NO / DK / FI**: 2026 rate guides being written in a parallel task
  (kilometergodtgjørelse / kørselsgodtgørelse / kilometrikorvaus)
- **PL, HU, CH**: nothing yet
- Planned slots to 22 Dec: see docs/CONTENT_QUEUE.md (UK and DE every slot, SE/NL/AT
  rotating, DK twice)

---

## Sweden (SE)

**Competitor pages**

| Title (as published) | URL | Type |
|---|---|---|
| Skatteverkets milersättning 2026 (+ 2023/2024/2025 versions) | driversnote.se/blog/skatteverkets-milersattning-2026 | yearly rate |
| Skatteverket guide till milersättning (hub) | driversnote.se/skatteverket-guide-till-milersattning | hub, 6 chapters: anställda, arbetsgivare, så räknar du, egenanställda, Skatteverkets krav på loggföring, tidigare belopp |
| Körjournal mall – Excel/PDF gratis | driversnote.se/blog/korjournal-mall-excel-pdf-gratis-nedladdning | template |
| Räkna ut milersättning och reseavdrag | driversnote.se/blog/rakna-ut-milersattning-och-reseavdrag | how to calculate |
| Skatteavdrag enskild firma | driversnote.se/blog/skatteavdrag-enskild-firma-guide-milersattning-och-andra-avdrag | self-employed |
| Krav på den bästa elektroniska körjournalen | driversnote.se/blog/krav-pa-den-basta-elektroniska-korjournalen | requirements / app |
| Körjournal (guide) | bokio.se/blogg/korjournal | requirements + template |
| Körjournal – mall för gratis nedladdning (PDF) | spiris.se/blogg/personalhantering/korjournal | template |
| Belopp och procentsatser 2026 | fortnox.se/fortnox-foretagsguide/…/belopp-och-procentsatser | all-rates table |
| Milersättning 2026 | sparkreceipt.com/sv-se/blogg/milersattning-2026 | yearly rate |

**Ranking signal**: "milersättning 2026" → SparkReceipt, Fortnox (2 URLs) on top;
Skatteverket and Driversnote are not in the first results from US search. "körjournal
mall skatteverket krav" → Bokio, driva-eget.se, Spiris, **skatteverket.se/…/bilforman/
korjournal**, Företagarna. Note: Skatteverket's körjournal page itself says templates
are sold and that one should check they contain all the headings in its example.
That is a good hook for a template that follows that example exactly.

**What the best ones do**: Bokio covers why, the 10 times / 100 mil rule, the 3,000 mil
reduction, drivmedelsförmån, trängselskatt, contents and a template on one page. Fortnox
wins "2026" terms with a single all-rates reference table that is updated every year.

**GAP list (max 5)**

1. **Körjournal mall 2026 – gratis PDF och Excel enligt Skatteverkets exempel**
   [borrowed subject] · term: *körjournal mall* · why: template intent ranks every
   year. Ours follows Skatteverket's example headings column by column and explains
   each one. Already planned for 3 Nov, keep it there. Sources: skatteverket.se
   …/bilforman/korjournal (example headings), SKV 292 (bilförmån), Rättslig vägledning
   "körjournal".
2. **Förmånsvärde och körjournal: sänkt förmånsvärde vid 3 000 mil tjänstekörning**
   [borrowed subject] · term: *förmånsvärde bil 2026*, *3000 mil tjänstekörning* · why:
   the log is the proof for the 25 % reduction, which matters directly to app users.
   Planned 24 Nov; widen it to cover the reduction. Sources: Skatteverket bilförmån
   pages, Skatteverkets förmånsbilberäknare, prisbasbelopp 2026 (SCB/Skatteverket).
3. **Drivmedelsförmån: så visar körjournalen vad som är privat** [borrowed subject] ·
   term: *drivmedelsförmån körjournal* · why: Skatteverket requires a monthly split
   of mil and the business share, or all fuel is taxed. Few good pages exist. Sources:
   skatteverket.se/…/bilforman/drivmedelsforman, the 1.2 multiplier rule.
4. **Reseavdrag 2026 för arbetsresor med egen bil – 25 kr/mil över 15 000 kr**
   [borrowed subject] · term: *reseavdrag 2026* · why: very high volume. Driversnote
   only covers it inside the rate post. Commuting is one of our trip categories. Check
   the 2026 threshold (11 000 kr in recent years; confirm whether it changed for 2026)
   and the distance rule (at least 5 km, 2 hours saved). Sources:
   skatteverket.se "Resor till och från arbetet", Inkomstskattelagen 12 kap. 26–30 §§.
5. **Milersättning för laddhybrid förmånsbil från 1 juli 2026** [own idea; seen as a
   news item only] · term: *milersättning laddhybrid 2026* · why: a rule change dated
   1 Jul 2026 (12 kr/mil can be paid even when the employer gives free charging, per
   secondary sources). Fresh topics with no strong page are where a new site can win.
   **Verify at Skatteverket before writing**, and consider making it a section of
   the milersättning page instead of a new page.

## Norway (NO)

**Competitor pages**: driversnote.no has **no guides** (product pages only). Ranking
domains for the rate: Sticos (statens satser table), Smarte Penger (article +
kjøregodtgjørelseskalkulator + "firmabil eller privateid bil" calculator), NAF
(satser for kjøregodtgjørelse). For "kjørebok": skatteetaten.no (2010 principle
statement "Bruk av arbeidsgivers bil – krav til dokumentasjon"), tek.no app news,
App Store pages (Quicklog/Kjørebok AS, BilBuddy, Mobil Kjørebok, Autogear), and a
Google Sheets "mal for digital kjørebok".

**Ranking signal**: "kilometergodtgjørelse 2026" returned nothing relevant from US
search, so the term is weak in Google's index. People in Norway search
*kjøregodtgjørelse*, *statens satser bil 2026* and *km-sats 2026*. **Check which
spelling the parallel NO rate guide targets.** The best competitor rate pages (Sticos,
Smarte Penger) give: 2026 statens sats 5,30 kr/km, the tax-free part 3,50 kr/km,
the taxable difference, and supplements (passasjer, utstyr, skogsvei 1,00 kr/km,
motorcycle and moped rates) in a table with 2025 beside 2026. Smarte Penger adds a
calculator. Compare ours with that.

**GAP list**

1. **Firmabil med elektronisk kjørebok: fordel etter kilometersats (3,40 kr/km i 2026)**
   [own idea, subject only on skatteetaten.no] · term: *firmabil kilometersats*,
   *elektronisk kjørebok firmabil* · why: Skatteetaten's 2026 car rates let an employee
   be taxed on actual private km, but only with an **electronic log administered by
   the employer**. That is our product's exact use case, and no app maker explains it.
   Sources: skatteetaten.no/satser/bilsatser---firmabil/?year=2026, Skatte-ABC
   "Bil – fordel ved privat bruk", Skattedirektoratets FSFIN §. Check whether a phone app
   kept by the employee counts as "administrert av arbeidsgiver". **Do not promise
   approval.**
2. **Kjørebok: hva Skatteetaten krever, og en gratis mal** [borrowed subject from
   SE/DK Driversnote; no NO competitor page] · term: *kjørebok*, *kjørebok mal* ·
   why: the head term has no strong owner. A template plus the official checklist
   (daily, continuous, start, visited company/site, end, km; odometer at least
   monthly) beats app-store pages. Sources: the Skatteetaten principle statement
   (2010, check it is still current), the current Skatte-ABC chapter on bil (dokumentasjon av yrkeskjøring).
3. **Yrkesbil: 6 000 km i næring – slik dokumenterer du det** [borrowed subject;
   official page only] · term: *yrkesbil 6000 km* · why: self-employed users need the
   log to cross the 6,000 km line (or >50 % business use), and the rule is assessed
   over three years. Sources: skatteetaten.no …/bil/bade-privat-og-i-naring/yrkesbil/,
   Skatte-ABC B-5-3.3.
4. **Reisefradrag 2026 for arbeidsreiser med egen bil** [borrowed subject] · term:
   *reisefradrag 2026* · why: high volume every spring at skattemelding time. Commute
   km come from the log. Check the 2026 sats and bunnbeløp at Skatteetaten
   (satser/reisefradrag). Sources: skatteetaten.no/satser/reisefradrag.
5. **Kjøregodtgjørelse over statens sats: hva blir skattepliktig?** [borrowed subject]
   · term: *skattefri kjøregodtgjørelse 2026* · why: the 5,30 vs 3,50 split confuses
   employees. One worked payslip example. **Merge into the parallel rate guide if it
   already covers this.** Sources: skatteetaten.no/satser/kilometergodtgjorelse,
   Statens reiseregulativ (DFØ / regjeringen.no særavtale).

## Denmark (DK)

**Competitor pages**

| Title | URL | Type |
|---|---|---|
| Taksterne for skattefri kørselsgodtgørelse stiger i 2026 | driversnote.dk/korselsgodtgorelses-guide-til-skat/taksterne-…-2026 | yearly rate (24 Nov 2025) |
| Kørselsgodtgørelses-guide til SKAT (hub) | driversnote.dk/korselsgodtgorelses-guide-til-skat | hub: 60-dages-reglen, for arbejdsgivere, for medarbejdere, for selvstændige, sådan beregner du, SKAT og arbejdsgivers krav til en kørebog, statens takst, tidligere satser |
| Bedste kørebog app | driversnote.dk/blog/bedste-korebog-app | app comparison |
| Firmabil eller egen bil | driversnote.dk/blog/firmabil-eller-egen-bil | comparison |
| Kørselsgodtgørelse (ordbog) | dinero.dk/ordbog/koerselsgodtgoerelse | glossary entry, "sidst opdateret 05/05/2026" |
| Kørselsregnskab skabelon | dinero.dk/ordbog/koerselsregnskab | template |
| 60-dages-reglen | skat.dk/60-dages-reglen | official |
| Satserne for skattefrie kørepenge 2026 | bdo.dk, danskindustri.dk, danskerhverv.dk | advisor news |
| Mileage Book (knowledge section: rates, 60-dages handbook, webinars) | mileagebook.com/da | local leader (B2B) |

**Ranking signal**: "kørselsgodtgørelse 2026" → Dinero, tax.dk, **skat.dk PDF skema
2026**, Danske Erhverv, DI, Pleo, BDO, Deloitte. "kørebog" → Dinero integration page
(Mileage Book), tax.dk Ligningsvejledning, Norwegian results. "60-dages reglen" →
skat.dk ×2, Dinero, RSM. Accounting SaaS and advisors own DK, and Driversnote is not
visible in US search. The best rate page (BDO/DI) shows a 2025 → 2026 table: 3,94
kr/km up to 20,000 km, 2,28 kr/km above, 0,64 kr/km bicycle/knallert. Check that
the parallel DK guide states that **the whole payment becomes taxable** if the rate is
exceeded, and the 20,000 km per employer example.

**GAP list** (DK still needs Amir's go, per CONTENT_QUEUE)

1. **Kørebog: SKATs krav – og en gratis skabelon** [borrowed subject] · term: *kørebog
   skat krav*, *kørebog skabelon* · why: planned 8 Dec. Make it the template page too.
   Use the Juridisk Vejledning detail: daily odometer start/end, date, business vs
   private split, destinations precise enough to check, no private abbreviations, must
   match the odometer; paper or electronic both fine (SKM2007.417.SR). Sources: Den
   juridiske vejledning C.A.4.3.3.3.3.3 (latest edition on skat.dk), skat.dk
   kørselsgodtgørelse pages.
2. **60-dages-reglen forklaret med kalender-eksempel** [borrowed subject] · term:
   *60 dages reglen* · why: steady volume. skat.dk ranks first, but the rule is hard
   to apply. A worked calendar (rolling 12 months; weekends and sickness don't count
   but don't break the period) is the useful part, and our log can count the days.
   Sources: skat.dk/60-dages-reglen, Ligningsloven § 9 B, JV C.A.7.1.
3. **Kørselsfradrag 2026 (befordringsfradrag): de rigtige satser** [borrowed subject;
   sources conflict] · term: *kørselsfradrag 2026* · why: one source gives 2,28/1,14
   kr/km and another says the rates were raised to 3,17/1,59 kr/km by a law passed 25
   June 2026. A page that settles it from skat.dk is worth a lot. **Verify at
   skat.dk/Skatteministeriet before anything is written.** Sources: skat.dk
   befordringsfradrag satser 2026, Folketinget lovforslag (June 2026).
4. **Firmabil eller kørselsgodtgørelse: regnestykke 2026** [borrowed subject] · term:
   *firmabil eller egen bil* · why: a decision page with one calculator (beskatning af
   fri bil vs tax-free kr/km). Sources: skat.dk "fri bil" (beskatningsgrundlag %,
   miljøtillæg 2026), Ligningsloven § 16, stk. 4.
5. **Kørselsgodtgørelse som selvstændig: standardsats eller faktiske udgifter**
   [borrowed subject] · term: *kørselsgodtgørelse selvstændig* · why: our sole-trader
   users can't pay themselves tax-free kørepenge from a personally owned business.
   The log supports the deduction either way. Sources: skat.dk erhvervsmæssig kørsel i
   egen bil (selvstændig), JV C.C.2.2.2.

## Finland (FI)

**Competitor pages**

| Title | URL | Type |
|---|---|---|
| Verohallinnon kilometrikorvaukset 2026 (+ separate "vahvistamat … vuodelle 2026" + 2023/24/25) | driversnote.fi/blog/verohallinnon-kilometrikorvaukset-2026 | yearly rate (20 Nov 2025) |
| Ilmainen kilometrikorvauslaskuri | driversnote.fi/blog/ilmainen-kilometrikorvauslaskuri-vuodelle | calculator |
| Verottajan vaatimukset ajopäiväkirjalle | driversnote.fi/blog/verottajan-vaatimukset-ajopaivakirjalle | requirements |
| Näin pidät ajopäiväkirjaa oikein | driversnote.fi/blog/nain-pidat-ajopaivakirjaa-oikein | how-to |
| Työsuhdeauto vai kilometrikorvaukset – kumpi on kannattavampi | driversnote.fi/blog/tyosuhdeauto-vai-… | comparison |
| Yrittäjän / yritysauton verovähennykset | driversnote.fi/blog/yrittajan-verovahennykset | self-employed |
| Kilometrikorvaus 2026 (laskuri) | summarum.fi/verolaskuri/kilometrikorvaus | calculator |
| Kilometrikorvaukset 2026 | veronmaksajat.fi/neuvot/…/kilometrikorvaukset-2026 | advisor (trade body) |
| Paras ajopäiväkirja sovellus 2026 | sparkreceipt.com/fi/blog/paras-ajopaivakirja-sovellus | app comparison |

**Ranking signal**: "kilometrikorvaus 2026 verohallinto" → Summarum (calculator)
first, SparkReceipt, Veronmaksajat, Taloustaito ×2, vero.fi ×2. "ajopäiväkirja" →
Motonet (paper log product), so **no strong digital owner**. Best rate content
(Veronmaksajat, Driversnote FI): 0,55 €/km (2025: 0,59), +4 c per passenger, +9 c
trailer, other add-ons (raskas kuorma, koira, metsätie), motorcycle 0,42, moped 0,23,
and 0,11 €/km for a car benefit with employee-paid fuel. Driversnote FI has the most
complete add-on list of its pages. Check that the parallel FI guide has all add-ons.

**GAP list**

1. **Ajopäiväkirja: mitä Verohallinto vaatii + ilmainen pohja** [borrowed subject] ·
   term: *ajopäiväkirja*, *ajopäiväkirja pohja* · why: the head term is owned by a
   paper product listing. A requirements + template page can take it. Sources:
   vero.fi "Auton käyttö elinkeinotoiminnassa / ajopäiväkirja" (find current page),
   Verohallinnon päätös 1005/2020 (applies only to taxi and foreign-registered work
   cars; say so clearly), syventävä ohje "Auto elinkeinotoiminnassa".
2. **Kilometrikorvauslaskuri 2026** [borrowed subject] · term: *kilometrikorvaus
   laskuri* · why: Summarum's calculator ranks first. Ours can include every 2026
   add-on and work offline. Could be an embedded block in the rate page instead of
   a new URL (the same pattern as the IRS calculator). Sources: Verohallinnon päätös
   verovapaista matkakustannusten korvauksista vuonna 2026.
3. **Työsuhdeauto: ajopäiväkirjalla pienempi verotusarvo (kilometriperusteinen
   käyttöetu)** [borrowed subject] · term: *työsuhdeauto ajopäiväkirja* · why: the
   km-based valuation (above 18,000 private km the value is calculated per km) needs a
   log. Check how it works today at vero.fi before writing. Sources: Verohallinnon päätös
   luontoisetujen raha-arvoista 2026, vero.fi autoetu pages, Veronmaksajat työsuhdeauto
   opas.
4. **Toiminimi ja oma auto: ajot kirjanpitoon 0,55 €/km ajopäiväkirjan perusteella**
   [borrowed subject] · term: *toiminimi kilometrikorvaus* · why: sole traders can't
   pay themselves an allowance; they deduct. The "more than 50 % business km → car
   belongs to business assets" rule is a strong hook. Sources: vero.fi "Elinkeinoauton
   ja yksityisauton kulut", Verohallinnon ohje "Auto elinkeinotoiminnassa".
5. **Matkakulujen vähennys 2026 (asunnon ja työpaikan väliset matkat)** [borrowed
   subject] · term: *matkakulujen vähennys 2026* · why: high volume in the tax season.
   Check the 2026 omavastuu, the per-km figure and the cap at vero.fi. Sources:
   vero.fi "Matkakulujen vähennys".

## Germany (DE)

**Competitor pages**

| Title | URL | Type |
|---|---|---|
| Die aktuelle Kilometerpauschale 2025 & 2026 | driversnote.de/blog/kilometerpauschale-2026 | yearly rate (22 Dec 2025, ~330 words) |
| 1-Prozent-Regelung (hub) + 4 chapters | driversnote.de/1-prozent-regelung/… | hub: für Selbständige, was ist günstiger, ohne 1 % und ohne Fahrtenbuch, geldwerter Vorteil |
| Firmenwagenrechner 2026 | driversnote.de/blog/firmenwagenrechner; vimcar.de/fahrtenbuch/firmenwagenrechner | calculator |
| Pendlerpauschale Rechner 2026 / Pendler- vs Kilometerpauschale | driversnote.de/blog/pendlerpauschale-rechner, …-versus-… | calculator + comparison |
| Fahrtenbuch-Vorlage PDF | driversnote.de/blog/fahrtenbuch-vorlage-…; vimcar.de/fahrtenbuch/vorlage | template |
| Anforderungen Fahrtenbuch / richtig führen / elektronisch vs Papier | driversnote.de/blog/… | requirements |
| Firmenwagen Privatnutzung, Car Allowance, Fahrzeug abschreiben | driversnote.de/blog/… | adjacent |
| Kilometergeld berechnen / Kilometergeld Steuer | driversnote.de/blog/kilometergeld-… | AT-term on DE site |
| Elektronisches Fahrtenbuch fürs Finanzamt – so wird es anerkannt | vimcar.de/ratgeber/… | requirements |
| Dienstwagenwechsel Versteuerung | vimcar.de/fahrtenbuch/dienstwagenwechsel-versteuerung | niche |

**Ranking signal**: "Fahrtenbuch führen Finanzamt Anforderungen" → Lexware, Avery
Zweckform (PDF guide), papierkram (Glossar), streit-software, Pleo (Vorlage), Geotab
(Glossar), Deutsche Handwerks-Zeitung. "Fahrtenbuch App Test" → computerwoche,
firmenauto.de (10 apps tested), DHZ, starting-up.de, für-gründer.de (6 providers
compared). Press tests and accounting SaaS rank; app makers rank on calculators.

**GAP list** (our base is strong; the gaps are calculators and the planned list)

1. **Firmenwagenrechner 2026: 1 %-Regel oder Fahrtenbuch – was spart mehr?**
   [borrowed subject] · term: *firmenwagenrechner*, *1 prozent regelung rechner* ·
   why: both main competitors have one. It is the strongest commercial bridge to
   "start a Fahrtenbuch". Add the calculator to the existing "Fahrtenbuch oder 1 %"
   page (same URL), or make a dedicated URL if the term is distinct in Search Console.
   Cover 1 %, 0,25 % / 0,5 % EV, 0,03 % or 0,002 % Arbeitsweg. Sources: EStG § 6 Abs. 1
   Nr. 4, § 8 Abs. 2, LStR 8.1 (9), BMF-Schreiben on E-Fahrzeuge (latest).
2. **Entfernungspauschale 2026: 0,38 € ab dem ersten Kilometer – Rechner** [borrowed
   subject] · term: *pendlerpauschale 2026*, *pendlerpauschale rechner* · why:
   planned 24 Nov. Highest-volume tax term in this field; 2026 changed (0,38 € from
   km 1; confirm in the Steueränderungsgesetz 2025). Give it a calculator. Sources:
   EStG § 9 Abs. 1 Nr. 4, BMF.
3. **Fahrtenbuch nachträglich erstellen – geht das?** [borrowed subject from press
   and FAQ sites] · term: *fahrtenbuch nachträglich* · why: planned 10 Nov. Real
   searcher pain; an honest "no, and here is what to do now" answer builds trust.
   Sources: BFH VI R 64/04, VI R 33/10; LStR 8.1 (9) Nr. 2.
4. **Fahrtenbuch-Apps im Vergleich: worauf es ankommt** (criteria, no brands)
   [borrowed subject] · term: *fahrtenbuch app test*, *fahrtenbuch app finanzamt* ·
   why: press tests rank and none of them is current. Our criteria page (already in
   the "later" list) answers the same intent without naming anyone. Sources: BMF/LStR,
   GoBD (BMF 28.11.2019, update 2024).
5. **Fahrtenbuch für Selbstständige: 50 % betriebliche Nutzung nachweisen**
   [borrowed subject] · term: *fahrtenbuch selbstständige*, *50 prozent betriebliche
   nutzung* · why: planned 6 Nov and 4 Dec as two pages. Consider one strong page.
   Sources: EStG § 6 Abs. 1 Nr. 4 S. 2, BMF 18.11.2009 (Nutzungsnachweis).

## Austria (AT)

**Competitor pages**: Vimcar mirrors its whole DE site under `/at/` (same text, no AT
law). Driversnote.at has no German content. Ranking domains: freefinance.at
(Kilometergeld, Fahrtenbuch), everbill.com ("Fahrtenbuch Österreich 2026: Muster mit
Pflichtangaben"), finanzinfo.at, selbststaendig-machen.at, missionline.it, a
teamzlab calculator, and one VwGH judgment on findok.bmf.gv.at.

**Ranking signal**: "Kilometergeld 2026 Österreich" → freefinance, everbill ×2,
finanzinfo, ÖAMTC, 5min.at. The sources **contradict each other** (0,50 € vs 0,42 €
per km; bike 0,25 vs 0,38). A page that quotes BGBl./BMF directly with a "checked"
date is the clear opening.

**GAP list**

1. **Kilometergeld 2026 in Österreich: 0,50 € pro km (amtlich geprüft)** [borrowed
   subject] · term: *kilometergeld 2026* · why: planned 6 Nov. Competing pages
   disagree; ours cites the Reisegebührenvorschrift / BGBl. II and gives
   passenger (+0,15 €), motorcycle and bike rates and the 30,000 km cap. Sources: RGV
   § 10, BGBl. II Nr. 289/2024 (confirm number), bmf.gv.at Kilometergeld.
2. **Fahrtenbuch Österreich: Pflichtangaben und Vorlage (VwGH-sicher)** [borrowed
   subject] · term: *fahrtenbuch österreich vorlage* · why: planned 27 Nov. Use VwGH
   30.1.2003, 99/15/0215 ("div. Kundenbesuche" with rounded km rejected) as the
   example of what fails. Sources: findok, LStR 2002 Rz 711 ff.
3. **Sachbezug Firmenauto 2026: 2 %, 1,5 %, 0 % E-Auto – und 50 %-Regel mit
   Fahrtenbuch** [borrowed subject] · term: *sachbezug firmenauto 2026* · why:
   planned 17 Nov. The half-Sachbezug at ≤ 500 km private per month needs a
   Fahrtenbuch, which is our hook. Sources: Sachbezugswerteverordnung § 4, BMF.
4. **Pendlerpauschale oder Kilometergeld?** [borrowed subject] · term:
   *pendlerpauschale österreich 2026* · why: planned 11 Dec; add the Pendlerrechner
   link (BMF). Sources: EStG § 16 Abs. 1 Z 6, BMF Pendlerrechner.
5. (no fifth page: AT is a small market; keep it at four)

## Switzerland (CH)

**Competitor pages**: no mileage-app competitor publishes CH-specific content
(driversnote.ch → English page; Vimcar no /ch). Ranking domains: weka.ch,
pfeffersack.ch ("Privatanteil Geschäftsfahrzeug Schweiz 2026: Anleitung" + Lexikon),
bexio ("Kilometergeld Schweiz"), magicheidi.ch, the cantonal tax office Bern (FAQ PDF
Geschäftsfahrzeug).

**GAP list** (we have nothing for CH yet; Körlogg 2.6 supports CH)

1. **Privatanteil Geschäftsauto 2026: 0,9 % pauschal oder Fahrtenbuch?** [borrowed
   subject] · term: *privatanteil geschäftsauto*, *0.9 prozent geschäftsauto* · why:
   the core CH decision; only treuhand/ERP blogs cover it. Worked CHF example and when
   the effective method (Fahrtenbuch) pays. Sources: ESTV Merkblatt N1/2007 (as
   amended 2022), Wegleitung zum Lohnausweis Rz 20–21, BKV (SR 642.118.1) Art. 5a.
   Check the claimed ">50 % business use" condition; one source states it, others don't.
2. **Fahrtenbuch Schweiz: was die Steuerverwaltung sehen will** [borrowed subject] ·
   term: *fahrtenbuch schweiz* · why: no clear owner. Self-employed must prove business
   km. Sources: ESTV, cantonal guides (Bern FAQ Geschäftsfahrzeug), Weka.
3. **Kilometerentschädigung Schweiz 2026: was ist üblich und was ist steuerfrei?**
   [borrowed subject] · term: *kilometerentschädigung schweiz*, *kilometergeld
   schweiz* · why: bexio ranks with a soft article. Explain that there is no single
   statutory rate (Spesenreglement; 70 Rp/km is common for the Fahrkostenabzug
   effective method — verify) and the Lohnausweis effect. Sources: ESTV Wegleitung
   Lohnausweis, Spesenreglement templates of cantonal offices, BKV Art. 5.
4. **Fahrkostenabzug 2026: Bundessteuer-Maximum und Kantone** [borrowed subject] ·
   term: *fahrkostenabzug 2026* · why: tax-season volume; commute km from the log.
   Check the current federal cap (CHF 3,200 or as adjusted for inflation) at ESTV.
   Sources: DBG Art. 26, BKV Art. 5.

## Netherlands (NL)

**Competitor pages**

| Title | URL | Type |
|---|---|---|
| Belastingdienst kilometervergoeding 2026 (+2025, 2023) | driversnote.nl/blog/belastingdienst-kilometervergoeding-2026 | yearly rate |
| Reiskostenvergoeding Belastingdienst gids (hub) | driversnote.nl/reiskostenvergoeding-belastingdienst-gids | hub: bedrijven, tarieven, werkgevers, werknemers, zzp'ers, rittenregistratie |
| Gratis formulier kilometerregistratie Belastingdienst | driversnote.nl/blog/gratis-formulier-kilometerregistratie-belastingdienst | template |
| Beste rittenregistratie app | driversnote.nl/blog/beste-ritten-registratie-app | app comparison |
| Hoe schrijf je een zakelijke auto af | driversnote.nl/blog/hoe-schrijf-je-een-zakelijke-auto-af-… | adjacent |
| Mobiliteitsbudget voor werknemers / slimme aftrekposten zzp | driversnote.nl/blog/… | adjacent |
| ~60 single-question posts (500 km grens, bewaartermijn, afgekeurd, Keurmerk RRS, lease vs eigen auto, handmatig toegestaan 2026?) | fleetgo.nl/blog/… | FAQ farm |
| Belastingdienst publiceert modellen rittenregistratie auto van de zaak (Sep 2024) | accountancyvanmorgen.nl/2024/09/10/… | news |

**Ranking signal**: "rittenregistratie belastingdienst" → Taxence, Accountancy van
Morgen (×2: the 2024 models; a court case where missing addresses kept the
bijtelling), overheid.nl, Rendement, Taxlive. Court cases and the 2024 Belastingdienst
models carry this term.

**GAP list**

1. **Rittenregistratie volgens het model van de Belastingdienst (gratis Excel)**
   [borrowed subject] · term: *rittenregistratie model belastingdienst*,
   *rittenregistratie excel* · why: the Belastingdienst published model registrations
   in Sept 2024. A template that follows them column by column is the best possible
   answer to the template intent. Sources: belastingdienst.nl "Rittenregistratie
   bijhouden" + the model files, Wet LB 1964 art. 13bis.
2. **Verklaring geen privégebruik: aanvragen, intrekken, controle** [borrowed subject]
   · term: *verklaring geen privégebruik* · why: planned 20 Nov. High volume, official
   pages are dry. Sources: belastingdienst.nl verklaring geen privégebruik auto,
   formulier.
3. **Bijtelling 2026: percentages en de elektrische auto** [borrowed subject] · term:
   *bijtelling 2026* · why: planned 1 Dec; very high volume. Keep it tight and link to
   the 500 km page. Sources: belastingdienst.nl bijtelling, Wet LB art. 13bis (2026
   percentages, EV cap).
4. **Rittenregistratie achteraf reconstrueren: kan dat?** [borrowed subject; FleetGO
   asks it, court cases answer it] · term: *rittenregistratie achteraf*,
   *rittenregistratie afgekeurd* · why: Rb. Noord-Nederland accepted a reconstruction;
   Rb. Den Haag rejected a log without addresses. Real case law, which nobody explains
   well. Sources: rechtspraak.nl ECLI numbers (look them up), Belastingdienst.
5. **Bestelauto: verklaring uitsluitend zakelijk gebruik en rittenregistratie**
   [borrowed subject] · term: *verklaring uitsluitend zakelijk gebruik bestelauto* ·
   why: a separate regime from the 500 km rule; many zzp users drive vans. Sources:
   belastingdienst.nl bestelauto, Wet LB art. 13bis lid 6.

## United Kingdom (UK)

**Competitor pages** (Driversnote .co.uk, ~100 URLs): yearly "HMRC mileage rate
2023/24/25/26" posts, yearly "advisory fuel rates 2023/24/25/26" posts, the
`hmrc-mileage-guide` hub (current rates, mileage allowance relief, claim MAR,
self-employed mileage, car allowances, salary sacrifice), free mileage log book
template, VAT on mileage, simplified expenses, BIK company cars, EV company car tax,
P87 dictionary entry, grey-fleet hub (6 pages, B2B), rideshare hub (Uber),
`/dictionary/` (14 glossary entries). MileIQ UK: a few old blog posts
(commuting rules, motoring expenses).

**Ranking signal**: "HMRC mileage rates 2026/27" → webexpenses, Cintra ×2, Hillier
Hopkins ×2, thehrdirector, makesworth. These are payroll and accounting firms, and
the 55p change (May 2026) brought a news wave. Our page already has 55p/25p and the
6 April 2026 split.

**GAP list** (UK and DE have planned slots every Tuesday and Friday; these are the
ones competitors prove)

1. **Advisory fuel rates (AFR) from 1 December 2026 – company car fuel per mile**
   [borrowed subject] · term: *advisory fuel rates* · why: changes every quarter, and
   Driversnote keeps a yearly URL. Planned 13 Nov; make it one evergreen URL updated
   every quarter with a dated history table. Sources: gov.uk "Advisory fuel rates"
   (quarterly table), the advisory electricity rate.
2. **Mileage Allowance Relief: claim the difference between 55p and what your
   employer pays (P87)** [borrowed subject] · term: *mileage allowance relief*,
   *p87 mileage* · why: planned 3 Nov. The 55p rise means more employees are now
   under-reimbursed, so the topic has just gained relevance. Sources: gov.uk "Claim tax
   relief for your job expenses: vehicles", HMRC EIM31200 ff., form P87.
3. **Claiming VAT on mileage: the fuel element and receipts** [borrowed subject] ·
   term: *vat on mileage* · why: not in our plan. Steady volume; the log + AFR + fuel
   receipts link is exactly our report. Sources: HMRC VAT Notice 700/64, gov.uk AFR.
4. **Self-employed mileage: simplified expenses vs actual costs** [borrowed subject]
   · term: *self employed mileage claim* · why: planned 6 Nov and 27 Nov as two pages.
   Consider one strong page with a worked comparison. Sources: gov.uk simplified
   expenses (vehicles), BIM75005, BIM47700.
5. **Temporary workplace and the 24-month rule** [borrowed subject] · term: *24 month
   rule hmrc* · why: planned 17 Nov; decides whether a journey is business or
   commuting, which is at the heart of a trip log. Sources: HMRC 490 (Employee travel),
   EIM32075 ff.

## United States (US, from 17 Nov 2026)

**Competitor pages**: Driversnote `irs-mileage-guide` hub (16 chapters: current rate,
historical rates, calculate reimbursement, California reimbursement, how to claim,
is reimbursement taxable, medical & charity, log requirements, employers, employees,
self-employed, standard vs actual), yearly "IRS mileage rate 2023/24/25/26" blog
posts, IRS log template (PDF/Excel/Sheets), mandatory reimbursement states, gig-driver
hub (~19 pages: DoorDash/Uber/Lyft/Instacart/Spark taxes and requirements),
small-business tax hub, `/dictionary/` (~24 entries), FAVR, ROI calculator. MileIQ
`/mileage-guide/` (~45): current rates, historical rates, commuting, medical,
charitable, per-state reimbursement (CA, IL, MA), car allowance. Everlance:
business-mileage hub (rate, template), per-state rate pages, per-occupation pages,
tax / savings calculators, "2026 IRS mileage rate prediction".

**Ranking signal**: "IRS mileage rate 2026" → driversnote.com.au(!), Paylocity, IFEBP,
Timeero, **irs.gov** (news release, two languages), SparkReceipt, Everlance. Secondary
sources report a **mid-year change to 76¢ from 1 July 2026 (Announcement 2026-11)**.
MileIQ still showed only 72.5¢ (updated Jan 2026). "mileage log template IRS free" →
driversnote.com.au, IONOS ×3, Everlance, plus template farms.

**GAP list** (calculator, log requirements and template are done/queued)

1. **IRS mileage rate 2026: 72.5¢ to June 30, 76¢ from July 1** [borrowed subject] ·
   term: *irs mileage rate 2026*, *irs mileage rate* · why: the biggest term in the
   whole field. Several ranking pages are stale on the mid-year change, and our
   calculator already has the facts. A dedicated rate page with a historical table
   (2020→2026) and links to the calculator. Publish the 2027 version the day the IRS
   announces (usually mid-December). Sources: IRS IR-2025-128, IRS Announcement
   2026-11 (**read the primary text before publishing**), irs.gov/tax-professionals/
   standard-mileage-rates, Rev. Proc. 2019-46.
2. **Standard mileage rate vs actual expenses: which saves more?** [borrowed subject]
   · term: *standard mileage vs actual expenses* · why: both majors have it; decision
   pages convert. Include the "must choose standard in year 1" rule. Sources: IRS Pub
   463 ch. 4, Rev. Proc. 2019-46.
3. **Gig driver mileage: what Uber, Lyft and DoorDash drivers can deduct** [borrowed
   subject, one page not a hub] · term: *doordash mileage deduction*, *uber driver
   mileage* · why: Driversnote's largest US hub targets this; gig drivers are heavy
   loggers. One honest page, not 19. Sources: IRS Gig Economy Tax Center, Pub 463,
   Schedule C instructions (line 9).
4. **Is mileage reimbursement required? State rules (California Labor Code 2802 and
   others)** [borrowed subject] · term: *is mileage reimbursement required by law* ·
   why: employee intent with high volume; MileIQ/Driversnote split it into per-state
   pages, but we keep it as one page with a table. Sources: CA Labor Code § 2802, IL
   820 ILCS 115/9.5, MA 940 CMR / M.G.L. c.149 §148, DOL FLSA minimum-wage rule.
5. **Medical and charity miles 2026 (20.5¢ / 23.5¢ and 14¢)** [borrowed subject] ·
   term: *medical mileage rate 2026* · why: smaller but uncontested facts; our trip
   categories can cover it. Could be a section of #1 instead. Sources: IR-2025-128,
   Announcement 2026-11, IRC § 170(i) (charity rate fixed by statute).

## Poland (PL)

**Competitor pages**: driversnote.pl has **no guides**. Ranking domains for
"kilometrówka 2026": infor.pl, firmove.pl, autobaza.pl, link4, fakturownia, rankomat,
inewi, fakturaxl (with a calculator). Sources disagree on whether the employee's
ewidencja is still required, and a reform of the rates (by kW and drive type) is
announced but not in force.

**GAP list**

1. **Ewidencja przebiegu pojazdu (VAT-26): 100 % odliczenia VAT – wzór i wymagania**
   [borrowed subject] · term: *ewidencja przebiegu pojazdu*, *ewidencja przebiegu
   pojazdu wzór* · why: a hard legal requirement (art. 86a ust. 6–7 ustawy o VAT) for
   cars used only for business. The log must be continuous, with odometer readings,
   and our export can match it exactly. Sources: ustawa o VAT art. 86a, VAT-26 form
   (podatki.gov.pl), Krajowa Informacja Skarbowa interpretations.
2. **Kilometrówka 2026: stawki 0,89 zł i 1,15 zł oraz zapowiadana reforma** [borrowed
   subject] · term: *kilometrówka 2026* · why: the sources contradict each other,
   and the reform makes freshness pay. Sources: Rozporządzenie Ministra
   Infrastruktury z 22.12.2022 (Dz.U. 2023 poz. 5), the draft reform on gov.pl/RCL
   (check status).
3. **Samochód w firmie: 75 % czy 20 % kosztów – kiedy potrzebna jest ewidencja**
   [borrowed subject] · term: *samochód w firmie 75 czy 20* · why: the decision every
   JDG owner faces. Sources: ustawa o PIT art. 23 ust. 1 pkt 46a and 47, ustawa o VAT
   art. 86a.
4. **Ewidencja przebiegu dla pracownika (prywatny samochód w delegacji)** [borrowed
   subject] · term: *ewidencja przebiegu pojazdu pracownika* · why: resolve the
   "abolished in 2019" confusion with the actual legal text. Sources: ustawa o PIT
   art. 21 ust. 1 pkt 23b, rozporządzenie MPiPS (podróże służbowe).

## Hungary (HU)

**Competitor pages**: no app maker publishes HU content. Ranking domain: adozona.hu
(articles on kiküldetési rendelvény and km-pénz; several old). NAV publishes a
monthly fuel price (üzemanyagár) that every útnyilvántartás calculation needs.

**GAP list**

1. **Útnyilvántartás 2026: mit kell tartalmaznia (NAV)** [borrowed subject] · term:
   *útnyilvántartás*, *útnyilvántartás minta* · why: no app competitor; a template
   (minta) + requirements page can lead the term. Sources: Szja tv. 3. számú melléklet
   (útnyilvántartás), NAV information booklet "Gépjárművel kapcsolatos költségek
   elszámolása" (2026 edition).
2. **Kiküldetési rendelvény és km-térítés 2026: normaköltség + NAV üzemanyagár**
   [borrowed subject] · term: *kiküldetési rendelvény 2026*, *km költségtérítés 2026*
   · why: tax-free reimbursement via rendelvény is the common case. Check the current
   általános személygépkocsi-normaköltség (it was 9 Ft/km in old articles; confirm the
   2026 figure at NAV). Sources: NAV, 60/1992 Korm. rendelet (fogyasztási normák).
3. **NAV üzemanyagár 2026 – havi táblázat** [own idea] · term: *nav üzemanyagár* ·
   why: monthly recurring searches; a small, always-current table can earn links.
   **Only if we can update it every month without fail** (a stale table is worse than
   none). Sources: nav.gov.hu üzemanyagárak.

---

## Ranked top 10 across all countries (expected value)

1. **US – IRS mileage rate 2026 (72.5¢ → 76¢ from July 1)**: largest term in the
   field, competitors stale on the mid-year change, launches with the US 3.0.
2. **DE – Firmenwagenrechner (1 % vs Fahrtenbuch) on the existing comparison page**:
   both main competitors use a calculator as their best converter; this links directly to starting a log.
3. **NO – Firmabil with electronic kjørebok: taxed at 3,40 kr/km in 2026**: a new rule
   that requires exactly what Körlogg is, and no app maker covers it (driversnote.no has zero guides).
4. **PL – Ewidencja przebiegu pojazdu (VAT-26) wzór i wymagania**: a legal must-have
   for 100 % VAT, with no app competitor content.
5. **NL – Rittenregistratie following the Belastingdienst model (free Excel)**:
   template intent + 2024 official models + case law.
6. **SE – Körjournal mall following Skatteverket's example headings**: proven
   template intent; Skatteverket itself tells readers to check the headings.
7. **UK – Advisory fuel rates, one evergreen URL updated quarterly**: recurring
   traffic, and Driversnote shows it pays.
8. **CH – Privatanteil Geschäftsauto 0,9 % oder Fahrtenbuch**: no app competitor at all.
9. **FI – Ajopäiväkirja: Verohallinnon vaatimukset + pohja**: the head term is owned
   by a paper-product listing.
10. **AT – Kilometergeld 2026 with the official BGBl source**: ranking pages contradict
    each other (0,50 vs 0,42 €), so a checked page can win.

## Three structural lessons from Driversnote and MileIQ

1. **Hub and chapters per country.** Each market has one pillar ("Skatteverket guide
   till milersättning", "IRS Mileage Guide", "HMRC mileage guide") with 6–16 chapter
   pages split by audience (employee / employer / self-employed / requirements /
   calculate / past rates), a breadcrumb into the hub and a sidebar listing every
   chapter on every page. korlogg.com guides are a flat list. Give each country index
   (/se/guider/, /de/ratgeber/, /guides/ …) a grouped structure ("Rules for your log",
   "Rates 2026", "Company car", "Self-employed") and add a "In this guide" chapter list
   to each page.
2. **Rates are a calendar, not an article.** They publish a new URL per year the day
   the authority announces (DK/FI 20–24 Nov, DE 22 Dec, US mid-Dec), keep old years
   as an archive, and win on timing even though the pages are thin (330–600 words, no
   official links, no examples). We should keep one evergreen URL per rate (our
   current pattern, which keeps links) with a dated history table. We must also put
   every authority's announcement date in the content calendar and publish within a
   day: IRS mid-Dec, HMRC AFR quarterly, SE/FI/DK/NO in Nov–Dec, NL in the
   Belastingplan, DE with the Jahressteuergesetz.
3. **Reusable assets carry the links.** Templates (PDF/Excel/Sheets), calculators
   and a single rate table are separate linkable things referenced from every
   requirements page. The glossary and the per-state / per-occupation pages are the
   filler part of their strategy. Skip those. Build one template and one calculator
   per country, and link them from every guide in that language.

## Not worth copying

- Per-state / per-occupation programmatic pages (Everlance, MileIQ): same text,
  different noun.
- One-question-per-URL FAQ farms (FleetGO): put the questions in FAQ sections of
  strong pages.
- Generic small-business blogs (MileIQ: food trucks, SEO tips, travel jobs): no topical
  fit, weakens the site.
- "Best X app" lists that rank yourself first: conflicts with "never game
  recommendations". The criteria page (no brands) covers the intent honestly.
