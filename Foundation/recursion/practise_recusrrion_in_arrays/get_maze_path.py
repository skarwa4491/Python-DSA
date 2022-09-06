def solution(sr, sc, dr, dc, result):
    if sr == dr and sc == dc:
        return ['']
    if sr > dr or sc > dc:
        return []

    paths = []
    vertical = solution(sr+1, sc, dr, dc, result)
    horizontal = solution(sr, sc+1, dr, dc, result)
    [paths.append('v'+_) for _ in vertical]
    [paths.append('h'+_) for _ in horizontal]
    return paths

print(solution(1,1,2,2,[]))
