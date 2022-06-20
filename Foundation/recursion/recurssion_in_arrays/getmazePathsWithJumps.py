import sys
sys.setrecursionlimit(10**6)
class Solution():
    """
        1. You are given a number n and a number m representing number of rows and columns in a maze.
        2. You are standing in the top-left corner and have to reach the bottom-right corner. 
        3. In a single move you are allowed to jump 1 or more steps horizontally (as h1, h2, .. ), or 1 or more steps vertically (as v1, v2, ..) or 1 or more steps diagonally (as d1, d2, ..). 
        4. Complete the body of getMazePath function - without changing signature - to get the list of all paths that can be used to move from top-left to bottom-right.
        Use sample input and output to take idea about output.
        Note -> The online judge can't force you to write the function recursively but that is what the spirit of question is. Write recursive and not iterative logic. The purpose of the question is to aid learning recursion and not test you.
    """
    def getMazePath(self ,sr, sc, dr ,dc):
        if sr > dr or sc>dc :
            return []
        if sr == dr-1 and sc==dc-1 :
            return [""]
        
        v1paths  = self.getMazePath(sr+1,sc,dr,dc)
        v2paths  = self.getMazePath(sr+2,sc,dr,dc)
        v3paths = self.getMazePath(sr+3,sc,dr,dc)
        h1paths = self.getMazePath(sr,sc+1,dr,dc)
        h2paths = self.getMazePath(sr,sc+2,dr,dc)
        h3paths = self.getMazePath(sr,sc+3,dr,dc)
        d1paths = self.getMazePath(sr+1,sc+1,dr,dc)
        d2paths = self.getMazePath(sr+2,sc+2,dr,dc)
        d3paths = self.getMazePath(sr+3,sc+3,dr,dc)
        paths = []
        [paths.append("h1"+path) for path in h1paths]
        [paths.append("h2"+path) for path in h2paths]
        [paths.append("h3"+path) for path in h3paths]
        [paths.append("v1"+path) for path in v1paths]
        [paths.append("v2"+path) for path in v2paths]
        [paths.append("v3"+path) for path in v3paths]
        [paths.append("v3"+path) for path in v3paths]
        [paths.append("d1"+path) for path in d1paths]
        [paths.append("d2"+path) for path in d2paths]
        [paths.append("d3"+path) for path in d3paths]
        
        return paths
    
    def getMazePathM2(self,sr,sc,dr,dc):
        if sr==dr or sc==dc:
            return []
        if sr==dr-1 and sc == dc-1:
            return [""]
        
        paths = []
        for i in range(1,dc-sc):
            hpaths = self.getMazePathM2(sr,sc+i,dr,dc)
            [paths.append("h"+str(i)+path) for path in  hpaths]
        
        for i in range(1,dr-sr):
            vpaths = self.getMazePathM2(sr+i,sc,dr,dc)
            [paths.append("v"+str(i)+path) for path in  vpaths]

        for i in range(1,dr-sr):
            if i < dc-sc:
                dpaths = self.getMazePathM2(sr+i,sc+i,dr,dc)
                [paths.append("d"+str(i)+path) for path in  dpaths]
        
        return paths
    
n = int(input())
m = int(input())
result = Solution().getMazePathM2(0,0,n,m)
# this code is only to submit on platform
print("[", end ='')
s = ""
for path in result:
     s+=path+", "
s=s.rstrip(s[-1:-3:-1])
print(s+"]" , end='')