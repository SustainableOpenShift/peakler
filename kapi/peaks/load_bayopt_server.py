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

from k8s_manager import K8sManager
from logfolder_data_source import LogFolderDataSource
from wrk2_log_parser import WrkLogParser

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)-6s | %(filename)-10s | %(funcName)-20s || %(message)s')

if __name__ == "__main__":
    k8sm = K8sManager()
    #k8sm.list_pods()
    res = k8sm.get_cluster_resources()
    logger.info(f"k8sm.get_cluster_resources() {res}")
    logger.info(f"k8sm.all_pods_running(): {k8sm.all_pods_running()}")

    ax_client = AxClient.load_from_json_file()
    best_parameters, values = ax_client.get_best_parameters()
    
    #logger.info(f"ax best_parameters: {best_parameters}")
    tAllocs = 0
    for k, v in best_parameters.items():
        k8sm.scale_deployment(name=k, replicas=v)
        print(k, v)
        tAllocs = tAllocs + v
    print("total allocs", tAllocs)
