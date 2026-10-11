---
tags: [k8s]
---

A Worker Node can be either a physical, or a virtual machine. It is where the [[pods]] are executed.
Each Worker node has 3 components :

1. [[kubelet]]
It's the principal actor of the Worker Node, it handles the running pods.

2. [[kube-proxy]]
Handle the network rules for the [[service]].

3. [[container-runtime]]
Execute the containers.
