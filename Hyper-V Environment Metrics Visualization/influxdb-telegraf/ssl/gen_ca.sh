#!/bin/sh

# Generate for nginx
openssl req \
  -new \
  -newkey rsa:4096 \
  -days 3650 \
  -nodes \
  -x509 \
  -subj "/C=RU/ST=RU/L=Kazan/O=nginx ingress/CN=nginx.dc.local" \
  -keyout nginx.key \
  -out nginx.pem


# Generate for InfluxDB
openssl req \
  -new \
  -newkey rsa:4096 \
  -days 3650 \
  -nodes \
  -x509 \
  -subj "/C=RU/ST=RU/L=Kazan/O=InfluxDB ingress/CN=influx.dc.local" \
  -keyout influxdb.key \
  -out influxdb.pem