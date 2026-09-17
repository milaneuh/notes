To diagnosis a [[systemd]] service you are usually doing this, **in this order** :

```bash
# Get the status of the service 
systemctl status <service>

# Check the logs of the service
journalctl -u <service>          # add -b for the current boot, --since, -f to follow

# Check the effective unit, drop-ins included
systemctl cat <service>

# Check the resolved properties, which is not the same thing
systemctl show <service>
systemctl show <service> -p UMask -p User -p StateDirectory
```

The order matters. The source code of the application is the **last** place to look : if the process started and exited by itself, it had time to say something, and it said it in the journal.

In `systemctl status`, read the exit code before anything else. `code=exited, status=1/FAILURE` means systemd did launch the program and the program exited on its own, so look at the application and its environment. A `203/EXEC` or `200/CHDIR` means systemd could not even launch it, so look at the unit.

See [[systemd exit codes]] for the full triage table.

`Restart=always` turns a startup failure into a loop, so `status` only shows you the last lines of one attempt among many and they scroll. On a looping service, use the journal, not `status`.

After editing the unit, see [[Unit files are cached]].

if the service is supposed to expose a port you can use `ss` to check it :
```bash
ss -ltnp                          # -l listening, -t tcp, -n numeric, -p process
```

if the service is supposed to write or read a state file, check the **directory** first, since creating a file is a write to the directory :
```bash
ls -ld <path-to-directory>       # the directory itself
ls -l  <path-to-directory>       # its content
```

and test the right under the identity the service actually runs as, not yours :
```bash
sudo -u <service-user> <command>
```

That last one is what reveals a latent failure : a service that still answers proves nothing, see [[Permissions are checked at open]].

## Cards
Q: what is the order of commands when diagnosing a systemd service?
A: `systemctl status <service>`, then `journalctl -u <service>`, then `systemctl cat <service>` for the effective unit with drop-ins, then `systemctl show <service>` for the resolved properties.

Q: where is the last place to look when a systemd service fails?
A: the source code of the application. If the process started and exited by itself, it had time to say something, and it said it in the journal.

Q: what do you read first in `systemctl status`?
A: the exit code. It tells you whether systemd failed to launch the program, or the program launched and exited on its own.

Q: why does `systemctl status` become useless on a service with `Restart=always`?
A: the startup failure turns into a loop, so `status` only shows the last lines of one attempt among many, and they scroll. Use the journal instead.

Q: `systemctl cat` vs `systemctl show` — what is the difference?
A: `cat` shows the effective unit file with drop-ins included; `show` shows the resolved properties, which is not the same thing.

Q: how do you check that a service can actually use a directory?
A: test under the identity the service runs as, not yours: `sudo -u <service-user> <command>`. And check the directory itself with `ls -ld`, since creating a file is a write to the directory.
