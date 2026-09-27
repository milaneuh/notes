`systemd-resolved` is the local resolver daemon on a modern Ubuntu or Debian machine. It sits between the applications and the real DNS servers: it keeps a cache, it chooses which upstream to ask, and it answers questions on a **stub listener** bound to `127.0.0.53`, with a second one on `127.0.0.54`.

Applications reach it two ways. Through [[Name Service Switch]], when `nsswitch.conf` lists the `resolve` module on its `hosts:` line. Or through `/etc/resolv.conf`, for the programs that read that file directly.

## The file it generates

`/etc/resolv.conf` is a symlink, and the target is generated:

```
/etc/resolv.conf -> ../run/systemd/resolve/stub-resolv.conf
nameserver 127.0.0.53
```

So the "nameserver" every program reads is the stub, not a real server. `resolvectl status` reports which mode is in use, and `stub` is this one.

`/run` is a tmpfs, so that file lives in memory and is rebuilt at every boot. Editing it works until the next reboot, or until `resolved` regenerates it, whichever comes first. It is not a place to put a decision.

The **global** setting is `DNS=` in `/etc/systemd/resolved.conf`, or in a drop-in under `/etc/systemd/resolved.conf.d/`.

The **per link** setting comes from whatever configured the interface: the DHCP lease, netplan, or `systemd-networkd`.

**The per link setting wins.** The global `DNS=` is only a fallback for links that have none of their own. So writing `DNS=192.168.104.1` changes nothing on a machine whose `eth0` received a nameserver by DHCP, and `resolvectl status` shows the two levels separately so the contradiction is visible:

```
Current DNS Server: 192.168.104.1      ← global, mine
DNS Servers: 192.168.104.1
Link 2 (eth0)
Current DNS Server: 192.168.104.2      ← from the DHCP lease
DNS Servers: 192.168.104.2
```

To make the choice stick, the per link level is the one to change: set the link's server, or tell the DHCP client to stop accepting a nameserver from the lease, which netplan does with `dhcp4-overrides` and `use-dns: false`.

## Synthetic answers

`resolved` reads `/etc/hosts` and answers stub queries from its content, building a DNS response out of a static file. This is why `dig`, which skips NSS but still reads `resolv.conf`, sees `/etc/hosts` entries anyway: its default interlocutor is the stub.

Three signs that an answer was fabricated locally: the TTL is `0`, which no authoritative server returns; the `aa` flag is set, the stub claiming authority; and `resolvectl query` says it outright, `Data from: synthetic`. The counter proof is to ask a real server with `dig @<address>`, which answers `NXDOMAIN` for a name that only exists in `/etc/hosts`.

## It shares port 53 with another resolver

A machine can run `resolved` and a real DNS server at the same time, on the same port, because a [[listening address]] is the pair address plus port and they bind different addresses:

```
192.168.104.1:53   bind9
127.0.0.1:53       bind9
127.0.0.53:53      systemd-resolved
127.0.0.54:53      systemd-resolved
```

Asking for the wildcard `0.0.0.0:53` would collide with the stub and fail with `EADDRINUSE`.

## Tooling

- `resolvectl status` : the resolv.conf mode, the global servers, and the per link servers, listed separately
- `resolvectl query <name>` : the answer plus where it came from, cache, network or synthetic
- `resolvectl dns <link> <address>` : set a link's server, lost at the next reboot
- `resolvectl flush-caches` : drop the cache, including a cached negative answer
- `dig @127.0.0.53 <name>` : ask the stub on purpose instead of by accident

See [[name resolution]], [[Name Service Switch]], [[listening address]], [[loopback]], [[a name is not an address]]

## Cards
Q: what is `systemd-resolved` and where does it listen?
A: the local resolver daemon. It caches, chooses the upstream, and answers on a stub listener bound to `127.0.0.53`, with a second on `127.0.0.54`.

Q: what does `/etc/resolv.conf` actually point to on a machine running `systemd-resolved` in stub mode?
A: a generated file under `/run/systemd/resolve/`, whose single nameserver is `127.0.0.53`, the stub.

Q: between `DNS=` in `resolved.conf` and the nameserver a link received by DHCP, which one is used?
A: the per link one. The global `DNS=` is only a fallback for links that have no server of their own.

Q: you set `DNS=` in `resolved.conf`, restart the service, and queries still go to the old server. What is happening?
A: the interface has its own nameserver, from the DHCP lease or from netplan, and the per link setting wins. `resolvectl status` shows both levels.

Q: you edit `/etc/resolv.conf` and the change is gone after a reboot. Why?
A: it is a symlink to a file under `/run`, which is a tmpfs rebuilt at boot, and `resolved` regenerates it anyway.

Q: `dig` returns an answer for a name that exists only in `/etc/hosts`. How is that possible?
A: `dig` skips NSS but still reads `resolv.conf`, so it asks the stub, and the stub reads `/etc/hosts` and synthesises a DNS response from it.

Q: three signs that a DNS answer was fabricated locally rather than fetched?
A: a TTL of `0`, the `aa` flag set, and `resolvectl query` reporting `Data from: synthetic`.

Q: can a real DNS server run on the same machine as `systemd-resolved`?
A: yes. They bind different addresses on port 53, and an endpoint is the pair address plus port. Asking for `0.0.0.0:53` would collide and fail with `EADDRINUSE`.

Q: which command tells you where an answer came from, cache or network?
A: `resolvectl query <name>`. Neither `dig` nor `getent hosts` answers that question.
