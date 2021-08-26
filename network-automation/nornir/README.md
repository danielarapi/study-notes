# Setting up Nornir


- **Create a python 3 virutal environment with venv**
cd  
yum update -y  
python3 -m venv arapi-venv  
source arapi-venv/bin/activate  

- **Create a directory for Nornir**
cd  
mkdir Nornir-Automation  
cd Nornir-Automation  
touch config.yaml, groups.yaml, hosts.yaml, defaults.yaml, runbook1.py  


- **Install Nornir**
pip install --upgrade pip  
python3 -m pip install nornir  
python3 -m pip install nornir-scrapli  
pip freeze  

- **Order of Operations**
1. hosts.yaml  
2. groups.yaml  
3. defaults.yaml  


----------

## PLUGINS

Nornir only does two things:
- Inventory Management
- Concurrent Exectuion

Command execution are done through any of the following commands
- Scrapli
- Netmiko
- Napalm

```
python3 -m pip install nornir-utils
python3 -m pip install nornir_scrapli
python3 -m pip install nornir_netmiko
python3 -m pip install nornir_napalm
```
