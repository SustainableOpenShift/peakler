#!/bin/bash

#set -x

sudo rm /tmp/rapl.log

sudo systemctl restart rapl_log

#for (( i=1; i<=$(nproc); i+=1 )); do
for (( i=1; i<=2; i+=1 )); do
    stress-ng --cpu $i --cpu-method int64 -t 120s
done

sudo systemctl stop rapl_log
