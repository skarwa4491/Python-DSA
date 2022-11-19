import sys
class Solution:
    '''
        leet code 152
        for a given array , return max product of sub array
    '''
    def maxProduct(self, nums):
        product = 1
        ans = -sys.maxsize
        for num in nums:
            product *= num
            if product > ans:
                ans = product
            if product == 0:
                product = 1
        product = 1
        for num in reversed(nums):
            product *= num
            if product > ans:
                ans = product
            if product == 0:
                product = 1
        return ans