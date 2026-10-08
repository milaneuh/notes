---
tags: [k8s]
---
Master nodes coordinate, worker nodes run the load, and either kind can be a VM
or a physical machine. The control plane is not in the traffic path: it decides
and observes.

![[cluster-demo.png]]

A [[Deployment]] creates and maintains the pods, a [[Service]] routes traffic
to them. Delete a pod and the Deployment, seeing 2 of its 3 replicas, creates a
replacement with a new random suffix and a new IP, never the old name again.
That is why you talk to the Service and not to a pod.

A namespace is a naming scope, not a machine boundary: a Deployment, its pods
and its Service living in `demo` still run on whatever worker nodes the
scheduler picked.

See [[Kubernetes components]]
