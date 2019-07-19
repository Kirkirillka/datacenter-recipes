#!/bin/bash

# Download packages
yum install net-snmp net-snmp-utils -y


# Allow firewall go through
firewall-cmd --zone=public --add-service=snmp

# Enable snmp
systemctl enable snmpd
# Start snmp
systemctl start snmpd


