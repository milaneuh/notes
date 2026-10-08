---
tags: [linux, filesystem]
---
`ln report.txt copy.txt` copies nothing: it adds a second name pointing at the
existing [[inode]], and the reference counter goes from 1 to 2. Writing through
one name shows through the other, because there is only one file.

Deleting one name only decrements the counter. The content survives under the
remaining name, and the inode is freed only when the counter reaches 0 and
nothing holds it open.

See [[hardlink limits]], [[df vs du]]
