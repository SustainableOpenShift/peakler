#!/bin/bash

for n in $(kubectl get -o=name pvc,configmap,serviceaccount,secret,ingress,service,deployment,statefulset,hpa,job,cronjob)
do
    mkdir -p $(dirname $n)
    kubectl get $n -o yaml | ./kubectl-neat > $n.yaml
done
