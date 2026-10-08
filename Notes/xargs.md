---
tags: [linux, tooling]
---
Reads arguments from stdin and appends them to a command, an alternative to a
`for` loop: `ls *.txt | xargs wc -l`.

It exists because of [[ARG_MAX]]. When the input is longer than the cap, xargs
runs the command in several batches, which is why `wc -l` prints several
`total` lines, and why `cmd *` dies with `Argument list too long` where xargs
succeeds.

The habit above is the unsafe one: xargs splits on blanks, so `mon rapport.txt`
becomes two arguments naming two files that do not exist. For paths there is
only one safe form, since a filename may contain anything but `/` and NUL:

```bash
find . -name '*.txt' -print0 | xargs -0 wc -l
```

Three options worth knowing. `-I {}` places the argument somewhere other than
the end, at the cost of one execution per argument, so the batching is lost.
`-P 4` runs four executions in parallel, which a `for` loop cannot do and is
often the real reason to reach for xargs. `-t` prints each command before
running it, and prefixing with `echo` gives a true dry run.

Portability trap between a Mac and a linux VM: on empty input GNU xargs still
runs the command once unless you pass `-r`, while BSD xargs does not run it and
ignores `-r`.

When not to use it: `find … -exec cmd {} +` does the same batching with no pipe
and no separator problem, `while IFS= read -r line` reads better for real
logic, and a pipeline built on `ls` output is a bug whatever follows it.
