import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = collections.Counter(s)
        for i,char in enumerate(s):
            if map[char]==1:
                return i
        return -1

result = Solution().firstUniqChar("leetcode")
print(result)