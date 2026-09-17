Pods are the smallest deployable unit of computing you can deploy in [[Kubernetes]]

## The [[linux|Linux]] apis wrapped by Pods
- [[namespaces]]
Namespaces are what make a Pod a Pod. Containers inside the same Pod **share** the network, IPC and UTS namespaces : they see the same IP address and can talk to each other over `localhost`. They keep **separate** mount and PID namespaces, so each container still has its own filesystem and its own process tree.

- [[cgroups]]
Control groups limit and account the ressources (cpu, memory, io) the Pod and its containers are allowed to consume.
