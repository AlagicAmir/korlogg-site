#!/usr/bin/env python3
"""Build korlogg.com: plain HTML into the repo root (served by GitHub Pages from main).

    python3 tools/build.py

Sources: tools/content.py (marketing copy), src/legal/<lang>/*.html (privacy,
terms, support, deletion – ported from korklar-legal), src/guides/*.html,
src/help/help.json (tools/extract_help.py), assets/ (tools/images.py).
Switches: tools/config.py (KORLOGG_2_0_RELEASED and the support email).
"""
import html, json, pathlib, re, shutil, sys
from datetime import date

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import config as C
from content import LANGS, UI, HOME, HELP_LANG, BEACON_SHOTS, BEACON_HERO_SHOT, COUNTRY_LIST, TAX, STORE_LABEL, SOURCE_WORD, SAVE, REDEEM

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
# The build date. Guides with a later `<!-- publish: YYYY-MM-DD -->` are left out
# entirely (no page, no index entry, no sitemap, no hreflang) until that day;
# `--as-of YYYY-MM-DD` builds the site as it will look on another day (preview only).
TODAY = (sys.argv[sys.argv.index("--as-of") + 1] if "--as-of" in sys.argv else date.today().isoformat())
GENERATED = [l["prefix"].strip("/") for k, l in LANGS.items() if k != "en"] + \
            ["help", "support", "privacy", "terms", "delete-data", "guides", "code"]

# --------------------------------------------------------------------- pages
PAGES = []          # dicts: lang, cluster, path, title, desc, body, noindex, canonical, jsonld, og
CLUSTERS = {}       # cluster -> {lang: path}  (only indexable pages)

def add(lang, cluster, path, title, desc, body, noindex=False, canonical=None, jsonld=None, main_class=""):
    PAGES.append(dict(lang=lang, cluster=cluster, path=path, title=title, desc=desc, body=body,
                      noindex=noindex, canonical=canonical or path, jsonld=jsonld or [], main_class=main_class))
    if not noindex and cluster:
        CLUSTERS.setdefault(cluster, {})[lang] = path

def P(lang, page):
    """Path of a standard page in a language."""
    pre = LANGS[lang]["prefix"]
    return pre if page == "home" else f"{pre}{page}/"

GUIDES = {   # file stem -> (lang, path, cluster)
    "en-which-ibeacon": ("en", "/guides/which-ibeacon/", "guide-beacon"),
    "sv-vilken-ibeacon": ("sv", "/se/guider/vilken-ibeacon/", "guide-beacon"),
    "de-welcher-ibeacon": ("de", "/de/ratgeber/welcher-ibeacon/", "guide-beacon"),
    "sv-korjournal-innehall": ("sv", "/se/guider/vad-ska-en-korjournal-innehalla/", None),
    "sv-formansbil-ringa-omfattning": ("sv", "/se/guider/formansbil-privat-korning-ringa-omfattning/", None),
    "de-fahrtenbuch-inhalt": ("de", "/de/ratgeber/was-muss-ein-fahrtenbuch-enthalten/", None),
    "de-fahrtenbuch-oesterreich": ("de", "/de/ratgeber/fahrtenbuch-oesterreich-sachbezug-kilometergeld/", None),
    "en-hmrc-mileage-log": ("en", "/guides/hmrc-mileage-log/", None),
    "en-hmrc-mileage-rates": ("en", "/guides/hmrc-mileage-rates-2026-27/", None),
    "en-commuting-vs-business": ("en", "/guides/commuting-vs-business-mileage/", None),
    "nl-rittenregistratie-inhoud": ("nl", "/nl/gidsen/rittenregistratie-wat-moet-erin/", None),
    "nl-500-km-prive": ("nl", "/nl/gidsen/500-km-prive-bewijzen/", None),
    "nl-kilometervergoeding-2026": ("nl", "/nl/gidsen/kilometervergoeding-2026/", None),
    "sv-automatisk-korjournal": ("sv", "/se/guider/automatisk-korjournal/", None),
    "sv-korjournal-enskild-firma": ("sv", "/se/guider/korjournal-enskild-firma/", None),
    "de-fahrtenbuch-oder-1-prozent": ("de", "/de/ratgeber/fahrtenbuch-oder-1-prozent-regelung/", None),
    "de-kilometerpauschale-2026": ("de", "/de/ratgeber/kilometerpauschale-2026/", None),
    "de-fahrtenbuch-vorlage-oder-app": ("de", "/de/ratgeber/fahrtenbuch-vorlage-oder-app/", None),
}
GUIDE_INDEX = {"en": "/guides/", "sv": "/se/guider/", "de": "/de/ratgeber/", "nl": "/nl/gidsen/"}
LEGAL_LANGS = {"en", "sv", "de", "nl", "fi"}      # privacy/terms exist in these languages
DELETE_LANGS = {"en", "sv", "de"}
REDEEM_LANGS = set(REDEEM)                        # "redeem a code" page (en, sv, de, nl)

def esc(s): return html.escape(s, quote=True)

def store_url(lang, campaign=None):
    """With a campaign, App Store Connect counts the downloads from that link:
    web_<lang>_<position>, e.g. web_de_hero (40 characters at most)."""
    cc = LANGS[lang]["store"]
    url = f"https://apps.apple.com/{cc + '/' if cc else ''}app/id{C.APP_ID}"
    return f"{url}?pt={C.PROVIDER_ID}&ct={campaign[:40]}&mt=8" if campaign else url

def v2_label(lang):
    return UI[lang]["v2_released" if C.KORLOGG_2_0_RELEASED else "v2_pending"]

BADGE_W = {}   # badge width per language at height 40 (from Apple's SVG)

