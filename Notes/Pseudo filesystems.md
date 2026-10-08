---
tags: [linux, filesystem]
---
Four entries of the [[FHS]] are not stored on a disk at all: the kernel exposes
state as if it were files.

- `proc`: one directory per process plus kernel state. `/proc/<pid>/fd/` is the
  only way to reach a file that has no name any more.
- `sys`: devices, drivers, and the [[cgroups]] under `/sys/fs/cgroup`.
- `dev`: device files.
- `run`: a tmpfs, so it lives in RAM and is emptied at every boot, which is why
  pid files and sockets live there.

`/tmp` is often a tmpfs too.
