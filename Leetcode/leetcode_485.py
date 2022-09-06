class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        count = 0
        max_count = 0
        for ch in nums:
            if ch == 0:
                if count >= max_count:
                    max_count = count
                count = 0

            else:
                count += 1
        return max(count, max_count)


print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1,1,1]))