def badge_width(lang):
    if lang not in BADGE_W:
        svg = (ROOT / f"assets/badges/{lang}-black.svg").read_text()
        BADGE_W[lang] = float(re.search(r'width="([0-9.]+)"', svg).group(1))
    return BADGE_W[lang]

def store_button(lang, extra="", dark_bg=False, position="other", campaign=None):
    """Apple's official localized badge, unmodified. Black on light backgrounds, white
    in dark mode; always black on the blue hero (dark_bg=False keeps black)."""
    h = 44 if "small" in extra else 54
    w = round(badge_width(lang) * h / 40)
    black, white = f"/assets/badges/{lang}-black.svg", f"/assets/badges/{lang}-white.svg"
    alt = esc(UI[lang]["store_btn"])
    dark = "" if dark_bg else f'<source srcset="{white}" media="(prefers-color-scheme: dark)">'
    return (f'<a class="store-badge{extra}" href="{esc(store_url(lang, campaign or f'web_{lang}_{position}'))}" data-position="{position}"><picture>{dark}'
            f'<img src="{black}" width="{w}" height="{h}" alt="{alt}"></picture></a>')

def placeholders(text, lang):
    def link(page, l):
        if page == "delete":
            l = l if l in DELETE_LANGS else "en"; return P(l, "delete-data")
        if page in ("privacy", "terms"):
            l = l if l in LEGAL_LANGS else "en"
        return P(l, page)
    for page in ("privacy", "terms", "support", "delete", "home", "help"):
        text = text.replace("{{%s}}@en" % page, link(page, "en"))
        text = text.replace("{{%s}}" % page, link(page, lang))
    return text

def shot_img(lang, n, alt, sizes="(min-width: 900px) 260px, 62vw", eager=False):
    base = f"/assets/shots/{lang}/{n}"
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img src="{base}-400.webp" srcset="{base}-400.webp 400w, {base}-800.webp 800w" sizes="{sizes}" '
            f'width="400" height="869" alt="{esc(alt)}" {load} decoding="async">')

def shot_numbers(lang):
    return sorted(int(p.name.split("-")[0]) for p in (ROOT / "assets/shots" / lang).glob("*-400.webp"))

# ------------------------------------------------------------------- layout
def layout(pg):
    lang, ui = pg["lang"], UI[pg["lang"]]
    L = LANGS[lang]
    url = C.SITE + pg["path"]
    alts = ""
    if not pg["noindex"] and pg["cluster"]:
        group = CLUSTERS[pg["cluster"]]
        for l, p in group.items():
            alts += f'<link rel="alternate" hreflang="{LANGS[l]["hreflang"]}" href="{C.SITE}{p}">\n'
            if l == "de":
                alts += f'<link rel="alternate" hreflang="de-AT" href="{C.SITE}{p}">\n'
        if "en" in group:
            alts += f'<link rel="alternate" hreflang="x-default" href="{C.SITE}{group["en"]}">\n'
    robots = '<meta name="robots" content="noindex, follow">\n' if pg["noindex"] else ""
    og_img = f"{C.SITE}/assets/og/{lang}.png"
    jsonld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>\n' for j in pg["jsonld"])
    home = P(lang, "home")
    guides_link = f'<a href="{GUIDE_INDEX[lang]}">{esc(ui["nav_guides"])}</a>' if lang in GUIDE_INDEX else ""
    # language switcher: same page in other languages when it exists, else that language's home
    group = CLUSTERS.get(pg["cluster"], {}) if pg["cluster"] else {}
    items = "".join(
        f'<li><a href="{group.get(l, P(l, pg["cluster"]) if pg["cluster"] in ("help", "support", "privacy", "terms") else P(l, "home"))}" hreflang="{v["hreflang"]}" lang="{v["html"]}"'
        f'{" aria-current=\"true\"" if l == lang else ""}>{v["name"]}</a></li>' for l, v in LANGS.items())
    foot_legal = (f'<a href="{P(lang, "privacy")}">{esc(ui["privacy"])}</a>'
                  f'<a href="{P(lang, "terms")}">{esc(ui["terms"])}</a>'
                  f'<a href="{P(lang, "support")}">{esc(ui["support"])}</a>'
                  f'<a href="{P(lang, "help")}">{esc(ui["help"])}</a>'
                  + (f'<a href="{GUIDE_INDEX[lang]}">{esc(ui["guides"])}</a>' if lang in GUIDE_INDEX else ""))
    return f"""<!doctype html>
<html lang="{L["html"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(pg["title"])}</title>
<meta name="description" content="{esc(pg["desc"])}">
{robots}<link rel="canonical" href="{C.SITE}{pg["canonical"]}">
{alts}<meta name="apple-itunes-app" content="app-id={C.APP_ID}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#1669d9" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0b1220" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Körlogg">
<meta property="og:title" content="{esc(pg["title"])}">
<meta property="og:description" content="{esc(pg["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{ {"en": "en_GB", "sv": "sv_SE", "de": "de_DE", "da": "da_DK", "no": "nb_NO", "nl": "nl_NL", "fi": "fi_FI", "pl": "pl_PL"}[lang] }">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(pg["title"])}">
<meta name="twitter:description" content="{esc(pg["desc"])}">
<meta name="twitter:image" content="{og_img}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/assets/favicon-32.png" type="image/png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/assets/site.css?v={CSS_VERSION}">
<link rel="preconnect" href="https://nom.telemetrydeck.com" crossorigin>
<script src="https://cdn.telemetrydeck.com/websdk/telemetrydeck.min.js" data-app-id="{C.TELEMETRYDECK_APP_ID}" defer></script>
<script src="/assets/stats.js?v={STATS_VERSION}" defer></script>
{pg.get("head", "")}{jsonld}</head>
<body>
<a class="skip" href="#main">{esc(ui["skip"])}</a>
<header class="site-header">
<div class="wrap bar">
<a class="brand" href="{home}"><img src="/assets/logo-96.webp" width="32" height="32" alt=""><span>Körlogg</span></a>
<nav class="nav" aria-label="Körlogg">
<a href="{home}#features">{esc(ui["nav_features"])}</a>
<a href="{P(lang, "help")}">{esc(ui["nav_help"])}</a>
{guides_link}
<a href="{P(lang, "support")}">{esc(ui["nav_support"])}</a>
</nav>
<a class="get-app" href="{esc(store_url(lang, f"web_{lang}_header"))}" data-position="header">{esc(ui["get_app"])}</a>
<details class="lang">
<summary aria-label="{esc(ui["lang_label"])}"><svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zm-9 9h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg><span>{lang.upper()}</span></summary>
<ul>{items}</ul>
</details>
</div>
</header>
<main id="main" class="{pg["main_class"]}">
{pg["body"]}
</main>
<footer class="site-footer">
<div class="wrap">
<div class="foot-top">
<a class="brand" href="{home}"><img src="/assets/logo-96.webp" width="28" height="28" alt="" loading="lazy"><span>Körlogg</span></a>
{store_button(lang, " small", position="footer")}
</div>
<nav class="foot-links" aria-label="{esc(ui["support"])}">{foot_legal}</nav>
<p>{esc(ui["independent"])}</p>
<p>{esc(ui["publisher"])} <a href="mailto:{C.SUPPORT_EMAIL}">{C.SUPPORT_EMAIL}</a></p>
<ul class="foot-langs">{"".join(f'<li><a href="{P(l, "home")}" hreflang="{v["hreflang"]}" lang="{v["html"]}">{v["name"]}</a></li>' for l, v in LANGS.items())}</ul>
<p class="small">Apple, the Apple logo, iPhone and iPad are trademarks of Apple Inc., registered in the U.S. and other countries. App Store is a service mark of Apple Inc.</p>
</div>
</footer>
</body>
</html>
"""

