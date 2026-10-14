---
tags: [k8s]
---
A Replicas Set define required the number of pods to be running, if any pods shutdown, the replicas set will restart it automatically.
Usually, you are not creating the Replicas Set by hand, the [[deployment]] will do it.

It has three roles :

1. Watch the pods under it's label selector
2. Count the number of running pods
3. Create, or Delete pods until it reach the desired replicas number

It has three main components :

1. `replicas` the number of pods to maintain
2. `selector` the label selector
3. `template` the pods template to create

See [[deployment]],[[pods]],[[kubernetes]]
