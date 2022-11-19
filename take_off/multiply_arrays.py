'''
    100
    111
    
    100
    1000 --> 1100
    10000 --> 11100
    
'''
def solution(arr1, arr2):
    if len(arr2) > len(arr1):
        arr2, arr1 = arr1, arr2  # manage inputs

    j = len(arr2)-1
    results = list()
    carry = 0
    while j >= 0:
        result = list()
        for i in range(len(arr2)-1-j):
            result.insert(0,0)
            
        i = len(arr1)-1
        while i >= 0:
            digit = (arr2[j]*arr1[i])+carry
            if digit > 9:
                carry = digit//10
                digit = digit % 10
            else:
                carry = 0
            result.insert(0,digit)
            i-=1
        if carry != 0:
            result.insert(0,carry)
        result = [ str(_) for _ in result]
        results.append(int(''.join(result)))
        carry = 0
        j-=1
    
    print(sum(results))
    
solution([1,2],[1,2])