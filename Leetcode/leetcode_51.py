class Solution():
    def solveNQueens(self,n):   
        board = [["." for _ in range(n)] for _ in range(n)]
        ans =[]
        all_ans=[]
        self.nqueens(board,0,ans,all_ans)
        return all_ans
        
    def nqueens(self , board , row , ans , all_ans):
        if row == len(board):
            for row in board:
                ans.append("".join(row))
            all_ans.append(ans)
            ans = []
            return
        
        for col in range(len(board)):
            if(self.isQueenSafe(board,row,col)):
                board[row][col]="Q"
                self.nqueens(board, row+1 , ans , all_ans)
                board[row][col]="."
                ans = []
    
    def isQueenSafe(self,board,row,col)->bool:
        i=row
        j=col
        # check above rows if queen is present
        while i>=0 :
            if board[i][j]=="Q":
                return False
            i-=1
        i = row-1
        j = col-1
        while j>=0 and i>=0 :
            if board[i][j]=="Q":
                return False
            i-=1
            j-=1
            
        i = row-1
        j = col+1
        while j<len(board) and i>=0 :
            if board[i][j]=="Q":
                return False
            i-=1
            j+=1
        return True
        

n=int(input())
print(Solution().solveNQueens(n))