import time
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
#from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_netmiko.tasks import *

start = time.time()

show_cmd_list = """
show clock
show clock
show clock
show clock
""".strip().splitlines()

cfg_cmd_list = """
do show clock
do show clock
do show clock
do show clock
""".strip().splitlines()

nr = InitNornir(config_file="config.yaml")

def netmiko_show(task):
    for cmd in show_cmd_list:
        task.run(task=netmiko_send_command, command_string=cmd)

def netmiko_cfg(task):
    task.run(task=netmiko_send_config, config_commands=cfg_cmd_list)
    task.run(task=netmiko_send_config, config_file="file123.txt")

quit()

show_output = nr.run(task=netmiko_show)
print_result(show_output)

cfg_output = nr.run(task=netmiko_cfg)
print_result(cfg_output)

# - Print how long it took to execute script
print("\n---\nExecution time:", time.time()-start, "\n")

# Author: Daniel Arapi
# Updated: 08/19/21
