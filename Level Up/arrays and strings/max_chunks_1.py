"""
in an array of length n , all elements will be in range 0 to n-1

for a given array, partation the array in such a way that , when 
each partation is sorted , complete array should be sorted
return the number of partation

sample input = [2,0,1,3,5,4]
"""
import sys


class Solution():

    def get_max_chunks(self, list):
        maxi = sys.maxsize*-1
        count = 0
        for i, val in enumerate(list, start=0):
            maxi = max(maxi, val)
            if i == maxi:
                count += 1
        return count


print(Solution().get_max_chunks([2, 0, 1, 3, 5, 4]))
