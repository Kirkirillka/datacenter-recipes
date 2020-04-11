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

- Networks
- Volumes
- Resource limitations

## Example of microservice infrastructures


### GPS_Tracker

- [docker-compose.yml](https://github.com/Kirkirillka/GPS_Tracker/blob/master/docker-compose.yml)

![Deployment diagram](https://raw.githubusercontent.com/Kirkirillka/GPS_Tracker/master/docs/schemes/deployment/DeploymentDiagram-Containerized.png)


### One node ELK stack

- [docker-compose.yml](https://github.com/deviantony/docker-elk/blob/master/docker-stack.yml)


### Web microservice application

- [Development with Docker compose](http://howtocookmicroservices.com/docker-compose/)
- [docker-compose.yml](https://gist.github.com/akurkin/1d43fb03c6f415093bab)