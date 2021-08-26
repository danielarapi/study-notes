import time
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get, napalm_ping


start = time.time()

nr = InitNornir(config_file="config.yaml")

def napalm_show(task):
    task.run(task=napalm_get, getters=["get_facts", "get_environment", "get_interfaces"])

def napalm_ping_test(task):
    task.run(task=napalm_ping, dest="10.28.220.5")


##show_output = nr.run(task=napalm_show)
##print_result(show_output)

ping_output = nr.run(task=napalm_ping_test)
print_result(ping_output)

# - Print how long it took to execute script
print("\n---\nExecution time:", time.time()-start, "\n")

# Author: Daniel Arapi
# Updated: 08/19/21
