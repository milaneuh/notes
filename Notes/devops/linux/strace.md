strace is a tool for monitoring and diagnosing processes in linux. It provides insights on how a program interacts with the system, especially when the source code is not available.

Here are a few examples that I used during my troubleshooting exercises :

## trace network related system calls and log to file
```bash
strace -f -e trace=network -o /tmp/net_trace.log -p <PID>
```

## trace the system calls of a specific process
```bash
strace -p <PID>
```

## trace all files opened by a running process 
```bash
sudo strace -f -e openat -s 256 -p $(pgrep myapp) 2>&1 | grep -v "^Process"
```

## watch what a script does before it crashes
```bash
strace -o /tmp/crash_trace.log ./flaky_command && echo "OK" || echo "FAILED"
```

## find slow system calls
```bash
strace -c command_here
```

## Cards
Q: what does strace show?
A: the system calls a process makes, which is useful when the source is not available and the logs say nothing.

Q: which invocation gives a summary instead of a stream?
A: `strace -c`, which counts the calls and the time spent per system call.

Q: what is the risk of running strace on a service at rest?
A: reading normal idle behaviour, a poll in timeout for instance, as a symptom. Without a hypothesis the instrument only produces noise.
