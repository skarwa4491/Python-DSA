class Solution:
    def minSwaps(self, s: str) -> int:
        total_count_1 = s.count('1')
        total_count_0 = s.count('0')

        if abs(total_count_1-total_count_0) > 1:
            return -1

        even_1, even_0 = 0, 0
        odd_1, odd_0 = 0, 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '1':
                    even_1 += 1
                else:
                    even_0 += 1
            else:
                if s[i] == '0':
                    odd_0 += 1
                else:
                    odd_1 += 1
        min_1 = min(even_1, odd_1)
        min_0 = min(odd_1, odd_0)

        min_swaps = min(min_1, min_0)
        return min_swaps

print(Solution().minSwaps('100'))
