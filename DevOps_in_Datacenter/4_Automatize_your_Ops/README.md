# Automatize your Operations

## Requirements

- Visual Studio Code
- Ansible
- A set of virtual environments
  - staging/testing environment
    - 1 Debian10 host
  - production environment
    - 2 Debian 10 Buster hosts
    - 1 CentOS host

To make our life easier, we will use special syntax plugins for VS Code/
For the workshop, you should have some kind of virtual environment where we will play around with Ansible.

In the workshop we will do:

- Prepare inventory file for staging/production environment
- Prepare a role to install required software
  - load-balancer: nginx
  - db: MongoDB + docker
  - simple_python_app: Python3 + Python dependencies + docker
- Deploy a simple microservice infrastructure on those hosts
- Ensure that SSH root login is prohibited

For simplicity, let's suppose we're deploying our software like this is just static files located in the same directory as Ansible files are.In real case, please, use cloning from git repositories and Docker images.

## Exercise

In this workshop your task is to create a manageable web service infrastructure.

You must prepare a set of VM includes three VM:

1. A web backend service
2. A DB machine
3. A load-balancer machine

You are free to choose which way to use to do the task, however, there are some requirements and suggestions:

1. You should use an orchestration solution (Chef, Puppet, **Ansible** is prefered).
2. Use containers for the cases where it's appropriate.
3. The internal services must be isolated from the outside, one entry point is the load-balancer.
4. Use manageable PostgreSQL instance. If you would prefer to use a container for PostgreSQL, take into account possible consequences.
5. Use a simple web application from [Step-3](../3_Making_microservice_infrastructure) for the web backend service.
6. Try to follow Infrastructure-as-a-Code approach as frequent as possible. Use Git flow to track changes in your code, and post your repository on Gitlab.

Finally, as result, you will receive:

- Deployable description for your application infrastructure - IaaC.
- Shippable repository with observable history.
- Hand-on experience how to use automation tools.

## Short introduction

- [Introduction to Ansible by Radenko Čitaković](https://www.cisco.com/c/dam/m/sr_rs/events/2019/cisco-connect/pdf/using_ansible_in_dc_automation_radenko_citakovic.pdf)
- [Another good list of Ansible playbooks](https://github.com/Kirkirillka/ansible-handmade/tree/master/playbooks)
- [Example of IPSec server Ansible role](https://github.com/Kirkirillka/ansible-ipsec-vpn)
- [Ansible Best Practises](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
