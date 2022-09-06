class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr = 0, 1
        count = 0
        i = 1
        while(i < len(s)):
            if s[i-1] != s[i]:
                count += min(curr, prev)
                curr = 1
                prev = curr
            else:
                curr += 1
            i += 1
        count += min(curr, prev)
        return count
