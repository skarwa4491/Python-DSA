
# Complete the 'getMergedIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def getMergedIntervals(intervals):
    # Write your code here
    intervals.sort(key=lambda a: a[0])
    print(intervals)
    stack = []
    for i in range(len(intervals)):
        if i ==0:
            stack.append(intervals[i])
        else:
            top = stack [-1]
            if(intervals[i][0] > top[1]):
                stack.append(intervals[i])
            else:
                top[1] = max(intervals[i][1],top[1])
                stack[-1] = top
    return stack
        

if __name__ == '__main__':

    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = getMergedIntervals(intervals)
    print(result)
