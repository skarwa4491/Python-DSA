from traceback import print_tb


cities = list()
cities.append('Mumbai')
cities.append('Aurangabad')
cities.append('Pune')
cities.append('Goa')
cities.append('Delhi')

map = dict()
i = 0
for city in cities:
    current_length = len(city)
    map[current_length] = i
    i+=1

sorted_length = sorted(list(map.keys()))
result = [cities[map[key]]for key in sorted_length]

print(result)
