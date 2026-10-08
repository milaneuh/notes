---
tags: [linux, systemd]
---
`code=exited, status=N/NAME` says **who** failed, so it says where to look.
systemd reserves statuses from **200** up for its own failures, the ones that
happen before your program starts. Below that it is your program's own exit
status.

| seen | who failed | where to look |
|---|---|---|
| `status=1` or another small number | your program ran and exited | the journal |
| `203/EXEC` | systemd could not exec the command | the unit, `ExecStart=` |
| `200/CHDIR` | `WorkingDirectory=` does not exist | the unit |
| `217/USER` | the `User=` does not exist | the unit |
| `226/NAMESPACE` | a sandboxing directive failed | the unit |
| `killed, signal=KILL` | nobody: OOM, or a stop | memory, or who stopped it |
| `killed, signal=SEGV` | your program crashed | the journal, core dump |

Usual causes of `203/EXEC`: wrong or missing path, missing `x` bit, a shebang
pointing at an absent interpreter, or a confinement directive like
`ProtectSystem=` hiding the path from the service.

On a `203/EXEC` the journal is empty, and the emptiness **is** the signal:
the program never started, which sends you to the unit, not to the logging.

`systemd-analyze exit-status 203` decodes one; the full list is
`man systemd.exec`, section *Process Exit Codes*.

See [[Diagnosing a systemd service]]
