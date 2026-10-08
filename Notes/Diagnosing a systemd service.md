---
tags: [linux, systemd]
---
In this order:

```bash
systemctl status <svc>      # the exit code first
journalctl -u <svc>         # -b, --since, -f
systemctl cat <svc>         # the effective unit, drop-ins included
systemctl show <svc> -p UMask -p User -p StateDirectory   # resolved properties
```

The application source is the **last** place to look: a process that started
and exited by itself had time to say something, and it said it in the journal.

`cat` shows the unit text as assembled, `show` shows what the manager actually
computed, and they disagree exactly where a drop-in or a default surprises you.
With `Restart=always` the status view is useless, since the failure loops and
`status` only shows the tail of one attempt among many.

`systemctl status` prints only the last ten journal lines of the unit, and on
a service running quietly for hours those are the ones from **startup**. They
read like an ongoing failure while describing a moment long past, so check
their timestamps against `Active: since` and use
`journalctl -u <unit> --since -10min` for what is happening now.

Also misleading: a service that still answers proves nothing after a permission change,
see [[Permissions are checked at open]]. Test as the service identity,
`sudo -u <service-user> <command>`, and check the directory with `ls -ld`.

On `no space left on device`, ask the file system per mount point with
`df -h <path>` and `du -sh <mount>`, see [[df vs du]].

See [[systemd exit codes]], [[Unit files]]
