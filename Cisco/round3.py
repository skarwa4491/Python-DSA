arr1 = [3,2,1]
arr2 = [6,7,5]


def solution(arr1, arr2):
    arr1.sort()
    arr2.sort()
    result = list()
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+=1
        elif arr2[j] < arr1[i]:
            result.append(arr2[j])
            j+=1
        else:
            result.append(arr1[i])
            i+=1
            j+=1
    while i < len(arr1):
        result.append(arr1[i])
        i+=1
    while j < len(arr2):
        result.append(arr2[j])
        j+=1

    mid = len(result)//2
    if len(result) %2 == 0:
        num1 = result[mid-1]
        num2 = result[mid]
        return (num1+num2)//2
    else:
        return result[mid-1]

print(solution(arr1,arr2))
    