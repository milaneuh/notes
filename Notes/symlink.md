---
tags: [linux, filesystem]
---
A symbolic link is its own file, with its own [[inode]] and type `l` in
`ls -l`, holding nothing but a target path. A [[hardlink]] shares the target's
inode; a symlink does not.

Nothing guarantees the stored path still exists. When it does not, the link is
dangling: `ls` still shows it, reading it fails with
`No such file or directory`.

Symlinks are used far more than hardlinks because they have neither of the
[[hardlink limits]]: they can point at a directory and they can cross file
systems.
