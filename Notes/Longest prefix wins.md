---
tags: [networking, linux]
---
When two routes match, the kernel takes the more specific one:
`192.168.104.0/24` beats `192.168.0.0/16` for `192.168.104.50`.

The default route is `0.0.0.0/0`, a prefix of length zero. It matches every
destination and loses against anything else that matches, which is why traffic
only goes to the gateway when nothing more specific was found.

See [[Routing table]]
