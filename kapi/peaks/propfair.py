import time
import logging
import json
import random
import math

import pandas as pd
import numpy as np

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

def distribute_value(total, num_items):
    # Calculate the base value each item gets
    base_value = total // num_items
    # Calculate the remainder which needs to be distributed
    remainder = total % num_items
    # Create a list with the base value for each item
    distribution = [base_value] * num_items
    # Distribute the remainder across the items
    for i in range(remainder):
        distribution[i] += 1
    return distribution

if __name__ == "__main__":
    k8sm = K8sManager()
    res = k8sm.get_cluster_resources()
    logger.info(f"Number of allocatable resources: {res} CPUs")
    logger.info(f"k8sm.all_pods_running(): {k8sm.all_pods_running()}")
    
    #dis = distribute_value(int(res), len(HOTELRES_MICROSERVICES))
    #i = 0
    #sumd = 0
    #for s in HOTELRES_MICROSERVICES:
    #    key = "root--"+s
    #    nAlloc = dis[i]        
    #    i += 1
    #    sumd = sumd + nAlloc
    k8sm.scale_deployment(name="root--consul", replicas=6)
    k8sm.scale_deployment(name="root--frontend", replicas=6)
    k8sm.scale_deployment(name="root--geo", replicas=6)
    k8sm.scale_deployment(name="root--jaeger", replicas=6)
    k8sm.scale_deployment(name="root--memcached-profile", replicas=6)
    k8sm.scale_deployment(name="root--memcached-rate", replicas=6)
    k8sm.scale_deployment(name="root--memcached-reserve", replicas=6)
    k8sm.scale_deployment(name="root--profile", replicas=6)
    k8sm.scale_deployment(name="root--rate", replicas=6)
    k8sm.scale_deployment(name="root--recommendation", replicas=6)
    k8sm.scale_deployment(name="root--reservation", replicas=6)
    k8sm.scale_deployment(name="root--search", replicas=6)
    k8sm.scale_deployment(name="root--user", replicas=6)
    
    k8sm.scale_deployment(name="root--mongodb-geo", replicas=3)
    k8sm.scale_deployment(name="root--mongodb-profile", replicas=3)
    k8sm.scale_deployment(name="root--mongodb-rate", replicas=3)
    k8sm.scale_deployment(name="root--mongodb-recommendation", replicas=3)
    k8sm.scale_deployment(name="root--mongodb-reservation", replicas=3)
    k8sm.scale_deployment(name="root--mongodb-user", replicas=3)

    #logger.info(f"Allocated total {sumd}")
