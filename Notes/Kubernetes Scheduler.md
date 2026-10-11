---
tags: [k8s]
---

The `kube-scheduler` decides where to deploy each [[pods]]]. It analyses the pod's requirements and then find an adequate [[Kubernetes Worker Nodes]].
This process is in two steps :

1. Filter the inelegible nodes
    A node can be inelegible if :
        - It does not have enough resources
        - The pod can't pass the node's taint
        - The node can't pass the pod's affinity constraints
2. Scoring
    With the remaining nodes, it determines the best candidate through a series of scoring :
        - Based on the load spread
        - Based on the pod's affinity
        - Based on the available resources

3. Assign
    To assign the pod, it is simply going to write in the [[etcd]] database through the [[Kubernetes API Server]]
    ```yaml
    spec:
      nodeName: worker-node-1
    ```
