---
tags: [linux, filesystem]
---
**You cannot hardlink a directory.** It would create a reference loop in the
tree, so the kernel refuses: `ln: hard link not allowed for directory`.

**You cannot hardlink across file systems.** An inode number only means
something inside its own file system: inode `1234567` on the disk and on a usb
key are not the same inode. The error says which limit you hit,
`Invalid cross-device link`.

Hit either one and you want a [[symlink]].
