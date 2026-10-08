---
tags: [k8s]
---
An open source platform to manage containerized workloads, built on top of
linux and relying on linux APIs for filesystem, networking and storage. It does
not invent many concepts, it connects existing ones into a standard interface
over linux infrastructure, which is why learning the linux fundamentals first
makes debugging much easier.

The problem it answers: containers bundle and run an application well, but
managing them stays manual, and if one goes down somebody restarts it.
*50% of infrastructure cost is plumbing.*

What the framework provides: service discovery and load balancing, storage
orchestration, automated rollouts and rollbacks, bin packing, self-healing,
secrets and configuration management, batch execution, horizontal scaling,
IPv6/IPv4 dual stack, extendibility.

It started as Borg, Google's internal tool for clusters of micro-services, open
sourced in 2013 with the linux foundation. Docker Swarm and Mesos were the
alternatives.

See [[Kubernetes cluster]], [[Kubernetes components]], [[Pods]]
