---
tags: [linux, filesystem, permissions]
---
The user file-creation mode mask subtracts rights, it never grants them. The
result is `requested mode AND NOT umask`.

Write one by answering "what do I forbid?" three times, with `r=4 w=2 x=1`:
forbid nothing for owner, write for group, everything for other, so `027`.

| umask | meaning | file (0666) | dir (0777) |
|---|---|---|---|
| 022 | the default, everyone reads | 0644 | 0755 |
| 027 | group reads, other nothing | 0640 | 0750 |
| 007 | group reads and writes | 0660 | 0770 |
| 077 | owner only | 0600 | 0700 |

You cannot predict a mode from the umask alone, because the requested mode is a
property of the program: most ask `0666` for files and `0777` for directories,
SQLite asks `0644`, key tools ask `0600`. And "the mask is 7 minus what I want"
only works for directories, for the same reason. Check with `ls -l` instead of
trusting the arithmetic.

See [[Unix permissions]], [[systemd StateDirectory]]
