---
tags: [k8s]
---

There is multiple CNI (Container Network Interface) plugins available in kubernetes, the main ones are :

- Calico
[[Border Gateway Procotol]] based plugin, with full [[Network Policies]] support.

- Cilium
[[Extended Berkeley Packet Filter|ePBF]] based plugin, with full [[Network Policies]] support, native observability and greater performacne

- kindnet
minimal and configless, comes with Kind and great for learning purposes
