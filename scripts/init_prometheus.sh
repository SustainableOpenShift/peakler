#!/bin/bash

#set -x

tar -xf prometheus.tar.gz

echo "🟢 apply prometheus manifests 🟢"
kubectl apply --server-side -f kube-prometheus-0.13.0/manifests/setup

sleep 1
until kubectl get servicemonitors --all-namespaces ; do date; sleep 1; echo ""; done
sleep 1

kubectl apply -f kube-prometheus-0.13.0/manifests/

echo "🟢 wait 30 secs, hopefully all ready 🟢"
sleep 30
kubectl get pods --all-namespaces
