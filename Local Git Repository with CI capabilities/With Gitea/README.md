# Local Gitea installation in Docker with Drone CI

## Installation

First, clone official repo for auto PostgreSQL database provisioning

```bash
git clone https://github.com/mrts/docker-postgresql-multiple-databases.git
```

Then create **ci-network** overlay network in docker:

```bash
docker network create ci-network
```

Run docker-compose:

```bash
docker-compose up -d --build
```

Or in docker swarm mode:

```bash
docker service deploy -c docker-compose.yml gitea
```
