import sys
class Solution():
    """_summary_
    
    1. You are given a number n, representing the number of rows.
    2. You are given a number m, representing the number of columns.
    3. You are given n*m numbers, representing elements of 2d array a, which represents a gold mine.
    4. You are standing in front of left wall and are supposed to dig to the right wall. You can start from 
     any row in the left wall.
    5. You are allowed to move 1 cell right-up (d1), 1 cell right (d2) or 1 cell right-down(d3).
    """
    def find_max_gold(self,gold_bag):
        dp = [[0 for _ in gold] for gold in gold_bag]
        j = len(dp[0])-1
        while j>=0:
            i = len(dp)-1
            while i>=0:
                if j == len(dp[0])-1:
                    dp[i][j]=gold_bag[i][j]
                elif i==0:
                    dp[i][j]=gold_bag[i][j]+max(dp[i][j+1],dp[i+1][j+1])
                elif i==len(dp)-1:
                    dp[i][j]=gold_bag[i][j]+max(dp[i-1][j+1],dp[i][j+1])
                else:
                    dp[i][j] = gold_bag[i][j] + max(dp[i][j+1],dp[i-1][j+1],dp[i+1][j+1])
                i =i-1
            j=j-1
            
        maxi = sys.maxsize*-1
        i=len(dp)-1
        while i>=0:
            if maxi < dp[i][0]:
                maxi = dp[i][0]
            i =i-1
        return maxi

n = int(input())
m = int(input())

gold_bag = []    
for i in range(0, n):
    ar = []
    l = input()
    for j in range(0, m):
        lst = l.split(" ")
        val = int(lst[j])
        ar.append(val)
    gold_bag.append(ar)
    
print(Solution().find_max_gold(gold_bag))
    