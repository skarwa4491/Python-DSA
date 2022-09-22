from time import process_time_ns


mylist = ["apple", "banana", "cherry", "apple", "cherry"]

print(len(mylist)) # length of list
print(type(mylist))
print(isinstance(mylist,list))
mylist.append('mango') # add to last of list
mylist.insert(1,'lemons') # add at index 1

print(mylist)

l1 = [1,2,3]
l2 = [4,5,6]
tup = (1,2,3,)
print(l1+l2) # adds only list
l1.extend(l2) # adds any collection to list
l1.extend(tup)
print(l1)


l1.remove(1) # removes specific item
print(l1)
l1.pop(1) # remove indexed item , else pops last item