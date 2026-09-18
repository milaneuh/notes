In your system [[Unit Files]] are loaded in memory, so simply restarting a service wont apply the changes made to it's unit file. systemd has to re-read the unit files and rebuild its dependency graph first, you can ask for that using

```bash
	systemctl daemon-reload
```

So the sequence after editing a unit is always : edit, `daemon-reload`, `restart`, then verify.

systemd does warn you if you forget, but the warning is easy to skip past :

```
Warning: The unit file, source configuration file or drop-ins of <service> changed
on disk. Run 'systemctl daemon-reload' to reload units.
```

If you see it, you are testing the old version of the unit.

See [[Diagnosing a systemd service]]

## Cards
Q: why does restarting a service not apply changes to its unit file?
A: unit files are loaded in memory. systemd has to re-read them and rebuild its dependency graph first, via `systemctl daemon-reload`.

Q: what is the sequence after editing a unit file?
A: edit, `daemon-reload`, `restart`, then verify.

Q: systemd warns you if you forget `daemon-reload` — what does that warning mean in practice?
A: that you are testing the old version of the unit. The warning is easy to skip past.
