---
tags: [linux, containers]
---
Control groups limit, account and prioritise the resources (cpu, memory, io) a
group of processes may consume. Not to be confused with namespaces: namespaces
decide what a process can **see**, cgroups how much it can **use**.

The problem they answer: on a traditional system, an application that starts
looping takes 100% of the cpu and freezes the machine. A cgroup is the boundary
that stops one faulty process from starving the rest.

What happens at the limit depends on the resource. Memory: the process is
killed by the OOM killer, `OOMKilled` in Kubernetes. CPU: it is throttled, not
killed, and simply gets fewer cycles per period.

Managing them by hand means writing raw numbers and process ids into
`/sys/fs/cgroup/`, which is why a container runtime does it for you. Worth
noting that Docker's own contribution was the layered image format and its
distribution through a registry; the cgroup and namespace setup was originally
delegated to LXC.

See [[Pods]]
