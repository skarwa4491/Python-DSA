def solution(arr1, arr2):
    map1 = dict()
    result = []
    for i,num in enumerate(arr2,start=0):
        if map1.get(num , 0):
            map1[num].li.append(i)
        else:
            a = list()
            a.append(i)
            p = pair(a)
            map1[num] = p
    for num in arr1:
        if num in map1.keys():
            result.append(map1[num].li[map1[num].idx])
            map1[num].idx+=1
    print(result)

class pair:
    def __init__(self , li) -> None:
        self.idx = 0
        self.li = li

arr1 = [1,2,3,4,5,2]
arr2 = [4,3,2,1,5,2]
solution(arr1,arr2)