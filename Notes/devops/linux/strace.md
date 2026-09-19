strace is a tool for monitoring and diagnosing proccesses in linux. It provides insights on how a program intereacts witht he system, especially when the source code is not available.

Here is a few example that I used during my troubleshooting exercises :

## trace network related system calls and log to file
```bash
strace -e -f trace=network -o /tmp/net_trace.log -p <PID> 
```

## trace the system calls of a specific process
```bash
strace -p <PID>
```

## trace all files opened by a running process 
```bash
sudo strace -f -e openat -s 256 -p $(pgrep myapp) 2>&1 | grep -v "^Process"
```

## watch why a script does before it crashes
```bash
strace -o /tmp/crash_trace.log ./flaky_command && echo "OK" || echo "FAILED"
```

## find slow system calls
```bash
strace -c command_here
```