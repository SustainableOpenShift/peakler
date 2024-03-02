#!/bin/bash

set -x
for (( ; ; ))
do
    curl -s localhost:9102/metrics | grep -E 'microbench'
    sleep 1
done

