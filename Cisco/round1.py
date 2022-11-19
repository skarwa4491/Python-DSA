s = 'each person is is unique the unique personality is on each person'

words = s.split(' ')
map = dict()

for word in words:
    map[word] = map.get(word,0)+1

for key,value in map.items():
    if value > 1:
        print(key,value)
        
