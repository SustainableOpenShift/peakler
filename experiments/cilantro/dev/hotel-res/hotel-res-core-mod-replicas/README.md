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

sumd = 192
root--consul 7
root--frontend 5
root--geo 4
root--jaeger 8
root--memcached-profile 4
root--memcached-rate 3
root--memcached-reserve 7
root--mongodb-geo 3
root--mongodb-profile 3
root--mongodb-rate 3
root--mongodb-recommendation 3
root--mongodb-reservation 3
root--mongodb-user 3
root--profile 3
root--rate 13
root--recommendation 4
root--reservation 16
root--search 4
root--user 96

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

'root--consul': 9.933333333333334
'root--frontend': 11.25,
'root--geo': 11.516666666666667,
'root--jaeger': 15.7,
'root--memcached-profile': 13.9,
'root--memcached-rate': 3.8666666666666667,
'root--memcached-reserve': 5.0,
'root--mongodb-geo': 4.366666666666666,
'root--mongodb-profile': 4.0,
'root--mongodb-rate': 4.1,
'root--mongodb-recommendation': 4.033333333333333,
'root--mongodb-reservation': 4.316666666666666,
'root--mongodb-user':4.0,
'root--profile': 25.816666666666666,
'root--rate': 3.966666666666667,
'root--recommendation': 3.8833333333333333, '
root--reservation': 2.6166666666666667,
'root--search': 9.333333333333334,
'root--user': 6.15

10+11+12+16+14+4+5+4+4+4+4+4+4+26+4+4+3+9+6