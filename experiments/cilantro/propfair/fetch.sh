#!/bin/bash

set -x

mkdir -p results

for ((t=0;t<7;t++)); do
    kubectl logs $(kubectl get pods | awk '/cilantroscheduler/ {print $1;exit}') > results/cilantroscheduler.log
    kubectl -c 'hr-client' logs $(kubectl get pods | awk '/hr-client/ {print $1;exit}') > results/hr-client.log
    kubectl -c 'cilantro-hr-client' logs $(kubectl get pods | awk '/hr-client/ {print $1;exit}') > results/cilantro-hr-client.log
    
    kubectl cp $(kubectl get pods | awk '/hr-client/ {print $1;exit}'):/cilantrologs ./results/cilantrologs
    
    kubectl cp $(kubectl get pods | awk '/cilantroscheduler/ {print $1;exit}'):/cilantro/workdirs ./results/workdirs

    kubectl get pods > ./results/kubectl.pods
    kubectl get pods --all-namespaces > ./results/kubectl-all-namespaces.pods
    
    for ((i=2;i<=20;i++)); do
	mkdir -p results/10-10-1-$i-sensors
	scp -o ConnectTimeout=30 -r 10.10.1.$i:/tmp/sensors.* results/10-10-1-$i-sensors/
    done

    echo "Sleeping for 1 hour ......"
    sleep 3600
done
