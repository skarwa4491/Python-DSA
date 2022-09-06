def solution(arr):
    map = {num: True for num in arr}
    for num in arr:
        if num-1 in map.keys():
            map[num] = False
    max_len = 0
    max_sp = 0  # max start point
    for num in arr:
        if map[num]:
            tl = 1  # temp length
            tsp = num  # temp start point
            while tsp+tl in map.keys():
                tl += 1
            if tl > max_len:
                max_len = tl
                max_sp = tsp
    result = []
    for i in range(max_sp, max_sp+max_len):
        result.append(i)
    print(result)

solution([10, 5, 9, 1, 11, 8, 6, 15, 3, 12, 2])
