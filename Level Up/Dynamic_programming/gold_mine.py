def find_max_gold(gold):
    bag = [[0 for col in row]for row in gold]
    for j in range(len(gold[0])-1, -1, -1):
        for i in range(len(gold)-1, -1, -1):
            if j == len(gold[i])-1:
                bag[i][j] = gold[i][j]
            elif i == 0:
                bag[i][j] = gold[i][j] + max(bag[i][j+1], bag[i+1][j+1])
            elif i == len(gold)-1:
                bag[i][j] = gold[i][j] + max(bag[i][j+1], bag[i-1][j+1])
            else:
                bag[i][j] = gold[i][j] + \
                    max(bag[i][j+1], bag[i-1][j+1], bag[i+1][j+1])
    max_ = 0
    for b in bag:
        if b[0] > max_:
            max_ = b[0]
    print(max_)

gold = [[3, 2, 3, 1],
        [2, 4, 6, 0],
        [5, 0, 1, 3],
        [9, 1, 5, 1]]
find_max_gold(gold)
