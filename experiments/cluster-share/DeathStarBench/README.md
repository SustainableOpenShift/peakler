# DeathStarBench

## Helm setup
```
wget  https://get.helm.sh/helm-v3.16.1-linux-amd64.tar.gz
helm install dsb mediamicroservices
helm install dsb socialnetwork
```

## Wrk setup
```
dnf -y update
dnf -y install epel-release
dnf -y install gcc gcc-c++ git make emacs python3 python3-pip python3-devel wget readline-devel unzip
dnf -y install curl-devel expat-devel gettext-devel openssl-devel zlib-devel

cd /
wget https://www.lua.org/ftp/lua-5.1.5.tar.gz
tar -xf lua-5.1.5.tar.gz
cd lua-5.1.5
make linux
make all test
make linux
make install

cd /
wget https://luarocks.org/releases/luarocks-2.4.2.tar.gz
tar -xf luarocks-2.4.2.tar.gz
cd /luarocks-2.4.2
./configure
make build
make install
luarocks-5.1 install luasocket

cd /
git clone --recursive https://github.com/delimitrou/DeathStarBench.git

cd /DeathStarBench/wrk2/
make


history | cut -c 8-
```

### Run socialNetwork
```
cd /DeathStarBench/socialNetwork/
../wrk2/wrk -D exp -t 2 -c 2 -d 30s -L -s ./wrk2/scripts/social-network/mixed-workload.lua http://nginx-thrift.default.svc.cluster.local:8080 -R 10
```

### Run mediaMicroservices
```
cd /DeathStarBench/mediaMicroservices/
../wrk2/wrk -D exp -t 8 -c 8 -d 30s -L -s ./wrk2/scripts/media-microservices/compose-review.lua http://nginx-web-server.default2.svc.cluster.local:8080/wrk2-api/review/compose -R 10

```