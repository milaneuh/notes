---
tags: [networking]
---
Also called the internet layer: send and receive packets regardless of the
hardware or the operating system. Its protocol is IP, v4 written as a
dotted-quad `a.b.c.d`, v6 alongside it.

A host holds at least one address per subnet it is attached to, so three
addresses usually means three subnets.

```
$ ip addr show
inet 192.168.104.1/24 ... scope global dynamic eth0
inet6 fe80::5055:55ff:fe8e:6dc6/64 scope link
```

`inet` is v4, `inet6` is v6, and the `/24` names the [[subnet]] the address
belongs to. An interface showing only an `inet6 fe80::` line holds no IPv4
address at all, just a link-local one.

See [[Network layers]], [[Routing table]]
