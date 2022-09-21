# def solution():
#     map = dict()    
#     with open('/Users/laptop-on-rent-011/Documents/DSA_Pyhton/tessell/fi.text' , 'r') as file:
#         data_set = file.readlines()
#         for data in range(1, len(data_set)):
#             data_set_row = data_set[data].split(' ')
#             if data_set_row[2] in map.keys():
#                 if int(data_set_row[3]) > int(map[data_set_row[2]][-1]):
#                     map[data_set_row[2]] = data_set_row
#             else:
#                 map[data_set_row[2]] = data_set_row
#     print(map)
            
# solution()

# part-1 - start_time # 3
# part-2 - end of meet # 5
# his already scheduled meets 

schedules = [[10,12],[1,2],[4,5]]

def solution(start , end , schedule):
    schedule.sort(key = lambda a: a[0])
    for i in range(len(schedule)-1):
        current_meet = schedule[i]
        next_meet = schedules[i+1]
        if start >= current_meet[1] and end <= next_meet[0]:
            return True
    return False

print(solution(13,14,schedules))