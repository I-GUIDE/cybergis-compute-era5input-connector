#!/bin/env python3

import yaml
import os

connector_dict = {'$1': {'Input': {'Era5Input': 
                                     {'dataset': os.environ['param_dataset'], 
                                      'format': os.environ['param_format'], 
                                      'region': os.environ['param_region'],
                                      'origin': os.environ['param_origin'],
                                      'variable': os.environ['param_variable'],
                                      'time_aggregation': os.environ['param_time_aggregation'],
                                      'horizontal_aggregation': os.environ['param_horizontal_aggregation'],
                                      'year': os.environ['param_year'].split(','),
                                      'version': os.environ['param_version'],
                                      'uid':os.environ['param_uid'],
                                      'api_key':os.environ['param_api_key']}}}}

with open('/job/executable/era5input.yml','w') as era5file:
    yaml.dump(connector_dict,era5file)
