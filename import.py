
import json
import pandas as pd
from pandas import json_normalize
from flatten_json import flatten 

f = open('output.json', 'r+') # open the json file
data = json.load(f) # load as json
f.close()  

flat_json = flatten(data) 
df = json_normalize(flat_json)  
df.to_csv('json-to-csv.csv', sep=',', encoding='utf-8')
