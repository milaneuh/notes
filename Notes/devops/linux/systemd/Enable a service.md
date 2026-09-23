In [[systemd]], when you run `systemctl enable <service>`, [[systemd]] reads only the `[Install]` section of the [[Unit Files|unit]] and creates the [[symlinks]] that section asks for :

- for each `WantedBy=X`, a symlink in `X.wants/`
- for each `RequiredBy=X`, a symlink in `X.requires/`
- for an `Alias=`, a symlink named after the alias

It is usually a single symlink. `systemctl disable` deletes it, and that is basically all these two commands do.

The symlink **is** the activation. At boot, systemd reaches a target and starts everything that is symlinked in the `.wants/` directory of that target. It never reads `[Install]`. So as long as the symlink does not exist, that section does nothing, even if it has been in the unit file since the beginning.

```bash
ls -l /etc/systemd/system/multi-user.target.wants/
```

The targets of those symlinks also show the split : the packaged units point to `/usr/lib/systemd/system/`, yours point to `/etc/systemd/system/`. The distribution provides the definition, the administrator takes the decision to enable it.

See [[Active vs Enabled service]]

## Cards
Q: what does `systemctl enable <service>` actually do?
A: it reads only the `[Install]` section of the unit and creates the symlinks that section asks for. That is basically all it does; `disable` deletes them.

Q: `WantedBy=X` in `[Install]` — what does enabling create?
A: a symlink in `X.wants/`.

Q: at boot, how does systemd decide what to start?
A: it reaches a target and starts everything symlinked in that target's `.wants/` directory. It never reads `[Install]` at boot — the symlink **is** the activation.

Q: a unit has had `[Install]` in it since the beginning but the service does not start at boot. Why?
A: the symlink does not exist. Without it `[Install]` does nothing, because systemd only reads that section at `enable` time.

Q: what does the target of an enable symlink tell you?
A: where the unit came from. Packaged units point to `/usr/lib/systemd/system/`, yours point to `/etc/systemd/system/` — the distribution provides the definition, the administrator takes the decision.
