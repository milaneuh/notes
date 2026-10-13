---
tags: [k8s]
---
The pods phase attribute defines which state the pod currently is in. There is 5 phases :

1. Pending, the pod has been created but is not yet assigned to a node
2. Running, the pod is assigned and at least one container is running
3. Succeeded, all of the pod's containers have exited successfully (code 0)
4. Failed, at least one container exited in error
5. Unknown, undetermined state, usually because it is unreachable

See [[kubernetes]], [[pods]]
