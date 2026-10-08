---
tags: [linux, filesystem, permissions]
---
A new file is owned by the effective UID of the process that created it, not by
the owner of the directory. Files written by a service running as `svcuser` are
owned by `svcuser` and cannot be owned by `root` unless the service runs as
root.

The containing directory is a separate decision, and the better one is usually
`root:svcgroup 0770`: the service writes inside but cannot `chmod` the
directory to widen access, since widening requires owning it. With
`svcuser:svcgroup 0750` a compromised service can widen its own access.

Exception: with the setgid bit on the directory, new entries inherit the
directory's group instead of the creating process's.

See [[Unix permissions]], [[systemd StateDirectory]]
