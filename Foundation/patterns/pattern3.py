n = int(input())
nsp = n-1
nst = 1
for i in range(n):
    for j in range(nsp):
        print("\t",end="")
    
    for k in range(nst):
        print("*"+"\t",end="")
    print()
    nsp-=1
    nst+=1
    