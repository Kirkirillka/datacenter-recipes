# Что такое Ansible

- [Ansible Everything](https://www.ansible.com/hubfs/2018_Content/AnsibleEverything-Master.pdf?hsLang=en-us)
- [History of Ansible](https://www.ansible.com/blog/2013/12/08/the-origins-of-ansible)


Ansible - система управления конфигурациями, написанная на Python. Использует декларативный язык разметки (YAML). Ansible не использует какие-либо агенты для взаимодействия, может управлять как Linux, так и Windows узлами.


## История развития

Слово "Ansible" означает выдуманное средство гиперсвязи в книге "Игра Эндера" и было придоумано в романе "Мир Роканнона"

- Была написана Michael DeHann в 2012 году
- Была куплена RedHat в 2015 году


## Основные особенности

- Безагентный режим
  - Python/SSH для Linux
  - WinRM/PowerShell для Windows
- Более 2400 модулей под различные IT-потребности
- Декларативный язык YAML и шаблонизатор Jinja для описания заданий
- Не требует дополнительных модулей и программ на конфигурируемых системах


### Секции модулей

- Cloud - поддержка Amazon, Azure, Cloudstack, Digital Ocean, Docker, LXC< OpenStack, Rackspace, VMware, etc.
- Clustering - поддержка Consul, ZooKeeper, Kubernetes
- Commands - выполнение консольных команд и скриптов
- Crypto
- Database - поддержка баз данных MySQL, PostgreSQL, MongoDB, Redis, etc.
- Files - копирование, синхронизация, модификация, проверка, архивирование и т. д.
- Identity
- Inventory - работа с именами хостов или их ip-адресами.
- Messaging - поддержка RabbitMQ
- Monitoring - поддержка систем мониторинга DataDog, Nagios, Zabbix и пр.
- Network - работа с сетевым оборудованием и ПО F5 BIG-IP, Cisco IOS/NXOS, Juniper JunOS, OpenSwitch, Cumulus Linux
- Notification - отсылаются сообщения в Campfire, HipChat, Jabber, Pushbullet, Slack, через email/sms
- Packaging - работа с менеджерами пакетов apt, FreeBSD Ports, Gentoo, homebrew, pacman, opkg, Red Hat software channels, yum, xbps, zypper
- Remote Management
- Source Control - работа с системами контроля версий git, mercurial, subversion
- Storage
- System - работа с компонентами Linux/Unix систем — cron, iptables, LVM, SELinux, sshd, zfs
- Utilities - реализуют внутреннюю логику плейбуков
- Web infrastructure - работа с Apache, Django, JBoss, JIRA
- Windows - работа с компонентами Windows, в том числе IIS, Windows Firewall, реестром
