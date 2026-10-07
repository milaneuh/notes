See [[Kubernetes Cluster]], [[Pods]]
## Cards

Q: What is a Kubernetes Service and what is it's role ? 
A: A Kubernets Service is an access point to a group of [[Pods]]. Since Pods are ephemeral (and get recreated with a new IP) you do not contact them directly, you instead use a Service as an access point.

Q: How do you list all Kubernetes Services ? 
A: kubectl get services -A 

Q: What are the main types of Kubernetes Services ?
A: ClusterIP (default) is only accessible from inside the cluster. The other one is LoadBalancer, accessible from the outside with a dedicated address

