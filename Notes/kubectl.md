---
tags: [k8s]
---
The CLI client of the Kubernetes API server: every command is a wrapper over
one endpoint of that webservice.

The grammar is always `kubectl <verb> <resource type> [name] [options]`. The
verbs are few, `get`, `create`, `delete`, `describe`, and the resource types
are the nouns of k8s: nodes, pods, deployments.

```bash
kubectl cluster-info    # the cluster and its internal DNS
kubectl get nodes       # the machines in the cluster
```

See [[Kubernetes components]]
