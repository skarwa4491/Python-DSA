'''
    1. You are given an array(arr) which contains only 0's and 1's and a number K.
    2. You have to find the maximum number of consecutive 1's in the given array if you can flip at most K zeroes.
'''


def max_consecutive_one(s, k):
    count = 0
    i = -1
    j = -1
    ans = 0
    while True:
        f1 = False
        f2 = False
        while i < len(s)-1 and count <= k:
            f1 = True
            i += 1
            ch = s[i]
            if ch == '0':
                count += 1

        while j < i:
            f2 = True
            j += 1
            ch = s[i]
            if ch == '0':
                count -= 1
            if count <= k:
                length = i-j
                if length > ans:
                    ans = length
        
        if not f1 and not f2:
            break
    print(ans)

s = '110011'
max_consecutive_one(s,1)