#!/usr/bin/python

import yaml

def Pairs_and_engine():
  # Get translation pair and preferred engine
  with open('config_files/mt-defaults.wikimedia.yaml') as filter:
    document = yaml.safe_load(filter)
    return document
