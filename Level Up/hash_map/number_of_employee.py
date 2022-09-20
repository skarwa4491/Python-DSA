'''
    1. You are given number N and 2*N number of strings that contains mapping of the employee and his manager.
    2. An employee directly reports to only one manager. 
    3. All managers are employees but the reverse is not true.
    4. An employee reporting to himself is the CEO of the company.
    5. You have to find the number of employees under each manager in the hierarchy not just their direct reports.
    
    Solution :
    1. contruct a map  of key -> manager and value as set of employes
    2. 
'''
def find_managers(struct):
    def get_size(tree, mgr, result):
        if mgr not in tree.keys():
            result[mgr] = 0
            return 1
        size = 0
        children = tree[mgr]
        for child in children:
            cz = get_size(tree, child, result)
            size += cz
        result[mgr] = size
        return size+1

    emp_map = {}
    ceo = None
    for pair in struct:
        if pair[0] == pair[1]:
            ceo = pair[0]
        elif pair[1] in emp_map.keys():
            emp_map[pair[1]].add(pair[0])
        else:
            reporties = set()
            reporties.add(pair[0])
            emp_map[pair[1]] = reporties
    result = dict()
    get_size(emp_map, ceo, result)
    print(result, '---> ceo ---->',ceo)


struct = [['A', 'C'],
          ['B', 'C'],
          ['C', 'F'],
          ['D', 'E'],
          ['E', 'F'],
          ['F', 'F']]

find_managers(struct)
