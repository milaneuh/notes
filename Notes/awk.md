---
tags: [linux, tooling]
---
A field-oriented processing language. `grep` filters entire lines and `cut`
extracts fixed columns; awk cuts each line into a data structure you can test,
accumulate and reformat. Reach for it when you need the *data* of a line and
not its raw text.

Before your code runs, awk has split the line on the separator into `$1` to
`$NF`, with `$0` the whole line. Every block is a pattern followed by an action,
and the action only runs on lines the pattern matches. `NR` is the current line
number, so a csv header is skipped with `NR == 1 {next}` or guarded with
`NR > 1 { ... }`. The `END` block runs once after the last line, which is where
you print what you accumulated.

```bash
awk -F';' 'NR == 1 {next}
{ total += $3; lines++ }
END { print "average:", total/lines }' invoice.csv
```

`-F` sets the separator and has to be quoted: a bare `;` is read by the shell
as a command separator, so awk gets a `-F` with no argument.
