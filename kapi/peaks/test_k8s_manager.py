import logging

from k8s_manager import K8sManager
from logfolder_data_source import LogFolderDataSource
from wrk2_log_parser import WrkLogParser

HOTELRES_MICROSERVICES = ['consul', 'frontend', 'geo', 'jaeger',
                          'memcached-profile', 'memcached-rate',
                          'memcached-reserve',
                          'mongodb-geo', 'mongodb-profile', 'mongodb-rate',
                          'mongodb-recommendation', 'mongodb-reservation',
                          'mongodb-user', 'profile', 'rate', 'recommendation',
                          'reservation', 'search', 'user']

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)-6s | %(filename)-10s | %(funcName)-20s || %(message)s')

if __name__ == "__main__":
    k8sm = K8sManager()
    res = k8sm.get_cluster_resources()
    logger.info(f"Number of allocatable resources: {res} CPUs")
    logger.info(f"k8sm.all_pods_running(): {k8sm.all_pods_running()}")
