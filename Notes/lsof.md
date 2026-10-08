---
tags: [linux, tooling]
---
Lists open files, sockets, and files kept open after deletion. The one that
matters in practice is `lsof +L1`: entries with a link count of 0, deleted but
still held by a process, which is the usual answer to
[[df vs du|df and du disagreeing]].

Cheatsheet: https://linuxize.com/cheatsheet/lsof/
