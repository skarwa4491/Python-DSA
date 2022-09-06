from queue import PriorityQueue
import queue
# heap priority queue


def solution(arr, k):
    q = PriorityQueue()
    i = 0
    while i < len(arr) and  q.qsize() < k:
        if q.empty() or arr[i] not in q.queue:
            q.put(arr[i])
        i += 1
    i = 0
    for i in range(k, len(arr)):
        item = q.get()
        if arr[i] > item and arr[i] not in q.queue:
            q.put(arr[i])
        else:
            q.put(item)
    print(q.get())


arr = [10, 10, 9, 9, 15, 15, 33, -1]
k = 3
solution(arr, k)
