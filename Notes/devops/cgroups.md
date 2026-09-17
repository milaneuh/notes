Control groups are a [[linux]] kernel feature that **limits, accounts and prioritises** the ressources (cpu, memory, io) a group of processes can consume.

> Do not confuse cgroups with [[namespaces]] : namespaces decide **what a process can see** (isolation), cgroups decide **how much it can use** (limitation).

## The problem control groups answers
In a traditional operating system, if an application gets a bug and starts infinite looping, it can consume 100% of the cpu and freeze the entire machines.

Control Groups allows us to limit the ressource a Control Group can access, so one faulty process cannot starve the rest of the system.

## What happens when a limit is exceeded
It depends on the ressource :
- **memory** : the process is killed by the OOM killer (in [[Kubernetes]], `OOMKilled`).
- **cpu** : the process is **throttled**, not killed. It simply gets fewer cpu cycles per period and runs slower.

---
While powerful, managing control groups manually means writing raw numbers and process ids directly into the hidden system files under `/sys/fs/cgroup/`. It is tedious, complex and hard to maintain.

This is one of the problems [[Docker]] solves : through the docker api you configure the boundaries of the [[Containers|container]] and the Docker runtime handles the creation of the cgroups and namespaces for you.
