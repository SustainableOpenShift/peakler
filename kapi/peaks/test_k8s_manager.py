import logging

from k8s_manager import K8sManager
from logfolder_data_source import LogFolderDataSource
from wrk2_log_parser import WrkLogParser

from subprocess import Popen, PIPE, call

HOTELRES_MICROSERVICES = ['consul', 'frontend', 'geo', 'jaeger',
                          'memcached-profile', 'memcached-rate',
                          'memcached-reserve',
                          'mongodb-geo', 'mongodb-profile', 'mongodb-rate',
                          'mongodb-recommendation', 'mongodb-reservation',
                          'mongodb-user', 'profile', 'rate', 'recommendation',
                          'reservation', 'search', 'user']

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)-6s | %(filename)-10s | %(funcName)-20s || %(message)s')

server_to_ip = {
    "server2.hand32-213139.bayopsys-pg0.wisc.cloudlab.us" : "192.168.1.2",
    "server3.hand32-213139.bayopsys-pg0.wisc.cloudlab.us" : "192.168.1.3",
    "server4.hand32-213139.bayopsys-pg0.wisc.cloudlab.us" : "192.168.1.4",
    "server5.hand32-213139.bayopsys-pg0.wisc.cloudlab.us" : "192.168.1.5",
    "server6.hand32-213139.bayopsys-pg0.wisc.cloudlab.us" : "192.168.1.6",
    "server7.hand32-213139.bayopsys-pg0.wisc.cloudlab.us" : "192.168.1.7"
}

def runRemoteCommandGet(com, server):
    logger.info(f"ssh hand32@{server} {com}")
    p1 = Popen(["ssh", "hand32@"+server, com], stdout=PIPE)
    return p1.communicate()[0].strip()

if __name__ == "__main__":
    k8sm = K8sManager()
    res = k8sm.get_cluster_resources()
    logger.info(f"Number of allocatable resources: {res} CPUs")
    logger.info(f"k8sm.all_pods_running(): {k8sm.all_pods_running()}")

    print(k8sm.get_nodes(spec="server"))
    ret = runRemoteCommandGet("tail -n 10 ~/perf.server2.hand32-213139.bayopsys-pg0.wisc.cloudlab.us.log", "192.168.1.2")
    for line in str(ret).strip().split("\\n"):
        print(float(line.strip().split(",")[1]))
    
