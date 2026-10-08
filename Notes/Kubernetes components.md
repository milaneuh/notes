---
tags: [k8s]
---
![[Pasted image 20260915161050.png]]

**Control plane**, managing the overall state of the cluster:

- `kube-apiserver`: exposes the Kubernetes HTTP API, the core component
  everything else talks through
- `etcd`: the key-value store behind the api server, so the cluster state
- `kube-scheduler`: finds pods not yet bound to a node and assigns them
- `kube-controller-manager`: runs the controllers implementing the API's
  behaviour
- `cloud-controller-manager`: integrates with the cloud provider, optional and
  absent on bare metal

**On every node**:

- `kubelet`: checks that the pods and their containers are running
- `kube-proxy`: maintains the network rules implementing [[Service|Services]],
  optional because a network plugin can do it instead
- a container runtime: runs the containers

**Addons**: DNS for cluster-wide resolution, the Web UI dashboard, container
resource monitoring, cluster level logging to a central store.

See [[Kubernetes]]
