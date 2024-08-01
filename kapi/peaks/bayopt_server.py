import time
import logging
import json

import pandas as pd
import numpy as np

from ax.service.ax_client import AxClient, ObjectiveProperties
from ax.modelbridge.generation_strategy import GenerationStrategy, GenerationStep
from ax.modelbridge.registry import Models

#from k8s_manager import K8sManager
#from logfolder_data_source import LogFolderDataSource
#from wrk2_log_parser import WrkLogParser

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s| %(filename)-10s | %(funcName)-20s || %(message)s')

HOTELRES_MICROSERVICES = ['consul', 'frontend', 'geo', 'jaeger',
                          'memcached-profile', 'memcached-rate',
                          'memcached-reserve',
                          'mongodb-geo', 'mongodb-profile', 'mongodb-rate',
                          'mongodb-recommendation', 'mongodb-reservation',
                          'mongodb-user', 'profile', 'rate', 'recommendation',
                          'reservation', 'search', 'user']

def checkValidParams(params):
    print(params)
    
def evalpeaks(pname):
    reward = 0.0
    res = {
        pname: (reward, 0.0)
    }
    return res

if __name__ == "__main__":
    #k8sm = K8sManager()
    #k8sm.list_pods()
    #res = k8sm.get_cluster_resources()
    #logger.info(f"k8sm.get_cluster_resources() {res}")
    #logger.info(f"k8sm.all_pods_running(): {k8sm.all_pods_running()}")

    #log_parser = WrkLogParser()
    #data_source = LogFolderDataSource(log_dir_path="/cilantrologs",
    #                                  log_parser=log_parser)

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
    ax_client = AxClient(generation_strategy=gs, enforce_sequential_optimization=False, verbose_logging=True)
    pname = "peaks"
    params = []
    cons = ""
    res=48.0
    for s in HOTELRES_MICROSERVICES:
        d = {}
        d['name'] = "root--"+s
        cons = cons + d['name']+" + "
        d['type'] = "range"
        d['value_type'] = "int"
        d['log_scale'] = False
        d['bounds'] = [1, int(res)-int(len(HOTELRES_MICROSERVICES))]
        params.append(d)
    cons = cons[:-2]+"<= "+str(int(res))
    print(cons)
    
    ax_client.create_experiment(
        name=pname,
        parameters=params,
        objectives={pname: ObjectiveProperties(minimize=True)},
        choose_generation_strategy_kwargs={"max_parallelism_override": 16},
        parameter_constraints=[cons],  # Optional.
    )

    for i in range(0, 2):
        parameterization, trial_index = ax_client.get_next_trial()
        checkValidParams(parameterization)
        #ax_client.log_trial_failure(trial_index=trial_index)
        #ax_client.complete_trial(trial_index=trial_index, raw_data=evalpeaks(pname))
            
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
            


    
    
