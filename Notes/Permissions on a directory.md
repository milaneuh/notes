---
tags: [linux, filesystem, permissions]
---
`x` is the gate. Without it nothing inside is reachable by path, whatever the
mode of the files themselves. With `r` and no `x` you can list the names but
not open them.

So the non-zero digits of a directory mode are almost always odd: the usual
modes are `0700`, `0750`, `0755`, `0770`, `0775`, and something like `0660` on
a directory is a bug. The `x` bit on a data *file*, on the other hand, is
meaningless.

To close access to a directory's content, remove `x` from `other` on the
directory. That is more effective than tightening every file inside.

`/tmp` is the special case: `drwxrwxrwt`, where the sticky bit lets everybody
write but only the owner of an entry remove it. Without it, `w` on the
directory would be enough to delete somebody else's files.

See [[Unix permissions]]
