
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

You can also add other software on each nodes such as systemctl for example. 

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
