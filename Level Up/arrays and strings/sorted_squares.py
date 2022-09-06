class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        i = 0
        j = len(nums)-1
        result = [0]*len(nums)
        index = len(nums)-1

        while(i <= j):
            if (abs(nums[i]) >= abs(nums[j])):
                result[index] = nums[i] * nums[i]
                i += 1
                index -= 1
            else:
                result[index] = nums[j]*nums[j]
                j -= 1
                index -= 1
        return result
