To understand sockets or addresses we must assert this : in [[linux]] an address and it's name are two separate things.

1. [[name resolution]] : the name becomes an address
2. [[listing address]] : somebody is listening on that address and port
3. [[nftables]] : the packet has the authorization to pass

A literal address is not a name : `127.0.0.1` skips the first layer entirely, and the name returned by `hostname` is only a string in `/etc/hostname` until something decides what it resolves to. So testing by hand with an ip and testing with a name are two different tests, and the one I run is rarely the one the application runs.

When operating a system, before touching anything, you must define which one of these layers must be updated ([[failure signatues]]).

See also : 
- [[translating is not filtering]]
