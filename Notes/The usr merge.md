---
tags: [linux, filesystem]
---
On modern distributions `bin`, `sbin` and `lib` are symlinks into `usr`, so
`/bin/ls` and `/usr/bin/ls` are the same file. The [[FHS]] distinction is
historical: `usr` could be a separate file system mounted later, so the
essential binaries had to exist outside it.

`systemctl status` reports `Tainted: unmerged-bin` on a system where the merge
has not happened.
