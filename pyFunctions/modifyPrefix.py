#!/usr/bin/env python3


import yaml
import ipaddress

currentPrefix = "pyFunctions/currentPrefixList.yaml"
prefixList = "stophelpPrefixes.yaml"
prefixList = []

with open(currentPrefix, 'r') as xfile:
    xList = yaml.safe_load(xfile)

# print (xList[0]['prefix_lists'])
     
for x in xList[0]['prefix_lists']:
    name = x['name']
    if name == "CNX_ROUTES_TO_STOPHELP":
        for z in x['entries']:
            print (z['prefix'])
