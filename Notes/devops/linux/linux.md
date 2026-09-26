Index of the linux notes 

Architecture :
- [[FHS]]

Tooling : 
- [[lsof]] # Retrieve information on opened files
- [[runuser]] # Execute a command as another user
- [[df]] # Retrieve information on available disk space
- [[du]] # Retrieve information on disk usage per directory
- [[ss]] # Retrieve information on network sockets
- [[strace]] # Trace and intercepts syscalls
- [[dmesg]] # Retrieve information regarding the kernel ring buffer
- [[xargs]] # Build command lines from standard input, in batches
- [[find]] # Walk a directory tree and act on what matches

Concepts :
- [[df vs du]] # why the two disagree, and what it tells you
- [[ARG_MAX]] # the kernel cap on an argument list, why xargs batches
- [[Network Layers]] # What are the networks layers and how linux interacts with them
- [[Host header]] # how one address and port can serve several names
- [[reverse proxy]] # what it is, and why it always loses the client address
- [[configured state vs running state]] # validate, reload, then ask the service
