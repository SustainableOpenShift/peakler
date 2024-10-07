~~~
root@root--db0j1-head-546c447fd8-bb94x:/usr/local/bin# ray start --head --port=6379 --redis-shard-ports=6380,6381 --num-cpus=0 --object-manager-port=12345 --node-manager-port=12346 --dashboard-host=0.0.0.0 --block
root@root--db0j1-head-546c447fd8-bb94x:/usr/local/bin# ray --version
ray, version 1.6.0

root@root--db0j1-6489549d57-5cbn5:/cray_workloads# ray start --head --num-cpus=$MY_CPU_REQUEST --address=$ROOT__DB0J1_HEAD_SVC_SERVICE_HOST:$ROOT__DB0J1_HEAD_SVC_SERVICE_PORT_REDIS --object-manager-port=12345 --node-manager-port=12346 --block --verbose

root@root--db0j1-client-f4d78c4fc-z9t64:/cray_workloads# python cray_workloads/drivers/cray_runscript.py --cray-utilfreq 10 --cray-logdir /cilantrologs --cray-workload-type db_task --ray-svc-name root--db0j1-head-svc --sleep-time 0.0 --trace-scalefactor 0.5 --trace-path /cray_workloads/traces/twit-b1000-n88600.csv --query-bin 0 --db-path /cray_workloads/db_data/tpcds_data/sqlite/tpcds.db --queries-file-path /cray_workloads/db_data/tpcds_data/queries/processed --query-bins-path /cray_workloads/db_bins/bins_kk_duplicate.json
~~~