---
tags: [networking, linux]
---
Three layers sit between a name and a working connection:

1. [[Name resolution]] turns the name into an address.
2. Something is [[Listening address|listening]] on that address and port.
3. [[nftables|The packet is allowed through]].

Before touching anything, decide which of the three you are changing. And note
that testing with a literal address skips the first layer entirely, so
`curl 127.0.0.1:8080` is not the test the application runs. `hostname` is only
a string in `/etc/hostname` until something decides what it resolves to.
