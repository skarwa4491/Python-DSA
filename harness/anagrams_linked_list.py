def solution(l1, l2):
    map = dict()
    node = l1
    while node is not None:
        ch = node.data
        if ch in map.keys():
            map[ch] += 1
        else:
            map[ch]=1
        node= node.next
    node = l2
    while node is not None:
        ch = node.data
        if ch in map.keys():
            map[ch]-=1
            if map[ch] == 0:
                map.pop(ch)
        else:
            return False
        node=node.next
    if len(map) > 0:
        return False
    else:
        return True
    
l1 = 'S -> W -> A -> P -> N -> I -> L->S'
l2 = 'S -> S -> W -> A -> P -> N -> I -> L'
solution(l1,l2)
