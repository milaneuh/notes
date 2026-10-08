---
tags: [linux, filesystem]
---
A file and its name are two separate things. The inode holds the metadata,
owner, dates and the pointers to the data blocks; the name is only an entry in
a directory pointing at that inode. The inode does not know its own name, which
is why one file can have several.

A directory, structurally, is a table mapping names to inode numbers. That is
why [[Creating a file is writing in the directory]].

```
$ ls -li report.txt
8591538 -rw-r--r--. 1 ansible ansible 17 Jul 23 10:04 report.txt
```

`-i` prints the inode id in the first column, and the number right after the
permissions is the reference counter: how many names point at that inode.

```bash
stat -c 'link=%h inode=%i' a.txt   # counter and inode in one shot
find ~/lab -inum 8591547           # every name pointing at it
```

See [[hardlink]], [[symlink]]
