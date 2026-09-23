xargs will read each `stdin` argument line by line (or word by word) and will put each entries as an argument to a command. It's an alternative to `for` loops. 

Basic example :
```bash
ls *.txt | xargs wc -l
```

This is close to `wc -l list1.txt list2.txt`, but not identical, and the difference is the whole point of the tool. The kernel caps how long an argument list can be, and you can read that cap with `getconf ARG_MAX`. When the list is longer, xargs runs the command **several times**, in batches. So with `wc -l` on thousands of files you get several `total` lines, not one. That batching is why xargs works regardless of the number of files, and why `cmd *` fails with `Argument list too long`.

The example above is also the unsafe habit. xargs splits on blanks by default, so a file named `mon rapport.txt` becomes two arguments and the command sees two files that do not exist. As long as you manipulate paths, use a separator that cannot appear in a filename :

```bash
find . -name '*.txt' -print0 | xargs -0 wc -l
```

`-print0` terminates each name with a NUL byte, `-0` tells xargs to split on that. Nothing else is safe, because a filename can legally contain spaces, quotes, newlines, everything except `/` and NUL.

Three options worth knowing :

- `-I {}` puts the argument where you want instead of at the end, which unlocks every command that takes its argument in the middle. It forces one execution per argument, so you lose the batching.
- `-P 4` runs four executions in parallel. That is what a `for` loop cannot do, and it is often the real reason to reach for xargs.
- `-t` prints each command before running it. For a full dry run, prefix the command with `echo`.

Portability trap, and it matters when you work on a Mac and on Linux VMs. On empty input, GNU xargs still runs the command once unless you pass `-r`. BSD xargs, the one on macOS, does not run it and ignores `-r`. Same script, two behaviours.

When not to use it : `find … -exec cmd {} +` does the same batching without a pipe and without any separator problem. For anything with real logic, `while IFS= read -r line` is more readable. And a pipeline built on `ls` output is a bug waiting to happen whatever comes after it.

See [[find]], [[ARG_MAX]], [[linux]]

## Cards
Q: what does `xargs` do?
A: it reads arguments from `stdin` and appends them to a command. An alternative to a `for` loop.

Q: `ls *.txt | xargs wc -l` is the same as `wc -l a.txt b.txt` ?
A: close, but not identical. If the list exceeds `ARG_MAX`, xargs runs the command in several batches, so you get several `total` lines.

Q: why does xargs exist at all?
A: the kernel caps the length of an argument list (`getconf ARG_MAX`). xargs splits the input into batches that stay under it, which is why `cmd *` fails with `Argument list too long` where xargs succeeds.

Q: what breaks `find . | xargs cmd` ?
A: xargs splits on blanks, so a filename containing a space becomes two arguments.

Q: what is the safe form when you pipe filenames?
A: `find . -print0 | xargs -0 cmd`. NUL is the only byte that cannot appear in a filename.

Q: how do you place the argument somewhere other than the end?
A: `-I {}`. It forces one execution per argument, so you lose the batching.

Q: which xargs option a `for` loop cannot replace?
A: `-P n`, which runs n executions in parallel.

Q: how do you see what xargs is about to run?
A: `-t` prints each command before running it. For a real dry run, prefix with `echo`.

Q: xargs with empty input, what happens?
A: GNU runs the command once anyway unless you pass `-r`. BSD (macOS) does not run it and ignores `-r`.

Q: when should you not use xargs?
A: when `find … -exec cmd {} +` does the job without a pipe, or when the logic is rich enough that `while IFS= read -r line` reads better.
