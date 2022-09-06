"""_summary_
    for an array elements are not guranted with certail range
    for a given array, partation the array in such a way that , when 
each partation is sorted , complete array should be sorted
return the number of partation

sample input = [2,0,1,3,5,4]
partation on 2 and 3rd index
"""
import sys


class Solution():

    def get_max_chanks(self, arr):
        left_max = [0]*len(arr)
        right_min = [0]*len(arr)
        maxi = sys.maxsize * -1
        mini = sys.maxsize
        for i, val in enumerate(arr, start=0):
            maxi = max(maxi, val)
            left_max[i] = maxi

        for i in range(len(arr)-1, -1, -1):
            mini = min(mini, arr[i])
            right_min[i] = mini
        count = 0
        for i in range(len(left_max)-1):
            if left_max[i] >= right_min[i+1]:
                pass
            else:
                count += 1
        print(count)


Solution().get_max_chanks([30, 10, 20, 40, 60, 50, 75, 70])
