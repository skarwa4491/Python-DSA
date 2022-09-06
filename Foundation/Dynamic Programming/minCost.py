from typing import List


class Solution():
    def find_min_cost(self, costs: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(costs[0]))] for _ in range(len(costs))]
        i = len(costs)-1
        while i >= 0:
            j = len(costs[i])-1
            while j >= 0:
                if i == len(costs)-1 and j == len(costs[0])-1:
                    dp[i][j] = costs[i][j]
                elif(j == len(costs[0])-1):
                    dp[i][j] = costs[i][j]+dp[i+1][j]
                elif(i == len(costs)-1):
                    dp[i][j] = costs[i][j]+dp[i][j+1]
                else:
                    dp[i][j] = min(dp[i][j+1], dp[i+1][j]) + costs[i][j]
                j -= 1
            i -= 1
        return dp[0][0]


# n = int(input())
# m = int(input())
# costs = []
# for i in range(0, n):
#     ar = []
#     l = input()
#     for j in range(0, m):
#         lst = l.split(" ")
#         val = int(lst[j])
#         ar.append(val)
#         costs.append(ar)
costs = [[0, 1, 4, 2, 8, 2],
         [4, 3, 6, 5, 0, 4],
         [1, 2, 4, 1, 4, 6],
         [2, 0, 7, 3, 2, 2],
         [3, 1, 5, 9, 2, 4],
         [2, 7, 0, 8, 5, 1]]

print(Solution().find_min_cost(costs))
