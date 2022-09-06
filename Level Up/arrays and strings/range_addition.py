class Solution():
    '''
        1. Assume you have an array of length 'n' initialized with all 0's and are given 'q' queries to update.
        2. Each query is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
        3. Return the modified array after all 'q' queries were executed.
    '''
    def add_range_querries_bf(self, n, lists):
        arr = [0]*n+1
        for lst in lists:
            for i in range(lst[0], lst[1]+1):
                arr[i] += lst[2]

        print(arr)

    def add_range_querries_o_n(self, n, lists):
        arr = [0]*(n+1)
        for lst in lists:
            arr[lst[0]] += lst[2]
            arr[lst[1]+1] += lst[2]*-1
        sum = 0
        for i, n in enumerate(arr):
            sum += n
            arr[i] = sum
        print(arr[:-1])


Solution().add_range_querries_o_n(5, [
    [1, 3, 2],
    [2, 4, 3],
    [0, 2, -2]
])
