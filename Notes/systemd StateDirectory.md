---
tags: [linux, systemd]
---
Takes a whitespace-separated list of names, creates them below `/var/lib` when
the unit starts and exports `$STATE_DIRECTORY` with the full paths:
`StateDirectory=aaa/bbb ccc` gives `/var/lib/aaa/bbb:/var/lib/ccc`. The
directory is owned by root unless `User=` or `Group=` says otherwise.

It takes over an existing directory and **rewrites owner and mode at every
start**, so any `chown` or `chmod` done by hand is silently reverted.

`StateDirectoryMode=` defaults to `0755`, which lets `other` traverse and list.
And it only controls the directory: the mode of the files inside comes from the
process [[umask]], so both lines are needed.

```ini
StateDirectory=catalog-api
StateDirectoryMode=0750
UMask=027
```

For an owner systemd would not choose, root-owned while the service writes
inside, declare the directory in `/etc/tmpfiles.d/` instead (`man tmpfiles.d`).
The point of either is the same: the fix lives in a versioned file instead of a
`chmod` somebody typed once.

See [[File ownership]], [[Unit files]]
