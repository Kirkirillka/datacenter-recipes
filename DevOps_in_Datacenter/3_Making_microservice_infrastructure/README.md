# Step-3. Making microservice infrastructure.


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


// TODO

- Volumes
- Resource limitations


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


## Example of microservice infrastructures


### GPS_Tracker

- [docker-compose.yml](https://github.com/Kirkirillka/GPS_Tracker/blob/master/docker-compose.yml)

![Deployment diagram](https://raw.githubusercontent.com/Kirkirillka/GPS_Tracker/master/docs/schemes/deployment/DeploymentDiagram-Containerized.png)


### One node ELK stack

- [docker-compose.yml](https://github.com/deviantony/docker-elk/blob/master/docker-stack.yml)


### Web microservice application

- [Development with Docker compose](http://howtocookmicroservices.com/docker-compose/)
- [docker-compose.yml](https://gist.github.com/akurkin/1d43fb03c6f415093bab)