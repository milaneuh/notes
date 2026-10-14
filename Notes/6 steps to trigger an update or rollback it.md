---
tags: [k8s]
---

The CKAD certification test is timed, you'll have to remember quickly how to update or rollback an application.

1. Trigger a rolling update
`kubectl set image deployment/app app=image:v2`

2. Follow the progression
`kubectl rollout status deployment/app`

3. Consult the historic
`kubectl rollout history deployment/app`

4. Rollback
`kubectl rollout undo deployment/app`
or if you want a specific version
`kubectl rollout undo deployment/app --to-revision=2`

5. Verify the Replicas set
`kubectl get rs`
`kubectl describe deployment/app`

6. Common trap
`kubectl scale` does not write a new revision in the history

See [[deployment]], [[replicas-set]]
