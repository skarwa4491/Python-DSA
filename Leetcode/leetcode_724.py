class Solution:
    def pivotIndex(self, nums):
        sum_left = [0]*len(nums)
        sum_right = [0]*len(nums)
        
        sum = 0
        for i in range(len(nums)):
            sum+=nums[i]
            sum_left[i]=sum

        sum = 0
        for i in range(len(nums)-1,-1,-1):
            sum+=nums[i]
            sum_right[i] = sum
            
        idx = 0
        if idx == 0 and sum_right[idx+1] == 0:
            return idx
        
        idx = len(nums)-1
        if idx == len(nums)-1 and sum_left[idx-1]==0:
            return idx
        
        print(sum_left)
        print(sum_right)
        for i in range(0,len(nums)-1):
            if sum_left[i-1] == sum_right[i+1]:
                return i
        
        return -1
                
print(Solution().pivotIndex([1,7,3,6,5,6]))