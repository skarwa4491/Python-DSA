import numbers


def solution(number):
    '''
        for a given number, you can swap atmost only one digit
        and find max number formed if swapped
        
        leetcode 670
    '''
    right_max = list()
    number = [int(_) for _ in number]
    _max = len(number)-1
    for i in range(len(number)-1,-1,-1):
        if number[i]>number[_max]:
            _max = i
        right_max.insert(0,_max)
    print(number)
    for i in range(len(number)):
        if number[i] != 9 and number[i] < number[right_max[i]]:
            number[i],number[right_max[i]] = number[right_max[i]],number[i]
            break
    print(number)

solution('9987436294')