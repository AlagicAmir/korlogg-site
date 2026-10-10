#!/usr/bin/env python3
"""Local site check: serves the repo root, crawls every page from / and the sitemap,
and reports broken internal links/anchors/images, hreflang that is not reciprocal,
duplicate titles/descriptions/ids, unbalanced tags, images without alt, and banned
copy. `--external` also requests every external link once.

    python3 tools/check.py [--external]
"""
import http.server, re, sys, threading, urllib.request, urllib.error, functools
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote

ROOT = Path(__file__).resolve().parent.parent
PORT = 8765
BASE = f"http://127.0.0.1:{PORT}"
SITE = "https://korlogg.com"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
OPTIONAL_CLOSE = {"p", "li", "dt", "dd", "tr", "td", "th", "thead", "tbody", "option"}
BANNED = [r"finanzamtkonform", r"\bGratis\b", r"der Store\b", r"DSGVO-konform", r"kelpaa verottajalle", r"sluitend",
          r"nothing leaves your phone", r"geocod", r"\bguaranteed\b", r"\bgarantiert\b", r"(?<!eller )godkänd av Skatteverket",
          r"\$\d", r"\d+\s?kr\b(?![^<]*(?:mil|km))", r"€\s?\d+[,.]\d\d(?!\s?(?:€\s?)?(?:pro|per|/)\s?(?:km|Kilometer))"]

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self.ids, self.stack, self.errors, self.hreflang = [], [], [], [], {}
        self.title, self.desc, self.canonical, self.noindex, self._in_title = "", "", "", False, False
        self.text = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a: self.ids.append(a["id"])
        for k in ("href", "src"):
            if a.get(k) and tag != "link" or (tag == "link" and k == "href" and a.get("rel") in ("stylesheet", "icon", "apple-touch-icon", "manifest")):
                if a.get(k): self.links.append(a[k])
        if a.get("srcset"):
            self.links += [s.strip().split(" ")[0] for s in a["srcset"].split(",")]
        if tag == "img" and "alt" not in a: self.errors.append("img without alt: " + a.get("src", ""))
        if tag == "link" and a.get("rel") == "alternate" and a.get("hreflang"): self.hreflang[a["hreflang"]] = a["href"]
        if tag == "link" and a.get("rel") == "canonical": self.canonical = a["href"]
        if tag == "meta" and a.get("name") == "description": self.desc = a.get("content", "")
        if tag == "meta" and a.get("name") == "robots" and "noindex" in a.get("content", ""): self.noindex = True
        if tag == "title": self._in_title = True
        if tag not in VOID: self.stack.append(tag)
    def handle_startendtag(self, tag, attrs): self.handle_starttag(tag, attrs); (tag not in VOID) and self.stack.pop()
    def handle_endtag(self, tag):
        if tag == "title": self._in_title = False
        while self.stack and self.stack[-1] != tag and self.stack[-1] in OPTIONAL_CLOSE: self.stack.pop()
        if self.stack and self.stack[-1] == tag: self.stack.pop()
        else: self.errors.append(f"unexpected </{tag}> (open: {self.stack[-3:]})")
    def handle_data(self, d):
        if self._in_title: self.title += d
        self.text.append(d)

def serve():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    http.server.SimpleHTTPRequestHandler.log_message = lambda *a: None
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()

def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=20) as r: return r.status, r.read()
    except urllib.error.HTTPError as e: return e.code, b""

def main():
    serve()
    sitemap = (ROOT / "sitemap.xml").read_text()
    todo = ["/"] + [u.replace(SITE, "") for u in re.findall(r"<loc>(.*?)</loc>", sitemap)] + ["/404.html"]
    seen, pages, problems, external, assets = set(), {}, [], set(), set()
    while todo:
        path = todo.pop()
        if path in seen: continue
        seen.add(path)
        st, body = fetch(BASE + path)
        if st != 200: problems.append(f"{path}: HTTP {st}"); continue
        p = Page(); p.feed(body.decode()); p.close()
        if [t for t in p.stack if t not in OPTIONAL_CLOSE]: problems.append(f"{path}: unclosed {p.stack}")
        problems += [f"{path}: {e}" for e in p.errors]
        dup = {i for i in p.ids if p.ids.count(i) > 1}
        if dup: problems.append(f"{path}: duplicate ids {dup}")
        # the official per-km rates block (id="rates") is meant to contain amounts; check the rest
        q = Page(); q.feed(re.sub(r'(?s)<section class="section money" id="rates">.*?</section>', "", body.decode())); q.close()
        text = " ".join(q.text)
        for b in BANNED:
            if b == r"geocod" and re.search(r"/(privacy|terms|delete-data)/$", path): continue   # verbatim legal text
            if "kr" in b and ("ibeacon" in path or "/help/" in path): continue   # third-party beacon prices
            if "Gratis" in b and path.startswith("/nl/"): continue   # Dutch, not German
            for m in re.finditer(b, text, re.I):
                problems.append(f"{path}: banned/price pattern {b!r}: …{text[max(0,m.start()-40):m.end()+20]}…")
        pages[path] = p
        for l in p.links:
            u = urljoin(SITE + path, l)
            if u.startswith(SITE):
                pu = urlparse(u)
                tgt = unquote(pu.path)
                if tgt.endswith("/") or tgt.endswith(".html"):
                    todo.append(tgt);
                    if pu.fragment: assets.add((path, tgt, pu.fragment))
                else: assets.add((path, tgt, None))
            elif u.startswith("http"): external.add(u)
    for src, tgt, frag in assets:
        if frag:
            if tgt in pages and frag not in pages[tgt].ids: problems.append(f"{src}: missing anchor {tgt}#{frag}")
        else:
            st, _ = fetch(BASE + tgt.split("?")[0])
            if st != 200: problems.append(f"{src}: broken asset {tgt} ({st})")
    # hreflang reciprocity + canonical sanity
    for path, p in pages.items():
        if p.noindex: continue
        if p.canonical != SITE + path: problems.append(f"{path}: canonical {p.canonical}")
        for hl, href in p.hreflang.items():
            tp = href.replace(SITE, "")
            if tp not in pages: problems.append(f"{path}: hreflang {hl} -> missing {tp}"); continue
            if SITE + path not in pages[tp].hreflang.values(): problems.append(f"{path}: hreflang {hl} -> {tp} not reciprocal")
    for attr in ("title", "desc"):
        vals = {}
        for path, p in pages.items():
            if path == "/404.html": continue
            vals.setdefault(getattr(p, attr), []).append(path)
        problems += [f"duplicate {attr}: {v}" for k, v in vals.items() if len(v) > 1 and not all(pages[x].noindex for x in v[1:])]
        problems += [f"{path}: {attr} length {len(getattr(p, attr))}" for path, p in pages.items()
                     if not (10 <= len(getattr(p, attr)) <= (70 if attr == "title" else 170)) and not p.noindex]
    if "--external" in sys.argv:
        for u in sorted(external):
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (korlogg.com link check)"})
            try:
                with urllib.request.urlopen(req, timeout=20) as r: st = r.status
            except urllib.error.HTTPError as e: st = e.code
            except Exception as e: st = type(e).__name__
            if st != 200: problems.append(f"external {u}: {st}")
    print(f"{len(pages)} pages crawled, {len(assets)} internal refs, {len(external)} external links")
    print("\n".join(sorted(set(problems))) or "no problems")
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
