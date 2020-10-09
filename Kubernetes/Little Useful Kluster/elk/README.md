
https://www.linode.com/docs/kubernetes/how-to-deploy-the-elastic-stack-on-kubernetes/

```shell
helm repo add elastic https://helm.elastic.co
helm repo update
helm install elasticsearch elastic/elasticsearch
helm install filebeat elastic/filebeat
helm install kibana elastic/kibana
helm install metricbeat elastic/metricbeat

```