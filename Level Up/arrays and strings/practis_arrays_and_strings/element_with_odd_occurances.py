from unicodedata import numeric
from unittest import result


def solution(numbers):
    ''' find element with odd number of accourances'''
    map = dict()
    for number in numbers:
        map[number] = map.get(number, 0)+1

    result = list()
    for key, value in map.items():
        if value % 2 == 1 :
            result.append(key)
    print(result)
