# kongs

```bash
# using YAMLs
$ kubectl apply -f https://bit.ly/k4k8s

# or using Helm
$ helm repo add kong https://charts.konghq.com
$ helm repo update

# Helm 3
$ helm install kong/kong --generate-name --set ingressController.installCRDs=false -f values.yaml

```