# ------------------------------------------------------------------ helpers
def app_jsonld(lang):
    h = HOME[lang]
    return {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Körlogg",
            "operatingSystem": "iOS, iPadOS", "applicationCategory": "BusinessApplication",
            "description": h["desc"], "url": C.SITE + P(lang, "home"), "inLanguage": LANGS[lang]["html"],
            "image": f"{C.SITE}/assets/icon-512.png", "installUrl": store_url(lang), "downloadUrl": store_url(lang),
            "screenshot": [f"{C.SITE}/assets/shots/{lang}/{n}-800.webp" for n in shot_numbers(lang)[:4]],
            "author": {"@type": "Person", "name": "Amir Alagic"},
            "publisher": {"@type": "Person", "name": "Amir Alagic"}}

def breadcrumb(lang, items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": C.SITE + u}
                                for i, (n, u) in enumerate(items)]}

def _parse_guide(path):
    raw = path.read_text()
    meta = dict(re.findall(r"<!-- (\w+): (.*?) -->", raw))
    body = re.sub(r"<!-- \w+: .*? -->\n?", "", raw)
    return meta, body

def read_guide(stem):
    """The version of a guide that is live on TODAY. `src/guides/<stem>.html` is the
    guide; a queued rewrite of a live guide sits next to it as `<stem>@YYYY-MM-DD.html`
    with the same `publish` date and replaces it from that day (same URL)."""
    meta, body = _parse_guide(SRC / "guides" / f"{stem}.html")
    for rev in sorted((SRC / "guides").glob(f"{stem}@*.html")):
        m, b = _parse_guide(rev)
        if m.get("publish", rev.stem.split("@")[1]) <= TODAY:
            meta, body = m, b
    return meta, body

def is_live(stem):
    """False until the guide's own publish date (a guide without one is live)."""
    return _parse_guide(SRC / "guides" / f"{stem}.html")[0].get("publish", "") <= TODAY

def play_url(lang, campaign=None):
    """Google Play listing; the campaign goes into the install referrer (utm_campaign)."""
    hl = {"en": "en_GB", "sv": "sv", "de": "de", "nl": "nl", "da": "da", "no": "no", "fi": "fi", "pl": "pl"}[lang]
    ref = f"&referrer=utm_source%3Dkorlogg.com%26utm_medium%3Dweb%26utm_campaign%3D{campaign}" if campaign else ""
    return f"https://play.google.com/store/apps/details?id={C.PLAY_PACKAGE}&hl={hl}{ref}"

def alts(lang):
    h = HOME[lang]
    return h["alts_2_0_2"] if C.UK_RELEASED and "alts_2_0_2" in h else h["alts"]

def gallery(lang):
    h = HOME[lang]
    beacon = set(BEACON_SHOTS[lang])
    nums = [n for n in shot_numbers(lang) if C.KORLOGG_2_0_RELEASED or n not in beacon]
    figs = "".join(f'<li>{shot_img(lang, n, alts(lang)[n - 1])}</li>' for n in nums)
    return f'<ul class="gallery" role="list">{figs}</ul>'

# --------------------------------------------------------------------- home
def device(lang, alt, eager=True):
    base = f"/assets/hero/{lang}"
    load = 'fetchpriority="high" decoding="sync"' if eager else 'loading="lazy" decoding="async"'
    return (f'<div class="device"><img src="{base}-360.webp" srcset="{base}-360.webp 360w, {base}-720.webp 720w" '
            f'sizes="(min-width: 900px) 340px, 72vw" width="360" height="782" alt="{esc(alt)}" {load}></div>')

