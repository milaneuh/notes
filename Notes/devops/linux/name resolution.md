The linux name resolution converts human-readable hostsname into ip addresses using a modular stack. It uses [[Name Service Switch]] (`/etc/nsswitch.conf`) to check local files, it queries DNS servers through `/etc/resolv.conf` or `systemd-resolved` and uses tooling such as `dig` for diagnostic. 

Two things matter more than the stack itself. The order is declared, not universal : the `hosts:` line of `/etc/nsswitch.conf` decides whether files come before dns, so I read that line instead of assuming it. And the usual diagnostic tools do not follow that order. `dig` and `nslookup` query a DNS server directly and ignore `/etc/hosts`, so they can answer correctly while the application keeps failing. `getent hosts <name>` follows the same chain as the application, which makes it the only honest test.

A failed resolution is not always immediate either. An unreachable DNS server makes it hang for several seconds, so a slow failure does not point at a firewall by itself ([[failure signatues]]).

## Configuration files

- `/etc/hosts` : Static local ip-to-hostname mapping checked first by the system
- `/etc/nsswitch.conf` : Defines the lookup order for hostnames
- `/etc/resolv.conf` : Points the system to upstream DNS name servers (usually through a [[symlinks]])

## Tooling
- `getent hosts` : Resolves a name through the same chain as the application
- `resolvectl` : Manages and diagnoses `systemd-resolved` caches and statuses 
- `dig` : Queries DNS names servers directly to test records.
