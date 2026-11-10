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

# Hungarian came with 2.6 and lives in its own file (every key of every table), so it is
# read from the current master and trimmed to the help keys the other languages have.
HU_REF = "master"
hu_src = subprocess.run(["git", "-C", str(REPO), "show", f"{HU_REF}:Korlogg/Localization/Strings+Hungarian.swift"],
                        check=True, capture_output=True, text=True).stdout
hu_all = {m.group(1): m.group(2).replace('\\"', '"') for m in re.finditer(r'^\s+"([A-Za-z0-9]+)": "(.*)",\s*$', hu_src, re.M)}
tables["hu"] = {k: hu_all[k] for k in tables["en"] if k in hu_all}

# Keys whose wording was changed after the snapshot ref and should show on the site at once
# (Amir 2026-11-10: the "trip was not logged" question was renamed): read from master.
MASTER_KEYS = ["faqStartMissedQ"]
m_src = subprocess.run(["git", "-C", str(REPO), "show", "master:Korlogg/Localization/Strings+Help.swift"],
                       check=True, capture_output=True, text=True).stdout
m_lang = None
for line in m_src.splitlines():
    m = re.match(r"^        \.([a-z]{2}): \[", line)
    if m:
        m_lang = m.group(1); continue
    m = re.match(r'^\s+"([A-Za-z0-9]+)": "(.*)",\s*$', line)
    if m and m_lang in tables and m.group(1) in MASTER_KEYS:
        tables[m_lang][m.group(1)] = m.group(2).replace('\\"', '"')

topics = [{"key": k, "questions": re.findall(r'"([A-Za-z]+)"', qs)}
          for k, qs in re.findall(r'Topic\(key: "(\w+)", questions: \[([^\]]*)\]\)', view)
          if k != "faqUs"]   # the US topic is not published (no US launch)

OUT.write_text(json.dumps({"ref": REF, "hu_ref": HU_REF, "topics": topics, "strings": tables},
                          ensure_ascii=False, indent=1))
print(f"{OUT}: {len(topics)} topics, {sum(len(t['questions']) for t in topics)} questions, langs {list(tables)}")
