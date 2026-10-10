#!/usr/bin/env python3
"""Publish a noindex preview copy of the built site to AlagicAmir/korlogg-site-preview
(GitHub Pages at https://alagicamir.github.io/korlogg-site-preview/), for looking at
the site before korlogg.com's DNS points to GitHub. The real repo has a custom domain,
so its github.io address redirects to korlogg.com.

    python3 tools/preview.py
"""
import pathlib, re, shutil, subprocess, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "/korlogg-site-preview"
REPO = "AlagicAmir/korlogg-site-preview"
SKIP = {".git", "src", "tools", "docs", "CNAME", "README.md", ".gitignore"}

def main():
    out = pathlib.Path(tempfile.mkdtemp(prefix="korlogg-preview-"))
    for p in ROOT.iterdir():
        if p.name in SKIP: continue
        (shutil.copytree if p.is_dir() else shutil.copy2)(p, out / p.name)
    for f in out.rglob("*.html"):
        t = f.read_text()
        t = re.sub(r'((?:href|src)=")/(?!/)', rf"\1{BASE}/", t)
        t = re.sub(r'(srcset="[^"]*")', lambda m: re.sub(r"(^|, |\")/(?!/)", rf"\1{BASE}/", m.group(1)), t)
        t = t.replace("<head>", '<head>\n<meta name="robots" content="noindex, nofollow">', 1)
        f.write_text(t)
    (out / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
    (out / "sitemap.xml").unlink(missing_ok=True)
    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=out, check=True)
    subprocess.run(["git", "add", "-A"], cwd=out, check=True)
    subprocess.run(["git", "commit", "-qm", "Preview build of korlogg.com\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"], cwd=out, check=True)
    exists = subprocess.run(["gh", "repo", "view", REPO], capture_output=True).returncode == 0
    if not exists:
        subprocess.run(["gh", "repo", "create", REPO, "--public", "--description",
                        "Temporary noindex preview of korlogg.com (built from korlogg-site)"], check=True)
    subprocess.run(["git", "push", "-qf", f"https://github.com/{REPO}.git", "main"], cwd=out, check=True)
    if not exists:
        subprocess.run(["gh", "api", "-X", "POST", f"repos/{REPO}/pages", "-f", "source[branch]=main", "-f", "source[path]=/"], check=True)
    print(f"https://alagicamir.github.io{BASE}/")

if __name__ == "__main__":
    main()
