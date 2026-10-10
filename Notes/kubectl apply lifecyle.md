When you run the [[kubectl]] apply command, this is how it traverse the [[kubernetes]] architecture :

![[kubectl-apply-lifecycle.svg]]

1. You send a request from your terminal
`kubectl apply -f demo-app.yaml`

2. The [[Kubernetes API Server]] receive and validate the request. If everything is valid, it saves the desired state in the [[etcd]] database.
3. The [[Kubernetes Scheduler]] detects a newly unassigned [[pods|pod]], it's gonna check inside the [[kubernetes-cluster]] for the [[Kubernetes Node]] with the most ressources available and assign the pod to it.
4. [[kubelet]] will start the container. To achieve this, it will do four actions : Download the OCI image if it's not cached; Ask the [[Kubernetes Container Runtime]] to create the container; Define the volumes, environment variables and resources limits; Start the container;
5. [[kube-proxy]] will configure the network
6. The [[Kubernetes Controller Manager]] will monitor the pod
