
import json
import pandas as pd
from pandas import json_normalize
from flatten_json import flatten 

with open('output.json') as data_file:
    with open('output.csv', 'w',newline='') as fp.
        for line in data_file:
        data = json.load(line) # load as json
f.close()   

flat_json = flatten(data) 
df = json_normalize(flat_json)  
df.to_csv('json-to-csv.csv', sep=',', encoding='utf-8')