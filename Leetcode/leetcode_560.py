class Solution:
    def subarraySum(self, nums, k):
        i = 0
        j = i
        count = 0
        sum = 0
        while j < len(nums):
            sum += nums[j]
            
            if sum == k:
                count+=1
            elif sum > k:
                if i < len(nums)-1:
                    i+=1
                    j=i
                    sum=nums[j]
                    if sum == k:
                        count+=1
            j+=1
            
        return count
            
Solution().subarraySum([-1,-1,1],0)