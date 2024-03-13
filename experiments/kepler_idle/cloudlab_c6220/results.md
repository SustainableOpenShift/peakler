## Normal idle power: CPU Package, DRAM
hand32@node1:~/peakler/experiments/kepler_idle/cloudlab_c6220$ tail -f /tmp/rapl.log
10.719421 10.099686
17.33049 10.944229
10.405319 10.215683
12.033722 10.269455
11.173584 10.233887
11.414185 10.153687
11.584732 10.175293
11.832031 10.198807
11.27681 10.061768
12.659271 10.429565
12.536102 10.314194
15.077087 10.798126
11.971802 10.411591
10.165741 10.138184
12.15741 10.324173
12.889145 10.389709
12.779739 10.40358
13.661804 10.422379
12.531311 10.355545
10.607666 10.179443
11.751556 10.524963
17.117844 11.151062
12.811157 10.369446
11.353714 10.203079

## After setting up k8s+prometheus+kepler
```
hand32@node0:~/peakler/scripts$ kubectl get nodes
NAME                                              STATUS   ROLES           AGE     VERSION
node0.hand32-194769.bayopsys-pg0.apt.emulab.net   Ready    control-plane   20m     v1.28.7
node1.hand32-194769.bayopsys-pg0.apt.emulab.net   Ready    <none>          5m11s   v1.28.7

hand32@node0:~/peakler/scripts$ kubectl get pods --all-namespaces
NAMESPACE          NAME                                                                      READY   STATUS    RESTARTS   AGE
calico-apiserver   calico-apiserver-cc54f8954-c2xsq                                          1/1     Running   0          17m
calico-apiserver   calico-apiserver-cc54f8954-x9z52                                          1/1     Running   0          17m
calico-system      calico-kube-controllers-84b78db484-52chl                                  1/1     Running   0          18m
calico-system      calico-node-5zn79                                                         1/1     Running   0          4m28s
calico-system      calico-node-f48nh                                                         1/1     Running   0          18m
calico-system      calico-typha-647b77865b-nc7bg                                             1/1     Running   0          18m
calico-system      csi-node-driver-cppqk                                                     2/2     Running   0          18m
calico-system      csi-node-driver-qwwkr                                                     2/2     Running   0          4m28s
kepler             kepler-exporter-pxplx                                                     1/1     Running   0          65s
kube-system        coredns-5dd5756b68-wj66d                                                  1/1     Running   0          19m
kube-system        coredns-5dd5756b68-xfqnn                                                  1/1     Running   0          19m
kube-system        etcd-node0.hand32-194769.bayopsys-pg0.apt.emulab.net                      1/1     Running   0          19m
kube-system        kube-apiserver-node0.hand32-194769.bayopsys-pg0.apt.emulab.net            1/1     Running   0          19m
kube-system        kube-controller-manager-node0.hand32-194769.bayopsys-pg0.apt.emulab.net   1/1     Running   0          19m
kube-system        kube-proxy-ch2cl                                                          1/1     Running   0          19m
kube-system        kube-proxy-hb9x9                                                          1/1     Running   0          4m28s
kube-system        kube-scheduler-node0.hand32-194769.bayopsys-pg0.apt.emulab.net            1/1     Running   0          19m
monitoring         alertmanager-main-0                                                       2/2     Running   0          2m52s
monitoring         alertmanager-main-1                                                       2/2     Running   0          2m52s
monitoring         alertmanager-main-2                                                       2/2     Running   0          2m52s
monitoring         blackbox-exporter-6cfc4bffb6-dwfv7                                        3/3     Running   0          4m4s
monitoring         grafana-748964b847-hjhmq                                                  1/1     Running   0          4m1s
monitoring         kube-state-metrics-6b4d48dcb4-f2gck                                       3/3     Running   0          4m
monitoring         node-exporter-5cwzb                                                       2/2     Running   0          3m59s
monitoring         node-exporter-ldh6b                                                       2/2     Running   0          3m59s
monitoring         prometheus-adapter-79c588b474-74wq2                                       1/1     Running   0          3m56s
monitoring         prometheus-adapter-79c588b474-z8hj7                                       1/1     Running   0          3m56s
monitoring         prometheus-k8s-0                                                          2/2     Running   0          2m49s
monitoring         prometheus-k8s-1                                                          2/2     Running   0          2m49s
monitoring         prometheus-operator-68f6c79f9d-xgww5                                      2/2     Running   0          3m55s
tigera-operator    tigera-operator-94d7f7696-98d9r                                           1/1     Running   0          19m
```

```
hand32@node1:~/peakler/experiments/kepler_idle/cloudlab_c6220$ tail -f /tmp/rapl.log
26.797348 12.443787
32.432541 13.110825
32.087128 13.332642
29.817871 13.169235
31.360489 13.404495
29.401367 12.877106
36.303665 14.323837
30.57869 12.928574
26.924622 12.40535
30.083267 12.85054
28.520142 12.719498
34.128021 13.526871
27.612671 12.54332
26.132004 12.174622
27.793701 12.659958
30.604462 12.972351
35.643372 14.02507
31.282455 13.233429
30.721191 13.095352
31.816025 13.289505
28.457443 12.640976
37.017273 13.888504
30.240906 13.192856
```