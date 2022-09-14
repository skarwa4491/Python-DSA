# setu test


# sl1 = 'abcdefghijklmnopqrstuvwxyz'
# list1 = [c for c in sl1]
# list2 = reversed(list1)

# s = 'my name is swapnil'
# words = s.split(' ')
# ans = []
# for word in words:
#     result = ''
#     for w in word:
#         idx = list1.index(w)
#         result+=list2[idx]
#     ans.append(result)

# print(" ".join(ans))

l1 = ['s','w' , 'a' , 'p' , 'n' , 'i' , 'l']
i = 0
j = len(l1)-1

while i < j:
    l1[i] , l1[j] = l1[j],l1[i]
    i+=1
    j-=1
[0,1,2,3,4,5,6,7]

def my_range(end , start=0 ,step=1):
    if not isinstance(end , int) or not isinstance(start , int) or not isinstance(step , int):
        raise ValueError('start and ends are not int')

    if end < start:
        raise Error('')
    itr = start
    while itr < end:
        itr+=step
        