---
tags: [linux, systemd]
---
`systemctl enable` reads only the `[Install]` section and creates the symlinks
it asks for: one in `X.wants/` per `WantedBy=X`, one in `X.requires/` per
`RequiredBy=X`, one named after an `Alias=`. Usually a single symlink.
`disable` deletes it, and that is essentially all these commands do.

**The symlink is the activation.** At boot systemd reaches a target and starts
whatever is symlinked in that target's `.wants/` directory; it never reads
`[Install]` then. A unit can carry `[Install]` since forever and still not
start, because the symlink was never created.

The target of the symlink says who decided: packaged units point into
`/usr/lib/systemd/system/`, yours into `/etc/systemd/system/`. The distribution
provides the definition, the administrator takes the decision.

See [[Active vs Enabled]]
