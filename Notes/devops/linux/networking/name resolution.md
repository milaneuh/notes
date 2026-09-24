The linux name resolution converts human-readable hostnames into ip addresses using a modular stack. It uses [[Name Service Switch]] (`/etc/nsswitch.conf`) to check local files, it queries DNS servers through `/etc/resolv.conf` or `systemd-resolved` and uses tooling such as `dig` for diagnostics. 

Two things matter more than the stack itself. The order is declared, not universal : the `hosts:` line of `/etc/nsswitch.conf` decides whether files come before DNS, so I read that line instead of assuming it. And the usual diagnostic tools do not follow that order. `dig` and `nslookup` query a DNS server directly and ignore `/etc/hosts`, so they can answer correctly while the application keeps failing. `getent hosts <name>` follows the same chain as the application, which makes it the only honest test.

A failed resolution is not always immediate either. An unreachable DNS server makes it hang for several seconds, so a slow failure does not point at a firewall by itself.

The resolution process typically unfolds like this (simplified):
1. The application calls a function to look up the ip address behind a hostname. This function is in the system's shared library, so the application does not need to know the details of how it works. 
2. When the function in the shared library runs, it acts according to a set of rules found in the [[Name Service Switch]] to determine a plan of action on lookups. 
3. When the function decides to use DNS for the name lookup, it consults an additional configuration file to find a DNS name server. the name server is given as an IP address. 
4. The function sends a DNS lookup request (over the network) to the name server.
5. The name server replies with the IP address for the hostname and the function returns this IP address to the applications. 
## Configuration files

- `/etc/hosts` : Static local ip-to-hostname mapping checked first by the system
- `/etc/nsswitch.conf` : Defines the lookup order for hostnames
- `/etc/resolv.conf` : Points the system to upstream DNS name servers (usually through a [[symlinks|symlink]])

## Tooling
- `getent hosts` : Resolves a name through the same chain as the application
- `resolvectl` : Manages and diagnoses `systemd-resolved` caches and statuses 
- `dig` : Queries DNS name servers directly to test records.

## Cards
Q: which file decides whether `/etc/hosts` is consulted before DNS?
A: the `hosts:` line of `/etc/nsswitch.conf`. The order is declared there, it is not universal.

Q: why can `dig` answer correctly while the application keeps failing to resolve the same name?
A: `dig` and `nslookup` query a DNS server directly and ignore the NSS chain, so they never read `/etc/hosts`.

Q: which command resolves a name the way the application does?
A: `getent hosts <name>`, because it follows the same chain.

Q: a resolution that hangs several seconds before failing, what does it suggest?
A: an unreachable DNS server. A slow failure is not by itself the signature of a firewall.