ICON_CLOCK = '<svg aria-hidden="true" viewBox="0 0 24 24" width="28" height="28"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 7v5l3.5 2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
ICON_COIN = '<svg aria-hidden="true" viewBox="0 0 24 24" width="28" height="28"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="5.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 9.5v5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'

def save_block(lang):
    s = SAVE[lang]
    def card(icon, item):
        big, line, calc = item
        return (f'<li class="save-card"><span class="save-icon">{icon}</span><p class="save-big">{esc(big)}</p>'
                f'<p class="save-line">{esc(line)}</p><p class="save-calc">{esc(calc)}</p></li>')
    src = " · ".join(f'<a href="{u}">{esc(n.split(" – ")[0])}</a>' for n, u in s["sources"])
    return (f'<div class="save" id="save"><h3>{esc(s["h2"])}</h3><ul class="save-cards" role="list">'
            f'{card(ICON_CLOCK, s["time"])}{card(ICON_COIN, s["money"])}</ul>'
            f'<p class="src">{esc(SOURCE_WORD[lang])}: {src}</p></div>')

def build_home(lang):
    h, ui, tx = HOME[lang], UI[lang], TAX[lang]
    full = lang in ("en", "sv", "de")
    trust = "".join(f'<li><svg aria-hidden="true" viewBox="0 0 20 20" width="18" height="18"><path fill="currentColor" d="M8.2 13.6 4.6 10l-1.2 1.2 4.8 4.8 9-9-1.2-1.2z"/></svg>{esc(t)}</li>' for t in h["trust"])
    at = (f'<p class="hero-note">{esc(h["at_note"])} <a href="https://apps.apple.com/at/app/id{C.APP_ID}?pt={C.PROVIDER_ID}&amp;ct=web_de_at&amp;mt=8">{esc(h["at_link"])}</a></p>'
          if lang == "de" else "")
    hero = f"""<section class="hero">
<div class="wrap hero-grid">
<div class="hero-text">
<h1>{esc(tx["h1"])}</h1>
<p class="lede">{esc(tx["lede"])}</p>
<div class="cta-row">{store_button(lang, dark_bg=True, position="hero")}{qr_block(lang)}</div>
<p class="hero-note">{esc(ui["platform"])}</p>
{at}
</div>
<div class="hero-shot">{device(lang, alts(lang)[0])}</div>
</div>
<div class="wrap"><ul class="trust" role="list">{trust}</ul></div>
</section>"""
    who = "".join(f'<li class="card who-card"><span class="who-n" aria-hidden="true">{i + 1}</span><h3>{esc(t)}</h3><p>{esc(x)}</p></li>'
                  for i, (t, x) in enumerate(tx["who"]["cards"]))
    whosec = f"""<section class="section" id="who">
<div class="wrap">
<h2 class="center">{esc(tx["who"]["h2"])}</h2>
<ul class="cards three" role="list">{who}</ul>
</div>
</section>"""
    m = tx["money"]
    if "rows" in m:
        rows = "".join(f'<tr><th scope="row">{esc(c)}</th><td>{esc(r)}</td><td><a href="{s[1]}">{esc(s[0].split(" – ")[0])}</a></td></tr>' for c, r, s in m["rows"])
        figures = (f'<div class="table-wrap"><table class="facts rates"><thead><tr><th scope="col">{esc(m["head"][0])}</th>'
                   f'<th scope="col">{esc(m["head"][1])}</th><th scope="col">{esc(SOURCE_WORD[lang])}</th></tr></thead><tbody>{rows}</tbody></table></div>')
        srcs = ""
    else:
        figures = '<ul class="stats" role="list">' + "".join(f'<li><span class="stat-v">{esc(v)}</span><span class="stat-l">{esc(l)}</span></li>' for v, l in m["stats"]) + "</ul>"
        srcs = f'<p class="src">{esc(SOURCE_WORD[lang])}: ' + " · ".join(f'<a href="{u}">{esc(t)}</a>' for t, u in m["sources"]) + "</p>"
    money = f"""<section class="section money" id="rates">
<div class="wrap narrow center">
<h2>{esc(m["h2"])}</h2>
<p class="section-intro">{esc(m["intro"])}</p>
{figures}
<p class="example">{esc(m["example"])}</p>
<p class="muted small-note">{esc(m["note"])}</p>
{srcs}
{save_block(lang)}
</div>
</section>"""
    feats = "".join(f'<li class="card"><h3>{esc(t)}</h3><p>{esc(x)}</p></li>' for t, x in h["features"])
    features = f"""<section id="features" class="section alt">
<div class="wrap">
<h2 class="center">{esc(h["features_h2"])}</h2>
<ul class="cards" role="list">{feats}</ul>
</div>
</section>"""
    b = h["beacon"]
    bshot = BEACON_HERO_SHOT.get(lang, 2)
    blist = "".join(f"<li>{esc(x)}</li>" for x in b["bullets"])
    blink = (f'<p><a class="more" href="{[p for s, (l, p, c) in GUIDES.items() if l == lang and c == "guide-beacon"][0]}">{esc(b["link"])} →</a></p>'
             if b.get("link") else "")
    beacon = f"""<section class="section" id="ibeacon">
<div class="wrap split">
<div>
<p class="badge">{esc(v2_label(lang))}</p>
<h2>{esc(b["h2"])}</h2>
<p>{esc(b["text"])}</p>
{f'<ul class="ticks">{blist}</ul>' if blist else ""}
{blink}
</div>
<div class="split-shot">{shot_img(lang, bshot, alts(lang)[bshot - 1], sizes="(min-width: 900px) 280px, 62vw")}</div>
</div>
</section>"""
    report = build_report_table(lang) if full else ""
    shots = f"""<section class="section alt" aria-label="Screenshots">
<div class="wrap">{gallery(lang)}</div>
</section>"""
    privacy = ""
    if "privacy" in h:
        privacy = f"""<section class="section privacy-band">
<div class="wrap narrow">
<h2>{esc(h["privacy"]["h2"])}</h2>
<p>{esc(h["privacy"]["text"])}</p>
<p><a class="more" href="{P(lang, "privacy")}">{esc(ui["privacy"])} →</a></p>
</div>
</section>"""
    if "pro" in h:
        pl = "".join(f"<li>{esc(x)}</li>" for x in h["pro"]["bullets"])
        pro = f"""<section class="section">
<div class="wrap narrow">
<h2>{esc(h["pro"]["h2"])}</h2>
<ul class="ticks cols">{pl}</ul>
<p class="muted">{esc(h["pro"]["note"])}</p>
</div>
</section>"""
    else:
        pro = f'<section class="section"><div class="wrap narrow"><h2>Körlogg Pro</h2><p>{esc(h["pro_note"])}</p></div></section>'
    guides = ""
    if lang in GUIDE_INDEX:
        items = ""
        for stem, (l, path, _) in GUIDES.items():
            if l != lang or not is_live(stem): continue
            meta, _b = read_guide(stem)
            items += f'<li class="card link-card"><a href="{path}"><h3>{re.search(r"<h1>(.*?)</h1>", _b).group(1)}</h3><p>{esc(meta["description"])}</p></a></li>'
        guides = f"""<div class="guides-block">
<h2>{esc(h["guides_h2"])}</h2>
<ul class="cards" role="list">{items}</ul>
</div>"""
    faq = build_home_faq(lang)
    helpsec = f"""<section class="section alt">
<div class="wrap">
<div class="narrow faq-block">
<h2>{esc(h["help_h2"])}</h2>
{faq}
<p>{esc(h["help_text"])} <a class="more" href="{P(lang, "help")}">{esc(ui["help"])} →</a></p>
</div>
{guides}
</div>
</section>"""
    cta = f"""<section class="section cta-band">
<div class="wrap narrow center">
<h2>{esc(h["cta_h2"])}</h2>
<p>{esc(h["cta_text"])}</p>
{store_button(lang, position="end")}
<p class="hero-note">{esc(ui["platform"])}</p>
</div>
</section>"""
    mid = f"""<section class="section mid-cta">
<div class="wrap narrow center">
{store_button(lang, position="mid")}
<p class="hero-note">{esc(ui["platform"])}</p>{play_line(lang, f"web_{lang}_mid")}
</div>
</section>"""
    body = hero + whosec + money + features + report + mid + shots + beacon + privacy + pro + helpsec + cta
    add(lang, "home", P(lang, "home"), h["title"], h["desc"], body, jsonld=[app_jsonld(lang), home_faq_jsonld(lang)], main_class="home")
    base = f"/assets/hero/{lang}"
    PAGES[-1]["head"] = (f'<link rel="preload" as="image" href="{base}-360.webp" imagesrcset="{base}-360.webp 360w, {base}-720.webp 720w" '
                         f'imagesizes="(min-width: 900px) 340px, 72vw" fetchpriority="high">\n')

