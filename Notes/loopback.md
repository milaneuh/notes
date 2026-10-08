---
tags: [networking, linux]
---
`lo`, `127.0.0.1`: the virtual interface the host uses to talk to itself. A
packet on loopback never reaches the network.

So a service that answers locally and from nowhere else is bound on loopback.
That is the first hypothesis, before the firewall.

See [[Listening address]]
