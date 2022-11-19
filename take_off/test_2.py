from tracemalloc import start
from unittest import result


map = dict()
st = 'abcdefghijklmnopqrstuvwxyz'
map = {i: ch for i, ch in enumerate(st, start=1)}


def solution(number):
    if number <= 26:
        return map[number]
    else:
        # result = ''
        # base_char = number//26
        # reminder = number % 26
        # if base_char <= 26:
        #     if reminder == 0:
        #         result += map[base_char-1]
        #     else:
        #         result += map[base_char]
        # if reminder <= 26:
        #     if reminder == 0:
        #         result+=map[26]
        #     else:
        #         result+=map[reminder]
        # return result
        result = ''
        while number > 0:
            rem = number % 26
            if rem == 0:
                result+=(map[26])
                number = (number // 26) - 1
            else:
                result+=(map[rem])
                number = number//26
        print(result[::-1])

solution(705)
