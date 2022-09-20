import random

arr = [1,2,3,4,5]


def suffle(a):
    idx1 = random.randint(0 , len(a)-1)
    idx2 = random.randint(0 , len(a)-1)
    a[idx1],a[idx2] = a[idx2],a[idx1]
    return a

print(suffle(arr))