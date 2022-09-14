


# arr = [4,3,1,5,9]. sum = 14 
# o/p = {1,3}
# should be done in O(n^2) and O(n)


# def solution(arr,target):
#     for i in range(len(arr)):
#         sum = arr[i]
#         for j in range(i+1, len(arr)):
#             sum += arr[j]
#             if sum == target:
#                 return (i,j)

def optimized(arr, target):
    i = 0
    j = i
    sum = 0
    while j < len(arr):
        if sum == target:
            return (i,j)
        
        elif sum > target:
            if i < len(arr)-1:
                i+=1
                j=i
                sum = arr[j]
        sum+=arr[j]
        j+=1
        

# arr = [4,3,1,5,9]
# target = 3
# print(optimized(arr,target))      


# str ="abbcaaccb"
# o/p = "aaabbbccc"
# should be done in O(1) space

def solution(s):
    
    s_char = [c for c in s]
    i = 0
    j = 0
    k = len(s_char)-1
    while i < k:
        
        if s_char[i] == 'a':
            s_char[i],s_char[j] = s_char[j],s_char[i]
            i+=1
            j+=1
            
        elif s_char[i] == 'b':
             i+=1
            
        elif s_char[i] == 'c':
            s_char[i],s_char[k] = s_char[k],s_char[i]
            k-=1
            
    return ''.join(s_char)

print(solution('abbcaaccb'))
        