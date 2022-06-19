import sys
sys.setrecursionlimit(10**6)
class Solution():
    """_summary_

        1. You are given a number n representing number of stairs in a staircase.
        2. You are standing at the bottom of staircase. You are allowed to climb 1 step, 2 steps or 3 steps in one move.
        3. Complete the body of getStairPaths function - without changing signature - to get the list of all paths that can be used to climb the staircase up.
        Use sample input and output to take idea about output.
        Note -> The online judge can't force you to write the function recursively but that is what the spirit of question is. Write recursive and not iterative logic. The purpose of the question is to aid learning recursion and not test you.
    """
    def getPath(self,n):
        if n==0:
            return [""]
        if n<0:
            return []
        
        p1 = self.getPath(n-1)
        p2 = self.getPath(n-2)
        p3 = self.getPath(n-3)
        paths = ["1"+path for path in p1]
        [paths.append("2"+path) for path in p2]
        [paths.append("3"+path) for path in p3]
        return paths
        

stairs = int(input())  
result = Solution().getPath(stairs)
result = [int(path) for path in result]
print(result)
    