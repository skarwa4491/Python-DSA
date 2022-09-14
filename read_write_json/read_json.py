import json
import os
from pprint import pprint


def read_data(data , tab):
    for key,val in data.items():
        if isinstance(val,dict):
            tab+='\t'
            print(key, end="")
            read_data(val,tab)
        else:
            print(tab,key,":",val)
        
with open(os.getcwd()+'/read_write_json/sample.json','r') as f:
    data_string = f.read()
    data = json.loads(data_string)
    print()
    pprint(data)
    