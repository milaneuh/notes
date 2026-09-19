The driver message (dmesg) command in linux allows us to examine the [[kernel ring buffer]], and print the message buffer of the kernel. It is useful when the system encounters any problem during it's start-up, so by reading the content of dmesg command you can find out wehre the problem occurred. 

Since the output of dmesg is _very_ large it is recommended to use grep with it.

## check network interface detection 
```bash
dmesg | grep -i eth
```

## check servuce startup
```bash
dmesg | grep -i systemd
```