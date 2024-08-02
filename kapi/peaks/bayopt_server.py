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

#logger = logging.getLogger(__name__)
#logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s| %(filename)-10s | %(funcName)-20s || %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# create file handler which logs even debug messages
fh = logging.FileHandler(f"bayopt_server.log")
fh.setLevel(logging.INFO)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)-10s | %(funcName)-20s || %(message)s',
                              datefmt='%m-%d %H:%M:%S')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

HOTELRES_MICROSERVICES = ['consul', 'frontend', 'geo', 'jaeger',
                          'memcached-profile', 'memcached-rate',
                          'memcached-reserve',
                          'mongodb-geo', 'mongodb-profile', 'mongodb-rate',
                          'mongodb-recommendation', 'mongodb-reservation',
                          'mongodb-user', 'profile', 'rate', 'recommendation',
                          'reservation', 'search', 'user']

def checkValidParams(params, res, k8sm):
    numAllocs = 0
    for key in params.keys():
        #nAlloc = int((params[key]*res))
        #nAlloc = int(params[key])
        nAlloc = round(params[key])
        numAllocs = numAllocs + nAlloc
        logger.info(f"Scaling {key}: {nAlloc} {params[key]}")
        k8sm.scale_deployment(name=key, replicas=nAlloc)
    logger.info(f"Sleeping 60 seconds for the new {numAllocs} allocations to settle.")
    time.sleep(60)
    return k8sm.all_pods_running()
    
def evalpeaks(pname, valid, data_source):
    logger.info(f"Sleeping 60 seconds for the hr-client to generate new files.")
    time.sleep(60)
    
    reward = 999999.0
    if valid == True:
        data = data_source.get_data()
        if data:
            jdata = json.loads(data["debug"])
            logger.info(f"p99 rewar: {jdata['p99']}")
            reward = jdata['p99']        
    
    res = {
        pname: (reward, 0.0)
    }
    return res

if __name__ == "__main__":
    k8sm = K8sManager()
    #k8sm.list_pods()
    res = k8sm.get_cluster_resources()
    logger.info(f"k8sm.get_cluster_resources() {res}")
    logger.info(f"k8sm.all_pods_running(): {k8sm.all_pods_running()}")

    log_parser = WrkLogParser()
    data_source = LogFolderDataSource(log_dir_path="/cilantrologs",
                                      log_parser=log_parser)

    model_kwargs={
        "seed": 999,
        "fallback_to_sample_polytope": True,
    }

    gs = GenerationStrategy(
        steps=[
            # 1. Initialization step (does not require pre-existing data and is well-suited for 
            # initial sampling of the search space)
            GenerationStep(
                model=Models.SOBOL,
                num_trials=5,  # How many trials should be produced from this generation step
                min_trials_observed=3, # How many trials need to be completed to move to next model
                max_parallelism=5,  # Max parallelism for this step
                model_kwargs={
                    "seed": 999,
                    "fallback_to_sample_polytope": True,
                },  # Any kwargs you want passed into the model
                model_gen_kwargs={},  # Any kwargs you want passed to `modelbridge.gen`
            ),
            # 2. Bayesian optimization step (requires data obtained from previous phase and learns
            # from all data available at the time of each new candidate generation call)
            GenerationStep(
                model=Models.GPEI,
                num_trials=-1,  # No limitation on how many trials should be produced from this step
                max_parallelism=3,  # Parallelism limit for this step, often lower than for Sobol
                # More on parallelism vs. required samples in BayesOpt:
                # https://ax.dev/docs/bayesopt.html#tradeoff-between-parallelism-and-total-number-of-trials
            ),
        ]
    )
    
    """ setup ax """
    #ax_client = AxClient(generation_strategy=gs, enforce_sequential_optimization=False, verbose_logging=True)
    ax_client = AxClient(generation_strategy=gs, enforce_sequential_optimization=False)
    pname = "peaks"
    params = []
    cons = ""
    for s in HOTELRES_MICROSERVICES:
        d = {}
        d['name'] = "root--"+s
        cons = cons + d['name']+" + "
        d['type'] = "range"
        #d['value_type'] = "float"
        d['value_type'] = "int"
        d['log_scale'] = False
        d['bounds'] = [1, int(res)-len(HOTELRES_MICROSERVICES)-1]
        #d['bounds'] = [1.0, res-len(HOTELRES_MICROSERVICES)-1.0]
        #d['bounds'] = [(1.0/res), (res-len(HOTELRES_MICROSERVICES))/res]
        params.append(d)
    #consl = cons[:-2]+"<= "+str(res)
    #consh = cons[:-2]+">= "+str(res-1)
    consl = cons[:-2]+"<= "+str(int(res))
    consh = cons[:-2]+">= "+str(int(res)-1)
    #consl = cons[:-2]+"<= 1.0"
    #consh = cons[:-2]+">= 0.98"
    #print(cons)
    
    ax_client.create_experiment(
        name=pname,
        parameters=params,
        objectives={pname: ObjectiveProperties(minimize=True)},
        choose_generation_strategy_kwargs={"max_parallelism_override": 16},
        #parameter_constraints=[cons],  # Optional.
        parameter_constraints=[consl, consh],  # Optional.
    )

    for i in range(0, 30):
        parameterization, trial_index = ax_client.get_next_trial()
        ret = checkValidParams(parameterization, res, k8sm)
        logger.info(f"checkValidParams: {ret}")
        if ret == False:
            ax_client.log_trial_failure(trial_index=trial_index)
        else:
            ax_client.complete_trial(trial_index=trial_index, raw_data=evalpeaks(pname, ret, data_source))
            
    """
    #logger.info("scaling..")
    #k8sm.scale_deployment(name="root--mongodb-recommendation", replicas=1)
    #k8sm.scale_deployment(name="root--mongodb-geo", replicas=1)
    #k8sm.scale_deployment(name="root--mongodb-profile", replicas=1)    
    #time.sleep(10)
    
    #print(k8sm.all_pods_running())

    while True:
        try:
          data = data_source.get_data()
        except StopIteration as e:
            logger.info(f"{str(e)}")
            break

        if data:
            jdata = json.loads(data["debug"])
            logger.info(jdata['p99'])
        time.sleep(1)
    """
            


    
    
