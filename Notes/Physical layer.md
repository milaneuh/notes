---
tags: [networking]
---
On ethernet, every device has a MAC address and all data travels in frames
carrying the sender's and the receiver's MAC. Two ethernet networks need a
bridge to talk.

Since the network layer has to work over any medium, the kernel provides the
liaison: a **network interface** links the IP settings to the hardware,
`eth0`, `wlan0`.

```
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 ...
```

The leading `2` is the ifindex, readable at `/sys/class/net/eth0/ifindex`.
`UP` is administrative, somebody ran `ip link set eth0 up`. `LOWER_UP` is
carrier, the driver sees a cable. `UP` with `NO-CARRIER` and no `LOWER_UP` is a
configured interface with no physical link, and an interface without `UP` at
all means nobody brought it up, which is the thing to fix before suspecting
addresses, routes or names.

See [[Network layers]]
