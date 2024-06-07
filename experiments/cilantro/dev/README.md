# Steps to manually run hotel reservation and cilantro scheduler

## Assumes a kubernetes cluster is already set up and launch hotel reservation system with: `./launch_hotelres.sh`
```
hand32@node0:~/peakler/experiments/cilantro/dev$ kubectl get pods
NAME                                            READY   STATUS    RESTARTS   AGE
root--consul-56f5cf4f78-pwz8q                   1/1     Running   0          18h
root--frontend-57fdd49d77-v6xp2                 1/1     Running   0          18h
root--geo-7cbdf78874-rhmnv                      1/1     Running   0          18h
root--jaeger-65f6b96558-ml25r                   1/1     Running   0          18h
root--memcached-profile-7d6fcb6b8-jtw85         1/1     Running   0          18h
root--memcached-rate-bcc5c97f8-4k98b            1/1     Running   0          18h
root--memcached-reserve-bdcb467b4-bbmpg         1/1     Running   0          18h
root--mongodb-geo-7fbbd9c9c5-9tkf5              1/1     Running   0          23h
root--mongodb-profile-6bb85f4df7-zv9t2          1/1     Running   0          18h
root--mongodb-rate-6d6d667b6-tplr6              1/1     Running   0          18h
root--mongodb-recommendation-59d6b7ccf9-pv7mp   1/1     Running   0          23h
root--mongodb-reservation-7b474745f-s2d8c       1/1     Running   0          23h
root--mongodb-user-6d96648ddc-pj2j8             1/1     Running   0          18h
root--profile-78b66fd976-qpd75                  1/1     Running   0          23h
root--rate-856cbffd6b-p86zg                     1/1     Running   0          18h
root--recommendation-68974cc4fb-fz4lf           1/1     Running   0          18h
root--reservation-7cf759c699-zsp4n              1/1     Running   0          18h
root--search-7dc6c88fd6-nw2pb                   1/1     Running   0          18h
root--user-6bdbbd5d85-s87f4                     1/1     Running   0          23h
```

## Launch cilantro-hr-client.yaml
This launches both hr-client and cilantro-hr-client
`hr-client` is for running wrk2 workload generator to get the tail latency distributions of running the benchmark
`cilantro-hr-client` is the RPC mechanism to pipe output of `hr-client` to `cilantroscheduler` such that it can then make autoscaling decisions
```
hand32@node0:~/peakler/experiments/cilantro/dev$ kubectl apply -f cilantroscheduler.yaml
```

An example run of `hr-client`, where it generates a load of 3000 RPS for 30 seconds and outputs the data to `/cilantrologs/`
```
hand32@node0:~/peakler/experiments/cilantro/dev$ kubectl exec --stdin --tty hr-client-8b4c44b97-sjhjh -c hr-client -- bin/bash
[root@hr-client-8b4c44b97-sjhjh /]# python3 driver/wrk_runscript.py --wrk-logdir /cilantrologs/ --wrk-qps 3000 --wrk-duration 30 --wrk-num-threads 32 --wrk-num-connections 32 --wrk-url http://frontend.default.svc.cluster.local:5000
06-07 18:37:01 | INFO   | wrk_driver                               || Got an initial resource allocs: {'root--consul': 1, 'root--frontend': 1, 'root--geo': 1, 'root--jaeger': 1, 'root--memcached-profile': 1, 'root--memcached-rate': 1, 'root--memcached-reserve': 1, 'root--mongodb-geo': 1, 'root--mongodb-profile': 1, 'root--mongodb-rate': 1, 'root--mongodb-recommendation': 1, 'root--mongodb-reservation': 1, 'root--mongodb-user': 1, 'root--profile': 1, 'root--rate': 1, 'root--recommendation': 1, 'root--reservation': 1, 'root--search': 1, 'root--user': 1}
06-07 18:37:01 | INFO   | wrk_driver                               || Running resource alloc updater thread.
06-07 18:37:01 | INFO   | wrk_driver                               || Running command: ./wrk2/wrk -R 3000 -D exp -t 32 -c 32 -d 30 -L -s /wrk2/scripts/hotel-reservation/mixed-workload_type_1.lua http://frontend.default.svc.cluster.local:5000
06-07 18:37:32 | INFO   | wrk_driver                               || Command finished with exit code 0
06-07 18:37:32 | INFO   | wrk_driver                               || Round complete with allocation {'root--consul': 1.0, 'root--frontend': 1.0, 'root--geo': 1.0, 'root--jaeger': 1.0, 'root--memcached-profile': 1.0, 'root--memcached-rate': 1.0, 'root--memcached-reserve': 1.0, 'root--mongodb-geo': 1.0, 'root--mongodb-profile': 1.0, 'root--mongodb-rate': 1.0, 'root--mongodb-recommendation': 1.0, 'root--mongodb-reservation': 1.0, 'root--mongodb-user': 1.0, 'root--profile': 1.0, 'root--rate': 1.0, 'root--recommendation': 1.0, 'root--reservation': 1.0, 'root--search': 1.0, 'root--user': 1.0}. Writing results to disk.
```
