#!/usr/bin/env python3
"""Snapshot the in-app Help strings from the Körlogg app repo into src/help/help.json.

Usage: python3 tools/extract_help.py [git-ref]   (default: the ref of the 2.0 build in review)
Reads ~/repo/Korlogg (read-only) with `git show`, so the website shows exactly the
answers of that app build.
"""
import json, re, subprocess, sys, pathlib

REPO = pathlib.Path.home() / "repo/Korlogg"
REF = sys.argv[1] if len(sys.argv) > 1 else "2704d10"   # Körlogg 2.0 (20)
OUT = pathlib.Path(__file__).resolve().parent.parent / "src/help/help.json"

def show(path):
    return subprocess.run(["git", "-C", str(REPO), "show", f"{REF}:{path}"],
                          check=True, capture_output=True, text=True).stdout

strings = show("Korlogg/Localization/Strings+Help.swift")
view = show("Korlogg/Features/Settings/HelpView.swift")

tables, lang = {}, None
for line in strings.splitlines():
    m = re.match(r"^        \.([a-z]{2}): \[", line)
    if m:
        lang = m.group(1); tables[lang] = {}; continue
    m = re.match(r'^\s+"([A-Za-z0-9]+)": "(.*)",\s*$', line)
    if m and lang:
        tables[lang][m.group(1)] = m.group(2).replace('\\"', '"')

topics = [{"key": k, "questions": re.findall(r'"([A-Za-z]+)"', qs)}
          for k, qs in re.findall(r'Topic\(key: "(\w+)", questions: \[([^\]]*)\]\)', view)
          if k != "faqUs"]   # the US topic is not published (no US launch)

OUT.write_text(json.dumps({"ref": REF, "topics": topics, "strings": tables},
                          ensure_ascii=False, indent=1))
print(f"{OUT}: {len(topics)} topics, {sum(len(t['questions']) for t in topics)} questions, langs {list(tables)}")
