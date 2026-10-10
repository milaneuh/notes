When the [[deployment]] stays stuck at step 0/1, it usually means that the [[pods|pod]] is not ready.
That means you have to check the pod's event and assert why it is not ready yet.

```
# Describe the stuck deployement
kubectl describe deployment nginx -n demo-app
# Get the pods event of the namespace
kubectl get events -n demo-app
```
