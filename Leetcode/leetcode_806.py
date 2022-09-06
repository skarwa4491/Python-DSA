class Solution:
    def numberOfLines(self, widths, s):
        lines = 1
        total = 0
        for c in s:
            total += widths[ord(c) - 97]
            if total > 100:
                lines += 1
                total = widths[ord(c) - 97]
        return [lines, total]


print(Solution().numberOfLines(widths=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                               s="abcdefghijklmnopqrstuvwxyz"))
