---
tags: [networking, linux]
---
The application calls into the shared library, which follows the rules in
`/etc/nsswitch.conf` to decide what to ask, consults `/etc/resolv.conf` for a
DNS server when it gets there, and returns the address.

- `/etc/hosts`: the static local mapping
- `/etc/nsswitch.conf`: the lookup order, see [[Name Service Switch]]
- `/etc/resolv.conf`: the upstream servers, usually a symlink

`getent hosts <name>` is the only honest test, because it follows that same
chain. `dig` and `nslookup` query a DNS server directly and ignore NSS, so they
can answer correctly while the application keeps failing.

A resolution that hangs several seconds before failing points at an unreachable
DNS server. Slowness is not by itself the signature of a firewall.

See [[systemd-resolved]], [[a name is not an address]]
