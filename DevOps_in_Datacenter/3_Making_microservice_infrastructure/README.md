# Step-3. Making microservice infrastructure.


## Exercise

> This exercise is most important for the on-going Kubernetes workshop, because here you will learn how to containerize your application and prepare a microservice infrastructure to run it.

1. Read theoretical resources
2. Prepare a **Dockerfile** and **docker-compose.yml** for the Python app from the [Step-2](../2_Development_with_Git).
    - Use named volume for web server. 
    - MongoDB must be isolated.
    - The Python Web service is available only through Nginx proxy on default port.
    _ Use overlay networks.
3. Study some examples of real microservice infrastructures [in this section](#example-of-microservice-infrastructures)  below.
4. Prepare hand-made description for the following infrastructures
    - WordPress CRM + PostgreSQL database.
    - A simple JavaScript [application](https://github.com/johny/react-and-redux-tasks-app) with Nginx as proxy server.
    - One-node standalone monitoring subsystem (Prometheus + Graphana + node_exporter) and monitor local Docker host metrics with graphics.

## Short description of Docker and Docker-compose

![Docker architecture](https://docs.docker.com/engine/images/architecture.svg)

Underlying technologies:

- Namespaces - provide isolated workspaces. Used workspaces:
    - The `pid` namespace: Process isolation (PID: Process ID).
    - The `net` namespace: Managing network interfaces (NET: Networking).
    - The `ipc` namespace: Managing access to IPC resources (IPC: InterProcess Communication).
    - The `mnt` namespace: Managing filesystem mount points (MNT: Mount).
    - The `uts` namespace: Isolating kernel and version identifiers. (UTS: Unix Timesharing System).
- Control groups (`cgroups`) - resource control
- Union file systems (UnionFS - AUFS, btrfs, vfs, DeviceMapper)
- CopyOnWrite strategy
- Container format


Key advises:

- Minimize size of images with Multistaging - [link](https://docs.docker.com/develop/develop-images/multistage-build/)
- Use persistent and efficient way to store data - Volumes and Binds - [link](https://docs.docker.com/storage/volumes/)
- Try to use CI/CD tools    
- Divide your infrastructure into testing and production part



### Docker networks

Network driver summary
- **User-defined bridge networks** are best when you need multiple containers to communicate on the same Docker host.
- **Host** networks are best when the network stack should not be isolated from the Docker host, but you want other aspects of the container to be isolated.
- **Overlay** networks are best when you need containers running on different Docker hosts to communicate, or when multiple applications work together using swarm services.
- **Macvlan** networks are best when you are migrating from a VM setup or need your containers to look like physical hosts on your network, each with a unique MAC address.
- **Third-party network plugins** allow you to integrate Docker with specialized network stacks.

[Network modes](https://docs.docker.com/network/):

#### Bridge mode 

**bridge** - Isolated L2 networking, default mode, create a bridge interface in the host machine, then in each container create an isolated interface and bridge it to the host.
 
 **Bridge networks are usually used when your applications run in standalone containers that need to communicate**.

#### Host mode

**host** - Run on the host network. Use the same port pool ($2^{16} -1$) on the host machine, so possible overlapping possible.


#### Overlay mode

**Overlay** - Isolated L3 networking, VXLAN in Docker Swarm, the same for standalone Docker.

#### Macvlan mode

**macvlan** - set an unique MAC address on isolated container interface, host interface runs promiscuous mode.

Using the macvlan driver is sometimes the best choice when dealing with legacy applications that expect to be directly connected to the physical network, rather than routed through the Docker host’s network stack.


#### None mode

**none** - doesn't allow a container to communicate over network.


### Working with Data in Docker

More information is available [here](https://docs.docker.com/storage/).

By default, each container has a writable layer, however, this layer will be deleted once the container is removed.

![Types of Mounts](https://docs.docker.com/storage/images/types-of-mounts.png)

There are three types of mount:

- **Temporary storage in memory** - `tmpfs`.
- **Bind mounts** - mount a directory\file from host machine into container.
- **Volumes** - volumes are managed by Docker. Can be *named* or *anonymous*. You can define a driver for volume and access not-Docker provided mount (NFS, Cloud-based driver, etc.).


### Resource limits

[About Resource limits](https://docs.docker.com/config/containers/resource_constraints/)


You can limit these type of resources provided by host:

- At most CPU cycles time available
- Which CPU cores are accessible for a container
- At most memory amount available


## [Example of microservice infrastructures](#Example of microservice infrastructures)


### GPS_Tracker

- [docker-compose.yml](https://github.com/Kirkirillka/GPS_Tracker/blob/master/docker-compose.yml)

![Deployment diagram](https://raw.githubusercontent.com/Kirkirillka/GPS_Tracker/master/docs/schemes/deployment/DeploymentDiagram-Containerized.png)


### One node ELK stack

- [docker-compose.yml](https://github.com/deviantony/docker-elk/blob/master/docker-stack.yml)


### Web microservice application

- [Development with Docker compose](http://howtocookmicroservices.com/docker-compose/)
- [docker-compose.yml](https://gist.github.com/akurkin/1d43fb03c6f415093bab)


### Prometheus stack

- [GitHub repository](https://github.com/vegasbrianc/prometheus)