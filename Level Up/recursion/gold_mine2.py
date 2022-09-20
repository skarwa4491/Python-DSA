'''
1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers, representing elements of 2d array a, which represents a gold mine.
4. You are allowed to take one step left, right, up or down from your current position.
5. You can't visit a cell with 0 gold and the same cell more than once. 
6. Each cell has a value that is the amount of gold available in the cell.
7. You are required to identify the maximum amount of gold that can be dug out from the mine if 
     you start and stop collecting gold from any position in the grid that has some gold.

'''


def solution(matrix, row, col, bag, is_visited):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[row]) or matrix[row][col] == 0 or is_visited[row][col] == True:
        return

    is_visited[row][col] = True
    bag.append(matrix[row][col])
    solution(matrix, row-1, col, bag, is_visited)
    solution(matrix, row, col + 1, bag, is_visited)
    solution(matrix, row+1, col, bag, is_visited)
    solution(matrix, row, col - 1, bag, is_visited)


matrix = [
    [0, 1, 4, 2, 8, 2],
    [4, 3, 6, 5, 0, 4],
    [1, 2, 4, 1, 4, 6],
    [2, 0, 7, 3, 2, 2],
    [3, 1, 5, 9, 2, 4],
    [2, 7, 0, 8, 5, 1]
]


_max = 0
is_visited = [[False for col in row] for row in matrix]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != 0 and is_visited[i][j] == False:
            collected_gold = list()
            solution(matrix, i, j, collected_gold, is_visited)
            total_gold = sum(collected_gold)
            if total_gold > _max:
                _max = total_gold

print(_max)
