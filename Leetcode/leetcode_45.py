class Solution:
    def jump(self, nums) -> int:
        dp =[0]*(len(nums))
        dp[-1] = 0
        i = len(nums)-2
        while i>=0:
            j=1
            minimum = len(nums)
            while j<=nums[i] and i+j <len(dp):
                if dp[i+j] >= 0:
                    minimum=min(minimum,dp[i+j])
                j+=1
            
            dp[i] = minimum + 1
            i-=1
        
        print(dp)
        return dp[0]
Solution().jump([2,3,1,1,4])