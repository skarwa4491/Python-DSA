a = {1: 'r', 2: 's', 3: 't', 4: 'u', 5: 'v', 6:'w', 7:'y'}
b = ['r', 's', 'p', 't', 'u', 'v', 'w', 'x', 'y', 'z']

result = [ _ for _ in b if _ not in a.values()]
print(result)

a = [1, 2, 3, 2, 1, 4, 3, 5, 7, 6, 6,5, 7, 8, 9, 8, 9]
map = dict()

for _ in a:
    map[_] = map.get(_, 0)+1
print(map)
for key, value in map.items():
    if value == 1:
        print(key) 
        break

