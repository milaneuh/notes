---
tags: [linux, tooling]
---
The default tool for text transformation in a stream. The `s` command is
`s/PATTERN/REPLACEMENT/FLAGS`, where the pattern is a regex and the flags are
`g` (every occurrence on the line), `i` (case insensitive) or a number (that
occurrence only).

```bash
sed 's/prod/release/g' hosts.old
```

Deletion is a different command, addressed by a pattern: `/^#/d` drops
comments, `/^$/d` drops blank lines. `s///` only ever replaces.

Without `-i`, sed prints to stdout and the file is untouched. `-i.bak` edits in
place and keeps the original, which is the form to use on anything you cannot
regenerate. `-E` turns on extended regex and groups, and `-e` chains several
transformations in one pass:

```bash
sed -E -i.bak \
  -e 's/host[[:space:]]*=[[:space:]]*.*/host=db.staging.example.com/' \
  -e '/^#/d' -e '/^$/d' db.conf
```
