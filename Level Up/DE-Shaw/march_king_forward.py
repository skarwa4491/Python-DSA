def solution(board, sr, sc, dr, dc):
    if sc == dc and sr == 1:
        return 1
    if sr == 0 or sc == 0 or sc > board:
        return 0

    count1 = solution(board,sr-1, sc-1, dr, dc)
    count2 = solution(board,sr-1, sc, dr, dc)
    count3 = solution(board, sr-1, sc + 1, dr, dc)
    
    return count1+count2+count3

size = 4
print(solution(size, size, (size//2)+1, 1, (size//2)+1))
