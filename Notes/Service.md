---
tags: [k8s]
---
A stable access point to a group of pods. Pods are ephemeral and come back with
a new IP, so you do not contact them directly: the Service's ClusterIP is
stable for its whole life and keeps tracking its pods by label.

`ClusterIP` is the default and only answers inside the cluster; `LoadBalancer`
gets a dedicated address reachable from outside.

```bash
kubectl get services -A
```

See [[Kubernetes cluster]], [[Pods]]
