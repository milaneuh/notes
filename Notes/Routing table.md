---
tags: [networking, linux]
---
Connecting subnets means passing data through a host attached to more than one.
That is all a router is. The kernel tells a local destination from a remote one
with the routing table:

```
$ ip route show
default via 192.168.104.2 dev eth0 proto dhcp src 192.168.104.1 metric 200
192.168.104.0/24 dev eth0 proto kernel scope link src 192.168.104.1 metric 200
```

`via` hands the packet to a gateway; `scope link` means the destination is on
the directly attached network and this host reaches it itself. `dev` is the
interface, `proto` says who installed the route, `src` is the address put in
outgoing packets, `metric` is the weight and the lowest wins.

Without a `default` line the host cannot leave its own subnet, though the local
link still works. With one, and nothing outside answering, the question moves
to the gateway: reachable, and forwarding?

See [[Longest prefix wins]], [[subnet]]
