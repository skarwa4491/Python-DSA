from tracemalloc import start


s = "abcefg"
ss = "pqrst"
i=0
j=0
for (i ,c1),(j ,c2) in zip(enumerate(s,start=-1),enumerate(ss,start=-len(ss)-1)): 
    print(i,"-->",c1 , j,"-->",c2)