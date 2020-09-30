# Kubernetes architecture

## K8s components

### Control plane

* **kube-apiserver** - the API server to expose the Kubernetes API. Scales by deploying more instances.
* **etcd** - consistent and highly-avaialble key value store
* **kube-scheduler** - component that watches for newly created Pods with no assigned node, and selects a node for them to run on. Accounted factors: resource req-s (individual and collective), hardware/software/policy constraints, affinity and anti-affinity specifications, data locality, inter-workload interference, deadlines.
* **kube-controller-manager** - runs controller pocesses. Logically, each controller is a separate process, but bundled in one binary. These built-in controllers provide important core behaviors. These controllers include:
    - Deployment Controller
    - Job Controller
    - Node Controller - Responsible for noticing and responding when nodes go down
    - Replication controller - Responsible for maintaining the correct number of pods for every replication controller object in the system
    - Endpoints controller- Populates the Endpoints object (join Services & Pods)
    - Service Account & Token controllers - Create default accounts and API access tokens for new namespaces
* **cloud-controller-manager** - component that embeds cloud-specific control logic. The cloud controller manager lets you link your cluster into your cloud provider's API. To separate out the components that interact with that cloud platform from components that just interact withyour cluster. The following controllers can have cloud provider dependencies:
    - Node controller: for checking the cloud provider to determine if a node has been deleted in the cloud after it stops responding
    - Route controller: For setting up routes in the underlying cloud infrastructure
    - Service controller: For creating, updating and deleting cloud provider load balancers

### Node components

* **kubelet** - an agent that runs on each node in the cluster. It makes sure that containers are running in a Pod. PodSpecs
* **kube-proxy** - is a network proxy that runs on each node in your cluster, implementing part of the Kubernetes Service concept. Maintains network rules on nodes.

The componets on a node include:

* kubelet
* container runtime
* kube-proxy

### Controllers

In robotics and automation, a *control loop* is a non-terminating loop that regulates the state of a system (example: Termostat, desired and current states). Each controller tries to move the current cluster state closer to the desired state.

### Container images

A container image is a ready-to-run software package, containing everything needed to run an application: the code and any runtime it requires, application and system libraries, and default values for any essential settings.
