---
tags: [k8s, networking]
---
The [[deployment]] will create the [[pods]] with the label `app=nginx`
The [[service]] will select pods who who have the same label.
The endpoints will show the pods hit by the service

This link can silently fail, for example, if the endpoint is empty, the service will still respond.

To debug this you can first see what is the label associated with the service :
`kubectl describe service nginx -n demo-app`

And then see what are the pods holding the same label as the service :

`kubectl get pods --show-labels`
