# Q1=answer
import json

with open('/Users/laptop-on-rent-011/Documents/DSA_Pyhton/palo alto networks/smaple.json', 'r') as f:
    json_data = json.load(f)
    idx = 1
    for question in json_data['questions']:
        print('Q'+str(idx) +'='+ question['answers'][question['correctIndex']])
        idx+=1