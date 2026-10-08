---
name: anki-cards
description: Write notes in this flat Zettelkasten vault as atomic Anki cards (title = front, body = back), then sync them to Anki. Use when the user asks to add or refresh notes / flashcards / Anki cards, or names a subject to make notes for.
---

# Notes are the cards

The vault is flat: every `.md` lives directly in `Notes/`. One note holds one
idea, and **the note itself is the card** — the filename is the front, the body
is the back. There are no `## Cards` blocks and no index notes; links between
notes are the only structure.

Sub-directories of `Notes/` (e.g. `Notes/KBRW/`) hold reference material, not
cards. The sync skips them.

## 1. Write atomic notes

The title is a **statement, not a question, not a topic**:

- `Unit files are cached until daemon-reload.md` — good, it's the claim itself.
- `What does daemon-reload do?.md` — no, that's a flashcard question.
- `systemd.md` — no, that's a topic. Split it into the claims it contains.

Body: 1–5 lines answering "why / how", plus code if the note is about a
command. If the body needs an "and" between two unrelated facts, it's two
notes. Keep the user's own wording and code formatting.

```markdown
---
tags: [systemd]
---
systemd reads unit files into memory at boot. Editing a file on disk changes
nothing until `systemctl daemon-reload` re-reads it.

See [[A unit file describes one service to systemd]]
```

Rules:

- Filenames are the identity. Reuse a title verbatim to update its card;
  rename it and you get a new card (the old one stays in Anki).
- Link liberally with `[[Other note title]]` — in a flat vault links are the
  only structure. Put them in a trailing `See [[...]]` block: the sync strips
  that block, so links stay in Obsidian and never reach the card. A link inside
  the body itself renders as plain text on the card.
- `tags:` in frontmatter become the Anki tags. Use the subject (`k8s`, `linux`,
  `systemd`, `kbrw`).
- Images work on either side: `![[Pasted image ....png]]` or `![alt](https://...)`.
- Line breaks, `inline code` and fenced code blocks survive into the card;
  other markdown does not.
- Before writing, grep the vault for a note that already states the idea and
  extend it instead of adding a near-duplicate.
- No em dashes. Use a colon, a comma or a full stop.

## 2. Sync

```bash
python3 anki_sync.py
```

Prints `N added, M updated`. Requires Anki running with the
AnkiConnect add-on (code 2055492159); the script exits with that message if it
can't reach it. If Anki isn't running, say so — the notes are written and will
sync on the next run, that's not a failure.
