---
tags: [k8s]
---
In [[kubernetes]], regardless of the network plugin used there is three rules that always apply :

1. Every [[pods]] gets it's own IP address.
2. A pod can communicate freely with other pods in it's namespace.
3. The services have a static ip address.
