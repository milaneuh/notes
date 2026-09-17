When a [[systemd]] service fails, `systemctl status` shows a line like :

```
Process: 12836 ExecStart=/usr/bin/python3 /opt/app.py (code=exited, status=1/FAILURE)
```

That code tells you **who** failed, so it tells you where to look. It is the first thing to read, before the logs.

The rule : systemd reserves the statuses from **200** upwards for its own failures, the ones that happen *before* your program starts. Below that, it is the exit status of your own program.

| What you see | Who failed | Where to look |
| --- | --- | --- |
| `code=exited, status=1` or another small number | your program, it ran then exited by itself | the journal, it had time to say something |
| `status=203/EXEC` | systemd could not execute the command | the unit, `ExecStart=` |
| `status=200/CHDIR` | systemd, `WorkingDirectory=` does not exist | the unit |
| `status=217/USER` | systemd, the `User=` does not exist | the unit |
| `status=226/NAMESPACE` | systemd, a sandboxing directive failed | the unit |
| `code=killed, signal=KILL` | nobody failed, it was killed | out of memory, or a `stop` |
| `code=killed, signal=SEGV` | your program crashed | the journal, and a core dump if enabled |

The full list is in `man systemd.exec`, section *Process Exit Codes*. You can also decode one directly :

```bash
systemd-analyze exit-status 203
```

## The practical trap

On a `203/EXEC` you will open the journal, find almost nothing, and be tempted to conclude that logging is broken.

The emptiness **is** the signal. A silent journal for a service that failed means the program never started, which sends you to the unit. A talkative journal means the opposite.

Usual causes of `203/EXEC` : the path in `ExecStart=` is wrong or the file does not exist, the file is not executable so the `x` bit is missing, it is a script and its shebang points to an interpreter that is not installed, or a confinement directive like `ProtectSystem=` hides the path from the service.

See [[Diagnosing a systemd service]], [[Permissions on a directory]]

## Cards
Q: in a systemd `status=N/NAME` exit code, what is the 200 boundary?
A: systemd reserves statuses from **200** upwards for its own failures, the ones that happen before your program starts. Below that it is the exit status of your own program.

Q: `code=exited, status=1/FAILURE` — who failed and where do you look?
A: your program. It ran then exited by itself, so it had time to say something — look at the journal.

Q: `status=203/EXEC` — who failed and where do you look?
A: systemd could not execute the command. Look at the unit, `ExecStart=`.

Q: `status=200/CHDIR` — who failed?
A: systemd. `WorkingDirectory=` does not exist. Look at the unit.

Q: `status=217/USER` — who failed?
A: systemd. The `User=` does not exist. Look at the unit.

Q: `status=226/NAMESPACE` — who failed?
A: systemd. A sandboxing directive failed. Look at the unit.

Q: `code=killed, signal=KILL` — who failed?
A: nobody. It was killed — out of memory, or a `stop`.

Q: on a `203/EXEC`, the journal is empty. What does that mean?
A: the emptiness **is** the signal. A silent journal for a failed service means the program never started, which sends you to the unit — not that logging is broken.

Q: usual causes of `203/EXEC`?
A: the path in `ExecStart=` is wrong or missing, the file is not executable (no `x` bit), a script shebang points to an interpreter that is not installed, or a confinement directive like `ProtectSystem=` hides the path from the service.

Q: how do you decode a systemd exit status from the command line?
A: `systemd-analyze exit-status 203`. The full list is in `man systemd.exec`, section *Process Exit Codes*.
