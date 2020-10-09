```shell
helm repo add gitlab https://charts.gitlab.io/
helm repo update

helm install gitlab/gitlab --set global.hosts.domain=gitlab-on-k8s.com --set certmanager-issuer.email=kirillkukarcev@gmail.com

```