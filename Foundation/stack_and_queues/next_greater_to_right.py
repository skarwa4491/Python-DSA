from readline import read_init_file
from turtle import st


def next_greater_right(arr):
    # number based
    ngr = [-1]*len(arr)
    stack = []
    stack.append(arr[-1])
    for i in range(len(arr)-2, -1, -1):
        while(len(stack) > 0 and arr[i] > stack[-1]):
            stack.pop()
        if len(stack) != 0:
            ngr[i] = stack[-1]
        stack.append(arr[i])
    print(ngr)


def next_greater_alternate(arr):
    ngr = [-1]*len(arr)
    stack = []
    stack.append(0)
    for i in range(1, len(arr)):
        while len(stack) > 0 and arr[stack[-1]] < arr[i]:
            pos = stack[-1]
            ngr[pos] = arr[i]
            stack.pop()
        stack.append(i)
    print(ngr)

arr = [2, 5, 9, 3, 1, 12, 6, 8, 7]
print(arr)
#next_greater_right(arr)
next_greater_alternate(arr)
