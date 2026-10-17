---
tags: [k8s]
---

There is four main differences :

1. Layer
- The service is living on the transport layer. It is using the TCP/UDP protocols directly.
- The Ingres is living on the application layer. It is using the HTTP/s protocol.

2. Routing
- The service is routing using IP/ports directly.
- The Ingress is routing using the HTTP request path/host/header

3. TLS
- The service does not use [[tls-certificates]]
- The ingress does.

4. Usage
- You are mainly using the service for internal communication or simple exposition
- You are using the ingress for public API or websites.


See [[service]], [[Kubernetes Ingress]]