def build_report_table(lang):
    """What the exported log contains – the facts, not a promise (en/sv/de)."""
    T = {
        "en": ("What the exported log contains", ["Field", "In Körlogg"], [
            ("Date, start and end time", "Every trip"), ("Start and end address", "Every trip"),
            ("Distance and odometer at start and end", "Every trip; calculated readings marked ≈"),
            ("Purpose, places, companies and people visited", "Business trips"),
            ("Driver and car (registration number)", "Every trip"),
            ("Changes made afterwards", "Listed in the export"),
            ("Business and private totals", "Per month and year")],
            "Whether a log is accepted is decided by the tax office or employer that receives it."),
        "sv": ("Det här innehåller den exporterade körjournalen", ["Uppgift", "I Körlogg"], [
            ("Datum, start- och sluttid", "Varje resa"), ("Start- och slutadress", "Varje resa"),
            ("Sträcka och mätarställning vid start och slut", "Varje resa; beräknade värden märks ≈"),
            ("Ärende, besökta platser, företag och kontaktpersoner", "Tjänsteresor"),
            ("Förare och bil (registreringsnummer)", "Varje resa"),
            ("Ändringar i efterhand", "Redovisas i exporten"),
            ("Summa tjänst och privat", "Per månad och år")],
            "Om en körjournal godtas avgör Skatteverket eller arbetsgivaren som tar emot den."),
        "de": ("Das steht im exportierten Fahrtenbuch", ["Angabe", "In Körlogg"], [
            ("Datum, Beginn und Ende", "Jede Fahrt"), ("Start- und Zieladresse", "Jede Fahrt"),
            ("Strecke und Kilometerstand zu Beginn und Ende", "Jede Fahrt; berechnete Werte mit ≈ markiert"),
            ("Reisezweck, besuchte Orte, Firmen und Personen", "Dienstfahrten"),
            ("Fahrer und Fahrzeug (Kennzeichen)", "Jede Fahrt"),
            ("Nachträgliche Änderungen", "Im Änderungsprotokoll des Exports"),
            ("Summen dienstlich und privat", "Pro Monat und Jahr")],
            "Ob ein Fahrtenbuch anerkannt wird, entscheidet das Finanzamt."),
    }
    h2, head, rows, note = T[lang]
    tr = "".join(f"<tr><th scope=\"row\">{esc(a)}</th><td>{esc(b)}</td></tr>" for a, b in rows)
    return f"""<section class="section">
<div class="wrap narrow">
<h2>{esc(h2)}</h2>
<div class="table-wrap"><table class="facts"><thead><tr><th scope="col">{esc(head[0])}</th><th scope="col">{esc(head[1])}</th></tr></thead><tbody>{tr}</tbody></table></div>
<p class="muted">{esc(note)}</p>
</div>
</section>"""

