import time
import logging
import json
import random
import math

import pandas as pd
import numpy as np

from ax.service.ax_client import AxClient, ObjectiveProperties
from ax.modelbridge.generation_strategy import GenerationStrategy, GenerationStep
from ax.modelbridge.registry import Models
from ax.service.utils.report_utils import exp_to_df

from k8s_manager import K8sManager
from logfolder_data_source import LogFolderDataSource
from wrk2_log_parser import WrkLogParser

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(message)s')

HOTELRES_MICROSERVICES = ['consul', 'frontend', 'geo', 'jaeger',
                          'memcached-profile', 'memcached-rate',
                          'memcached-reserve',
                          'mongodb-geo', 'mongodb-profile', 'mongodb-rate',
                          'mongodb-recommendation', 'mongodb-reservation',
                          'mongodb-user', 'profile', 'rate', 'recommendation',
                          'reservation', 'search', 'user']

if __name__ == "__main__":
    k8sm = K8sManager()
    #k8sm.list_pods()
    res = k8sm.get_cluster_resources()
    logger.info(f"k8sm.get_cluster_resources() {res}")
    #logger.info(f"k8sm.all_pods_running(): {k8sm.all_pods_running()}")

    ax_client = AxClient.load_from_json_file("ax_client_snapshot3.json")
    df = exp_to_df(ax_client.experiment)
    ndf = df[df.trial_index == 215]
    print('p99:', ndf['peaksp99'].iloc[0], 'power:', ndf['peakspwr'].iloc[0])
    params = {}
    for col in ndf.columns:
        if 'root--' in col:
            params[col] = ndf[col].iloc[0]

    numAllocs = 0
    arrNodes = []
    for s in HOTELRES_MICROSERVICES:
        k = 'root--'+s
        kn = 'root--'+s+'-node'
        nAlloc = round(params[k])
        nNode = params[kn]
        arrNodes.append(nNode)
        logger.info(f"Scaling {k} to {nAlloc} replicas all running on {nNode}")
        k8sm.scale_deployment_node(name=k, replicas=nAlloc, node=nNode)        
        numAllocs = numAllocs + nAlloc
    uniqNodes = set(arrNodes)        
    logger.info(f"Total {numAllocs} allocations.")    
    logger.info(f"Unique nodes: {sort(uniqNodes)}")
