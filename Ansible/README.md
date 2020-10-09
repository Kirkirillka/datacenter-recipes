# Plan:

## Theory:
1. What Ansible is? History, main features.
2. Architecture concepts of Ansible
3. Application fields. Where Ansible is widely used and what it could help you to gain.

## Practical:
0. YAML syntax observation
1. Prepare infrastructure to be connected via SSH
2. Prepare inventory list
3. Run several commands
  - ping
  - command: uname -a
  - yum install nginx
  - service enable nginx
  - reboot
4. Install docker-engine with handmade ansible playbook

## Improvisation

Task description:

You will need to write an Ansible playbook which makes:
- Disable SELinux
- Allow HTTP on firewall
- Install Docker engine
- Runs official Wordpress docker image on the 10000 port
- Install nginx on target systemm, not a container
- Configure nginx to proxy all requests to the created Wordpress docker image
- Restart the server


As the result, you must be able to open a web-page  hosted by nginx and see Wordpress's greeting page.

Links for you to help
- [Docker Wordpress image](https://hub.docker.com/_/wordpress)
- [Ansible firewall module for RHEL](https://docs.ansible.com/ansible/latest/modules/firewalld_module.html)
- [Ansible Yum module](https://docs.ansible.com/ansible/latest/modules/yum_module.html)
- [Ansible Systemd services management module](https://docs.ansible.com/ansible/latest/modules/yum_module.html)
- [Ansible SELinux module](https://docs.ansible.com/ansible/latest/modules/selinux_module.html)
- [Ansible Template for Configuration module](https://docs.ansible.com/ansible/latest/modules/template_module.html)
- [Ansible model for Docker configuration](https://docs.ansible.com/ansible/latest/modules/docker_container_module.html)
- [Ansible pip Python packages management module](https://docs.ansible.com/ansible/latest/modules/pip_module.html)
