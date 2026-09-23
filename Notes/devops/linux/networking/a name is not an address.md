To understand sockets or addresses we must assert this : in [[linux]] an address and its name are two separate things.

1. [[name resolution]] : the name becomes an address
2. [[listening address]] : somebody is listening on that address and port
3. [[nftables]] : the packet has the authorization to pass

A literal address is not a name : `127.0.0.1` skips the first layer entirely, and the name returned by `hostname` is only a string in `/etc/hostname` until something decides what it resolves to. So testing by hand with an ip and testing with a name are two different tests, and the one I run is rarely the one the application runs.

When operating a system, before touching anything, you must define which one of these layers must be updated.

## Cards
Q: what are the three layers between a name and a working connection?
A: name resolution turns the name into an address, something has to be listening on that address and port, and the packet has to be allowed through.

Q: `curl 127.0.0.1:8080` answers but the application fails on the same host. What did I not test?
A: the first layer. A literal address skips resolution entirely, so my test and the application's test are not the same test.

Q: where does the machine's own name come from?
A: a string in `/etc/hostname`. It stays a string until something decides what it resolves to.
