class Solution:
    '''
        Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
        Integers in each row are sorted in ascending from left to right.
        Integers in each column are sorted in ascending from top to bottom.
        leetcode - 240
    '''
    def searchMatrix(self, matrix,target):
        row = 0
        col = len(matrix[0])-1
        
        while row < len(matrix) and col >=0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col-=1
            elif matrix[row][col] < target:
                row+=1
        return False