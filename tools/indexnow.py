"""Tell search engines (Bing first, and through IndexNow also Yandex, Seznam, Naver) which
korlogg.com pages are new or changed, so they are crawled within days instead of weeks.
ChatGPT's search leans on Bing, so this is also how new guides reach ChatGPT sooner.

    python3 tools/indexnow.py --all                 # every indexable page in the sitemap
    python3 tools/indexnow.py --since <git sha>     # pages whose built HTML changed since that commit
    python3 tools/indexnow.py --published-today     # guides whose publish date is today
    add --dry-run to print the URLs without sending

The key file /<INDEXNOW_KEY>.txt lives in the repo root and is deployed with the site.
Runs in .github/workflows/publish.yml after each deploy.
"""
import json, pathlib, re, subprocess, sys, urllib.request
from datetime import date

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import config as C

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOST = C.SITE.split("//", 1)[1]


def url_for(html_path):
    """'guides/x/index.html' -> https://korlogg.com/guides/x/ ; None for pages search engines must skip."""
    p = ROOT / html_path
    if not p.exists() or not html_path.endswith(".html") or html_path == "404.html":
        return None
    if re.search(r'<meta name="robots" content="noindex', p.read_text(errors="ignore")):
        return None
    rel = html_path[:-len("index.html")] if html_path.endswith("index.html") else html_path
    return f"{C.SITE}/{rel}"


def all_urls():
    return re.findall(r"<loc>(.*?)</loc>", (ROOT / "sitemap.xml").read_text())


def changed_since(sha):
    out = subprocess.run(["git", "diff", "--name-only", sha, "HEAD", "--", "*.html"],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    return [u for u in map(url_for, out) if u]


def published_today():
    import build                                     # reuse GUIDES and the publish-date parser
    today = date.today().isoformat()
    return [C.SITE + path for stem, (_, path, _) in build.GUIDES.items()
            if build._parse_guide(build.SRC / "guides" / f"{stem}.html")[0].get("publish") == today]


def submit(urls):
    body = json.dumps({"host": HOST, "key": C.INDEXNOW_KEY,
                       "keyLocation": f"{C.SITE}/{C.INDEXNOW_KEY}.txt", "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--all" in args:
        urls = all_urls()
    elif "--since" in args:
        urls = changed_since(args[args.index("--since") + 1])
    elif "--published-today" in args:
        urls = published_today()
    else:
        sys.exit(__doc__)
    urls = sorted(set(urls))
    print(f"{len(urls)} URL(s)")
    for u in urls:
        print(" ", u)
    if urls and "--dry-run" not in args:
        print("IndexNow:", submit(urls))   # 200 or 202 = accepted
