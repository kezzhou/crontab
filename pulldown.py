#### Imports ####
import os
import sys
import time
import requests as rq ## pull api from web
import json ## for visualization
import pandas as pd



#### pulling down data from an API ####

cwd = os.getcwd()

apiDataset = rq.get('https://data.cms.gov/data-api/v1/dataset/137f90cb-ac53-4b3d-8358-e65cf64e03d3/data') ## we bring in public cms json api with requests and the appropriate url

apiDataset = apiDataset.json() ## we then use json package to visualize api dataset for us

apiDataset = pd.DataFrame(apiDataset)

apiDataset.to_csv('./covidnursingdata.csv')

data = apiDataset

now = time.time() ## getting current time 

nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now)) ## saving as string

with open(cwd + '/pulldown_' + nowStr + '.txt', 'w') as f:
    f.write(str(data)) ## creating new file