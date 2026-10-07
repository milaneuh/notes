![700](https://kubernetesbootcamp.github.io/kubernetes-bootcamp/public/images/module_01_cluster.svg)

A typical k8s cluster consists of : 

1. The _master node(s)_, coordinates everything happening inside the cluster.
2. The _worker node(s)_ just like master nodes they can be either VM or physical machines, they are used as worker machines inside the cluster  
See [[Kubernetes]]

## Cards

Q: In this cluster, what guarantees that 3 `web` pods exist, and what sends traffic to them ?
![[cluster-demo.png]]
A: The `Deployment: web` (replicas: 3) creates and maintains the pods. The `Service: web` (ClusterIP) routes traffic to them. The control plane is not in the traffic path, it only decides and observes the cluster state.

Q: In this cluster, the pod `web-abc12` is deleted. What happens, and what is the name of the new pod ?
![[cluster-demo.png]]
A: The Deployment notices it only has 2 of its 3 replicas and creates a new pod. The name is new (random suffix), never `web-abc12` again, and so is the IP. That is why you talk to the Service and not to a pod.

Q: In this cluster, does the Service address change when the pods are replaced ?
![[cluster-demo.png]]
A: No. The ClusterIP of `web` is stable for the life of the Service. Only the pods behind it change, the Service keeps tracking them by label.

Q: What does `Namespace: demo` on the worker nodes mean in this schema ?
![[cluster-demo.png]]
A: The Deployment, the pods and the Service all live in the `demo` namespace. It's a naming scope, not a machine boundary. The pods still run on whatever worker nodes the scheduler picked.
