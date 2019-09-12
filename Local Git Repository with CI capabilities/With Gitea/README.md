# Gitea + Drone CI

## Information

In this configuration combined four elements:

- PostgreSQL v11 - RDBMS
- Gitea v1.9.3 - Github-like self-hosted repository management system
- Drone CI Server v1.3.1 - CI/CD platform
- Drone CI Agent v1.3.1 -  a linux agent to run jobs from Drone Server

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
