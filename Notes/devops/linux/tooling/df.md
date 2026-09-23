The df (disk free) command shows the available disk space in a file system

Example : 

```bash
	df -h /srv/catalog
```

Whatever argument you give it, df never talks about that object, it talks about the **file system that contains it**. So read it per [[mount point]], not globally.

The -h flag is to print in a human readable format, in powers of 1024. The capital `-H` is the same thing in powers of 1000.

See [[df vs du]]

## Cards
Q: what does df show?
A: the available disk space of a file system.

Q: you run df on a file. What does it report?
A: not the file, the file system that **contains** it. df always answers about the containing file system, so read it per mount point and never globally.

Q: difference between `df -h` and `df -H`?
A: `-h` is human readable in powers of 1024, `-H` is the same in powers of 1000.
