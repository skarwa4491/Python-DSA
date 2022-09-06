from queue import PriorityQueue

def solution(arr,k):
    pq = PriorityQueue()
    
    for i in range(0,k+1):
        pq.put(arr[i])
        
    for i in range(k+1,len(arr)):
        print(pq.get() , end="\t")
        pq.put(arr[i])

    while not pq.empty():
        print(pq.get(), end="\t")


solution([2,3,1,4,6,7,5,8,9], 2)