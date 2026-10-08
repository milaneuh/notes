---
tags: [k8s, linux]
---
The smallest deployable unit in Kubernetes: you never deploy a container on its
own, the Pod is what the scheduler places and the kubelet watches.

It is a Pod because of the linux namespaces it wraps. Containers inside one
**share** the network, IPC and UTS namespaces, so they see the same IP and talk
over `localhost`, and keep **separate** mount and PID namespaces, so each has
its own filesystem and process tree.

Its [[cgroups]] limit and account the resources (cpu, memory, io) the Pod and
its containers may consume.

See [[Kubernetes]], [[Kubernetes cluster]]
