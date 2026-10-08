---
tags: [linux, tooling]
---
Prints the [[kernel ring buffer]], which is why it answers for hardware,
drivers, the OOM killer and filesystem errors, everything happening before
user-space logging exists.

The buffer is large and the interesting line drowns in it, so it is almost
always piped into grep:

```bash
dmesg | grep -i eth        # interface detection
dmesg | grep -i systemd    # service startup
```
