s = 'my name is swapnil, I work for treebo'

# s_arr = s.split(" ")
# hash_map = dict()

# for word in s_arr:
#     for w in word:
#         hash_map[w] = hash_map.get(w,0)+1

# print(hash_map)

words = s.split(' ')

i = 0
j = len(words)-1
while i < j:
    words[i],words[j] = words[j],words[i] # swapping values
    i+=1
    j-=1
print(' '.join(words))
