The driver message (dmesg) command in linux allows us to examine the [[kernel ring buffer]], and print the message buffer of the kernel. It is useful when the system encounters any problem during its start-up, so by reading the content of dmesg command you can find out where the problem occurred. 

Since the output of dmesg is _very_ large it is recommended to use grep with it.

## check network interface detection 
```bash
dmesg | grep -i eth
```

## check service startup
```bash
dmesg | grep -i systemd
```

## Cards
Q: what does dmesg read?
A: the [[kernel ring buffer]], the kernel's own message buffer.

Q: when is dmesg the right instrument?
A: hardware, drivers, the OOM killer, filesystem errors, and anything that happens before user-space logging starts.

Q: why is a grep almost always needed with it?
A: the buffer is very large, so the interesting line is drowned.
