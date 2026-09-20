The Socket Statistics (ss) command is a useful command to display information about network sockets. The command provides details about TCP, UDP and other socket types, including their states and associated processes.

Example: list all listening UDP and TCP sockets

Command :
```
ss -ltu
```

## Cards
Q: what does `ss -ltu` list?
A: every listening TCP and UDP socket.

Q: which option shows the process behind a socket, and what does it need?
A: `-p`, and root privileges to see sockets that do not belong to me.

Q: why read `ss` before opening the service configuration?
A: `ss` shows the endpoint actually bound, which is the running state. The configuration file only shows the intention.
