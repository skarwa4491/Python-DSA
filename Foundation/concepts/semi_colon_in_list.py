li =[1,2,3]
li2=li # here two refrence point to same object
li3=li[:] # this creates a new object if li and assign to li3
print(id(li) , id(li2) , id(li3) , id(li[:]))
li[:]=li2
print(id(li) , id(li2) , id(li3) , id(li[:]))
li[:]=li3 # this replaces all item of li with li3