# --------------------------------------------------------------------- help
HELP = json.loads((SRC / "help/help.json").read_text())

def help_text(lang, key):
    t = HELP["strings"][HELP_LANG.get(lang, lang)][key]
    t = t.replace("{authority}", LANGS[lang]["authority"])
    if lang == "de":   # the site speaks to Germany and Austria at once
        t = t.replace("das Kilometergeld des Autos", "die Kilometerpauschale bzw. das Kilometergeld des Autos")
        t = t.replace("Kilometergeld und Abgleich", "Kilometerpauschale bzw. Kilometergeld und Abgleich")
    if lang == "sv":
        t = t.replace("Skatteverket frågar efter", "Skatteverket frågar efter")
    return t

HOME_FAQ_KEYS = ["faqStartHow", "faqOdoHow", "faqStartMissed", "faqProWhat", "faqPrivacyWhere", "faqProCancel"]

def home_faq_jsonld(lang):
    """FAQPage for the home page: exactly the questions and answers shown in its FAQ."""
    return {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": LANGS[lang]["html"],
            "mainEntity": [{"@type": "Question", "name": help_text(lang, k + "Q"),
                            "acceptedAnswer": {"@type": "Answer", "text": help_text(lang, k + "A")}} for k in HOME_FAQ_KEYS]}

def qr_block(lang):
    """QR code to the App Store, beside the hero badge; CSS shows it on desktop widths only."""
    return (f'<a class="qr" href="{esc(store_url(lang, f"web_{lang}_qr"))}" data-position="qr">'
            f'<img src="/assets/qr/{lang}.svg" width="96" height="96" alt="" loading="lazy">'
            f'<span>{esc(UI[lang]["qr_note"])}</span></a>')

def play_line(lang, campaign):
    """Google Play link, only once the Android app is live (config.PLAY_RELEASED)."""
    if not C.PLAY_RELEASED: return ""
    return f'<p><a class="more" href="{esc(play_url(lang, campaign))}">Google Play →</a></p>'

def build_home_faq(lang):
    keys = HOME_FAQ_KEYS
    return '<div class="faq">' + "".join(
        f'<details><summary>{esc(help_text(lang, k + "Q"))}</summary><p>{esc(help_text(lang, k + "A"))}</p></details>'
        for k in keys) + "</div>"

def build_help(lang):
    ui = UI[lang]
    sections, qa = "", []
    for tp in HELP["topics"]:
        badge = f'<p class="badge">{esc(v2_label(lang))}</p>' if tp["key"] == "faqBeacon" else ""
        items = ""
        for q in tp["questions"]:
            Q, A = help_text(lang, q + "Q"), help_text(lang, q + "A")
            anchor = re.sub(r"(?<!^)(?=[A-Z])", "-", q[3:]).lower()
            items += f'<details id="{anchor}"><summary>{esc(Q)}</summary><p>{esc(A)}</p></details>'
            qa.append({"@type": "Question", "name": Q, "acceptedAnswer": {"@type": "Answer", "text": A}})
        sections += f'<section class="help-topic">{badge}<h2>{esc(help_text(lang, tp["key"] + "Title"))}</h2><div class="faq">{items}</div></section>'
    contact = (f'<section class="card contact"><h2>{esc(help_text(lang, "faqContactTitle"))}</h2>'
               f'<p><a class="btn" href="{P(lang, "support")}">{esc(help_text(lang, "faqContactButton"))}</a></p></section>')
    body = f"""<div class="wrap narrow page">
<h1>{esc(help_text(lang, "faqRow"))}</h1>
<p class="lede">{esc(ui["help_intro"])}</p>{redeem_pointer(lang)}
{sections}
{contact}
</div>"""
    jl = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": qa}]
    add(lang, "help", P(lang, "help"), ui["help_title"], ui["help_desc"], body, jsonld=jl)

# ------------------------------------------------------------------ redeem
def redeem_path(lang):
    return P(lang, REDEEM[lang]["slug"])

def redeem_pointer(lang):
    """One line on the help and support pages that leads to the redeem page."""
    if lang not in REDEEM_LANGS: return ""
    r = REDEEM[lang]
    return f'<p class="help-pointer">{esc(r["pointer"])} <a href="{redeem_path(lang)}">{esc(r["h1"])}</a>.</p>'

def build_redeem(lang):
    """How to redeem an offer code (iPhone and Android). Not in the main nav;
    linked from the help and support pages. No Apple redemption URLs here."""
    r, ui = REDEEM[lang], UI[lang]
    steps = lambda items, first="": "<ol>" + "".join(
        f"<li>{t}{first if i == 0 else ''}</li>" for i, t in enumerate(items)) + "</ol>"
    badge = f'<p>{store_button(lang, " small", position="code")}</p>'
    email = f'<a href="mailto:{C.SUPPORT_EMAIL}?subject=K%C3%B6rlogg%20code">{C.SUPPORT_EMAIL}</a>'
    support = f'<a href="{P(lang, "support")}">{esc(ui["support"])}</a>'
    inner = (f'<h1>{esc(r["h1"])}</h1>\n<p class="lede">{esc(r["lede"])}</p>\n'
             f'<h2>iPhone</h2>\n{steps(r["ios"], badge)}\n'
             f'<h2>Android</h2>\n{steps(r["android"])}\n'
             f'<h2>{esc(r["after_h"])}</h2>\n' + "".join(f"<p>{t}</p>" for t in r["after"]) + "\n"
             f'<p class="note">{r["contact"].format(email=email, support=support)}</p>')
    jl = [breadcrumb(lang, [("Körlogg", P(lang, "home")), (r["h1"], redeem_path(lang))])]
    add(lang, "code", redeem_path(lang), r["title"], r["desc"],
        f'<div class="wrap narrow page"><article class="card legal">{inner}</article></div>', jsonld=jl)

