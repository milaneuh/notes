---
name: anki-cards
description: Write Anki flashcards into notes as `## Cards` blocks, then sync them to Anki. Use when the user asks to generate, add, or refresh flashcards / Anki cards from their notes, or names a note or folder to make cards for.
---

# Anki cards from notes

Two steps: append a `## Cards` block to the note(s), then run `anki_sync.py`.

## 1. Pick the notes

- User named notes or a folder → use those.
- User said "my notes" with no target → ask which folder, don't do all 38.
- Skip index/hub notes (a note whose body is mostly `[[links]]` with one-line
  descriptions). They have no content to test, only structure.

Read each note fully before writing cards for it.

## 2. Write the cards

Append to the end of the note, keeping any existing `## Cards` block and adding
to it rather than replacing it:

```markdown
## Cards
Q: what does umask do to a requested mode?
A: subtracts. The result is `requested & ~umask`; it never adds a bit the program didn't ask for.
```

Rules:

- Format is exact: `Q:` line, then `A:` which may span multiple lines until the
  next `Q:` or the end of the block. The sync script's parser depends on this.
- **The question is the identity.** Re-running the skill on a note matches
  existing cards by question text. Reuse a question verbatim to update its
  answer; change the wording and you get a duplicate card instead.
- 3–6 cards per note. A note that yields more is really several notes.
- One fact per card. If the answer needs "and", it's two cards.
- Test understanding, not recall of phrasing. `Q: why does editing a unit file
  not take effect?` beats `Q: what does the note say about caching?`.
- Tables and lists in a note are usually one card per row, not one card for the
  whole table.
- Keep the note's own wording and code formatting in the answer. The user wrote
  it that way on purpose.
- Skip anything already covered by an existing card in that note.

## 3. Sync

```bash
python3 anki_sync.py
```

Prints `N added, M updated`. Requires Anki running with the AnkiConnect add-on
(code 2055492159); the script exits with that message if it can't reach it.
If Anki isn't running, say so and tell the user the cards are in the notes and
will sync on the next run — don't treat it as a failure.

Cards are tagged with their parent folder name (`devops`, `KBRW`).
