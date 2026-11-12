# Links to korlogg.com: ready-to-paste texts (2026-11-12)

Goal: a handful of real pages that mention **Körlogg** by name and link to
`https://korlogg.com/se/` (Swedish) or `https://korlogg.com/` (English).
Amir submits these himself; each needs an account or a sent email.
Check every fact against the live site on the day you post.

## 1. korlogg.se (do this first, 5 minutes)

Today `korlogg.se` points at 188.66.62.59, which answers with the default
"Synology Web Station" page and an expired certificate. `www.korlogg.se` has
no DNS record. DNS is at Loopia.

Fix in Loopia Kundzon → Domännamn → korlogg.se:

- Turn on **Vidarebefordran** (URL forwarding) for `korlogg.se` and
  `www.korlogg.se` to `https://korlogg.com/se/`, type **301 permanent**.
- Remove the A record to 188.66.62.59 if Loopia does not replace it itself.

Check afterwards: `curl -sI http://korlogg.se` should show `301` and
`Location: https://korlogg.com/se/`.

## 2. App directories (English)

Use the same wording everywhere so the brand reads the same on every page.

**Name:** Körlogg
**Website:** https://korlogg.com/
**Platforms:** iPhone, iPad, Android
**Category:** Mileage tracker / Business / Finance

**Tagline (60 characters):**
Automatic mileage log with no account and no server

**Short description:**
Körlogg is an automatic mileage log app. It notices when you start driving,
measures the trip with GPS and ends it when the car has stood still. You swipe
each trip business or private and export the log as PDF or Excel with date,
addresses, distance, purpose and odometer readings.

**Longer description:**
Körlogg records car trips by itself; you never start or stop anything. Each
trip is marked business or private with one swipe. The app works out the
mileage allowance with the country's official rates and builds the monthly
and yearly report for the tax office and the employer. Country rules are built
in for Sweden, the UK, Germany, Austria, the Netherlands, Denmark, Norway,
Finland and Poland. There is no account and no Körlogg server: trips stay on
the phone, or in your own iCloud if you turn on sync. Logging is free and
unlimited; Körlogg Pro (subscription or one-time purchase) adds PDF and Excel
export, several cars and drivers and Bluetooth beacon logging. Made in Sweden.

Where to post:

| Site | What to do |
|---|---|
| alternativeto.net | Add Körlogg as an application, then mark it as an alternative to Driversnote, MileIQ and Mileage Book |
| producthunt.com | Launch as a product; first comment = the short description plus why you built it |
| saashub.com | Submit product, list Driversnote and MileIQ as competitors |
| slant.co / appagg.com | Optional, same texts |

Most of these mark their links nofollow. They are still worth doing: they
are indexed pages that tie the name Körlogg to the domain.

## 3. Swedish outreach (worth more than the directories)

Who to write to: accounting firms and bookkeeping blogs that explain
körjournal or milersättning, company-car blogs, small-business newsletters,
and Swedish app or tech blogs. Offer something useful to their readers, not a
link request.

**Ämne:** Körjournal utan konto – tips till era läsare?

Hej!

Jag heter Amir och har byggt Körlogg, en svensk app som för körjournalen
automatiskt. Jag såg er artikel om [körjournal / milersättning / förmånsbil]
och tänkte att den här jämförelsen kan vara till nytta för era läsare:

https://korlogg.com/se/guider/jamfor-korjournal-appar/

Den jämför Körlogg, Driversnote, Mileage Book och GPS-box, med varje uppgift
hämtad från tillverkarens egen sida och datum för kontrollen. Vi skriver också
rakt ut när en annan lösning passar bättre.

Om ni vill testa Körlogg Pro skickar jag gärna en kod. Och hittar ni något fel
i guiden rättar jag det direkt.

Vänliga hälsningar
Amir Alagic
support@korlogg.com

## 4. Search Console (after the next deploy)

- URL Inspection → Request indexing for `https://korlogg.com/se/`,
  `/se/guider/jamfor-korjournal-appar/` and `/se/guider/alternativ-till-driversnote/`.
- Performance → filter query `körlogg` and `körjournal`; note position and
  impressions now, compare in four weeks.
