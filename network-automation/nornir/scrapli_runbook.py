import time
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_command, send_commands, send_commands_from_file
from nornir_scrapli.tasks import send_config, send_configs, send_configs_from_file

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

def scrapli_show(task):
    task.run(task=send_command, command="show clock")
    task.run(task=send_commands, commands=show_cmd_list)
    task.run(task=send_commands_from_file, file="file123.txt")

def scrapli_cfg(task):
    task.run(task=send_config, config="do show clock")
    task.run(task=send_config, config=f"do show clock {task.host['ntp_server']}")
    task.run(task=send_configs, configs=cfg_cmd_list)
    task.run(task=send_configs_from_file, file="file123.txt")

quit()

show_output = nr.run(task=scrapli_show)
print_result(show_output)

cfg_output = nr.run(task=scrapli_cfg)
print_result(cfg_output)

# - Print how long it took to execute script
print("\n---\nExecution time:", time.time()-start, "\n")

# Author: Daniel Arapi
# Updated: 08/19/21
