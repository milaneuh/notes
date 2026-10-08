---
tags: [networking]
---
A connected group of hosts inside a range of addresses: `192.168.2.1` to
`192.168.2.31` is one, so is `192.168.1.1` to `192.168.255.255`.

**CIDR** writes the mask as the count of its leading 1 bits, so
`192.168.104.0/255.255.255.0` becomes `192.168.104.0/24`. An IPv4 address is 32
bits, so a prefix runs `/0` to `/32`; `/16` is `255.255.0.0`, `/26` is
`255.255.255.192`, and a `/24` holds 256 addresses.

A mask is always a run of 1 bits followed by a run of 0 bits, so an octet can
only be 0, 128, 192, 224, 240, 248, 252, 254 or 255. `210` is `11010010`, which
breaks the run, and `255.192.255.0` is not a mask at all.

Two addresses are on the same subnet only if the masked bits match:
`192.168.104.10/24` and `192.168.105.10/24` are not, and need a router.

See [[Routing table]]
