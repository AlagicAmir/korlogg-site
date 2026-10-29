#!/usr/bin/env python3
"""Snapshot the Android app's own Help answers into src/help/help_android.json.

The help page shows the iPhone answers (tools/extract_help.py); where Android works
differently, the answer gets an "Android:" paragraph with the Android app's wording.
Reads ~/repo/KorloggAndroid (read-only) with `git show`.

Usage: python3 tools/extract_help_android.py [git-ref]   (default: HEAD; the snapshot is from Android 1.1.1 (12), 5510338)
"""
import json, subprocess, sys, pathlib

REPO = pathlib.Path.home() / "repo/KorloggAndroid"
REF = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
OUT = pathlib.Path(__file__).resolve().parent.parent / "src/help/help_android.json"
ASSETS = "app/src/main/assets"
LANGS = ["sv", "en", "da", "nb", "de", "nl", "fi", "pl"]
# Questions whose iPhone answer does not hold on Android (permissions, battery,
# store, export, privacy). faqProTrial is left out on purpose.
KEYS = ["faqStartPerms", "faqStartMissed", "faqReportExport", "faqProWhat", "faqProRestore",
        "faqProInvoice", "faqProCancel", "faqPrivacyLocation"]

def show(path):
    return json.loads(subprocess.run(["git", "-C", str(REPO), "show", f"{REF}:{path}"],
                                     check=True, capture_output=True, text=True).stdout)

ref = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", REF],
                     check=True, capture_output=True, text=True).stdout.strip()
strings = {}
for lang in LANGS:
    android = show(f"{ASSETS}/strings-android/{lang}.json")
    strings[lang] = {k + "A": android[k + "A"] for k in KEYS}

OUT.write_text(json.dumps({"ref": ref, "strings": strings}, ensure_ascii=False, indent=1))
print(f"{OUT}: {len(KEYS)} answers, langs {LANGS}, ref {ref}")
