#!/usr/bin/env python3


#import yaml
#import ipaddress

prefixList = "stophelpPrefix.yaml"


with open(prefixList, 'r') as xfile:
    pList = yaml.safe_load(xfile)

seq = 0
fromPL = []
for x in pList['fromStophelp']:
    prefix = x['prefix']
    seq = seq + 5
    newPrefix = {"action": "permit", "prefix": prefix, "sequence": seq }
    fromPL.append(newPrefix)

seq = 0
toPL = []
for x in pList['toStophelp']:
    prefix = x['prefix']
    seq = seq + 5
    newPrefix = {"action": "permit", "prefix": prefix, "sequence": seq }
    toPL.append(newPrefix)

master = {"fromPL": fromPL, "toPL": toPL}

with open("pyFunctions/fromStophelpPy.yaml", "w") as f:
    f.write("---\n")
    yaml.dump(master, f)
    f.close

# print(fromPL)

# for x in pList['toStophelp']:
#     print(x['prefix'])
