---
tags: [linux, tooling]
---
Shows the system calls a process makes, which is the instrument for when the
source is unavailable and the logs say nothing.

```bash
strace -p <PID>                                      # attach
strace -f -e trace=network -o /tmp/net.log -p <PID>  # one family, to a file
strace -f -e openat -s 256 -p $(pgrep myapp)         # which files it opens
strace -c command                                    # summary, not a stream
```

`-c` counts calls and time spent per system call, which is how you find the
slow one instead of reading the whole trace.

Tracing a service at rest produces noise, not symptoms: a poll sitting in
timeout looks like a problem to someone who came without a hypothesis.
