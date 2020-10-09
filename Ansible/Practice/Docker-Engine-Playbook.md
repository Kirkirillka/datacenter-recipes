# Установка Docker c помощью Ansible Playbook'а и запуск nginx контейнера


Первое, с чем стоит познакомиться, так это типовым шаблоном для playbook'а.
Пусть следующий YAML содержится в файле **play.yaml**:

```YAML
- hosts: workshop
  vars:
    command: uname
  tasks:
    - name: Check the connection status
      ping:
    - name: Check if nginx is installed
      yum:
        name: nginx
        state: present
    - name: Run a command defined in a variable
      command: "{{command}}"
```


Для запуска playbook'а:

```bash
ansible-playbook -i inventory.yaml  play.yaml
```

![](images/play.png)


Шаблон требует некоторого разъяснения:
- с помощью ключевого слова *hosts* мы определяем узел или группу узлов, на которых будет запущен playbook
- далее с помощью ключевого слова *vars* мы определяем переменную *command* со строковым значением
- далее мы определяем перечень заданий для выполнения.
- в последнем третьем задании мы использовали подстановку по шаблону. "{{command}}" - означает, что будет произведен поиск переменной с именем command, значение подставлено в playbook и будет использовано при вызове модуля *command*


После того, как мы определили типовой шаблон playbook'а, время написать собственный, который:
- Остановит SELinux и firewalld
- Установит Docker из репозитория epel-release
- Запустит демон Docker-а и добавит в автозагрузку
- Запустит контейнер с nginx


```YAML
- hosts: workshop
  tasks:
    # Required for proper docker networks working. In other case, see the required configuration for firewalld
    - name: Disable firewalld
      service:
        name: firewalld
        state: stopped
        enabled: false
    # Should be either stopped or allowed for docker to work
    - name: Disable SELinux
      selinux:
        state: disabled
    # Contains much more available packages
    - name: Make sure epel-release is installed
      yum:
        name: epel-release
        state: latest
    # pip requires for Python package installation for Docker support
    - name: Install docker, pip via Yum
      yum:
        name: [docker-latest, python-pip]
        state: latest          
    - name: install certain python modules for docker
      pip:
        name: "{{ item }}"
        state: present
      with_items:
        - docker
    - name: Start docker and make in autorunning
      service:
        name: docker-latest
        state: restarted
        enabled: yes
    # Run a nginx container and map 80 port of the container to 10000 port on the host.
    # Then try to curl :10000 port
    - name: Run nginx in a container
      docker_container:
        name: web-nginx
        image: nginx
        published_ports: 0.0.0.0:10000:80

```
