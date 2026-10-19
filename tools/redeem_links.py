#!/usr/bin/env python3
"""Turn Körlogg offer codes into redemption links and QR codes.

    python3 tools/redeem_links.py codes.txt --platform ios --out ~/Desktop/codes
    pbpaste | python3 tools/redeem_links.py --platform android --out /tmp/play-codes

Input: one code per line (from a file or stdin); blank lines and lines starting
with # are skipped, duplicates are written once. Output in --out:
  links.csv          code,link
  <code>.png         one QR code per code (needs `pip3 install --user "qrcode[pil]"`;
                     without it the CSV is still written and a note is printed)
See docs/redeem-codes.md. The links are for sending to people; they never go on
the website.
"""
import argparse, csv, pathlib, re, sys
from urllib.parse import quote

APP_ID = "6809322275"   # Körlogg on the App Store (same as tools/config.py)

def link(code, platform):
    c = quote(code, safe="")
    if platform == "ios":
        return f"https://apps.apple.com/redeem?ctx=offercodes&id={APP_ID}&code={c}"
    return f"https://play.google.com/redeem?code={c}"

def read_codes(src):
    seen, codes = set(), []
    for line in src:
        code = line.strip()
        if not code or code.startswith("#") or code in seen: continue
        seen.add(code); codes.append(code)
    return codes

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?", help="file with one code per line (default: stdin)")
    ap.add_argument("--platform", choices=("ios", "android"), required=True)
    ap.add_argument("--out", required=True, help="output folder (created if missing)")
    a = ap.parse_args()

    if a.file:
        with open(a.file, encoding="utf-8") as f: codes = read_codes(f)
    else:
        codes = read_codes(sys.stdin)
    if not codes: sys.exit("No codes found.")

    out = pathlib.Path(a.out).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    rows = [(c, link(c, a.platform)) for c in codes]
    with open(out / "links.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["code", "link"]); w.writerows(rows)
    print(f"{len(rows)} links -> {out / 'links.csv'}")

    try:
        import qrcode
    except ImportError:
        print('Note: the qrcode library is missing, so no QR images were written. '
              'Install it with: pip3 install --user "qrcode[pil]"')
        return
    for code, url in rows:
        name = re.sub(r"[^A-Za-z0-9_-]", "_", code) + ".png"
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
        qr.add_data(url); qr.make(fit=True)
        qr.make_image(fill_color="black", back_color="white").save(out / name)
    print(f"{len(rows)} QR codes -> {out}")

if __name__ == "__main__":
    main()
