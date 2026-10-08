---
tags: [networking]
---
A client opening `http://api.catalog.lab/items` resolves the name, then
connects to the address on port 80. At that point resolution has done its job
and the name is no longer needed to reach the machine. The name comes back
*inside* the request:

```
> GET /items HTTP/1.1
> Host: api.catalog.lab
```

The client copies whatever URL it was handed, so calling a server by address
puts the address in the header.

This is what makes **name based virtual hosting** possible: one endpoint serves
many names, because every request announces which name was asked for, and a
[[reverse proxy]] is the program whose job is to sort on it. A request with no
`Host`, or an unknown one, falls back to the default virtual host, where
serving something unintended leaks information.

Two layers are at work and are not interchangeable. Address and port belong to
the network and transport layers; the `Host` header is application layer,
inside the request. A TCP relay that never parses HTTP never sees the name, so
it cannot route by name.

```bash
curl -v <url>                              # > sent, < received, * curl talking
curl -H 'Host: <name>' http://<address>/   # test a vhost without touching DNS
```

See [[a name is not an address]], [[Network layers]]
