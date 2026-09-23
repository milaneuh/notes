A service does not serve an address, it binds to an endpoint : the couple of an address and a port. The process asks the kernel to reserve it, and the kernel grants it or refuses it. The listening address is therefore a configuration decision, written in a file by someone, not a property of the machine nor of the network. It always comes from the service's own configuration and never from the system : `BIND_ADDRESS` in an `EnvironmentFile`, `listen` in nginx, `ListenAddress` in `sshd_config`.

`0.0.0.0` is not an address, it is a wildcard for every local address, including the ones the machine does not have yet. A new interface or a VPN coming up tomorrow exposes the service without anything having been changed, so it is never a neutral choice. Binding `127.0.0.1` is the opposite decision : the service is reachable through [[loopback]] only, which also explains why `127.0.1.1` can be bound even though `ip addr` never displays it.

Because it is an exposure decision, the real question is who owns it. The listening address and the firewall can both close the same port, but they are written by different people : the service owner writes the first, the platform writes the second. Choosing one over the other decides who has to be involved the day the exposure has to change, and that is the part worth arguing about in a design review.

A process can only bind to an address the machine already holds. Asking for a non local address fails at startup with `EADDRNOTAVAIL` ("Cannot assign requested address") and the service never comes up at all. That failure shows in the unit status, not in the traffic, which is what tells it apart from a service that starts and is simply unreachable.

## Tooling

- `ss -ltnp` : which endpoints are bound, and by which PID
- `ip addr` : which addresses the machine holds, so which ones can be bound

## Cards
Q: what does a service actually bind to?
A: an endpoint, the couple address plus port, reserved from the kernel. Never an address alone.

Q: where is the listening address decided?
A: in the service's own configuration, written in a file by someone. It is not a property of the machine nor of the network.

Q: why is `0.0.0.0` never a neutral choice?
A: it is a wildcard for every local address, including the ones the machine does not have yet. A new interface or a VPN exposes the service without anything having been changed.

Q: a service asks to bind an address the machine does not hold. What happens?
A: it fails at startup with `EADDRNOTAVAIL`, "Cannot assign requested address". The failure shows in the unit status, not in the traffic.

Q: the listening address and the firewall can both close the same port. What is the real difference?
A: who owns the decision. The service owner writes the first, the platform writes the second, and that decides who has to be involved the day the exposure changes.
