#!/bin/bash

function updateAll {
    sed -i "s/replicas: [0-9]\+/replicas: $1/" geo/geo-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" geo/mongodb-geo-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" user/mongodb-user-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" user/user-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" frontend/frontend-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" search/search-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" profile/memcached-profile-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" profile/mongodb-profile-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" profile/profile-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" jaeger/jaeger-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" reserve/reservation-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" reserve/mongodb-reservation-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" reserve/memcached-reservation-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" reccomend/mongodb-recommendation-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" reccomend/recommendation-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" consul/consul-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" rate/memcached-rate-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" rate/mongodb-rate-deployment.yaml
    sed -i "s/replicas: [0-9]\+/replicas: $1/" rate/rate-deployment.yaml
}

"$@"
