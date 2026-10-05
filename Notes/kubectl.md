## Cards
Q: What is kubectl ?
A: Kubectl is the CLI client of the Kbernetes API server. Every kubectl command is just a wrapper for an endpoint of this webservice 

Q: What's the grammar of the kubectl command
A: The grammar is always `kubectl <verb> <ressource type> [name] [options]`. The verbs are few (`get`, `create`, `delete`, `describe`), and the ressource types are the nouns of k8s ([[Nodes|nodes]], [[Pods|pods]], [[Deployments|deployments]] ). 

Q: With kubectl, how do you get infos regarding the cluster and it's Internal DNS
A:  `kubectl cluster-infos`

Q: With kubectl, how do you list the machines inside the cluster
A: `kubectl get nodes`
