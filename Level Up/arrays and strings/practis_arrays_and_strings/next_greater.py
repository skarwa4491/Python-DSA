import difflib
from unicodedata import digit


def solution(number):
    '''
        you are given a number , find next greater number with same digits
    '''
    digits = [int(_) for _ in number]
    
    i = len(digits)-1
    si = None
    while i > 0:
        if digits[i-1] < digits[i]:
            si = i-1
            break
        i-=1
    if si is None:
        return "Number can't be formed"
    min_index = None
    for i in range(len(digits)-1,si,-1):
        if digits[i] > digits[si]:
            min_index = i
            break
    digits[si], digits[min_index] = digits[min_index],digits[si]
    digits[si+1:] = sorted(digits[si+1:])
    digits = [str(_) for _ in digits]
    return ''.join(digits)

print(solution('321'))
        
    