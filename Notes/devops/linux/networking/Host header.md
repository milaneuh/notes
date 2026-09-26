A client that opens `http://api.catalog.lab/items` does two separate things. It resolves the name into an address, and it opens a TCP connection to that address on the port the URL scheme implies, 80 for `http://`. At that moment the [[name resolution]] has finished its job and the name is no longer needed to reach the machine.

The name comes back inside the request. HTTP/1.1 carries it in the `Host` header, and the client fills that header from the URL it was handed:

```
> GET /items HTTP/1.1
> Host: api.catalog.lab
```

Observed on `lab2`, asking an application by address instead of by name. The client copies whatever it was given, so the address ends up in the header:

```
$ curl -v http://192.168.104.3:8081/items
> GET /items HTTP/1.1
> Host: 192.168.104.3:8081
```

This is what makes **name based virtual hosting** possible. A single endpoint, one address and one port, serves many names, because every request announces which name was asked for. Three names resolving to the same address tell the client nothing about which application should answer, and the sorting is done by the server that reads the header. A [[reverse proxy]] is the program whose job that is.

The `Host` header is the only information that decision rests on. A request carrying no `Host`, or one naming something the server does not know, cannot be routed by name, and the server falls back to whatever it declared as its default virtual host. Serving something unintended there is a way to leak information.

Two layers are at work and they are not interchangeable. The address and the port of the connection belong to the network and transport layers. The `Host` header lives in the application layer, inside the request itself. A device that only looks at the connection never sees the name, which is why a TCP relay cannot route by name.

*À compléter : ce que je croyais avant de comprendre ça.*

## Tooling

- `curl -v <url>` : `>` lines are what the client sends, `<` lines are what the server answers, `*` lines are curl commenting
- `curl -H 'Host: <name>' http://<address>/` : test a virtual host by forging the header, without touching DNS

See [[a name is not an address]], [[reverse proxy]], [[name resolution]], [[Network Layers]]

## Cards
Q: what does the `Host` header carry, and where does the client get it from?
A: the name that was asked for, copied from the URL the client was given.

Q: what makes it possible for one address and one port to serve several names?
A: every HTTP request announces the requested name in its `Host` header, so the server can sort on it.

Q: which layer does the `Host` header belong to, and which layer carries the address and port?
A: the header is application layer, inside the request. The address and port are network and transport layer, in the connection.

Q: you call a server by its IP address instead of its name. What does the `Host` header contain?
A: the address, because the client copies whatever was in the URL.

Q: a TCP relay forwards bytes between two sockets. Can it route requests by name?
A: no. The name is inside the HTTP request, and a relay that never parses HTTP never sees it.

Q: three names resolve to the same address, and a request arrives with no `Host` header. What happens?
A: it cannot be routed by name, so the server hands it to its default virtual host, whatever that serves.
