cities = list()
cities.append('Mumbai')
cities.append('Aurangabad')
cities.append('Pune')
cities.append('Goa')
cities.append('Delhi')

map = dict()

cities.sort(key = lambda a: len(a))
print(cities)