The df (disk free) command shows the available disk space in a file system

Example : 

```bash
	df -h /srv/catalog
```

Whatever argument you give it, df never talks about that object, it talks about the **file system that contains it**. So read it per [[mount point]], not globally.

The -h flag is to print in a human readable format, in powers of 1024. The capital `-H` is the same thing in powers of 1000.

See [[df vs du]]