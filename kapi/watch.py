import logging

from kubernetes import client, config, watch
from kubernetes.client import ApiException, V1Deployment, V1ContainerImage

# Configs can be set in Configuration class directly or using helper
# utility. If no argument provided, the config will be loaded from
# default location.
config.load_kube_config()
#config.load_incluster_config()
v1 = client.CoreV1Api()
appsapi = client.AppsV1Api()
w = watch.Watch()

#logger = logging.getLogger('k8s_events')
#logger.setLevel(logging.DEBUG)

# Listing the cluster nodes
node_list = v1.list_node()
for node in node_list.items:
    node = node.metadata.name
    print(node)

ret = v1.list_namespaced_pod(namespace="default", watch=False)
for pod in ret.items:
    if 'frontend' in pod.metadata.name:
        #print(pod)
        print(f"Name: {pod.metadata.name}\n\tNamespace: {pod.metadata.namespace}\n\tIP: {pod.status.pod_ip}\n\tNode: {pod.spec.node_name}")
        #body = {"spec": {"replicas": 2, "nodeName": "server5.hand32-211847.bayopsys-pg0.wisc.cloudlab.us"}}
        #body = {"spec": {"nodeName": "server5.hand32-211847.bayopsys-pg0.wisc.cloudlab.us"}}
        body = {"spec":{"template":{"spec":{"nodeName": "server5.hand32-211847.bayopsys-pg0.wisc.cloudlab.us"}}}}
        try:
            #appsapi.patch_namespaced_deployment_scale("root--frontend", namespace="default", body=body)
            appsapi.patch_namespaced_deployment("root--frontend", namespace="default", body=body)
        except ApiException as e:
            print("Failed to scale {pod.metadata.name}")
            raise e
#for event in w.stream(v1.list_pod_for_all_namespaces):
#    logger.info("Event: %s %s %s" % (event['type'], event['object'].kind, event['object'].metadata.name))
#    if event['type'] == 'ADDED' and event['object'].kind == 'Pod':
#        event['object'].spec.node_name = node
#    print("Event: %s %s %s %s" % (event['type'], event['object'].kind, event['object'].metadata.name, event['object'].spec.node_name))
    
