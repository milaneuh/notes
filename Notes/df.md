---
tags: [linux, tooling]
---
Disk free: the available space of a file system.

```bash
df -h /srv/catalog
```

Whatever you point it at, df never talks about that object, it talks about the
file system that **contains** it. So read it per [[mount point]], never
globally. `-h` is human readable in powers of 1024, `-H` the same in powers of
1000.

See [[df vs du]]
