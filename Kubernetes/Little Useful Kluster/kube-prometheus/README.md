```shell
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://kubernetes-charts.storage.googleapis.com/
helm repo update

kubectl create ns monitoring

helm install -n monitoring kube-prometheus prometheus-community/kube-prometheus-stack
```