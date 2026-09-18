hardlink can not be used for everything and does bring limitations, such as 

1. You cannot hardlink a directory
The linux system prevents it, if you did hardlink between directories it would create a reference loop in the arborescence. 

```bash
ln ~/lab /home/ansible/lab-copy
```

```
ln: ~/lab: hard link not allowed for directory
```


2. You cannot hardlink between two [[File System]]
The inode identifier only makes sense in it's own FS. The inode `1234567` in your disk and the same inode in a flash usb drive are not the same.

```bash
ln ~/report.txt /dev/shm/test
```

```
ln: failed to create hard link '/dev/shm/test' => '/home/ansible/report.txt':
Invalid cross-device link
```

`/dev/shm` is a tmpfs, so another [[File System]]. Note that the error message tells you which of the two limits you just hit.

If what you are trying to do fits in one of these limitations, checkout [[symlinks]]

## Cards
Q: what are the two limits of hardlinks?
A: you cannot hardlink a directory, and you cannot hardlink between two file systems.

Q: why can you not hardlink a directory?
A: it would create a reference loop in the arborescence, so the system prevents it.

Q: why can you not hardlink across file systems?
A: an inode identifier only makes sense inside its own file system. The inode `1234567` on your disk and the same number on a usb drive are not the same inode.

Q: `ln` fails with "Invalid cross-device link". Which limit did you hit?
A: the second one, the two paths are on different file systems. The directory limit gives a different message, "hard link not allowed for directory".

Q: what do you use when you hit one of the two limits?
A: a symlink.
