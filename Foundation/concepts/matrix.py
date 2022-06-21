board = [['.', '.', 'Q', '.'], ['Q', '.', '.', '.'], ['.', '.', '.', 'Q'], ['.', 'Q', '.', '.']]
combo =""
ans =[]
for b in board:
    ans.append("".join(b))
print(ans)
