import json

f = open('response.json')
data = json.load(f)

eligilbe_keys = ['first_name','last_name','email']
optional_keys  =[ 'age', 'gender']

for key in data.keys():
    if key == 'user_profile':
        user_data = data[key]
        for user_key in user_data.keys():
            if user_key in eligilbe_keys:
                print('valid keys')
                assert user_data[user_key] == 'Swapnil'
            else:
                print('error mandit key is not present')
