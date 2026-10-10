#!/usr/bin/env python3
"""Build the site's images from the Körlogg app repo (read-only):
store screenshots -> assets/shots/<lang>/<n>-{400,800}.webp, app icon -> favicons,
and one 1200x630 share image per language -> assets/og/<lang>.png."""
import glob, pathlib, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = pathlib.Path.home() / "repo/Korlogg"
SHOTS = APP / "fastlane/screenshots_2_0"
ICON = APP / "Korlogg/Resources/Assets.xcassets/AppIcon.appiconset/icon-1024.png"
LOCALES = {"en": "en-GB", "sv": "sv", "de": "de-DE", "da": "da", "no": "no", "nl": "nl-NL", "fi": "fi", "pl": "pl"}
OG_LINES = {
    "en": ("Your mileage log for taxes", "– kept automatically."),
    "sv": ("Automatisk körjournal", "för förmånsbil och", "milersättning."),
    "de": ("Ihr Fahrtenbuch fürs Finanzamt", "– automatisch geführt."),
    "da": ("Kørebog til skatten", "– helt automatisk."),
    "no": ("Kjørebok for skatten", "– helt automatisk."),
    "nl": ("Rittenregistratie voor de", "Belastingdienst – vanzelf."),
    "fi": ("Ajopäiväkirja verotusta", "varten – automaattisesti."),
    "pl": ("Ewidencja przebiegu do VAT", "i kilometrówki – sama."),
}

def webp(src: Image.Image, out: pathlib.Path, width: int, q=78):
    h = round(src.height * width / src.width)
    tmp = out.with_suffix(".tmp.png")
    src.resize((width, h), Image.LANCZOS).save(tmp)
    subprocess.run(["cwebp", "-quiet", "-q", str(q), "-m", "6", str(tmp), "-o", str(out)], check=True)
    tmp.unlink()

def shots():
    for lang, loc in LOCALES.items():
        d = ROOT / "assets/shots" / lang; d.mkdir(parents=True, exist_ok=True)
        for f in sorted(glob.glob(str(SHOTS / loc / "*_APP_IPHONE_69_*.png"))):
            n = pathlib.Path(f).name.split("_")[0]
            im = Image.open(f).convert("RGB")
            for w in (400, 800):
                webp(im, d / f"{n}-{w}.webp", w)

def icons():
    d = ROOT / "assets"; d.mkdir(exist_ok=True)
    ic = Image.open(ICON).convert("RGBA")
    # iOS-style rounded mask for the favicon and header logo (the store icon is square)
    def rounded(size):
        im = ic.resize((size, size), Image.LANCZOS)
        m = Image.new("L", (size * 4, size * 4), 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, size * 4 - 1, size * 4 - 1), radius=int(size * 4 * 0.225), fill=255)
        im.putalpha(m.resize((size, size), Image.LANCZOS)); return im
    ic.convert("RGB").resize((180, 180), Image.LANCZOS).save(d / "apple-touch-icon.png", optimize=True)
    rounded(32).save(d / "favicon-32.png", optimize=True)
    rounded(192).save(d / "icon-192.png", optimize=True)
    rounded(512).save(d / "icon-512.png", optimize=True)
    r = rounded(96); r.save(d / "logo-96.png", optimize=True)
    subprocess.run(["cwebp", "-quiet", "-q", "85", "-alpha_q", "100", str(d / "logo-96.png"), "-o", str(d / "logo-96.webp")], check=True)
    rounded(48).save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    return rounded

def og(rounded):
    d = ROOT / "assets/og"; d.mkdir(parents=True, exist_ok=True)
    bold = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 64, index=1)
    big = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 54, index=1)
    for lang, loc in LOCALES.items():
        W, H = 1200, 630
        bg = Image.new("RGB", (W, H))
        top, bot = (15, 55, 121), (30, 116, 220)
        px = ImageDraw.Draw(bg)
        for y in range(H):
            t = y / H
            px.line([(0, y), (W, y)], fill=tuple(round(a + (b - a) * t) for a, b in zip(top, bot)))
        shot = Image.open(SHOTS / loc / "1_APP_IPHONE_69_1.png").convert("RGB")
        phone = shot.crop((90, 560, 1230, 2868))           # the phone, without the headline
        ph = phone.resize((round(phone.width * 700 / phone.height), 700), Image.LANCZOS)
        bg.paste(ph, (W - ph.width - 40, 70))
        ic = rounded(120)
        bg.paste(ic, (70, 80), ic)
        dr = ImageDraw.Draw(bg)
        dr.text((210, 108), "Körlogg", font=bold, fill="white")
        lines = OG_LINES[lang]
        y0 = 300 if len(lines) == 2 else 262
        for i, line in enumerate(lines):
            dr.text((70, y0 + 68 * i), line, font=big, fill="white")
        dr.text((70, 520), "korlogg.com", font=ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 34), fill=(205, 222, 248))
        bg.save(d / f"{lang}.png", optimize=True)
        subprocess.run(["pngquant", "--force", "--quality", "70-90", "--ext", ".png", str(d / f"{lang}.png")], check=False)

RAW = APP / "fastlane/raw_2_0"
HERO_RAW = {"en": "en_trips", "sv": "sv_trips", "de": "de_trips_DE", "da": "da_trips", "no": "nb_trips",
            "nl": "nl_trips", "fi": "fi_trips", "pl": "pl_trips"}

def hero():
    """Unframed trip-list screens for the CSS phone frame in the hero."""
    d = ROOT / "assets/hero"; d.mkdir(parents=True, exist_ok=True)
    for lang, name in HERO_RAW.items():
        im = Image.open(RAW / f"{name}.png").convert("RGB")
        for w in (360, 720):
            webp(im, d / f"{lang}-{w}.webp", w, q=82)

if __name__ == "__main__":
    shots(); r = icons(); og(r); hero()
    print("done")
