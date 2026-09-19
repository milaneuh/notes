**The** Filesystem Hierarchy Standard or FHS defines the arborescence and the content of the main directories of the [[File System]] in a Linux system.

The arborescence is :

| directory | description                                               |
| --------- | --------------------------------------------------------- |
| etc       | Configuration files of the system and the services        |
| var       | Variable files such as logs, databases or temporary files |
| bin       | Essential command binaries                                |
| boot      | Static files of the boot loader                           |
| dev       | Device files                                              |
| lib       | Essential libraries (shared)                              |
| media     | [[mount point]] for removable media                       |
| mnt       | [[mount point]] for temporary mounting a [[File System]]  |
| opt       | Add-on application software packages                      |
| proc      | Kernel and process interface                              |
| run       | Data relevant for running processes                       |
| sbin      | Essential system binaries                                 |
| srv       | Data for services provided by this system                 |
| sys       | Kernel and device interface                               |
| tmp       | Temporary files                                           |
| usr       | Secondary hierarchy                                       |
| home      | Home directories of normal users                          |
| root      | Home directory of root                                    |

## Not all of these are real directories on a disk

Four of them are **pseudo filesystems** : the kernel exposes information as if it were files, and nothing is stored on a disk.

- `proc` : one directory per process, plus kernel state. `/proc/<pid>/fd/` is the only way to reach a file that has no name any more, see [[Deleted but still open files]].
- `sys` : devices, drivers, and [[cgroups]] under `/sys/fs/cgroup`.
- `dev` : device files.
- `run` : a `tmpfs`, so it lives in RAM and is emptied at every boot. That is why pid files and sockets live there.

`tmp` is often a `tmpfs` too, and it carries the sticky bit (`drwxrwxrwt`) so that everybody can write in it but nobody can delete somebody else's files, see [[Permissions on a directory]].

## The usr merge

On most modern distributions `bin`, `sbin` and `lib` are symlinks into `usr`. So `/bin/ls` and `/usr/bin/ls` are the same file. The FHS distinction between them is historical : it dates from a time when `usr` could be a separate, later-mounted [[File System]], and the essential binaries had to be available before that.

`systemctl status` says `Tainted: unmerged-bin` on a system where the merge has not happened.

## Cards
Q: what does the FHS define?
A: the arborescence and the content of the main directories of the file system in a Linux system.

Q: which directories of the FHS are not stored on a disk?
A: `proc`, `sys`, `dev` and `run`. They are pseudo filesystems, the kernel exposes information as files. `run` is a tmpfs and is emptied at every boot.

Q: what is `/srv` for?
A: data for the services provided by this system.

Q: why are `/bin` and `/usr/bin` the same thing on a modern system?
A: because of the usr merge, `bin`, `sbin` and `lib` are symlinks into `usr`. The original distinction existed because `usr` could be a separate filesystem mounted later.
