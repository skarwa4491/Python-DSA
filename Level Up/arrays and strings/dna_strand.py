def dnaComplement(s):
    # Write your code here
    ''' reverse a string and repalce all chars
    '''
    arr = [_ for _ in s]
    i = 0
    j = len(arr)-1
    while(i < j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    
    for i, val in enumerate(arr):
        if arr[i] == 'A':
            arr[i]= 'T'
        elif arr[i] == 'T':
            arr[i]= 'A'
        elif arr[i] == 'C':
            arr[i] = 'G'
        elif arr[i] == 'G':
            arr[i] = 'C'
    return ''.join(arr)


if __name__ == '__main__':

    s = input()

    result = dnaComplement(s)
    print(result)
