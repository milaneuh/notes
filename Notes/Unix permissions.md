---
tags: [linux, filesystem, permissions]
---
Three classes, owner, group and other, each with `r`, `w` and `x`. The letters
do not mean the same thing on a file and on a directory:

| | file | directory |
|---|---|---|
| `r` | read the content | list the names |
| `w` | modify the content | create or delete entries |
| `x` | execute as a program | traverse, ie. resolve a name inside |

The pieces:

- [[Permissions on a directory]], where `x` is the gate
- [[Creating a file is writing in the directory]]
- [[File ownership]], who owns a new file and why it matters
- [[root is not a permission class]]
- [[umask]], what the mode starts from
- [[Permissions are checked at open]], why a change looks like it worked

See [[File system]]
