---
tags: [networking, linux]
---
The local resolver daemon on a modern Debian or Ubuntu. It caches, picks the
upstream, and answers on a stub listener bound to `127.0.0.53`, with a second
on `127.0.0.54`. Applications reach it through the `resolve` module in
[[Name Service Switch]], or through `/etc/resolv.conf`.

That file is a symlink to a generated one under `/run`, holding
`nameserver 127.0.0.53`. Since `/run` is a tmpfs, editing it lasts until the
next reboot or the next regeneration, so it is not a place to put a decision.

**The per-link DNS server wins.** `DNS=` in `/etc/systemd/resolved.conf` is only
a fallback for links that have none of their own, so it changes nothing on a
machine whose `eth0` got a nameserver by DHCP. `resolvectl status` shows the two
levels separately. To make the choice stick, set the link's server or stop the
DHCP client from accepting one (`dhcp4-overrides`, `use-dns: false` in netplan).

resolved also synthesises answers out of `/etc/hosts`, which is why `dig`,
skipping NSS but still reading `resolv.conf`, sees those entries: its
interlocutor is the stub. Three signs an answer was fabricated locally: a TTL
of `0`, the `aa` flag set, and `resolvectl query` saying `Data from: synthetic`.
The counter-proof is `dig @<real server>`, which returns `NXDOMAIN`.

It shares port 53 with a real DNS server by binding different addresses, since
an endpoint is address plus port. Asking for `0.0.0.0:53` would collide with the
stub and fail with `EADDRINUSE`.

```bash
resolvectl status          # mode, global servers, per-link servers
resolvectl query <name>    # the answer and where it came from
resolvectl flush-caches    # including a cached negative answer
```

See [[Name resolution]], [[Listening address]]
