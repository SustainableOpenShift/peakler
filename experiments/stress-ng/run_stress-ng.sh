#!/bin/bash

#set -x

export NCORES=${NCORES:=$(nproc)}
export TIME=${TIME:=60}
export METHOD=${METHOD:="int64"}
export NITERS=${NITERS:=3}


mkdir results

# enable HyperThreads
echo on | sudo tee /sys/devices/system/cpu/smt/control
# enable TurboBoost
echo "0" | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo
sleep 60

NCORES=$(nproc)

echo "NITERS: ${NITERS}"
echo "NCORES: ${NCORES}"
echo "TIME: ${TIME}"

for ((iter=0; iter<${NITERS}; iter+=1 )); do
    for (( i=1; i<=${NCORES}; i+=1 )); do
	#echo "stress-ng --vm ${i} --vm-bytes 2G --mmap ${i} --mmap-bytes 2G --page-in -t ${TIME}s"
	#echo "results/stress-ng.iter${iter}.numcpus${i}.TurboOn.HyperThreadOn.vm2G.${TIME}"
	sudo rm /tmp/rapl.log
	sudo systemctl restart rapl_log
	
	#stress-ng --cpu $i --cpu-method int64 -t ${TIME}s
	stress-ng --vm ${i} --vm-bytes 2G --mmap ${i} --mmap-bytes 2G --page-in -t ${TIME}s
	
	sudo systemctl stop rapl_log
	
	#cp /tmp/rapl.log "results/stress-ng.iter${iter}.numcpus${i}.TurboOn.HyperThreadOn.int64.60"
	cp /tmp/rapl.log "results/stress-ng.iter${iter}.numcpus${i}.TurboOn.HyperThreadOn.vm2G.${TIME}"
    done
done

# disable HyperThreads
echo off | sudo tee /sys/devices/system/cpu/smt/control
# disable TurboBoost
echo "1" | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo
sleep 60

for ((iter=0; iter<${NITERS}; iter+=1 )); do
    for (( i=1; i<=${NCORES}; i+=1 )); do
	sudo rm /tmp/rapl.log
	sudo systemctl restart rapl_log
	
	#stress-ng --cpu $i --cpu-method int64 -t ${TIME}s
	stress-ng --vm ${i} --vm-bytes 2G --mmap ${i} --mmap-bytes 2G --page-in -t ${TIME}s
	
	sudo systemctl stop rapl_log
	cp /tmp/rapl.log "results/stress-ng.iter${iter}.numcpus${i}.TurboOff.HyperThreadOff.vm2G.${TIME}"
	#cp /tmp/rapl.log "results/stress-ng.iter${iter}.numcpus${i}.TurboOff.HyperThreadOff.int64.60"
    done
done