# ------------------------------------------------------------------ support
def contact_block(lang):
    ui = UI[lang]
    s = f'<p>{esc(ui["support_email_intro"])} <a href="mailto:{C.SUPPORT_EMAIL}?subject=K%C3%B6rlogg%20support">{C.SUPPORT_EMAIL}</a>. {esc(ui["support_email_note"])}</p>'
    if not C.SUPPORT_EMAIL_LIVE:
        s += f'<p>{esc(ui["support_email_fallback"])} <a href="mailto:{C.FALLBACK_EMAIL}?subject=K%C3%B6rlogg%20support">{C.FALLBACK_EMAIL}</a>.</p>'
    return s

def build_support(lang):
    ui = UI[lang]
    src = SRC / "legal" / lang / "support.html"
    if src.exists():
        inner = placeholders(src.read_text(), lang).replace("{{contact}}", contact_block(lang))
        inner = inner.replace("</h1>", f'</h1>\n<p class="help-pointer">{esc(ui["support_help"])} <a href="{P(lang, "help")}">{esc(ui["help"])}</a>.</p>{redeem_pointer(lang)}', 1)
    else:
        inner = (f'<h1>{esc(ui["support_title"].split(" – ")[0])}</h1>{contact_block(lang)}'
                 f'<p>{esc(ui["support_help"])} <a href="{P(lang, "help")}">{esc(ui["help"])}</a>.</p>{redeem_pointer(lang)}'
                 f'<ul><li><a href="{P(lang if lang in LEGAL_LANGS else "en", "privacy")}">{esc(ui["privacy"])}</a></li>'
                 f'<li><a href="{P(lang if lang in LEGAL_LANGS else "en", "terms")}">{esc(ui["terms"])}</a></li>'
                 f'<li><a href="{P("en", "delete-data")}">{esc(ui["delete"])}</a></li></ul>')
    add(lang, "support", P(lang, "support"), ui["support_title"], ui["support_desc"],
        f'<div class="wrap narrow page"><article class="card legal">{inner}</article></div>')

# -------------------------------------------------------------------- legal
def build_legal(lang, page):
    ui = UI[lang]
    key = {"privacy": "privacy", "terms": "terms", "delete-data": "delete"}[page]
    title_key = {"privacy": "privacy_title", "terms": "terms_title", "delete-data": "delete_title"}[page]
    desc_key = {"privacy": "privacy_desc", "terms": "terms_desc", "delete-data": "delete_desc"}[page]
    note = ""
    src = SRC / "legal" / lang / f"{page}.html"
    if src.exists():
        inner, noindex, canonical, src_lang = src.read_text(), False, None, lang
        if ui.get("translation_note"):
            note = f'<p class="note">{esc(ui["translation_note"])} <a href="{P("en", page)}" hreflang="en" lang="en">English</a></p>'
    else:   # da/no/pl: localized header, English text below, canonical to the English page
        inner, noindex, canonical, src_lang = (SRC / "legal/en" / f"{page}.html").read_text(), True, P("en", page), "en"
        others = " · ".join(f'<a href="{P(l, page)}" hreflang="{LANGS[l]["hreflang"]}">{LANGS[l]["name"]}</a>' for l in ("en", "nl", "fi"))
        note = f'<p class="note">{esc(ui["en_only"])} {others}</p>'
    inner = placeholders(inner, src_lang if src_lang != lang else lang)
    site_note = ""
    if page == "privacy":
        site_note = f'<aside class="site-note"><h2>{esc(ui["site_note_h"])}</h2><p>{ui["site_note"]}</p></aside>'
    body_lang = f' lang="en"' if src_lang != lang else ""
    title = ui[title_key] or UI["en"][title_key]
    desc = ui[desc_key] or UI["en"][desc_key]
    add(lang, page, P(lang, page), title, desc,
        f'<div class="wrap narrow page">{note}<article class="card legal"{body_lang}>{inner}</article>{site_note}</div>',
        noindex=noindex, canonical=canonical)

