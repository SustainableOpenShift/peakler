#!/bin/bash

for (( ; ; ))
do
    curl -s 10.10.126.13:9102/metrics
    sleep 1
done
