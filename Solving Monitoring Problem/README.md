# Monitoring Systems Parameters and Requirements

## Links

- https://studbooks.net/75829/ekonomika/trebovaniya_sistemam_monitoringa
- https://www.researchgate.net/figure/Detailed-analysis-of-functional-requirements-for-cloud-monitoring-tools_tbl4_320804254
- https://habr.com/ru/post/308610/
- https://habr.com/ru/company/sberbank/blog/420731/
- https://vc.ru/dev/62715-kak-my-stroili-monitoring-na-prometheus-clickhouse-i-elk

## Quality of monitoring systems


## Monitoring systems' duty

- to gather information about IT services - more business-wise thinking.
- to gather information about IT infrastructure - servers, networks, etc.
- optimization of IT infrastructure usage.
- outage time minimization - information about a possible issue is already found.
- incident time management minimization - all necessary information about services relationship, it is possible to know in which place a failure occurs.
- proactive notification about problems in IT infrastructure.
- centralized services management.

## List of requirements for monitoring systems

- automated searching and deletction for montoring objects and components.
- support for hardware and software monitoring.
- support for multiple sensors.
- preinstalled rules and templates for well-known services.
- measure influence level of service's crash on other infrastructure.
- alerting subsystem.
- triggers, correlation.
- visualization subsystem.
- Pull + Push architecture (Agent, agent-less).
- Ability to scale horizontally.
- Third-part integration.


## Metrics to monitor

### Operation System Level

- CPU
  - CPU Core Number
  - CPU Usage
  - CPU Load
- Memory 
  - Amount of memory granted
  - Amount of memory used
  - Amount of memory free
- Swap
  - Swap usage
  - Swap I/O bytes
- Network
  - RX bytes/sec
  - TX bypes/sec
- Disk
  - Disk latency
  - Disk iops
  - Read/Write bytes/sec

