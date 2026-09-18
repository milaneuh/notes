
![[Pasted image 20260915161050.png]]
⬆︎ This is the components of a [[Kubernetes]] cluster. 

## [[Control Plane]] components : 
Manage the overall state of the cluster

- [[kube-apiserver]] 
The core component server that exposes the Kubernetes HTTP API.

- [[etcd]]
KV store for api server data

- [[kube-scheduler]]
Explore for unassigned [[Pods|pods]] not yet bounded to a [[Nodes|node]] and assign them. 

- [[kube-controller-manager]]
runs [[Controllers|controllers]] to implement the k8s api behaviour

- [[cloud-controller-manager]] (optional)
- integrates with underlying cloud providers

## [[Nodes|Node]] components :
Runs on every [[Nodes]], maintaining running [[Pods]] and providing runtime environment 

- [[kubelet]]
Check if pods are running, including the underlying containers

- [[kube-proxy]] (optional)
Maintains network rules on nodes to implements [[Services]]

- [[Container Runtime]]
Software responsible for running [[Containers]] 

You can also add other software on each nodes, such as systemd for example. 

## Addons
Addons can extends the features of k8s. The most importants includes :

- [[DNS]]
For cluster-wide DNS resolution

- [[Web UI]] (Dashboard)
For cluster management interface

- [[Container Ressource Monitoring]]
For collecting and storing container metrics. 

- [[Cluster Level Logging]]
For saving container logs to a central log store

## Cards
Q: which components make up the Kubernetes control plane?
A: kube-apiserver, etcd, kube-scheduler, kube-controller-manager, and optionally cloud-controller-manager.

Q: which Kubernetes components run on every node?
A: the kubelet, kube-proxy (optional) and a container runtime.

Q: what does kube-apiserver do?
A: it is the core component server that exposes the Kubernetes HTTP API.

Q: what does etcd store?
A: it is the key-value store holding the api server data, so the state of the cluster.

Q: what does kube-scheduler do?
A: it looks for unassigned pods, not yet bound to a node, and assigns them to one.

Q: what does kube-controller-manager do?
A: it runs the controllers that implement the behaviour of the Kubernetes api.

Q: what does the kubelet do?
A: it checks that the pods are running, including their underlying containers.

Q: what does kube-proxy do, and why is it listed as optional?
A: it maintains the network rules on nodes to implement Services. It is optional because a network plugin can provide the same behaviour itself.

Q: what is the container runtime responsible for?
A: running the containers.

Q: what is the role of the cloud-controller-manager?
A: integrating with the underlying cloud provider. It is optional and absent on a cluster that runs on bare metal.

Q: what are the main Kubernetes addons?
A: DNS for cluster-wide resolution, the Web UI dashboard, container resource monitoring, and cluster level logging.
