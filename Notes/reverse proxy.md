---
tags: [networking]
---
A server that accepts client connections in front of one or several
applications and answers on their behalf, the clients believing they talk to
the application. A forward proxy acts for the **client**, which is configured
to use it; a reverse proxy acts for the **servers**, and clients know nothing
about it.

The **upstream** is the application behind it. The **server block**, a virtual
host elsewhere, is the rule mapping a [[Host header]] to an upstream.

**It always loses the client address.** The proxy terminates the incoming
connection and opens a new one, so the socket peer the upstream sees is the
proxy. This is structural, layer 4 and layer 7 alike, and no setting changes it.
Three techniques recover the original address, each needing cooperation:

- `X-Forwarded-For`, a header the proxy adds. Useless to an application that
  logs its socket peer address instead of reading headers.
- the **PROXY protocol**, a preamble on the TCP stream, which the upstream has
  to parse.
- a **transparent proxy** (`IP_TRANSPARENT`, TPROXY), borrowing the client's
  source address, which needs firewall rules and privileges.

Without one of them the address exists only in the proxy's log, and correlating
two logs is ambiguous for identical concurrent requests.

Which application answered is not visible in the page either: a proxy serving a
file left by another program looks exactly like that program. The answer is in
the response headers, `Server` and whatever signature the application adds.

```bash
nginx -t      # validate before reloading
ss -ltnp      # who really holds the port
```

See [[Host header]], [[Configured state vs running state]]
