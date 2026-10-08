---
tags: [networking]
---
A service does not serve an address, it binds an **endpoint**: the pair address
plus port, reserved from the kernel.

That pair is a configuration decision written in the service's own file by
somebody, never a property of the machine or the network: `BIND_ADDRESS` in an
`EnvironmentFile`, `listen` in nginx, `ListenAddress` in `sshd_config`.

`0.0.0.0` is not an address but a wildcard for every local address, including
the ones the machine does not have yet, so a new interface or a VPN exposes the
service tomorrow with nothing having changed. It is never the neutral choice.
Binding `127.0.0.1` is the opposite decision, and also why `127.0.1.1` can be
bound although `ip addr` never shows it.

Binding an address the machine does not hold fails at startup with
`EADDRNOTAVAIL`, "Cannot assign requested address", and the service never comes
up. That failure shows in the unit status, not in the traffic, which is what
tells it apart from a service that starts and is merely unreachable.

The listening address and the firewall can close the same port, but the service
owner writes one and the platform writes the other. Which one carries the
restriction decides who must be involved the day the exposure changes.

```bash
ss -ltnp     # which endpoints are bound, by which process
ip addr      # which addresses the machine holds, so which can be bound
```

See [[loopback]], [[nftables]]
