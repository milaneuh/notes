#!/usr/bin/env python3
"""Push the notes into Anki via AnkiConnect, one note = one card.

The vault is flat Zettelkasten: every .md under Notes/ holds a single idea and
its title is a statement, not a question. The title becomes the card front, the
body the card back, minus the trailing `See [[...]]` block, which is navigation
for Obsidian and noise on a flashcard.

    Notes/A Pod shares the network namespace between its containers.md
    ---
    tags: [k8s]
    ---
    They see the same IP and talk over `localhost`. See [[Pods are the ...]]

Frontmatter is stripped; `tags:` becomes the Anki tags. Only the notes at the
top level of Notes/ are cards: anything in a sub-directory is reference material
and is left alone.

Images embed as `![[file.png]]` (found anywhere under Notes/) or `![alt](url)`;
line breaks, `code` and code blocks are kept, `[[wikilinks]]` become plain text.

Re-running is idempotent: same title -> updated back, new title -> new card.
Renaming a note makes a new card, the old one stays in Anki.
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

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
TAGS = re.compile(r"^tags:\s*\[(.*?)\]\s*$", re.M)
SEE = re.compile(r"\n\s*\nSee .*\Z", re.S)  # trailing link block, for Obsidian only


def anki(action, **params):
    req = json.dumps({"action": action, "version": 6, "params": params}).encode()
    with urllib.request.urlopen(urllib.request.Request(URL, req)) as r:
        res = json.load(r)
    if res["error"]:
        raise RuntimeError(f"{action}: {res['error']}")
    return res["result"]


def parse(md):
    """(tags, body) of a note."""
    m = FRONTMATTER.match(md)
    meta, body = (m.group(1), md[m.end():]) if m else ("", md)
    t = TAGS.search(meta)
    tags = [x.strip() for x in t.group(1).split(",") if x.strip()] if t else []
    return tags, SEE.sub("", body.strip()).strip()


IMG = re.compile(r"!\[\[([^\]]+)\]\]|!\[[^\]]*\]\(([^)]+)\)")
BLOCK = re.compile(r"^```[^\n]*\n(.*?)^```\s*$", re.M | re.S)
CODE = re.compile(r"`([^`]+)`")
LINK = re.compile(r"(?<!!)\[\[([^\]|:]+)(?:\|([^\]]+))?\]\]")  # not [[:space:]]


def media(ref):
    """Store an image in Anki's media folder, return its filename."""
    if ref.startswith(("http://", "https://")):
        name = ref.rsplit("/", 1)[-1]
        anki("storeMediaFile", filename=name, url=ref, deleteExisting=False)
        return name
    hit = next(ROOT.rglob(ref), None)
    if hit is None:
        return None
    anki("storeMediaFile", filename=hit.name, path=str(hit.resolve()), deleteExisting=False)
    return hit.name


def render(text):
    """Markdown subset -> Anki field HTML."""
    def img(m):
        name = media(m.group(1) or m.group(2))
        return f'<img src="{name}">' if name else m.group(0)
    text = IMG.sub(img, text)
    text = LINK.sub(lambda m: m.group(2) or m.group(1), text)
    text = BLOCK.sub(lambda m: f"<pre>{m.group(1).rstrip()}</pre>", text)
    text = CODE.sub(r"<code>\1</code>", text)
    # <pre> keeps its own newlines, everything else needs <br>
    return "".join(
        p if i % 2 else p.replace("\n", "<br>")
        for i, p in enumerate(re.split(r"(<pre>.*?</pre>)", text, flags=re.S))
    )


def esc(s):
    return s.replace('"', '\\"')


def main():
    try:
        anki("createDeck", deck=DECK)
    except urllib.error.URLError:
        sys.exit("Anki not reachable on 8765. Start Anki (AnkiConnect add-on 2055492159).")

    added = updated = 0
    for path in sorted(ROOT.glob("*.md")):
        tags, body = parse(path.read_text())
        front, back = path.stem, render(body)
        existing = anki("findNotes", query=f'deck:{DECK} "front:{esc(front)}"')
        if existing:
            anki("updateNoteFields", note={"id": existing[0], "fields": {"Back": back}})
            anki("addTags", notes=existing, tags=" ".join(tags)) if tags else None
            updated += 1
        else:
            anki("addNote", note={
                "deckName": DECK,
                "modelName": "Basic",
                "fields": {"Front": front, "Back": back},
                "tags": tags,
                "options": {"allowDuplicate": False},
            })
            added += 1
    print(f"{added} added, {updated} updated")


def test():
    assert parse("---\ntags: [a, b]\n---\nbody\n") == (["a", "b"], "body")
    assert parse("plain body") == ([], "plain body")
    assert parse("claim\n\nSee [[a]], [[b]]\n") == ([], "claim")

    global media
    media = lambda ref: ref.rsplit("/", 1)[-1]
    assert render("a\nb") == "a<br>b"
    assert render("use `ls`") == "use <code>ls</code>"
    assert render("![[x.png]]") == '<img src="x.png">'
    assert render("![d](http://h/y.png)") == '<img src="y.png">'
    assert render("see [[a note]] and [[x|y]]") == "see a note and y"
    assert render("sed 's/[[:space:]]//'") == "sed 's/[[:space:]]//'"
    assert render("x\n```sh\nls\ncd\n```") == "x<br><pre>ls\ncd</pre>"
    print("ok")


if __name__ == "__main__":
    test() if "--test" in sys.argv else main()
