---
tags: [linux, tooling, networking]
---
Socket statistics: states, addresses and owning processes.

```bash
ss -ltu     # every listening TCP and UDP socket
ss -ltnp    # same, numeric, with the process behind each socket
```

`-p` only names the process for sockets you own unless you are root.

Read it before reading the service configuration: ss shows the endpoint
actually bound, which is the running state, while the file only shows the
intention. See [[Configured state vs running state]], [[Listening address]].
