# Idle Power w/ k8s calico and 2 node cluster
```
hand32@node0:~/peakler/experiments/kepler_idle/cloudlab_c220g1$ kubectl get pods --all-namespaces
NAMESPACE          NAME                                                                        READY   STATUS    RESTARTS   AGE
calico-apiserver   calico-apiserver-d84fb9f8c-9rf6p                                            1/1     Running   0          88m
calico-apiserver   calico-apiserver-d84fb9f8c-f9jg8                                            1/1     Running   0          88m
calico-system      calico-kube-controllers-5d5568595b-f2vp4                                    1/1     Running   0          89m
calico-system      calico-node-h7wvd                                                           1/1     Running   0          6m16s
calico-system      calico-node-v2v8t                                                           1/1     Running   0          89m
calico-system      calico-typha-7dfcbcf87-84jgl                                                1/1     Running   0          89m
calico-system      csi-node-driver-5js7q                                                       2/2     Running   0          6m16s
calico-system      csi-node-driver-xwwkq                                                       2/2     Running   0          89m
kube-system        coredns-5dd5756b68-6474j                                                    1/1     Running   0          89m
kube-system        coredns-5dd5756b68-gnbgl                                                    1/1     Running   0          89m
kube-system        etcd-node0.hand32-216770.bayopsys-pg0.wisc.cloudlab.us                      1/1     Running   0          89m
kube-system        kube-apiserver-node0.hand32-216770.bayopsys-pg0.wisc.cloudlab.us            1/1     Running   0          89m
kube-system        kube-controller-manager-node0.hand32-216770.bayopsys-pg0.wisc.cloudlab.us   1/1     Running   0          89m
kube-system        kube-proxy-57sdd                                                            1/1     Running   0          6m16s
kube-system        kube-proxy-gjt86                                                            1/1     Running   0          89m
kube-system        kube-scheduler-node0.hand32-216770.bayopsys-pg0.wisc.cloudlab.us            1/1     Running   0          89m
tigera-operator    tigera-operator-94d7f7696-4brl7                                             1/1     Running   0          89m
hand32@node0:~/peakler/experiments/kepler_idle/cloudlab_c220g1$ kubectl get nodes
NAME                                                STATUS   ROLES           AGE     VERSION
node0.hand32-216770.bayopsys-pg0.wisc.cloudlab.us   Ready    control-plane   90m     v1.28.13
node1.hand32-216770.bayopsys-pg0.wisc.cloudlab.us   Ready    <none>          6m33s   v1.28.13


hand32@node0:~/peakler/experiments/kepler_idle/cloudlab_c220g1$ perf stat -a -e power/energy-pkg/ -x, -I 1000 sleep 30
     1.001048308,19.63,Joules,power/energy-pkg/,2002406532,100.00,,
     2.002369058,19.41,Joules,power/energy-pkg/,2002617705,100.00,,
     3.003657679,19.70,Joules,power/energy-pkg/,2002496823,100.00,,
     4.004397295,20.51,Joules,power/energy-pkg/,2001466651,100.00,,
     5.005371945,19.62,Joules,power/energy-pkg/,2001956212,100.00,,
     6.006690093,19.83,Joules,power/energy-pkg/,2002571112,100.00,,
     7.007981444,19.78,Joules,power/energy-pkg/,2002540608,100.00,,
     8.009255185,19.98,Joules,power/energy-pkg/,2002549310,100.00,,
     9.010173328,20.63,Joules,power/energy-pkg/,2001809675,100.00,,
    10.011539065,20.24,Joules,power/energy-pkg/,2002666685,100.00,,
    11.012863271,19.41,Joules,power/energy-pkg/,2002600098,100.00,,
    12.014159193,19.62,Joules,power/energy-pkg/,2002553640,100.00,,
    13.015467568,19.40,Joules,power/energy-pkg/,2002564616,100.00,,
    14.016397996,20.38,Joules,power/energy-pkg/,2001757310,100.00,,
    15.017684136,19.52,Joules,power/energy-pkg/,2002537085,100.00,,
    16.018938023,19.38,Joules,power/energy-pkg/,2002538156,100.00,,
    17.020244105,19.16,Joules,power/energy-pkg/,2002660434,100.00,,
    18.021605628,18.93,Joules,power/energy-pkg/,2002574333,100.00,,
    19.021995538,20.25,Joules,power/energy-pkg/,2000776440,100.00,,
    20.023328610,20.47,Joules,power/energy-pkg/,2002664420,100.00,,
    21.024695105,19.91,Joules,power/energy-pkg/,2002629957,100.00,,
    22.025853034,19.56,Joules,power/energy-pkg/,2002270636,100.00,,
    23.027145425,19.83,Joules,power/energy-pkg/,2002473497,100.00,,
    24.028397601,20.65,Joules,power/energy-pkg/,2002512718,100.00,,
    25.029700228,19.92,Joules,power/energy-pkg/,2002585670,100.00,,
    26.030977720,19.63,Joules,power/energy-pkg/,2002498120,100.00,,
    27.032243335,19.58,Joules,power/energy-pkg/,2002534568,100.00,,
    28.033536050,19.76,Joules,power/energy-pkg/,2002529044,100.00,,
    29.034832776,20.81,Joules,power/energy-pkg/,2002576147,100.00,,
    30.001688646,19.61,Joules,power/energy-pkg/,1933622135,100.00,,
```