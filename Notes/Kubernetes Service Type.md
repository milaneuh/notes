---
tags: [k8s]
---

There is four types of service you can create in K8s :

1. ClusterIP (default)

The service is only accessible from inside the cluster, it is usually what you would go after since you often do not want a service accessible from outside the cluster.

2. NodePort
The service is accessible through a port on each cluster's node. It is most often used when you do not use a cloud provider, or for local environment tests.

3. LoadBalancer
Bind the service to an external cloud provider for load balancing.

4. ExternalName
This type is a bit different from the three others. It does not bind to any pods nor does it do proxying. It is simply redirecting to an external DNS name.

See [[kubernetes]], [[service]]
