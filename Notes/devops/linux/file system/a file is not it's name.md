To understand [[hardlink]] or [[symlinks]] we must assert this : in [[linux]] a file and it's name are two separate things.

The permissions, dates, owner and the **pointers to the data blocks** are stored in another structure called [[inode]], identified by an unique identifier in the [[File System]]. The data itself lives in the blocks, not in the inode.

The name, is just an entry in a **directory** pointing to that inode. A directory is exactly that : a table mapping names to inode numbers, which is why [[Creating a file is writing in the directory|creating a file is a write to the directory]].

Nothing stops two different names from pointing to the same file, this what [[hardlink]] do.

```bash
ls -li report.txt
```

```
8591538 -rw-r--r--. 1 ansible ansible 17 Jul 23 10:04 report.txt
```

the first column, added by the `-i` option, is the inode identifier. The number just after the permissions, here it is `1` is the reference counter.

## Cards
Q: in linux, what is the relationship between a file and its name?
A: they are two separate things. The metadata and the pointers to the data blocks live in an inode, the name is only an entry in a directory pointing to that inode.

Q: what is a directory, structurally?
A: a table mapping names to inode numbers. That is why creating a file is a write to the directory.

Q: what does the `-i` option add to `ls -l`?
A: the inode identifier, in the first column.

Q: in `ls -l`, what is the number just after the permissions?
A: the reference counter, the number of names pointing to that inode.

Q: does the inode contain the name of the file?
A: no. The name lives in the directory, not in the inode. That is why one inode can have several names.
