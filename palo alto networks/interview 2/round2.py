def solution():
    map = dict()
    
    with open('/Users/laptop-on-rent-011/Documents/DSA_Pyhton/palo alto networks/interview 2/log.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.split(":")[1]
            line = line.split(" ")
            map[line[-1]] = map.get(line[-1],0)+1
    
    sorted_map = dict(sorted(map.items() , key = lambda a:a[1]))
    print(sorted_map)

solution()