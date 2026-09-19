Open source platform to manage containerized workloads. 

Kubernetes is built on top of [[linux]] and relies on linux API for it's basic functionalities, such as [[disk vs filesystem|filesystem]], networking and storage. In short, k8s provide a standard and consistent interface for managing linux based infrastructures. 

It is not necessarily creating new concepts or technologies, but more so connecting already existing concepts together to facilitate the exploitation of the infrastructure.

It is recommended to learn the linux fundamentals before learning Kubernetes because it will make debugging and understanding the concepts much easier.  
## The problems k8s answers 
> 50% of infrastructure cost is plumbing

[[Containers]] are a good way to bundle and run applications, however the management of these containers is still a manuel process. For example, if a container goes down, you have to manually restart it. 

K8s allows you to automate theses things and provides a framework to facilitate the managements of a containerized workloads. 
This framework provide :

- [[Service Discovery]] and [[Load Balancing]] 
- [[Storage Orchestration]]
- [[Automated Rollouts]] and [[Automated Rollbacks]]
- [[Automated Bin Packing]]
- [[Self-Healing]]
- [[Secrets Management]] and [[Configuration Management]]
- [[Batch Execution]]
- [[Horizontal Scaling]]
- [[IPv6/IPv4 Dual Stack]]
- [[Extendibility]]
 
See [[Origins of Kubernetes]], [[Pods]], [[Kubernetes Components]]

## Cards
Q: what problem does Kubernetes answer?
A: containers bundle and run applications well, but managing them stays manual — if a container goes down you restart it yourself. k8s automates that and gives a framework for managing containerized workloads.

Q: name the capabilities the Kubernetes framework provides.
A: service discovery and load balancing, storage orchestration, automated rollouts and rollbacks, automated bin packing, self-healing, secrets and configuration management, batch execution, horizontal scaling, IPv6/IPv4 dual stack, extendibility.


