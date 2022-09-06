def solution(n, result):
    if n < 0:
        return []

    if n == 0:
        return ['']

    paths = []
    one_step = solution(n-1, result)
    two_step = solution(n-2, result)
    three_step = solution(n-3, result)
    [paths.append('1'+step)for step in one_step]
    [paths.append('2'+step)for step in two_step]
    [paths.append('2'+step)for step in three_step]
    return paths


print(solution(3, []))
