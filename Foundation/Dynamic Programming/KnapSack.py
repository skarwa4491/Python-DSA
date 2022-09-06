class Solution():
    def knapSack(self,values, weights,bag_weight):
        
        dp =[ [0 for _ in range(bag_weight+1)] for _ in range(len(values)+1)]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if j>=weights[i-1]:
                    dp[i][j]=max(dp[i-1][j],(dp[i-1][j-weights[i-1]] + values[i-1]))
        return dp[len(dp)-1][len(dp[0])-1]
                         
                    
n = int(input())
#values = [ int(input()) for _ in range(n)]
#weights = [ int(input()) for _ in range(n)]
values_input = input().split(" ")
values = [int(e) for e in values_input if e.isdigit()]
weight_input = input().split(" ")
weights = [int(e) for e in weight_input if e.isdigit()]
bag_weight = int(input())
print(Solution().knapSack(values,weights,bag_weight))