# ------------------------------------------------------------------- guides
def build_guides():
    for stem, (lang, path, cluster) in GUIDES.items():
        if not is_live(stem): continue
        meta, body = read_guide(stem)
        body = placeholders(body, lang)
        # a guide may name its own App Store campaign (guide_<slug>); {{store}} in the text links with it
        campaign = meta.get("campaign")
        body = body.replace("{{store}}", esc(store_url(lang, campaign)))
        # {{play}} … {{/play}}: the Google Play link, shown only once the Android app is live
        body = body.replace("{{playurl}}", esc(play_url(lang, campaign)))
        body = re.sub(r"(?s)\{\{play\}\}(.*?)\{\{/play\}\}", r"\1" if C.PLAY_RELEASED else "", body)
        badge = f'<p class="badge">{esc(v2_label(lang))}</p>' if meta.get("v2") == "true" else ""
        h1 = re.search(r"<h1>(.*?)</h1>", body).group(1)
        crumbs = f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{P(lang, "home")}">Körlogg</a> › <a href="{GUIDE_INDEX[lang]}">{esc(UI[lang]["guides"])}</a></nav>'
        cta = (f'<aside class="card guide-cta"><img src="/assets/logo-96.webp" width="56" height="56" alt="" loading="lazy">'
               f'<div><p><strong>Körlogg</strong> – {esc(HOME[lang]["h1"])}.</p>{store_button(lang, " small", position="middle", campaign=campaign)}</div></aside>')
        article = {"@context": "https://schema.org", "@type": "Article", "headline": re.sub("<[^>]+>", "", h1),
                   "description": meta["description"], "inLanguage": LANGS[lang]["html"], "dateModified": meta.get("modified", "2026-10-10"),
                   "author": {"@type": "Person", "name": "Amir Alagic"}, "mainEntityOfPage": C.SITE + path,
                   "image": f"{C.SITE}/assets/og/{lang}.png"}
        jl = [article, breadcrumb(lang, [("Körlogg", P(lang, "home")), (UI[lang]["guides"], GUIDE_INDEX[lang]), (re.sub("<[^>]+>", "", h1), path)])]
        faq = re.search(r'(?s)<section class="guide-faq">(.*?)</section>', body)
        if faq:   # questions as <h3>, each answered by the <p> after it
            plain = lambda s: html.unescape(re.sub("<[^>]+>", "", s)).strip()
            qa = [{"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
                  for q, a in re.findall(r"(?s)<h3>(.*?)</h3>\s*<p>(.*?)</p>", faq.group(1))]
            jl.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": qa})
        add(lang, cluster, path, meta["title"], meta["description"],
            f'<div class="wrap narrow page">{crumbs}{badge}<article class="guide">{body}</article>{cta}</div>',
            jsonld=jl)
    for lang, path in GUIDE_INDEX.items():
        ui = UI[lang]
        items = ""
        for stem, (l, p, _) in GUIDES.items():
            if l != lang or not is_live(stem): continue
            meta, _b = read_guide(stem)
            h1 = re.search(r"<h1>(.*?)</h1>", _b).group(1)
            items += f'<li class="card link-card"><a href="{p}"><h2>{h1}</h2><p>{esc(meta["description"])}</p></a></li>'
        others = " · ".join(f'<a href="{p}" hreflang="{LANGS[l]["hreflang"]}">{LANGS[l]["name"]}</a>' for l, p in GUIDE_INDEX.items() if l != lang)
        body = (f'<div class="wrap narrow page"><h1>{esc(ui["guides_h1"])}</h1><p class="lede">{esc(ui["guides_intro"])}</p>'
                f'<ul class="cards one" role="list">{items}</ul><p class="muted">{esc(ui["other_lang_guides"])}: {others}</p></div>')
        add(lang, "guides", path, ui["guides_title"], ui["guides_desc"], body)

# ---------------------------------------------------------------------- 404
def build_404():
    blocks = "".join(f'<section lang="{LANGS[l]["html"]}"><h2>{esc(UI[l]["nf_h1"])}</h2><p>{esc(UI[l]["nf_text"])} <a href="{P(l, "home")}">{esc(UI[l]["nf_home"])}</a></p></section>'
                     for l in ("en", "sv", "de"))
    body = (f'<div class="wrap narrow page center"><h1>404</h1>{blocks}'
            f'<p class="muted">{" · ".join(f"<a href=\"{P(l, "home")}\">{v["name"]}</a>" for l, v in LANGS.items())}</p></div>')
    PAGES.append(dict(lang="en", cluster=None, path="/404.html", title=UI["en"]["nf_title"], desc=UI["en"]["nf_text"],
                      body=body, noindex=True, canonical="/", jsonld=[], main_class=""))

# --------------------------------------------------------------------- main
def clean():
    for d in GENERATED:
        p = ROOT / d
        if p.is_dir(): shutil.rmtree(p)
    for f in ("index.html", "404.html", "sitemap.xml", "robots.txt"):
        (ROOT / f).unlink(missing_ok=True)

def write(path, text):
    out = ROOT / (path.lstrip("/") + ("index.html" if path.endswith("/") else ""))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)

def main():
    global CSS_VERSION
    import hashlib
    CSS_VERSION = hashlib.sha1((ROOT / "assets/site.css").read_bytes()).hexdigest()[:8]
    global STATS_VERSION
    STATS_VERSION = hashlib.sha1((ROOT / "assets/stats.js").read_bytes()).hexdigest()[:8]
    clean()
    for lang in LANGS:
        build_home(lang); build_help(lang); build_support(lang)
        build_legal(lang, "privacy"); build_legal(lang, "terms")
        if lang in DELETE_LANGS: build_legal(lang, "delete-data")
        if lang in REDEEM_LANGS: build_redeem(lang)
    build_guides(); build_404()
    for pg in PAGES:
        write(pg["path"], layout(pg))
    # sitemap with hreflang alternates
    urls = ""
    for pg in PAGES:
        if pg["noindex"]: continue
        alt = ""
        if pg["cluster"]:
            for l, p in CLUSTERS[pg["cluster"]].items():
                alt += f'<xhtml:link rel="alternate" hreflang="{LANGS[l]["hreflang"]}" href="{C.SITE}{p}"/>'
                if l == "de": alt += f'<xhtml:link rel="alternate" hreflang="de-AT" href="{C.SITE}{p}"/>'
            if "en" in CLUSTERS[pg["cluster"]]:
                alt += f'<xhtml:link rel="alternate" hreflang="x-default" href="{C.SITE}{CLUSTERS[pg["cluster"]]["en"]}"/>'
        urls += f"<url><loc>{C.SITE}{pg['path']}</loc><lastmod>{TODAY}</lastmod>{alt}</url>\n"
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                                      'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + "</urlset>\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /src/\nDisallow: /tools/\nDisallow: /docs/\n\nSitemap: {C.SITE}/sitemap.xml\n")
    print(f"{len(PAGES)} pages; 2.0 released: {C.KORLOGG_2_0_RELEASED}")

CSS_VERSION = "0"
STATS_VERSION = "0"
if __name__ == "__main__":
    main()
