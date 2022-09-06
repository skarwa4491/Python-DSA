def find_elements_with_odd_number_of_occurrences():
    # Write your code here
    # for a given array find elements with odd number of occurances
    n = int(input())
    arr =[]
    for _ in range(n):
        arr.append(int(input()))
    map ={}
    print(arr)
    for num in arr:
        if map.get(num):
            map.update({num:map.get(num)+1})
        else:
            map.update({num:1})
    for key,val in map.items():
        if val%2==0:
            print(key)
            
    

if __name__ == '__main__':
    find_elements_with_odd_number_of_occurrences()
