---
tags: [linux, systemd]
---
Loaded into memory, which is why restarting a service does not pick up an edit.
systemd has to re-read them and rebuild its dependency graph first:

```bash
systemctl daemon-reload
```

The sequence after editing a unit is always edit, `daemon-reload`, restart,
verify. systemd does warn you when you forget, and that warning means you are
testing the old version of the unit.

Options worth knowing: [[systemd Type]], [[systemd StateDirectory]].

See [[systemd]], [[systemd Timers]]
