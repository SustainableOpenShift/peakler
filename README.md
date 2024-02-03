# peakler Project

# Kubernetes Setup Instructions
Following instructions at: https://www.cherryservers.com/blog/install-kubernetes-on-ubuntu

This assumes two nodes: `node0` and `node1` that are interconnected via a LAN/VLAN with ip addresses `10.10.1.1` and `10.10.1.2`

`node0` has public facing IP `128.110.96.109`

### Node Information
```
Ubuntu 22.04.2 LTS
Linux 5.15.0-86-generic
```

### Steps for both `node0` and `node1`
```
sudo apt-get update

# disable swap
sudo swapoff -a
sudo sed -i '/ swap / s/^/#/' /etc/fstab
lsblk

# Run these separately
# set hostname on node0 
sudo hostnamectl set-hostname "kube-master-1"
# set hostname on node1
sudo hostnamectl set-hostname "kube-worker-2"

# update /etc/hosts
sudo nano /etc/hosts
10.10.1.1 kube-master-1  
10.10.1.2 kube-worker-2

# Set up the IPV4 bridge on all nodes
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter

# sysctl params required by setup, params persist across reboots
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF

sudo sysctl --system

# Install kubelet, kubeadm, and kubectl on each node
sudo apt-get install -y apt-transport-https ca-certificates curl
sudo mkdir /etc/apt/keyrings
curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-archive-keyring.gpg
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt install -y kubelet=1.28.2-00 kubeadm=1.28.2-00 kubectl=1.28.2-00

# prevents them from being updated, upgraded, etc
sudo apt-mark hold kubeadm kubelet kubectl

# install docker
sudo apt install docker.io
sudo mkdir /etc/containerd
sudo sh -c "containerd config default > /etc/containerd/config.toml"
sudo sed -i 's/ SystemdCgroup = false/ SystemdCgroup = true/' /etc/containerd/config.toml
sudo systemctl restart containerd.service
sudo systemctl enable kubelet.service
sudo systemctl restart kubelet.service
sudo systemctl enable kubelet.service

# initialize kubernetes services
sudo kubeadm config images pull
```

### Steps for `node0`
```
# initializes cluster on kube-master-1
sudo kubeadm init --pod-network-cidr=10.10.0.0/16

# assuming init runs correctly
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# use Calico for node communication
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/tigera-operator.yaml
curl https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/custom-resources.yaml -O

# this is to replace the 192.168.0.0/16 in custom-resources.yaml to our --pod-network-cidr=10.10.0.0/16
sed -i 's/cidr: 192\.168\.0\.0\/16/cidr: 10.10.0.0\/16/g' custom-resources.yaml
kubectl create -f custom-resources.yaml

# make sure everything is up and running
kubectl get pods --all-namespaces

# creates a new join command for node1 to join the cluster
kubeadm token create --print-join-command

# after node1 joins below
@kube-master-1:~$ kubectl get nodes -o wide
NAME            STATUS   ROLES           AGE   VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
kube-master-1   Ready    control-plane   47h   v1.28.2   10.10.1.1     <none>        Ubuntu 22.04.2 LTS   5.15.0-86-generic   containerd://1.7.2
kube-worker-2   Ready    <none>          46h   v1.28.2   10.10.1.2     <none>        Ubuntu 22.04.2 LTS   5.15.0-86-generic   containerd://1.7.2

# make sure everything is up and running
@kube-master-1:~$ kubectl get pods --all-namespaces
NAMESPACE          NAME                                       READY   STATUS    RESTARTS   AGE
calico-apiserver   calico-apiserver-66f746f458-f7px9          1/1     Running   0          46h
calico-apiserver   calico-apiserver-66f746f458-pd2j2          1/1     Running   0          46h
calico-system      calico-kube-controllers-84dc8bcc94-fx22p   1/1     Running   0          47h
calico-system      calico-node-99kzc                          1/1     Running   0          46h
calico-system      calico-node-kwss5                          1/1     Running   0          47h
calico-system      calico-typha-8d9f94f9c-2z5jd               1/1     Running   0          47h
calico-system      csi-node-driver-5djhx                      2/2     Running   0          46h
calico-system      csi-node-driver-k7snh                      2/2     Running   0          47h
kube-system        coredns-5dd5756b68-f7s4d                   1/1     Running   0          47h
kube-system        coredns-5dd5756b68-xj8rf                   1/1     Running   0          47h
kube-system        etcd-kube-master-1                         1/1     Running   0          47h
kube-system        kube-apiserver-kube-master-1               1/1     Running   0          47h
kube-system        kube-controller-manager-kube-master-1      1/1     Running   0          47h
kube-system        kube-proxy-96ppb                           1/1     Running   0          46h
kube-system        kube-proxy-r7fkr                           1/1     Running   0          47h
kube-system        kube-scheduler-kube-master-1               1/1     Running   0          47h
tigera-operator    tigera-operator-94d7f7696-99j5n            1/1     Running   0          47h
```

### Steps for `node1`
```
# clean up state just incase
sudo kubeadm reset

# uses previous --print-join-commnd from node0
sudo kubeadm join 128.110.96.109:6443 --token XXXXXX --discovery-token-ca-cert-hash XXXXX
```

# Kepler Setup Instructions
Following instructions at: https://sustainable-computing.io/installation/kepler/

## Deploy Promethesus
https://sustainable-computing.io/installation/kepler/#deploy-the-prometheus-operator
```
git clone --depth 1 https://github.com/prometheus-operator/kube-prometheus
cd kube-prometheus
kubectl apply --server-side -f manifests/setup
until kubectl get servicemonitors --all-namespaces ; do date; sleep 1; echo ""; done
kubectl apply -f manifests/
```
