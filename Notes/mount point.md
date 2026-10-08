---
tags: [linux, filesystem]
---
Linux has no drive letters. A file system is attached at a directory, the mount
point, and serves every path under it. For a path that is not itself a mount
point, the nearest mount above it wins. `/etc`, `/usr` and `/var` are usually
plain directories inside the file system mounted on `/`, not attachments of
their own.

The mount table is the kernel's list of what is attached where:

```bash
mountpoint <path>    # is this directory itself an attachment?
findmnt -T <path>    # which mount actually serves this path?
```

Mounting over a directory hides its content rather than deleting it. The
shadowed entries come back when you unmount.

See [[File system]]
