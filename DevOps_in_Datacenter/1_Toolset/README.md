# Step-1. Toolset preparation

## Tasks

1. Install required software
2. Set up a host with DevOps tools/ Run Vagrant to start up a DevOps host
3. Check software running
   1. `git --version`
   2. `ansible --version`
   3. `docker run hello-world`
   4. `kubectl`

## Description

A right set of instruments is a key of success for every professional.

The same works for DevOps. For the beginning, we will require the following set of instruments:

- VirtualBox Hypervisor ([official link](https://www.virtualbox.org/wiki/Downloads)) + VirtualBox Extension Pack ([direct link](https://download.virtualbox.org/virtualbox/6.1.4/Oracle_VM_VirtualBox_Extension_Pack-6.1.4.vbox-extpack)).
- Vagrant ([official link](https://www.vagrantup.com/)) - a tool to configure development environment, allows to run a set of virtual machines infrastructure as a code (IaaS).
- Docker + docker-compose
- Git
- kubectl
- Python 3.8
- Ansible

The vast majority of DevOps tools are intended for Linux OS, therefore we have to prepare a host to run these instruments. You can install it by yourself or run a prepared `Vagrantfile` mentioned below.

## Using Vagrant-described infrastructure

We provide an already defined `Vagrantfile` which you can use to start up ready-to-go DevOps host. The host will include all required packages.

Requirements:

- VirtualBox OS (host OS doesn't matter).
- VirtualBox Extension Pack.
- Ansible installed

DevOps host characteristics:

- Ubuntu Bionic 18.04
- 2 CPU
- 2 GB RAM
- 40 GB HDD
- 2 Network adapters
  - auto-configured NAT adapter (DHCP-enabled)
  - private host network (192.168.10.10, 192.168.10.10/24)

### Provisioning problem

In case if you have troubles with VM provisioning, e.g. you'are using Windows host, then you can install packages inside the VM:

1. Open SSH session in the VM
2. Go to `/vagrant/ansible` directory
3. Install Ansible `sudo apt-get install ansible`
4. Run Ansible playbook `ansible-playbook -i inventories/local devops.yml`


### Useful vagrant commands

Start up machines

```bash
vagrant up
```

Start up a specified VM

```bash
vagrant up ubuntu
```

Stop VMs

```bash
vagrant halt
```

Open SSH connection to a VM

```bash
vagrant ssh ubuntu
```

Force VM provisioning

```bash
vagrant provision --force
```

Delete all VMs

```bash
vagrant destroy
```