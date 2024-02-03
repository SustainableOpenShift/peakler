# peakler

## Kubernetes Setup Instructions
Following instructions at: https://www.cherryservers.com/blog/install-kubernetes-on-ubuntu

This assumes two nodes: `node0` and `node1` that are interconnected via a LAN/VLAN with ip addresses `10.10.1.1` and `10.10.1.2`

`node0` has public facing IP `128.110.96.109`

### Node Information
```
Ubuntu 22.04.2 LTS
Linux 5.15.0-86-generic
```

### Steps
```
sudo apt-get update

# disable swap
sudo swapoff -a
sudo sed -i '/ swap / s/^/#/' /etc/fstab
lsblk

# set hostnames on node0 and node1
sudo hostnamectl set-hostname "kube-master-1"
sudo hostnamectl set-hostname "kube-master-1"

# update /etc/hosts on both nodes
sudo nano /etc/hosts
10.10.1.1 kube-master-1  
10.10.1.2 kube-worker-1

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

# Apply sysctl params without reboot
sudo sysctl --system
```
