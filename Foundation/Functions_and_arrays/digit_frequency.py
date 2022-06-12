"""
__Question__
1. You are given a number n.
2. You are given a digit d.
3. You are required to calculate the frequency of digit d in number n.

"""
number = int(input())
digit = int(input())


def find_frequency(number,digit):
    count =0
    while number != 0:
        d = number%10
        if d==digit:
            count+=1
        number = number//10
    
    return count

print(find_frequency(number,digit))