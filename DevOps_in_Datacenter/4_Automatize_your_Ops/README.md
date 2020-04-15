# Automatize your Operations

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

// TODO

- Add link on Ansible
- Write Ansible key ideas
- Ansible best practise
 