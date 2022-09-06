"""_summary_
find next greater element to left , in form of index
and mark the differnce  from current to next greater to right

# incomplete
"""

def find_span_backward(arr):
    # next greater element to left
    span = [-1] * len(arr)
    span[0] = 1
    stack = [0]
    for i in range(1, len(arr)):
        while len(stack) > 0 and arr[i] >= arr[stack[-1]]:
            stack.pop()
        if len(stack) > 0:
            span[i] = i-stack[-1]
        else:
            span[i] = i+1
        stack.append(i)
    print(span)


arr = [2, 5, 9, 3, 1, 12, 6, 8, 7]
print(arr)
print(find_span_backward(arr), 'right to left traversal')
