import json
import os

with open(os.getcwd()+'/read_write_json/sample.json','r') as f:
    data = json.load(f)
    print(data , type(data))
    jsn = json.dumps(data)
    print('___________________')
    print(jsn)

print(os.getcwd())