#!/usr/bin/env python3
"""QR codes for the home-page hero (desktop only): assets/qr/<lang>.svg, each pointing
to that language's App Store link with the campaign web_<lang>_qr. Made locally with
the `qrcode` package (pip install qrcode); no external service. Re-run only when the
App Store link changes, then `python3 tools/build.py`.

    python3 tools/qr.py
"""
import pathlib, re, sys
import qrcode, qrcode.image.svg

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build
from content import LANGS

OUT = build.ROOT / "assets/qr"

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for lang in LANGS:
        url = build.store_url(lang, f"web_{lang}_qr")
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=2,
                           image_factory=qrcode.image.svg.SvgPathImage)
        qr.add_data(url); qr.make(fit=True)
        svg = qr.make_image().to_string(encoding="unicode")
        # crisp, unitless, white background so it scans in dark mode too
        svg = re.sub(r'width="[^"]*mm" height="[^"]*mm" ', "", svg, count=1)
        svg = svg.replace("<path ", '<rect width="100%" height="100%" fill="#fff"/><path shape-rendering="crispEdges" ', 1)
        (OUT / f"{lang}.svg").write_text(svg)
        print(lang, url)

if __name__ == "__main__":
    main()
