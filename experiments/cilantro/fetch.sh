#!/bin/bash

#set -x

export NITERS=${NITERS:=1}
export WORKERS=${WORKERS:="10.10.1.2 10.10.1.3 10.10.1.4 10.10.1.5"}
export SCHED=${SCHED:="default"}

mkdir -p $SCHED/results

for w in $WORKERS; do
    echo "starting power log"
    
    ssh $w sudo systemctl stop rapl_log
    ssh $w sudo rm /tmp/rapl.log
    ssh $w sudo systemctl restart rapl_log
done

for ((t=0;t<$NITERS;t++)); do    
    kubectl logs $(kubectl get pods | awk '/cilantroscheduler/ {print $1;exit}') > $SCHED/results/cilantroscheduler.log
    kubectl -c 'hr-client' logs $(kubectl get pods | awk '/hr-client/ {print $1;exit}') > $SCHED/results/hr-client.log
    kubectl -c 'cilantro-hr-client' logs $(kubectl get pods | awk '/hr-client/ {print $1;exit}') > $SCHED/results/cilantro-hr-client.log
    
    kubectl cp $(kubectl get pods | awk '/hr-client/ {print $1;exit}'):/cilantrologs $SCHED/results/cilantrologs    
    kubectl cp $(kubectl get pods | awk '/cilantroscheduler/ {print $1;exit}'):/cilantro/workdirs $SCHED/results/workdirs

    kubectl get pods -o wide > $SCHED/results/kubectl.pods
    kubectl get pods -o wide --all-namespaces > $SCHED/results/kubectl-all-namespaces.pods
    
    echo "Sleeping for 1 hour ......"
    sleep 3600
    for w in $WORKERS; do
	scp -r $w:/tmp/rapl.log $SCHED/results/rapl.$w.log
    done
done

for w in $WORKERS; do
    ssh $w sudo systemctl stop rapl_log
done

./clean_cluster.sh
