from queue import PriorityQueue

def solution(arr,k):
    queue = PriorityQueue()
    for num in arr:
        if queue.qsize() < k:
            queue.put(num)
        else:
            min = queue.get()
            if num > min:
                queue.put(num)
            else:
                queue.put(min)
    print(queue.get())

solution([2,10,5,17,7,18,6,4],3)

