from itertools import permutations
l=[1,2,3,4,5,6,7,8,9]
perm = permutations(l,4)
li=[]
for i in list(perm):
    s=""
    for j in i:
        s=s+str(j)
    li.append(s)
for i in li:
    t = 2*int(i)
    
    ts = str(t)
    st = i+ts
    if("1" in st and "2" in st and "3" in st and "4" in st and "5" in st and "6" in st and "7" in st and "8" in st and "9" in st):
        print(st)