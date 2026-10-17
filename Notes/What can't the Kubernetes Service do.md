---
tags: [k8s]
---

Since the Kubernetes Service is living on the transport layer, there are a few things it can not do :

1. HTTP Routing (Instead, use [[Kubernetes Ingress]])
2. TLS (Instead, use ingress + [[cert-manager]]
3. Security filtering (Instead, use [[Kubernetes NetworkPolicies]]
4. Rate limiting, circuit breaket (Instead, use [[Kubernetes Service Mesh]]

See [[kubernetes]], [[service]], [[difference-between-a-kubernetes-service-and-ingress]]
