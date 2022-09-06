from enum import Flag
from select import kevent
from tracemalloc import start


def find_itenary(tours):
    itenaries = {tour[0]: tour[1] for tour in tours}
    start_point = dict()
    for tour in tours:
        if tour[0] not in start_point.keys():
            start_point[tour[0]] = True
        else:
            start_point[tour[0]] = False
        start_point[tour[1]] = False
    keys = list(start_point.keys())
    point = list(start_point.values()).index(True)
    start = keys[point]
    destination = itenaries[start]
    result = start +'----->'
    while destination in itenaries.keys():
        result += destination +'---->'
        destination = itenaries[destination]
    
    result += destination
    print(result)
        


tours = [['chennai', 'banglore'],
         ['bombay', 'delhi'],
         ['goa', 'chennai'],
         ['delhi', 'goa']]
find_itenary(tours)
