#!/usr/bin/env python3
"""Push `## Cards` blocks from the notes into Anki via AnkiConnect.

Card format, anywhere under a `## Cards` heading in a .md file:

    ## Cards
    Q: what does umask do?
    A: subtracts permission bits from what the program requests.

Re-running is idempotent: same question -> updated answer, new question -> new card.
Requires Anki running with the AnkiConnect add-on (code 2055492159).
"""
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent / "Notes"
DECK = "Notes"
URL = "http://127.0.0.1:8765"

CARDS_BLOCK = re.compile(r"^## Cards\s*$(.*?)(?=^## |\Z)", re.M | re.S)
QA = re.compile(r"^Q:\s*(.+?)\s*^A:\s*(.+?)(?=^Q:|\Z)", re.M | re.S)


def anki(action, **params):
    req = json.dumps({"action": action, "version": 6, "params": params}).encode()
    with urllib.request.urlopen(urllib.request.Request(URL, req)) as r:
        res = json.load(r)
    if res["error"]:
        raise RuntimeError(f"{action}: {res['error']}")
    return res["result"]


def parse(md):
    """Yield (question, answer) from every `## Cards` block in a note."""
    for block in CARDS_BLOCK.findall(md):
        for q, a in QA.findall(block):
            yield q.strip(), a.strip()


def esc(s):
    return s.replace('"', '\\"')


def main():
    try:
        anki("createDeck", deck=DECK)
    except urllib.error.URLError:
        sys.exit("Anki not reachable on 8765. Start Anki (AnkiConnect add-on 2055492159).")

    added = updated = 0
    for path in sorted(ROOT.rglob("*.md")):
        tag = path.parent.name
        for q, a in parse(path.read_text()):
            existing = anki("findNotes", query=f'deck:{DECK} "front:{esc(q)}"')
            if existing:
                anki("updateNoteFields", note={"id": existing[0], "fields": {"Back": a}})
                updated += 1
            else:
                anki("addNote", note={
                    "deckName": DECK,
                    "modelName": "Basic",
                    "fields": {"Front": q, "Back": a},
                    "tags": [tag],
                    "options": {"allowDuplicate": False},
                })
                added += 1
    print(f"{added} added, {updated} updated")


def test():
    md = "intro\n## Cards\nQ: a?\nA: one\nline two\n\nQ: b?\nA: two\n\n## Other\nQ: no\n"
    assert list(parse(md)) == [("a?", "one\nline two"), ("b?", "two")], list(parse(md))
    assert list(parse("no cards here")) == []
    print("ok")


if __name__ == "__main__":
    test() if "--test" in sys.argv else main()
