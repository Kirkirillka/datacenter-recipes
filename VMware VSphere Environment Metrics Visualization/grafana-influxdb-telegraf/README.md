# Exporting VMWare Metrics using Grafana-Influxdb-Telegraf

Inspiring articles:
- [link1](https://computingforgeeks.com/how-to-monitor-vmware-esxi-with-grafana-and-telegraf/)
- [link2](https://jorgedelacruz.uk/2018/10/01/looking-for-the-perfect-dashboard-influxdb-telegraf-and-grafana-part-xii-native-telegraf-plugin-for-vsphere/)


## Installation

### Modify credentials to connect to VMWare vCenter

Modify the following parameters in **telegraf.conf**:

``` toml
[[inputs.vsphere]]
## List of vCenter URLs to be monitored. These three lines must be uncommented
## and edited for the plugin to work.
vcenters = [ "https://IP/sdk" ]
   username = "USERNAME"
   password = "PASSWORD"
```

### Start containers
```bash
docker-compose start
```

### Add InfluxDB as datasource

Make sure you connecting to local DNS binding **http://influxdb:8086** instead of IP address.

Credentials to connect to InfluxDB are specified in environment vars in [docker-compose](docker-compose.yaml).

![](https://itsecforu.ru/wp-content/uploads/2019/04/grafana-add-influxdb-data-source-02-768x421.png)


### Import the following dashboards:
- [Grafana vSphere Overview Dashboard - 8159](https://grafana.com/dashboards/8159)
- [Grafana vSphere Datastore Dashboard – 8162](https://grafana.com/dashboards/8162)
- [Grafana vSphere Hosts Dashboard – 8165](https://grafana.com/dashboards/8165)
- [Grafana vSphere VMs Dashboard – 8168](https://grafana.com/dashboards/8168)

### Here we go

One point to note - the list of metrics is skipped, so all metrics are collected.

Here you can see specific metrics to add [link](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/vsphere).

![](https://camo.githubusercontent.com/dffee05782a4cf90b20e74f859bb3c8138a87e83/68747470733a2f2f7777772e6a6f72676564656c616372757a2e65732f77702d636f6e74656e742f75706c6f6164732f323031382f31302f67726166616e612d657378692d3032322e706e67)
