A reverse proxy is a server that accepts client connections in front of one or several applications and answers on their behalf. The clients believe they are talking to the application.

The two families of proxy are told apart by the side they work for. A forward proxy acts for the **client**, which is configured to go through it. A reverse proxy acts for the **servers**, and the clients know nothing about it. That is where the word reverse comes from.

Three terms come with it. The **upstream**, or backend, is the application sitting behind the proxy. The **server block**, called a virtual host in other products, is the rule that says which [[Host header]] goes to which upstream. And the decision itself rests on that header alone.

## It always loses the client address

A reverse proxy accepts the incoming connection, then opens a **new** connection towards the upstream. There are two TCP connections, and the socket peer address the upstream sees is the proxy.

This is structural. Any proxy that terminates a connection and opens another one does it, whether it parses the application protocol or only relays bytes. No configuration setting changes that on its own.

Three techniques recover the original address, and all three need cooperation from somewhere.

`X-Forwarded-For` is a header the proxy adds, naming the client that connected to it. It works only if the application reads headers for that purpose. An application that logs its socket peer address never sees it, and the header arrives for nobody.

The **PROXY protocol**, invented by HAProxy and supported by nginx, prefixes the TCP stream with a small preamble declaring the original address. The upstream has to know how to parse it.

The **transparent proxy**, with `IP_TRANSPARENT` and TPROXY, makes the proxy borrow the client's source address. It needs firewall rules and privileges.

When none of the three is available, the original address exists only in the proxy's own log, and recovering it means correlating two logs on the fields both sides already write. That correlation becomes ambiguous for identical requests arriving concurrently, since nothing in the shared fields distinguishes them.

## Which application answered

The page returned says nothing about which server sent it. A proxy serving a file left behind by another program looks exactly like that program. The answer is in the response headers, `Server` and any signature the application adds itself.

*À compléter : le jour où j'ai cru qu'apache tournait encore.*

## Tooling

- `curl -v <url>` : the `<` lines carry `Server` and the application's own signature headers
- `nginx -t` : validate the configuration before reloading it
- `ss -ltnp` : which process actually holds the port the proxy is supposed to own

See [[Host header]], [[listening address]], [[configured state vs running state]], [[nftables]]

## Cards
Q: what distinguishes a forward proxy from a reverse proxy?
A: the side it works for. A forward proxy acts for the client, which is configured to use it. A reverse proxy acts for the servers, and clients do not know it is there.

Q: what is an upstream?
A: the application sitting behind the proxy, the destination a server block forwards to.

Q: why does an upstream see the proxy's address instead of the client's?
A: the proxy terminates the incoming connection and opens a new one. The socket peer of the second connection is the proxy.

Q: which proxies lose the original source address?
A: every proxy that terminates a connection and opens another, layer 4 and layer 7 alike. It is structural, not a setting.

Q: you set `X-Forwarded-For` on the proxy and the application still logs the proxy's address. Why?
A: the application reads its socket peer address, which is not an HTTP header. Setting a header only helps an application that reads that header.

Q: the three ways to recover the original client address, and what each one requires?
A: `X-Forwarded-For`, which the application must read. PROXY protocol, which the upstream must parse. Transparent proxying, which needs firewall rules and privileges.

Q: a page comes back looking like it came from another web server entirely. How do you find out who really answered?
A: the response headers. `Server`, plus whatever signature the application adds. The body proves nothing.
