import sys

l = [10,3,6,7,4,7,2,12,9,7]
prev = sys.maxsize
result = [[prev]]

for num in l:
    ans = result[-1][-1]
    prev_list = result[-1]
    if num < ans:
        ans = list()
        ans.append(num)
        result.append(ans)
    elif num > ans:
        prev_list.append(num)
        result[-1]= prev_list
        
print(result[1:])