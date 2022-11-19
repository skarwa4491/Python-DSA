from unicodedata import numeric


def solution(arr):
    ''' for a given collection of numbers
        find a number which is more than 50% of a
        collection
    '''

    def get_candidate(arr):
        count = 0
        value = arr[0]
        i = 0
        while i < len(arr):
            if arr[i] == value:
                count += 1
            else:
                count -= 1
            if count == 0:
                count = 1
                value = arr[i]
            i += 1
        return value

    candiate = get_candidate(arr)
    count = 0
    for number in arr:
        if number == candiate:
            count+=1
    
    if count > len(arr)//2:
        return candiate
    else:
        return 0

arr = [1,3,1,3,3,3,1,2,2,3,3]
print(solution(arr))
