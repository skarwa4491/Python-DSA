def pair_up(nums, k):
    map = dict()
    for num in nums:
        reminder = num % k
        frequency = map.get(reminder, 0)
        if frequency == 0:
            map[reminder] = 1
        else:
            map[reminder] += 1
    result = False
    for num in nums:
        reminder = num % k
        if reminder == 0 and map[reminder] % 2 == 0:
            result = True
        elif 2*reminder == k and map[reminder] % 2 == 0:
            result = True
        else:
            if (k-reminder) not in map.keys():
                return False
            if map[reminder] == map[k-reminder]:
                result = True
            else:
                return False
    print(map)
    return result


arr = [9, 7, 5, 3]
print(pair_up(arr, 6))
