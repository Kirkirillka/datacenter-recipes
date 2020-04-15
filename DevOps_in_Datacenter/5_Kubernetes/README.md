# Kubernetes

- https://drive.google.com/file/d/1Lfi8r0GZdFIMgprUrwaf-Lru5RsctML7/view
- https://github.com/cncf/presentations/tree/master/kubernetes
- [RU] Kubernetes для бизнеса -[True Engineering](https://trueengineering.ru/ru/cases/k8s_for_business)

## Exercise

Your task is to install a 3-nodes Kubernetes cluster.

You have two options to install and run Kubernetes cluster:

- Manual installation
- Automated installation with specialized tools (I could suggest [Kubespray](https://github.com/kubernetes-sigs/kubespray))

Personally, I suggest to use a tool, not type command by yourself.

So, in your installation, you will have to prepare:

- Three Kubernetes nodes. 1 Master and 2 Nodes.
- Configured Ingress service based on nginx.
- Installed [Helm](https://helm.sh/) package manager.
- Installed monitoring service with Prometheus and Graphana - [linl](https://github.com/coreos/kube-prometheus)

As usual, there some requirements for your work:

- Please, keep all code, especially Kubernetes YAML configuration in a well structured Git repository.
- Try to use automation tools, such as Ansible.

## Kubernetes Short Review

Advantages

- Help to provide hgih availability of system, works for years
- Dynamic growing of software
- A unified development and operation team work in the same environment

However, Kubernetes is _expensive_:

- A bunch of new technologies
- Requires to reformat the ways you used in design, development, testing and operations
- Kubernetes is a compicated system, also require attention and qualified engineers for administration

Finally, you will get:

- Updating procedure will be much easire and more explicit for everyone.
- A new engineer can faster to start work in
- CI/CD pipeline is explit and automated
- Unified user experience for team
- Online updating

Tips:

- `helm install prometheus stable/prometheus --set alertmanager.persistentVolume.enabled=False --set server.persistentVolume.enabled=false`

## Description

Kubernetes stands for Greek "pilot", "helmsman of a ship", or "кормчий" (рус.)

Kubernetes is a **Production Grade COntainer Orchestration System**

- All services are natively Load Balanced
- Can scaly up and down dynamically
- Self-healing and seamless upgrading or rollback of applications

## Key concepts

- Pods
- Services

### Pods

Atomic unit or smalles "unit of work" of Kubernetes. Can include one or several containers. They are ephemeral, which means they can be created or deleted without warning.

### Services

Unified method of accessing the exposed workload of Pods

This is **durable resource**, not epheral:

- Static cluster IP
- Static namespaced DNS name

## Kubernetes Components

We can define master-running components and nodes-running elemets:

- Kubernetes Master
  - kube-apiserver
  - kube-controller-manager
  - kube-scheduler
- Nodes
  - kubelet
  - kube-proxy

The **Kubernetes master** is responsible for maintaining the desired state of your cluster.

The **nodes** are the machines that run your applications and cloud workflows. The Kubernetes master controls each node.

![Kubernetes Components](https://d33wubrfki0l68.cloudfront.net/7016517375d10c702489167e704dcb99e570df85/7bb53/images/docs/components-of-kubernetes.png)

## Kubernetes objects

Kubernetes Abstractions

Basic objects

- Pod
- Service
- Volume
- Namespace

Abstractions depending on [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/)

- Deployment
- DeamonSet
- StatefulSet
- ReplicateSet
- Job
