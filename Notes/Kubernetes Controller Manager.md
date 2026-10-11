---
tags: [k8s]
---
The `kube-controller-manager` reconcile the [[kubernetes-components]] together. It is constantly comparing the expected state and the running state.
It is constantly in a permanent loop through three stages :

1. Watch
Assert the currently running state in the [[Kubernetes API Server]].
2. Compare
Compare the running state with the expected state stored in [[etcd]].

3. Act
Correct the discrepancie between the two states.
