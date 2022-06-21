import sys
sys.setrecursionlimit(10**6)

class Solution():
    """_summary_
    1. You are given a number n, representing the number of rows.
    2. You are given a number m, representing the number of columns.
    3. You are given n*m numbers, representing elements of 2d array a. The numbers can be 1 or 0 only.
    4. You are standing in the top-left corner and have to reach the bottom-right corner. 
    Only four moves are allowed 't' (1-step up), 'l' (1-step left), 'd' (1-step down) 'r' (1-step right). You can only move to cells which have 0 value in them. You can't move out of the boundaries or in the cells which have value 1 in them (1 means obstacle)
    5. Complete the body of floodfill function - without changing signature - to print all paths that can be used to move from top-left to bottom-right.
    Note1 -> Please check the sample input and output for details
    Note2 -> If all four moves are available make moves in the order 't', 'l', 'd' and 'r'

    """
    
    def floodfill(self ,arr, sr,sc ,dr, dc , boolean_mat ,ans) :
        if(sr<0 or sc<0 or sr>=dr or sc>=dc or arr[sr][sc]==1 or boolean_mat[sr][sc]==True):
            return
        if sr==dr-1 and sc==dc-1:
            print(ans)
            return
        
        boolean_mat[sr][sc]=True
        self.floodfill(arr,sr-1,sc,dr,dc,boolean_mat , ans+"t")
        self.floodfill(arr,sr,sc-1,dr,dc,boolean_mat , ans+"l")
        self.floodfill(arr,sr+1,sc,dr,dc,boolean_mat , ans+"d")
        self.floodfill(arr,sr,sc+1,dr,dc,boolean_mat , ans+"r")
        boolean_mat[sr][sc]=False

n = int(input())
m = int(input())

matrix =[ [int(input()) for _ in range(m)] for _ in range(n) ]

boolean_matrix =[ [False for _ in range(m)]for _ in range(n) ]

Solution().floodfill(arr=matrix,sr=0,sc=0,dr=n,dc=m,boolean_mat=boolean_matrix,ans="")