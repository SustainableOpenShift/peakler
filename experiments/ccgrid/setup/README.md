
## Setup

```
wget https://go.dev/dl/go1.23.2.linux-amd64.tar.gz
tar -xf go1.23.2.linux-amd64.tar.gz

git clone --depth 1 git@github.com:sustainable-computing-io/kepler.git
make build-manifest OPTS="BM_DEPLOY PROMETHEUS_DEPLOY"
kubectl create -f _output/generated-manifest/deployment.yaml

git clone --depth 1 https://github.com/prometheus-operator/kube-prometheus
cd kube-prometheus
kubectl apply --server-side -f manifests/setup
until kubectl get servicemonitors --all-namespaces ; do date; sleep 1; echo ""; done
kubectl apply -f manifests/

```