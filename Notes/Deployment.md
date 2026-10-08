---
tags: [k8s]
---
The most common controller for running an application. It does not just create
pods: it maintains the replica count, replaces failing pods and pilots
progressive updates.

```bash
kubectl get deployments -A
```

See [[Kubernetes cluster]], [[Pods]]
