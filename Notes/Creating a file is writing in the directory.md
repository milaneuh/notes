---
tags: [linux, filesystem, permissions]
---
The file does not exist yet, so the right you need is `w` on the **directory**,
not on the file. Deletion is a write to the directory too, which is why you can
delete a file you cannot read.

A permission error on file creation is therefore always a question about the
directory, and the error message rarely says so.

See [[Permissions on a directory]], [[inode]]
