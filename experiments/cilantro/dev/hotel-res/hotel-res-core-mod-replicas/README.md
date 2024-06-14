# Modified number of replicas per deployment

```
Based off calculations from ucbopt

root--consul num pods 7
root--frontend num pods 16
root--geo num pods 7
root--jaeger num pods 5
root--memcached-profile num pods 6
root--memcached-rate num pods 7
root--memcached-reserve num pods 5
root--mongodb-geo num pods 3
root--mongodb-profile num pods 3
root--mongodb-rate num pods 4
root--mongodb-recommendation num pods 3
root--mongodb-reservation num pods 4
root--mongodb-user num pods 4
root--profile num pods 9
root--rate num pods 5
root--recommendation num pods 5
root--reservation num pods 7
root--search num pods 14
root--user num pods 6
sum deploy =  120

hand32@node0:~/peakler/experiments/cilantro/dev/hotel-res/hotel-res-core-mod-replicas$ grep -r "replicas:"
geo/geo-deployment.yaml:  replicas: 7
geo/mongodb-geo-deployment.yaml:  replicas: 3
user/mongodb-user-deployment.yaml:  replicas: 4
user/user-deployment.yaml:  replicas: 6
frontend/frontend-deployment.yaml:  replicas: 16
search/search-deployment.yaml:  replicas: 14
profile/memcached-profile-deployment.yaml:  replicas: 6
profile/mongodb-profile-deployment.yaml:  replicas: 3
profile/profile-deployment.yaml:  replicas: 9
jaeger/jaeger-deployment.yaml:  replicas: 5
reserve/reservation-deployment.yaml:  replicas: 7
reserve/mongodb-reservation-deployment.yaml:  replicas: 4
reserve/memcached-reservation-deployment.yaml:  replicas: 5
reccomend/mongodb-recommendation-deployment.yaml:  replicas: 3
reccomend/recommendation-deployment.yaml:  replicas: 5
consul/consul-deployment.yaml:  replicas: 7
rate/memcached-rate-deployment.yaml:  replicas: 7
rate/mongodb-rate-deployment.yaml:  replicas: 4
rate/rate-deployment.yaml:  replicas: 5
hand32@node0:~/peakler/experiments/cilantro/dev/hotel-res/hotel-res-core-mod-replicas$ grep -r "replicas:" |  awk -F 'replicas: ' '/replicas:/ {sum += $2} END {print sum}'
120
```