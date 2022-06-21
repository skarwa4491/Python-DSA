import sys
sys.setrecursionlimit(10**6)
class Solution():
    """_summary_

        1. You are given a number n, representing the count of elements.
        2. You are given n numbers.
        3. You are given a number "tar".
        4. Complete the body of printTargetSumSubsets function - without changing signature - to calculate and print all subsets of given elements, the contents of which sum to "tar". Use sample input and output to get more idea.
        Note -> The online judge can't force you to write the function recursively but that is what the spirit of question is. Write recursive and not iterative logic. The purpose of the question is to aid learning recursion and not test you.
    """
    
    def targetSum(self, arr, idx , target , sos,ans:list):
        if idx==len(arr):
            if sos==target:
                print(ans+".")
            return
        
        self.targetSum(arr,idx+1,target ,sos+arr[idx] , ans+str(arr[idx])+",")
        self.targetSum(arr,idx+1,target,sos,ans)

arr = [int(input()) for _ in range(int(input()))]
target = int(input())

Solution().targetSum(arr, 0, target ,0 , "")