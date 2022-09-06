
def next_greater_element_to_right(arr):
    ngr = [-1]*len(arr)
    stack = [len(arr)-1]
    for i in range(len(arr)-2, -1, -1):
        while(len(stack) > 0 and arr[i] > arr[stack[-1]]):
            stack.pop()
        if len(stack) != 0:
            ngr[i] = arr[stack[-1]]
        stack.append(i)
    print(ngr)


def next_greater_element_to_left(arr):
    ngl = [-1]*len(arr)
    stack = [0]
    for i in range(1, len(arr)):
        while(len(stack) > 0 and arr[i] > arr[stack[-1]]):
            stack.pop()
        if len(stack) != 0:
            ngl[i] = arr[stack[-1]]
        stack.append(i)
    print(ngl)


def next_smaller_element_to_right(arr):
    nsr = [-1]*len(arr)
    stack = [len(arr)-1]
    for i in range(len(arr)-2, -1, -1):
        while(len(stack) > 0 and arr[i] < arr[stack[-1]]):
            stack.pop()
        if len(stack) != 0:
            nsr[i] = arr[stack[-1]]
        stack.append(i)
    print(nsr)


def next_smaller_element_to_left(arr):
    nsl = [-1]*len(arr)
    stack = [0]
    for i in range(1, len(arr)):
        while(len(stack) > 0 and arr[i] < arr[stack[-1]]):
            stack.pop()
        if(len(stack)) > 0:
            nsl[i] = arr[stack[-1]]
        stack.append(i)
    print(nsl)


next_greater_element_to_left([1,2,1])
