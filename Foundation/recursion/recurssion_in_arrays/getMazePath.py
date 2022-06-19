import sys
sys.setrecursionlimit(10**6)
class Solution():
    """_summary_
            1. You are given a number n and a number m representing number of rows and columns in a maze.
            2. You are standing in the top-left corner and have to reach the bottom-right corner. 
            3. Only two moves are allowed 'h' (1-step horizontal) and 'v' (1-step vertical).
            4. Complete the body of getMazePath function - without changing signature - to get the list of all paths that can be used to move from top-left to bottom-right.
               Use sample input and output to take idea about output.

            Note -> The online judge can't force you to write the function recursively but that is what the spirit of question is. Write recursive and not iterative logic. The purpose of the question is to aid learning recursion and not test you.  
    """
    def findPath(self, sr, sc ,dr,dc):
        if sr == dr or sc ==dc:
            return []
        if sr==dr-1 and sc==dc-1:
            return [""]
        
        vpaths = self.findPath(sr+1,sc,dr,dc )
        hpaths = self.findPath(sr,sc+1,dr,dc)
        paths = ["h"+trace for trace in hpaths]
        [paths.append("v"+trace) for trace in vpaths]
        paths.sort()
        return paths

        
    
n = int(input())
m = int(input())
result = Solution().findPath(0,0,n,m)
print(result)