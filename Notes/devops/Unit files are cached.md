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
