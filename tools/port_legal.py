#!/usr/bin/env python3
"""One-off: copy the legal page bodies from AlagicAmir/korklar-legal/korlogg verbatim
into src/legal/<lang>/<page>.html, with internal links turned into {{placeholders}}
that build.py resolves per language. The text itself is not touched."""
import re, pathlib
SRC = pathlib.Path.home() / "repo/korklar-legal/korlogg"
OUT = pathlib.Path(__file__).resolve().parent.parent / "src/legal"
LINKS = {"privacy.html": "{{privacy}}", "terms.html": "{{terms}}", "support.html": "{{support}}",
         "delete-data.html": "{{delete}}", "index.html": "{{home}}"}
jobs = [("en", p) for p in ("privacy", "terms", "support", "delete-data")] + \
       [(l, p) for l in ("nl", "fi") for p in ("privacy", "terms")]
for lang, page in jobs:
    path = SRC / (f"{page}.html" if lang == "en" else f"{lang}/{page}.html")
    html = path.read_text()
    body = re.search(r'<div class="card">(.*?)</div><p class="foot">', html, re.S).group(1)
    # language links inside the "Last updated" line: the site's switcher replaces them
    body = re.sub(r' · <a href="(?:nl|fi)/(?:privacy|terms)\.html">[^<]*</a>', "", body)
    def fix(m):
        href = m.group(1)
        name = href.split("/")[-1]
        if href.startswith(("http", "mailto")): return m.group(0)
        if href.startswith("../") and lang != "en":   # nl/fi pages pointing at the English ones
            return f'href="{LINKS[name]}@en"'
        return f'href="{LINKS[name]}"'
    body = re.sub(r'href="([^"]+)"', fix, body)
    d = OUT / lang; d.mkdir(parents=True, exist_ok=True)
    (d / f"{page}.html").write_text(body.strip() + "\n")
    print(lang, page, len(body))
