class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n==1:
            return 0
        x  = self.findTheWinner(n-1,k)
        y = (x+k)%n
        return y

print(Solution().findTheWinner(5,2))