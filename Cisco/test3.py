# num = 32
# num2 = 33
# num1 = 32

# print('address num1',id(num1))
# print('address num',id(num))
# print('address num2',id(num2))

# num+=2

# print('address of num after change',id(num))

li = [3,4,5,1,2]

ans = [i for i in li if i%2==0]

print(ans)

map = { i : i*i for i in li}
print(map)