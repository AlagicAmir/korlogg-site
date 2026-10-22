# Redeeming Körlogg codes (internal)

Who gets what:
- **Accountants:** a lifetime Pro code for themselves (offer code on the lifetime purchase).
- **Their clients:** a "3 months Pro free" offer code on the yearly subscription. It renews at the normal price after the free period unless cancelled.

Public help page (no URLs below are on it): `/code/` (en), `/se/code/`, `/de/code/`, `/nl/code/`, built from `REDEEM` in `tools/content.py` by `tools/build.py`. Linked from the help and support pages, not from the main nav.

In the iOS app: Settings → "Redeem code" / "Lös in kod" / "Code einlösen" / "Code inwisselen" opens Apple's code sheet.

## Link formats

App Store (Körlogg, id 6809322275), one-time or custom offer codes:

    https://apps.apple.com/redeem?ctx=offercodes&id=6809322275&code=CODE

Google Play promo codes:

    https://play.google.com/redeem?code=CODE

`CODE` must be URL-encoded (the tool does it). Tapping the iOS link opens the App Store with the offer; if Körlogg is not installed, the App Store offers to install it first.

Do not put these formats on the website (Amir 2026-10-14) – send links or QR codes to the people who get codes.

## Tool: tools/redeem_links.py

Turns a list of codes into a CSV of links and one QR code PNG per code.

    # codes.txt: one code per line (blank lines and # comments skipped)
    python3 tools/redeem_links.py codes.txt --platform ios --out ~/Desktop/korlogg-codes
    pbpaste | python3 tools/redeem_links.py --platform android --out ~/Desktop/play-codes

Output in `--out`: `links.csv` (`code,link`) and `<code>.png` per code. QR images need the `qrcode` library (`pip3 install --user "qrcode[pil]"`); without it the script prints a note and still writes the CSV.

Keep code lists and the output outside this repo (the site is public).
